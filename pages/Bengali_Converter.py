import streamlit as st
from ui import apply_global_styles, language_nav, CONV_CSS_ADDITIONS, footer_nav

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
    17:"সতেরো",18:"আঠারো",19:"ঊনিশ",20:"বিশ",21:"একুশ",
    22:"বাইশ",23:"তেইশ",24:"চব্বিশ",25:"পঁচিশ",26:"ছাব্বিশ",27:"সাতাশ",
    28:"আঠাশ",29:"উনত্রিশ",
    30:"ত্রিশ",31:"একত্রিশ",32:"বত্রিশ",33:"তেত্রিশ",34:"চৌত্রিশ",35:"পঁয়ত্রিশ",
    36:"ছত্রিশ",37:"সাঁইত্রিশ",38:"আটত্রিশ",39:"উনচল্লিশ",
    40:"চল্লিশ",41:"একচল্লিশ",42:"বিয়াল্লিশ",43:"তেতাল্লিশ",44:"চুয়াল্লিশ",
    45:"পঁয়তাল্লিশ",46:"ছেচল্লিশ",47:"সাতচল্লিশ",48:"আটচল্লিশ",49:"উনপঞ্চাশ",
    50:"পঞ্চাশ",51:"একান্ন",52:"বায়ান্ন",53:"তিপান্ন",54:"চুয়ান্ন",
    55:"পঞ্চান্ন",56:"ছাপান্ন",57:"সাতান্ন",58:"আটান্ন",59:"উনষাট",
    60:"ষাট",61:"একষট্টি",62:"বাষট্টি",63:"তেষট্টি",64:"চৌষট্টি",
    65:"পঁয়ষট্টি",66:"ছেষট্টি",67:"সাতষট্টি",68:"আটষট্টি",69:"উনসত্তর",
    70:"সত্তর",71:"একাত্তর",72:"বাহাত্তর",73:"তিয়াত্তর",74:"চুয়াত্তর",
    75:"পঁচাত্তর",76:"ছিয়াত্তর",77:"সাতাত্তর",78:"আটাত্তর",79:"উনআশি",
    80:"আশি",81:"একাশি",82:"বিরাশি",83:"তিরাশি",84:"চুরাশি",
    85:"পঁচাশি",86:"ছিয়াশি",87:"সাতাশি",88:"আটাশি",89:"উননব্বই",
    90:"নব্বই",91:"একানব্বই",92:"বিরানব্বই",93:"তিরানব্বই",94:"চুরানব্বই",
    95:"পঁচানব্বই",96:"ছিয়ানব্বই",97:"সাতানব্বই",98:"আটানব্বই",99:"নিরানব্বই",
}

ROMANIZED_ATOMS = {
    0:"shunnô",1:"æk",2:"dui",3:"tin",4:"char",5:"pãch",6:"chhôy",7:"shat",
    8:"aṭ",9:"nôy",10:"dôsh",11:"ægaro",12:"baro",13:"tero",14:"choddô",
    15:"pônero",16:"sholo",17:"shôtero",18:"aṭharo",19:"unish",20:"bish",
    21:"ekush",
    22:"baish",23:"teish",24:"chôbbish",25:"pãchish",26:"chhabbish",27:"sataash",
    28:"aṭhash",29:"unatrish",
    30:"trish",31:"ækotrish",32:"bôtrish",33:"tetrish",34:"chôutrish",35:"pãyôtrish",
    36:"chhôtrish",37:"shãitrish",38:"aṭôtrish",39:"unôchôllish",
    40:"chôllish",41:"ækoechôllish",42:"biyallish",43:"tetallish",44:"chuallish",
    45:"pãytallish",46:"chhechôllish",47:"shaatchôllish",48:"aṭchôllish",49:"unôpôñchash",
    50:"pônchash",51:"ækañnô",52:"bayañnô",53:"tipañnô",54:"chuañnô",
    55:"pôñchañnô",56:"chhapañnô",57:"shatañnô",58:"aṭañnô",59:"unôshaṭ",
    60:"shaṭ",61:"ækoeshôṭṭi",62:"bashôṭṭi",63:"teshôṭṭi",64:"chôushôṭṭi",
    65:"pãyshôṭṭi",66:"chheshôṭṭi",67:"shaatshaṭṭi",68:"aṭshôṭṭi",69:"unôshôttôr",
    70:"shôttôr",71:"ækattor",72:"bahattor",73:"tiyattor",74:"chuattor",
    75:"pãchattor",76:"chhiyattor",77:"shatattor",78:"aṭattor",79:"unôashi",
    80:"ashi",81:"ækashi",82:"birashi",83:"tirashi",84:"churashi",
    85:"pãchashi",86:"chhiyashi",87:"shatashi",88:"aṭashi",89:"unônôbbôi",
    90:"nôbbôi",91:"ækanôbbôi",92:"biranôbbôi",93:"tiranôbbôi",94:"churanôbbôi",
    95:"pãchanôbbôi",96:"chhiyanôbbôi",97:"shatanôbbôi",98:"aṭanôbbôi",99:"niranôbbôi",
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
        hundred = "ækshô" if romanized else "একশ"
        if n == 100:
            return hundred
        rem = number_to_bengali_words(n - 100, romanized)
        return f"{hundred} {rem}"
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
    if any('ঀ' <= ch <= '৿' for ch in text):
        return bengali_words_to_number(text)
    return romanized_words_to_number(text)


# ============================================================
# PAGE CONFIG & STYLES
# ============================================================
st.set_page_config(page_title="Bengali Numeral Converter", layout="wide")
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
.conv-result-row{display:grid;grid-template-columns:6rem 1fr;gap:.35rem .9rem;align-items:baseline}
.conv-result-sublabel{font-family:'DM Sans',sans-serif;font-size:.62rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--ink-faint)}
.conv-result-subvalue{font-family:'Crimson Pro',Georgia,serif;font-size:1.05rem;font-weight:400;color:var(--ink);line-height:1.55;word-break:break-word}
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
st.markdown(CONV_CSS_ADDITIONS, unsafe_allow_html=True)

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

language_nav("Bengali", "converter")

# ── TWO-COLUMN LAYOUT ───────────────────────────────────────────────────────

# initialize so both are accessible across column boundaries
_input_arabic = ""
_input_lang = ""

left_col, right_col = st.columns([1, 1], gap="large")

with right_col:
    # ── DIRECTION SELECTOR ──────────────────────────────────────────────────
    st.markdown('<div class="conv-section-label conv-direction-label">Conversion Direction</div>', unsafe_allow_html=True)

    direction = st.radio(
        "Conversion direction",
        ["Arabic → Bengali", "Bengali → Arabic"],
        horizontal=True,
        label_visibility="collapsed",
        key="bengali_direction",
    )

with left_col:
    # ── PRESET EXAMPLES ─────────────────────────────────────────────────────
    st.markdown('<div class="conv-section-label">Preset Examples</div>', unsafe_allow_html=True)

    arabic_presets  = [0, 5, 12, 21, 100, 325, 12345, 10000000]
    bengali_presets = [
        "শূন্য", "পাঁচ", "বারো", "একুশ",
        "একশ", "তিন শত পঁচিশ", "বারো হাজার তিন শত পঁয়তাল্লিশ", "এক কোটি",
    ]

    with st.container(border=False):
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

    # ── INPUT & CONVERSION ──────────────────────────────────────────────────
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
        _input_arabic = arabic_input
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
        _input_lang = bengali_input

with right_col:
    if direction == "Arabic → Bengali":
        if _input_arabic:
            if _input_arabic.lstrip("-").isdigit():
                try:
                    n      = int(_input_arabic)
                    digits = number_to_bengali_digits(n)
                    beng   = number_to_bengali_words(n, romanized=False)
                    rom    = number_to_bengali_words(n, romanized=True)
                    st.markdown(f"""
                    <div class="conv-result-card">
                        <div class="conv-result-label">Bengali numeral</div>
                        <div class="conv-result-row">
                            <span class="conv-result-sublabel">Digits</span>
                            <span class="conv-result-subvalue">{digits}</span>
                        </div>
                        <div class="conv-result-row">
                            <span class="conv-result-sublabel">Words</span>
                            <span class="conv-result-subvalue">{beng}</span>
                        </div>
                        <div class="conv-result-row">
                            <span class="conv-result-sublabel">Romanized</span>
                            <span class="conv-result-subvalue">{rom}</span>
                        </div>
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
<div class="conv-empty-state">
    <p>Enter a value on the left to see the result.</p>
</div>
""", unsafe_allow_html=True)
    else:
        if _input_lang:
            try:
                result = str(bengali_to_number(_input_lang))
                st.markdown(f"""
                <div class="conv-result-card">
                    <div class="conv-result-label">Arabic numeral</div>
                    <div class="conv-result-value">{result}</div>
                </div>
                """, unsafe_allow_html=True)
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
    Implements the Indian numbering system (lakhs, crores) with standard Bengali number names.
    Data from <a href="https://en.wikipedia.org/wiki/Bengali_numerals" target="_blank">Wikipedia</a>.
    Converter algorithm by Yi Zou. Grammar detail in the Linguistics section.
</div>
""", unsafe_allow_html=True)

# ── NAVIGATION (full width) ──────────────────────────────────
footer_nav("Bengali", "converter")
