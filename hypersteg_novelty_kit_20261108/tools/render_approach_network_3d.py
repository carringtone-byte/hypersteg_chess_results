#!/usr/bin/env python3
"""Build a small, dependency-free 3D canvas view of the approach map."""
from __future__ import annotations

import argparse
import json
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render_approach_network import full_graph  # noqa: E402


PAGE = r'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Hypersteg Approach Map · 3D</title>
<style>
:root{color-scheme:dark;--bg:#151515;--panel:#202020;--line:#393939;--text:#f3f3f3;--muted:#a8a8a8;--red:#c9232d;--red2:#e02d38}
*{box-sizing:border-box}html,body{height:100%;margin:0;background:var(--bg);color:var(--text);font:14px/1.4 Inter,Segoe UI,system-ui,sans-serif;overflow:hidden}
#scene{position:fixed;inset:0;background:radial-gradient(ellipse at 52% 50%,#252525 0,#1b1b1b 46%,#141414 82%)}canvas{width:100%;height:100%;display:block;cursor:grab}canvas.drag{cursor:grabbing}
.top{position:fixed;top:18px;left:20px;right:20px;display:flex;align-items:center;justify-content:space-between;gap:18px;pointer-events:none}.brand{pointer-events:auto;display:flex;align-items:center;gap:13px}.brand h1{font-size:17px;font-weight:600;letter-spacing:.01em;margin:0 0 3px}.brand p{margin:0;color:var(--muted);font-size:11px}.logo{display:block;width:142px;height:62px;padding:3px 7px;object-fit:contain;background:#fbfcfd;border-radius:6px}
.toolbar{pointer-events:auto;display:flex;gap:8px;align-items:center;flex-wrap:wrap;justify-content:flex-end}.toolbar input,.toolbar select,.toolbar button{border:1px solid #414141;background:rgba(34,34,34,.96);color:var(--text);border-radius:7px;padding:9px 11px;font:inherit;outline:none}.toolbar input{width:220px}.toolbar input::placeholder{color:#929292}.toolbar input:focus,.toolbar select:focus{border-color:var(--red)}.toolbar select{max-width:210px}.toolbar button{cursor:pointer;border-color:var(--red);background:var(--red);font-weight:600}.toolbar button:hover{background:var(--red2);border-color:var(--red2)}
.card{position:fixed;left:20px;bottom:20px;max-width:min(460px,calc(100vw - 40px));padding:13px 15px;border:1px solid #3c3c3c;border-left:3px solid var(--red);border-radius:7px;background:rgba(31,31,31,.95);backdrop-filter:blur(8px);box-shadow:0 12px 32px #0007}.card h2{font-size:14px;font-weight:600;margin:0 0 4px}.card p{margin:3px 0;color:var(--muted);font-size:12px;overflow-wrap:anywhere}.pill{display:inline-block;border:1px solid #494949;border-radius:4px;padding:3px 8px;margin:4px 5px 0 0;color:#e5e5e5;font-size:11px}
.help{position:fixed;right:20px;bottom:20px;color:#aaa;font-size:11px;text-align:right;line-height:1.7}.key{display:inline-block;border:1px solid #484848;border-radius:4px;padding:0 5px;color:#e0e0e0;background:#252525}
.legend{position:fixed;top:95px;left:20px;display:flex;gap:13px;flex-wrap:wrap;color:#c0c0c0;font-size:11px;max-width:500px}.legend span{white-space:nowrap}.swatch{width:8px;height:8px;display:inline-block;border-radius:50%;margin-right:5px;box-shadow:0 0 8px currentColor}
@media(max-width:760px){.top{left:12px;right:12px;top:10px;display:block}.brand{gap:9px}.logo{width:103px;height:45px}.toolbar{justify-content:flex-start;margin-top:10px}.toolbar input{width:min(48vw,220px)}.legend{top:110px;left:12px;max-width:75vw}.card{left:12px;bottom:12px}.help{right:12px;bottom:12px;max-width:34vw}.brand p{max-width:70vw}}
</style></head><body>
<main id="scene"><canvas id="network" aria-label="Interactive 3D approach network"></canvas></main>
<header class="top"><div class="brand"><img class="logo" src="haki_logo.png" alt="Haki"><div><h1>Approach Network + Agent Schemes</h1><p>19 AGENT-DEVELOPED additions / 165 mechanisms / 195 published approaches</p></div></div>
<div class="toolbar"><input id="search" type="search" placeholder="Search approaches or techniques…" aria-label="Search">
<select id="family"><option value="">All families</option></select><button id="home">Reset view</button></div></header>
<div class="legend"><span><i class="swatch" style="background:#c9232d;color:#c9232d"></i>Mechanism class</span><span><i class="swatch" style="background:#f3f3f3;color:#f3f3f3"></i>Mechanism</span><span><i class="swatch" style="background:#db5961;color:#db5961"></i>Published approach</span><span><i class="swatch" style="background:#fff;color:#fff"></i>Family</span><span><i class="swatch" style="background:#e02d38;color:#e02d38"></i>Uses mechanism</span><span><i class="swatch" style="background:#ffb454;color:#ffb454"></i>AGENT-DEVELOPED / new additions</span></div>
<section class="card" id="info"><h2>Explore the map</h2><p>Drag to rotate · scroll to zoom · click a node to inspect its connections.</p></section>
<div class="help"><span class="key">drag</span> rotate &nbsp; <span class="key">scroll</span> zoom<br>Click a node to see its links</div>
<script id="data" type="application/json">__DATA__</script>
<script>
const data=JSON.parse(document.getElementById('data').textContent),canvas=document.getElementById('network'),ctx=canvas.getContext('2d'),familyPicker=document.getElementById('family'),search=document.getElementById('search'),info=document.getElementById('info');
const palette=['#c9232d','#d7535b','#a91f28','#e96b72','#8c2027','#bf3840','#df4d56','#9d2931','#c43b44','#ec777d','#7e2229','#d34851','#a52b33','#e16067'];
const families=[...new Set(data.nodes.filter(n=>n.type==='family').map(n=>n.label))];const hue=new Map(families.map((f,i)=>[f,palette[i%palette.length]]));
const nodes=data.nodes.map(n=>({...n,x:0,y:0,z:0,screen:null,r:n.type==='mechanism class'?9:n.type==='mechanism'?5.2:n.type==='family'?10:n.type==='agent scheme'?8:n.type==='technique'?4.8:3.1})),byId=new Map(nodes.map(n=>[n.id,n]));
const edges=data.edges.map(e=>({...e,a:byId.get(e.source),b:byId.get(e.target)})).filter(e=>e.a&&e.b);
const famNodes=nodes.filter(n=>n.type==='family'),techNodes=nodes.filter(n=>n.type==='technique'),appNodes=nodes.filter(n=>n.type==='approach'),agentNodes=nodes.filter(n=>n.type==='agent scheme'),classNodes=nodes.filter(n=>n.type==='mechanism class'),mechNodes=nodes.filter(n=>n.type==='mechanism');
for(const f of families){const o=document.createElement('option');o.value=f;o.textContent=f;familyPicker.append(o)}
function spherePoint(i,n,r,phase=0){const golden=Math.PI*(3-Math.sqrt(5)),y=1-(i/(Math.max(1,n-1)))*2,rad=Math.sqrt(Math.max(0,1-y*y)),a=golden*i+phase;return{x:Math.cos(a)*rad*r,y:y*r,z:Math.sin(a)*rad*r}}
const parentEdges=edges.filter(e=>e.relation==='taxonomy');
// Center the 3D clusters on the mechanism taxonomy.
classNodes.forEach((n,i)=>Object.assign(n,spherePoint(i,classNodes.length,145,-.6)));
const pending=new Set(mechNodes);for(let pass=0;pass<mechNodes.length+2&&pending.size;pass++){for(const n of [...pending]){const p=parentEdges.find(e=>e.b===n)?.a;if(p&&(p.type==='mechanism class'||p.type==='mechanism')&&(p.x||p.y||p.z)){const siblings=parentEdges.filter(e=>e.a===p&&e.b.type==='mechanism').map(e=>e.b),i=Math.max(0,siblings.indexOf(n)),q=spherePoint(i,siblings.length,95,.8);n.x=p.x+q.x;n.y=p.y+q.y;n.z=p.z+q.z;pending.delete(n)}}}
pending.forEach((n,i)=>Object.assign(n,spherePoint(i,pending.size,310,1.1)));
const byApproach=new Map();for(const e of edges)if(e.relation==='Uses mechanism'&&e.a.type==='approach'&&e.b.type==='mechanism'){if(!byApproach.has(e.a.id))byApproach.set(e.a.id,[]);byApproach.get(e.a.id).push(e.b)}
appNodes.forEach((n,i)=>{const ms=byApproach.get(n.id)||[];if(ms.length){const c={x:ms.reduce((s,m)=>s+m.x,0)/ms.length,y:ms.reduce((s,m)=>s+m.y,0)/ms.length,z:ms.reduce((s,m)=>s+m.z,0)/ms.length},siblings=appNodes.filter(x=>(byApproach.get(x.id)||[]).some(m=>ms.includes(m))),j=Math.max(0,siblings.indexOf(n)),q=spherePoint(j,siblings.length,56,1.3);n.x=c.x+q.x;n.y=c.y+q.y;n.z=c.z+q.z}else Object.assign(n,spherePoint(i,appNodes.length,390,1.4))});
const byAgentMechanism=new Map();for(const e of edges)if(e.relation==='Uses mechanism'&&e.a.type==='agent scheme'&&e.b.type==='mechanism'){if(!byAgentMechanism.has(e.a.id))byAgentMechanism.set(e.a.id,[]);byAgentMechanism.get(e.a.id).push(e.b)}
agentNodes.forEach((n,i)=>{const ms=byAgentMechanism.get(n.id)||[],c=ms.length?{x:ms.reduce((s,m)=>s+m.x,0)/ms.length,y:ms.reduce((s,m)=>s+m.y,0)/ms.length,z:ms.reduce((s,m)=>s+m.z,0)/ms.length}:spherePoint(i,agentNodes.length,500);const q=spherePoint(i,agentNodes.length,150+(n.noveltyDistance||0)*100,2.2);n.x=c.x+q.x;n.y=c.y+q.y;n.z=c.z+q.z});
for(const f of famNodes){const children=appNodes.filter(a=>a.family===f.label);if(children.length){f.x=children.reduce((s,n)=>s+n.x,0)/children.length;f.y=children.reduce((s,n)=>s+n.y,0)/children.length;f.z=children.reduce((s,n)=>s+n.z,0)/children.length;const q=spherePoint(famNodes.indexOf(f),famNodes.length,90,.3);f.x+=q.x;f.y+=q.y;f.z+=q.z}else Object.assign(f,spherePoint(famNodes.indexOf(f),famNodes.length,500))}
let yaw=-.35,pitch=.28,camera=1450,selected=null,hover=null,dragging=false,last={x:0,y:0},start={x:0,y:0},filterFamily='',familyFocus=new Set(),query='',frame=0;
function resize(){const d=window.devicePixelRatio||1;canvas.width=innerWidth*d;canvas.height=innerHeight*d;ctx.setTransform(d,0,0,d,0,0)}window.addEventListener('resize',resize);resize();
function transform(n){const cy=Math.cos(yaw),sy=Math.sin(yaw),cp=Math.cos(pitch),sp=Math.sin(pitch);const x=n.x*cy-n.z*sy,z=n.x*sy+n.z*cy,y=n.y*cp-z*sp,zz=n.y*sp+z*cp+camera,k=1050/zz;return{x:innerWidth/2+x*k,y:innerHeight/2+y*k,k,z:zz}}
function matches(n){return(!filterFamily||n.family===filterFamily||n.label===filterFamily||familyFocus.has(n.id))&&(!query||(`${n.label} ${n.family} ${n.id}`).toLowerCase().includes(query))}
function related(node){const s=new Set([node.id]);for(const e of edges)if(e.a===node)s.add(e.b.id);else if(e.b===node)s.add(e.a.id);return s}
function lineColor(e){return e.relation==='taxonomy'?'#92929255':({'Uses mechanism':'#e02d38','Supports':'#b85c63','Rebuts':'#ee7780','Depends-on':'#d18389','Refines':'#f19ba1','Qualifies':'#9c4249','Restates':'#d94b54','Supersedes':'#83252b'}[e.relation]||'#c8c8c8')}
function draw(){ctx.clearRect(0,0,innerWidth,innerHeight);const focus=selected?related(selected):null;
  for(const n of nodes)n.screen=transform(n);
  const ordered=[...edges].sort((a,b)=>(b.a.screen.z+b.b.screen.z)-(a.a.screen.z+a.b.screen.z));
  for(const e of ordered){const hot=!selected||focus.has(e.a.id)&&focus.has(e.b.id);ctx.globalAlpha=hot?(e.relation==='taxonomy'?.25:.75):.04;ctx.strokeStyle=lineColor(e);ctx.lineWidth=e.relation==='taxonomy'?.75:1.6;ctx.beginPath();ctx.moveTo(e.a.screen.x,e.a.screen.y);ctx.lineTo(e.b.screen.x,e.b.screen.y);ctx.stroke();if(hot&&e.relation!=='taxonomy'&&e.a.screen.k>.7){const a=e.a.screen,b=e.b.screen,ang=Math.atan2(b.y-a.y,b.x-a.x);ctx.fillStyle=lineColor(e);ctx.beginPath();ctx.moveTo(b.x,b.y);ctx.lineTo(b.x-5*Math.cos(ang-.45),b.y-5*Math.sin(ang-.45));ctx.lineTo(b.x-5*Math.cos(ang+.45),b.y-5*Math.sin(ang+.45));ctx.fill()}}
  for(const n of [...nodes].sort((a,b)=>b.screen.z-a.screen.z)){const p=n.screen,active=matches(n),hot=!selected||focus.has(n.id);ctx.globalAlpha=active?(hot?1:.14):.025;const color=n.type==='agent scheme'?'#ffb454':n.type==='family'?'#f7f7f7':n.type==='mechanism class'?'#c9232d':n.type==='mechanism'?'#f0eeee':hue.get(n.family)||'#d7535b';const radius=Math.max(1.5,n.r*p.k);ctx.fillStyle=color;ctx.shadowColor=color;ctx.shadowBlur=n===selected?18:active?6:0;ctx.beginPath();if(n.type==='agent scheme'){ctx.moveTo(p.x,p.y-radius);ctx.lineTo(p.x+radius,p.y);ctx.lineTo(p.x,p.y+radius);ctx.lineTo(p.x-radius,p.y);ctx.closePath()}else ctx.arc(p.x,p.y,radius,0,Math.PI*2);ctx.fill();ctx.shadowBlur=0;
    if(n.type==='family'||n===hover||n===selected){ctx.globalAlpha=active?1:.18;ctx.font=`${n.type==='family'?12:11}px system-ui`;ctx.fillStyle=n.type==='family'?'#eff6fa':'#e3edf4';ctx.fillText(n.label,p.x+radius+5,p.y+4)}}
  ctx.globalAlpha=1;frame++;if(!dragging&&!selected)yaw+=.00022;requestAnimationFrame(draw)}
function hit(x,y){let found=null,best=Infinity;for(const n of nodes){if(!matches(n))continue;const p=n.screen,d=Math.hypot(p.x-x,p.y-y),r=Math.max(6,n.r*p.k+2);if(d<r&&d<best){found=n;best=d}}return found}
function show(n){selected=n;if(!n){info.innerHTML='<h2>Explore the map</h2><p>Drag to rotate · scroll to zoom · click a node to inspect its connections.</p>';return}const near=edges.filter(e=>e.a===n||e.b===n).map(e=>({edge:e,node:e.a===n?e.b:e.a}));let html=`<h2>${esc(n.label)}</h2><p>${esc(n.type)}${n.family?' · '+esc(n.family):''}</p>`;if(near.length){html+='<div>';for(const x of near.slice(0,6))html+=`<span class="pill">${esc(x.edge.relation)} · ${esc(x.node.label)}</span>`;if(near.length>6)html+=`<span class="pill">+${near.length-6} more links</span>`;html+='</div>'}info.innerHTML=html}
function esc(s){return String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
canvas.addEventListener('pointerdown',e=>{dragging=true;canvas.classList.add('drag');last={x:e.clientX,y:e.clientY};start={...last};canvas.setPointerCapture(e.pointerId)});canvas.addEventListener('pointermove',e=>{if(dragging){yaw+=(e.clientX-last.x)*.006;pitch=Math.max(-1.35,Math.min(1.35,pitch+(e.clientY-last.y)*.006));last={x:e.clientX,y:e.clientY}}else{hover=hit(e.clientX,e.clientY);canvas.style.cursor=hover?'pointer':'grab'}});canvas.addEventListener('pointerup',e=>{if(dragging){const moved=Math.hypot(e.clientX-start.x,e.clientY-start.y);dragging=false;canvas.classList.remove('drag');if(moved<4){const n=hit(e.clientX,e.clientY);if(n)show(n)}}});canvas.addEventListener('pointercancel',()=>{dragging=false;canvas.classList.remove('drag')});
canvas.addEventListener('wheel',e=>{e.preventDefault();camera=Math.max(650,Math.min(3800,camera*(e.deltaY>0?1.1:.91)))},{passive:false});search.addEventListener('input',()=>{query=search.value.trim().toLowerCase();if(query){const n=nodes.find(matches);if(n){yaw=0;pitch=0;show(n)}}});familyPicker.addEventListener('change',()=>{filterFamily=familyPicker.value;familyFocus=new Set();if(filterFamily){const apps=appNodes.filter(n=>n.family===filterFamily);for(const a of apps){familyFocus.add(a.id);for(const e of edges.filter(e=>e.a===a&&e.relation==='Uses mechanism')){familyFocus.add(e.b.id);for(const p of parentEdges.filter(p=>p.b===e.b))familyFocus.add(p.a.id)}}for(const t of techNodes.filter(n=>n.family===filterFamily))familyFocus.add(t.id);const f=famNodes.find(n=>n.label===filterFamily);if(f)show(f)}else show(null)});document.getElementById('home').onclick=()=>{yaw=-.35;pitch=.28;camera=1450;filterFamily='';familyFocus=new Set();query='';selected=null;search.value='';familyPicker.value='';show(null)};
draw();
</script></body></html>'''


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()
    graph = full_graph(args.root / "maps")
    keep = {n["id"] for n in graph["nodes"] if n["type"] in {"family", "approach", "mechanism", "mechanism class"}}
    nodes = [n for n in graph["nodes"] if n["id"] in keep]
    edges = [e for e in graph["edges"] if e["source"] in keep and e["target"] in keep]
    by_id = {n["id"] for n in nodes}
    family_ids = {n["label"]: n["id"] for n in nodes if n["type"] == "family"}
    for node in nodes:
        if node["type"] == "approach" and node.get("family") in family_ids:
            edges.append({"source": family_ids[node["family"]], "target": node["id"], "relation": "taxonomy", "arrow": "---"})
    feature_path = args.root / "maps" / "approach_features.tsv"
    with feature_path.open(encoding="utf-8", newline="") as stream:
        for row in csv.DictReader(stream, delimiter="\t"):
            approach_id = "n_" + row["address"].replace(":", "_").replace("-", "_").replace(" ", "_")
            for mechanism in filter(None, row["mechanism"].split(";")):
                mechanism_id = "mech_" + mechanism.replace("-", "_")
                if approach_id in by_id and mechanism_id in by_id:
                    edges.append({"source": approach_id, "target": mechanism_id, "relation": "Uses mechanism", "arrow": "-->"})
    # Agent-devised schemes are shown as a distinct, explicitly labeled layer.
    registry = args.root / "maps" / "agent_chess_schemes.tsv"
    if registry.exists():
        with registry.open(encoding="utf-8", newline="") as stream:
            scheme_rows = list(csv.DictReader(stream, delimiter="\t"))
        approach_sets = {}
        with feature_path.open(encoding="utf-8", newline="") as stream:
            for row in csv.DictReader(stream, delimiter="\t"):
                aid = "n_" + row["address"].replace(":", "_").replace("-", "_").replace(" ", "_")
                approach_sets[aid] = {"mech_" + m.replace("-", "_") for m in filter(None, row["mechanism"].split(";"))}
        for row in scheme_rows:
            mids = ["mech_" + m.replace("-", "_") for m in filter(None, row["mechanisms"].split(";"))]
            mids = [m for m in mids if m in by_id]
            aset = set(mids)
            best_score, best_id = -1.0, ""
            for aid, pset in approach_sets.items():
                union = aset | pset
                score = len(aset & pset) / len(union) if union else 0
                if score > best_score: best_score, best_id = score, aid
            nearest = next((n["label"].replace("<br/>", " ").replace("<br>", " ").replace("\ufffd", " ").replace("\u2026", "...") for n in nodes if n["id"] == best_id), "Unmapped")
            sid = "agent_scheme_" + row["scheme_id"]
            nodes.append({"id": sid, "label": row["label"], "type": "agent scheme", "team": row["team"], "version": row["version"], "summary": row["summary"], "runs": row["runs"], "noveltyDistance": round(1-best_score, 3), "nearestApproach": nearest})
            by_id.add(sid)
            for mid in mids: edges.append({"source": sid, "target": mid, "relation": "Uses mechanism", "arrow": "-->"})
    # Each record's family field drives cluster color and family filtering.
    payload = json.dumps({"nodes": nodes, "edges": edges}, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    output = args.out or args.root / "maps" / "approach_network_agent_schemes.html"
    output.write_text(PAGE.replace("__DATA__", payload), encoding="utf-8")
    counts = {kind: sum(n["type"] == kind for n in nodes) for kind in ("family", "approach", "mechanism class", "mechanism", "agent scheme")}
    print(f"Wrote {output}: {len(nodes)} nodes {counts}, {len(edges)} links")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
