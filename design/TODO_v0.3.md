# TODO v0.3 (step list — one line per step, updated as we go)
- [x] S1 knowledge harvest — wf_eda73434-df6: 42 base cards + 282 hub cards (324), 578 kg edges, KNOWLEDGE_STATUS_v0.3.md (adopt 100, adapt 35, superseded 42, outdated 2)
- [x] S2 literature review — wf_70946651-7ca: 8 questions, 62 citation cards (METADATA_OK; I3 route running), DIGEST.md with 8 DAG candidates
- [x] S3 improvement DAG — design/DAG_v0.3.yaml (26 nodes, 25 edges: 21 proposed, 2 deferred, 3 done), docs/dag_v0.3.svg; 6 nodes need founder decision
- [x] S4 simulation — sim/v0.3/report.md: baseline recall 0.70 (missed: composite_quote, hidden_ai_fill, inflated_bearing, injected_infinity) → combined 0.85 with 0 false alarms; ship: I/Z taxonomy gate, comparison-evidence field; revise: verdict-class vocab, PCS flag, genre-router diagnostic, intake tier flag; drop: verifiability flag (kernel already covers), prereg fields
- [ ] S4b add kernel checks for the 3 still-missed defect classes (composite_quote "…" in exact_passage; hidden_ai_fill = ai_filled empty while cooking log has AI steps; inflated_bearing = own-lineage/context card with SUPPORTS) — carry into S5 as DAG nodes
- [ ] S5 FOUNDATION v0.6 + architecture review (waiting: founder decisions on 6 nodes)
- [ ] S6 build + README (DAG, kg graph)
- [ ] S7 release v0.3.0
RAM rule: check `free -g` before every Workflow; ≤6 workers; never two Workflows at once.
