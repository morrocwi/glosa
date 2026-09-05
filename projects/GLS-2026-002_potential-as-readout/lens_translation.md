# Lens translation — GLS-2026-002 (potential-as-readout)

> tier: Dr (specified; independently unreviewed). Follows `methodology/P00_lens.md` (lens-in before
> analysis, lens-out before the hypothesis is stated) and fills the field names owned by
> `schema/claim_card.schema.json`'s `lens_translation` block, this project's own copy. Sourced from
> `NOTE_2026-09-05_potential-choice-violence_axis.md` (cpg_research_journal/research/
> society-justice-peace/) and `paper/main.tex`'s own problem section.

## question_human

**text_verbatim** (Thai, verbatim — the problem card's own Q1,
`blackbox/log/entries.jsonl#BBL-2026-09-05-129/130`):

> "ตรวจว่า 'เครื่องศักยภาพ' ในบันทึก Effective, Corrigible Agency Potential (AP) นั่งอยู่บนสมการและ
> นิยามของงานเดิมในซีรีส์ Society, Justice, Peace & Violence ได้จริงหรือไม่ โดยเฉพาะกรณีระบอบที่
> อยู่รอดด้วยการกดปราบ แล้วสกัดแกนร่วมออกมาให้ต่อยอดได้"

**language:** th
**blackbox_line_ref:** `GLOSA-PC-20260905-0002.yaml#intake.q1_issue` (project copy);
`NOTE_2026-09-05_potential-choice-violence_axis.md#0`

English rendering (not a translation-in-place — the field above stays Thai verbatim; a separate
reading aid): *check whether the "potential machine" in the Agency Potential note actually sits on
the equations and definitions of the programme's own four prior papers, especially in the case of a
regime that survives by suppression, then extract the shared axis so it can be built on.*

## question_readout

Under the access relation this programme actually has (§`access_relation_R` below), does the word
"potential" — as it appears in Agency Potential's $\Pi^{\mathrm{feas}}$, Causal Ethics'
$R_{\mathrm{adm}}$, Causal Agency's $V$, and Causal Grammar's "feasible life-space" — name **one**
readable, checkable quantity across all four texts, or does each text silently declare its own
feasible set and only share a name?

Contaminated concept flagged here (per `paper/main.tex`'s own reading, §"The problem"): "ศักยภาพ"
(potential) as ordinarily used quietly treats the feasible/admissible/viable set as something
simply *given*, rather than as itself a readout that must be stated to be checked — the declaration
step is exactly where the four prior papers, and Agency Potential after them, are silent.

## local_contrast_space_X

The finite, named set of readable states this question distinguishes between (not a continuum of
"more or less potential"):

- `X1` — "potential" reported as a bare declared set (a feasible/admissible/viable region asserted
  without a stated rule for what belongs in it) — the failure mode `paper/main.tex` names as
  "declares a set... and measures against it; none says how the set itself is read."
- `X2` — "potential" reported as an envelope over a witnessed set (D2's witness rule: a finite,
  enumerable set under a retained selection rule — only policies with a retained execution record
  count).
- `X3` — as `X2`, and additionally separated by layer: layer-1 potential (choice within a fixed
  constraint structure $C$) kept apart from layer-2 potential (capacity to change $C$ itself) — D3.
- `X4` — as `X3`, and additionally separated from what was actually exercised ($\pi_{\mathrm{used}}$)
  and from what an evaluator's instrument returns ($Y_{\mathrm{obs}}=\mathcal O_q(H)$) — D1 / NC-78.
- `X5` — a compression of `X2`-`X4` (a shrinking capability set) read with the diagnosis of the
  shrinkage (an obstruction ledger, cost asymmetry) kept apart from the attribution of who is
  responsible for it — D6 / NC-79.

## access_relation_R

What this programme's own five texts can actually reach, as opposed to what would be needed for a
population-level or externally-validated claim about "potential" in general — the access model this
project's readout is computed against:

- **Has access to:** the programme's own four prior formal papers and their stated equations/
  definitions; the fifth note (AP, not yet deposited); the programme's own epistemic core (Readout
  Genesis, Readout Universe — N2, ARCH-L4, VI.3, V.9/VIII.4, VI.6, ETH-1(iv)/ETH-8/ETH-11); one
  executed two-node numerical fixture (`sim/nogo_fixture.py`); openly fetchable published literature
  in peace research, capability theory, and information-theoretic agency (Galtung, Sen/Nussbaum,
  Bandura, Emirbayer & Mische, Bazzani, Klyubin/Polani, Foucault).
- **Does NOT have access to:** any human population's actual measured capability sets (no fieldwork,
  no survey, no cohort); an independently authored second fixture testing the same no-go claim; an
  I5 (outside human, no stake) review route, not yet arranged for this project.
- **Consequence for R:** any claim this project makes about "potential" as a portable concept is
  itself read through this same restricted access relation — a definitional/literature-comparison
  check plus one fixture, not a population-level empirical demonstration. This is
  `restriction_provenance` below.

## claim_function_Phi_z0

The readout functional this project evaluates a candidate hypothesis against, at the reference
point $z0$ = "one of the programme's own five texts' use of the word potential, before this
project's own comparison pass": does restating that text's feasible/admissible/viable set under the
witness rule (H1), the two-layer separation (H2), or the fixture-tested pseudo-peace signature (H3)
let an independent reader recover the same distinction the source text draws — i.e. does the
programme's own reading discipline actually apply cleanly to texts it did not write with that
discipline in mind, or does it only look like it applies? `Phi_z0` is this fit-checking functional,
not a truth-functional — passing it certifies that the reading discipline recovers a checkable
distinction in the source text, not that the source text's own claim about the world is true.

## formal_applicability

`exact_functional` for H1 (the witness rule is stated as an exact set-membership test) and H3 (the
fixture computes exact numerical quantities); `relational_pointwise` for H2 (the layer-1/layer-2
separation is checked per-source, pointwise, not as one global functional) — per `P00_lens.md` §3.2b's
plain-language enum; not `not_applicable_narrative`, since this is a design/definitional-comparison
question, not narrative-only reporting.

## restriction_provenance

Named explicitly per `access_relation_R` above: every distinction this project draws about
"potential" is itself drawn from inside the same programme that produced the four prior papers and
the fifth note being checked — this is a reflexive check (the programme's own epistemic core applied
to the programme's own prior claims), not an externally commissioned audit. This is disclosed, not
hidden: the founder's own ruling (BBL-2026-09-05-130, "เรามีคำตอบทุกอย่างในเจเนซีสและรี้ดเอาท์อยู่แล้ว")
explicitly frames this project as closing gaps with the programme's *own* existing machinery, which
is exactly the restricted-access condition this section names.

---

*Lens-in/lens-out performed under Readout Universe — Yaoharee Lahtee (lens, DOI
10.5281/zenodo.21529456, 10.5281/zenodo.21665100; repos github.com/morrocwi/readout_universe,
github.com/morrocwi/readout_genesis). Drafted by AI (the AI assistant seat); not yet reviewed by an
independent route; candidate hypotheses drawn from this translation live in `hypotheses.md` and are
selected in `hypothesis_selection.yaml` per the founder's own three verbatim rulings
(BBL-2026-09-05-130/132/134).*
