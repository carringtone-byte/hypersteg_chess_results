#!/usr/bin/env python3
"""Render the generated Mermaid approach map as a standalone interactive HTML graph."""
from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path


NODE_RE = re.compile(
    r'^\s*(\w+)\s*(?:\["(.*?)"\]|\("(.*?)"\)|\{\{"(.*?)"\}\}|\(\["(.*?)"\]\))\s*$'
)
SUBGRAPH_RE = re.compile(r'^\s*subgraph\s+(\w+)\["(.*?)"\]\s*$')
EDGE_RE = re.compile(r'^\s*(\w+)\s+([-.=o<>]+)(?:\|([^|]+)\|)?\s+(\w+)\s*$')


def extract_graph(source: str) -> dict:
    match = re.search(r"```mermaid\s*\n(.*?)\n```", source, re.S)
    if not match:
        raise ValueError("No Mermaid graph found in approach_map.md")
    nodes: dict[str, dict] = {}
    edges: list[dict] = []
    family = ""
    for line in match.group(1).splitlines():
        sub = SUBGRAPH_RE.match(line)
        if sub:
            family = sub.group(1)[:-2] if sub.group(1).endswith("_g") else sub.group(1)
            label = re.sub(r"\s+\(\d+\)$", "", sub.group(2))
            node_type = "stub" if family == "other_families" else "family"
            nodes.setdefault(family, {"id": family, "label": label, "type": node_type, "family": label if node_type == "family" else ""})
            continue
        if line.strip() == "end":
            family = ""
            continue
        edge = EDGE_RE.match(line)
        if edge:
            source_id, arrow, relation, target_id = edge.groups()
            edges.append({"source": source_id, "target": target_id,
                          "relation": relation or "taxonomy", "arrow": arrow})
            continue
        node = NODE_RE.match(line)
        if node:
            node_id = node.group(1)
            label = next((value for value in node.groups()[1:] if value is not None), "")
            if node_id == "other_families":
                node_type, node_family = "stub", ""
            elif node_id.startswith("fam_"):
                node_type = "family"
                label = re.sub(r":\s*\d+\s+direct$", "", label)
                node_family = label
            elif node_id.startswith("cls_"):
                node_type, node_family = "mechanism class", ""
            elif node_id.startswith("mech_"):
                node_type, node_family = "mechanism", ""
            elif node_id.startswith("tech_"):
                node_type = "technique"
                node_family = nodes.get(family, {}).get("label", family)
            elif node_id.startswith("paper_"):
                node_type = "paper"
                node_family = ""
            else:
                node_type = "approach"
                node_family = nodes.get(family, {}).get("label", family)
            nodes[node_id] = {"id": node_id, "label": label, "type": node_type,
                              "family": node_family}
    known = set(nodes)
    edges = [edge for edge in edges if edge["source"] in known and edge["target"] in known]
    return {"nodes": list(nodes.values()), "edges": edges}


def full_graph(maps_dir: Path) -> dict:
    """Combine the family/technique overview with each family's approach map."""
    overview = extract_graph((maps_dir / "approach_map.md").read_text(encoding="utf-8"))
    nodes = {node["id"]: node for node in overview["nodes"]}
    edges = {(e["source"], e["target"], e["relation"], e["arrow"]): e for e in overview["edges"]}
    for path in sorted(maps_dir.glob("approach_map_*.md")):
        if re.search(r"_\d{8}\.md$", path.name):
            continue
        graph = extract_graph(path.read_text(encoding="utf-8"))
        for node in graph["nodes"]:
            if node["id"] not in nodes or nodes[node["id"]]["type"] == "family" and node["type"] != "family":
                nodes[node["id"]] = node
        for edge in graph["edges"]:
            edges[(edge["source"], edge["target"], edge["relation"], edge["arrow"])] = edge
    return {"nodes": list(nodes.values()), "edges": list(edges.values())}


HTML_TEMPLATE = r'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Hypersteg Approach Network</title>
<style>
:root{color-scheme:light;--ink:#17212b;--muted:#5b6875;--line:#d5dde5;--panel:#f6f8fa;--blue:#277da1;--gold:#f9c74f;--green:#43aa8b;--red:#d1495b;--purple:#8064a2}
*{box-sizing:border-box}body{margin:0;font:14px/1.45 system-ui,Segoe UI,Arial,sans-serif;color:var(--ink);background:#fff}
header{padding:14px 18px;border-bottom:1px solid var(--line);display:flex;align-items:center;gap:18px;flex-wrap:wrap}h1{font-size:20px;margin:0}header p{margin:0;color:var(--muted)}
#layout{display:grid;grid-template-columns:minmax(0,1fr) 320px;height:calc(100vh - 66px);min-height:520px}#graph-wrap{position:relative;overflow:hidden;background:radial-gradient(#e6ebf0 .65px,transparent .65px);background-size:18px 18px}canvas{display:block;width:100%;height:100%;cursor:grab}canvas.dragging{cursor:grabbing}
aside{border-left:1px solid var(--line);padding:14px;overflow:auto;background:var(--panel)}.controls{display:grid;gap:10px;margin-bottom:14px}input,select,button{font:inherit;padding:8px 9px;border:1px solid #bdc7d1;border-radius:5px;background:white;color:var(--ink)}button{cursor:pointer}button:hover{background:#edf3f7}.row{display:flex;gap:6px}.row button{flex:1}.checks{display:grid;grid-template-columns:1fr 1fr;gap:5px 10px;color:#354250}.checks label{white-space:nowrap}.counts{color:var(--muted);font-size:12px}
#detail{border-top:1px solid var(--line);padding-top:12px}#detail h2{font-size:16px;margin:0 0 6px}#detail .kind{font-size:12px;color:var(--muted);margin-bottom:8px}#detail p{margin:6px 0;overflow-wrap:anywhere}.legend{display:grid;grid-template-columns:1fr 1fr;gap:6px;color:#354250;font-size:12px;margin:12px 0}.dot{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:6px}
.help{font-size:12px;color:var(--muted)}.tooltip{position:absolute;display:none;pointer-events:none;background:#17212b;color:white;padding:5px 8px;border-radius:4px;font-size:12px;max-width:300px;z-index:2}
@media(max-width:850px){#layout{grid-template-columns:1fr;height:auto;min-height:0}#graph-wrap{height:65vh;min-height:420px}aside{border-left:0;border-top:1px solid var(--line)}}
</style>
</head>
<body>
<header><h1>Hypersteg Approach Network</h1><p>Published approaches grouped by family and technique; labeled links show taxonomy or paper-stated relations.</p></header>
<div id="layout"><main id="graph-wrap"><canvas id="graph"></canvas><div id="tooltip" class="tooltip"></div></main>
<aside>
<div class="controls">
<input id="search" type="search" placeholder="Find an approach or technique…" aria-label="Search nodes">
<select id="family"><option value="">All families</option></select>
<div class="checks"><label><input type="checkbox" data-type="family" checked> Families</label><label><input type="checkbox" data-type="technique" checked> Techniques</label><label><input type="checkbox" data-type="approach" checked> Approaches</label><label><input type="checkbox" data-type="paper" checked> Papers</label><label><input type="checkbox" data-type="mechanism" checked> Mechanisms</label><label><input type="checkbox" data-type="mechanism class" checked> Mechanism classes</label></div>
<div class="row"><button id="fit">Fit graph</button><button id="reset">Reset</button></div>
<div class="counts" id="counts"></div>
</div>
<div class="legend"><span><i class="dot" style="background:#277da1"></i>Family</span><span><i class="dot" style="background:#f9c74f"></i>Technique</span><span><i class="dot" style="background:#43aa8b"></i>Approach</span><span><i class="dot" style="background:#8064a2"></i>Paper</span><span><i class="dot" style="background:#d1495b"></i>Mechanism</span><span><i class="dot" style="background:#f08a5d"></i>Mechanism class</span></div>
<div id="detail"><h2>Explore the network</h2><p>Search or click a node to inspect its neighbors. Drag nodes to rearrange; drag the background to pan; use the mouse wheel or pinch to zoom. Clicking a relation highlights connected nodes.</p></div>
<p class="help">The map is derived from the kit's taxonomy, feature table, and verified claim records. Taxonomy links group material; colored directional links record paper relations such as refines, rebuts, or depends-on.</p>
</aside></div>
<script id="graph-data" type="application/json">__DATA__</script>
<script>
const DATA=JSON.parse(document.getElementById('graph-data').textContent), canvas=document.getElementById('graph'),ctx=canvas.getContext('2d'),wrap=document.getElementById('graph-wrap'),tip=document.getElementById('tooltip');
const COLORS={family:'#277da1',technique:'#f9c74f',approach:'#43aa8b',paper:'#8064a2',mechanism:'#d1495b','mechanism class':'#f08a5d',stub:'#9aa5b1'};
const REL={taxonomy:'#aeb8c2',Supports:'#2e7d32',Rebuts:'#c62828','Depends-on':'#6a1b9a',Refines:'#1565c0',Qualifies:'#ef6c00',Restates:'#00838f','Duplicate-of':'#757575',Supersedes:'#4e342e'};
const nodes=DATA.nodes.map(n=>({...n,x:0,y:0,vx:0,vy:0,r:n.type==='family'?13:n.type==='technique'?8:n.type==='paper'?8:5}));
const byId=new Map(nodes.map(n=>[n.id,n]));
const edges=DATA.edges.map(e=>({...e,a:byId.get(e.source),b:byId.get(e.target)})).filter(e=>e.a&&e.b);
const families=[...new Set(nodes.map(n=>n.family).filter(Boolean))].sort();const familySel=document.getElementById('family');
for(const f of families){const o=document.createElement('option');o.value=f;o.textContent=f;familySel.append(o)}
const cx=()=>canvas.clientWidth/2,cy=()=>canvas.clientHeight/2;let scale=1,offset={x:0,y:0},selected=null,hover=null,drag=null,panning=null,filterText='',filterFamily='',enabled=new Set(['family','technique','approach','paper','mechanism','mechanism class']);
function initPositions(){const unit=Math.min(canvas.clientWidth,canvas.clientHeight),famNodes=nodes.filter(n=>n.type==='family');famNodes.forEach((f,i)=>{const a=2*Math.PI*i/famNodes.length-Math.PI/2;f.x=Math.cos(a)*unit*.31;f.y=Math.sin(a)*unit*.31});
  for(const f of famNodes){const members=nodes.filter(n=>n.family===f.label&&n!==f);members.forEach((n,i)=>{const a=2*Math.PI*i/Math.max(1,members.length)+Math.atan2(f.y,f.x);const rad=n.type==='approach'?78:n.type==='paper'?125:42;n.x=f.x+Math.cos(a)*rad;n.y=f.y+Math.sin(a)*rad})}
  const classes=nodes.filter(n=>n.type==='mechanism class');classes.forEach((n,i)=>{const a=2*Math.PI*i/Math.max(1,classes.length)-Math.PI/2;n.x=Math.cos(a)*unit*.13;n.y=Math.sin(a)*unit*.13});
  const membersByClass=new Map(classes.map(c=>[c.id,[]]));for(const e of edges){if(e.a.type==='mechanism class'&&e.b.type==='mechanism')membersByClass.get(e.a.id).push(e.b);if(e.b.type==='mechanism class'&&e.a.type==='mechanism')membersByClass.get(e.b.id).push(e.a)}
  for(const c of classes){const ms=[...new Set(membersByClass.get(c.id))];ms.forEach((n,i)=>{const a=2*Math.PI*i/Math.max(1,ms.length)-Math.PI/2;n.x=c.x+Math.cos(a)*(48+Math.floor(i/8)*30);n.y=c.y+Math.sin(a)*(48+Math.floor(i/8)*30)})}
  const unplaced=nodes.filter(n=>n.type==='mechanism'&&n.x===0&&n.y===0);unplaced.forEach((n,i)=>{const a=2*Math.PI*i/Math.max(1,unplaced.length);n.x=Math.cos(a)*unit*.27;n.y=Math.sin(a)*unit*.27});
  const papers=nodes.filter(n=>n.type==='paper');papers.forEach((n,i)=>{const ns=edges.filter(e=>e.a===n||e.b===n).map(e=>e.a===n?e.b:e.a).filter(x=>x.x||x.y);if(ns.length){n.x=ns.reduce((s,x)=>s+x.x,0)/ns.length+(i%2?26:-26);n.y=ns.reduce((s,x)=>s+x.y,0)/ns.length+(i%3-1)*25}else{const a=2*Math.PI*i/Math.max(1,papers.length);n.x=Math.cos(a)*unit*.2;n.y=Math.sin(a)*unit*.2}});
  const stubs=nodes.filter(n=>n.type==='stub');stubs.forEach((n,i)=>{n.x=-unit*.22;n.y=i*24});fitGraph();}
function resize(){const dpr=window.devicePixelRatio||1;canvas.width=canvas.clientWidth*dpr;canvas.height=canvas.clientHeight*dpr;ctx.setTransform(dpr,0,0,dpr,0,0);if(nodes.every(n=>n.x===0&&n.y===0))initPositions();draw()}
function world(p){return{x:(p.x-cx()-offset.x)/scale,y:(p.y-cy()-offset.y)/scale}}
function screen(n){return{x:cx()+offset.x+n.x*scale,y:cy()+offset.y+n.y*scale}}
function matchFilter(n){return enabled.has(n.type)&&(!filterFamily||n.family===filterFamily||n.label===filterFamily)&&(!filterText||(`${n.label} ${n.id} ${n.family}`).toLowerCase().includes(filterText))}
function neighbors(id){const s=new Set([id]);for(const e of edges)if(e.a.id===id)s.add(e.b.id);else if(e.b.id===id)s.add(e.a.id);return s}
function draw(){ctx.clearRect(0,0,canvas.clientWidth,canvas.clientHeight);const focus=selected?neighbors(selected.id):null;
  for(const e of edges){const a=screen(e.a),b=screen(e.b),active=(!selected||focus.has(e.a.id)&&focus.has(e.b.id)),alpha=active?1:.09;ctx.globalAlpha=alpha;ctx.strokeStyle=REL[e.relation]||'#aeb8c2';ctx.lineWidth=(e.relation==='taxonomy'?1:2)*Math.min(1.5,scale);ctx.beginPath();ctx.moveTo(a.x,a.y);ctx.lineTo(b.x,b.y);ctx.stroke();if(e.relation!=='taxonomy'){const ang=Math.atan2(b.y-a.y,b.x-a.x),len=7;ctx.fillStyle=ctx.strokeStyle;ctx.beginPath();ctx.moveTo(b.x,b.y);ctx.lineTo(b.x-len*Math.cos(ang-.42),b.y-len*Math.sin(ang-.42));ctx.lineTo(b.x-len*Math.cos(ang+.42),b.y-len*Math.sin(ang+.42));ctx.closePath();ctx.fill()}}
  ctx.globalAlpha=1;
  for(const n of nodes){const p=screen(n),visible=matchFilter(n),focusNode=!selected||focus.has(n.id);ctx.globalAlpha=visible?(focusNode?1:.18):.035;ctx.fillStyle=COLORS[n.type];ctx.beginPath();ctx.arc(p.x,p.y,Math.max(2,n.r*scale),0,Math.PI*2);ctx.fill();if(n===selected||n===hover){ctx.strokeStyle='#17212b';ctx.lineWidth=2;ctx.stroke()}if(scale>.75&&(n.type==='family'||n===selected||n===hover)){ctx.font=`${n.type==='family'?12:11}px system-ui`;ctx.fillStyle='#17212b';ctx.fillText(n.label,p.x+n.r*scale+4,p.y+4)}}ctx.globalAlpha=1;
  const visible=nodes.filter(matchFilter).length;document.getElementById('counts').textContent=`${visible} of ${nodes.length} nodes · ${edges.length} links`;
}
function fitGraph(){const xs=nodes.map(n=>n.x),ys=nodes.map(n=>n.y),w=Math.max(...xs)-Math.min(...xs)+180,h=Math.max(...ys)-Math.min(...ys)+180;scale=Math.min((canvas.clientWidth-50)/w,(canvas.clientHeight-50)/h,1.3);offset={x:-(Math.min(...xs)+Math.max(...xs))/2*scale,y:-(Math.min(...ys)+Math.max(...ys))/2*scale};draw()}
function showDetail(n){selected=n;const adjacent=edges.filter(e=>e.a===n||e.b===n);let relations=adjacent.map(e=>{const other=e.a===n?e.b:e.a;return `<li><b>${escapeHtml(e.relation)}</b> → ${escapeHtml(other.label)} <small>(${escapeHtml(other.type)})</small></li>`}).join('');document.getElementById('detail').innerHTML=`<h2>${escapeHtml(n.label)}</h2><div class="kind">${escapeHtml(n.type)}${n.family?` · ${escapeHtml(n.family)}`:''}</div><p><code>${escapeHtml(n.id)}</code></p>${relations?`<p>Connected nodes</p><ul>${relations}</ul>`:'<p>No direct links in the rendered map.</p>'}`;draw()}
function escapeHtml(s){return String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function nearest(pos){let best=null,dist=Infinity;for(const n of nodes){if(!matchFilter(n))continue;const p=screen(n),d=Math.hypot(p.x-pos.x,p.y-pos.y);if(d<dist&&d<Math.max(9,n.r*scale+5)){best=n;dist=d}}return best}
canvas.addEventListener('pointerdown',e=>{canvas.setPointerCapture(e.pointerId);const p={x:e.offsetX,y:e.offsetY},n=nearest(p);if(n){drag=n;canvas.classList.add('dragging')}else panning={x:p.x,y:p.y,ox:offset.x,oy:offset.y}});
canvas.addEventListener('pointermove',e=>{const p={x:e.offsetX,y:e.offsetY};if(drag){const q=world(p);drag.x=q.x;drag.y=q.y;draw()}else if(panning){offset.x=panning.ox+p.x-panning.x;offset.y=panning.oy+p.y-panning.y;draw()}else{hover=nearest(p);if(hover){tip.style.display='block';tip.style.left=(p.x+12)+'px';tip.style.top=(p.y+12)+'px';tip.textContent=hover.label}else tip.style.display='none';draw()}});
canvas.addEventListener('pointerup',e=>{if(drag){const n=drag;drag=null;canvas.classList.remove('dragging');if(Math.hypot(e.offsetX-(screen(n).x),e.offsetY-screen(n).y)<4)showDetail(n)}panning=null});
canvas.addEventListener('wheel',e=>{e.preventDefault();const before=world({x:e.offsetX,y:e.offsetY});scale=Math.max(.12,Math.min(4,scale*(e.deltaY<0?1.12:.89)));offset.x=e.offsetX-cx()-before.x*scale;offset.y=e.offsetY-cy()-before.y*scale;draw()},{passive:false});
document.getElementById('search').addEventListener('input',e=>{filterText=e.target.value.trim().toLowerCase();if(filterText){const n=nodes.find(n=>matchFilter(n));if(n)showDetail(n)}draw()});familySel.addEventListener('change',e=>{filterFamily=e.target.value;draw()});document.querySelectorAll('[data-type]').forEach(x=>x.addEventListener('change',()=>{x.checked?enabled.add(x.dataset.type):enabled.delete(x.dataset.type);draw()}));document.getElementById('fit').onclick=fitGraph;document.getElementById('reset').onclick=()=>{filterText='';filterFamily='';document.getElementById('search').value='';familySel.value='';enabled=new Set(['family','technique','approach','paper','mechanism','mechanism class']);document.querySelectorAll('[data-type]').forEach(x=>x.checked=true);selected=null;initPositions()};
window.addEventListener('resize',resize);resize();
</script>
</body>
</html>'''


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument("--source", type=Path)
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()
    source_path = args.source or args.root / "maps" / "approach_map.md"
    out_path = args.out or args.root / "maps" / "approach_network.html"
    graph = full_graph(source_path.parent) if source_path.name == "approach_map.md" else extract_graph(source_path.read_text(encoding="utf-8"))
    payload = json.dumps(graph, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(HTML_TEMPLATE.replace("__DATA__", payload), encoding="utf-8")
    counts = {kind: sum(node["type"] == kind for node in graph["nodes"])
              for kind in ("family", "technique", "approach", "paper", "mechanism class", "mechanism")}
    print(f"Wrote {out_path}: {len(graph['nodes'])} nodes {counts}; {len(graph['edges'])} links")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
