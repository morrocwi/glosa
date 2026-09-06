# LRS digest — Paper A: Before Meaning, Before Choice (GLS-2026-004)

Source runs: `lit new before-meaning-before-choice h1/h2/h3 --search-mode TARGETED_SEARCH` (2026-09-06), cross-vendor check `--vendor claude` (route:claude, independence_class I1 — same vendor, fresh headless session, not yet a true third-party I3 pass). Hypothesis text and falsifiers per `QUESTIONS.md`, itself sourced from the novelty-boundary review BBL-144 (`cpg_research_journal/research/society-justice-peace/master-river/LITREVIEW_2026-09-06_novelty_boundary.md`). H4 has a citations/rows skeleton on disk but no `litreview_manifest.yaml` and an empty dialogue table — it was **not run** in this pass and is excluded below except where noted.

Hypothesis selection remains human-owned (founder, Yaoharee Lahtee) per QUESTIONS.md framing. Nothing below selects a hypothesis; it stocks the dialogue table for that decision.

---

## H1 — Admission order (root gate)

Manifest: `h1/litreview_manifest.yaml` — accuracy_gate PASS, diversity_gate PASS, overall **PASS**. 14 cards (10 verified, 4 parked/record-only).

| card id | source | year | fetch status | route bearing | stance | what it would say against us (one line) |
|---|---|---|---|---|---|---|
| cite-bateson-1972-bmbc-h1-001 | Bateson, "Form, Substance and Difference" | 1972 | FETCHED (Polanyi Society mirror) | I1 | ORTHOGONAL | H1's four-gate decomposition may over-elaborate what Bateson treats as one primitive selection act. |
| cite-floridi-sep-semantic-info-bmbc-h1-002 | SEP, "Semantic Conceptions of Information" | live entry | FETCHED | I1 | ORTHOGONAL | If every semantic-info theory already orders syntactic before semantic, the ordering half of H1 is not different from the existing literature — the four-gate decomposition would need to be the differentiating element on its own. |
| cite-kolchinsky-wolpert-2018-bmbc-h1-003 | Kolchinsky & Wolpert, "Semantic information, autonomous agency..." | 2018 | FETCHED (arXiv 1806.08053) | I1 | **NO** | A physics-grounded two-layer order via one causal-necessity/viability criterion, no four named gates needed — Occam's razor challenge. |
| cite-sangiorgi-2009-bmbc-h1-004 | Sangiorgi, "On the origins of bisimulation and coinduction" | 2009 | FETCHED (author PDF) | I1 | ORTHOGONAL | Bisimulation's relational equivalence is already well-founded without an admission-order narrative. |
| cite-faccin-schaub-delvenne-2020-bmbc-h1-005 | Faccin, Schaub & Delvenne, lumpability (Buchholz 1994 treatment) | 2020 | FETCHED (arXiv 2005.00337) | I1 | ORTHOGONAL | Lumpability alone gives a precise dynamics-preservation gate without H1's other three gates or a provenance record. |
| cite-ravindran-barto-2004-bmbc-h1-006 | Ravindran & Barto, "Approximate Homomorphisms" | 2004 | FETCHED (UMass self-archive) | I1 | ORTHOGONAL | A rigorous quantified loss-bound already exists for non-exact MDP abstraction; H1's "loss gate" may be a rename. |
| cite-shalizi-crutchfield-2001-bmbc-h1-007 | Shalizi & Crutchfield, "Computational Mechanics" | 2001 | FETCHED (arXiv cond-mat/9907176) | I1 | ORTHOGONAL | Causal states/epsilon-machines already give a canonical minimal non-semantic construct without four named gates. |
| cite-tishby-pereira-bialek-1999-bmbc-h1-008 | Tishby, Pereira & Bialek, "The information bottleneck method" | 1999 | FETCHED (arXiv physics/0004057) | I1 | ORTHOGONAL | The rate-relevance tradeoff already formalizes a loss/relevance gate; H1's "loss gate" may restate it. |
| cite-readout-genesis-synthesis-2026-bmbc-h1-009 | Readout Genesis Standalone Synthesis (own lineage) | 2026 | FETCHED (Zenodo 21529456) | I1 | ORTHOGONAL (own) | Own-lineage; does not argue against itself — human must confirm it is not just relabeling Kolchinsky/Wolpert or lumpability. |
| cite-readout-condition-2026-bmbc-h1-010 | The Readout Condition (own lineage) | 2026 | FETCHED (Zenodo 22301318) | I1 | ORTHOGONAL (own) | Own-lineage; human must confirm Paper A's four gates actually implement this existence/attribution/disclosure norm. |
| cite-park-1981-bmbc-h1-parked-001 | Park, "Concurrency and automata on infinite sequences" | 1981 | NOT_FETCHED (paywalled Springer LNCS) | — | record-only | no open copy found |
| cite-kemeny-snell-1976-bmbc-h1-parked-002 | Kemeny & Snell, *Finite Markov Chains* | 1976 | NOT_FETCHED (paywalled monograph) | — | record-only | no open copy found |
| cite-giere-2006-bmbc-h1-parked-003 | Giere, *Scientific Perspectivism* | 2006 | NOT_FETCHED (paywalled monograph) | — | record-only | QUESTIONS.md itself flags as record-only |
| cite-massimi-2022-bmbc-h1-parked-004 | Massimi, *Perspectival Realism* | 2022 | NOT_FETCHED (OUP claimed-open, Cloudflare 403 twice) | — | record-only | no reachable open copy on this pass |

### 3 strongest challenges (H1)
1. **Kolchinsky & Wolpert 2018** (Interface Focus, arXiv:1806.08053) — abstract, sentence 5: *"We define semantic information as the syntactic information that a physical system has about its environment which is causally necessary for the system to maintain its own existence."* Already layers semantic on syntactic information via one causal-necessity/viability criterion — structurally adjacent to H1's admission order but with one criterion, not four gates.
2. **Faccin, Schaub & Delvenne 2020** (arXiv:2005.00337v2, Supplementary Material) — *"A Markov chain is said to be lumpable [50, 51] if we can aggregate its states xt such that the dynamics of the aggregated states yt is again a Markov chain."* A clean, independently-checkable dynamics-preservation gate on its own, no provenance record required.
3. **Ravindran & Barto 2004** (UMass self-archived PDF, Abstract) — *"We also present a result on bounding the loss resulting from this approximation."* A rigorous quantified loss-bounding result for non-exact abstraction, in isolation from H1's other three gates. (Tishby/Pereira/Bialek 1999's information-bottleneck abstract sentence is the same-strength runner-up for the same "loss gate" component.)

---

## H2 — Direction of derivation for meaning and experience

Manifest: `h2/litreview_manifest.yaml` — accuracy_gate PASS, diversity_gate PASS, overall **PASS**. 13 cards (8 verified, 5 parked/record-only).

| card id | source | year | fetch status | route bearing | stance | what it would say against us (one line) |
|---|---|---|---|---|---|---|
| cite-sep-phenomenology-h2-001 | SEP, "Phenomenology" | live entry | FETCHED | I1 | **NO** | Intentionality is presented as experience's own central, primitive structure — not built up after a non-semantic layer. |
| cite-zacks2007-eventperception-h2-002 | Zacks et al., event segmentation | 2007 | FETCHED (PMC2852534) | I1 | ORTHOGONAL | Event segmentation is reader-side, but the paper never states a semantic/non-semantic admission order. |
| cite-friston2010-fep-h2-004 | Friston, free-energy principle | 2010 | PAYWALLED_ABSTRACT_ONLY | I1 | ORTHOGONAL | Abstract alone cannot confirm/deny an admission order comparable to H2's. |
| cite-lindquist2006-language-emotion-h2-005 | Lindquist et al., language & emotion perception | 2006 | PAYWALLED_ABSTRACT_ONLY | I1 | ORTHOGONAL | If emotion-word accessibility measurably speeds/slows perception, semantic influence may reach into perception before a non-semantic layer finishes — live potential challenge, unconfirmed without full text. |
| cite-own-meaning-giving-h2-001 | Experience Is Meaning-Giving (own) | 2026 | FETCHED (Zenodo 22357744) | I1 | YES (own) | Own-lineage; cannot itself defeat H2, does not test it against an outside view. |
| cite-own-meaning-before-naming-h2-002 | Meaning Before Naming (own) | 2026 | FETCHED (Zenodo 22410666) | I1 | YES (own) | Own-lineage; restates H2 in the same vocabulary rather than testing it. |
| cite-own-human-lora-h2-003 | Experience Is the Human LoRA (own) | 2026 | FETCHED (Zenodo 21425420) | I1 | YES (own) | Own-lineage; supports the premise but is not independent evidence. |
| cite-own-readout-genesis-lens-h2-bmbc-001 | Readout Genesis retained-distinction lens (own, reused from potential-as-readout/h2) | 2026 | FETCHED (Zenodo 21529456) | I1 | YES (own) | Own-lineage root construct, not standing against outside literature. |
| cite-parr-pezzulo-friston2022-h2-003 | Parr, Pezzulo & Friston, *Active Inference* ch.4 | 2022 | FETCHED (real chapter text + manually confirmed passage) | parked — mechanical crossvendor re-check could not re-retrieve the chapter PDF via Wayback on repeated attempts | record-only | Wayback serving inconsistency, not a passage problem |
| cite-dipaolo-rohde-dejaegher2010-h2-006 | Di Paolo, Rohde & De Jaegher, "Horizons for the Enactive Mind" | 2010 | PAYWALLED_ABSTRACT_ONLY (OpenAlex) | parked | record-only | no full chapter text obtainable |
| cite-dejaegher-dipaolo2007-h2-007 | De Jaegher & Di Paolo, participatory sense-making | 2007 | NOT_FETCHED | parked | record-only | closed access everywhere checked (Unpaywall/OpenAlex/Crossref/Europe PMC), author site 404 |
| cite-thompson2007-mindinlife-h2-008 | Thompson, *Mind in Life* | 2007 | NOT_FETCHED (closed monograph) | parked | record-only | no OA mirror |
| cite-varela-thompson-rosch1991-h2-009 | Varela, Thompson & Rosch, *The Embodied Mind* | 1991 | NOT_FETCHED (closed monograph) | parked | record-only | no OA mirror |

### 3 strongest challenges (H2)
1. **SEP, "Phenomenology"** — opening paragraph of §1: *"The central structure of an experience is its intentionality, its being directed toward something, as it is an experience of or about some object."* Directly instantiates the account H2 says it reverses.
2. **Lindquist et al. 2006** (abstract, sentence 2): *"The authors predicted and found that the accessibility of emotion words influenced participants' speed or accuracy in perceiving facial behaviors depicting emotion."* A live potential challenge (semantic/naming reaching into perception) — unconfirmed pending full text.
3. Evidentiary gap, not a source: every fully-read YES stance for H2 is own-lineage; no independently-authored full-text source was obtained that tests H2's specific two-layer admission-order claim against outside literature. The De Jaegher & Di Paolo 2007 participatory-sense-making line (QUESTIONS.md's most central enactivist relative) is entirely unreachable on this pass.

---

## H3 — Live possibility between capability and choice; power before prohibition

Manifest: `h3/litreview_manifest.yaml` — accuracy_gate PASS, diversity_gate PASS, overall **PASS**. 12 cards (11 verified, 1 parked/record-only).

| card id | source | year | fetch status | route bearing | stance | what it would say against us (one line) |
|---|---|---|---|---|---|---|
| cite-galtung1969-potentialgap-bmbc-001 | Galtung, "Violence, Peace, and Peace Research" (potential-actual gap) | 1969 | FETCHED | I1 | ORTHOGONAL | Galtung's potential-actual gap already does the descriptive work; H3's narrower graded live-candidate subset is an addition Galtung neither makes nor needs. |
| cite-galtung1969-negpospeace-bmbc-002 | Galtung, negative/positive peace | 1969 | FETCHED | I1 | YES | Different unit of analysis (macro-structural peace vs. an actor's live-candidate options) — the parallel may be looser than the row suggests. |
| cite-galtung1990-culturalviolence-bmbc-003 | Galtung, "Cultural Violence" | 1990 | FETCHED | I1 | YES | Cultural violence legitimates existing violence but does not itself claim to act before any prohibition exists — H3's stronger claim goes beyond this passage. |
| cite-pettit-globalrepublican-bmbc-004 | Pettit, "The Globalized Republican Ideal" | n.d. (EUI MWP) | FETCHED | I1 | YES | Supplies the concept (robustness) but no method — no counterfactual measurement + provenance + corrigibility interface; that gap is exactly H3's claimed contribution. |
| cite-foucault1982-bmbc-005 | Foucault, "The Subject and Power" | 1982 | FETCHED | I1 | YES | Already names H3's exact mechanism (structuring the possible field of action); if read as including a graded live-candidate distinction, what H3 would add is only the operational interface, not the phenomenon itself — which H3 itself concedes. |
| cite-nussbaum2011-senquote-bmbc-006 | Nussbaum, *Creating Capabilities* (quoting Sen 1999) | 2011 | FETCHED | I1 | **NO** | "Feasible for her to achieve" could implicitly already exclude merely-formal options given conversion factors — narrowing feasibility toward H3's live-possibility field without naming it. |
| cite-robeyns2017-bmbc-007 | Robeyns, *Wellbeing, Freedom and Social Justice* | 2017 | FETCHED (OpenEdition, CC BY) | I1 | **NO** | "Real freedoms" may already exclude the formally-possible-but-unconsiderable — similar filtering work to H3's interface, without naming it. |
| cite-kabeer1999-bmbc-008 | Kabeer, "Resources, Agency, Achievements" | 1999 | FETCHED (abstract) | I1 | ORTHOGONAL | Pitched at a general-capacity granularity, different from H3's per-action live-possibility field. |
| cite-chemero2003-bmbc-010 | Chemero, "An Outline of a Theory of Affordances" | 2003 | PAYWALLED_ABSTRACT_ONLY | I1 | ORTHOGONAL | Relational reframing of affordances might implicitly narrow toward H3's field, but the abstract alone does not show that. |
| cite-rietveldkiverstein2014-bmbc-011 | Rietveld & Kiverstein, "A Rich Landscape of Affordances" | 2014 | PAYWALLED_ABSTRACT_ONLY | I1 | ORTHOGONAL | Named directly in H3's own falsifier clause; on the abstract alone it broadens (not narrows) feasibility — falsifier not met on this evidence, but paywalled full text was not fetched. |
| cite-fricker2007-sep-bmbc-012 | Fricker, epistemic injustice, via SEP "Feminist Epistemology..." | 2007 | FETCHED | I1 | YES | Narrower, epistemic-specific (credibility discounting in uptake) rather than a general action-oriented live-possibility field — analogy across domains may overstate the match. |
| cite-gibson1979-affordances-bmbc-009 | Gibson, *The Ecological Approach to Visual Perception* | 1979 | FETCHED, METADATA_OK | parked | record-only | claim-match not run to VERIFIED in this pass |

### 3 strongest challenges (H3)
1. **Foucault 1982** (Critical Inquiry 8(4), p.790): *"To govern, in this sense, is to structure the possible field of action of others."* Names H3's exact mechanism; H3's own falsifier is close to met at the concept level — H3's claimed addition is only the operational interface (counterfactual measurement + provenance + corrigibility), not the phenomenon.
2. **Pettit**, "The Globalized Republican Ideal" (EUI MWP master-class paper, p.3): *"you do not enjoy freedom as non-domination or independence just by virtue of actually escaping interference; it must also be that you would not suffer interference even if you had wished to act otherwise..."* Already supplies the counterfactual-robustness concept H3 needs to distinguish "observed calm" from a genuinely open channel — without an empirical measurement method.
3. **Nussbaum 2011 quoting Sen 1999** (Ch.2, p.20): *"a person's 'capability' refers to the alternative combinations of functionings that are feasible for her to achieve. Capability is thus a kind of freedom..."* Names the whole feasible set as the unit of analysis with no further live-candidate split — the capability-theory rebuttal is that "feasible" may already implicitly filter toward something like H3's field. Rietveld & Kiverstein 2014 is the named-in-falsifier runner-up, unread past its abstract (paywalled).

---

## Same/different/cited ledger vs. the novelty-boundary review (BBL-144)

QUESTIONS.md names the relatives BBL-144 flagged per hypothesis. Status after this pass:

| Hypothesis | Relative named in BBL-144 | Now backed by a verified fetched passage? | Disposition |
|---|---|---|---|
| H1 | Bateson 1972 | yes | different — ORTHOGONAL, ties selection to one primitive act, not H1's four gates |
| H1 | Floridi / SEP semantic-info | yes | different — ORTHOGONAL, states the two-layer order without H1's four named gates |
| H1 | Kolchinsky & Wolpert 2018 | yes | **near-neighbor, cited as strongest challenge** — same two-layer order, one criterion vs. H1's four gates; human same/different call still open |
| H1 | Sangiorgi 2009 (bisimulation survey; stands in for Park 1981/Milner 1989) | yes | different — ORTHOGONAL, no admission-order narrative |
| H1 | Kemeny & Snell 1976 (lumpability origin) | no — record-only, paywalled monograph, use Faccin/Schaub/Delvenne 2020 as the fetched modern treatment instead | record-only |
| H1 | Faccin, Schaub & Delvenne 2020 (modern lumpability) | yes | different but **strong single-gate match** for the dynamics-preservation gate alone |
| H1 | Ravindran & Barto 2004 (MDP homomorphism) | yes | different but **strong single-gate match** for the loss gate alone |
| H1 | Shalizi & Crutchfield 2001 | yes | different — ORTHOGONAL |
| H1 | Tishby, Pereira & Bialek 1999 | yes | different but **strong single-gate match** for the loss gate alone |
| H1 | Giere 2006 | no — record-only per QUESTIONS.md's own flag | record-only |
| H1 | Massimi 2022 | no — OUP-claimed-open but Cloudflare 403 on direct fetch, twice | record-only |
| H2 | SEP "Phenomenology" | yes | **cited as strongest challenge** — NO, states H2's reversed order does not hold for phenomenology's own starting point |
| H2 | Thompson 2007 *Mind in Life* | no — record-only, closed monograph | record-only |
| H2 | Di Paolo, Rohde & De Jaegher 2010 | yes (abstract only) | different — ORTHOGONAL on abstract; record-only for full-text depth |
| H2 | De Jaegher & Di Paolo 2007 (participatory sense-making) | no — closed everywhere checked | record-only, biggest evidence gap per QUESTIONS.md's own framing |
| H2 | Parr, Pezzulo & Friston 2022 (Active Inference) | yes (chapter text and passage manually confirmed) but parked for the mechanical crossvendor re-check | record-only pending a stable re-fetch |
| H2 | Zacks et al. 2007 (event segmentation) | yes | different — ORTHOGONAL |
| H2 | Lindquist et al. 2006 | yes (abstract only) | different on this evidence, flagged as a live potential challenge pending full text |
| H3 | Gibson 1979 | yes (fetched) but not re-verified to claim_match this pass | record-only |
| H3 | Chemero 2003 / Rietveld & Kiverstein 2014 (rich landscape of affordances) | abstract only for both | different on abstract evidence; Rietveld & Kiverstein is H3's own named falsifier candidate and remains open pending full text |
| H3 | Sen 1999 / Nussbaum 2011 / Robeyns 2017 / Kabeer 1999 | yes, all four fetched | Nussbaum and Robeyns are **cited as challenges** (NO); Kabeer is ORTHOGONAL (granularity mismatch) |
| H3 | Galtung 1969 / 1990 | yes, all three passages fetched | mixed YES/ORTHOGONAL — H3's addition (counterfactual measurement + provenance + corrigibility) is not in Galtung's definitions |
| H3 | Foucault 1982 | yes | **cited as strongest challenge** — names H3's exact mechanism at the concept level |
| H3 | Pettit | yes | **cited as strongest challenge** — supplies the concept, not the method |
| H3 | Fricker 2007 | yes (via SEP) | different — narrower epistemic-specific mechanism, cross-domain analogy may overstate the match |
| H3 | Mahmood 2001 | not attempted this pass | not in current card set — open item |

---

## What Paper A must say differently as a result

1. **H1's abstract/intro cannot claim the two-layer ordering itself as what distinguishes it.** Kolchinsky & Wolpert 2018 already gives a physics-grounded syntactic-then-semantic order via one causal-necessity criterion — same order, not different. Paper A's actual claim must be narrowed to: the specific **four-way decomposition** (reader, translation, loss, dynamics-preservation) **plus a provenance record**, not "an admission order exists" — and it must explicitly address why one criterion (Kolchinsky & Wolpert) is insufficient where four gates are needed.
2. **H1's "loss gate" and "dynamics-preservation gate" are not new machinery** — they map onto existing, independently-citable constructs (information bottleneck / MDP approximate-homomorphism bounds for loss; lumpability for dynamics-preservation). Paper A should cite these as same-component precedents rather than presenting the gates as original, and state what the four-gate bundling adds beyond the sum of these single-gate results (the candidate answer, per this review, is the provenance/attribution/disclosure record — Paper A must actually demonstrate that, not merely assert it).
3. **H2 cannot be asserted against phenomenology without addressing SEP's own framing directly.** The SEP entry states intentionality as experience's own central structure, not a downstream derivation — this is a live disagreement, not a gap in the literature H2 can route around. Paper A needs either a direct rebuttal of the intentionality-is-primitive reading or an explicit scope restriction (e.g., "this account targets pre-reflective/non-intentional retained structure, not experience-as-such").
4. **H2 currently has no independent (non-own-lineage) full-text confirmation.** Every fully-read YES stance is self-sourced. Paper A must either (a) flag this honestly as an open evidentiary gap in its own tier language, not present the own-lineage citations as external support, or (b) obtain the De Jaegher & Di Paolo 2007 full text (the QUESTIONS.md-named central enactivist relative, currently entirely unreachable) before claiming any literature-level confirmation.
5. **H3's own falsifier is close to being met at the concept level by Foucault 1982 and Pettit.** Paper A must state its contribution as strictly the **operational interface** (counterfactual measurement + provenance + actor ownership + corrigibility) over an already-named phenomenon (Foucault's field-structuring, Pettit's robustness-as-non-domination) — not as discovering the phenomenon itself. This is consistent with H3's own text ("the contribution is the interface, not the phenomenon") but the literature now makes that restriction load-bearing, not optional.
6. **H3's capability-theory relatives (Nussbaum/Robeyns) are cited as live rebuttals, not neutral background.** Paper A cannot present "feasible"/"real freedoms" as unable to capture the live-candidate distinction without addressing the capability theorists' own likely reply (conversion-factor filtering may already do similar work). Either show a concrete case where conversion-factor-adjusted feasibility and H3's live-candidate field diverge, or narrow H3's claim to the measurement/provenance interface alone (per point 5).
7. **Every parked/record-only card must stay flagged as such in Paper A's own citation apparatus** (fetch_status NOT_FETCHED or PAYWALLED_ABSTRACT_ONLY) — none of Park 1981, Kemeny & Snell 1976, Giere 2006, Massimi 2022, Thompson 2007, Varela/Thompson/Rosch 1991, De Jaegher & Di Paolo 2007, or Gibson 1979 (h3, unverified this pass) may be cited in Paper A as if their full text had been read; only the abstract-level or metadata-level claim actually verified above may be used.
8. **H4 has no literature-review pass yet** (skeleton only, no manifest, empty dialogue table) — Paper A cannot draw on H4 relatives (Glickman & Sharot 2024, Bastani et al. 2025, Risko & Gilbert 2016) until that hypothesis gets its own LRS run.

---

## Counts

- Cards total (H1+H2+H3): **39** (14 + 13 + 12)
- Verified: **29** (10 + 8 + 11)
- Parked / record-only: **10** (4 + 5 + 1)
- Manifests: `h1/litreview_manifest.yaml` PASS, `h2/litreview_manifest.yaml` PASS, `h3/litreview_manifest.yaml` PASS
- H4: not run this pass (excluded from the totals above)
