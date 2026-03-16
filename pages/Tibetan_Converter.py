import streamlit as st
from ui import apply_global_styles

# ============================================================
# TIBETAN NUMERAL SYSTEM
# Arabic → Tibetan (script + romanisation)
# ============================================================

ATOMS = {
    0: ("ཀླད་ཀོར་", "laykor"),
    1: ("གཅིག་",    "chig"),
    2: ("གཉིས་",   "nyi"),
    3: ("གསུམ་",   "sum"),
    4: ("བཞི་",    "shi"),
    5: ("ལྔ་",     "nga"),
    6: ("དྲུག་",   "trug"),
    7: ("བདུན་",   "dün"),
    8: ("བརྒྱད་",  "gyay"),
    9: ("དགུ་",    "gu"),
}

TEENS = {
    10: ("བཅུ་",       "chu"),
    11: ("བཅུ་གཅིག་",  "chu chig"),
    12: ("བཅུ་གཉིས་",  "chu nyi"),
    13: ("བཅུ་གསུམ་",  "chu sum"),
    14: ("བཅུ་བཞི་",   "chu shi"),
    15: ("བཅོ་ལྔ་",    "cho nga"),
    16: ("བཅུ་དྲུག་",  "chu trug"),
    17: ("བཅུ་བདུན་",  "chu dün"),
    18: ("བཅོ་བརྒྱད་", "cho gyay"),
    19: ("བཅུ་དགུ་",   "chu gu"),
}

DECADES = {
    20: ("ཉི་ཤུ་",   "nyi shu"),
    30: ("སུམ་ཅུ",   "sum ju"),
    40: ("བཞི་བཅུ",  "shi ju"),
    50: ("ལྔ་བཅུ",   "nga ju"),
    60: ("དྲུག་ཅུ",  "trug chu"),
    70: ("བདུན་ཅུ",  "dün ju"),
    80: ("བརྒྱད་ཅུ", "gyay ju"),
    90: ("དགུ་བཅུ",  "gu ju"),
}

DECADE_LINKERS = {
    20: ("རྩ་", "tsa"),
    30: ("སོ་", "so"),
    40: ("ཞེ་", "shey"),
    50: ("ང་",  "nga"),
    60: ("རེ་", "rey"),
    70: ("དོན་","dön"),
    80: ("གྱ་", "gya"),
    90: ("གོ་", "go"),
}

MAGNITUDES = [
    (10**12, ("ཁྲག་ཁྲིག་ཆེན་པོ་", "thrag trig chen po")),
    (10**11, ("ཁྲག་ཁྲིག་",        "thrag trig")),
    (10**10, ("ཐེར་འབུམ་ཆེན་པོ་", "ther pum chen po")),
    (10**9,  ("ཐེར་འབུམ་",        "ther pum")),
    (10**8,  ("དུང་ཕྱུར་",        "dung chur")),
    (10**7,  ("བྱེ་བ་",           "che wa")),
    (10**6,  ("ས་ཡ་",             "sa ya")),
    (10**4,  ("ཁྲི་",             "thri")),
    (10**3,  ("སྟོང་",            "tong")),
    (100,    ("བརྒྱ་",            "gya")),
]

def number_to_tibetan(n):
    if n < 0:
        raise ValueError("Negative numbers not supported")
    if n in ATOMS:
        return ATOMS[n]
    if n in TEENS:
        return TEENS[n]
    if n in DECADES:
        return DECADES[n]
    if n < 100:
        decade = (n // 10) * 10
        unit   = n % 10
        d_word, d_rom = DECADES[decade]
        l_word, l_rom = DECADE_LINKERS[decade]
        u_word, u_rom = ATOMS[unit]
        return (f"{d_word}{l_word}{u_word}", f"{d_rom} {l_rom} {u_rom}")
    for value, (mag_word, mag_rom) in MAGNITUDES:
        if n >= value:
            multiplier = n // value
            remainder  = n % value
            if multiplier == 1:
                head_word, head_rom = mag_word, mag_rom
            else:
                m_word, m_rom = number_to_tibetan(multiplier)
                head_word = f"{m_word}{mag_word}"
                head_rom  = f"{m_rom} {mag_rom}"
            if remainder == 0:
                return head_word, head_rom
            r_word, r_rom = number_to_tibetan(remainder)
            return (f"{head_word}དང་{r_word}", f"{head_rom} dang {r_rom}")


# ============================================================
# PAGE CONFIG & STYLES
# ============================================================
st.set_page_config(page_title="Tibetan Numeral Converter", layout="centered")
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
.conv-nav-btn.active:hover{transform:none;background:var(--parchment-3);color:var(--ink-muted);border-color:var(--rule-strong);box-shadow:none}
.conv-caption{font-family:'DM Sans',sans-serif;font-size:.75rem;color:var(--ink-faint);line-height:1.55;margin-top:1rem}
.conv-caption a{color:var(--accent)!important;text-decoration:underline!important;text-decoration-color:rgba(184,92,56,.35)!important}
.conv-caption a:hover{text-decoration-color:var(--accent)!important}
</style>"""
st.markdown(CONV_CSS, unsafe_allow_html=True)

# ── MASTHEAD ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="conv-masthead">
    <div class="conv-masthead-eyebrow">Numeral Converter</div>
    <div class="conv-masthead-title">Tibetan Numerals</div>
    <div class="conv-masthead-desc">
        Convert Arabic numerals into Tibetan script and standard romanization.
    </div>
</div>
""", unsafe_allow_html=True)

# ── PRESET EXAMPLES ─────────────────────────────────────────────────────────
st.markdown('<div class="conv-section-label">Preset Examples</div>', unsafe_allow_html=True)

arabic_presets = [3, 10, 21, 45, 108, 256, 1000, 4032]

with st.container(border=True):
    st.markdown('<p class="conv-presets-sublabel">Click a value to load it</p>', unsafe_allow_html=True)
    cols = st.columns(4)
    for i, num in enumerate(arabic_presets):
        if cols[i % 4].button(str(num), key=f"p_a_{i}", use_container_width=True):
            st.session_state["arabic_input"] = str(num)

# ── INPUT & CONVERSION ──────────────────────────────────────────────────────
st.markdown('<div class="conv-section-label">Convert</div>', unsafe_allow_html=True)

st.markdown("""
<div class="conv-input-card">
    <div class="conv-input-title">Enter an Arabic numeral</div>
    <div class="conv-input-hint">Type a whole number, or click a preset above.</div>
</div>
""", unsafe_allow_html=True)

arabic_input = st.text_input(
    "Arabic numeral", key="arabic_input",
    placeholder="e.g. 256", label_visibility="collapsed",
)

if arabic_input:
    if arabic_input.isdigit():
        try:
            tib, rom = number_to_tibetan(int(arabic_input))
            result = f"{tib}  ({rom})"
            st.markdown(f"""
            <div class="conv-result-card">
                <div class="conv-result-label">Tibetan (script · romanized)</div>
                <div class="conv-result-value">{result}</div>
            </div>
            """, unsafe_allow_html=True)
        except Exception as e:
            st.markdown(f'<div class="conv-error-card"><p class="conv-error-text">{e}</p></div>',
                        unsafe_allow_html=True)
    else:
        st.markdown('<div class="conv-error-card"><p class="conv-error-text">Please enter a valid non-negative integer.</p></div>',
                    unsafe_allow_html=True)

# ── CAPTION & NAVIGATION ────────────────────────────────────────────────────
st.markdown("""
<div class="conv-caption">
    Implements the Tibetan numeral system with script and romanization.
    Data from <a href="https://www.omniglot.com/language/numbers/tibetan.htm" target="_blank">Omniglot</a>.
    Converter algorithm by Yi Zou. Grammar detail in the Linguistics section.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="conv-nav-footer">
    <a class="conv-nav-btn active" href="/Tibetan_Converter">Tibetan Converter</a>
    <a class="conv-nav-btn" href="/Tibetan_Linguistics">Tibetan Linguistics →</a>
</div>
""", unsafe_allow_html=True)