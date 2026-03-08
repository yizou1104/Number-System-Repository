import streamlit as st
from ui import apply_global_styles

# ============================================================
# TRADITIONAL YORUBA NUMERAL GENERATOR (FINAL)
# Arabic numeral → Yoruba numeral
#
# Implemented principles:
# - Lexical blocking (11–19, 110, 120, 200–900)
# - Mixed-base system (20–90)
# - Subtractive dominance
# - Additive thousands only
# - Bounded: 0–1999
# ============================================================


# ------------------------------------------------------------
# 1. ATOMIC NUMERALS (1–10)
# ------------------------------------------------------------
ATOMS = {
    1: "ọ̀kan",
    2: "èjì",
    3: "ẹ̀ta",
    4: "ẹ̀rin",
    5: "àrún",
    6: "ẹ̀fà",
    7: "èje",
    8: "ẹ̀jọ",
    9: "ẹ̀sán",
    10: "ẹ̀wá",
}


# ------------------------------------------------------------
# 2. SALIENT BASES (≤ 100)
# ------------------------------------------------------------
BASES = {
    20: "ogún",
    30: "ọgbọ̀n",
    40: "ogójì",
    50: "àádọ́ta",
    60: "ọgọ́ta",
    70: "àádọ́rin",
    80: "ọgọ́rin",
    90: "àádọ́rùn",
}

THOUSAND = "ẹgbẹ̀rún"


# ------------------------------------------------------------
# 3. LEXICAL BLOCKING
# ------------------------------------------------------------
LEXICAL = {
    # 11–19
    11: "ọ̀kanlá",
    12: "èjìlá",
    13: "ẹ̀talá",
    14: "ẹ̀rinlá",
    15: "ẹ́ẹdógún",
    16: "ẹẹ́rìndílógún",
    17: "eétàdílógún",
    18: "eéjìdílógún",
    19: "oókàndílógún",

    # Special decade–hundred forms
    110: "àádọ́fà",
    120: "ọgọ́fà",

    # Lexical hundreds
    200: "igba",
    300: "ọ̀ọ́dúrún",
    400: "irinwó",
    500: "ọ̀ọ́dẹ́gbẹ̀ta",
    600: "ẹgbẹ̀ta",
    700: "ọ̀ọ́dẹ́gbẹ̀rin",
    800: "ẹgbẹ̀rin",
    900: "ẹ̀ẹ́dẹ́gbẹ̀rún",
}


# ------------------------------------------------------------
# 4. MORPHOLOGICAL OPERATORS
# ------------------------------------------------------------
def additive(x, base):
    """x + base"""
    return f"{x} lélọ́ {base}"


def subtractive(x, base):
    """base − x"""
    return f"{x} dín lọ́ {base}"


# ------------------------------------------------------------
# 5. BASE SELECTION
# ------------------------------------------------------------
def select_base(n):
    """Select the largest culturally salient base < n"""
    return max(b for b in BASES if b < n)


# ------------------------------------------------------------
# 6. CORE GENERATOR
# ------------------------------------------------------------
def number_to_yoruba(n):
    """
    Convert a non-negative integer (0–1999)
    into traditional Yoruba numeral.
    """

    if n < 0 or n >= 2000:
        raise ValueError("Supported range is 0–1999")

    if n == 0:
        return "òdo"

    # ---- Thousands (additive only) ----
    if n >= 1000:
        remainder = n - 1000
        if remainder == 0:
            return THOUSAND
        return additive(number_to_yoruba(remainder), THOUSAND)

    # ---- Lexical blocking ----
    if n in LEXICAL:
        return LEXICAL[n]

    # ---- Atomic ----
    if n in ATOMS:
        return ATOMS[n]

    # ---- Base-relative composition ----
    base = select_base(n)
    remainder = n - base

    # Subtractive dominance
    if remainder <= base / 2:
        return additive(number_to_yoruba(remainder), BASES[base])
    else:
        higher_bases = [b for b in BASES if b > base]
        if not higher_bases:
            # No higher base exists → force additive composition
            return additive(number_to_yoruba(remainder), BASES[base])

        next_base = min(higher_bases)
        diff = next_base - n
        return subtractive(number_to_yoruba(diff), BASES[next_base])



# ============================================================
# STREAMLIT UI
# ============================================================

st.set_page_config(page_title="Yoruba Numeral Converter", layout="centered")

apply_global_styles()


st.title("Yoruba Numeral Converter")

st.write(
    "Convert **Arabic numerals** into **traditional Yoruba numerals**, "
    "using the classical subtractive–additive system."
)

st.markdown("---")

# ------------------------------------------------------------
# Preset examples
# ------------------------------------------------------------
st.subheader("Preset Examples")

presets = [
    1, 5, 11, 15, 19,
    20, 21, 29, 30, 35,
    40, 45, 59,
    100, 110, 120,
    256, 400, 999,
    1000, 1111, 1500
]

cols = st.columns(4)

for i, n in enumerate(presets):
    if cols[i % 4].button(str(n)):
        st.session_state["arabic_input"] = str(n)

st.markdown("---")

# ------------------------------------------------------------
# Input & output
# ------------------------------------------------------------
arabic_input = st.text_input(
    "Enter an Arabic numeral (0–1999):",
    key="arabic_input",
    placeholder="e.g. 256"
)

if arabic_input:
    if arabic_input.isdigit():
        try:
            yoruba = number_to_yoruba(int(arabic_input))
            st.success(yoruba)
        except ValueError as e:
            st.error(str(e))
    else:
        st.error("Please enter a valid integer.")

st.markdown("---")
st.caption(
    "Implements a traditional Yoruba numeral system with lexical blocking "
    "and subtractive dominance. Source data retrieved from https://www.mathsdesign.com/mathematics/numbers-in-different-languages/yoruba-numbers/ and https://www.nairaland.com/1286110/onka-yoruba-numbers-numbering-system. "
    "Converter algorithm created by Yi Zou."
)

# --------------------------------------------------
# Related Pages Navigation
# --------------------------------------------------
st.markdown("---")
st.subheader("Explore More")

nav_cols = st.columns(2)

with nav_cols[0]:
    st.page_link(
        "pages/Yoruba_Linguistics.py",
        label="Linguistics",
        help="Structure, grammar, and historical development of the Yoruba numeral system"
    )

with nav_cols[1]:
    st.page_link(
        "pages/Yoruba_Converter.py",
        label="Converter",
        help="Return to the numeral converter"
    )
