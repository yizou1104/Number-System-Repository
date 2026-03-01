import streamlit as st
from cn2an import cn2an, an2cn

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(
    page_title="Chinese Numeral Converter",
    layout="centered"
)

# --------------------------------------------------
# Title
# --------------------------------------------------
st.title("Chinese Numeral Converter")

st.write(
    "Convert between **Chinese numerals** and **Arabic numerals** "
    "using standard modern Mandarin conventions."
)

st.markdown("---")

# --------------------------------------------------
# Conversion direction selector
# --------------------------------------------------
direction = st.radio(
    "Choose conversion direction:",
    ["Chinese → Arabic", "Arabic → Chinese"],
    horizontal=True
)

st.write("")

# --------------------------------------------------
# Preset examples (dynamic)
# --------------------------------------------------
st.subheader("Preset Examples")

chinese_presets = [
    "三", "十", "十五", "三十六",
    "一百二十三", "三百二十五",
    "一千零八", "四万零三十"
]

arabic_presets = [
    3, 10, 15, 36,
    123, 325,
    1008, 40030
]

cols = st.columns(4)

if direction == "Chinese → Arabic":
    for i, cn in enumerate(chinese_presets):
        if cols[i % 4].button(cn):
            st.session_state["chinese_input"] = cn

else:
    for i, num in enumerate(arabic_presets):
        if cols[i % 4].button(str(num)):
            st.session_state["arabic_input"] = str(num)

st.markdown("---")

# --------------------------------------------------
# Input & conversion
# --------------------------------------------------
if direction == "Chinese → Arabic":
    chinese_input = st.text_input(
        "Enter a Chinese numeral:",
        key="chinese_input",
        placeholder="e.g. 三百二十五"
    )

    if chinese_input:
        try:
            result = cn2an(chinese_input)
            st.success(f"**Arabic numeral:** {result}")
        except Exception:
            st.error("Invalid Chinese numeral format.")

else:
    arabic_input = st.text_input(
        "Enter an Arabic numeral:",
        key="arabic_input",
        placeholder="e.g. 403892"
    )

    if arabic_input:
        if arabic_input.isdigit():
            try:
                result = an2cn(int(arabic_input))
                st.success(f"**Chinese numeral:** {result}")
            except Exception:
                st.error("Number too large or unsupported.")
        else:
            st.error("Please enter a valid integer.")

# --------------------------------------------------
# Notes
# --------------------------------------------------
st.markdown("---")
st.caption(
    "Presets follow standard simplified Chinese numeral usage. "
    "Variants, financial numerals, and historical forms are discussed "
    "in the Linguistics section. "
    "Utilizes the cn2an library for conversions: https://github.com/Ailln/cn2an"
)

# --------------------------------------------------
# Related Pages Navigation
# --------------------------------------------------
st.markdown("---")
st.subheader("Explore More")

nav_cols = st.columns(3)

with nav_cols[0]:
    st.page_link(
        "pages/Chinese_Linguistics.py",
        label="Linguistics",
        help="Structure, grammar, and historical development of the numeral system"
    )

with nav_cols[1]:
    st.page_link(
        "pages/Olympiad_Problems.py",
        label="Olympiad Problems",
        help="Competition-style problems involving Chinese numerals"
    )

with nav_cols[2]:
    st.page_link(
        "pages/Chinese_Converter.py",
        label="Converter",
        help="Return to the numeral converter"
    )
