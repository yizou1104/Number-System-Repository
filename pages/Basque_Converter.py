import streamlit as st
from ui import apply_global_styles

# ============================================================
# BASQUE NUMERAL GENERATOR & PARSER (BATUA)
# Arabic ↔ Basque bidirectional conversion
#
# Grammar principles implemented:
# - Lexical blocking (1–19, 40, 60, 80, 100–900, 1000)
# - Vigesimal base (20, 40, 60, 80)
# - Additive dominance (eta)
# - Multiplicative composition for thousands > 1
# ============================================================

# ------------------------------------------------------------
# 1. ATOMIC NUMERALS (0–19)
# ------------------------------------------------------------
ATOMS = {
    0: "zero",  1: "bat",    2: "bi",       3: "hiru",
    4: "lau",   5: "bost",   6: "sei",      7: "zazpi",
    8: "zortzi",9: "bederatzi", 10: "hamar",
    11: "hamaika",   12: "hamabi",    13: "hamahiru",
    14: "hamalau",   15: "hamabost",  16: "hamasei",
    17: "hamazazpi", 18: "hemezortzi",19: "hemeretzi",
}

# ------------------------------------------------------------
# 2. BASE UNITS AND FUSED FORMS
# ------------------------------------------------------------
BASE_20 = "hogei"

TWENTIES_MAP = {
    1: "hogei", 2: "berrogei", 3: "hirurogei", 4: "laurogei",
}

HUNDREDS_MAP = {
    1: "ehun",      2: "berrehun",       3: "hirurehun",
    4: "laurehun",  5: "bostehun",       6: "seiehun",
    7: "zazpiehun", 8: "zortziehun",     9: "bederatziehun",
}

THOUSAND = "mila"

# ------------------------------------------------------------
# 3. MORPHOLOGICAL OPERATORS
# ------------------------------------------------------------
def additive(x, y):
    return f"{x} eta {y}"

def multiplicative(x, base):
    return f"{x} {base}"

# ------------------------------------------------------------
# 4. CORE GENERATOR (ARABIC → BASQUE)
# ------------------------------------------------------------
def number_to_basque(n):
    if n < 0:
        raise ValueError("Negative numbers are not supported")
    if n in ATOMS:
        return ATOMS[n]
    if n >= 1000:
        thousands = n // 1000
        remainder = n % 1000
        head = THOUSAND if thousands == 1 else multiplicative(number_to_basque(thousands), THOUSAND)
        return head if remainder == 0 else additive(head, number_to_basque(remainder))
    if n >= 100:
        hundreds = n // 100
        remainder = n % 100
        head = HUNDREDS_MAP[hundreds]
        return head if remainder == 0 else additive(head, number_to_basque(remainder))
    if n >= 20:
        twenties = n // 20
        remainder = n % 20
        head = TWENTIES_MAP[twenties]
        return head if remainder == 0 else additive(head, number_to_basque(remainder))
    raise RuntimeError(f"Unexpected number: {n}")

# ------------------------------------------------------------
# 5. REVERSE PARSER (BASQUE → ARABIC)
# ------------------------------------------------------------
ATOM_VALUES = {v: k for k, v in ATOMS.items()}

LEXICAL_VALUES = {
    "hogei": 20, "berrogei": 40, "hirurogei": 60, "laurogei": 80,
    "ehun": 100, "berrehun": 200, "hirurehun": 300, "laurehun": 400,
    "bostehun": 500, "seiehun": 600, "zazpiehun": 700,
    "zortziehun": 800, "bederatziehun": 900, "mila": 1000,
}

def basque_to_number(text):
    text = text.strip()
    if not text:
        raise ValueError("Empty input")
    tokens = text.split()

    if "eta" in tokens:
        idx = tokens.index("eta")
        return basque_to_number(" ".join(tokens[:idx])) + basque_to_number(" ".join(tokens[idx + 1:]))

    if "mila" in tokens:
        idx = tokens.index("mila")
        left, right = tokens[:idx], tokens[idx + 1:]
        multiplier = 1 if not left else basque_to_number(" ".join(left))
        value = multiplier * 1000
        if right:
            value += basque_to_number(" ".join(right))
        return value

    hundred_words = set(HUNDREDS_MAP.values())
    for word in hundred_words:
        if word in tokens:
            idx = tokens.index(word)
            left, right = tokens[:idx], tokens[idx + 1:]
            multiplier = 1 if not left else basque_to_number(" ".join(left))
            value = multiplier * LEXICAL_VALUES[word]
            if right:
                value += basque_to_number(" ".join(right))
            return value

    for word in {"hogei", "berrogei", "hirurogei", "laurogei"}:
        if word in tokens:
            idx = tokens.index(word)
            left, right = tokens[:idx], tokens[idx + 1:]
            multiplier = 1 if not left else basque_to_number(" ".join(left))
            value = multiplier * LEXICAL_VALUES[word]
            if right:
                value += basque_to_number(" ".join(right))
            return value

    if text in ATOM_VALUES:
        return ATOM_VALUES[text]
    if text in LEXICAL_VALUES:
        return LEXICAL_VALUES[text]
    raise ValueError(f"Unrecognised Basque numeral: '{text}'")


# ============================================================
# PAGE CONFIG & GLOBAL STYLES
# ============================================================
st.set_page_config(page_title="Basque Numeral Converter", layout="centered")
apply_global_styles()

# ============================================================
# CONVERTER CSS
# Reusable across all converter pages — paste CONV_CSS verbatim
# and change only masthead content, presets, conversion logic,
# and nav links. No CSS changes needed between languages.
# ============================================================
CONV_CSS = """
<style>
.conv-masthead {
    border-top: 3px solid var(--ink);
    border-bottom: 1px solid var(--rule);
    padding: 1.75rem 0 1.4rem 0;
    margin-bottom: 1.75rem;
}
.conv-masthead-eyebrow {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.68rem; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.18em;
    color: var(--accent);
    display: flex; align-items: center; gap: 0.65rem;
    margin-bottom: 0.65rem;
}
.conv-masthead-eyebrow::before {
    content: ''; display: inline-block;
    width: 1.75rem; height: 1.5px;
    background: var(--accent); flex-shrink: 0;
}
.conv-masthead-title {
    font-family: 'Crimson Pro', Georgia, serif;
    font-size: 3rem; font-weight: 700;
    color: var(--ink); letter-spacing: -0.04em;
    line-height: 1.05; margin-bottom: 0.5rem;
}
.conv-masthead-desc {
    font-family: 'Crimson Pro', Georgia, serif;
    font-style: italic; font-size: 1.1rem;
    color: var(--ink-muted); line-height: 1.55;
    margin-bottom: 0;
}
.conv-section-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.72rem; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.16em;
    color: var(--ink-soft);
    display: flex; align-items: center; gap: 1rem;
    margin: 2rem 0 1rem 0;
}
.conv-section-label::before {
    content: ''; display: inline-block;
    width: 2rem; height: 1px;
    background: var(--ink-muted); flex-shrink: 0;
}
.conv-section-label::after {
    content: ''; flex: 1; height: 1px; background: var(--rule);
}
.conv-presets-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.68rem; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.14em;
    color: var(--ink-faint);
    margin-bottom: 0.65rem; margin-top: 0;
}
.conv-input-title {
    font-family: 'Crimson Pro', Georgia, serif;
    font-size: 1.25rem; font-weight: 600;
    color: var(--ink); letter-spacing: -0.02em;
    margin: 0 0 0.3rem 0; line-height: 1.2;
}
.conv-input-hint {
    font-family: 'Crimson Pro', Georgia, serif;
    font-style: italic; font-size: 0.95rem;
    color: var(--ink-faint); margin: 0 0 0.85rem 0;
    line-height: 1.4;
}
.conv-result-card {
    background: rgba(46,107,122,0.04);
    border: 1px solid rgba(46,107,122,0.18);
    border-left: 3px solid var(--teal);
    border-radius: 0 4px 4px 0;
    padding: 0.75rem 1.1rem;
    margin-top: 0.8rem;
}
.conv-result-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.6rem; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.14em;
    color: var(--teal); margin-bottom: 0.3rem;
}
.conv-result-value {
    font-family: 'Crimson Pro', Georgia, serif;
    font-size: 1.05rem; font-weight: 400;
    color: var(--ink); line-height: 1.55;
    word-break: break-word;
}
.conv-error-card {
    background: rgba(184,92,56,0.05);
    border: 1px solid rgba(184,92,56,0.2);
    border-left: 3px solid var(--accent);
    border-radius: 0 4px 4px 0;
    padding: 0.75rem 1.1rem;
    margin-top: 0.8rem;
}
.conv-error-text {
    font-family: 'Crimson Pro', Georgia, serif;
    font-size: 1rem; color: var(--accent);
    font-style: italic; margin: 0;
}
.conv-nav-footer {
    display: flex; gap: 0.75rem;
    padding: 1.4rem 0 0.5rem 0;
    border-top: 1px solid var(--rule);
    margin-top: 2.5rem; flex-wrap: wrap;
}
.conv-nav-btn {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.78rem; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.09em;
    color: var(--ink); background: var(--parchment-2);
    border: 1.5px solid var(--rule-strong); border-radius: 3px;
    padding: 0.55rem 1.1rem; text-decoration: none;
    display: inline-flex; align-items: center; gap: 0.4rem;
    white-space: nowrap; cursor: pointer;
    box-shadow: 2px 2px 0 rgba(26,22,18,0.08);
    transition: all 0.18s cubic-bezier(0.4,0,0.2,1);
}
.conv-nav-btn:hover {
    background: var(--ink); color: var(--parchment);
    border-color: var(--ink);
    box-shadow: 3px 3px 0 var(--accent);
    transform: translate(-1px,-1px); text-decoration: none;
}
.conv-nav-btn.active {
    background: var(--parchment-3); color: var(--ink-muted);
    cursor: default; box-shadow: none;
}
.conv-nav-btn.active:hover {
    transform: none; background: var(--parchment-3);
    color: var(--ink-muted); border-color: var(--rule-strong);
    box-shadow: none;
}
.conv-caption {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.75rem; color: var(--ink-faint);
    line-height: 1.55; margin-top: 1rem;
}
.conv-caption a {
    color: var(--accent) !important;
    text-decoration: underline !important;
    text-decoration-color: rgba(184,92,56,0.35) !important;
}
.conv-caption a:hover { text-decoration-color: var(--accent) !important; }
</style>
"""
st.markdown(CONV_CSS, unsafe_allow_html=True)


# ============================================================
# MASTHEAD
# ============================================================
st.markdown("""
<div class="conv-masthead">
    <div class="conv-masthead-eyebrow">Numeral Converter</div>
    <div class="conv-masthead-title">Basque (Batua)</div>
    <div class="conv-masthead-desc">
        Bidirectional conversion between Arabic numerals and standard Basque numerals.
        Implements vigesimal structure with lexical blocking and additive <em>eta</em>.
    </div>
</div>
""", unsafe_allow_html=True)


# ============================================================
# DIRECTION SELECTOR
# ============================================================
st.markdown('<div class="conv-section-label">Conversion Direction</div>', unsafe_allow_html=True)

direction = st.radio(
    "Choose conversion direction:",
    ["Arabic → Basque", "Basque → Arabic"],
    horizontal=True,
    label_visibility="collapsed",
)


# ============================================================
# PRESET EXAMPLES
# ============================================================
st.markdown('<div class="conv-section-label">Preset Examples</div>', unsafe_allow_html=True)

arabic_presets = [5, 12, 20, 25, 36, 100, 325, 1046]
basque_presets = [
    "bost", "hamabi", "hogei", "hogei eta bost",
    "hogei eta hamasei", "ehun", "hirurehun eta hogeita bost",
    "mila berrogei eta sei",
]

with st.container(border=True):
    st.markdown('<p class="conv-presets-label">Click a value to load it</p>', unsafe_allow_html=True)
    cols = st.columns(4)
    if direction == "Arabic → Basque":
        for i, num in enumerate(arabic_presets):
            if cols[i % 4].button(str(num), key=f"preset_a_{i}"):
                st.session_state["arabic_input"] = str(num)
    else:
        for i, txt in enumerate(basque_presets):
            if cols[i % 4].button(txt, key=f"preset_b_{i}"):
                st.session_state["basque_input"] = txt


# ============================================================
# INPUT & CONVERSION
# ============================================================
st.markdown('<div class="conv-section-label">Convert</div>', unsafe_allow_html=True)

if direction == "Arabic → Basque":
    with st.container(border=True):
        st.markdown('<p class="conv-input-title">Enter an Arabic numeral</p>', unsafe_allow_html=True)
        st.markdown('<p class="conv-input-hint">Type a whole number, or click a preset above.</p>', unsafe_allow_html=True)
        arabic_input = st.text_input(
            "Arabic numeral",
            key="arabic_input",
            placeholder="e.g. 325",
            label_visibility="collapsed",
        )
        if arabic_input:
            if arabic_input.lstrip("-").isdigit():
                try:
                    result = number_to_basque(int(arabic_input))
                    st.markdown(f"""
                    <div class="conv-result-card">
                        <div class="conv-result-label">Basque (Batua)</div>
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
    with st.container(border=True):
        st.markdown('<p class="conv-input-title">Enter a Basque numeral</p>', unsafe_allow_html=True)
        st.markdown('<p class="conv-input-hint">Standard Batua orthography, e.g. <em>hogei eta bost</em>.</p>', unsafe_allow_html=True)
        basque_input = st.text_input(
            "Basque numeral",
            key="basque_input",
            placeholder="e.g. hogei eta bost",
            label_visibility="collapsed",
        )
        if basque_input:
            try:
                result = basque_to_number(basque_input)
                st.markdown(f"""
                <div class="conv-result-card">
                    <div class="conv-result-label">Arabic numeral</div>
                    <div class="conv-result-value">{result}</div>
                </div>
                """, unsafe_allow_html=True)
            except Exception as e:
                st.markdown(f'<div class="conv-error-card"><p class="conv-error-text">{e}</p></div>',
                            unsafe_allow_html=True)


# ============================================================
# CAPTION & NAVIGATION
# ============================================================
st.markdown("""
<div class="conv-caption">
    Implements standard Batua vigesimal structure with lexical blocking.
    Source data from <a href="https://www.omniglot.com/language/numbers/basque.html" target="_blank">Omniglot</a>.
    Converter algorithm by Yi Zou. Grammar detail in the Linguistics section.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="conv-nav-footer">
    <a class="conv-nav-btn active" href="/Basque_Converter">Basque Converter</a>
    <a class="conv-nav-btn" href="/Basque_Linguistics">Basque Linguistics →</a>
</div>
""", unsafe_allow_html=True)