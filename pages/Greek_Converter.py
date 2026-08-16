import streamlit as st
from ui import apply_global_styles, language_nav, CONV_CSS_ADDITIONS, footer_nav
import unicodedata

"""
Greek numeral converter: Arabic ↔ Greek (Greek script words, romanized words)
Fully corrected with feminine hundreds and robust parsing.
Based on: https://www.omniglot.com/language/numbers/greek.htm
"""

# ── apply_global_styles must be called before set_page_config ──────────────
apply_global_styles()
import unicodedata  # noqa: F811 (re-import matches original structure)

# ------------------------------------------------------------
# 1. ATOMIC NUMERALS (0–19)
# ------------------------------------------------------------
GREEK_ATOMS = {
    0: "μηδέν", 1: "ένα",   2: "δύο",   3: "τρία",  4: "τέσσερα",
    5: "πέντε", 6: "έξι",   7: "επτά",  8: "οκτώ",  9: "εννιά",
    10: "δέκα", 11: "έντεκα", 12: "δώδεκα", 13: "δεκατρία",
    14: "δεκατέσσερα", 15: "δεκαπέντε", 16: "δεκαέξι",
    17: "δεκαεπτά", 18: "δεκαοκτώ", 19: "δεκαεννιά",
}

ROMANIZED_ATOMS = {
    0: "midén",  1: "éna",     2: "dýo",   3: "tría",   4: "téssera",
    5: "pénte",  6: "éxi",     7: "eptá",  8: "októ",   9: "enniá",
    10: "déka",  11: "énteka", 12: "dódéka", 13: "dekatría",
    14: "dekatéssera", 15: "dekapénte", 16: "dekaéxi",
    17: "dekaeptá", 18: "dekaoktó", 19: "dekaenniá",
}

# ------------------------------------------------------------
# 2. TENS (20–90)
# ------------------------------------------------------------
TENS = {
    20: ("είκοσι", "eikósi"),   30: ("τριάντα", "triánta"),
    40: ("σαράντα", "saránta"), 50: ("πενήντα", "penínta"),
    60: ("εξήντα", "exínta"),   70: ("εβδομήντα", "ebdomínta"),
    80: ("ογδόντα", "ogdónta"), 90: ("ενενήντα", "enenínta"),
}

# ------------------------------------------------------------
# 3. HUNDREDS – neuter (standalone) and feminine (with thousands)
# ------------------------------------------------------------
HUNDREDS_NEUTER = {
    100: ("εκατό", "ekató"),       200: ("διακόσια", "diakósia"),
    300: ("τριακόσια", "triakósia"), 400: ("τετρακόσια", "tetrakósia"),
    500: ("πεντακόσια", "pentakósia"), 600: ("εξακόσια", "exakósia"),
    700: ("επτακόσια", "eptakósia"),   800: ("οκτακόσια", "oktakósia"),
    900: ("εννιακόσια", "enniakósia"),
}

HUNDREDS_FEMININE = {
    200: ("διακόσιες", "diakósies"),   300: ("τριακόσιες", "triakósies"),
    400: ("τετρακόσιες", "tetrakósies"), 500: ("πεντακόσιες", "pentakósies"),
    600: ("εξακόσιες", "exakósies"),   700: ("επτακόσιες", "eptakósies"),
    800: ("οκτακόσιες", "oktakósies"), 900: ("εννιακόσιες", "enniakósies"),
}

# ------------------------------------------------------------
# 4. THOUSANDS & MILLIONS
# ------------------------------------------------------------
THOUSAND_SINGULAR = ("χίλια", "chília")
THOUSAND_PLURAL_WORDS = ["χιλιάδες", "chiliádes"]
MILLION_SINGULAR = ("ένα εκατομμύριο", "éna ekatommýrio")
MILLION_PLURAL_WORDS = ["εκατομμύρια", "ekatommýria", "εκατομμύριο", "ekatommýrio"]

# ------------------------------------------------------------
# 5. NORMALIZER
# ------------------------------------------------------------
def _norm(s):
    return unicodedata.normalize("NFC", s)

# ------------------------------------------------------------
# 6. ATOMIC LOOKUP (for parser)
# ------------------------------------------------------------
ATOMIC = {}
for k, v in GREEK_ATOMS.items():
    ATOMIC[_norm(v)] = k
for k, v in ROMANIZED_ATOMS.items():
    ATOMIC[_norm(v)] = k
for val, (g, r) in TENS.items():
    ATOMIC[_norm(g)] = val
    ATOMIC[_norm(r)] = val
for val, (g, r) in HUNDREDS_NEUTER.items():
    ATOMIC[_norm(g)] = val
    ATOMIC[_norm(r)] = val
for val, (g, r) in HUNDREDS_FEMININE.items():
    ATOMIC[_norm(g)] = val
    ATOMIC[_norm(r)] = val

# ------------------------------------------------------------
# 7. MULTIPLICATIVE BASE WORDS (for thousands and millions plural)
# ------------------------------------------------------------
MULT = {}
for w in THOUSAND_PLURAL_WORDS:
    MULT[_norm(w)] = 1000
for w in MILLION_PLURAL_WORDS:
    MULT[_norm(w)] = 1_000_000

# ------------------------------------------------------------
# 8. ARABIC → GREEK GENERATOR
# ------------------------------------------------------------
def number_to_greek_words(n: int, romanized: bool = False) -> str:
    if n < 0:
        raise ValueError("Negative numbers are not supported")
    if n == 0:
        return _norm(ROMANIZED_ATOMS[0] if romanized else GREEK_ATOMS[0])

    def _choose(pair):
        g, r = pair
        return _norm(r if romanized else g)

    if n <= 19:
        return _norm(ROMANIZED_ATOMS[n] if romanized else GREEK_ATOMS[n])
    if n <= 99:
        ten = (n // 10) * 10
        unit = n % 10
        ten_word = _choose(TENS[ten])
        if unit == 0:
            return ten_word
        return ten_word + " " + _norm(ROMANIZED_ATOMS[unit] if romanized else GREEK_ATOMS[unit])
    if n <= 999:
        hundreds = (n // 100) * 100
        rem = n % 100
        hundred_word = _choose(HUNDREDS_NEUTER[hundreds])
        if rem == 0:
            return hundred_word
        return hundred_word + " " + number_to_greek_words(rem, romanized)
    if n <= 999_999:
        thousands = n // 1000
        rem = n % 1000
        if thousands == 1:
            thousand_word = _norm(THOUSAND_SINGULAR[1] if romanized else THOUSAND_SINGULAR[0])
        else:
            multiplier = number_to_greek_words(thousands, romanized)
            plural = _norm("chiliádes" if romanized else "χιλιάδες")
            thousand_word = multiplier + " " + plural
        if rem == 0:
            return thousand_word
        return thousand_word + " " + number_to_greek_words(rem, romanized)
    millions = n // 1_000_000
    rem = n % 1_000_000
    if millions == 1:
        million_word = _norm(MILLION_SINGULAR[1] if romanized else MILLION_SINGULAR[0])
    else:
        multiplier = number_to_greek_words(millions, romanized)
        plural = _norm("ekatommýria" if romanized else "εκατομμύρια")
        million_word = multiplier + " " + plural
    if rem == 0:
        return million_word
    return million_word + " " + number_to_greek_words(rem, romanized)

# ------------------------------------------------------------
# 9. GREEK → ARABIC PARSER
# ------------------------------------------------------------
def greek_to_number(text: str) -> int:
    text = _norm(text.strip())
    if not text:
        raise ValueError("Empty input")
    tokens = text.split()
    n = len(tokens)

    million_idx = None
    for i, tok in enumerate(tokens):
        if tok in MULT and MULT[tok] == 1_000_000:
            million_idx = i
            break

    thousand_idx = None
    for i, tok in enumerate(tokens):
        if i != million_idx and tok in MULT and MULT[tok] == 1000:
            thousand_idx = i
            break

    total = 0
    pos = 0

    if million_idx is not None:
        mult = 1
        if pos < million_idx:
            mult = sum(ATOMIC[tok] for tok in tokens[pos:million_idx] if tok in ATOMIC)
        total += mult * 1_000_000
        pos = million_idx + 1

    if thousand_idx is not None:
        mult = 1
        if pos < thousand_idx:
            mult = sum(ATOMIC[tok] for tok in tokens[pos:thousand_idx] if tok in ATOMIC)
        total += mult * 1000
        pos = thousand_idx + 1

    if pos < n:
        rem = sum(ATOMIC[tok] for tok in tokens[pos:] if tok in ATOMIC)
        total += rem

    return total


# ============================================================
# PAGE CONFIG & STYLES
# ============================================================
st.set_page_config(page_title="Greek Numeral Converter", layout="wide")

CONV_CSS = """
<style>
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
</style>
"""
st.markdown(CONV_CSS, unsafe_allow_html=True)
st.markdown(CONV_CSS_ADDITIONS, unsafe_allow_html=True)

# ── MASTHEAD ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="conv-masthead">
    <div class="conv-masthead-eyebrow">Numeral Converter</div>
    <div class="conv-masthead-title">Greek Numerals</div>
    <div class="conv-masthead-desc">
        Bidirectional conversion between Arabic numerals and Modern Greek words —
        Greek script and romanized forms.
    </div>
</div>
""", unsafe_allow_html=True)

language_nav("Greek", "converter")

# ── TWO-COLUMN LAYOUT ────────────────────────────────────────────────────────

# initialize so both are accessible across column boundaries
_input_arabic = ""
_input_lang = ""

left_col, right_col = st.columns([1, 1], gap="large")

with right_col:
    # ── DIRECTION SELECTOR ──────────────────────────────────────────────────
    st.markdown('<div class="conv-section-label conv-direction-label">Conversion Direction</div>', unsafe_allow_html=True)

    direction = st.radio(
        "Conversion direction",
        ["Arabic → Greek", "Greek → Arabic"],
        horizontal=True,
        label_visibility="collapsed",
        key="greek_direction",
    )

with left_col:
    # ── PRESET EXAMPLES ─────────────────────────────────────────────────────
    st.markdown('<div class="conv-section-label">Preset Examples</div>', unsafe_allow_html=True)

    arabic_presets = [0, 1, 5, 12, 21, 100, 325, 1234]
    greek_presets  = [
        "μηδέν", "ένα", "πέντε", "δώδεκα",
        "είκοσι ένα", "εκατό",
        "τριακόσια είκοσι πέντε", "χίλια διακόσια τριάντα τέσσερα",
    ]

    with st.container(border=False):
        st.markdown('<p class="conv-presets-sublabel">Click a value to load it</p>', unsafe_allow_html=True)
        cols = st.columns(4)
        if direction == "Arabic → Greek":
            for i, num in enumerate(arabic_presets):
                if cols[i % 4].button(str(num), key=f"p_a_{i}", use_container_width=True):
                    st.session_state["arabic_input"] = str(num)
        else:
            for i, txt in enumerate(greek_presets):
                if cols[i % 4].button(txt, key=f"p_b_{i}", use_container_width=True):
                    st.session_state["greek_input"] = txt

    # ── INPUT & CONVERSION ──────────────────────────────────────────────────
    st.markdown('<div class="conv-section-label">Convert</div>', unsafe_allow_html=True)

    if direction == "Arabic → Greek":
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
            <div class="conv-input-title">Enter a Greek numeral</div>
            <div class="conv-input-hint">Greek script or romanized form, e.g. <em>τριακόσια είκοσι πέντε</em> or <em>triakósia eíkosi pénte</em>.</div>
        </div>
        """, unsafe_allow_html=True)
        greek_input = st.text_input(
            "Greek numeral", key="greek_input",
            placeholder="e.g. τριακόσια είκοσι πέντε", label_visibility="collapsed",
        )
        _input_lang = greek_input

with right_col:
    if direction == "Arabic → Greek":
        if _input_arabic:
            if _input_arabic.lstrip("-").isdigit():
                try:
                    n = int(_input_arabic)
                    gw = number_to_greek_words(n, romanized=False)
                    rw = number_to_greek_words(n, romanized=True)
                    st.markdown(f"""
                    <div class="conv-result-card">
                        <div class="conv-result-label">Greek numeral</div>
                        <div class="conv-result-row">
                            <span class="conv-result-sublabel">Script</span>
                            <span class="conv-result-subvalue">{gw}</span>
                        </div>
                        <div class="conv-result-row">
                            <span class="conv-result-sublabel">Romanized</span>
                            <span class="conv-result-subvalue">{rw}</span>
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
                result = str(greek_to_number(_input_lang))
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


# ── NAVIGATION (full width) ──────────────────────────────────
footer_nav("Greek", "converter")
