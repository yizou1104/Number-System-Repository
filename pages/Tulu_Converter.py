import streamlit as st

from ui import apply_global_styles, language_nav, CONV_CSS_ADDITIONS, footer_nav
from Tulu import (
    PRONUNCIATION, number_to_tulu, tulu_romanised, tulu_to_number,
    kannada_digits, indian_grouping, source_note, alternatives, breakdown,
)
from Tulu import alternative_strings  # noqa: F401 — entry point for the page checks

# ============================================================
# TULU CONVERTER
# Data, sources and logic live in Tulu.py.
# ============================================================

st.set_page_config(page_title="Tulu Numeral Converter", layout="wide")
apply_global_styles()

CONV_CSS = """<style>
/* Kannada script for the Tulu forms; Charis SIL, subset to the IPA characters used, for pronunciations */
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+Kannada:wght@400;600&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Charis+SIL&text=%20abdeilmnoprstu~%C9%96%C9%AF%C9%B2%C9%B3%C9%BE%CA%8B%CA%92%CB%90%CC%AA%CD%A1%E2%81%B1&display=swap');
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
.tu-main{font-size:1.95rem;font-weight:600;letter-spacing:-.01em;line-height:1.25}
.tu-muted{font-family:'DM Sans',sans-serif;font-size:.74rem;color:var(--ink-faint);letter-spacing:.02em}
.tu-alt{display:block;padding:.12rem 0;font-size:1.2rem;line-height:1.4}
.tu-figure{background:var(--card-bg);border:1px solid var(--card-border);border-radius:6px;padding:.7rem .9rem .5rem;margin-top:.8rem}
.tu-figure-label{font-family:'DM Sans',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.13em;color:var(--ink-faint);margin:.1rem 0 .4rem .1rem}
.tu-note{border:1px solid var(--rule);border-left:3px solid var(--ink-muted);background:var(--parchment-2);border-radius:0 4px 4px 0;padding:.7rem 1.05rem;margin-top:.8rem}
.tu-note-label{font-family:'DM Sans',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.13em;color:var(--ink-soft);margin-bottom:.3rem}
.tu-note p{font-family:'Crimson Pro',Georgia,serif;font-size:.97rem;color:var(--ink-muted);line-height:1.55;margin:0}
.tu-kn{font-family:'Noto Serif Kannada','Crimson Pro',serif}
.tu-main{font-family:'Noto Serif Kannada','Crimson Pro',serif;font-size:1.85rem;font-weight:600;line-height:1.5}
.tu-digits{font-family:'Noto Serif Kannada',serif;font-size:1.45rem;font-weight:600}
.tu-ipa{font-family:'Charis SIL',serif;font-size:1.15rem}
.tu-digit-note{border:1px solid rgba(184,92,56,.35);border-left:3px solid var(--accent);background:rgba(184,92,56,.05);border-radius:0 4px 4px 0;padding:.75rem 1.05rem;margin:.9rem 0 .2rem}
.tu-digit-note-label{font-family:'DM Sans',sans-serif;font-size:.62rem;font-weight:700;text-transform:uppercase;letter-spacing:.13em;color:var(--accent);margin-bottom:.3rem}
.tu-digit-note p{font-family:'Crimson Pro',Georgia,serif;font-size:.98rem;color:var(--ink-muted);line-height:1.55;margin:0}
.tu-digit-row{font-family:'Noto Serif Kannada',serif;font-size:1.05rem;color:var(--ink);letter-spacing:.25em}
.tu-parts{background:var(--card-bg);border:1px solid var(--card-border);border-radius:6px;padding:.8rem 1.05rem;margin-top:.8rem}
.tu-parts-label{font-family:'DM Sans',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.13em;color:var(--ink-faint);margin-bottom:.45rem}
.tu-parts-row{display:grid;grid-template-columns:4.6rem minmax(6rem,1.3fr) minmax(6rem,1.2fr) minmax(6rem,1.3fr);gap:.3rem .8rem;align-items:baseline;padding:.28rem 0;border-bottom:1px solid var(--rule)}
.tu-parts-row:last-child{border-bottom:none}
.tu-parts-head{font-family:'DM Sans',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--ink-faint)}
.tu-parts-val{font-family:'DM Sans',sans-serif;font-size:.85rem;color:var(--ink-soft)}
.tu-parts-kn{font-family:'Noto Serif Kannada',serif;font-size:1.02rem;color:var(--ink)}
.tu-parts-rom{font-family:'Crimson Pro',Georgia,serif;font-size:1rem;font-style:italic;color:var(--ink-muted)}
</style>"""
st.markdown(CONV_CSS, unsafe_allow_html=True)
st.markdown(CONV_CSS_ADDITIONS, unsafe_allow_html=True)

st.markdown("""
<div class="conv-masthead">
    <div class="conv-masthead-eyebrow">Numeral Converter</div>
    <div class="conv-masthead-title">Tulu Numerals</div>
    <div class="conv-masthead-desc">Convert between Arabic numerals and Tulu, a Dravidian language of coastal Karnataka and Kerala written in the Kannada script. Tulu has no digits of its own in Unicode, so its numbers are written here in Kannada digits.</div>
</div>
""", unsafe_allow_html=True)

language_nav("Tulu", "converter")


def rows_html(rows):
    return "".join(
        f'<div class="conv-result-row">'
        f'<span class="conv-result-sublabel">{label}</span>'
        f'<span class="conv-result-subvalue">{value}</span>'
        f"</div>"
        for label, value in rows
    )


def note_html(label, text):
    return (f'<div class="tu-note"><div class="tu-note-label">{label}</div>'
            f"<p>{text}</p></div>")


def error_html(msg):
    return f'<div class="conv-error-card"><p class="conv-error-text">{msg}</p></div>'


def breakdown_html(n):
    head = ('<div class="tu-parts-row"><span class="tu-parts-head">Value</span>'
            '<span class="tu-parts-head">Word</span><span class="tu-parts-head">Romanised</span>'
            '<span class="tu-parts-head">In this number</span></div>')
    body = "".join(
        f'<div class="tu-parts-row"><span class="tu-parts-val">{v}</span>'
        f'<span class="tu-parts-kn">{wk}</span><span class="tu-parts-rom">{wr}</span>'
        f'<span class="tu-parts-kn">{shape}</span></div>'
        for v, wk, wr, shape in breakdown(n)
    )
    return f'<div class="tu-parts"><div class="tu-parts-label">Part by part</div>{head}{body}</div>'


def result_rows(n):
    rows = [
        ("Tulu", f'<span class="tu-main">{number_to_tulu(n)}</span>'),
        ("Romanised", f"<em>{tulu_romanised(n)}</em> <span class='tu-muted'>· Brigel's spelling (1872)</span>"),
        ("Kannada digits", f'<span class="tu-digits">{kannada_digits(n)}</span> '
                           f"<span class='tu-muted'>· the digits used for Tulu; it has none of its own</span>"),
    ]
    if n in PRONUNCIATION:
        rows.append(("Pronunciation today",
                     f'<span class="tu-ipa">{PRONUNCIATION[n]}</span> '
                     f"<span class='tu-muted'>· D'Souza (2019)</span>"))
    alts = "".join(
        f"<span class='tu-alt'><span class='tu-kn'>{k}</span> <em>{r}</em> "
        f"<span class='tu-muted'>· {who}</span></span>"
        for k, r, who in alternatives(n)
    )
    if alts:
        rows.append(("Also recorded", alts))
    rows.append(("Source", source_note(n)))
    return rows


DIGIT_NOTE = """
<div class="tu-digit-note">
    <div class="tu-digit-note-label">About the digits: these are Kannada digits</div>
    <p>Unicode encodes no digits for Tulu's own Tulu-Tigalari script, and lists the Kannada digits
    under it instead (Unicode 18.0). Brigel's 1872 grammar already printed Tulu numbers this way.
    Seven proposals since 2021 have asked Unicode for separate Tulu digits, and none has been
    accepted; the <a href="/Tulu_Linguistics" target="_self">grammar page</a> links to each.</p>
    <p class="tu-digit-row" style="margin-top:.45rem">೦ ೧ ೨ ೩ ೪ ೫ ೬ ೭ ೮ ೯</p>
</div>"""

EMPTY = '<div class="conv-empty-state"><p>Enter a value on the left to see the result.</p></div>'

arabic_input = ""
tu_input = ""

left_col, right_col = st.columns([1, 1], gap="large")

with right_col:
    st.markdown('<div class="conv-section-label conv-direction-label">Conversion Direction</div>',
                unsafe_allow_html=True)
    direction = st.radio(
        "Direction", ["Arabic → Tulu", "Tulu → Arabic"],
        horizontal=True, label_visibility="collapsed", key="tu_direction",
    )
    st.markdown(DIGIT_NOTE, unsafe_allow_html=True)

with left_col:
    st.markdown('<div class="conv-section-label">Preset Examples</div>', unsafe_allow_html=True)
    if direction == "Arabic → Tulu":
        presets = [0, 7, 11, 19, 21, 25, 39, 90, 101, 150, 1001, 1200]
        st.markdown('<p class="conv-presets-sublabel">Click a value to load it</p>', unsafe_allow_html=True)
        cols = st.columns(4)
        for i, num in enumerate(presets):
            if cols[i % 4].button(f"{num:,}", key=f"p_a_{i}", use_container_width=True):
                st.session_state["tu_arabic_input"] = str(num)

        st.markdown('<div class="conv-section-label">Convert</div>', unsafe_allow_html=True)
        st.markdown("""
<div class="conv-input-card">
    <div class="conv-input-title">Enter a number</div>
    <div class="conv-input-hint">0 to 99,999, or 1,00,000 (a lakh) or 1,00,00,000 (a crore). Kannada digits such as ೨೫ work too.</div>
</div>""", unsafe_allow_html=True)
        arabic_input = st.text_input(
            "Enter a number", key="tu_arabic_input",
            placeholder="e.g. 25", label_visibility="collapsed",
        )
    else:
        presets = ["ಒಂಜಿ", "ಒರ್ಮ್ಬ", "ಇರ್ವತೊಂಜಿ", "ಸೊಣ್ಪ", "ನೂತವೊಂಜಿ", "ಸಾರ", "irvatụeinụ", "ಲಕ್ಷ"]
        st.markdown('<p class="conv-presets-sublabel">Click a form to load it</p>', unsafe_allow_html=True)
        cols = st.columns(2)
        for i, form in enumerate(presets):
            if cols[i % 2].button(form, key=f"p_b_{i}", use_container_width=True):
                st.session_state["tu_word_input"] = form

        st.markdown('<div class="conv-section-label">Convert</div>', unsafe_allow_html=True)
        st.markdown("""
<div class="conv-input-card">
    <div class="conv-input-title">Enter a Tulu numeral</div>
    <div class="conv-input-hint">In Kannada script, in Brigel's romanisation with or without accents (<em>irvatueinu</em>), or in Kannada digits.</div>
</div>""", unsafe_allow_html=True)
        tu_input = st.text_input(
            "Enter a Tulu numeral", key="tu_word_input",
            placeholder="e.g. ಇರ್ವತ್ಐನ್", label_visibility="collapsed",
        )

with right_col:
    if direction == "Arabic → Tulu":
        if arabic_input:
            try:
                raw = arabic_input.strip().replace(",", "").replace(" ", "")
                raw = raw.translate(str.maketrans("೦೧೨೩೪೫೬೭೮೯", "0123456789"))
                negative = raw.startswith("-")
                digits = raw[1:] if negative else raw
                if not digits.isdecimal():
                    raise ValueError("Please enter a whole number.")
                # past any range the converter covers; avoids Python's limit on very long integers
                n = int(digits) if len(digits.lstrip("0")) <= 18 else 10 ** 18
                n = -n if negative else n
                st.markdown(
                    f'<div class="conv-result-card"><div class="conv-result-label">Tulu numeral</div>'
                    f"{rows_html(result_rows(n))}</div>",
                    unsafe_allow_html=True,
                )
                if len(breakdown(n)) > 1:
                    st.markdown(breakdown_html(n), unsafe_allow_html=True)
                if n == 1000:
                    st.markdown(note_html(
                        "Thousand today",
                        "Brigel's word is <em>sāra</em>. Both lists in Chan's database, from 1995 "
                        "and 2019, give <em>saːvira</em> or <em>saːʋiɾa</em> for 1,000, though the "
                        "older one (Shetty 1995) still has <em>saːra</em> in 2,000.",
                    ), unsafe_allow_html=True)
                if source_note(n) == "built by Brigel's patterns":
                    st.markdown(note_html(
                        "Built by pattern",
                        "Brigel prints 1 to 25, the tens, every hundred, and examples of each "
                        "joining form (101, 150, 1,001, 1,020, 1,200, 11,000); this number follows "
                        "the same patterns. Männer's dictionary confirms the pattern beyond the "
                        "twenties with 39, <em>muppa-tormba</em>.",
                    ), unsafe_allow_html=True)
            except ValueError as exc:
                st.markdown(error_html(exc), unsafe_allow_html=True)
        else:
            st.markdown(EMPTY, unsafe_allow_html=True)
    else:
        if tu_input:
            try:
                n = tulu_to_number(tu_input)
                rows = [
                    ("Arabic numeral", f'<span class="tu-main" style="font-family:Crimson Pro,serif">{indian_grouping(n)}</span>'),
                    ("Kannada digits", f'<span class="tu-digits">{kannada_digits(n)}</span>'),
                    ("Tulu", f'<span class="tu-kn" style="font-size:1.3rem">{number_to_tulu(n)}</span>'),
                    ("Romanised", f"<em>{tulu_romanised(n)}</em>"),
                    ("Source", source_note(n)),
                ]
                st.markdown(
                    f'<div class="conv-result-card"><div class="conv-result-label">Arabic numeral</div>'
                    f"{rows_html(rows)}</div>",
                    unsafe_allow_html=True,
                )
            except ValueError as exc:
                st.markdown(error_html(exc), unsafe_allow_html=True)
        else:
            st.markdown(EMPTY, unsafe_allow_html=True)

    st.markdown("""
<div class="conv-caption">
Tulu forms in Kannada script and romanisation as printed in J. Brigel's <em>A Grammar of the Tulu
Language</em> (1872), with zero and 39 from A. Männer's <em>Tulu–English Dictionary</em> (1886), and
numbers between Brigel's examples built by his patterns. Pronunciations are Royson Norman D'Souza's
(2019) in Chan's <em>Numeral Systems of the World's Languages</em>. Algorithm by Yi Zou.
</div>
""", unsafe_allow_html=True)

footer_nav("Tulu", "converter")
