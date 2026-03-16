import streamlit as st
from ui import apply_global_styles

# ============================================================
# BENGALI NUMERAL SYSTEM
# Bidirectional: Arabic ↔ Bengali (Digits, Words, Romanized)
# Based on: https://en.wikipedia.org/wiki/Bengali_numerals
# ============================================================

# ------------------------------------------------------------
# 1. ATOMIC NUMERALS (0–99)
# ------------------------------------------------------------
BENGALI_ATOMS = {
    0:"শূন্য",1:"এক",2:"দুই",3:"তিন",4:"চার",5:"পাঁচ",6:"ছয়",7:"সাত",8:"আট",9:"নয়",
    10:"দশ",11:"এগারো",12:"বারো",13:"তেরো",14:"চৌদ্দ",15:"পনেরো",16:"ষোলো",
    17:"সতেরো",18:"আঠারো",19:"ঊনিশ",20:"বিশ",21:"একুশ",30:"ত্রিশ",
    40:"চল্লিশ",50:"পঞ্চাশ",60:"ষাট",70:"সত্তর",80:"আশি",90:"নব্বই",
}

ROMANIZED_ATOMS = {
    0:"shunnô",1:"æk",2:"dui",3:"tin",4:"char",5:"pãch",6:"chhôy",7:"shat",
    8:"aṭ",9:"nôy",10:"dôsh",11:"ægaro",12:"baro",13:"tero",14:"choddô",
    15:"pônero",16:"sholo",17:"shôtero",18:"aṭharo",19:"unish",20:"bish",
    21:"ekush",30:"trish",40:"chôllish",50:"pônchash",60:"shaṭ",
    70:"shôttôr",80:"ashi",90:"nôbbôi",
}

BENGALI_VALUES  = {v: k for k, v in BENGALI_ATOMS.items()}
ROMANIZED_VALUES = {v: k for k, v in ROMANIZED_ATOMS.items()}

# ------------------------------------------------------------
# 2. BASE UNITS (Indian numbering system)
# ------------------------------------------------------------
BASE_UNITS = [
    ("কোটি", "koṭi",   10_000_000),
    ("লাখ",  "lakh",   100_000),
    ("হাজার","hajar",  1_000),
    ("শত",   "shôtô",  100),
]

BENGALI_BASE_VALUES   = {beng: value for beng, roman, value in BASE_UNITS}
ROMANIZED_BASE_VALUES = {roman: value for _, roman, value in BASE_UNITS}
BENGALI_BASE_VALUES["একশ"]   = 100
ROMANIZED_BASE_VALUES["ækshô"] = 100

# ------------------------------------------------------------
# 3. ARABIC → BENGALI
# ------------------------------------------------------------
def number_to_bengali_digits(n: int) -> str:
    return str(n).translate(str.maketrans("0123456789", "০১২৩৪৫৬৭৮৯"))

def number_to_bengali_words(n: int, romanized: bool = False) -> str:
    if n < 0:
        raise ValueError("Negative numbers are not supported")
    if n == 0:
        return ROMANIZED_ATOMS[0] if romanized else BENGALI_ATOMS[0]
    atom_map = ROMANIZED_ATOMS if romanized else BENGALI_ATOMS
    if n <= 99 and n in atom_map:
        return atom_map[n]
    if 100 <= n < 200:
        if n == 100:
            return "ækshô" if romanized else "একশ"
        one     = "æk"   if romanized else "এক"
        hundred = "ækshô" if romanized else "একশ"
        rem = number_to_bengali_words(n - 100, romanized)
        return f"{one} {hundred} {rem}" if rem else f"{one} {hundred}"
    for beng, roman, value in BASE_UNITS:
        if n >= value:
            q, r = n // value, n % value
            unit = roman if romanized else beng
            if q == 1 and value >= 1000:
                prefix = ("æk" if romanized else "এক") + " " + unit
            else:
                prefix = number_to_bengali_words(q, romanized) + " " + unit
            return prefix if r == 0 else prefix + " " + number_to_bengali_words(r, romanized)
    return ""

# ------------------------------------------------------------
# 4. BENGALI → ARABIC
# ------------------------------------------------------------
def bengali_digits_to_number(text: str) -> int:
    cleaned = text.strip().replace(" ", "")
    arabic_str = cleaned.translate(str.maketrans("০১২৩৪৫৬৭৮৯", "0123456789"))
    try:
        return int(arabic_str)
    except ValueError:
        raise ValueError("Invalid Bengali digit sequence")

def _parse_words(tokens, value_map, base_map):
    if not tokens:
        return None
    full = " ".join(tokens)
    if full in value_map:
        return value_map[full]
    for base_word, base_value in sorted(base_map.items(), key=lambda x: -x[1]):
        if base_word in tokens:
            idx = tokens.index(base_word)
            left_tokens, right_tokens = tokens[:idx], tokens[idx + 1:]
            multiplier = 1
            if left_tokens:
                left_val = _parse_words(left_tokens, value_map, base_map)
                if left_val is None:
                    return None
                multiplier = left_val
            remainder = 0
            if right_tokens:
                rem_val = _parse_words(right_tokens, value_map, base_map)
                if rem_val is None:
                    return None
                remainder = rem_val
            return multiplier * base_value + remainder
    return None

def bengali_words_to_number(text: str) -> int:
    tokens = text.strip().split()
    result = _parse_words(tokens, BENGALI_VALUES, BENGALI_BASE_VALUES)
    if result is None:
        raise ValueError("Invalid Bengali numeral")
    return result

def romanized_words_to_number(text: str) -> int:
    tokens = text.strip().split()
    result = _parse_words(tokens, ROMANIZED_VALUES, ROMANIZED_BASE_VALUES)
    if result is None:
        raise ValueError("Invalid romanized Bengali numeral")
    return result

def bengali_to_number(text: str) -> int:
    text = text.strip()
    if not text:
        raise ValueError("Empty input")
    if all(ch in "০১২৩৪৫৬৭৮৯" or ch.isspace() for ch in text):
        return bengali_digits_to_number(text)
    if any('\u0980' <= ch <= '\u09FF' for ch in text):
        return bengali_words_to_number(text)
    return romanized_words_to_number(text)


# ============================================================
# PAGE CONFIG & STYLES
# ============================================================
st.set_page_config(page_title="Bengali Numeral Converter", layout="centered")
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
    <div class="conv-masthead-title">Bengali Numerals</div>
    <div class="conv-masthead-desc">
        Bidirectional conversion between Arabic numerals and Bengali —
        Bengali script digits, Bengali words, and romanized forms.
    </div>
</div>
""", unsafe_allow_html=True)

# ── DIRECTION SELECTOR ──────────────────────────────────────────────────────
st.markdown('<div class="conv-section-label">Conversion Direction</div>', unsafe_allow_html=True)

direction = st.radio(
    "Conversion direction",
    ["Arabic → Bengali", "Bengali → Arabic"],
    horizontal=True,
    label_visibility="collapsed",
    key="bengali_direction",
)

# ── PRESET EXAMPLES ─────────────────────────────────────────────────────────
st.markdown('<div class="conv-section-label">Preset Examples</div>', unsafe_allow_html=True)

arabic_presets  = [0, 5, 12, 21, 100, 325, 12345, 10000000]
bengali_presets = [
    "শূন্য", "পাঁচ", "বারো", "একুশ",
    "একশ", "তিন শত পঁচিশ", "বারো হাজার তিন শত পঁয়তাল্লিশ", "এক কোটি",
]

with st.container(border=True):
    st.markdown('<p class="conv-presets-sublabel">Click a value to load it</p>', unsafe_allow_html=True)
    cols = st.columns(4)
    if direction == "Arabic → Bengali":
        for i, num in enumerate(arabic_presets):
            if cols[i % 4].button(str(num), key=f"p_a_{i}", use_container_width=True):
                st.session_state["arabic_input"] = str(num)
    else:
        for i, txt in enumerate(bengali_presets):
            if cols[i % 4].button(txt, key=f"p_b_{i}", use_container_width=True):
                st.session_state["bengali_input"] = txt

# ── INPUT & CONVERSION ──────────────────────────────────────────────────────
st.markdown('<div class="conv-section-label">Convert</div>', unsafe_allow_html=True)

if direction == "Arabic → Bengali":
    st.markdown("""
    <div class="conv-input-card">
        <div class="conv-input-title">Enter an Arabic numeral</div>
        <div class="conv-input-hint">Type a whole number, or click a preset above.</div>
    </div>
    """, unsafe_allow_html=True)
    arabic_input = st.text_input(
        "Arabic numeral", key="arabic_input",
        placeholder="e.g. 325", label_visibility="collapsed",
    )
    if arabic_input:
        if arabic_input.lstrip("-").isdigit():
            try:
                n      = int(arabic_input)
                digits = number_to_bengali_digits(n)
                beng   = number_to_bengali_words(n, romanized=False)
                rom    = number_to_bengali_words(n, romanized=True)
                result = f"{digits}\n{beng}\n{rom}"
                st.markdown(f"""
                <div class="conv-result-card">
                    <div class="conv-result-label">Bengali digits · words · romanized</div>
                    <div class="conv-result-value">{result}</div>
                </div>
                """, unsafe_allow_html=True)
            except Exception as e:
                st.markdown(f'<div class="conv-error-card"><p class="conv-error-text">{e}</p></div>',
                            unsafe_allow_html=True)
        else:
            st.markdown('<div class="conv-error-card"><p class="conv-error-text">Please enter a valid whole number.</p></div>',
                        unsafe_allow_html=True)

else:
    st.markdown("""
    <div class="conv-input-card">
        <div class="conv-input-title">Enter a Bengali numeral</div>
        <div class="conv-input-hint">Bengali digits (০-৯), Bengali words, or romanized words.</div>
    </div>
    """, unsafe_allow_html=True)
    bengali_input = st.text_input(
        "Bengali numeral", key="bengali_input",
        placeholder="e.g. তিন শত পঁচিশ", label_visibility="collapsed",
    )
    if bengali_input:
        try:
            result = str(bengali_to_number(bengali_input))
            st.markdown(f"""
            <div class="conv-result-card">
                <div class="conv-result-label">Arabic numeral</div>
                <div class="conv-result-value">{result}</div>
            </div>
            """, unsafe_allow_html=True)
        except Exception as e:
            st.markdown(f'<div class="conv-error-card"><p class="conv-error-text">{e}</p></div>',
                        unsafe_allow_html=True)

# ── CAPTION & NAVIGATION ────────────────────────────────────────────────────
st.markdown("""
<div class="conv-caption">
    Implements the Indian numbering system (lakhs, crores) with standard Bengali number names.
    Data from <a href="https://en.wikipedia.org/wiki/Bengali_numerals" target="_blank">Wikipedia</a>.
    Converter algorithm by Yi Zou. Grammar detail in the Linguistics section.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="conv-nav-footer">
    <a class="conv-nav-btn active" href="/Bengali_Converter">Bengali Converter</a>
    <a class="conv-nav-btn" href="/Bengali_Linguistics">Bengali Linguistics →</a>
</div>
""", unsafe_allow_html=True)