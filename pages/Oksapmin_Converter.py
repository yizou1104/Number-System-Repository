import streamlit as st

from ui import apply_global_styles, language_nav, CONV_CSS_ADDITIONS, footer_nav
from Oksapmin import (
    UPPER_QUANTITY, LOWER_QUANTITY, SECOND_CIRCUIT, MAX_COUNT,
    TEN_DROPPED_FROM, OK_SVG_CSS, number_to_oksapmin, oksapmin_lookup,
    gloss, literal, variants, side, body_svg, saxe_spelling,
)
from Oksapmin import oksapmin_to_number  # noqa: F401 — entry point for the audit scripts

# ============================================================
# OKSAPMIN BODY-TALLY CONVERTER
# Data, sources and logic live in Oksapmin.py.
# ============================================================

# ============================================================
# PAGE CONFIG & STYLES
# ============================================================
st.set_page_config(page_title="Oksapmin Numeral Converter", layout="wide")
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
.ok-form{font-family:'DM Mono','Courier New',monospace;font-size:1.25rem;color:var(--ink)}
.ok-mono{font-family:'DM Mono','Courier New',monospace;font-size:.95rem;color:var(--ink)}
.ok-figure{background:var(--card-bg);border:1px solid var(--card-border);border-radius:6px;padding:.6rem .8rem .2rem;margin-top:.8rem}
.ok-figure-label{font-family:'DM Sans',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.13em;color:var(--ink-faint);margin:.2rem 0 .1rem .2rem}
.ok-note{border:1px solid var(--rule);border-left:3px solid var(--ink-muted);background:var(--parchment-2);border-radius:0 4px 4px 0;padding:.7rem 1.05rem;margin-top:.8rem}
.ok-note-label{font-family:'DM Sans',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.13em;color:var(--ink-soft);margin-bottom:.3rem}
.ok-note p{font-family:'Crimson Pro',Georgia,serif;font-size:.97rem;color:var(--ink-muted);line-height:1.55;margin:0}
</style>"""
st.markdown(CONV_CSS, unsafe_allow_html=True)
st.markdown(CONV_CSS_ADDITIONS, unsafe_allow_html=True)
st.markdown(OK_SVG_CSS, unsafe_allow_html=True)

st.markdown("""
<div class="conv-masthead">
    <div class="conv-masthead-eyebrow">Numeral Converter</div>
    <div class="conv-masthead-title">Oksapmin Numerals</div>
    <div class="conv-masthead-desc">Convert between Arabic numerals and the Oksapmin body tally of Papua New Guinea — twenty-seven named points running from one thumb, over the face, to the other hand.</div>
</div>
""", unsafe_allow_html=True)

language_nav("Oksapmin", "converter")


def rows_html(rows):
    return "".join(
        f'<div class="conv-result-row">'
        f'<span class="conv-result-sublabel">{label}</span>'
        f'<span class="conv-result-subvalue">{value}</span>'
        f"</div>"
        for label, value in rows
    )


def note_html(label, text):
    return (f'<div class="ok-note"><div class="ok-note-label">{label}</div>'
            f"<p>{text}</p></div>")


def error_html(msg):
    return f'<div class="conv-error-card"><p class="conv-error-text">{msg}</p></div>'


def figure_html(dialect, active, caption):
    return (f'<div class="ok-figure"><div class="ok-figure-label">{caption}</div>'
            f"{body_svg(dialect, active)}</div>")


DIALECT_LABELS = {"upper": "Upper Oksapmin", "lower": "Lower Oksapmin"}
SOURCES = {
    "upper": "Lawrence (2018), corroborated by Saxe (1981)",
    "lower": "Loughnane (2009) for 1–16; Loughnane (2008) for 17–27",
}

direction = st.radio(
    "Direction",
    ["Arabic → Oksapmin", "Oksapmin → Arabic"],
    horizontal=True,
    label_visibility="collapsed",
)

left_col, right_col = st.columns([1, 1], gap="large")

arabic_input = ""
ok_input = ""

with left_col:
    st.markdown('<div class="conv-section-label">Dialect</div>', unsafe_allow_html=True)
    dialect_label = st.radio(
        "Dialect",
        ["Upper Oksapmin", "Lower Oksapmin"],
        horizontal=True,
        label_visibility="collapsed",
        key="ok_dialect",
    )
    dialect = "upper" if dialect_label.startswith("Upper") else "lower"
    other = "lower" if dialect == "upper" else "upper"
    st.markdown(
        '<div class="conv-caption" style="margin-top:.4rem">The two dialects are mutually '
        'intelligible but use different words, and count the second hand in opposite '
        'directions.</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="conv-section-label">Preset Examples</div>', unsafe_allow_html=True)
    if direction == "Arabic → Oksapmin":
        presets = [1, 5, 6, 10, 12, 14, 15, 20, 22, 23, 27, 29]
        st.markdown('<p class="conv-presets-sublabel">Click a value to load it</p>', unsafe_allow_html=True)
        cols = st.columns(4)
        for i, num in enumerate(presets):
            if cols[i % 4].button(str(num), key=f"p_a_{i}", use_container_width=True):
                st.session_state["ok_arabic_input"] = str(num)

        st.markdown('<div class="conv-section-label">Convert</div>', unsafe_allow_html=True)
        st.markdown("""
<div class="conv-input-card">
    <div class="conv-input-title">Enter a number (1–27)</div>
    <div class="conv-input-hint">One circuit of the body. In Upper Oksapmin, 28 and 29 show how the count turns back up the arm.</div>
</div>""", unsafe_allow_html=True)
        arabic_input = st.text_input(
            "Enter a number",
            key="ok_arabic_input",
            placeholder="e.g. 14",
            label_visibility="collapsed",
        )
    else:
        presets = ["tiβəna", "nata", "ɾuma", "tən kina", "tən xətxəta",
                   "tipun tən", "xətxət tən", "tan-besa", "amun=xe", "tit pu"]
        st.markdown('<p class="conv-presets-sublabel">Click a form to load it</p>', unsafe_allow_html=True)
        cols = st.columns(2)
        for i, form in enumerate(presets):
            if cols[i % 2].button(form, key=f"p_b_{i}", use_container_width=True):
                st.session_state["ok_word_input"] = form

        st.markdown('<div class="conv-section-label">Convert</div>', unsafe_allow_html=True)
        st.markdown("""
<div class="conv-input-card">
    <div class="conv-input-title">Enter an Oksapmin form</div>
    <div class="conv-input-hint">Either dialect, or Saxe's spelling. Without special letters, type ə as <em>a</em>, x as <em>h</em>, β as <em>p</em> and ɾ as <em>r</em> — Lawrence's practical spelling: <em>tipana</em> for tiβəna.</div>
</div>""", unsafe_allow_html=True)
        ok_input = st.text_input(
            "Enter an Oksapmin form",
            key="ok_word_input",
            placeholder="e.g. tən kina",
            label_visibility="collapsed",
        )

with right_col:
    if direction == "Arabic → Oksapmin":
        if arabic_input:
            val = arabic_input.strip()
            if val.lstrip("-").isdigit():
                try:
                    n = int(val)
                    form = number_to_oksapmin(n, dialect)
                    rows = [(DIALECT_LABELS[dialect], f'<span class="ok-form">{form}</span>')]
                    if variants(n, dialect):
                        rows.append(("Variants", f'<span class="ok-mono">{" ~ ".join(variants(n, dialect))}</span>'))
                    rows.append(("Body point", f"{gloss(n, dialect)} <span style='color:var(--ink-faint)'>· {side(n)}</span>"))
                    rows.append(("Literal", f"'{literal(n, dialect)}'"))
                    if dialect == "upper":
                        rows.append(("Saxe (1981)", f'<span class="ok-mono">{saxe_spelling(n)}</span>'))
                        if n <= MAX_COUNT:
                            q = UPPER_QUANTITY[n]
                            if n == MAX_COUNT:
                                q += " &nbsp;·&nbsp; as a unit: <em>tit pu</em> 'once around the body'"
                            rows.append(("Counting things", f'<span class="ok-mono">{q}</span>'))
                    elif n in LOWER_QUANTITY:
                        q, status, where = LOWER_QUANTITY[n]
                        rows.append(("Counting things",
                                     f'<span class="ok-mono">{q}</span> '
                                     f"<span style='color:var(--ink-faint)'>· {status}, {where}</span>"))
                    if n <= MAX_COUNT:
                        rows.append((DIALECT_LABELS[other],
                                     f'<span class="ok-mono">{number_to_oksapmin(n, other)}</span> '
                                     f"<span style='color:var(--ink-faint)'>· {gloss(n, other)}</span>"))
                    st.markdown(
                        f'<div class="conv-result-card">'
                        f'<div class="conv-result-label">Oksapmin numeral</div>'
                        f"{rows_html(rows)}</div>",
                        unsafe_allow_html=True,
                    )
                    st.markdown(figure_html(dialect, n, f"{DIALECT_LABELS[dialect]} — the count, point by point"),
                                unsafe_allow_html=True)

                    if n in SECOND_CIRCUIT:
                        first = SECOND_CIRCUIT[n]
                        st.markdown(note_html(
                            "Second pass",
                            f"Past 27 the count turns back up the arm. {n} is the same word as "
                            f"{first} — Saxe &amp; Esmonde (2004) note that the 21st and 29th points "
                            f"are both <em>tan-besa</em>. Only the pointing gesture, and the listener's "
                            f"memory of how far the count has gone, tells them apart.",
                        ), unsafe_allow_html=True)
                    elif dialect == "upper" and n >= TEN_DROPPED_FROM:
                        st.markdown(note_html(
                            "Often shortened",
                            f"Lawrence notes that from 23 onward <em>tən</em> is often left out, "
                            f"leaving <em>{form.removeprefix('tən ')}</em> — the same word as "
                            f"{n - 22}. The gesture shows which hand is meant. Saxe's list and "
                            f"Lawrence's agree that this hand is counted thumb first, though "
                            f"Lawrence's own prose summary describes the reverse order.",
                        ), unsafe_allow_html=True)
                    elif dialect == "lower" and n >= 17:
                        st.markdown(note_html(
                            "Single source",
                            "Loughnane's grammar lists the count only to 16. Forms from 17 come "
                            "from her 2008 entry in Chan's numeral database, the only record of "
                            "this dialect's second side — including its mirror-image finger order.",
                        ), unsafe_allow_html=True)
                except ValueError as exc:
                    st.markdown(error_html(exc), unsafe_allow_html=True)
            else:
                st.markdown(error_html("Please enter a whole number."), unsafe_allow_html=True)
        else:
            st.markdown(
                '<div class="conv-empty-state"><p>Enter a value on the left to see the result.</p></div>',
                unsafe_allow_html=True,
            )
    else:
        if ok_input:
            try:
                hits = oksapmin_lookup(ok_input)
                n, hit_dialect, role, note = hits[0]
                label = {"counting": "Count", "counting things": "Counting things",
                         "unit": "Unit"}[role]
                rows = [
                    ("Value", f"<strong>{n}</strong>"),
                    ("Dialect", DIALECT_LABELS[hit_dialect]),
                    ("Body point", f"{gloss(n, hit_dialect)} <span style='color:var(--ink-faint)'>· {side(n)}</span>"),
                    ("Use", label + (f" — {note}" if note else "")),
                ]
                st.markdown(
                    f'<div class="conv-result-card">'
                    f'<div class="conv-result-label">Arabic numeral</div>'
                    f"{rows_html(rows)}</div>",
                    unsafe_allow_html=True,
                )
                others = [h for h in hits[1:] if (h[0], h[1]) != (n, hit_dialect)]
                if others:
                    listed = "; ".join(
                        f"<strong>{h[0]}</strong> in {DIALECT_LABELS[h[1]]}"
                        + (f" ({h[3]})" if h[3] else "")
                        for h in others
                    )
                    st.markdown(note_html("Also read as", listed), unsafe_allow_html=True)
                if n in (21, 22) and hit_dialect == "upper":
                    st.markdown(note_html(
                        "Second pass",
                        f"On a second circuit the same word names {29 if n == 21 else 28} "
                        f"(Saxe &amp; Esmonde 2004).",
                    ), unsafe_allow_html=True)
                st.markdown(figure_html(hit_dialect, n, f"{DIALECT_LABELS[hit_dialect]} — point {n}"),
                            unsafe_allow_html=True)
            except ValueError as exc:
                st.markdown(error_html(exc), unsafe_allow_html=True)
        else:
            st.markdown(
                '<div class="conv-empty-state"><p>Enter a form on the left to see the result.</p></div>',
                unsafe_allow_html=True,
            )

    st.markdown("""
<div class="conv-caption">
Upper Oksapmin follows Marshall Lawrence's 2018 entry in Chan's <em>Numeral Systems of the World's
Languages</em>, with Saxe's (1981) transcription of the same count alongside. Lower Oksapmin follows
Robyn Loughnane's <em>A Grammar of Oksapmin</em> (2009) and her 2008 database entry. Forms are
reproduced as each source prints them; nothing is generated beyond what they record.
</div>
""", unsafe_allow_html=True)

footer_nav("Oksapmin", "converter")
