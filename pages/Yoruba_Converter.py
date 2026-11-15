import streamlit as st
from ui import apply_global_styles, language_nav, CONV_CSS_ADDITIONS, footer_nav

# ============================================================
# YORUBA NUMERALS
# The forms Ethelbert Kari gave for Chan's numeral database (1998), taken
# from Armstrong's Yoruba Numerals (1962), with the IPA letter ɡ written g.
# Only recorded numbers are given: Bowen (1858) shows how the others are
# built, but without tone marks, so they are not generated.
# ============================================================

KARI = {
    1: "o\u00f3kan",
    2: "e\u00e9j\u00ec",
    3: "\u1eb9\u1eb9\u0301ta",
    4: "\u1eb9\u1eb9\u0301rin",
    5: "a\u00e1r\u00f9n",
    6: "\u1eb9\u1eb9\u0301f\u00e0",
    7: "\u1eb9\u1eb9\u0301je",
    8: "\u1eb9\u1eb9\u0301j\u1ecd",
    9: "\u1eb9\u1eb9\u0301s\u00e0n",
    10: "\u1eb9\u1eb9\u0301w\u00e0\u00e1",
    11: "o\u00f3k\u00e0n l\u00e0\u00e1",
    12: "e\u00e9j\u00ec l\u00e0\u00e1",
    13: "\u1eb9\u1eb9\u0301t\u00e0 l\u00e0\u00e1",
    14: "\u1eb9\u1eb9\u0301r\u00ecn l\u00e0\u00e1",
    15: "\u1eb9\u0300\u1eb9\u0301dog\u00fan",
    16: "\u1eb9\u1eb9\u0301r\u00ecn d\u00edn l\u00f3g\u00fan",
    17: "\u1eb9\u1eb9\u0301t\u00e0 d\u00edn l\u00f3g\u00fan",
    18: "e\u00e9j\u00ec d\u00edn l\u00f3g\u00fan",
    19: "o\u00f3k\u00e0n d\u00edn l\u00f3g\u00fan",
    20: "og\u00fan",
    21: "o\u00f3k\u00e0n l\u00e9 l\u00f3g\u00fan",
    22: "e\u00e9j\u00ec l\u00e9 l\u00f3g\u00fan",
    23: "\u1eb9\u1eb9\u0301t\u00e0 l\u00e9 l\u00f3g\u00fan",
    24: "\u1eb9\u1eb9\u0301r\u00ecn l\u00e9 l\u00f3g\u00fan",
    25: "\u1eb9\u0300\u1eb9\u0301d\u1ecd\u0300\u1ecd\u0301gb\u1ecd\u0300\u01f9",
    26: "\u1eb9\u1eb9\u0301r\u00ecn d\u00edn l\u1ecdgb\u1ecd\u0300n",
    27: "\u1eb9\u1eb9\u0301t\u00e0 d\u00edn l\u1ecdgb\u1ecd\u0300n",
    28: "e\u00e9j\u00ec d\u00edn l\u1ecdgb\u1ecd\u0300n",
    29: "o\u00f3k\u00e0n d\u00edn l\u1ecdgb\u1ecd\u0300n",
    30: "\u1ecdgb\u1ecd\u0300n",
    50: "\u00e0\u00e1d\u1ecd\u0301ta",
    60: "\u1ecdg\u1ecd\u0301ta",
    70: "\u00e0\u00e1d\u1ecd\u0301rin",
    80: "\u1ecdg\u1ecd\u0301rin",
    90: "\u00e0\u00e1d\u1ecd\u0301r\u00f9\u0144",
    100: "\u1ecdg\u1ecd\u0301r\u00f9n",
    200: "igba",
    400: "ir\u00ednw\u00f3",
    1000: "\u1eb9gb\u1eb9\u0300r\u00fan",
    2000: "\u1eb9gb\u1eb9\u0300w\u00e1"
}

# Kari prints 40 as ọgbọ̀ji, which runs 30 (ọgbọ̀n) into forty; Crowther (1852)
# and Bowen (1858) both give ogoji, from ogún èjì 'twenty two', without tones.
FORTY = "ogoji"

ALTERNATIVES = {
    100: [("\u1ecd\u0300r\u00fan", "Kari (1998)")],
    2000: [("\u1eb9gb\u00e0\u00e1", "Kari (1998)")],
}

# Bowen (1858), section 209: how numbers between the recorded ones are built
BOWEN_EXAMPLES = "35 is 'five from forty', 45 'five from fifty', 101 'one laid on a hundred'"


def number_to_yoruba(n):
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"Expected int, got {type(n).__name__}")
    if n < 0:
        raise ValueError("Negative numbers are not supported.")
    if n == 0:
        raise ValueError("None of the sources consulted gives a Yoruba word for zero.")
    if n == 40:
        return FORTY
    if n in KARI:
        return KARI[n]
    raise ValueError(
        f"Kari's list (from Armstrong 1962) records 1 to 30, the tens to 100, and 200, "
        f"400, 1,000 and 2,000. Bowen (1858) shows how the rest are built — {BOWEN_EXAMPLES} "
        f"— but without tone marks, so {n:,} is not written out here."
    )


# ============================================================
# PAGE CONFIG & STYLES
# ============================================================
st.set_page_config(page_title='Yoruba Numeral Converter', layout='wide')
apply_global_styles()

CONV_CSS = '<style>\n.conv-masthead{border-top:3px solid var(--ink);border-bottom:1px solid var(--rule);padding:1.75rem 0 1.4rem 0;margin-bottom:1.75rem}\n.conv-masthead-eyebrow{font-family:\'DM Sans\',sans-serif;font-size:.68rem;font-weight:700;text-transform:uppercase;letter-spacing:.18em;color:var(--accent);display:flex;align-items:center;gap:.65rem;margin-bottom:.65rem}\n.conv-masthead-eyebrow::before{content:\'\';display:inline-block;width:1.75rem;height:1.5px;background:var(--accent);flex-shrink:0}\n.conv-masthead-title{font-family:\'Crimson Pro\',Georgia,serif;font-size:3rem;font-weight:700;color:var(--ink);letter-spacing:-.04em;line-height:1.05;margin-bottom:.5rem}\n.conv-masthead-desc{font-family:\'Crimson Pro\',Georgia,serif;font-style:italic;font-size:1.05rem;color:var(--ink-muted);line-height:1.55;margin:0}\n.conv-section-label{font-family:\'DM Sans\',sans-serif;font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.16em;color:var(--ink-soft);display:flex;align-items:center;gap:1rem;margin:2rem 0 1rem 0}\n.conv-section-label::before{content:\'\';display:inline-block;width:2rem;height:1px;background:var(--ink-muted);flex-shrink:0}\n.conv-section-label::after{content:\'\';flex:1;height:1px;background:var(--rule)}\ndiv[data-testid="stRadio"]>div{display:flex;gap:0;background:var(--card-bg);border:1px solid var(--card-border);border-radius:6px;padding:.35rem;box-shadow:0 1px 3px rgba(26,22,18,.05),0 4px 14px rgba(26,22,18,.04),inset 0 1px 0 rgba(255,255,255,.65);width:fit-content}\ndiv[data-testid="stRadio"] label{display:flex!important;align-items:center!important;font-family:\'DM Sans\',sans-serif!important;font-size:.9rem!important;font-weight:600!important;letter-spacing:.02em!important;text-transform:none!important;color:var(--ink-soft)!important;background:transparent!important;border:1.5px solid transparent!important;border-radius:4px!important;padding:.55rem 1.35rem!important;cursor:pointer!important;transition:all .18s cubic-bezier(.4,0,.2,1)!important;white-space:nowrap!important}\ndiv[data-testid="stRadio"] label>span:first-child{display:none!important}\ndiv[data-testid="stRadio"] label:hover{background:var(--parchment-3)!important;border-color:var(--rule-strong)!important;color:var(--ink)!important}\ndiv[data-testid="stRadio"] label:has(input:checked){background:var(--ink)!important;border-color:var(--ink)!important;box-shadow:3px 3px 0 var(--accent)!important;transform:translate(-1px,-1px)!important}\ndiv[data-testid="stRadio"] label:has(input:checked) p,div[data-testid="stRadio"] label:has(input:checked) span{color:var(--parchment)!important}\ndiv[data-testid="stRadio"] label p{font-family:\'DM Sans\',sans-serif!important;font-size:.9rem!important;font-weight:600!important;margin:0!important;line-height:1!important}\n.conv-presets-sublabel{font-family:\'DM Sans\',sans-serif;font-size:.65rem;font-weight:700;text-transform:uppercase;letter-spacing:.14em;color:var(--ink-faint);margin-bottom:.65rem;margin-top:0}\n.conv-input-card{background:var(--card-bg);border:1px solid var(--card-border);border-radius:6px;padding:1.3rem 1.5rem 1.4rem;margin-bottom:.5rem;box-shadow:0 1px 3px rgba(26,22,18,.05),0 6px 20px rgba(26,22,18,.06),inset 0 1px 0 rgba(255,255,255,.7)}\n.conv-input-title{font-family:\'Crimson Pro\',Georgia,serif;font-size:1.3rem;font-weight:600;color:var(--ink);letter-spacing:-.02em;margin:0 0 .25rem 0;line-height:1.2}\n.conv-input-hint{font-family:\'Crimson Pro\',Georgia,serif;font-style:italic;font-size:.93rem;color:var(--ink-faint);margin:0 0 .8rem 0;line-height:1.4}\n.conv-result-card{background:rgba(46,107,122,.04);border:1px solid rgba(46,107,122,.18);border-left:3px solid var(--teal);border-radius:0 4px 4px 0;padding:.75rem 1.1rem;margin-top:.8rem}\n.conv-result-label{font-family:\'DM Sans\',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.14em;color:var(--teal);margin-bottom:.3rem}\n.conv-result-value{font-family:\'Crimson Pro\',Georgia,serif;font-size:1.05rem;font-weight:400;color:var(--ink);line-height:1.55;word-break:break-word}\n.conv-error-card{background:rgba(184,92,56,.05);border:1px solid rgba(184,92,56,.2);border-left:3px solid var(--accent);border-radius:0 4px 4px 0;padding:.75rem 1.1rem;margin-top:.8rem}\n.conv-error-text{font-family:\'Crimson Pro\',Georgia,serif;font-size:1rem;color:var(--accent);font-style:italic;margin:0}\n.conv-nav-footer{display:flex;gap:.75rem;padding:1.4rem 0 .5rem 0;border-top:1px solid var(--rule);margin-top:2.5rem;flex-wrap:wrap}\n.conv-nav-btn{font-family:\'DM Sans\',sans-serif;font-size:.78rem;font-weight:700;text-transform:uppercase;letter-spacing:.09em;color:var(--ink);background:var(--parchment-2);border:1.5px solid var(--rule-strong);border-radius:3px;padding:.55rem 1.1rem;text-decoration:none;display:inline-flex;align-items:center;gap:.4rem;white-space:nowrap;cursor:pointer;box-shadow:2px 2px 0 rgba(26,22,18,.08);transition:all .18s cubic-bezier(.4,0,.2,1)}\n.conv-nav-btn:hover{background:var(--ink);color:var(--parchment);border-color:var(--ink);box-shadow:3px 3px 0 var(--accent);transform:translate(-1px,-1px);text-decoration:none}\n.conv-nav-btn.active{background:var(--parchment-3);color:var(--ink-muted);cursor:default;box-shadow:none}\n.conv-nav-btn.active:hover{transform:none;background:var(--parchment-3);color:var(--ink-muted);border-color:var(--rule-strong);box-shadow:none}\n.conv-caption{font-family:\'DM Sans\',sans-serif;font-size:.75rem;color:var(--ink-faint);line-height:1.55;margin-top:1rem}\n.conv-caption a{color:var(--accent)!important;text-decoration:underline!important;text-decoration-color:rgba(184,92,56,.35)!important}\n.conv-caption a:hover{text-decoration-color:var(--accent)!important}\n</style>'
st.markdown(CONV_CSS, unsafe_allow_html=True)
st.markdown(CONV_CSS_ADDITIONS, unsafe_allow_html=True)
st.markdown("""<style>
.conv-result-row{display:grid;grid-template-columns:8.5rem 1fr;gap:.35rem .9rem;align-items:baseline;padding:.12rem 0}
.conv-result-sublabel{font-family:'DM Sans',sans-serif;font-size:.62rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--ink-faint)}
.conv-result-subvalue{font-family:'Crimson Pro',Georgia,serif;font-size:1.05rem;color:var(--ink);line-height:1.55;word-break:break-word}
</style>""", unsafe_allow_html=True)

st.markdown('''
<div class="conv-masthead">
    <div class="conv-masthead-eyebrow">Numeral Converter</div>
    <div class="conv-masthead-title">Yoruba Numerals</div>
    <div class="conv-masthead-desc">Convert Arabic numerals into Yoruba, which counts by twenties, adding to one round number or taking away from the next — for the numbers recorded with tone marks.</div>
</div>
''', unsafe_allow_html=True)

language_nav("Yoruba", "converter")

direction = 'Arabic → Yoruba'

# Initialize input vars before columns
arabic_input = ""

left_col, right_col = st.columns([1, 1], gap="large")

with left_col:
    st.markdown('<div class="conv-section-label">Preset Examples</div>', unsafe_allow_html=True)

    arabic_presets = [5, 11, 15, 16, 21, 25, 26, 50, 70, 100, 400, 2000]

    with st.container(border=False):
        st.markdown('<p class="conv-presets-sublabel">Click a value to load it</p>', unsafe_allow_html=True)
        cols = st.columns(4)
        for i, num in enumerate(arabic_presets):
            if cols[i % 4].button(str(num), key=f'p_a_{i}', use_container_width=True):
                st.session_state['arabic_input'] = str(num)

    st.markdown('<div class="conv-section-label">Convert</div>', unsafe_allow_html=True)

    st.markdown('''
<div class="conv-input-card">
    <div class="conv-input-title">Enter an Arabic numeral</div>
    <div class="conv-input-hint">1 to 30, a ten up to 100, or 200, 400, 1,000 or 2,000 — the numbers recorded with tone marks.</div>
</div>''', unsafe_allow_html=True)
    arabic_input = st.text_input('Enter an Arabic numeral', key='arabic_input', placeholder='e.g. 26', label_visibility="collapsed")

with right_col:
    if arabic_input:
        val = arabic_input.strip()
        if val.lstrip('-').isdigit():
            try:
                n = int(val)
                rows = [("Yoruba", number_to_yoruba(n))]
                if n == 40:
                    rows.append(("Note", "Spelling of Crowther (1852) and Bowen (1858), without tone "
                                         "marks; Kari's list misprints 40 as ọgbọ̀ji."))
                for form, why in ALTERNATIVES.get(n, []):
                    rows.append(("Also recorded", f"{form} <span style='font-family:DM Sans,sans-serif;"
                                                  f"font-size:.74rem;color:var(--ink-faint)'>· {why}</span>"))
                body = "".join(
                    f'<div class="conv-result-row"><span class="conv-result-sublabel">{k}</span>'
                    f'<span class="conv-result-subvalue">{v}</span></div>' for k, v in rows)
                st.markdown(f'''<div class="conv-result-card">
    <div class="conv-result-label">Yoruba numeral</div>
    {body}
</div>''', unsafe_allow_html=True)
            except Exception as e:
                st.markdown(f'<div class="conv-error-card"><p class="conv-error-text">{e}</p></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="conv-error-card"><p class="conv-error-text">Please enter a valid whole number.</p></div>', unsafe_allow_html=True)
    else:
        st.markdown("""
<div class="conv-empty-state">
    <p>Enter a value on the left to see the result.</p>
</div>
""", unsafe_allow_html=True)


    st.markdown('''
<div class="conv-caption">The forms Ethelbert Kari recorded for Chan's <em>Numeral Systems of the World's
Languages</em> (1998), from Robert G. Armstrong's <em>Yoruba Numerals</em> (1962), with 40 from Crowther
(1852) and Bowen (1858). Other numbers are not generated, because the open sources that describe them do
not mark tone. Algorithm by Yi Zou.</div>
''', unsafe_allow_html=True)

# ── NAVIGATION ──────────────────────────────────────────────
footer_nav("Yoruba", "converter")
