# Literature search questions — potential-as-readout (GLS-2026-002)

> For workers `lit-h1-h3` and `lit-h2` populating `records/lit/potential-as-readout/h{1,2,3}/`.
> Source-first citation discipline applies throughout (glosa rule 17): every citation card carries
> `fetched_from_url` + `page_or_locator` + `line_or_paragraph` + ONE continuous verbatim
> `exact_passage` copied from the fetched text, never from memory, never spliced. Comparison
> vocabulary is `same`/`different`/`cited` only — never `novel`/`first`/`prior art`/`breakthrough`
> (glosa gate rule 6). Rate-limit discipline: sleep >=1.5s between Zenodo/Crossref/arXiv fetches, on
> 429 wait 30s and retry once, then fall back to Wayback or Unpaywall; paywalled sources get a
> record-level card with `fetch_status: PAYWALLED_ABSTRACT_ONLY` and `exact_passage` from the
> abstract only.

Background: `paper/main.tex` (Potential as a Readout,
`cpg_research_journal/research/society-justice-peace/paper/main.tex`) already cites and quotes
Galtung (1969/1990), Sen/Kabeer, Bandura, Emirbayer & Mische, Bazzani (2023), Klyubin & Polani
(2005), Foucault (1982), and the programme's own four prior papers (Causal Grammar, Causal Ethics,
Violence-as-Instability, Causal Agency) plus the Readout Genesis/Readout Universe core. Sources
already fetched locally are listed in `paper/sources/` (bazzani2023.html, csaky2026.html,
foucault1982.pdf/.pages.txt, galtung1969.pdf/.pages.txt, galtung1990.pdf/.pages.txt,
klyubin2005.pdf/.pages.txt, sathaanand2021.pdf/.txt) — check there first before re-fetching.

## H1 — Witness rule (operational definition of a feasible/potential set)

Hypothesis: potential = the envelope over a **witnessed** set (finite, enumerable, under a retained
selection rule — only policies with a retained execution record count), not a declared, unretained
continuum.

Search questions:
1. Does Galtung's own peace-research literature (1969, 1990, and any successor treatment of the
   violence-as-gap definition) ever state, anywhere, an operational test for what counts as a
   person's "potential realization" — i.e. a rule for which possibilities are admitted into the
   baseline the gap is measured against? Or is the baseline always asserted?
2. Does capability theory (Sen 1985/1999, Nussbaum, Kabeer 1999) define the "capability set" with
   any equivalent to a retained-record/witnessed-execution test, or is it declared from a list of
   valued functionings?
3. Does information-theoretic agency (Klyubin & Polani 2005, and successors on empowerment) define
   the actuation channel's alphabet — the set of actions "available" to the agent — with any
   evidentiary/witnessed criterion, or is the available-action set simply given by the environment
   model?
4. Search AI-safety/corrigibility literature (e.g. work on capability elicitation, "capability
   overhang", or eval-based capability measurement) for any explicit finite-witnessed-record
   definition of a system's "capability" that resembles the witness rule stated here. Log same/
   different/cited for each hit.
5. For each source above: does it state, explicitly or by clear implication, that the declared
   feasible/capability/admissible set could differ from what has actually been observed/executed —
   and if so, does it give a rule for resolving the difference, or leave it as an open gap (as this
   project claims all four does)?

## H2 — Two layers of agency (choice within a structure vs. change of the structure)

Hypothesis: "potential" conflates (a) choosing within a fixed constraint structure and (b) changing
the structure itself; these must be kept separate (Causal Agency's own layer-2 "agency" vs.
"proto-agency" distinction, D3).

Search questions:
1. Does Sen's capability approach, or Nussbaum's central capabilities list, distinguish between
   choosing among existing options and the capacity to expand/renegotiate the option set itself
   (e.g. via political voice, collective action)? Quote the exact passage if so.
2. Does Bandura's social-cognitive theory of agency (intentionality, forethought, self-regulation,
   self-reflection, 2001) draw a line between exercising agency within a given environment and
   agency directed at changing the environment/structure itself? Is this the same line, a
   different line, or unaddressed?
3. Does Emirbayer & Mische's (1998) "iterational / projective / practical-evaluative" structure of
   agency map onto, differ from, or leave unaddressed the layer-1/layer-2 line this project draws?
4. Does Bazzani (2023) — already fetched, `paper/sources/bazzani2023.html` — micro-meso-macro
   conversion-factor account distinguish factors that let a person use existing capabilities from
   factors that let a person change the conversion process itself? Quote exactly.
5. Search relational-sociology or political-agency literature more broadly for an existing named
   distinction equivalent to this project's layer-1/layer-2 split (e.g. "first-order" vs.
   "second-order" agency, "adaptive" vs. "transformative" agency). Log same/different/cited.

## H3 — Pseudo-peace numerical signature (fixture-tested)

Hypothesis: a suppression regime that lowers visible instability-amplitude without changing the
underlying operator shows a distinguishable numerical signature (threshold re-crossing once a
suppression budget is exhausted; unbounded accumulated force under sustained suppression) versus a
genuine operator change (repair) that achieves the same visible calm at zero accumulated cost.
Already executed once: `sim/nogo_fixture.py` / `sim/nogo_fixture_result.json` (tier
`finite_diagnostic` on that fixture only, one documented failed-then-corrected control).

Search questions:
1. Does the violence-as-instability / structural-violence literature (beyond this programme's own
   `lahtee_vi`) report any comparable observation — that suppressing a visible symptom without
   addressing the underlying structural driver produces recurrence once suppression lapses, or
   escalating cost the longer suppression is sustained? Quote exactly; log same/different/cited.
2. Does AI-safety/corrigibility literature discuss an analogous distinction between suppressing a
   model's visible undesired output (e.g. via output filtering/RLHF-style amplitude suppression)
   versus changing the underlying capability/objective structure — and does any such source report
   a "cost grows unboundedly under sustained suppression, recurs once suppression stops" pattern?
3. Is there any published finite-memory or control-theoretic no-go result (outside this programme)
   stating that no *bounded* intervention can drive a sustained-load system to a permanently
   sub-threshold state, comparable to the Violence-as-Instability No-Go theorem this fixture tests?
   Log same/different/cited — do not claim priority either way.
4. Foucault (1982, already fetched) on power "structuring the possible field of action of others" —
   does this text, or literature building on it, discuss a bounded-suppression-vs-structural-change
   distinction with any numerical or quasi-numerical framing?
5. Search for any independently reproduced or critiqued version of a comparable two-node/small-
   network instability fixture (control-theory, epidemiology, or social-dynamics literature) that
   could serve as a cross-check or a counter-instance to this project's own fixture result.

## Output format expected from each lit worker

Under each `h{1,2,3}/`: a completed `search_log.yaml` (already scaffolded), a `litreview_manifest.yaml`,
a `dialogue_table.md` (already scaffolded), and one citation card per source found under
`h{N}/citations/` (schema: `schema/citation_card.schema.json`), named `cite-potential-h{N}-NNN.yaml`
to match the placeholder ids already referenced in `claims/GLOSA-CC-20260905-030{1,2,3}.yaml`'s
`five_questions.seen.citation_refs` / `five_questions.tested.evidence_relations`. **These placeholder
ids must be reconciled against whatever ids the lit workers actually assign** — if a lit worker's
citation card uses a different id, the claim cards' evidence_relations and citation_refs need a
follow-up pass to point at the real id, not left silently mismatched (glosa gate rule 10: no finding
is ever dropped, no hand-off truncated).
