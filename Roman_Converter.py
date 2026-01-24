import streamlit as st
import unicodedata

# ============================================================
# ROMAN NUMERAL CONVERTER (BIDIRECTIONAL, WITH OVERLINES)
# ============================================================

OVERLINE = "\u0305"  # Unicode combining overline (×1000)

# ------------------------------------------------------------
# 1. BASE ROMAN DATA
# ------------------------------------------------------------
ROMAN_PAIRS = [
    (1000, "M"),
    (900,  "CM"),
    (500,  "D"),
    (400,  "CD"),
    (100,  "C"),
    (90,   "XC"),
    (50,   "L"),
    (40,   "XL"),
    (10,   "X"),
    (9,    "IX"),
    (5,    "V"),
    (4,    "IV"),
    (1,    "I"),
]

ROMAN_VALUES = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

# ------------------------------------------------------------
# 2. HELPERS
# ------------------------------------------------------------
def _int_to_roman_under_1000(n):
    result = []
    for value, symbol in ROMAN_PAIRS:
        while n >= value:
            result.append(symbol)
            n -= value
    return "".join(result)


def _apply_overline(s, level):
    for _ in range(level):
        s = "".join(ch + OVERLINE for ch in s)
    return s


# ------------------------------------------------------------
# 3. ARABIC → ROMAN
# ------------------------------------------------------------
def arabic_to_roman(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Roman numerals require a positive integer")

    parts = []
    level = 0

    while n > 0:
        chunk = n % 1000
        if chunk:
            roman_chunk = _int_to_roman_under_1000(chunk)
            roman_chunk = _apply_overline(roman_chunk, level)
            parts.append(roman_chunk)
        n //= 1000
        level += 1

    return "".join(reversed(parts))


# ------------------------------------------------------------
# 4. ROMAN → ARABIC
# ------------------------------------------------------------
def roman_to_arabic(s):
    if not s:
        raise ValueError("Empty input")

    s = s.upper()
    i = 0
    total = 0

    while i < len(s):
        ch = s[i]
        if ch not in ROMAN_VALUES:
            raise ValueError(f"Invalid Roman symbol: {ch}")

        value = ROMAN_VALUES[ch]

        # Count overlines
        j = i + 1
        overlines = 0
        while j < len(s) and s[j] == OVERLINE:
            overlines += 1
            j += 1

        value *= 1000 ** overlines

        # Subtractive lookahead
        if j < len(s) and s[j] in ROMAN_VALUES:
            next_value = ROMAN_VALUES[s[j]]
            k = j + 1
            next_overlines = 0
            while k < len(s) and s[k] == OVERLINE:
                next_overlines += 1
                k += 1

            next_value *= 1000 ** next_overlines

            if next_value > value:
                total += next_value - value
                i = k
                continue

        total += value
        i = j

    return total


# ============================================================
# STREAMLIT UI
# ============================================================

st.set_page_config(page_title="Roman Numeral Converter", layout="centered")

st.title("Roman Numeral Converter")

st.write(
    "Convert between **Roman numerals** and **Arabic numerals**, "
    "including extended notation using Unicode overlines (×1000)."
)

st.markdown("---")

# ------------------------------------------------------------
# Direction selector
# ------------------------------------------------------------
direction = st.radio(
    "Choose conversion direction:",
    ["Arabic → Roman", "Roman → Arabic"],
    horizontal=True
)

st.markdown("---")

# ------------------------------------------------------------
# Preset examples
# ------------------------------------------------------------
st.subheader("Preset Examples")

arabic_presets = [4, 9, 44, 99, 399, 944, 2024, 4032]
roman_presets = ["IV", "IX", "XLIV", "XCIX", "CCCXCIX", "CMXLIV", "MMXXIV"]

cols = st.columns(4)

if direction == "Arabic → Roman":
    for i, n in enumerate(arabic_presets):
        if cols[i % 4].button(str(n)):
            st.session_state["arabic_input"] = str(n)
else:
    for i, r in enumerate(roman_presets):
        if cols[i % 4].button(r):
            st.session_state["roman_input"] = r

st.markdown("---")

# ------------------------------------------------------------
# Input & output
# ------------------------------------------------------------
if direction == "Arabic → Roman":
    arabic_input = st.text_input(
        "Enter an Arabic numeral:",
        key="arabic_input",
        placeholder="e.g. 4032"
    )

    if arabic_input:
        if arabic_input.isdigit() and int(arabic_input) > 0:
            try:
                st.success(arabic_to_roman(int(arabic_input)))
            except Exception as e:
                st.error(str(e))
        else:
            st.error("Please enter a positive integer.")

else:
    roman_input = st.text_input(
        "Enter a Roman numeral:",
        key="roman_input",
        placeholder="e.g. MMXXIV"
    )

    if roman_input:
        try:
            st.success(str(roman_to_arabic(roman_input)))
        except Exception as e:
            st.error(str(e))

st.markdown("---")
st.caption(
    "Implements canonical Roman numeral rules, including subtractive notation "
    "and extended overline-based magnitudes."
)

# ------------------------------------------------------------
# Related Pages Navigation
# ------------------------------------------------------------
st.markdown("---")
st.subheader("Explore More")

nav_cols = st.columns(3)

with nav_cols[0]:
    st.page_link(
        "pages/Roman_Linguistics.py",
        label="Linguistics",
        help="Structure, historical development, and notation rules"
    )

with nav_cols[1]:
    st.page_link(
        "pages/Roman_Olympiad_Problems.py",
        label="Olympiad Problems",
        help="Competition-style problems involving Roman numerals"
    )

with nav_cols[2]:
    st.page_link(
        "pages/Roman_Converter.py",
        label="Converter",
        help="Return to the numeral converter"
    )