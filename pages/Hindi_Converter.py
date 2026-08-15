import streamlit as st
from ui import apply_global_styles, language_nav, CONV_CSS_ADDITIONS, footer_nav

# ============================================================
# HINDI NUMERAL SYSTEM
# Bidirectional: Arabic ↔ Hindi (Devanagari digits, words, romanized)
# ============================================================

# ------------------------------------------------------------
# 1. ATOMIC NUMERALS (0–99)
# ------------------------------------------------------------
DEVANAGARI_ATOMS = {
    0:"शून्य",1:"एक",2:"दो",3:"तीन",4:"चार",5:"पाँच",6:"छह",7:"सात",8:"आठ",9:"नौ",
    10:"दस",11:"ग्यारह",12:"बारह",13:"तेरह",14:"चौदह",15:"पंद्रह",16:"सोलह",
    17:"सत्रह",18:"अठारह",19:"उन्नीस",20:"बीस",21:"इक्कीस",22:"बाईस",23:"तेईस",
    24:"चौबीस",25:"पच्चीस",26:"छब्बीस",27:"सत्ताईस",28:"अट्ठाईस",29:"उनतीस",
    30:"तीस",31:"इकतीस",32:"बत्तीस",33:"तैंतीस",34:"चौंतीस",35:"पैंतीस",
    36:"छत्तीस",37:"सैंतीस",38:"अड़तीस",39:"उनतालीस",40:"चालीस",41:"इकतालीस",
    42:"बयालीस",43:"तैंतालीस",44:"चौवालीस",45:"पैंतालीस",46:"छियालीस",
    47:"सैंतालीस",48:"अड़तालीस",49:"उनचास",50:"पचास",51:"इक्यावन",52:"बावन",
    53:"तिरेपन",54:"चौवन",55:"पचपन",56:"छप्पन",57:"सत्तावन",58:"अट्ठावन",
    59:"उनसठ",60:"साठ",61:"इकसठ",62:"बासठ",63:"तिरेसठ",64:"चौंसठ",65:"पैंसठ",
    66:"छियासठ",67:"सड़सठ",68:"अड़सठ",69:"उनहत्तर",70:"सत्तर",71:"इकहत्तर",
    72:"बहत्तर",73:"तिहत्तर",74:"चौहत्तर",75:"पचहत्तर",76:"छिहत्तर",
    77:"सतहत्तर",78:"अठहत्तर",79:"उनासी",80:"अस्सी",81:"इक्यासी",82:"बयासी",
    83:"तिरासी",84:"चौरासी",85:"पचासी",86:"छियासी",87:"सत्तासी",88:"अट्ठासी",
    89:"नवासी",90:"नब्बे",91:"इक्यानवे",92:"बानवे",93:"तिरानवे",94:"चौरानवे",
    95:"पंचानवे",96:"छियानवे",97:"सत्तानवे",98:"अट्ठानवे",99:"निन्यानवे",
}

ROMANIZED_ATOMS = {
    0:"shoonya",1:"ek",2:"do",3:"teen",4:"chaar",5:"paanch",6:"chhah",7:"saat",
    8:"aath",9:"nau",10:"das",11:"gyaarah",12:"baarah",13:"terah",14:"chaudah",
    15:"pandrah",16:"solah",17:"satrah",18:"athaarah",19:"unnees",20:"bees",
    21:"ikkees",22:"baaees",23:"teis",24:"chaubees",25:"pachchees",26:"chhabbees",
    27:"sattaais",28:"atthaais",29:"unatees",30:"tees",31:"ikatees",32:"batees",
    33:"taintees",34:"chauntees",35:"paiñtees",36:"chhattees",37:"saiñtees",
    38:"adatees",39:"unataalees",40:"chaalees",41:"ikataalees",42:"bayaalees",
    43:"taintaalees",44:"chauvaalees",45:"paiñtaalees",46:"chiyaalees",
    47:"saiñtaalees",48:"adataalees",49:"unachaas",50:"pachaas",51:"ikyaavan",
    52:"baavan",53:"tirepan",54:"chauvan",55:"pachapan",56:"chhappan",
    57:"sattaavan",58:"atthaavan",59:"unsath",60:"saath",61:"ikasath",
    62:"baasath",63:"tiresath",64:"chausath",65:"paiñsath",66:"chiyaasath",
    67:"sadasath",68:"adasath",69:"unahtarr",70:"sattar",71:"ikahtarr",
    72:"bahtarr",73:"tihtarr",74:"chauhtarr",75:"pachahtarr",76:"chhihtarr",
    77:"satahtarr",78:"athahtarr",79:"unaasee",80:"assee",81:"ikyaasee",
    82:"bayaasee",83:"tiraasee",84:"chauraasee",85:"pachaasee",86:"chiyaasee",
    87:"sattaasee",88:"atthaasee",89:"navaasee",90:"nabbe",91:"ikyaanave",
    92:"baanave",93:"tiraanave",94:"chauraanave",95:"panchaanave",96:"chiyaanave",
    97:"sattaanave",98:"atthaanave",99:"ninyaanave",
}

DEVANAGARI_VALUES = {v: k for k, v in DEVANAGARI_ATOMS.items()}
ROMANIZED_VALUES  = {v: k for k, v in ROMANIZED_ATOMS.items()}

# ------------------------------------------------------------
# 2. BASE UNITS (Indian numbering system)
# ------------------------------------------------------------
BASE_UNITS = [
    ("करोड़", "crore",  10_000_000),
    ("लाख",  "lakh",   100_000),
    ("हज़ार", "hazaar", 1_000),
    ("सौ",   "sau",    100),
]

DEVANAGARI_BASE_VALUES = {deva: value for deva, roman, value in BASE_UNITS}
ROMANIZED_BASE_VALUES  = {roman: value for _, roman, value in BASE_UNITS}
DEVANAGARI_BASE_VALUES["एक सौ"] = 100
ROMANIZED_BASE_VALUES["ek sau"] = 100

# ------------------------------------------------------------
# 3. ARABIC → HINDI
# ------------------------------------------------------------
def number_to_hindi_digits(n: int) -> str:
    return str(n).translate(str.maketrans("0123456789", "०१२३४५६७८९"))

def number_to_hindi_words(n: int, romanized: bool = False) -> str:
    if n < 0:
        raise ValueError("Negative numbers are not supported")
    if n == 0:
        return ROMANIZED_ATOMS[0] if romanized else DEVANAGARI_ATOMS[0]
    atom_map = ROMANIZED_ATOMS if romanized else DEVANAGARI_ATOMS
    if n <= 99 and n in atom_map:
        return atom_map[n]
    if 100 <= n < 200:
        if n == 100:
            return "sau" if romanized else "सौ"
        one     = "ek"  if romanized else "एक"
        hundred = "sau" if romanized else "सौ"
        return f"{one} {hundred} {number_to_hindi_words(n - 100, romanized)}"
    for deva, roman, value in BASE_UNITS:
        if n >= value:
            q, r = n // value, n % value
            unit = roman if romanized else deva
            if q == 1 and value >= 1000:
                prefix = ("ek" if romanized else "एक") + " " + unit
            else:
                prefix = number_to_hindi_words(q, romanized) + " " + unit
            return prefix if r == 0 else prefix + " " + number_to_hindi_words(r, romanized)
    return ""

# ------------------------------------------------------------
# 4. HINDI → ARABIC
# ------------------------------------------------------------
def hindi_digits_to_number(text: str) -> int:
    cleaned = text.strip().replace(" ", "")
    arabic_str = cleaned.translate(str.maketrans("०१२३४५६७८९", "0123456789"))
    try:
        return int(arabic_str)
    except ValueError:
        raise ValueError("Invalid Devanagari digit sequence")

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

def hindi_words_to_number(text: str) -> int:
    tokens = text.strip().split()
    result = _parse_words(tokens, DEVANAGARI_VALUES, DEVANAGARI_BASE_VALUES)
    if result is None:
        raise ValueError("Invalid Devanagari numeral")
    return result

def romanized_words_to_number(text: str) -> int:
    tokens = text.strip().split()
    result = _parse_words(tokens, ROMANIZED_VALUES, ROMANIZED_BASE_VALUES)
    if result is None:
        raise ValueError("Invalid romanized Hindi numeral")
    return result

def hindi_to_number(text: str) -> int:
    text = text.strip()
    if not text:
        raise ValueError("Empty input")
    if all(ch in "०१२३४५६७८९" or ch.isspace() for ch in text):
        return hindi_digits_to_number(text)
    if any('ऀ' <= ch <= 'ॿ' for ch in text):
        return hindi_words_to_number(text)
    return romanized_words_to_number(text)


# ============================================================
# PAGE CONFIG & STYLES
# ============================================================
st.set_page_config(page_title="Hindi Numeral Converter", layout="wide")
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
    <div class="conv-masthead-title">Hindi Numerals</div>
    <div class="conv-masthead-desc">
        Bidirectional conversion between Arabic numerals and Hindi —
        Devanagari digits, Devanagari words, and romanized forms.
    </div>
</div>
""", unsafe_allow_html=True)

language_nav("Hindi", "converter")

# ── INITIALIZE INPUT VARS ─────────────────────────────────────────────────────
arabic_input = ""
hindi_input = ""

# ── TWO COLUMN LAYOUT ─────────────────────────────────────────────────────────
left_col, right_col = st.columns([1, 1], gap="large")

with right_col:
    # ── DIRECTION SELECTOR ──────────────────────────────────────────────────
    st.markdown('<div class="conv-section-label conv-direction-label">Conversion Direction</div>', unsafe_allow_html=True)

    direction = st.radio(
        "Conversion direction",
        ["Arabic → Hindi", "Hindi → Arabic"],
        horizontal=True,
        label_visibility="collapsed",
        key="hindi_direction",
    )

with left_col:
    # ── PRESET EXAMPLES ─────────────────────────────────────────────────────
    st.markdown('<div class="conv-section-label">Preset Examples</div>', unsafe_allow_html=True)

    arabic_presets = [0, 5, 12, 21, 100, 325, 12345, 10000000]
    hindi_presets  = [
        "शून्य", "पाँच", "बारह", "इक्कीस",
        "सौ", "तीन सौ पच्चीस", "बारह हज़ार तीन सौ पैंतालीस", "एक करोड़",
    ]

    with st.container(border=True):
        st.markdown('<p class="conv-presets-sublabel">Click a value to load it</p>', unsafe_allow_html=True)
        cols = st.columns(4)
        if direction == "Arabic → Hindi":
            for i, num in enumerate(arabic_presets):
                if cols[i % 4].button(str(num), key=f"p_a_{i}", use_container_width=True):
                    st.session_state["arabic_input"] = str(num)
        else:
            for i, txt in enumerate(hindi_presets):
                if cols[i % 4].button(txt, key=f"p_b_{i}", use_container_width=True):
                    st.session_state["hindi_input"] = txt

    # ── INPUT & CONVERSION ──────────────────────────────────────────────────
    st.markdown('<div class="conv-section-label">Convert</div>', unsafe_allow_html=True)

    if direction == "Arabic → Hindi":
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
    else:
        st.markdown("""
        <div class="conv-input-card">
            <div class="conv-input-title">Enter a Hindi numeral</div>
            <div class="conv-input-hint">Devanagari digits (०-९), Devanagari words, or romanized words.</div>
        </div>
        """, unsafe_allow_html=True)
        hindi_input = st.text_input(
            "Hindi numeral", key="hindi_input",
            placeholder="e.g. तीन सौ पच्चीस", label_visibility="collapsed",
        )

with right_col:
    if direction == "Arabic → Hindi":
        if arabic_input:
            if arabic_input.lstrip("-").isdigit():
                try:
                    n      = int(arabic_input)
                    digits = number_to_hindi_digits(n)
                    deva   = number_to_hindi_words(n, romanized=False)
                    rom    = number_to_hindi_words(n, romanized=True)
                    st.markdown(f"""
                    <div class="conv-result-card">
                        <div class="conv-result-label">Hindi numeral</div>
                        <div class="conv-result-row">
                            <span class="conv-result-sublabel">Digits</span>
                            <span class="conv-result-subvalue">{digits}</span>
                        </div>
                        <div class="conv-result-row">
                            <span class="conv-result-sublabel">Words</span>
                            <span class="conv-result-subvalue">{deva}</span>
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
        if hindi_input:
            try:
                result = str(hindi_to_number(hindi_input))
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


# ── NAVIGATION ──────────────────────────────────────────────
footer_nav("Hindi", "converter")
