# knowledge/harvest_v0.3 — full card index (K1-index)

All 324 knowledge cards under `knowledge/harvest_v0.3/`, one row per `kc-*.yaml` file, generated from the cards' own `id`/`kind`/`title`/`base_relation`/`glosa_use`/`source` fields — this file is a rollup, it does not re-derive or restate any card's tier or judgment. Per-hub tables with the same columns already exist at `knowledge/harvest_v0.3/<hub>/INDEX.md`; this file is the flat, all-hubs index named by `ROADMAP_v0.3.md` step S6 and `design/REPO_SPEC_v0.6_PATCH.md` §2. Full narrative discussion per hub: `knowledge/harvest_v0.3/KNOWLEDGE_STATUS_v0.3.md`. Regenerate with `python3 docs/gen_kg_svg.py` (also writes `docs/kg_v0.3.json`/`docs/kg_v0.3.svg` from the same card set) — never hand-edit this table.

`base_relation`: `holds` | `refined_by_later_work` | `superseded` | `outdated` | `open` (a card judged against the `base` hub's lens/spine texts; see `knowledge/harvest_v0.3/base/`). `glosa_use`: `adopt` (cite/use as-is) | `adapt` (use with reformulation) | `already_in_glosa` | `skip`.

## Counts by hub

| hub | n cards |
|---|---|
| ph | 116 |
| ep | 52 |
| base | 42 |
| aihp | 33 |
| ai | 27 |
| he | 19 |
| islam | 16 |
| se | 12 |
| tourism | 7 |
| **total** | **324** |

## All cards

| hub | id | kind | title | base_relation | glosa_use | source |
|---|---|---|---|---|---|---|
| ai | kc-ai-001 | definition | The Readout Condition — Existence/Attribution/Disclosure norm | holds | adopt | sources/READOUT_CONDITION_2026-08.txt |
| ai | kc-ai-002 | method | Readout Condition — defeater-routing and the identification ladder | refined_by_later_work | adapt | sources/READOUT_CONDITION_2026-08.txt |
| ai | kc-ai-003 | definition | Possession–Constitution Collapse and knower fetishism | holds | adopt | sources/WRITTEN_BY_AI_STILL_TRUE_v6.txt |
| ai | kc-ai-004 | rule | Two constraints replacing knower-fetishism: channel over face | refined_by_later_work | adopt | sources/WRITTEN_BY_AI_STILL_TRUE_v6.txt |
| ai | kc-ai-005 | method | glosa — methodology answering five questions per claim | holds | already_in_glosa | registry/zenodo_all_records.json |
| ai | kc-ai-006 | claim | Claim card as substitute for institutional certification (three propositions) | open | already_in_glosa | registry/zenodo_all_records.json |
| ai | kc-ai-007 | claim | Controlled epistemic chain reaction and the k_epi multiplication factor | refined_by_later_work | adapt | registry/zenodo_all_records.json |
| ai | kc-ai-008 | tool | Blackbox Log — append-only verbatim positional record | holds | adopt | registry/zenodo_all_records.json |
| ai | kc-ai-009 | definition | Bounded dynamic semantic mobility for hypothesis generation | refined_by_later_work | adapt | registry/zenodo_all_records.json |
| ai | kc-ai-010 | method | MOCA — Readout Condition applied to mission-attributable sacrifice | refined_by_later_work | adapt | registry/zenodo_all_records.json |
| ai | kc-ai-011 | definition | Standalone Scholar — dual-track architecture (synthetic plurality vs validation) | refined_by_later_work | adopt | registry/zenodo_all_records.json |
| ai | kc-ai-012 | claim | Human LoRA Factorization Thesis — bounded-rank experiential update | holds | adopt | registry/zenodo_all_records.json |
| ai | kc-ai-013 | claim | AI expands potential only under disciplined revision (constraint-first epistemology) | holds | adopt | registry/zenodo_all_records.json |
| ai | kc-ai-014 | claim | Deep Authorship and Causal-Structural Alignment (replaces naked correspondence) | holds | adapt | registry/zenodo_all_records.json |
| ai | kc-ai-015 | claim | Knowledge history as succession of authorized interpretive agencies | holds | adopt | registry/zenodo_all_records.json |
| ai | kc-ai-016 | claim | NIDA slides — forgetting one's status as chooser under AI mediation | holds | skip | registry/zenodo_all_records.json |
| ai | kc-ai-017 | definition | Knowledge as stabilized translation under bounded observation | holds | adopt | registry/zenodo_all_records.json |
| ai | kc-ai-018 | claim | Structural law: learning shifts from accumulation to discrimination under abundance | refined_by_later_work | adapt | registry/zenodo_all_records.json |
| ai | kc-ai-019 | claim | Information access vs context access — AI does not reconstruct situational conditions | holds | adopt | registry/zenodo_all_records.json |
| ai | kc-ai-020 | method | Admissibility-first AI-coached planning with explicit no-go conditions | refined_by_later_work | adapt | registry/zenodo_all_records.json |
| ai | kc-ai-021 | tool | CMG-F — diagnostic, non-optimizing structural graph fingerprinting | holds | adapt | registry/zenodo_all_records.json |
| ai | kc-ai-022 | claim | Causal Guardrails — pre-linguistic admissibility checks against hallucination/sycophancy | refined_by_later_work | adopt | registry/zenodo_all_records.json |
| ai | kc-ai-023 | tool | SANA runtime — bounded, faith-safe, non-clinical crisis companion | open | skip | registry/zenodo_all_records.json |
| ai | kc-ai-024 | claim | Neurobiological mismatch between education design and adolescent reward system | open | skip | registry/zenodo_all_records.json |
| ai | kc-ai-025 | claim | Language as cognitive infrastructure — Elective Connectivity mechanism | open | skip | registry/zenodo_all_records.json |
| ai | kc-ai-026 | claim | Dialogue as a mirror of thought — sincerity vs haste determines its epistemic yield | open | skip | registry/zenodo_all_records.json |
| ai | kc-ai-027 | claim | Language bridge — LLMs as accelerants of human-capital-to-social-capital conversion | superseded | skip | registry/zenodo_all_records.json |
| aihp | kc-aihp-001 | method | glosa's own paper applies claim-card discipline reflexively to itself (K0, tier Dr) | holds | already_in_glosa | 10.5281/zenodo.22307843 |
| aihp | kc-aihp-002 | claim | Reflexive finding: glosa's own evidence is independence class I0, hence K0 not K1 | holds | already_in_glosa | 10.5281/zenodo.22307843 |
| aihp | kc-aihp-003 | claim | Three falsifiable propositions (H1 design, H2 conceptual, H3 empirical) on claim-card discipline | holds | already_in_glosa | 10.5281/zenodo.22307841 |
| aihp | kc-aihp-004 | definition | 'Problem before observation' spine node: RA = OA(W;ΠA) ≠ W as the first node, not 'Reality→' | holds | adopt | 10.5281/zenodo.22307841 |
| aihp | kc-aihp-005 | method | Controlled epistemic chain reaction: human retains the question, AI recursively decomposes and gates candidates | holds | adapt | 10.5281/zenodo.22308072 |
| aihp | kc-aihp-006 | tool | Shared evidence registry (Claim Registry E01-E25) for the 4-paper Bounded Knower programme, tier-honest 'Observed' | holds | adapt | 10.5281/zenodo.22308066 |
| aihp | kc-aihp-007 | claim | Blackbox Log entry BBL-2026-09-04-024: knowledge disputes outside institutions are usually about legitimacy, not truth | holds | already_in_glosa | 10.5281/zenodo.22307891 |
| aihp | kc-aihp-008 | claim | Before Evidence Can Decide: candidate-set formation and discovery routing precede evidential adjudication (agenda paper, [Open]) | open | skip | 10.5281/zenodo.22307564 |
| aihp | kc-aihp-009 | claim | Knowledge Topology: discovery time and direction as a readout theory of the first passage to a usable hypothesis | open | skip | 10.5281/zenodo.22307561 |
| aihp | kc-aihp-010 | method | Imagination as bounded dynamic semantic mobility: a readout-native architecture for hypothesis generation | holds | adapt | 10.5281/zenodo.22307148 |
| aihp | kc-aihp-011 | rule | The Readout Condition: Existence, Attribution, Disclosure — three principles governing claim-level distinctions | holds | adopt | 10.5281/zenodo.22301318 |
| aihp | kc-aihp-012 | method | Identification ladder + typed provenance DAG + defeater-routing result | holds | adopt | 10.5281/zenodo.22301318 |
| aihp | kc-aihp-013 | claim | Possession–Constitution Collapse and 'knower fetishism': epistemic value does not require a human-like knower | holds | adopt | 10.5281/zenodo.22301202 |
| aihp | kc-aihp-014 | rule | Two constraints replacing knower-fetishism: provenance-only channel, and metadata must not be identified with the role it proxies | holds | adopt | 10.5281/zenodo.22301202 |
| aihp | kc-aihp-015 | claim | NIDA national-conference slides: AI-mediated society risks the human forgetting their own status as chooser and responsibility-bearer | refined_by_later_work | skip | 10.5281/zenodo.22302410 |
| aihp | kc-aihp-016 | claim | NIDA national-conference slides (duplicate deposit): AI-mediated civilization of knowledge and human responsibility | refined_by_later_work | skip | 10.5281/zenodo.22301886 |
| aihp | kc-aihp-017 | method | Standalone Scholar: dual-track architecture separating AI-assisted formation from independent human friction | holds | already_in_glosa | 10.5281/zenodo.22163849 |
| aihp | kc-aihp-018 | rule | Global-search bias correction: every socially relevant flagship needs both a global conversion route and a local one | holds | adapt | 10.5281/zenodo.22163849 |
| aihp | kc-aihp-019 | definition | Information Epistemic Foundation: knowledge as an auditable status of a claim, not a possession of a knower | holds | adopt | 10.5281/zenodo.21529456 |
| aihp | kc-aihp-020 | method | Meta-readout governance operator: readout-of-readout composition with finite retention | holds | adapt | 10.5281/zenodo.21529456 |
| aihp | kc-aihp-021 | claim | Human LoRA Factorization Thesis: durable experiential change is rank-bounded by a finite readout bottleneck | holds | skip | 10.5281/zenodo.21425420 |
| aihp | kc-aihp-022 | claim | Agency-Horizon Theorem: every agent under the framework's axioms exhibits five information-horizon properties | holds | skip | 10.5281/zenodo.19640361 |
| aihp | kc-aihp-023 | claim | Constraint-first epistemology: AI expands human potential only when machine-mediated dissonance becomes disciplined revision | holds | adopt | 10.5281/zenodo.19215748 |
| aihp | kc-aihp-024 | claim | Non-zero Kantian floor: finite cognition entails a structural, non-metaphysical floor of mediation | holds | skip | 10.5281/zenodo.19205869 |
| aihp | kc-aihp-025 | claim | Truth as Causal-Structural Alignment, not naked correspondence; the translation gap is the condition of agency, not a defect | holds | skip | 10.5281/zenodo.19176260 |
| aihp | kc-aihp-026 | claim | Knowledge crises are authority crises: the history of knowledge is the history of changing interpretive authority | holds | adopt | 10.5281/zenodo.18943971 |
| aihp | kc-aihp-027 | definition | Knowledge as stabilized translation under bounded observation, not direct access | holds | skip | 10.5281/zenodo.18925129 |
| aihp | kc-aihp-028 | claim | Structural law of epistemic stabilization: beyond a threshold of generative exposure, learning shifts from accumulation to discrimination | holds | skip | 10.5281/zenodo.18711408 |
| aihp | kc-aihp-029 | claim | AI expands information access without reconstructing full event-specific context | holds | skip | 10.5281/zenodo.18517054 |
| aihp | kc-aihp-030 | claim | AI-cognitive interaction and youth potential: reflective dialogue as a mechanism, pre-readout vocabulary | refined_by_later_work | skip | 10.5281/zenodo.22308448 |
| aihp | kc-aihp-031 | claim | Operational Linguistic Wisdom: language as cognitive infrastructure activating linguistic capital via LLMs, pre-readout vocabulary | refined_by_later_work | skip | 10.5281/zenodo.22308446 |
| aihp | kc-aihp-032 | claim | Dialogue as mirror of thought: sincerity/attentiveness produce wisdom, haste/bias produce epistemic distortion | refined_by_later_work | skip | 10.5281/zenodo.22308451 |
| aihp | kc-aihp-033 | claim | The language bridge: human capital converts to social capital only by crossing disciplinary/professional dialects | refined_by_later_work | skip | 10.5281/zenodo.17280546 |
| base | kc-base-001 | definition | Readout-not-truth (founding refusal) | holds | adopt | readout_universe/philosophy.md |
| base | kc-base-002 | claim | Q1 — No pre-existing magnitude | holds | adopt | readout_universe/philosophy.md |
| base | kc-base-003 | claim | Q2 — Quantity as projection | holds | adopt | readout_universe/philosophy.md |
| base | kc-base-004 | rule | Q3 — Identity by role, not by number (equal-number fallacy) | holds | adopt | readout_universe/philosophy.md |
| base | kc-base-005 | claim | Truth re-read as tracking, not correspondence | holds | adopt | readout_universe/philosophy.md |
| base | kc-base-006 | claim | no_decoder_recovers_state theorem (non-injective readout) | holds | adopt | readout_universe/philosophy.md |
| base | kc-base-007 | definition | Six-tier discipline (never collapsed) | holds | already_in_glosa | readout_universe/philosophy.md |
| base | kc-base-008 | rule | Fail-Able Gate Law (Type-P vs Type-U) | holds | adopt | readout_universe/philosophy.md |
| base | kc-base-009 | definition | δ_R — the one primitive (retained distinction) | holds | adopt | readout_universe/philosophy.md |
| base | kc-base-010 | rule | RD1–RD9 — the arithmetic genome | holds | skip | readout_universe/logic.md |
| base | kc-base-011 | definition | L_R := D_W − W (the one derived link) | holds | skip | readout_universe/philosophy.md |
| base | kc-base-012 | claim | L_R forced by three properties of δ_R's own meaning | holds | skip | readout_universe/philosophy.md |
| base | kc-base-013 | method | Witness table ruling out rival operators to L_R | holds | skip | readout_universe/philosophy.md |
| base | kc-base-014 | claim | The one-line chain: δ_R → L_R → per-agency readout (N2) | holds | adopt | readout_universe/philosophy.md |
| base | kc-base-015 | definition | Discrete number ladder δ_R → D → ℤ → ℚ → ℝ | holds | adapt | readout_universe/philosophy.md |
| base | kc-base-016 | rule | Injected-infinity/zero taxonomy (I1–I4, Z1–Z4) | holds | adopt | readout_universe/logic.md |
| base | kc-base-017 | rule | Operator-grounding clause: + − × ÷ ∂ ∇ = < are retained-information operations | holds | adapt | readout_universe/philosophy.md |
| base | kc-base-018 | rule | Contaminated-concept → discrete-replacement table | holds | adopt | readout_universe/logic.md |
| base | kc-base-019 | method | Pre-write CHECKLIST (5 steps, contaminated-concept gate) | holds | adapt | readout_universe/logic.md |
| base | kc-base-020 | claim | Mother equation — the record is a translation, never the truth itself | holds | adopt | readout_universe/logic.md |
| base | kc-base-021 | claim | Same-shaped formula, three different tiers — not silently reconciled | holds | adopt | readout_universe/logic.md |
| base | kc-base-022 | definition | The trunk equation (EQ-015) | holds | skip | readout_universe/logic.md |
| base | kc-base-023 | definition | Epistemic Nuclear Core N1–N5 (domain-independent) | holds | adapt | readout_universe/logic.md |
| base | kc-base-024 | method | Three Epistemic Scalars and the DECIDE/ABSTAIN/ESCALATE verdict gate | holds | adapt | readout_universe/logic.md |
| base | kc-base-025 | rule | What this system explicitly does NOT claim | holds | adopt | readout_universe/philosophy.md |
| base | kc-base-026 | definition | RAR A1–A8 — logic of retention | holds | adapt | readout_universe/logic.md |
| base | kc-base-027 | definition | Bounded knower framing | holds | adopt | readout_universe/philosophy.md |
| base | kc-base-028 | definition | τ_c > 0 — persistence axiom, mass as a readout of τ_c | holds | skip | readout_genesis/READOUT_GENESIS_CORE.md |
| base | kc-base-029 | definition | E00.1–E00.7 — the primordial root axioms | holds | adapt | readout_genesis/READOUT_GENESIS_CORE.md |
| base | kc-base-030 | method | Root-to-Trunk Progression (P0 → ... → Universal Spine PDE) | holds | skip | readout_genesis/READOUT_GENESIS_CORE.md |
| base | kc-base-031 | rule | What Part I does not yet claim (bounded-scope discipline) | holds | adopt | readout_genesis/READOUT_GENESIS_CORE.md |
| base | kc-base-032 | rule | Doctrine reminder: readout-not-truth, symbols are finite discrete computable objects | holds | adopt | readout_genesis/READOUT_GENESIS_CORE.md |
| base | kc-base-033 | definition | MQ.08 — discrete stepper (deepest operational equation) | holds | skip | readout_genesis/READOUT_GENESIS_CORE.md |
| base | kc-base-034 | method | Term-by-term honest tier table (II.6) | holds | adopt | readout_genesis/READOUT_GENESIS_CORE.md |
| base | kc-base-035 | rule | Bounded-Judge Law (independent adversarial review requirement) | holds | already_in_glosa | readout_universe/philosophy.md |
| base | kc-base-036 | claim | Agrippa's trilemma applied to the tier system itself | holds | adopt | readout_universe/philosophy.md |
| base | kc-base-037 | claim | Case study — the tier discipline catching itself mid-flight (EQ-069–071 retraction) | holds | adopt | readout_universe/philosophy.md |
| base | kc-base-038 | method | Verdict-class vocabulary — DERIVED/FORCED/DEFINITIONAL-RELABEL/POSITED/BORROWED-SCALE/OPEN | holds | adopt | readout_universe/philosophy.md |
| base | kc-base-039 | claim | Falsifiable claims table (C1–C7) and its own 'We do NOT claim' | holds | adopt | readout_universe/claims.md |
| base | kc-base-040 | claim | Sorites Paradox — the one node meeting the corpus's own strict three-file binding | holds | adopt | readout_universe/paradoxes.md |
| base | kc-base-041 | claim | Retraction discipline worked example — AP21/scope_correction | holds | adopt | readout_universe/scope_correction.md |
| base | kc-base-042 | definition | README Principles — Position, Lens Law, tier discipline, philosophy-leads | holds | adapt | readout_universe/README.md |
| ep | kc-ep-001 | claim | Dialogue as reflective interlocutor (human-AI) | holds | adapt | 10.5281/zenodo.22308451 |
| ep | kc-ep-002 | claim | The language bridge as human-to-social-capital conversion | holds | skip | 10.5281/zenodo.17280546 |
| ep | kc-ep-003 | method | Operational Linguistic Wisdom: three-stage activation mechanism | holds | skip | 10.5281/zenodo.22308446 |
| ep | kc-ep-004 | claim | Reflective Note: verbatim-preserved ethnographic self-observation | refined_by_later_work | adapt | 10.5281/zenodo.17341231 |
| ep | kc-ep-005 | claim | Infinity as transcendental ground of meaning (contested vs. readout-not-truth) | open | skip | 10.5281/zenodo.18085092 |
| ep | kc-ep-006 | method | Constructible ordering from a primitive step relation (precursor) | refined_by_later_work | skip | 10.5281/zenodo.18133010 |
| ep | kc-ep-007 | method | Causal Calculus: primitive aggregation under finite causal access | refined_by_later_work | skip | 10.5281/zenodo.18164015 |
| ep | kc-ep-008 | method | Causal Guardrails: pre-linguistic admissibility checks for LLMs | holds | adapt | 10.5281/zenodo.18176092 |
| ep | kc-ep-009 | claim | Event-specific context vs. interpretive context in AI-mediated meaning access | holds | skip | 10.5281/zenodo.18517054 |
| ep | kc-ep-010 | claim | Learning under generative abundance: a structural regime shift | holds | adapt | 10.5281/zenodo.18711408 |
| ep | kc-ep-011 | claim | Invariance as condition of same-world discourse | refined_by_later_work | skip | 10.5281/zenodo.18798732 |
| ep | kc-ep-012 | method | CMP Knowledge Stability Theorem: three induction puzzles as one structural condition | holds | adapt | 10.5281/zenodo.18870302 |
| ep | kc-ep-013 | claim | Knowledge as stabilization of representation under admissible variation | holds | adapt | 10.5281/zenodo.18907015 |
| ep | kc-ep-014 | claim | Knowledge as stabilized translation under bounded observation | holds | adopt | 10.5281/zenodo.18925129 |
| ep | kc-ep-015 | claim | Judicial neutrality as institutional achievement, not visual sameness | holds | skip | 10.5281/zenodo.18918275 |
| ep | kc-ep-016 | claim | The civilization of knowledge as a history of interpretive authority | holds | adopt | 10.5281/zenodo.18943971 |
| ep | kc-ep-017 | claim | Causal Qualia: phenomenal interior as bounded causal organization, not brute privacy | holds | skip | 10.5281/zenodo.18968098 |
| ep | kc-ep-018 | method | Beyond Halal Labels: premature category stabilization in Muslim-friendly tourism | open | skip | 10.5281/zenodo.19059720 |
| ep | kc-ep-019 | method | Three Layers, One Moon: PCS applied to hilal (crescent-sighting) disagreement | open | skip | 10.5281/zenodo.19124963 |
| ep | kc-ep-020 | method | PCS as a scale-invariant mechanism of cultural failure | open | skip | 10.5281/zenodo.19115417 |
| ep | kc-ep-021 | claim | Constraint-first epistemology: a non-zero floor of mediation | holds | adopt | 10.5281/zenodo.19205869 |
| ep | kc-ep-022 | definition | สัจจะสัมพันธ์ (Relational Truth) — Thai restatement | holds | already_in_glosa | 10.5281/zenodo.19183837 |
| ep | kc-ep-023 | claim | Deep Authorship and Causal-Structural Alignment: beyond free-will misframing | holds | adopt | 10.5281/zenodo.19176260 |
| ep | kc-ep-024 | claim | Relational Alethic Realism: truth as disciplined answerability, not transparency | holds | adopt | 10.5281/zenodo.19209662 |
| ep | kc-ep-025 | claim | AI expands human potential only via disciplined revision under constraint | holds | adopt | 10.5281/zenodo.19215748 |
| ep | kc-ep-026 | definition | θ(E): relational invariance without intrinsic nature | holds | adopt | 10.5281/zenodo.19474326 |
| ep | kc-ep-027 | definition | Relational Alethic Realism as metaphysics-first reconstruction (book) | holds | adopt | 10.5281/zenodo.19537197 |
| ep | kc-ep-028 | method | Mind as Information Horizon: telegraph equation to expertise on a discrete causal graph | refined_by_later_work | skip | 10.5281/zenodo.19640361 |
| ep | kc-ep-029 | claim | Catuskoti-on-Catuskoti: what survives Nāgārjuna's self-applied fourfold negation | holds | skip | 10.5281/zenodo.20035321 |
| ep | kc-ep-030 | claim | Dependent Order, Directed Selection, Dependent Identity (Ash'arī theology) | open | skip | 10.5281/zenodo.19951961 |
| ep | kc-ep-031 | claim | The explanatory insufficiency of randomness | holds | skip | 10.5281/zenodo.20473230 |
| ep | kc-ep-032 | claim | Objective chance is not explanatorily primitive; modal difference is prior | holds | skip | 10.5281/zenodo.20537309 |
| ep | kc-ep-033 | method | Experience Is the Human LoRA: readout-retention theory of selective model change | holds | adopt | 10.5281/zenodo.21425420 |
| ep | kc-ep-034 | claim | The Architecture of Faqr (five registers of creaturely dependence) | open | skip | 10.5281/zenodo.21439275 |
| ep | kc-ep-035 | definition | Readout Genesis Standalone Synthesis: typed belief layer and meta-readout governance | holds | adopt | 10.5281/zenodo.21529456 |
| ep | kc-ep-036 | method | The Declaration Bound: bit-accurate retained-state separation for deferred spectral queries | holds | adopt | 10.5281/zenodo.21634023 |
| ep | kc-ep-037 | definition | What a zero readout certifies: zero as the failure locus of retained distinction | holds | adopt | 10.5281/zenodo.21665100 |
| ep | kc-ep-038 | claim | Epistemic hardening: asymmetric revisability in Muslim knowledge regimes | holds | adopt | 10.5281/zenodo.22129490 |
| ep | kc-ep-039 | claim | AI and the civilization of knowledge (NIDA 2026 slides, v1) | holds | already_in_glosa | 10.5281/zenodo.22302410 |
| ep | kc-ep-040 | claim | AI and the civilization of knowledge (NIDA 2026 slides, v2) | holds | already_in_glosa | 10.5281/zenodo.22301886 |
| ep | kc-ep-041 | method | The Standalone Scholar: dual-track architecture for AI-native scholarship | holds | adopt | 10.5281/zenodo.22163849 |
| ep | kc-ep-042 | definition | The Readout Condition: existence, attribution, disclosure | holds | adopt | 10.5281/zenodo.22301318 |
| ep | kc-ep-043 | claim | Written by AI, still true: the Possession-Constitution Collapse and knower fetishism | holds | adopt | 10.5281/zenodo.22301202 |
| ep | kc-ep-044 | claim | Faqr, scholarly authority, and non-transferable responsibility | holds | adopt | 10.5281/zenodo.22206607 |
| ep | kc-ep-045 | method | The Epistemic Chain Reaction: controlled human-AI amplification (Bounded Knower Paper IV) | holds | adopt | 10.5281/zenodo.22308072 |
| ep | kc-ep-046 | method | State of Evidence registry for the Readout hypothesis-generation programme (E01-E25) | holds | adopt | 10.5281/zenodo.22308066 |
| ep | kc-ep-047 | tool | Blackbox Log: daily append-only verbatim voice record | holds | adopt | 10.5281/zenodo.22307891 |
| ep | kc-ep-048 | method | Before Evidence Can Decide: candidate-set formation and discovery routing (Paper III) | holds | adapt | 10.5281/zenodo.22307564 |
| ep | kc-ep-049 | method | Knowledge Topology and the First Passage to Usable Hypotheses (Paper II) | holds | adapt | 10.5281/zenodo.22307561 |
| ep | kc-ep-050 | method | From Problem to Hypothesis: bounded dynamic semantic mobility (Paper I) | holds | adopt | 10.5281/zenodo.22307148 |
| ep | kc-ep-051 | definition | glosa v0.1.0/v0.2.0: methodology + skill + tools for human-AI knowledge co-production | holds | adopt | 10.5281/zenodo.22307843 |
| ep | kc-ep-052 | claim | Rigour Without Infrastructure: three propositions on claim-card discipline | holds | adopt | 10.5281/zenodo.22307841 |
| he | kc-he-001 | method | Referral governance — separating clinical decision, information transfer, and payment authorization | holds | adopt | 10.5281/zenodo.22302173 |
| he | kc-he-002 | method | SOMA-READ — frozen preregistration deposited before ethics approval, before any data | open | adopt | 10.5281/zenodo.22302190 |
| he | kc-he-003 | rule | T-PHE — practitioner standpoint paired with a cited tier-one evidence dossier, no clinical recommendation | holds | already_in_glosa | 10.5281/zenodo.22302161 |
| he | kc-he-004 | method | RRHM Open Lab — sealed prediction package with an independent reproduction and a recorded prior | holds | adopt | 10.5281/zenodo.22255211 |
| he | kc-he-005 | method | RRHM phobia model — pre-registering which falsification gates are simulable before any participant | holds | adopt | 10.5281/zenodo.22227003 |
| he | kc-he-006 | method | CPRMH — seventeen pre-specified falsifiers, locked before outcome access | holds | adopt | sources/CPRMH_v12.txt |
| he | kc-he-007 | method | CPRMH — versioned living-evidence object with machine-assisted retrieval plus mandatory human adjudication | holds | adopt | sources/CPRMH_v12.txt |
| he | kc-he-008 | definition | Wellbeing from Informationism — repair-permissive causal-informational coherence, not symptom absence | holds | skip | 10.5281/zenodo.20283074 |
| he | kc-he-009 | definition | Health as constraint-admissible trajectory — identity redefined as admissible continuity, not static sameness | holds | skip | 10.5281/zenodo.18813886 |
| he | kc-he-010 | rule | AI-coached endurance training — admissibility-first, no-go conditions derived and empirically anchored, not optimized-for-performance | holds | adopt | 10.5281/zenodo.18404721 |
| he | kc-he-011 | rule | Autonomic Safety paper — operational guidance explicitly bounded to feasibility (GO/NO-GO), not clinical decision | holds | adopt | 10.5281/zenodo.18281221 |
| he | kc-he-012 | definition | High Capability, Low Execution — execution failure reframed as finite causal capacity, not motivation deficit | holds | skip | 10.5281/zenodo.18264276 |
| he | kc-he-013 | rule | Cellular Aging paper — falsifiable constraints derived without pathway-specific or clinical claims | holds | adopt | 10.5281/zenodo.18212478 |
| he | kc-he-014 | definition | Causal Psychology — apparent psychological failure reframed as environmental impossibility, not individual deficiency | holds | skip | 10.5281/zenodo.18175678 |
| he | kc-he-015 | rule | Life as Hazard Management — nondiagnostic white paper, no new biological constants or clinical prescriptions | holds | adopt | 10.5281/zenodo.18174493 |
| he | kc-he-016 | rule | SANA runtime — explicit non-medical/non-psychiatric/non-legal scope stated inside an operational AI spec | holds | adopt | 10.5281/zenodo.17825408 |
| he | kc-he-017 | claim | AI-Cognitive Interaction (youth potential) — K0 conceptual paper, SSRN-first, no priority claim, deposited unchanged | holds | adopt | 10.5281/zenodo.22308448 |
| he | kc-he-018 | definition | Strong, Warm & Safe Family Ecosystem — policy brief integrating ethics framework and social-innovation practice | open | skip | 10.5281/zenodo.17280895 |
| he | kc-he-019 | rule | Systemic Repair Capacity Theory — explicit no-novelty-at-mechanism-level claim, novelty scoped to architecture only | holds | adopt | 10.5281/zenodo.20229203 |
| islam | kc-islam-001 | rule | Practitioner standpoint paired with cited evidence, no clinical recommendation (islam-hub angle) | holds | already_in_glosa | 10.5281/zenodo.22302161 |
| islam | kc-islam-002 | claim | Revelation is not fallible; the human juristic determination of it is — distinguishing revelation from juristic readouts | holds | adopt | 10.5281/zenodo.22206607 |
| islam | kc-islam-003 | claim | Functional sacralization of fiqh — human determinations acquiring practical sacred-normativity when institutions make dissent costly | holds | adopt | 10.5281/zenodo.22206607 |
| islam | kc-islam-004 | claim | AI-mediated society risks the human forgetting their own status as chooser and responsibility-bearer | holds | adopt | 10.5281/zenodo.22302410 |
| islam | kc-islam-005 | definition | Epistemic hardening — declining social revisability of human interpretive claims | holds | adopt | 10.5281/zenodo.22129490 |
| islam | kc-islam-006 | method | Every doctrine states the conditions under which it would be defeated | holds | adopt | 10.5281/zenodo.21439275 |
| islam | kc-islam-007 | method | Power-literate satire framework offered as analytical tool, not normative verdict | holds | adopt | 10.5281/zenodo.20159825 |
| islam | kc-islam-008 | claim | Knowledge as the residue of beliefs that survived the world's resistance | holds | adopt | 10.5281/zenodo.19951961 |
| islam | kc-islam-009 | rule | Layer confusion — applying one layer's tools/authority to a question belonging to another layer | holds | adopt | 10.5281/zenodo.19124963 |
| islam | kc-islam-010 | definition | Premature Category Stabilization as a scale-invariant mechanism; peace defined by three structural conditions | holds | adopt | 10.5281/zenodo.19115417 |
| islam | kc-islam-011 | claim | Premature category stabilization — provider-defined service templates precede and distort the diversity they claim to serve | holds | adapt | 10.5281/zenodo.19059720 |
| islam | kc-islam-012 | tool | Behavioral dataset explicitly withholds interpretive commentary | holds | adopt | 10.5281/zenodo.17305576 |
| islam | kc-islam-013 | tool | Statistical dataset compiled from named sources, explicitly excludes interpretive analysis | holds | adopt | 10.5281/zenodo.17305534 |
| islam | kc-islam-014 | claim | Dialogue quality, not the interlocutor's nature, determines whether wisdom or distortion results | holds | adopt | 10.5281/zenodo.22308451 |
| islam | kc-islam-015 | method | Cultural-Based Practitioners framework converts faith/cultural capital into verifiable social and economic value | holds | skip | 10.5281/zenodo.17281646 |
| islam | kc-islam-016 | claim | Contribution declared theoretical/analytical, not empirical, up front | holds | adopt | 10.5281/zenodo.18258377 |
| ph | kc-ph-001 | claim | Dark Energy as Mean Damping: From Lyapunov Energy Decay to Cosmological Coherence | superseded | skip | 10.5281/zenodo.17534299 |
| ph | kc-ph-002 | claim | The Yaoharee Proposal_ An Epistemic Architecture of Observable Reality | superseded | skip | 10.5281/zenodo.17334604 |
| ph | kc-ph-003 | claim | Epistemic Coherence_Yaoharee_proposal | open | skip | 10.5281/zenodo.17335199 |
| ph | kc-ph-004 | claim | Empirical Calibration and Validation of the Epistemic Coherence Equation | open | skip | 10.5281/zenodo.17335909 |
| ph | kc-ph-005 | method | MUS/Epistemic Framework: Quantum-Gravity Unification via Coherence Field Dynamics | superseded | skip | 10.5281/zenodo.17343968 |
| ph | kc-ph-006 | method | MUS/Epistemic (MU) v1.5 — Technical Whitepaper | superseded | skip | 10.5281/zenodo.17344093 |
| ph | kc-ph-007 | method | The Yaoharee Proposal — A Transdisciplinary Framework for Contextual Coherence Across Physical, Cognitive, and Ethical S | superseded | skip | 10.5281/zenodo.17378613 |
| ph | kc-ph-008 | claim | UFC Equation v1.3.4 — Mathematical Compact Edition | superseded | skip | 10.5281/zenodo.17382545 |
| ph | kc-ph-009 | method | Equation-of-Everything (V0.7) — SURE-∞ Framework | superseded | skip | 10.5281/zenodo.17393189 |
| ph | kc-ph-010 | claim | The Equation of Coherence — From Cosmic Order to Quantum Trace - The Yaoharee Proposal | superseded | skip | 10.5281/zenodo.17403714 |
| ph | kc-ph-011 | claim | UB-ONE v6.3 (Minimal) — Full Reviewer Pack for | open | skip | 10.5281/zenodo.17419226 |
| ph | kc-ph-012 | method | Reflective Note: Ten Days of Returning to the Language of Mathematics | open | skip | 10.5281/zenodo.17420969 |
| ph | kc-ph-013 | claim | The Emergence of Mass Consistent with Both Relativity and Quantum Physics | open | skip | 10.5281/zenodo.17439693 |
| ph | kc-ph-014 | claim | Geometric Resolution to the Hierarchy Problem: The Scale‑Locked Identity | open | skip | 10.5281/zenodo.17442210 |
| ph | kc-ph-015 | claim | The Scale-Lock Breaking Paradox and the Origin of Λ | superseded | skip | 10.5281/zenodo.17443390 |
| ph | kc-ph-016 | claim | A Tri-Domain Symmetry in Gravity-Frequency Scaling: A Testable Hypothesis from Mathematical Synthesis | open | skip | 10.5281/zenodo.17457748 |
| ph | kc-ph-017 | claim | Energy-Wavelength Tri-Domain Symmetry: A Testable Hypothesis Connecting Quantum, Relativistic, and Classical Regimes | open | skip | 10.5281/zenodo.17457923 |
| ph | kc-ph-018 | claim | Alpha-Closure: Scale-Invariant Coherence with Constant Coherence Time | open | skip | 10.5281/zenodo.17463932 |
| ph | kc-ph-019 | claim | Yaoharee Cosmo data collection 2025 | open | skip | 10.5281/zenodo.17464990 |
| ph | kc-ph-020 | claim | Equation of Everything ∞ Final - Yaoharee Proposal | superseded | skip | 10.5281/zenodo.17468593 |
| ph | kc-ph-021 | claim | K=32: Equation of Everything (EoE) | superseded | skip | 10.5281/zenodo.17473885 |
| ph | kc-ph-022 | claim | EoE (K = 32): Core Proof of H0–H4 with Sharp Threshold | superseded | skip | 10.5281/zenodo.17475130 |
| ph | kc-ph-023 | claim | EoE (K = 32): One-Document Core (H0–H9) | superseded | skip | 10.5281/zenodo.17475434 |
| ph | kc-ph-024 | claim | Local-Only Derivation of an Emergent Coherence Field from the Seed Algebra 𝐴𝜀 = delta | superseded | skip | 10.5281/zenodo.17486875 |
| ph | kc-ph-025 | method | Scale-Lock from Lyapunov Dissipation in a Local-Only Framework | superseded | skip | 10.5281/zenodo.17487171 |
| ph | kc-ph-026 | claim | L2 Scale-Lock and Mass Emergence via Lyapunov Dissipation Numerical | superseded | skip | 10.5281/zenodo.17489688 |
| ph | kc-ph-027 | claim | L0–L3: Minimal-Viable Foundation for the Emergent Coherence Field | superseded | skip | 10.5281/zenodo.17495915 |
| ph | kc-ph-028 | method | L4 — Phase–Amplitude Persistence in Human EEG (N=36) Empirical Validation of the Lyapunov–Scale–Lock Framework | superseded | skip | 10.5281/zenodo.17498858 |
| ph | kc-ph-029 | method | Information Field Theory v0.1: Phase, Damp, Sync, and W0 Toward a Unified Framework Connecting Cosmos, Quantum, and Mind | superseded | skip | 10.5281/zenodo.17516592 |
| ph | kc-ph-030 | claim | A Proposed Gauge-Coupled Unification of Informational, Curvature, and Electromagnetic Dynamics | superseded | skip | 10.5281/zenodo.17520367 |
| ph | kc-ph-031 | claim | Lyapunov Energy Decay for Gauge-Coupled Complex Scalar Fields with Covariant Friction : IFT_v0.1_LyapunovProof | superseded | skip | 10.5281/zenodo.17520951 |
| ph | kc-ph-032 | claim | Lyapunov Energy Decay for Gauge-Coupled Complex Scalar Fields with Covariant Friction | superseded | skip | 10.5281/zenodo.17524006 |
| ph | kc-ph-033 | claim | Long-Tail Energy Relaxation in an Old Polluted White Dwarf: A Theoretical Remark on LSPM J0207+3331 | open | skip | 10.5281/zenodo.17535103 |
| ph | kc-ph-034 | claim | Theoretical Remark: Non-ideal Dissipation as the Missing Piece Bridging Ambipolar-Diffusive Winds in Red Giants and Long | superseded | skip | 10.5281/zenodo.17535369 |
| ph | kc-ph-035 | method | Theoretical Remark: Massive Star Evolution in Extremely Metal-Poor Environments under the Lyapunov–Scale–Log Framework | superseded | skip | 10.5281/zenodo.17539048 |
| ph | kc-ph-036 | claim | Theoretical Remark: A Possible Slowdown of Cosmic Expansion and a Self-Contained Lyapunov Mean-Damping Interpretation Co | superseded | skip | 10.5281/zenodo.17539731 |
| ph | kc-ph-037 | rule | Axiom 4: Non-Equilibrium Information Physics | superseded | skip | 10.5281/zenodo.17543179 |
| ph | kc-ph-038 | claim | Unified Equation v4.3-r1.5 (Stage II, ScopeTight) | superseded | skip | 10.5281/zenodo.17543503 |
| ph | kc-ph-039 | method | Unified Information Field Foundation (A Minimal Mathematical Framework Linking Energy, Information, and Stability) | superseded | skip | 10.5281/zenodo.17566315 |
| ph | kc-ph-040 | claim | Mass from the Informational Field | superseded | skip | 10.5281/zenodo.17581909 |
| ph | kc-ph-041 | claim | When GR Is an Information Tensor, Not Matter: Resolving Dark Matter | open | skip | 10.5281/zenodo.17588162 |
| ph | kc-ph-042 | rule | Axiom 11 — Disk Before Mass | superseded | skip | 10.5281/zenodo.17599562 |
| ph | kc-ph-043 | rule | Axiom 12 — Informational CP-Asymmetry | superseded | skip | 10.5281/zenodo.17600798 |
| ph | kc-ph-044 | rule | Axioms 13–14: Informational Vacuum and Universal Couplings | superseded | skip | 10.5281/zenodo.17601814 |
| ph | kc-ph-045 | method | Informational Diffusivity of Black-Hole Ringdown: A Causally Constrained Telegraph-Based Surrogate Framework | refined_by_later_work | skip | 10.5281/zenodo.17616410 |
| ph | kc-ph-046 | method | Concept note : Information Dynamics Across Scales: Telegraph Flow, Memory, and Boundary Capacity | refined_by_later_work | skip | 10.5281/zenodo.17624695 |
| ph | kc-ph-047 | method | Non-Equilibrium Information Physics : Concept note | superseded | skip | 10.5281/zenodo.17625342 |
| ph | kc-ph-048 | claim | A Robust 2π-nat Upper Bound for Localized Fermions: From Barut's Lepton-Mass Prediction to Gravitational Entropy Account | open | skip | 10.5281/zenodo.17645741 |
| ph | kc-ph-049 | claim | Fine-Structure Constant as Geometric Necessity: First Derivation of α from Information-Theoretic Architecture | open | skip | 10.5281/zenodo.17636870 |
| ph | kc-ph-050 | claim | Elementary Fermions Carry Exactly 2π Nat of Information: A Horizon–Confinement Identity | open | skip | 10.5281/zenodo.17643816 |
| ph | kc-ph-051 | claim | A PDE–Based Proof that Every Compton-Localized Particle Carries Exactly 2π Nat of Information | open | skip | 10.5281/zenodo.17646112 |
| ph | kc-ph-052 | method | A Short Note on a Striking Numerical Observation in Charged-Lepton Masses from a Minimal C5-Symmetric Five-Site Model | open | skip | 10.5281/zenodo.17647053 |
| ph | kc-ph-053 | claim | Conservative, Falsifiable Claims for Electroweak Mixing at the Z Pole : Non-Equilibrium Informational Field Theory | superseded | skip | 10.5281/zenodo.17660702 |
| ph | kc-ph-054 | method | Phenomenological Discovery Note: Minimal-Claim Numerical Consistencies Across Gauge, Scalar, and Gravitational Sectors a | open | skip | 10.5281/zenodo.17663564 |
| ph | kc-ph-055 | claim | An Informational-Pixel Ansatz for the Vacuum Energy: A Mathematical Invitation to Resolve the Vacuum Catastrophe | superseded | skip | 10.5281/zenodo.17664596 |
| ph | kc-ph-056 | claim | Spectral–Geometric Constraint at the Z Pole: Couplings, Electroweak Masses, Fermion Ratios, and FAIR Verification of the | open | skip | 10.5281/zenodo.17674631 |
| ph | kc-ph-057 | claim | Operational Compactness: Unified One-Parameter Interfaces for Newtonian, Gravitational, and Micro-Informational Domains | open | skip | 10.5281/zenodo.17679504 |
| ph | kc-ph-058 | claim | Informational Pixel Field: Master Lagrangian and Nine-Domain Architecture | superseded | skip | 10.5281/zenodo.17682481 |
| ph | kc-ph-059 | claim | Draf_Non-Equilibrium Informational Field Theory_physic_humanlife_ai_coherence | superseded | skip | 10.5281/zenodo.17711131 |
| ph | kc-ph-060 | method | Cosmological and Quantum Constraints on Scalar-Modulated Gauge Couplings from an Informational Field Framework | superseded | skip | 10.5281/zenodo.17715539 |
| ph | kc-ph-061 | claim | Information Inertia and Geometric Causality: A Structural Synthesis of Reality Beyond "It from Bit" | open | skip | 10.5281/zenodo.17767416 |
| ph | kc-ph-062 | claim | Causal Informational Ordering: On the Pre-Geometric Nature of Time and Change | refined_by_later_work | skip | 10.5281/zenodo.17807792 |
| ph | kc-ph-063 | claim | Reality is the causal structure of a single informational field | superseded | skip | 10.5281/zenodo.17812102 |
| ph | kc-ph-064 | claim | Mass as Inverse Causal Time: A Unified Resolution of Four Persistent Puzzles in Particle Physics and Cosmology | open | skip | 10.5281/zenodo.17828120 |
| ph | kc-ph-065 | claim | Causal Regularization of Newtonian Gravity via Maxwell–Cattaneo Transport | refined_by_later_work | skip | 10.5281/zenodo.17846399 |
| ph | kc-ph-066 | claim | Mass as a Structural Necessity of Finite-Speed Causal Transport | open | skip | 10.5281/zenodo.17855403 |
| ph | kc-ph-067 | claim | Reframing Naturalness: The Hierarchy Problem as a Timescale Stability Question | open | skip | 10.5281/zenodo.17873797 |
| ph | kc-ph-068 | claim | The Social Life of Particles How Causal Memory Reveals Hidden Order in the Mass Spectrum | refined_by_later_work | skip | 10.5281/zenodo.17875968 |
| ph | kc-ph-069 | claim | Mass as Causal Memory: A Structural Unication of Black Hole Physics | refined_by_later_work | skip | 10.5281/zenodo.17878952 |
| ph | kc-ph-070 | claim | Pixel Gravity and the Structure of Causal Memory: Kernel Uniqueness and Planck-Limited Relaxation | refined_by_later_work | skip | 10.5281/zenodo.17890616 |
| ph | kc-ph-071 | claim | CAUSAL MEMORY IN PHYSICS | refined_by_later_work | skip | 10.5281/zenodo.17899050 |
| ph | kc-ph-072 | claim | The Causal-Memory Architecture of the Universe | refined_by_later_work | skip | 10.5281/zenodo.17901698 |
| ph | kc-ph-073 | claim | Complexity from Causal Memory: A τc-Based Physics of Depth | refined_by_later_work | skip | 10.5281/zenodo.17913256 |
| ph | kc-ph-074 | claim | Causal-Time Diagnostic: A Concise, Model-Independent Test of Late-Time Acceleration | open | skip | 10.5281/zenodo.17914472 |
| ph | kc-ph-075 | claim | Chronometry of the Degenerate State: White Dwarf Cooling Anomalies, Crystallization Kinetics, and the Q-Branch Phenomeno | open | skip | 10.5281/zenodo.17921185 |
| ph | kc-ph-076 | method | The Telegraph–Causal Framework for Ultra-Fast Outflows in NGC 3783 | refined_by_later_work | skip | 10.5281/zenodo.17922382 |
| ph | kc-ph-077 | claim | A Minimal Telegraph Representation of Finite-Speed Causal Transport | refined_by_later_work | skip | 10.5281/zenodo.17926609 |
| ph | kc-ph-078 | claim | Hear the Noise Before You Fix It: A One–Page, CP–Safe, Memory–Aware QEC Upgrade | open | skip | 10.5281/zenodo.17942505 |
| ph | kc-ph-079 | method | The Causal-Memory Program: Canon | refined_by_later_work | skip | 10.5281/zenodo.17993686 |
| ph | kc-ph-080 | claim | FOUNDATION Truth, Physics, and Cosmology from Causal Memory | refined_by_later_work | skip | 10.5281/zenodo.18013670 |
| ph | kc-ph-081 | claim | Uniqueness of Telegraph Dynamics Under Minimal Causal-Dissipative Constraints | refined_by_later_work | skip | 10.5281/zenodo.18051281 |
| ph | kc-ph-082 | claim | The Causal Accessibility Horizon: A Structural Limit on Finite-Time Reachability | refined_by_later_work | skip | 10.5281/zenodo.18053352 |
| ph | kc-ph-083 | claim | Early Warning Necessitates Timely Controllability Under Finite-Speed Causal Response | open | skip | 10.5281/zenodo.18055068 |
| ph | kc-ph-084 | method | Black Holes in the Causal-Memory Framework: A Sketch | refined_by_later_work | skip | 10.5281/zenodo.18059378 |
| ph | kc-ph-085 | method | Causal–Memory Program: Short Talk (Two-Column Boxed) | open | skip | 10.5281/zenodo.18065304 |
| ph | kc-ph-086 | claim | A Soft–Gated (Multiplier–Enforced) Energy–Flux Root Lagrangian: Variational Consistency, Universal Projection (Local), U | open | skip | 10.5281/zenodo.18073917 |
| ph | kc-ph-087 | claim | Causal Memory Transport Equations | refined_by_later_work | skip | 10.5281/zenodo.18075029 |
| ph | kc-ph-088 | method | InformationCausal Emergence of Physics: A Concept Note on Why Geometry, Mass, and Dynamics Are Not Fundamental | open | skip | 10.5281/zenodo.18076195 |
| ph | kc-ph-089 | claim | Time as Causal Memory A Philosophical Synthesis from Newton to Quantum Gravity | refined_by_later_work | skip | 10.5281/zenodo.18081443 |
| ph | kc-ph-090 | claim | Why Purely Markovian Ringdown Is Not Admissible Under Persistent Causal Memory | refined_by_later_work | skip | 10.5281/zenodo.18098346 |
| ph | kc-ph-091 | method | Post–2025 Cosmological Forecast Note under the Causal State History Principle | refined_by_later_work | skip | 10.5281/zenodo.18103092 |
| ph | kc-ph-092 | method | Note: Causal State History as a Structural Constraint (Discussion Route) | refined_by_later_work | skip | 10.5281/zenodo.18105213 |
| ph | kc-ph-093 | claim | Physics Letter: A Structural No-Go on Bias without Record-Cost Asymmetry in Causal Memory Architectures | refined_by_later_work | skip | 10.5281/zenodo.18113633 |
| ph | kc-ph-094 | claim | Tully–Fisher as Gravitational Memory: Why the Universe Remembers (with Spatial Diffusion) | superseded | skip | 10.5281/zenodo.18202473 |
| ph | kc-ph-095 | claim | Kibble Balance as Operational Identity: Why ℏ is an Exchange Rate | superseded | skip | 10.5281/zenodo.18202644 |
| ph | kc-ph-096 | claim | Non-Circular Operational Identification of the Gravitational Constant 𝐺 & ℏ in Causal Memory Gravity | refined_by_later_work | skip | 10.5281/zenodo.18202581 |
| ph | kc-ph-097 | claim | Cosmology from Finite Causal Memory | refined_by_later_work | skip | 10.5281/zenodo.18208238 |
| ph | kc-ph-098 | claim | Time as Irreversible Causal Record A Mathematical Derivation from Causality and Passivity | refined_by_later_work | skip | 10.5281/zenodo.18210933 |
| ph | kc-ph-099 | claim | Interactive Causal Memory Theory: Emergent Noise, Shock, and Record Formation in Multi-Agent Systems | refined_by_later_work | skip | 10.5281/zenodo.18213737 |
| ph | kc-ph-100 | method | Bounded Causal Influence as a Structural Constraint Causal Physics Note | refined_by_later_work | skip | 10.5281/zenodo.18234573 |
| ph | kc-ph-101 | method | Telegraph-on-Graph Bottleneck Stress Test : Causal Physic Note | refined_by_later_work | skip | 10.5281/zenodo.18345135 |
| ph | kc-ph-102 | method | Causal Memory Graph Framework An AI-Implementable Specification for Boundary-Aware Structural Graph Analysis | refined_by_later_work | skip | 10.5281/zenodo.18372525 |
| ph | kc-ph-103 | claim | Emergence of Power–Law Memory from Linear Spectral Superposition Necessity of Long–Time Non–Markovianity without Fractio | open | skip | 10.5281/zenodo.18378477 |
| ph | kc-ph-104 | method | Spectral Representation of Causal Memory Dynamics: A Practical Guide for Implementation | refined_by_later_work | skip | 10.5281/zenodo.18382712 |
| ph | kc-ph-105 | method | Causal Memory Program: Generator Update Note | refined_by_later_work | skip | 10.5281/zenodo.18427189 |
| ph | kc-ph-106 | claim | Causal Memory Gravity Seed | refined_by_later_work | skip | 10.5281/zenodo.18449869 |
| ph | kc-ph-107 | claim | Causal Quantum Gravity | refined_by_later_work | skip | 10.5281/zenodo.18677955 |
| ph | kc-ph-108 | claim | Causal Memory Admissibility (CMAP): A Structural Necessity Classication Discrete-First, Primitives-Grounded, Domain-Inde | refined_by_later_work | skip | 10.5281/zenodo.18757034 |
| ph | kc-ph-109 | claim | PRFT v28 Master Standalone – Full Detailed Rewrite: Q3 Null-Cone Geometry, Dissipative Readout, and Adapter-Limited Solv | holds | already_in_glosa | 10.5281/zenodo.20552148 |
| ph | kc-ph-110 | method | Pixel Gravity Field Theory: A Clocked Retained-Readout Framework for Field-to-Channel Computation | holds | already_in_glosa | 10.5281/zenodo.20615715 |
| ph | kc-ph-111 | claim | Synthesis of the Information Universe: Relativity and Mass as Readouts of Retained Distinctions, Assembled from Classica | holds | already_in_glosa | 10.5281/zenodo.21203637 |
| ph | kc-ph-112 | claim | black-hole-merger-information: the Davies point and black-hole merger remnants — a crossing locus, the observed populati | holds | already_in_glosa | 10.5281/zenodo.21431683 |
| ph | kc-ph-113 | claim | The Discrete Retention Lagrangian: Damping from a Variational Principle Forced by an Information-Retention Axiom | holds | already_in_glosa | 10.5281/zenodo.21443916 |
| ph | kc-ph-114 | claim | The Mystery Ladder: Compressing the Weakness of Gravity to Three Open Atoms, with an Information Semantics for the Atom  | holds | adapt | 10.5281/zenodo.21443942 |
| ph | kc-ph-115 | claim | Retention–Hodge–Dirac Closure: A Discrete Information Criterion for Three-Dimensional Directional Feedback, with Five Ex | holds | adapt | 10.5281/zenodo.21444163 |
| ph | kc-ph-116 | method | Transform-Free Inertia Methods for Generalized Banded Symmetric Eigenproblems | open | skip | 10.5281/zenodo.21635722 |
| se | kc-se-001 | rule | Descriptive-only comparison table — no outperformance claim across adjacent frameworks | holds | adopt | 10.5281/zenodo.22302161 |
| se | kc-se-002 | rule | Adjacent evidence is not evidence the intervention itself works — a standing caveat, stated once | holds | adopt | 10.5281/zenodo.22302161 |
| se | kc-se-003 | rule | Five-tier claim ladder for a social-enterprise management framework (Th-coqc through NI/Open) | holds | adopt | 10.5281/zenodo.22301882 |
| se | kc-se-004 | rule | Unidentified values return NI, never zero — a readout-audit layer over every calculated claim | holds | adopt | 10.5281/zenodo.22301882 |
| se | kc-se-005 | definition | Readout non-equivalence in an enterprise's own data model — a channel-specific lossy map, not the state | refined_by_later_work | adapt | 10.5281/zenodo.22301882 |
| se | kc-se-006 | rule | Reflexive practitioner-inquiry disclosure — using one's own organisation as illustration, and saying why | holds | adopt | 10.5281/zenodo.22227005 |
| se | kc-se-007 | method | Systematic prior-art review reporting "partially anticipated, not found in formulation" — not a novelty claim | holds | adopt | 10.5281/zenodo.22227005 |
| se | kc-se-008 | claim | Candidate Forgetting — the crisis is not AI's answer, it is losing track that the answer was a candidate | holds | adopt | 10.5281/zenodo.22302410 |
| se | kc-se-009 | rule | From AI Governance to Epistemic Governance — govern the output's status, not only the system | holds | adopt | 10.5281/zenodo.22302410 |
| se | kc-se-010 | method | Faith-based Cultural-Based Practitioners as a governance framework, not a claim about outcomes | outdated | skip | 10.5281/zenodo.17281646 |
| se | kc-se-011 | method | SWSF policy brief — eight dimensions, four mechanisms, framework-integration method, no outcome claim | outdated | skip | 10.5281/zenodo.17280895 |
| se | kc-se-012 | method | Simulation-battery evidence for social-enterprise survival — finite runs, stated consistency with empirical rates | refined_by_later_work | adapt | 10.5281/zenodo.18506938 |
| tourism | kc-tourism-001 | claim | Premature Category Stabilization generalized as a scale-invariant mechanism, framework's own limits named | holds | skip | 10.5281/zenodo.19115417 |
| tourism | kc-tourism-002 | claim | Premature category stabilization — provider-side interpretation as the mechanism, not certification sufficiency | open | skip | 10.5281/zenodo.19059720 |
| tourism | kc-tourism-003 | method | Explicit 'proves vs. still cannot explain' gap statement before advancing a new mechanism | holds | adapt | 10.5281/zenodo.19059720 |
| tourism | kc-tourism-004 | method | Behavioral dataset compiled with interpretation deliberately excluded from the record | holds | already_in_glosa | 10.5281/zenodo.17305576 |
| tourism | kc-tourism-005 | method | Statistical dataset sourced from named third-party institutions, analysis explicitly withheld | holds | already_in_glosa | 10.5281/zenodo.17305534 |
| tourism | kc-tourism-006 | claim | Cultural-Based Practitioner framework built from cross-national case studies, not a single-site claim | open | skip | 10.5281/zenodo.17281646 |
| tourism | kc-tourism-007 | rule | Contribution explicitly typed as theoretical/analytical, empirical findings explicitly disclaimed | holds | already_in_glosa | 10.5281/zenodo.18258377 |
