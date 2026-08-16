import streamlit as st
from ui import apply_global_styles, language_nav, CONV_CSS_ADDITIONS, footer_nav

# ============================================================
# HIGH VALYRIAN (Valyrio) NUMERAL SYSTEM
# Bidirectional: Arabic ↔ High Valyrian. Range: 1–10 only.
# Sources: D. J. Peterson canon, Duolingo HV course, Wiki of Ice and Fire
# Numbers above 10 lack published canonical forms.
# ============================================================

# ── Backend ──────────────────────────────────────────────────────────────────

_NUMERALS = {1:"mēre", 2:"tymptir", 3:"hāre", 4:"rytsas", 5:"tōme",
             6:"byssa", 7:"jēdar", 8:"ōñoso", 9:"glaeson", 10:"vōre"}
_NUMERALS_REV = {v.lower(): k for k, v in _NUMERALS.items()}

CONFIDENCE = {1:"HIGH", 2:"HIGH", 3:"HIGH",
              4:"MEDIUM", 5:"MEDIUM", 6:"MEDIUM",
              7:"MEDIUM", 8:"MEDIUM", 9:"MEDIUM", 10:"MEDIUM"}


def number_to_high_valyrian(n):
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"Expected int, got {type(n).__name__}")
    if n < 1 or n > 10:
        raise ValueError(
            "High Valyrian conversion is limited to 1–10. "
            "No published canonical compositional system exists for numbers above 10."
        )
    return _NUMERALS[n]


def high_valyrian_to_number(text):
    text = text.strip().lower()
    if not text:
        raise ValueError("Empty input.")
    if text in _NUMERALS_REV:
        return _NUMERALS_REV[text]
    raise ValueError(
        f"Unrecognised High Valyrian numeral: '{text}'. "
        f"Supported forms (1–10): {', '.join(_NUMERALS.values())}."
    )


# ============================================================
# PAGE
# ============================================================
st.set_page_config(page_title="High Valyrian Numeral Converter", layout="wide")
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
div[data-testid="stRadio"]>div{display:flex;gap:0;background:var(--card-bg);border:1px solid var(--card-border);border-radius:6px;padding:.35rem;box-shadow:0 1px 3px rgba(26,22,18,.05),0 4px 14px rgba(26,22,18,.04),inset 0 1px 0 rgba(255,255,255,.65);width:fit-content}
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
.conv-result-card{background:rgba(46,107,122,.04);border:1px solid rgba(46,107,122,.18);border-left:3px solid var(--teal);border-radius:0 4px 4px 0;padding:.75rem 1.1rem;margin-top:.8rem}
.conv-result-label{font-family:'DM Sans',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.14em;color:var(--teal);margin-bottom:.3rem}
.conv-result-value{font-family:'Crimson Pro',Georgia,serif;font-size:1.05rem;font-weight:400;color:var(--ink);line-height:1.55;word-break:break-word}
.conv-error-card{background:rgba(184,92,56,.05);border:1px solid rgba(184,92,56,.2);border-left:3px solid var(--accent);border-radius:0 4px 4px 0;padding:.75rem 1.1rem;margin-top:.8rem}
.conv-error-text{font-family:'Crimson Pro',Georgia,serif;font-size:1rem;color:var(--accent);font-style:italic;margin:0}
.conv-note-card{background:rgba(184,92,56,.04);border:1px solid rgba(184,92,56,.18);border-left:3px solid var(--accent);border-radius:0 4px 4px 0;padding:.85rem 1.2rem;margin:.5rem 0 1.5rem 0}
.conv-note-card p{font-family:'Crimson Pro',Georgia,serif;font-size:.98rem;font-style:italic;color:var(--ink-soft);margin:0;line-height:1.55}
.conv-note-card strong{font-style:normal;font-weight:600;color:var(--ink)}
.conv-nav-footer{display:flex;gap:.75rem;padding:1.4rem 0 .5rem 0;border-top:1px solid var(--rule);margin-top:2.5rem;flex-wrap:wrap}
.conv-nav-btn{font-family:'DM Sans',sans-serif;font-size:.78rem;font-weight:700;text-transform:uppercase;letter-spacing:.09em;color:var(--ink);background:var(--parchment-2);border:1.5px solid var(--rule-strong);border-radius:3px;padding:.55rem 1.1rem;text-decoration:none;display:inline-flex;align-items:center;gap:.4rem;white-space:nowrap;cursor:pointer;box-shadow:2px 2px 0 rgba(26,22,18,.08);transition:all .18s cubic-bezier(.4,0,.2,1)}
.conv-nav-btn:hover{background:var(--ink);color:var(--parchment);border-color:var(--ink);box-shadow:3px 3px 0 var(--accent);transform:translate(-1px,-1px);text-decoration:none}
.conv-nav-btn.active{background:var(--parchment-3);color:var(--ink-muted);cursor:default;box-shadow:none}
.conv-caption{font-family:'DM Sans',sans-serif;font-size:.75rem;color:var(--ink-faint);line-height:1.55;margin-top:1rem}
.conv-caption a{color:var(--accent)!important;text-decoration:underline!important}
</style>"""
st.markdown(CONV_CSS, unsafe_allow_html=True)
st.markdown(CONV_CSS_ADDITIONS, unsafe_allow_html=True)

st.markdown("""
<div class="conv-masthead">
    <div class="conv-masthead-eyebrow">Numeral Converter</div>
    <div class="conv-masthead-title">High Valyrian Numerals</div>
    <div class="conv-masthead-desc">
        Bidirectional conversion between Arabic numerals and High Valyrian (Valyrio).
        Range limited to 1–10 — see canon caveat below.
    </div>
</div>
""", unsafe_allow_html=True)

language_nav("High Valyrian", "converter")

# Canon caveat — prominent
st.markdown("""
<div class="conv-note-card">
    <p><strong>Canon limitation:</strong> High Valyrian was created by linguist
    David J. Peterson for HBO's <em>Game of Thrones</em>. Numerals 1–3 are
    high-confidence published forms; 4–10 are community-verified but with less
    direct attestation. <strong>No canonical compositional system exists for
    numbers above 10</strong>, so this converter does not fabricate forms beyond
    that range.</p>
</div>
""", unsafe_allow_html=True)

# ── INITIALIZE INPUT VARS ─────────────────────────────────────────────────────
arabic_input = ""
hv_input = ""

# ── TWO COLUMN LAYOUT ─────────────────────────────────────────────────────────
left_col, right_col = st.columns([1, 1], gap="large")

with right_col:
    # ── DIRECTION SELECTOR ──────────────────────────────────────────────────
    st.markdown('<div class="conv-section-label conv-direction-label">Conversion Direction</div>', unsafe_allow_html=True)
    direction = st.radio("Direction", ["Arabic → Valyrian", "Valyrian → Arabic"],
                         horizontal=True, label_visibility="collapsed", key="hv_dir")

with left_col:
    st.markdown('<div class="conv-section-label">Preset Examples</div>', unsafe_allow_html=True)
    arabic_presets = [1, 2, 3, 4, 5, 7, 8, 10]
    hv_presets = ["mēre", "tymptir", "hāre", "rytsas",
                  "tōme", "jēdar", "ōñoso", "vōre"]

    with st.container(border=False):
        st.markdown('<p class="conv-presets-sublabel">Click a value to load it</p>', unsafe_allow_html=True)
        cols = st.columns(4)
        if direction == "Arabic → Valyrian":
            for i, num in enumerate(arabic_presets):
                if cols[i % 4].button(str(num), key=f"p_a_{i}", use_container_width=True):
                    st.session_state["arabic_input"] = str(num)
        else:
            for i, txt in enumerate(hv_presets):
                if cols[i % 4].button(txt, key=f"p_b_{i}", use_container_width=True):
                    st.session_state["hv_input"] = txt

    st.markdown('<div class="conv-section-label">Convert</div>', unsafe_allow_html=True)
    if direction == "Arabic → Valyrian":
        st.markdown("""
        <div class="conv-input-card">
            <div class="conv-input-title">Enter an Arabic numeral</div>
            <div class="conv-input-hint">Whole number from 1 to 10.</div>
        </div>
        """, unsafe_allow_html=True)
        arabic_input = st.text_input("Arabic numeral", key="arabic_input",
                                     placeholder="e.g. 5", label_visibility="collapsed")
    else:
        st.markdown("""
        <div class="conv-input-card">
            <div class="conv-input-title">Enter a High Valyrian numeral</div>
            <div class="conv-input-hint">Macrons preserved (e.g. <em>mēre</em>, <em>tōme</em>).</div>
        </div>
        """, unsafe_allow_html=True)
        hv_input = st.text_input("Valyrian numeral", key="hv_input",
                                 placeholder="e.g. mēre", label_visibility="collapsed")

with right_col:
    if direction == "Arabic → Valyrian":
        if arabic_input:
            if arabic_input.isdigit():
                try:
                    n = int(arabic_input)
                    result = number_to_high_valyrian(n)
                    conf = CONFIDENCE.get(n, "?")
                    st.markdown(f'<div class="conv-result-card"><div class="conv-result-label">High Valyrian numeral · {conf} confidence</div><div class="conv-result-value">{result}</div></div>',
                                unsafe_allow_html=True)
                except Exception as e:
                    st.markdown(f'<div class="conv-error-card"><p class="conv-error-text">{e}</p></div>',
                                unsafe_allow_html=True)
            else:
                st.markdown('<div class="conv-error-card"><p class="conv-error-text">Please enter a valid whole number.</p></div>',
                            unsafe_allow_html=True)
        else:
            st.markdown("""
<div class="conv-empty-state">
    <p>Enter a value on the left to see the result.</p>
</div>
""", unsafe_allow_html=True)
    else:
        if hv_input:
            try:
                result = str(high_valyrian_to_number(hv_input))
                st.markdown(f'<div class="conv-result-card"><div class="conv-result-label">Arabic numeral</div><div class="conv-result-value">{result}</div></div>',
                            unsafe_allow_html=True)
            except Exception as e:
                st.markdown(f'<div class="conv-error-card"><p class="conv-error-text">{e}</p></div>',
                            unsafe_allow_html=True)
        else:
            st.markdown("""
<div class="conv-empty-state">
    <p>Enter a value on the left to see the result.</p>
</div>
""", unsafe_allow_html=True)


    st.markdown("""
<div class="conv-caption">
    High Valyrian (Valyrio) is the constructed liturgical and historical
    language of the Targaryen dynasty in <em>A Song of Ice and Fire</em> and
    <em>Game of Thrones</em>, developed by linguist David J. Peterson from
    glimpses in George R. R. Martin's text. Sources: Peterson public posts,
    Duolingo HV course, Wiki of Ice and Fire. Limited canon respected — no
    compound forms invented.
</div>
""", unsafe_allow_html=True)

# ── NAVIGATION ──────────────────────────────────────────────
footer_nav("High Valyrian", "converter")
