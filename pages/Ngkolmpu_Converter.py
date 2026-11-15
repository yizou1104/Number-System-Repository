import streamlit as st

from ui import apply_global_styles, language_nav, CONV_CSS_ADDITIONS, footer_nav
from Ngkolmpu import (
    MAX_COUNT, POWERS, number_to_ngkolmpu, ngkolmpu_lookup, literal, source_note,
    base_six, donohue_forms, donohue_strings, counting_steps,
)
from Ngkolmpu import ngkolmpu_to_number  # noqa: F401 — entry point for the audit scripts

# ============================================================
# NGKOLMPU (KANUM) SENARY CONVERTER
# Data, sources and logic live in Ngkolmpu.py.
# ============================================================

st.set_page_config(page_title="Ngkolmpu Numeral Converter", layout="wide")
apply_global_styles()

CONV_CSS = """<style>
.conv-masthead{border-top:3px solid var(--ink);border-bottom:1px solid var(--rule);padding:1.75rem 0 1.4rem 0;margin-bottom:1.75rem}
.conv-masthead-eyebrow{font-family:'DM Sans',sans-serif;font-size:.68rem;font-weight:700;text-transform:uppercase;letter-spacing:.18em;color:var(--accent);display:flex;align-items:center;gap:.65rem;margin-bottom:.65rem}
.conv-masthead-eyebrow::before{content:'';display:inline-block;width:1.75rem;height:1.5px;background:var(--accent);flex-shrink:0}
.conv-masthead-title{font-family:'Crimson Pro',Georgia,serif;font-size:3rem;font-weight:700;color:var(--ink);letter-spacing:-.04em;line-height:1.05;margin-bottom:.5rem}
.conv-masthead-desc{font-family:'Crimson Pro',Georgia,serif;font-style:italic;font-size:1.05rem;color:var(--ink-muted);line-height:1.55;margin:0}
.conv-section-label{font-family:'DM Sans',sans-serif;font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.16em;color:var(--ink-soft);display:flex;align-items:center;gap:1rem;margin:2rem 0 1rem 0}
.conv-section-label::before{content:'';display:inline-block;width:2rem;height:1px;background:var(--ink-muted);flex-shrink:0}
.conv-section-label::after{content:'';flex:1;height:1px;background:var(--rule)}
div[data-testid="stRadio"]>div{display:flex;gap:0;background:var(--card-bg);border:1px solid var(--card-border);border-radius:6px;padding:.35rem;box-shadow:0 1px 3px rgba(26,22,18,.05),0 4px 14px rgba(26,22,18,.04),inset 0 1px 0 rgba(255,255,255,.65);width:fit-content;flex-wrap:wrap}
div[data-testid="stRadio"] label{display:flex!important;align-items:center!important;font-family:'DM Sans',sans-serif!important;font-size:.9rem!important;font-weight:600!important;letter-spacing:.02em!important;text-transform:none!important;color:var(--ink-soft)!important;background:transparent!important;border:1.5px solid transparent!important;border-radius:4px!important;padding:.55rem 1.35rem!important;cursor:pointer!important;transition:all .18s cubic-bezier(.4,0,.2,1)!important;white-space:nowrap!important}
div[data-testid="stRadio"] label>span:first-child{display:none!important}
div[data-testid="stRadio"] label:hover{background:var(--parchment-3)!important;border-color:var(--rule-strong)!important;color:var(--ink)!important}
div[data-testid="stRadio"] label:has(input:checked){background:var(--ink)!important;border-color:var(--ink)!important;box-shadow:3px 3px 0 var(--accent)!important;transform:translate(-1px,-1px)!important}
div[data-testid="stRadio"] label:has(input:checked) p,div[data-testid="stRadio"] label:has(input:checked) span{color:var(--parchment)!important}
div[data-testid="stRadio"] label p{font-family:'DM Sans',sans-serif!important;font-size:.9rem!important;font-weight:600!important;margin:0!important;line-height:1!important}
.conv-presets-sublabel{font-family:'DM Sans',sans-serif;font-size:.65rem;font-weight:700;text-transform:uppercase;letter-spacing:.14em;color:var(--ink-faint);margin-bottom:.65rem;margin-top:0}
.conv-input-card{background:var(--card-bg);border:1px solid var(--card-border);border-radius:6px;padding:1.3rem 1.5rem 1.4rem;margin-bottom:.5rem;box-shadow:0 1px 3px rgba(26,22,18,.05),0 6px 20px rgba(26,22,18,.06),inset 0 1px 0 rgba(255,255,255,.7)}
.conv-input-title{font-family:'Crimson Pro',Georgia,serif;font-size:1.3rem;font-weight:600;color:var(--ink);letter-spacing:-.02em;margin:0 0 .25rem 0;line-height:1.2}
.conv-input-hint{font-family:'Crimson Pro',Georgia,serif;font-style:italic;font-size:.93rem;color:var(--ink-faint);margin:0 0 .8rem 0;line-height:1.4}
.conv-result-card{background:rgba(46,107,122,.04);border:1px solid rgba(46,107,122,.18);border-left:3px solid var(--teal);border-radius:0 4px 4px 0;padding:.85rem 1.1rem;margin-top:.8rem}
.conv-result-label{font-family:'DM Sans',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.14em;color:var(--teal);margin-bottom:.55rem}
.conv-result-row{display:grid;grid-template-columns:8.5rem 1fr;gap:.35rem .9rem;align-items:baseline;padding:.12rem 0}
.conv-result-sublabel{font-family:'DM Sans',sans-serif;font-size:.62rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--ink-faint)}
.conv-result-subvalue{font-family:'Crimson Pro',Georgia,serif;font-size:1.05rem;font-weight:400;color:var(--ink);line-height:1.55;word-break:break-word}
.conv-error-card{background:rgba(184,92,56,.05);border:1px solid rgba(184,92,56,.2);border-left:3px solid var(--accent);border-radius:0 4px 4px 0;padding:.75rem 1.1rem;margin-top:.8rem}
.conv-error-text{font-family:'Crimson Pro',Georgia,serif;font-size:1rem;color:var(--accent);font-style:italic;margin:0}
.conv-empty-state{font-family:'Crimson Pro',Georgia,serif;font-style:italic;color:var(--ink-faint);padding:1.1rem 0}
.conv-caption{font-family:'DM Sans',sans-serif;font-size:.75rem;color:var(--ink-faint);line-height:1.55;margin-top:1rem}
.ng-main{font-size:1.95rem;font-weight:600;letter-spacing:-.01em;line-height:1.25}
.ng-muted{font-family:'DM Sans',sans-serif;font-size:.74rem;color:var(--ink-faint);letter-spacing:.02em}
.ng-alt{display:block;padding:.12rem 0;font-size:1.2rem;line-height:1.4}
.ng-figure{background:var(--card-bg);border:1px solid var(--card-border);border-radius:6px;padding:.7rem .9rem .5rem;margin-top:.8rem}
.ng-figure-label{font-family:'DM Sans',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.13em;color:var(--ink-faint);margin:.1rem 0 .4rem .1rem}
.ng-note{border:1px solid var(--rule);border-left:3px solid var(--ink-muted);background:var(--parchment-2);border-radius:0 4px 4px 0;padding:.7rem 1.05rem;margin-top:.8rem}
.ng-note-label{font-family:'DM Sans',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.13em;color:var(--ink-soft);margin-bottom:.3rem}
.ng-note p{font-family:'Crimson Pro',Georgia,serif;font-size:.97rem;color:var(--ink-muted);line-height:1.55;margin:0}
</style>"""
st.markdown(CONV_CSS, unsafe_allow_html=True)
st.markdown(CONV_CSS_ADDITIONS, unsafe_allow_html=True)

st.markdown("""
<div class="conv-masthead">
    <div class="conv-masthead-eyebrow">Numeral Converter</div>
    <div class="conv-masthead-title">Ngkolmpu Numerals</div>
    <div class="conv-masthead-desc">Convert between Arabic numerals and Ngkolmpu, a language of southern Papua that counts in sixes, with a word for each power of six up to 7,776 — the sizes of a yam count.</div>
</div>
""", unsafe_allow_html=True)

language_nav("Ngkolmpu", "converter")


def rows_html(rows):
    return "".join(
        f'<div class="conv-result-row">'
        f'<span class="conv-result-sublabel">{label}</span>'
        f'<span class="conv-result-subvalue">{value}</span>'
        f"</div>"
        for label, value in rows
    )


def note_html(label, text):
    return (f'<div class="ng-note"><div class="ng-note-label">{label}</div>'
            f"<p>{text}</p></div>")


def error_html(msg):
    return f'<div class="conv-error-card"><p class="conv-error-text">{msg}</p></div>'


def donohue_html(n):
    return "".join(
        f"<span class='ng-alt'><em>{form}</em> "
        f"<span class='ng-muted'>· {series} series, {note}</span></span>"
        for series, form, note in donohue_forms(n)
    )


def sixes_svg(n):
    """n dots in rows of six: complete sixes in the accent colour."""
    sixes, ones = counting_steps(n) if n < 36 else (6, 0)
    r, gap = 9, 26
    cells = []
    for i in range(36):
        row, col = divmod(i, 6)
        cx, cy = 16 + col * gap, 16 + row * gap
        if i < n and row < sixes:
            style = 'fill="var(--accent)"'
        elif i < n:
            style = 'fill="var(--ink-muted)"'
        else:
            style = 'fill="none" stroke="var(--rule-strong)" stroke-width="1.2"'
        cells.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" {style}/>')
    width = 16 * 2 + 5 * gap
    return (f'<svg viewBox="0 0 {width} {width}" width="{width}" height="{width}" '
            f'role="img" aria-label="{n} in rows of six">' + "".join(cells) + "</svg>")


def figure_html(n):
    if n == 36:
        caption = "Six full sixes — ptae, the first power word"
    else:
        sixes, ones = counting_steps(n)
        parts = []
        if sixes:
            parts.append(f"{sixes} six" + ("es" if sixes > 1 else ""))
        if ones:
            parts.append(f"{ones} one" + ("s" if ones > 1 else ""))
        caption = " and ".join(parts)
    return (f'<div class="ng-figure"><div class="ng-figure-label">{caption}</div>'
            f"{sixes_svg(n)}</div>")


EMPTY = '<div class="conv-empty-state"><p>Enter a value on the left to see the result.</p></div>'

arabic_input = ""
ng_input = ""

left_col, right_col = st.columns([1, 1], gap="large")

with right_col:
    st.markdown('<div class="conv-section-label conv-direction-label">Conversion Direction</div>',
                unsafe_allow_html=True)
    direction = st.radio(
        "Direction", ["Arabic → Ngkolmpu", "Ngkolmpu → Arabic"],
        horizontal=True, label_visibility="collapsed", key="ng_direction",
    )

with left_col:
    st.markdown('<div class="conv-section-label">Preset Examples</div>', unsafe_allow_html=True)
    if direction == "Arabic → Ngkolmpu":
        presets = [1, 5, 6, 7, 8, 13, 19, 30, 35, 36, 216, 7776]
        st.markdown('<p class="conv-presets-sublabel">Click a value to load it</p>', unsafe_allow_html=True)
        cols = st.columns(4)
        for i, num in enumerate(presets):
            if cols[i % 4].button(f"{num:,}", key=f"p_a_{i}", use_container_width=True):
                st.session_state["ng_arabic_input"] = str(num)

        st.markdown('<div class="conv-section-label">Convert</div>', unsafe_allow_html=True)
        st.markdown("""
<div class="conv-input-card">
    <div class="conv-input-title">Enter a number</div>
    <div class="conv-input-hint">1 to 35, or one of the powers of six: 36, 216, 1,296 or 7,776.</div>
</div>""", unsafe_allow_html=True)
        arabic_input = st.text_input(
            "Enter a number", key="ng_arabic_input",
            placeholder="e.g. 13", label_visibility="collapsed",
        )
    else:
        presets = ["naempr", "traowo", "naempr traowo naempr", "yempoka traowo naempr",
                   "ptae", "tarumpao", "ylla ptae", "ulamaeke"]
        st.markdown('<p class="conv-presets-sublabel">Click a form to load it</p>', unsafe_allow_html=True)
        cols = st.columns(2)
        for i, form in enumerate(presets):
            if cols[i % 2].button(form, key=f"p_b_{i}", use_container_width=True):
                st.session_state["ng_word_input"] = form

        st.markdown('<div class="conv-section-label">Convert</div>', unsafe_allow_html=True)
        st.markdown("""
<div class="conv-input-card">
    <div class="conv-input-title">Enter a Ngkolmpu numeral</div>
    <div class="conv-input-hint">Carroll's forms, or one of Donohue's older series such as <em>ylla ptae</em> (9). <em>æ</em> may be typed as <em>ae</em>.</div>
</div>""", unsafe_allow_html=True)
        ng_input = st.text_input(
            "Enter a Ngkolmpu numeral", key="ng_word_input",
            placeholder="e.g. yempoka traowo naempr", label_visibility="collapsed",
        )

with right_col:
    if direction == "Arabic → Ngkolmpu":
        if arabic_input:
            try:
                s_in = arabic_input.strip().replace(",", "")
                if not s_in.lstrip("-").isdigit():
                    raise ValueError("Please enter a whole number.")
                n = int(s_in)
                rows = [
                    ("Ngkolmpu", f'<span class="ng-main">{number_to_ngkolmpu(n)}</span>'),
                    ("Literally", literal(n)),
                    ("Source", source_note(n)),
                    ("In base six", f"{base_six(n)}<sub>6</sub>"),
                ]
                older = donohue_html(n)
                if older:
                    rows.append(("Donohue (1996 data)", older))
                st.markdown(
                    f'<div class="conv-result-card"><div class="conv-result-label">Ngkolmpu numeral</div>'
                    f"{rows_html(rows)}</div>",
                    unsafe_allow_html=True,
                )
                if n <= 36:
                    st.markdown(figure_html(n), unsafe_allow_html=True)
                if n in POWERS and n > 36:
                    st.markdown(note_html(
                        "A power of six",
                        f"{number_to_ngkolmpu(n)} is a single word for {n:,}. Carroll records these "
                        f"words in a yam-counting story — '…216, which is what we count to, that's the "
                        f"counting… 216, 1296 7776' — but not how the numbers between them were built.",
                    ), unsafe_allow_html=True)
                if n in (6, 12, 18, 24) or n in POWERS:
                    st.markdown(note_html(
                        "Two values for one word",
                        "In Donohue's 1996 data <em>ptae</em>, <em>tarwmpao</em>, <em>ntamnao</em> "
                        "and <em>wramaekr</em> mean either 6, 12, 18 and 24 or 36, 216, 1,296 and "
                        "7,776. Evans (2009) reads the first set as counts through cycles of six. "
                        "Carroll's speakers use only the second.",
                    ), unsafe_allow_html=True)
            except ValueError as exc:
                st.markdown(error_html(exc), unsafe_allow_html=True)
        else:
            st.markdown(EMPTY, unsafe_allow_html=True)
    else:
        if ng_input:
            try:
                readings = ngkolmpu_lookup(ng_input)
                n, who = readings[0]
                rows = [("Arabic numeral", f'<span class="ng-main">{n:,}</span>'),
                        ("Reading", who + (" (2016–2019)" if who == "Carroll" else
                                           " (1996 data)" if who.startswith("Donohue") else ""))]
                if n <= MAX_COUNT or n in POWERS:
                    rows.append(("Carroll's form", number_to_ngkolmpu(n)))
                    rows.append(("Literally", literal(n)))
                others = sorted({(v, w) for v, w in readings[1:] if v != n})
                if others:
                    rows.append(("Also read as", "; ".join(f"{v:,} ({w})" for v, w in others)))
                st.markdown(
                    f'<div class="conv-result-card"><div class="conv-result-label">Arabic numeral</div>'
                    f"{rows_html(rows)}</div>",
                    unsafe_allow_html=True,
                )
                if n <= 36:
                    st.markdown(figure_html(n), unsafe_allow_html=True)
            except ValueError as exc:
                st.markdown(error_html(exc), unsafe_allow_html=True)
        else:
            st.markdown(EMPTY, unsafe_allow_html=True)

    st.markdown("""
<div class="conv-caption">
Ngkolmpu as recorded by Matthew Carroll: his ANU thesis (2016) for one to six and the powers of
six, and his 2018 blog post and 2019 entry in Chan's <em>Numeral Systems of the World's Languages</em>
for the sixes in between. Mark Donohue's three older series, from fieldwork in 1996, are shown as
Carroll (2016) and Evans (2009) reproduce them. Algorithm by Yi Zou.
</div>
""", unsafe_allow_html=True)

footer_nav("Ngkolmpu", "converter")
