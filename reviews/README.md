# reviews/ — independent review trail

The full review packets (architecture review, build checks, the R1–R7 publish gate, the
re-verify pass) are kept **locally, git-ignored**: they quote internal working material
verbatim (private repository names, local paths, third-party file names) as audit evidence,
which is exactly what a public copy must not carry. What is public is the sanitized summary
`PUBLISH_GATE_v1_public.md`: finding ids, class, status. Reviewer identity: separate AI
routes (not the maker), tier finite_diagnostic; no human reviewer yet (I5 pending).
