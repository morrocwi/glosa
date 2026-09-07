# P24 — Mathematical floor: the readout-first lens before any mathematics enters a draft

tier: Dr (specified; independently unreviewed)

> readout-not-truth applies to this card itself. Grounded in the `information-discrete-math` skill
> (Yaoharee Lahtee) and its treatise, DOI 10.5281/zenodo.22644131 (concept 10.5281/zenodo.22644130),
> and in Toledo (`github.com/morrocwi/toledo`, concept DOI 10.5281/zenodo.22537318), the equation
> home of record under `P19`. AI drafted this card. Comparison language is same/different/cited
> only.

## id

`P24`

## Rule

Before any mathematics enters a glosa draft — a number, a limit, a derivative, an angle, a zero or
an infinity, a "smooth" function, an operator — the writer, human or AI, applies the
information-discrete-math (IDM) lens in this order:

1. **Contaminated-concept check.** Scan the statement for a left-column concept in the table below
   and replace it with its discrete readout, citing the IDM object by its **Toledo code**, never by
   copying the treatise's prose (one-fact-one-home, `P00`). This is a **citation table**: concept →
   discrete replacement → Toledo code. Where no Toledo code has been registered yet for the specific
   reading needed, the row says so plainly — the concept is not presented as coded.
2. **Compute on ℚ (the ℚ-computability law).** Every quantity a draft actually computes is a finite,
   discrete, rational readout — no machine ever lands on a continuum real. A computed quantity
   carries its own **ℚ tier** (`exact` or `Th_coqc`, with a witness) separate from any `+ℝ-Open`
   fence placed on the completed limit or whole-space object it approximates. Fencing a computed
   rational result as blanket `+ℝ-Open` is under-claiming, the mirror image of overclaiming, and
   just as dishonest (founder ruling, information-discrete-math, 2026-07-29: "ถ้า ℝ-rung คำนวนได้
   เราก็ต้องคำนวนได้ด้วย ℚ" — if an ℝ-rung is actually computed, it is computed on ℚ).
3. **Tier every claim.** `Th_coqc` (machine-checked, axiom-free over ℚ) / `finite_diagnostic`
   (measured) / `Dr` (stance/narrative) / `Open` (needs the continuum, not computed). The tier
   enum and its meaning are owned once by `claim_card.tier` (`schema/claim_card.schema.json`,
   `P06`); this card does not redeclare it, only requires it be applied to mathematical content.
4. **Register first (`P19`).** A new or revised equation is looked up or registered in Toledo
   *before* it is used in a glosa draft, per `P19`'s registration table and its gate: "no AI agent
   … may use an equation that is not registered in Toledo, in any output."

### Citation table — contaminated concept → discrete replacement → Toledo code

Pattern only, reproduced from the IDM skill's own contaminated-concept table (mathematics-specific)
the way `methodology/data/contaminated_concept_table.json` already generalizes that pattern to
glosa's knowledge-legitimacy phrasing (`P04`) — no private treatise prose copied, each row cites the
Toledo root/reading it resolves to instead:

| Contaminated concept (left column, IDM skill) | Discrete-correct replacement | Toledo code |
|---|---|---|
| real number ℝ / ℝ-completeness (LUB/Dedekind); a limit that "lands" | ℝ as a *readout* of finite ℚ-approximants (Bishop regular Cauchy sequences of ℚ); √2, π are non-readouts | `R` (root, tier `+ℝ-axioms` — not axiom-free, per Toledo's own tiering) |
| the point (zero extent, `r = 0`) | a node / a retained distinction (finite, has neighbours) | `delta_R` (root — the primitive retained difference) |
| zero as an occupied state | a refused non-readout, approached never reached — or the `L_R` kernel = indistinguishability, not a void | `L_R` (root); `laplacian_ones_in_kernel` = `L_R/M.22.v1` |
| infinity `+∞` / `N → ∞` | ℚ has no `+∞`; a "limit" is the finite approach, never the endpoint | `Q` (root — field of fractions of `Z`, axiom-free) |
| infinite divisibility (`h → 0`) | a finite step / discrete floor — machine-checked, nothing below the first tick | `D` (root); `discrete_floor` = `D/M.55.v1`; `no_density_at_root` = `D/M.56.v1` |
| angle / degree (inverse-trig needs ℝ-completeness) | an overlap fraction, `\|⟨v,e⟩_G\|² / (⟨v,v⟩_G · ⟨e,e⟩_G)` (rational: `+,·,÷` only) | `Keystone` (root — retained-information density identity); `cauchy_schwarz_2` = `Keystone/M.01.v1` |
| derivative / integral as a continuum limit | discrete difference `Δ` + sum `Σ` + the discrete FTC | `Z` (root); `delta_sum` = `Z/M.01.v1`; `FTCC_telescope` = `Z/M.06.v1` |
| operator on a continuum (`∂²`, d'Alembertian) | the graph Laplacian `L_R` (symmetric, PSD, div-grad, summation-by-parts) | `L_R` (root); `laplacian_symmetric` = `L_R/M.20.v1` |
| distance as coordinate difference `√Σ(Δxᵢ)²` | accumulated retained resistance along the optimal graph path | `L_R` (root) — no reading registered yet for the geodesic-distance construction specifically; **not yet in Toledo**, do not present as coded |
| continuity / "smooth" (ε–δ over ℝ) | discrete Lipschitz / non-expansive maps; ε–δ continuity as a derived rung on ℝ-as-readout | **not yet in Toledo** at the specific-reading level — cite `R` (root) for the general continuum-as-readout stance only |
| π, e, φ as "numbers" | readout-invariants — diagnostics that reconstruction succeeded, only finite ℚ-approximants appear | **not yet in Toledo** at the specific-reading level — cite `R` (root) for the general continuum-as-readout stance only |

Any row marked "not yet in Toledo" fails the gate below if the concept is used without either the
discrete replacement or an honest "not yet coded" note (`P19`'s own publish-gate check, extended
here to methodology cards themselves).

## Why / incident

Toledo's canonicalisation of the programme's 946 numbered equations (2026-09-06/07) found the same
objects restated many times under different notation with no shared discipline for catching a
continuum concept smuggled in as if it were a finite computation — the exact failure mode the IDM
skill's pre-write checklist exists to catch mathematics-side, and that `P19`'s registration gate
exists to catch equation-identity-side. `P24` closes the third gap: nothing in glosa's own
methodology, before this card, told a writer to run the IDM lens *before* a number, limit, angle, or
operator reached a draft at all — `P04`'s contaminated-concept scan covers knowledge-legitimacy
phrasing ("consensus", "proven", "validated by experts") but not mathematical-continuum phrasing
("angle", "limit", "zero", "operator"), a different table for a different smuggling class.

## Inputs → outputs

- **Inputs:** the draft text containing mathematics (a claim card's `statement`/`ledger`, a paper
  section, a review report) and the IDM skill's contaminated-concept table (cited by pattern, not
  copied prose) plus Toledo's `registry/CANONICAL.json` / `docs/TOLEDO_CODES.md`.
- **Outputs:** for each mathematical expression, either (a) a discrete replacement with its Toledo
  code cited in place of the left-column concept, or (b) an honest "not yet in Toledo" note; a ℚ
  tier (`exact`/`Th_coqc`) on every computed quantity, separate from any `+ℝ-Open` fence on its
  completed-limit counterpart; and the claim's overall tier (`Th_coqc`/`finite_diagnostic`/`Dr`/
  `Open`) on `claim_card.tier`.

## Gate

A draft whose mathematics uses a left-column concept from the citation table above **without**
either the discrete replacement or a Toledo code (or an explicit "not yet in Toledo" note) does not
pass the publish gate (`P10`) — this mirrors `P19`'s own equation gate ("an equation with no Toledo
lookup is not presented as new") extended to the concept-level citation this card adds. **Failing
control (example):** a draft states "the derivative of the trajectory landed at infinity as
`h → 0`" with no discrete-Δ replacement and no Toledo code — this fires the gate as a hard fail
(unreplaced I2/I4 injection, IDM skill's own naming). **Not-failing case (example):** a draft states
"the discrete difference `Δ` of the trajectory, computed on ℚ (`Z/M.01.v1`, `delta_sum`), stays
bounded as the step floor `τ_c` is approached, never reached (`D/M.55.v1`, `discrete_floor`)" — the
concept is replaced, the Toledo codes are cited, and the claim is tiered; this passes.

Same mechanism as `P04`'s `EXTERNAL_VALIDATION_PROPOSED` hard fail: a full-text scan against the
citation table above is mechanically checkable text-matching, distinct from the harder judgment call
of whether a *given* mathematical move actually needed the continuum at all (a human/AI judgment
this card records but does not automate, same limit `P04` already states for its own scan).

## Human / AI split

Human: judges whether a given mathematical move genuinely required a continuum concept (the harder
call the mechanical scan cannot make), decides whether a "not yet in Toledo" gap blocks the draft or
is accepted with the note, and approves any new Toledo registration under `P19`. AI: runs the
contaminated-concept scan against the citation table, proposes the discrete replacement and its
Toledo code (or flags the "not yet in Toledo" gap), computes the ℚ tier for anything it actually
computes, and never asserts a `+ℝ-Open` fence over a quantity it just finished computing on ℚ.

## Disclaimers

`D-TIER` (the tier stated is the tier actually reached, never rounded up) · `D-AIFILL` (any
AI-proposed replacement or Toledo-code citation, `P07`) · `D-EXTERNAL-INPUT` (the IDM skill and
Toledo are vetted external/sister-repo sources, cited not copied). Registering a Toledo code
certifies identity and lineage of an equation, and a Coq "Closed under the global context" certifies
consistency of a finite model over ℚ — neither certifies the mathematics was the right model of the
world (same disclaimer `P19` states for registration generally).

## NC pairs

Discrete readout ≠ continuum non-readout (IDM's own one commitment) · computed-on-ℚ ≠ asserted-over-
completed-ℝ (the ℚ-computability law) · a refused endpoint being unreadable ≠ a wall (IDM skill,
checklist item 4) · Toledo-coded ≠ derived · registered ≠ validated (`P19`'s own NC pairs, carried
here unchanged).

## Not-do

- Do not copy the IDM treatise's or SKILL.md's contaminated-concept table prose into a glosa file —
  cite the Toledo code and, where useful, the skill's own table row by name; one fact, one home.
- Do not invent a Toledo code to make a citation table row look coded — an unregistered reading is
  marked "not yet in Toledo," never silently coded (same prohibition `P19`'s Not-do section states).
- Do not fence a quantity the draft actually computed as blanket `+ℝ-Open` — split into the computed
  ℚ core (its own honest tier) and the open completed-limit tail, per the ℚ-computability law.
- Do not treat a `Th_coqc` tag on a computed core as covering an input for which the cited witness's
  hypothesis does not hold (e.g. citing a nonneg-weight witness for signed weights) — drop to `exact`
  honestly instead.

## Tier

Dr — specified from the IDM skill/treatise, the ℚ-computability law ruling, and Toledo's registered
codes; independently unreviewed (no I2+ check has run on this card, `P19`/`P06`'s independence
ladder).
