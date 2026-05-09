import streamlit as st
from ui import apply_global_styles, home_nav

# ============================================================
# ESPERANTO NUMERAL SYSTEM
# Bidirectional: Arabic ↔ Esperanto. Range: 0–999,999,999.
# Sources: PMEG (Wennergren), Fundamento de Esperanto (Zamenhof 1905)
# ============================================================

# ── Backend ──────────────────────────────────────────────────────────────────

_DIGITS = {0:"nul", 1:"unu", 2:"du", 3:"tri", 4:"kvar",
           5:"kvin", 6:"ses", 7:"sep", 8:"ok", 9:"naŭ"}
_DIGITS_REV = {v: k for k, v in _DIGITS.items()}

_TENS_WORDS = {10:"dek", 20:"dudek", 30:"tridek", 40:"kvardek",
               50:"kvindek", 60:"sesdek", 70:"sepdek",
               80:"okdek", 90:"naŭdek"}
_TENS_REV = {v: k for k, v in _TENS_WORDS.items()}

_HUNDREDS_WORDS = {100:"cent", 200:"ducent", 300:"tricent", 400:"kvarcent",
                   500:"kvincent", 600:"sescent", 700:"sepcent",
                   800:"okcent", 900:"naŭcent"}
_HUNDREDS_REV = {v: k for k, v in _HUNDREDS_WORDS.items()}


def _eo_sub_thousand(n):
    parts = []
    rem = n
    if rem >= 100:
        parts.append(_HUNDREDS_WORDS[(rem // 100) * 100]); rem %= 100
    if rem >= 10:
        parts.append(_TENS_WORDS[(rem // 10) * 10]); rem %= 10
    if rem > 0:
        parts.append(_DIGITS[rem])
    return " ".join(parts)


def number_to_esperanto(n):
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"Expected int, got {type(n).__name__}")
    if n < 0:
        raise ValueError("Negative numbers are not supported.")
    if n > 999_999_999:
        raise ValueError("Supported range is 0–999,999,999.")
    if n == 0:
        return "nul"
    parts = []
    rem = n
    if rem >= 1_000_000:
        m = rem // 1_000_000; rem %= 1_000_000
        parts.append("unu miliono" if m == 1 else f"{_eo_sub_thousand(m)} milionoj")
    if rem >= 1_000:
        t = rem // 1_000; rem %= 1_000
        parts.append("mil" if t == 1 else f"{_eo_sub_thousand(t)} mil")
    if rem > 0:
        parts.append(_eo_sub_thousand(rem))
    return " ".join(parts)


def _eo_parse_sub_thousand(tokens):
    if not tokens: return 0, tokens
    total = 0; consumed = False
    if tokens[0] in _HUNDREDS_REV:
        total += _HUNDREDS_REV[tokens[0]]; tokens = tokens[1:]; consumed = True
    if tokens and tokens[0] in _TENS_REV:
        total += _TENS_REV[tokens[0]]; tokens = tokens[1:]; consumed = True
    if tokens and tokens[0] in _DIGITS_REV and _DIGITS_REV[tokens[0]] > 0:
        total += _DIGITS_REV[tokens[0]]; tokens = tokens[1:]; consumed = True
    return (total if consumed else 0), tokens


def esperanto_to_number(text):
    text = text.strip().lower()
    if not text: raise ValueError("Empty input.")
    if text == "nul": return 0
    tokens = text.split()
    total = 0
    millions_idx = next((i for i, t in enumerate(tokens) if t in ("miliono","milionoj")), -1)
    if millions_idx >= 0:
        m_tok = tokens[:millions_idx]
        if not m_tok: raise ValueError("Expected multiplier before 'miliono(j)'.")
        if m_tok == ["unu"]: mult = 1
        else:
            mult, lo = _eo_parse_sub_thousand(m_tok)
            if lo or mult == 0: raise ValueError(f"Cannot parse millions multiplier: {m_tok}")
        total += mult * 1_000_000
        tokens = tokens[millions_idx + 1:]
    if "mil" in tokens:
        idx = tokens.index("mil")
        m_tok = tokens[:idx]
        if not m_tok: mult = 1
        else:
            mult, lo = _eo_parse_sub_thousand(m_tok)
            if lo or mult == 0: raise ValueError(f"Cannot parse thousands multiplier: {m_tok}")
        total += mult * 1_000
        tokens = tokens[idx + 1:]
    if tokens:
        sub, lo = _eo_parse_sub_thousand(tokens)
        if lo: raise ValueError(f"Unexpected tokens: {lo}")
        total += sub
    return total


# ============================================================
# PAGE
# ============================================================
st.set_page_config(page_title="Esperanto Numeral Converter", layout="centered")
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
.conv-nav-footer{display:flex;gap:.75rem;padding:1.4rem 0 .5rem 0;border-top:1px solid var(--rule);margin-top:2.5rem;flex-wrap:wrap}
.conv-nav-btn{font-family:'DM Sans',sans-serif;font-size:.78rem;font-weight:700;text-transform:uppercase;letter-spacing:.09em;color:var(--ink);background:var(--parchment-2);border:1.5px solid var(--rule-strong);border-radius:3px;padding:.55rem 1.1rem;text-decoration:none;display:inline-flex;align-items:center;gap:.4rem;white-space:nowrap;cursor:pointer;box-shadow:2px 2px 0 rgba(26,22,18,.08);transition:all .18s cubic-bezier(.4,0,.2,1)}
.conv-nav-btn:hover{background:var(--ink);color:var(--parchment);border-color:var(--ink);box-shadow:3px 3px 0 var(--accent);transform:translate(-1px,-1px);text-decoration:none}
.conv-nav-btn.active{background:var(--parchment-3);color:var(--ink-muted);cursor:default;box-shadow:none}
.conv-caption{font-family:'DM Sans',sans-serif;font-size:.75rem;color:var(--ink-faint);line-height:1.55;margin-top:1rem}
.conv-caption a{color:var(--accent)!important;text-decoration:underline!important}
</style>"""
st.markdown(CONV_CSS, unsafe_allow_html=True)

st.markdown("""
<div class="conv-masthead">
    <div class="conv-masthead-eyebrow">Numeral Converter</div>
    <div class="conv-masthead-title">Esperanto Numerals</div>
    <div class="conv-masthead-desc">
        Bidirectional conversion between Arabic numerals and Esperanto —
        a fully regular decimal system with no irregular forms.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="conv-section-label">Conversion Direction</div>', unsafe_allow_html=True)
direction = st.radio("Direction", ["Arabic → Esperanto", "Esperanto → Arabic"],
                     horizontal=True, label_visibility="collapsed", key="eo_dir")

st.markdown('<div class="conv-section-label">Preset Examples</div>', unsafe_allow_html=True)
arabic_presets = [0, 11, 21, 100, 234, 1000, 1234, 1000000]
eo_presets = ["nul", "dek unu", "dudek unu", "cent",
              "ducent tridek kvar", "mil",
              "mil ducent tridek kvar", "unu miliono"]

with st.container(border=True):
    st.markdown('<p class="conv-presets-sublabel">Click a value to load it</p>', unsafe_allow_html=True)
    cols = st.columns(4)
    if direction == "Arabic → Esperanto":
        for i, num in enumerate(arabic_presets):
            if cols[i % 4].button(str(num), key=f"p_a_{i}", use_container_width=True):
                st.session_state["arabic_input"] = str(num)
    else:
        for i, txt in enumerate(eo_presets):
            if cols[i % 4].button(txt, key=f"p_b_{i}", use_container_width=True):
                st.session_state["eo_input"] = txt

st.markdown('<div class="conv-section-label">Convert</div>', unsafe_allow_html=True)
if direction == "Arabic → Esperanto":
    st.markdown("""
    <div class="conv-input-card">
        <div class="conv-input-title">Enter an Arabic numeral</div>
        <div class="conv-input-hint">Whole number from 0 to 999,999,999.</div>
    </div>
    """, unsafe_allow_html=True)
    arabic_input = st.text_input("Arabic numeral", key="arabic_input",
                                 placeholder="e.g. 1234", label_visibility="collapsed")
    if arabic_input:
        if arabic_input.isdigit():
            try:
                result = number_to_esperanto(int(arabic_input))
                st.markdown(f'<div class="conv-result-card"><div class="conv-result-label">Esperanto numeral</div><div class="conv-result-value">{result}</div></div>',
                            unsafe_allow_html=True)
            except Exception as e:
                st.markdown(f'<div class="conv-error-card"><p class="conv-error-text">{e}</p></div>',
                            unsafe_allow_html=True)
        else:
            st.markdown('<div class="conv-error-card"><p class="conv-error-text">Please enter a valid whole number.</p></div>',
                        unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="conv-input-card">
        <div class="conv-input-title">Enter an Esperanto numeral</div>
        <div class="conv-input-hint">e.g. <em>ducent tridek kvar</em>.</div>
    </div>
    """, unsafe_allow_html=True)
    eo_input = st.text_input("Esperanto numeral", key="eo_input",
                             placeholder="e.g. ducent tridek kvar", label_visibility="collapsed")
    if eo_input:
        try:
            result = str(esperanto_to_number(eo_input))
            st.markdown(f'<div class="conv-result-card"><div class="conv-result-label">Arabic numeral</div><div class="conv-result-value">{result}</div></div>',
                        unsafe_allow_html=True)
        except Exception as e:
            st.markdown(f'<div class="conv-error-card"><p class="conv-error-text">{e}</p></div>',
                        unsafe_allow_html=True)

st.markdown("""
<div class="conv-caption">
    Esperanto, created by L. L. Zamenhof in 1887, is fully regular by design.
    Tens 20–90 are written as one word (dudek, tridek …); compound numbers
    use spaces. Sources: <em>Plena Manlibro de Esperanta Gramatiko</em> (Wennergren),
    <em>Fundamento de Esperanto</em> (Zamenhof 1905). Algorithm by Yi Zou.
</div>
""", unsafe_allow_html=True)

# ── NAVIGATION ──────────────────────────────────────────────
st.markdown('<div class="nav-row">', unsafe_allow_html=True)
st.page_link("pages/Esperanto_Linguistics.py", label="← Esperanto Linguistics")
st.page_link("Home.py", label="← Home")
st.markdown('</div>', unsafe_allow_html=True)
