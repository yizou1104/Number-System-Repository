import streamlit as st
from ui import apply_global_styles
from tarakimu import num_to_words

try:
    from tarakimu.utils import words_to_num
    HAS_REVERSE = True
except ImportError:
    HAS_REVERSE = False


# ============================================================
# SWAHILI NUMERAL CONVERTER (BIDIRECTIONAL)
# ============================================================

st.set_page_config(
    page_title="Swahili Numeral Converter",
    layout="centered"
)

apply_global_styles()


# --------------------------------------------------
# Title
# --------------------------------------------------
st.title("Swahili Numeral Converter")

st.write(
    "Convert between **Arabic numerals** and **standard Swahili numerals** "
    "(Kiswahili Sanifu)."
)

st.markdown("---")

# --------------------------------------------------
# Direction selector
# --------------------------------------------------
direction = st.radio(
    "Choose conversion direction:",
    ["Arabic → Swahili", "Swahili → Arabic"],
    horizontal=True,
    disabled=not HAS_REVERSE
)

if not HAS_REVERSE:
    st.info(
        "Reverse parsing (Swahili → Arabic) is limited and depends on the "
        "`tarakimu` version. Arabic → Swahili is fully supported."
    )

st.markdown("---")

# --------------------------------------------------
# Preset examples
# --------------------------------------------------
st.subheader("Preset Examples")

arabic_presets = [
    0, 5, 11, 19,
    20, 25, 47,
    100, 256, 999,
    1000, 2024
]

swahili_presets = [
    "sifuri",
    "tano",
    "kumi na moja",
    "ishirini na tano",
    "mia mbili hamsini na sita",
    "elfu moja",
]

cols = st.columns(4)

if direction == "Arabic → Swahili":
    for i, n in enumerate(arabic_presets):
        if cols[i % 4].button(str(n)):
            st.session_state["arabic_input"] = str(n)
else:
    for i, w in enumerate(swahili_presets):
        if cols[i % 4].button(w):
            st.session_state["swahili_input"] = w

st.markdown("---")

# --------------------------------------------------
# Input & output
# --------------------------------------------------
if direction == "Arabic → Swahili":
    arabic_input = st.text_input(
        "Enter an Arabic numeral:",
        key="arabic_input",
        placeholder="e.g. 256"
    )

    if arabic_input:
        if arabic_input.isdigit():
            try:
                value = int(arabic_input)
                st.success(num_to_words(value))
            except Exception:
                st.error("Number too large or unsupported.")
        else:
            st.error("Please enter a valid integer.")

else:
    swahili_input = st.text_input(
        "Enter a Swahili numeral:",
        key="swahili_input",
        placeholder="e.g. mia mbili hamsini na sita"
    )

    if swahili_input:
        try:
            result = words_to_num(swahili_input)
            st.success(str(result))
        except Exception:
            st.error("Invalid or unsupported Swahili numeral format.")

st.markdown("---")
st.caption(
    "Uses the tarakimu library for Swahili numeral generation. "
    "Noun-class agreement and dialectal variation are discussed "
    "in the Linguistics section."
)

# --------------------------------------------------
# Related Pages Navigation
# --------------------------------------------------
st.markdown("---")
st.subheader("Explore More")

nav_cols = st.columns(2)

with nav_cols[0]:
    st.page_link(
        "pages/Swahili_Linguistics.py",
        label="Linguistics",
        help="Structure, grammar, and historical development of the Swahili numeral system"
    )

with nav_cols[1]:
    st.page_link(
        "pages/Swahili_Converter.py",
        label="Converter",
        help="Return to the numeral converter"
    )
