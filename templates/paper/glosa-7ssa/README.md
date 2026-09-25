# templates/paper/glosa-7ssa/ — GLOSA-7SSA paper template

> tier: Dr (specified; independently unreviewed)

**What it is.** A LaTeX manuscript template (`main.tex`) plus its schema document
(`SCHEMA.md`) for academic conceptual/theoretical articles. 7SSA = "Seven-Section
Scholarly Architecture": one stable seven-sector intellectual core — Introduction;
Approach/Scope/Knowledge Base; Existing Knowledge and Theoretical Foundation; Problem
in Existing Knowledge; New Contribution; Critical Evaluation/Boundaries/Implications;
Conclusion — that can be rendered as 6–8 visible sections for a Q1 international
journal, 4–7 visible sections for a Thai-journal compression, or a specialty layout
(review / formal / legal / policy / SoK), while the underlying reasoning core stays
the same across renderers. `SCHEMA.md` is the founder's own pseudo-DAG specification
of this schema (world↔Thai crosswalk, the 4/5/7-section compressions, and 8
article-type renderers); it is reproduced here verbatim except for the recorded changes listed under "Terminology alignment" below, and is not glosa's own claim.

**When a router should pick this template.** For an article that is academic
conceptual, theoretical, philosophical, doctrinal-legal, integrative-review,
formal-conceptual, systematization-of-knowledge (SoK), or policy-analytic in genre —
i.e. genres where the contribution is a construct, distinction, theory, framework,
mechanism, taxonomy, formalization, legal principle, or research agenda, not a new
empirical dataset. Not the right template for a purely empirical/data-report paper
(no Methods/Results/experimental-design scaffolding is built in) or a pure formal-proof
artifact (no Coq/proof-object scaffolding is built in) — route those to a different
template.

**How it maps to glosa's own apparatus.**
- `main.tex` §"Core Epistemic Structure" is this template's rendering of glosa
  **P20** (`methodology/P20_core_epistemic_structure.md`): Core Respondent/
  Experience-Based Expert · Interactional Expert (or None) · AI Model(s) Used, plus
  the non-collapse line. It is the only place in this template where naming an AI
  model is appropriate (role-disclosure, not authorship).
- Appendix "Claim Matrix" and "Five-question claim audit"
  (`app:claim-matrix`, `app:five-q`) mirror glosa **P03** claim cards (five questions
  ⇄ Evidence-Assumption-Dependency) — one row per load-bearing claim, tiered, never a
  blanket paper-level tier.
- Appendix "Literature Review System record" (`app:lrs`) mirrors glosa **P13**
  (literature review: frozen scope → protocol → acquisition → extraction → citation
  verification → manifest/neighbour table) — L1–L6 as named there.
- Appendix "AI route-level disclosure and silent-lift audit" (`app:ai-route`) mirrors
  glosa **P07** (what AI added, route-level, never silently merged into the source).
- §"Approach, Scope, and Knowledge Base" → "AI involvement in the research process"
  and the "Declaration of generative AI..." block correspond to glosa **P06**
  (maker ≠ checker ≠ approver; independence ladder I0–I5). This template carries no
  `D-*` disclaimer catalogue of its own; if a manuscript needs those items, take them from
  `arxiv-onecol/disclaimers.tex`.
- Appendix "Pre-publication adversarial gate" (`app:publish-gate`, R1–R14) mirrors
  glosa **P10** (`methodology/P10_publish_gate.md`) — R1–R7 there correspond directly
  to this template's R1/R2/R3/R4/R5/R6/R7; R8–R14 add publication-ethics items
  (Human Mastery Gate, CRediT, funding/COI, ethics/consent/data/code declarations, AI
  public-disclosure/internal-log match, current journal-policy check, and confidential
  peer-review-material handling) that this template's cross-publisher profile adds on
  top of the base glosa gate.

**Build.** `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` from this
directory. Standard pdflatex packages only (see the `\usepackage` block at the top of
`main.tex`); no custom `.sty`, no `\input`/`\include`, and no `\bibliography{}` call —
references are a manual `thebibliography` placeholder, so no `refs.bib` is needed for
this template as shipped. `main.pdf` is committed on purpose (as in the arxiv
templates) so the rendered form can be read without building; delete the other build
artefacts (`*.aux .fls .fdb_latexmk .log .out .toc`) before committing — the repository's
root `.gitignore` already covers them.

**Status.** K0 internal working template, tier Dr (specified; independently
unreviewed) — this template itself has not been through glosa's own publish gate as a
claim; it is scaffolding, not a claim about how journals work. The cross-publisher
policy content embedded in `main.tex` (NRCT/ICMJE/Elsevier/Springer/Wiley conventions,
the "Internal policy-interoperability checklist") is the founder's own relayed
reading of those policies, reproduced as scaffolding text inside the template — it is
**NEEDS_VERIFICATION** against each target journal's actual current author guidelines
at submission time, never treated as settled cross-publisher fact by this repository.
`main.tex`'s own comment block says the same: "The current instructions of the target
journal always override placement, wording, file-format, and disclosure details."

**Files.**
- `main.tex` — the template, `[FILL: ...]` placeholders intact, submission-mode and
  glosa-audit-mode `\newif` toggles for a journal-facing vs. internal-audit render.
- `SCHEMA.md` — the founder's 7SSA pseudo-DAG schema document, reproduced verbatim except the recorded changes below
  with a short front-matter header; not glosa's own claim, not rewritten here.

## Source provenance

| File | Source (founder-owned, ~/Downloads at registration) | sha256 | Size |
|---|---|---|---|
| `main.tex` | `GLOSA_7SSA_Global_Scholarly_Schema_v1.tex` (2026-09-25) | `8e38ff0acd98357ae04274d4cb38ab4b9b2fedadde83b7d237a966da7e56c503` | 34,353 B |
| `SCHEMA.md` | `q1_world_thai_7sector_master_schema.pseudo.dag.md` (2026-09-25) | `1c8989c033254605e5df7c6e1a434cc3d640d061c6bcafe7408fc365d59df980` | 48,814 B |

Author of both sources: the founder (method direction). Whether the sources were
themselves AI-assisted upstream is OPEN; only the founder can state it. At registration an
AI assistant drafted this README.md and inserted the Core Epistemic Structure block into
`main.tex`; every other change is listed below.

## Recorded changes to the sources

`SCHEMA.md`: a 9-line HTML-comment header; line 1182 the gate key renamed to
`prior_work_collision_test`; line 1465 the sentence now reads "BUILD literature foundation
only after the gap survives the prior-work collision test"; line 1564 checklist label →
"Gap survives prior-work collision test"; line 1956 the key renamed to
`prior_work_collision`. `main.tex`: the Core Epistemic Structure block (P20) inserted before
`\section{Introduction}`; the R6 gate label → "Overclaim/register scan (contaminated-concept
table)", matching P10 R6. Reason for the renames: glosa rule 6 bars that word from template
and paper files; the gate's meaning (does a stated gap collide with prior work?) is unchanged.
Recorded 2026-09-25.

Publisher-policy references and the policy table inside `main.tex` are the founder's relayed
reading and remain NEEDS_VERIFICATION; the template says so in its own text.
