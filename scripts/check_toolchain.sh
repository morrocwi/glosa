#!/usr/bin/env bash
# scripts/check_toolchain.sh — prints a table of the glosa toolchain state.
# Never installs anything. Exits 1 only if a CORE item is missing (python3).
# See TOOLCHAIN.md for install instructions per row.
set -u

ROWS=()

add_row() {
    # name | present(yes/NO) | version | needed-for | degrade
    ROWS+=("$1|$2|$3|$4|$5")
}

check_bin() {
    local bin="$1"
    command -v "$bin" >/dev/null 2>&1
}

version_of() {
    local bin="$1"
    "$bin" --version 2>&1 | head -n1 | cut -c1-60
}

# core
if check_bin python3; then
    add_row "python3" "yes" "$(python3 --version 2>&1 | cut -c1-60)" "core: everything" "nothing runs"
    CORE_OK=1
else
    add_row "python3" "NO" "-" "core: everything" "nothing runs"
    CORE_OK=0
fi

if check_bin git; then
    add_row "git" "yes" "$(version_of git)" "version control / PR workflow" "no VCS operations"
else
    add_row "git" "NO" "-" "version control / PR workflow" "no VCS operations"
fi

if check_bin gh; then
    add_row "gh" "yes" "$(version_of gh)" "release/PR/issue workflow" "manual web-UI GitHub steps"
else
    add_row "gh" "NO" "-" "release/PR/issue workflow" "manual web-UI GitHub steps"
fi

# python modules
py_mod_check() {
    local mod="$1" label="$2" needed="$3" degrade="$4"
    if python3 -c "import ${mod}" >/dev/null 2>&1; then
        local ver
        ver=$(python3 -c "import ${mod}; print(getattr(${mod}, '__version__', 'n/a'))" 2>/dev/null)
        add_row "$label" "yes" "$ver" "$needed" "$degrade"
    else
        add_row "$label" "NO" "-" "$needed" "$degrade"
    fi
}

py_mod_check markdown "markdown (pip)" "md2html/md2pdf/md2docx/md2pptx parsing" "no rendering at all"
py_mod_check docx "python-docx (pip)" "md2docx direct build" "falls back to soffice html->docx"
py_mod_check pptx "python-pptx (pip)" "md2pptx" "pptx route unavailable"
py_mod_check jsonschema "jsonschema (pip)" "schema/*.schema.json validation" "schema checks cannot run"
py_mod_check yaml "PyYAML (pip)" "YAML manifests/decisions" "YAML-consuming scripts fail"

# rendering binaries
if check_bin soffice; then
    add_row "soffice/libreoffice" "yes" "$(version_of soffice)" "md2pdf, docx fallback, Thai PDF/DOCX" "no PDF route, no Thai rendering"
elif check_bin libreoffice; then
    add_row "soffice/libreoffice" "yes" "$(version_of libreoffice)" "md2pdf, docx fallback, Thai PDF/DOCX" "no PDF route, no Thai rendering"
else
    add_row "soffice/libreoffice" "NO" "-" "md2pdf, docx fallback, Thai PDF/DOCX" "no PDF route, no Thai rendering"
fi

if check_bin pdflatex; then
    add_row "pdflatex" "yes" "$(version_of pdflatex)" "tex2pdf (EN-only)" "no LaTeX route at all"
else
    add_row "pdflatex" "NO" "-" "tex2pdf (EN-only)" "no LaTeX route at all"
fi

if check_bin xelatex; then
    add_row "xelatex" "yes" "$(version_of xelatex)" "Thai-capable LaTeX" "Thai LaTeX unavailable; use md2pdf"
else
    add_row "xelatex" "NO" "-" "Thai-capable LaTeX" "Thai LaTeX unavailable; use md2pdf"
fi

if check_bin lualatex; then
    add_row "lualatex" "yes (Thai support unverified/known-broken here)" "$(version_of lualatex)" "Thai-capable LaTeX (alt route)" "treat as unavailable for Thai; use md2pdf"
else
    add_row "lualatex" "NO" "-" "Thai-capable LaTeX (alt route)" "treat as unavailable for Thai; use md2pdf"
fi

if check_bin pandoc; then
    add_row "pandoc" "yes" "$(version_of pandoc)" "optional alternate md route (not used by render.py)" "no effect; direct routes cover it"
else
    add_row "pandoc" "NO" "-" "optional alternate md route (not used by render.py)" "no effect; direct routes cover it"
fi

if check_bin bibtex; then
    add_row "bibtex" "yes" "$(version_of bibtex)" "tex2pdf bibliography step" "tex2pdf skips bibliography, warns"
else
    add_row "bibtex" "NO" "-" "tex2pdf bibliography step" "tex2pdf skips bibliography, warns"
fi

if check_bin curl; then
    add_row "curl" "yes" "$(version_of curl)" "citation checking (Crossref/OpenAlex HTTP)" "citation checks unavailable"
else
    add_row "curl" "NO" "-" "citation checking (Crossref/OpenAlex HTTP)" "citation checks unavailable"
fi

if check_bin fc-list; then
    if fc-list 2>/dev/null | grep -qi "noto.*thai"; then
        add_row "Noto Thai fonts" "yes" "Noto Sans/Serif/Looped Thai" "Thai rendering via soffice route" "Thai text may show fallback glyphs"
    else
        add_row "Noto Thai fonts" "NO" "-" "Thai rendering via soffice route" "Thai text may show fallback glyphs"
    fi
else
    add_row "Noto Thai fonts" "NO (fc-list absent)" "-" "Thai rendering via soffice route" "cannot verify; Thai text may show fallback glyphs"
fi

# print table
printf "%-24s | %-8s | %-45s | %-42s | %s\n" "tool" "present" "version" "needed-for" "degrade"
printf -- "-------------------------+----------+-----------------------------------------------+--------------------------------------------+-----------\n"
for row in "${ROWS[@]}"; do
    IFS='|' read -r name present ver needed degrade <<< "$row"
    printf "%-24s | %-8s | %-45s | %-42s | %s\n" "$name" "$present" "$ver" "$needed" "$degrade"
done

if [[ "${CORE_OK:-0}" -ne 1 ]]; then
    echo ""
    echo "CORE tool missing (python3) — see TOOLCHAIN.md" >&2
    exit 1
fi
exit 0
