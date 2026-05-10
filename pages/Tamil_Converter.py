import streamlit as st
from ui import apply_global_styles, home_nav

# ============================================================
# TAMIL NUMERAL SYSTEM
# Bidirectional: Arabic ↔ Tamil (digits, words, romanized)
# ============================================================

# ------------------------------------------------------------
# 1. TAMIL DIGITS (0-9, plus special symbols for 10, 100, 1000)
# ------------------------------------------------------------
TAMIL_DIGITS = {
    0: "௦", 1: "௧", 2: "௨", 3: "௩", 4: "௪",
    5: "௫", 6: "௬", 7: "௭", 8: "௮", 9: "௯",
    10: "௰", 100: "௱", 1000: "௲",
}

DIGIT_TO_ARABIC = {v: k for k, v in TAMIL_DIGITS.items()}

# ------------------------------------------------------------
# 2. ATOMIC NUMERALS 0–99 — Tamil words and romanized
# ------------------------------------------------------------
TAMIL_ATOMS = {
    0:"சுழியம்",1:"ஒன்று",2:"இரண்டு",3:"மூன்று",4:"நான்கு",
    5:"ஐந்து",6:"ஆறு",7:"ஏழு",8:"எட்டு",9:"ஒன்பது",
    10:"பத்து",11:"பதினொன்று",12:"பன்னிரண்டு",13:"பதின்மூன்று",
    14:"பதினான்கு",15:"பதினைந்து",16:"பதினாறு",17:"பதினேழு",
    18:"பதினெட்டு",19:"பத்தொன்பது",20:"இருபது",
    21:"இருபத்தி ஒன்று",22:"இருபத்தி இரண்டு",23:"இருபத்தி மூன்று",
    24:"இருபத்தி நான்கு",25:"இருபத்தி ஐந்து",26:"இருபத்தி ஆறு",
    27:"இருபத்தி ஏழு",28:"இருபத்தி எட்டு",29:"இருபத்தி ஒன்பது",
    30:"முப்பது",31:"முப்பத்தி ஒன்று",32:"முப்பத்தி இரண்டு",
    33:"முப்பத்தி மூன்று",34:"முப்பத்தி நான்கு",35:"முப்பத்தி ஐந்து",
    36:"முப்பத்தி ஆறு",37:"முப்பத்தி ஏழு",38:"முப்பத்தி எட்டு",
    39:"முப்பத்தி ஒன்பது",40:"நாற்பது",41:"நாற்பத்தி ஒன்று",
    42:"நாற்பத்தி இரண்டு",43:"நாற்பத்தி மூன்று",44:"நாற்பத்தி நான்கு",
    45:"நாற்பத்தி ஐந்து",46:"நாற்பத்தி ஆறு",47:"நாற்பத்தி ஏழு",
    48:"நாற்பத்தி எட்டு",49:"நாற்பத்தி ஒன்பது",50:"ஐம்பது",
    51:"ஐம்பத்தி ஒன்று",52:"ஐம்பத்தி இரண்டு",53:"ஐம்பத்தி மூன்று",
    54:"ஐம்பத்தி நான்கு",55:"ஐம்பத்தி ஐந்து",56:"ஐம்பத்தி ஆறு",
    57:"ஐம்பத்தி ஏழு",58:"ஐம்பத்தி எட்டு",59:"ஐம்பத்தி ஒன்பது",
    60:"அறுபது",61:"அறுபத்தி ஒன்று",62:"அறுபத்தி இரண்டு",
    63:"அறுபத்தி மூன்று",64:"அறுபத்தி நான்கு",65:"அறுபத்தி ஐந்து",
    66:"அறுபத்தி ஆறு",67:"அறுபத்தி ஏழு",68:"அறுபத்தி எட்டு",
    69:"அறுபத்தி ஒன்பது",70:"எழுபது",71:"எழுபத்தி ஒன்று",
    72:"எழுபத்தி இரண்டு",73:"எழுபத்தி மூன்று",74:"எழுபத்தி நான்கு",
    75:"எழுபத்தி ஐந்து",76:"எழுபத்தி ஆறு",77:"எழுபத்தி ஏழு",
    78:"எழுபத்தி எட்டு",79:"எழுபத்தி ஒன்பது",80:"எண்பது",
    81:"எண்பத்தி ஒன்று",82:"எண்பத்தி இரண்டு",83:"எண்பத்தி மூன்று",
    84:"எண்பத்தி நான்கு",85:"எண்பத்தி ஐந்து",86:"எண்பத்தி ஆறு",
    87:"எண்பத்தி ஏழு",88:"எண்பத்தி எட்டு",89:"எண்பத்தி ஒன்பது",
    90:"தொன்னூறு",91:"தொன்னூற்றி ஒன்று",92:"தொன்னூற்றி இரண்டு",
    93:"தொன்னூற்றி மூன்று",94:"தொன்னூற்றி நான்கு",95:"தொன்னூற்றி ஐந்து",
    96:"தொன்னூற்றி ஆறு",97:"தொன்னூற்றி ஏழு",98:"தொன்னூற்றி எட்டு",
    99:"தொன்னூற்றி ஒன்பது",
}

ROMANIZED_ATOMS = {
    0:"suzhiyam",1:"onru",2:"irandu",3:"munru",4:"nanku",
    5:"ainthu",6:"aaru",7:"ezhu",8:"ettu",9:"onpathu",
    10:"paththu",11:"pathinonru",12:"pannirandu",13:"pathinmunru",
    14:"pathinanku",15:"pathiainthu",16:"pathinaaru",17:"pathinezhu",
    18:"pathinettu",19:"paththonpathu",20:"irupathu",
    21:"irupathi onru",22:"irupathi irandu",23:"irupathi munru",
    24:"irupathi nanku",25:"irupathi ainthu",26:"irupathi aaru",
    27:"irupathi ezhu",28:"irupathi ettu",29:"irupathi onpathu",
    30:"muppathu",31:"muppathi onru",32:"muppathi irandu",
    33:"muppathi munru",34:"muppathi nanku",35:"muppathi ainthu",
    36:"muppathi aaru",37:"muppathi ezhu",38:"muppathi ettu",
    39:"muppathi onpathu",40:"narpathu",41:"narpathi onru",
    42:"narpathi irandu",43:"narpathi munru",44:"narpathi nanku",
    45:"narpathi ainthu",46:"narpathi aaru",47:"narpathi ezhu",
    48:"narpathi ettu",49:"narpathi onpathu",50:"aimpathu",
    51:"aimpathi onru",52:"aimpathi irandu",53:"aimpathi munru",
    54:"aimpathi nanku",55:"aimpathi ainthu",56:"aimpathi aaru",
    57:"aimpathi ezhu",58:"aimpathi ettu",59:"aimpathi onpathu",
    60:"arupathu",61:"arupathi onru",62:"arupathi irandu",
    63:"arupathi munru",64:"arupathi nanku",65:"arupathi ainthu",
    66:"arupathi aaru",67:"arupathi ezhu",68:"arupathi ettu",
    69:"arupathi onpathu",70:"ezhupathu",71:"ezhupathi onru",
    72:"ezhupathi irandu",73:"ezhupathi munru",74:"ezhupathi nanku",
    75:"ezhupathi ainthu",76:"ezhupathi aaru",77:"ezhupathi ezhu",
    78:"ezhupathi ettu",79:"ezhupathi onpathu",80:"enpathu",
    81:"enpathi onru",82:"enpathi irandu",83:"enpathi munru",
    84:"enpathi nanku",85:"enpathi ainthu",86:"enpathi aaru",
    87:"enpathi ezhu",88:"enpathi ettu",89:"enpathi onpathu",
    90:"thonnuru",91:"thonnurri onru",92:"thonnurri irandu",
    93:"thonnurri munru",94:"thonnurri nanku",95:"thonnurri ainthu",
    96:"thonnurri aaru",97:"thonnurri ezhu",98:"thonnurri ettu",
    99:"thonnurri onpathu",
}

TAMIL_VALUES    = {v: k for k, v in TAMIL_ATOMS.items()}
ROMANIZED_VALUES = {v: k for k, v in ROMANIZED_ATOMS.items()}

# ------------------------------------------------------------
# 3. BASE UNITS (Indian numbering system)
# ------------------------------------------------------------
BASE_UNITS = [
    ("கோடி",   "kodi",    10_000_000),
    ("இலட்சம்","ilatcham", 100_000),
    ("ஆயிரம்", "ayiram",   1_000),
    ("நூறு",   "nuru",     100),
]

TAMIL_BASE_VALUES    = {tam: value for tam, roman, value in BASE_UNITS}
ROMANIZED_BASE_VALUES = {roman: value for _, roman, value in BASE_UNITS}

# ------------------------------------------------------------
# 4. ARABIC → TAMIL
# ------------------------------------------------------------
def number_to_tamil_digits(n: int) -> str:
    if n == 0:     return TAMIL_DIGITS[0]
    if n == 10:    return TAMIL_DIGITS[10]
    if n == 100:   return TAMIL_DIGITS[100]
    if n == 1000:  return TAMIL_DIGITS[1000]
    return str(n).translate(str.maketrans("0123456789", "௦௧௨௩௪௫௬௭௮௯"))

def number_to_tamil_words(n: int, romanized: bool = False) -> str:
    if n < 0:
        raise ValueError("Negative numbers are not supported")
    if n == 0:
        return ROMANIZED_ATOMS[0] if romanized else TAMIL_ATOMS[0]
    atom_map = ROMANIZED_ATOMS if romanized else TAMIL_ATOMS
    if n <= 99:
        return atom_map[n]
    if 100 <= n < 1000:
        hundreds  = n // 100
        remainder = n % 100
        hundred_word = "nuru" if romanized else "நூறு"
        prefix = hundred_word if hundreds == 1 else atom_map[hundreds] + " " + hundred_word
        return prefix if remainder == 0 else prefix + " " + atom_map[remainder]
    for tam, roman, value in BASE_UNITS:
        if n >= value:
            quotient  = n // value
            remainder = n % value
            unit_name = roman if romanized else tam
            prefix = unit_name if quotient == 1 else number_to_tamil_words(quotient, romanized) + " " + unit_name
            return prefix if remainder == 0 else prefix + " " + number_to_tamil_words(remainder, romanized)
    return ""

# ------------------------------------------------------------
# 5. TAMIL → ARABIC
# ------------------------------------------------------------
def tamil_digits_to_number(text: str) -> int:
    cleaned = text.strip().replace(" ", "")
    if not cleaned:
        raise ValueError("Empty input")
    if cleaned in DIGIT_TO_ARABIC:
        return DIGIT_TO_ARABIC[cleaned]
    result_str = ""
    for ch in cleaned:
        if ch in DIGIT_TO_ARABIC:
            result_str += str(DIGIT_TO_ARABIC[ch])
        else:
            raise ValueError(f"Invalid Tamil digit character: {ch!r}")
    return int(result_str)

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

def tamil_words_to_number(text: str) -> int:
    tokens = text.strip().split()
    result = _parse_words(tokens, TAMIL_VALUES, TAMIL_BASE_VALUES)
    if result is None:
        raise ValueError("Invalid Tamil numeral")
    return result

def romanized_words_to_number(text: str) -> int:
    tokens = text.strip().split()
    result = _parse_words(tokens, ROMANIZED_VALUES, ROMANIZED_BASE_VALUES)
    if result is None:
        raise ValueError("Invalid romanized Tamil numeral")
    return result

def tamil_to_number(text: str) -> int:
    text = text.strip()
    if not text:
        raise ValueError("Empty input")
    tamil_chars = set("௦௧௨௩௪௫௬௭௮௯௰௱௲")
    if all(ch in tamil_chars or ch.isspace() for ch in text):
        return tamil_digits_to_number(text)
    if any('\u0B80' <= ch <= '\u0BFF' for ch in text):
        return tamil_words_to_number(text)
    return romanized_words_to_number(text)


# ============================================================
# PAGE CONFIG & STYLES
# ============================================================
st.set_page_config(page_title="Tamil Numeral Converter", layout="centered")
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
.conv-result-card{background:rgba(46,107,122,.04);border:1px solid rgba(46,107,122,.18);border-left:3px solid var(--teal);border-radius:0 4px 4px 0;padding:.85rem 1.1rem;margin-top:.8rem}
.conv-result-label{font-family:'DM Sans',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.14em;color:var(--teal);margin-bottom:.55rem}
.conv-result-row{display:grid;grid-template-columns:6rem 1fr;gap:.35rem .9rem;align-items:baseline}
.conv-result-sublabel{font-family:'DM Sans',sans-serif;font-size:.62rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--ink-faint)}
.conv-result-subvalue{font-family:'Crimson Pro',Georgia,serif;font-size:1.05rem;font-weight:400;color:var(--ink);line-height:1.55;word-break:break-word}
.conv-result-single{font-family:'Crimson Pro',Georgia,serif;font-size:1.05rem;font-weight:400;color:var(--ink);line-height:1.55;word-break:break-word}
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
    <div class="conv-masthead-title">Tamil Numerals</div>
    <div class="conv-masthead-desc">
        Bidirectional conversion between Arabic numerals and Tamil —
        Tamil script digits, Tamil words, and romanized forms.
    </div>
</div>
""", unsafe_allow_html=True)

# ── DIRECTION SELECTOR ──────────────────────────────────────────────────────
st.markdown('<div class="conv-section-label">Conversion Direction</div>', unsafe_allow_html=True)

direction = st.radio(
    "Conversion direction",
    ["Arabic → Tamil", "Tamil → Arabic"],
    horizontal=True,
    label_visibility="collapsed",
    key="tamil_direction",
)

# ── PRESET EXAMPLES ─────────────────────────────────────────────────────────
st.markdown('<div class="conv-section-label">Preset Examples</div>', unsafe_allow_html=True)

arabic_presets = [0, 5, 11, 21, 100, 325, 1000, 10000000]
tamil_presets  = [
    "சுழியம்", "ஐந்து", "பதினொன்று", "இருபத்தி ஒன்று",
    "நூறு", "முப்பத்தி ஐந்து", "ஆயிரம்", "ஒரு கோடி",
]

with st.container(border=True):
    st.markdown('<p class="conv-presets-sublabel">Click a value to load it</p>', unsafe_allow_html=True)
    cols = st.columns(4)
    if direction == "Arabic → Tamil":
        for i, num in enumerate(arabic_presets):
            if cols[i % 4].button(str(num), key=f"p_a_{i}", use_container_width=True):
                st.session_state["arabic_input"] = str(num)
    else:
        for i, txt in enumerate(tamil_presets):
            if cols[i % 4].button(txt, key=f"p_b_{i}", use_container_width=True):
                st.session_state["tamil_input"] = txt

# ── INPUT & CONVERSION ──────────────────────────────────────────────────────
st.markdown('<div class="conv-section-label">Convert</div>', unsafe_allow_html=True)

if direction == "Arabic → Tamil":
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
                digits = number_to_tamil_digits(n)
                words  = number_to_tamil_words(n, romanized=False)
                rom    = number_to_tamil_words(n, romanized=True)
                st.markdown(f"""
                <div class="conv-result-card">
                    <div class="conv-result-label">Tamil numeral</div>
                    <div class="conv-result-row">
                        <span class="conv-result-sublabel">Digits</span>
                        <span class="conv-result-subvalue">{digits}</span>
                    </div>
                    <div class="conv-result-row">
                        <span class="conv-result-sublabel">Words</span>
                        <span class="conv-result-subvalue">{words}</span>
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
    <div class="conv-input-card">
        <div class="conv-input-title">Enter a Tamil numeral</div>
        <div class="conv-input-hint">
            Tamil script digits (e.g. <em>௩௨௫</em>), Tamil words
            (e.g. <em>முப்பத்தி ஐந்து</em>), or romanized words (e.g. <em>muppathi ainthu</em>).
        </div>
    </div>
    """, unsafe_allow_html=True)
    tamil_input = st.text_input(
        "Tamil numeral", key="tamil_input",
        placeholder="e.g. முப்பத்தி ஐந்து",
        label_visibility="collapsed",
    )
    if tamil_input:
        try:
            result = str(tamil_to_number(tamil_input))
            st.markdown(f"""
            <div class="conv-result-card">
                <div class="conv-result-label">Arabic numeral</div>
                <div class="conv-result-single">{result}</div>
            </div>
            """, unsafe_allow_html=True)
        except Exception as e:
            st.markdown(f'<div class="conv-error-card"><p class="conv-error-text">{e}</p></div>',
                        unsafe_allow_html=True)

# ── NAVIGATION ──────────────────────────────────────────────
st.markdown('<div class="nav-row">', unsafe_allow_html=True)
st.page_link("pages/Tamil_Linguistics.py", label="Tamil Linguistics →")
st.page_link("Home.py", label="← Home")
st.markdown('</div>', unsafe_allow_html=True)