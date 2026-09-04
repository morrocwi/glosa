# glosa v0.3 — roadmap (step DAG, founder instruction 2026-09-05, BBL-2026-09-05-113/114/115)

> Readout, not truth. Every step ends with an artifact a stranger can check. One Workflow at a
> time, ≤6 concurrent workers, no embeddings/GPU work — RAM on this workstation is 14 GB with
> ~8 GB free (founder: "ระวังแรมให้ดี").

| step | what | input | output (checkable) | gate to next |
|---|---|---|---|---|
| S1 knowledge harvest | read every member of the Zenodo hubs (base = Readout Universe textbook + Readout Genesis core); extract knowledge cards: definition / rule / claim, each with source DOI + locator (rule 17) and a status **holds / refined-by-later-work / superseded / outdated / open** judged against the base | hubs ep, ai, aihp; readout_universe + readout_genesis repos; local sources/ | `knowledge/harvest_v0.3/*.yaml` + `KNOWLEDGE_STATUS_v0.3.md` (table) | ≥1 cross-vendor spot-check per hub; no card without locator |
| S2 literature review | S14 LRS on the improvement questions raised by S1 and by the v0.2 self-application (rule 17, I3 route) | S1 gaps | `records/lit/glosa-v0.3/*` manifests PASS | accuracy + diversity gates |
| S3 improvement DAG | nodes = proposed changes (from S1 statuses, S2, dogfood findings, gate v1/v2 warnings); edges = dependencies; each node carries an acceptance test | S1, S2 | `design/DAG_v0.3.yaml` + rendered `docs/dag_v0.3.svg` | every node has a test + owner |
| S4 simulation | synthetic claim cards + adversarial cases run through the kernel: measure gate precision/recall before vs after each DAG node (finite_diagnostic) | S3 | `sim/v0.3/report.md` with numbers | no node ships without a measured effect |
| S5 architecture | FOUNDATION v0.6 draft + REPO_SPEC v0.6; chair ruling on disputes | S1–S4 | design/FOUNDATION_v0.6.md | independent architecture review MUST list |
| S6 build | ultracode build of the DAG nodes; tests; docs; README with DAG + knowledge graph (kg) render | S5 | code + tests green | publish gate R1–R7 |
| S7 release | v0.3.0: Zenodo new version, tag, registry | S6 | DOIs | founder go |

Owner of every human decision: founder. Owner of every mechanical check: kernel. Step status is kept in `design/TODO_v0.3.md`.
