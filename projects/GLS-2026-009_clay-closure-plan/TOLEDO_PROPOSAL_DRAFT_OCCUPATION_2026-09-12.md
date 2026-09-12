# DRAFT (not registered) — three NEW DERIVATION / PROPOSAL entries for Toledo, NS-P2 proposals file
Status: draft text only; to be turned into JSON entries on the local Toledo branch research/ns-p2-vnext-proposals-2026-09-12
after founder go + Toledo governance ACK. Parents verified in CANONICAL.json.
1. PROP-RG-OCCUPATION-PRIMAL-01  — statement: for a finite registered event set E with event cones C_e ⊆ ℚ^{n_e},
   balance operator B (incidence ⊗ retained-coordinate selector) and productivity row p, the occupation primal is
   (P): z ∈ Π_e C_e ∩ {d = 0, x = 0}, Bz = 0, Σ_e p_e(z_e) = 1.  parents: weld/M.02.v1, EQ-001/C.16.v1, Genesis B.3.
   tier: Dr (definition).  origin: GLS-2026-009 C0_SCHEMA §3–§5.  Coq: none yet.
2. PROP-RG-FARKAS-DUAL-CERTIFICATE-01 — statement: for closed rational polyhedral C^(r), (P) infeasible ⇔ ∃ y, η > 0,
   λ ≥ 0 with Bᵀy − η p = Σ λ·(rows of C^(r)); checker expands the identity only.  parents: PROP-RG-OCCUPATION-PRIMAL-01
   + standard Farkas lemma (relayed, external).  tier: Dr (finite theorem, standard).  Coq: none yet.
3. PROP-RG-OCC-SOUND-01 — statement: if an exact normalized productive zero-defect/no-exit recurrent core exists and
   (i) events commute with the lift (weld/M.02.v1), (ii) reader sufficiency (weld/M.03.v1, E.06.v1), (iii) G4 bounded
   normalized states, (iv) ZPR, (v) C^(0) closed and outer-sound, then (P) on C^(0) is feasible.  Contrapositive:
   DUAL certificate ⇒ no exact productive recurrent core.  tier: Open (theorem candidate).  forbidden_claims:
   does_not_prove_NS_regularity; does_not_replace_G4_or_G7.
