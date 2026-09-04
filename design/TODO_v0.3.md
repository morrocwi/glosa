# TODO v0.3 (step list — one line per step, updated as we go)
- [x] S1 knowledge harvest — wf_eda73434-df6: 42 base cards + 282 hub cards (324), 578 kg edges, KNOWLEDGE_STATUS_v0.3.md (adopt 100, adapt 35, superseded 42, outdated 2)
- [x] S2 literature review — wf_70946651-7ca: 8 questions, 62 cards → 60 VERIFIED (I3) + 2 parked; all 8 manifests PASS; rule 26 caught 4 composite quotes the route had passed
- [x] S3 improvement DAG — design/DAG_v0.3.yaml (26 nodes, 25 edges: 21 proposed, 2 deferred, 3 done), docs/dag_v0.3.svg; 6 nodes need founder decision
- [x] S4 simulation — sim/v0.3/report.md: baseline recall 0.70 (missed: composite_quote, hidden_ai_fill, inflated_bearing, injected_infinity) → combined 0.85 with 0 false alarms; ship: I/Z taxonomy gate, comparison-evidence field; revise: verdict-class vocab, PCS flag, genre-router diagnostic, intake tier flag; drop: verifiability flag (kernel already covers), prereg fields
- [ ] S4b add kernel checks for the 3 still-missed defect classes (composite_quote "…" in exact_passage; hidden_ai_fill = ai_filled empty while cooking log has AI steps; inflated_bearing = own-lineage/context card with SUPPORTS) — carry into S5 as DAG nodes
- [x] S5 FOUNDATION v0.6 patch spec — architecture review wf_32bcc737-f85 (20 MUST + 15 SHOULD) → all 20 MUST applied (review response section); 6 DAG nodes still pending founder
- [x] S6 build — wf_757d03a2-879: rules 18,19,20,21,23,26-28 in kernel (181 tests), schema 0.7.0, sim regression test, kg render, FOUNDATION v0.6 + REPO_SPEC v0.6, README v0.3.0 with DAG + kg; CLI --citation-cards; own card 0202 downgraded by rule 28 (own-lineage SUPPORTS → NEUTRAL)
- [ ] S7 release v0.3.0 — gate v3 PASS_WITH_LIMITS (all BLOCKs fixed); Zenodo new version + tag pending founder push
RAM rule: check `free -g` before every Workflow; ≤6 workers; never two Workflows at once.

## Finding 2026-09-05 (S6 build, live)
New kernel rule 26 (composite-quote detector) immediately caught 4 of our own S2 citation cards (q4-001, q4-006, q4-008, q8-008) whose exact_passage carried an ellipsis splice — passages the cross-vendor I3 route had passed because its mechanical check matches only the first 12 words. Rule 26 closes that gap at the origin; the route script should also refuse spliced passages (todo).
