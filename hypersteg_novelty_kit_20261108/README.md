# Hypersteg novelty kit, 8 November 2026

With this kit you can run the novelty audit in `novelty_audit_protocol.md`. The graph zip sent earlier is for browsing; this one is for judging.

- `maps/`: the mechanism tree (`mechanism_taxonomy.tsv`, v3, the audit key), the family tree and the approach feature table.
- `maps/approach_network.html` and `maps/haki_logo.png`: the base mechanism-centered 3D network, styled to the Haki dark theme and supplied wordmark.
- `maps/approach_network_agent_schemes.html`: a separate copy with 19 clearly labeled AGENT-DEVELOPED chess schemes. Orange diamond nodes identify these additions; click one for its team, version, summary, run source, mechanism links, and distance score. The score is 1 minus the Jaccard overlap between the scheme's mapped mechanism set and the nearest published approach's mechanism set (0-1); higher means more distant from this literature corpus, not proof of novelty.
- `maps/agent_chess_schemes.tsv`: the curated scheme registry. Keep `haki_logo.png` beside either HTML file. Regenerate the agent-scheme copy with `python tools/render_approach_network_3d.py`; the original base HTML remains unchanged.
- `literature/verified_claims/`: 93 quote ledgers, one per paper. Each approach row and each grounding claim cites a claim in one of them.
- `tools/`: the Ledger tools; `build_approach_map.py` is the one the protocol uses. Python 3.10 or later, standard library only.

Look up the neighbours of one or more mechanism nodes (protocol step 2):

    python3 tools/build_approach_map.py neighbours --root . m-payoff-anchored-symbols

Check that every landing leaf of the tree has published evidence:

    python3 tools/build_approach_map.py check-coverage --root .

The WARNING lines name approaches placed only at non-landing nodes (evaluation, foundation and detector nodes), against which no scheme is judged. They are expected.
