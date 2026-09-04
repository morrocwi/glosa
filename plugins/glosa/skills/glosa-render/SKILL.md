---
name: glosa-render
description: Render a glosa markdown document (paper, claim card, review) to HTML/PDF/DOCX/PPTX, or a LaTeX main.tex to PDF, using tools/render.py. Load before generating any human-facing output file from glosa markdown/LaTeX sources.
---

# glosa-render

Points to `tools/render.py` (the rendering layer) and `TOOLCHAIN.md` (the install/degrade
reference). This skill does not render anything itself — it tells you which command to
run and which route is safe for the language you're rendering.

## Commands

```
python3 tools/render.py md2html  in.md out.html [--lang th|en]
python3 tools/render.py md2pdf   in.md out.pdf
python3 tools/render.py md2docx  in.md out.docx
python3 tools/render.py md2pptx  in.md out.pptx
python3 tools/render.py tex2pdf  main.tex
python3 tools/render.py all      paper/main_en.md paper/main_th.md --out dist/
python3 tools/render.py check
python3 tools/render.py deliver-manifest dist/manifest.json --dir dist
```

## Which route for which language

- **Thai content (any of it, mixed or pure):** use `md2pdf` / `md2docx` / `md2pptx`
  (all route through markdown → LibreOffice `soffice --headless`). This is the only
  route verified in this environment to render Thai glyphs correctly (Noto Sans/Serif/
  Looped Thai fonts installed).
- **English-only LaTeX (`tex2pdf`):** `pdflatex` works but is **EN-only**. `xelatex` is
  missing and `lualatex`'s Thai font stack (fontspec/luaotfload) is broken here — do not
  route Thai LaTeX through `tex2pdf`; it will warn and may produce missing/garbled
  glyphs. Use `md2pdf` for a Thai document instead of forcing LaTeX.
- Run `python3 tools/render.py check` (or `bash scripts/check_toolchain.sh`) before
  relying on any route — environments differ; do not assume yesterday's result.

## What is NOT verified by this tool

- It does not check citation accuracy, claim tiers, forbidden words, or schema
  conformance — those are `scripts/check_*.sh` and the schema/ validators.
- It does not upgrade or downgrade the epistemic tier of the source content. Every
  output carries a footer/closing-slide line: "tier of content unchanged (Dr unless
  stated)" — that line is a reminder, not a re-assertion that the content is verified.
- `md2docx`'s direct python-docx build handles headings/paragraphs/lists/tables/code/
  blockquotes only; anything more complex in the source markdown degrades to a plain
  paragraph. If the direct build fails, it automatically falls back to a LibreOffice
  HTML→DOCX conversion.
- Rendering success is not delivery. To share a rendered file outside the repo, see
  `plugins/glosa/skills/glosa-deliver/SKILL.md` — a separate, human-approval-gated step.

See `TOOLCHAIN.md` for what's installed, what degrades if a tool is missing, and the
full "requires admin" list.
