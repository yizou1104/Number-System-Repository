import streamlit as st
from ui import apply_global_styles, home_nav

# ============================================================
# BASQUE NUMERAL GENERATOR & PARSER (BATUA)
# ============================================================

ATOMS = {
    0: "zero",  1: "bat",    2: "bi",       3: "hiru",
    4: "lau",   5: "bost",   6: "sei",      7: "zazpi",
    8: "zortzi",9: "bederatzi", 10: "hamar",
    11: "hamaika",   12: "hamabi",    13: "hamahiru",
    14: "hamalau",   15: "hamabost",  16: "hamasei",
    17: "hamazazpi", 18: "hemezortzi",19: "hemeretzi",
}

TWENTIES_MAP = {1: "hogei", 2: "berrogei", 3: "hirurogei", 4: "laurogei"}

HUNDREDS_MAP = {
    1: "ehun",      2: "berrehun",   3: "hirurehun",
    4: "laurehun",  5: "bostehun",   6: "seiehun",
    7: "zazpiehun", 8: "zortziehun", 9: "bederatziehun",
}

THOUSAND = "mila"

def additive(x, y):
    return f"{x} eta {y}"

def multiplicative(x, base):
    return f"{x} {base}"

def number_to_basque(n):
    if n < 0:
        raise ValueError("Negative numbers are not supported")
    if n in ATOMS:
        return ATOMS[n]
    if n >= 1000:
        thousands, remainder = n // 1000, n % 1000
        head = THOUSAND if thousands == 1 else multiplicative(number_to_basque(thousands), THOUSAND)
        return head if remainder == 0 else additive(head, number_to_basque(remainder))
    if n >= 100:
        hundreds, remainder = n // 100, n % 100
        head = HUNDREDS_MAP[hundreds]
        return head if remainder == 0 else additive(head, number_to_basque(remainder))
    if n >= 20:
        twenties, remainder = n // 20, n % 20
        head = TWENTIES_MAP[twenties]
        return head if remainder == 0 else additive(head, number_to_basque(remainder))
    raise RuntimeError(f"Unexpected number: {n}")

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
    for word in set(HUNDREDS_MAP.values()):
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
# PAGE CONFIG & STYLES
# ============================================================
st.set_page_config(page_title="Basque Numeral Converter", layout="centered")
apply_global_styles()

# ============================================================
# CONVERTER CSS
# Template for all converter pages — copy CONV_CSS verbatim,
# change only masthead content, presets, logic, and nav links.
# ============================================================
CONV_CSS = """
<style>
/* ── MASTHEAD ──────────────────────────────────────────────── */
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
    font-style: italic; font-size: 1.05rem;
    color: var(--ink-muted); line-height: 1.55; margin: 0;
}

/* ── SECTION LABEL ─────────────────────────────────────────── */
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


/* Style the Streamlit radio to look like a toggle card */
div[data-testid="stRadio"] > div {
    display: flex;
    gap: 0;
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 6px;
    padding: 0.35rem;
    box-shadow: 0 1px 3px rgba(26,22,18,0.05),
                0 4px 14px rgba(26,22,18,0.04),
                inset 0 1px 0 rgba(255,255,255,0.65);
    width: fit-content;
}
/* Each radio option label */
div[data-testid="stRadio"] label {
    display: flex !important;
    align-items: center !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.9rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.02em !important;
    text-transform: none !important;
    color: var(--ink-soft) !important;
    background: transparent !important;
    border: 1.5px solid transparent !important;
    border-radius: 4px !important;
    padding: 0.55rem 1.35rem !important;
    cursor: pointer !important;
    transition: all 0.18s cubic-bezier(0.4, 0, 0.2, 1) !important;
    white-space: nowrap !important;
}
/* Hide the radio dot — target the BaseWeb radio indicator span */
div[data-testid="stRadio"] label > span:first-child {
    display: none !important;
}
/* Hover state */
div[data-testid="stRadio"] label:hover {
    background: var(--parchment-3) !important;
    border-color: var(--rule-strong) !important;
    color: var(--ink) !important;
}
/* Selected state — label containing a checked input */
div[data-testid="stRadio"] label:has(input:checked) {
    background: var(--ink) !important;
    border-color: var(--ink) !important;
    box-shadow: 3px 3px 0 var(--accent) !important;
    transform: translate(-1px, -1px) !important;
}
/* Text colour inside selected label — must override explicitly */
div[data-testid="stRadio"] label:has(input:checked) p,
div[data-testid="stRadio"] label:has(input:checked) span {
    color: var(--parchment) !important;
}
/* Paragraph inside each label */
div[data-testid="stRadio"] label p {
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.9rem !important;
    font-weight: 600 !important;
    margin: 0 !important;
    line-height: 1 !important;
}

/* ── PRESET SUBLABEL ───────────────────────────────────────── */
.conv-presets-sublabel {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.65rem; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.14em;
    color: var(--ink-faint); margin-bottom: 0.65rem; margin-top: 0;
}

/* ── INPUT CARD ────────────────────────────────────────────── */
.conv-input-card {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 6px;
    padding: 1.3rem 1.5rem 1.4rem;
    margin-bottom: 0.5rem;
    box-shadow: 0 1px 3px rgba(26,22,18,0.05),
                0 6px 20px rgba(26,22,18,0.06),
                inset 0 1px 0 rgba(255,255,255,0.7);
}
.conv-input-title {
    font-family: 'Crimson Pro', Georgia, serif;
    font-size: 1.3rem; font-weight: 600;
    color: var(--ink); letter-spacing: -0.02em;
    margin: 0 0 0.25rem 0; line-height: 1.2;
}
.conv-input-hint {
    font-family: 'Crimson Pro', Georgia, serif;
    font-style: italic; font-size: 0.93rem;
    color: var(--ink-faint); margin: 0 0 0.8rem 0;
    line-height: 1.4;
}

/* ── RESULT CARD ───────────────────────────────────────────── */
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

/* ── ERROR CARD ────────────────────────────────────────────── */
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

/* ── NAV FOOTER ────────────────────────────────────────────── */
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

/* ── CAPTION ───────────────────────────────────────────────── */
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
        Bidirectional conversion between Arabic numerals and standard Basque
        numerals. Implements vigesimal structure with lexical blocking and
        additive <em>eta</em>.
    </div>
</div>
""", unsafe_allow_html=True)


# ============================================================
# DIRECTION SELECTOR
# The st.radio drives all logic. CSS hides the native widget
# but keeps it interactive. The HTML card below re-renders
# the state visually on every rerun.
# ============================================================
st.markdown('<div class="conv-section-label">Conversion Direction</div>', unsafe_allow_html=True)

direction = st.radio(
    "Conversion direction",
    ["Arabic → Basque", "Basque → Arabic"],
    horizontal=True,
    label_visibility="collapsed",
    key="basque_direction",
)


# ============================================================
# PRESET EXAMPLES
# Flex-wrap grid: buttons auto-wrap, widths fit their labels,
# spacing stays consistent regardless of label length.
# ============================================================
st.markdown('<div class="conv-section-label">Preset Examples</div>', unsafe_allow_html=True)

arabic_presets  = [5, 12, 20, 25, 36, 100, 325, 1046]
basque_presets  = [
    "bost", "hamabi", "hogei", "hogei eta bost",
    "hogei eta hamasei", "ehun",
    "hirurehun eta hogeita bost", "mila berrogei eta sei",
]

with st.container(border=True):
    st.markdown('<p class="conv-presets-sublabel">Click a value to load it</p>', unsafe_allow_html=True)
    cols = st.columns(4)
    if direction == "Arabic → Basque":
        for i, num in enumerate(arabic_presets):
            if cols[i % 4].button(str(num), key=f"p_a_{i}", use_container_width=True):
                st.session_state["arabic_input"] = str(num)
    else:
        for i, txt in enumerate(basque_presets):
            if cols[i % 4].button(txt, key=f"p_b_{i}", use_container_width=True):
                st.session_state["basque_input"] = txt


# ============================================================
# INPUT & CONVERSION
# ============================================================
st.markdown('<div class="conv-section-label">Convert</div>', unsafe_allow_html=True)

if direction == "Arabic → Basque":
    st.markdown("""
    <div class="conv-input-card">
        <div class="conv-input-title">Enter an Arabic numeral</div>
        <div class="conv-input-hint">Type a whole number, or click a preset above to load it automatically.</div>
    </div>
    """, unsafe_allow_html=True)
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
    st.markdown("""
    <div class="conv-input-card">
        <div class="conv-input-title">Enter a Basque numeral</div>
        <div class="conv-input-hint">Standard Batua orthography, e.g. <em>hogei eta bost</em>. Click a preset above to load an example.</div>
    </div>
    """, unsafe_allow_html=True)
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
    Source data from
    <a href="https://www.omniglot.com/language/numbers/basque.html" target="_blank">Omniglot</a>.
    Converter algorithm by Yi Zou. Grammar detail in the Linguistics section.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="conv-nav-footer">
    <a class="conv-nav-btn active" href="/Basque_Converter">Basque Converter</a>
    <a class="conv-nav-btn" href="/Basque_Linguistics">Basque Linguistics →</a>
</div>
""", unsafe_allow_html=True)
home_nav()