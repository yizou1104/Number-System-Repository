import streamlit as st

# ============================================================
# THAI NUMERAL SYSTEM
# Bidirectional: Arabic ↔ Thai
# ============================================================

# ------------------------------------------------------------
# 1. ATOMIC DIGITS
# ------------------------------------------------------------
THAI_DIGITS = {
    0: "ศูนย์",
    1: "หนึ่ง",
    2: "สอง",
    3: "สาม",
    4: "สี่",
    5: "ห้า",
    6: "หก",
    7: "เจ็ด",
    8: "แปด",
    9: "เก้า",
}

THAI_VALUES = {
    "ศูนย์": 0,
    "หนึ่ง": 1,
    "เอ็ด": 1,
    "สอง": 2,
    "ยี่": 2,
    "สาม": 3,
    "สี่": 4,
    "ห้า": 5,
    "หก": 6,
    "เจ็ด": 7,
    "แปด": 8,
    "เก้า": 9,
}

# ------------------------------------------------------------
# 2. UNITS
# ------------------------------------------------------------
THAI_UNITS = [
    (10**6, "ล้าน"),
    (10**5, "แสน"),
    (10**4, "หมื่น"),
    (10**3, "พัน"),
    (10**2, "ร้อย"),
    (10,    "สิบ"),
]

UNIT_VALUES = {
    "สิบ": 10,
    "ร้อย": 100,
    "พัน": 1000,
    "หมื่น": 10000,
    "แสน": 100000,
    "ล้าน": 1000000,
}

# ------------------------------------------------------------
# 3. ARABIC → THAI
# ------------------------------------------------------------
def number_to_thai(n: int) -> str:
    if n < 0:
        raise ValueError("Negative numbers not supported")

    if n == 0:
        return THAI_DIGITS[0]

    result = ""

    for value, unit in THAI_UNITS:
        digit = n // value
        n %= value

        if digit == 0:
            continue

        if value == 10:
            if digit == 1:
                result += "สิบ"
            elif digit == 2:
                result += "ยี่สิบ"
            else:
                result += THAI_DIGITS[digit] + "สิบ"
        else:
            if digit == 1:
                result += unit
            else:
                result += THAI_DIGITS[digit] + unit

    if n > 0:
        if n == 1 and result != "":
            result += "เอ็ด"
        else:
            result += THAI_DIGITS[n]

    return result

# ------------------------------------------------------------
# 4. THAI → ARABIC
# ------------------------------------------------------------
def thai_to_number(text: str) -> int:
    total = 0
    current = 0
    i = 0

    while i < len(text):
        matched = False

        for unit, value in UNIT_VALUES.items():
            if text.startswith(unit, i):
                if current == 0:
                    current = 1
                current *= value
                total += current
                current = 0
                i += len(unit)
                matched = True
                break

        if matched:
            continue

        for word, value in THAI_VALUES.items():
            if text.startswith(word, i):
                current += value
                i += len(word)
                matched = True
                break

        if not matched:
            raise ValueError("Invalid Thai numeral format")

    return total + current

# ============================================================
# STREAMLIT UI
# ============================================================

st.set_page_config(
    page_title="Thai Numeral Converter",
    layout="centered"
)

st.title("Thai Numeral Converter")

st.write(
    "Convert between **Arabic numerals** and **Thai numerals** "
    "using standard modern Thai conventions."
)

st.markdown("---")

# ------------------------------------------------------------
# Direction selector
# ------------------------------------------------------------
direction = st.radio(
    "Choose conversion direction:",
    ["Arabic → Thai", "Thai → Arabic"],
    horizontal=True
)

st.markdown("---")

# ------------------------------------------------------------
# Preset examples
# ------------------------------------------------------------
st.subheader("Preset Examples")

arabic_presets = [
    0, 5, 11, 19,
    20, 21, 45,
    100, 256, 999,
    1000, 2024
]

thai_presets = [
    "ศูนย์",
    "ห้า",
    "สิบเอ็ด",
    "ยี่สิบเอ็ด",
    "สี่สิบห้า",
    "สองร้อยห้าสิบหก",
    "เก้าร้อยเก้าสิบเก้า",
    "พัน",
    "สองพันยี่สิบสี่",
]

cols = st.columns(4)

if direction == "Arabic → Thai":
    for i, n in enumerate(arabic_presets):
        if cols[i % 4].button(str(n)):
            st.session_state["arabic_input"] = str(n)
else:
    for i, t in enumerate(thai_presets):
        if cols[i % 4].button(t):
            st.session_state["thai_input"] = t

st.markdown("---")

# ------------------------------------------------------------
# Input & output
# ------------------------------------------------------------
if direction == "Arabic → Thai":
    arabic_input = st.text_input(
        "Enter an Arabic numeral:",
        key="arabic_input",
        placeholder="e.g. 256"
    )

    if arabic_input:
        if arabic_input.isdigit():
            try:
                result = number_to_thai(int(arabic_input))
                st.success(result)
            except Exception:
                st.error("Number too large or unsupported.")
        else:
            st.error("Please enter a valid integer.")

else:
    thai_input = st.text_input(
        "Enter a Thai numeral:",
        key="thai_input",
        placeholder="e.g. สองร้อยห้าสิบหก"
    )

    if thai_input:
        try:
            result = thai_to_number(thai_input)
            st.success(str(result))
        except Exception:
            st.error("Invalid Thai numeral format.")

st.markdown("---")
st.caption(
    "Implements a rule-based Thai numeral system. "
    "Irregular forms such as ยี่ (20s) and เอ็ด (final 1) "
    "are handled explicitly. Converter created by Yi Zou. Further discussion appears "
    "in the Linguistics section."
)

# ------------------------------------------------------------
# Related Pages Navigation
# ------------------------------------------------------------
st.markdown("---")
st.subheader("Explore More")

nav_cols = st.columns(3)

with nav_cols[0]:
    st.page_link(
        "pages/Thai_Linguistics.py",
        label="Linguistics",
        help="Grammar, irregularities, and structure of Thai numerals"
    )

with nav_cols[1]:
    st.page_link(
        "pages/Thai_Olympiad_Problems.py",
        label="Olympiad Problems",
        help="Competition-style problems involving Thai numerals"
    )

with nav_cols[2]:
    st.page_link(
        "pages/Thai_Converter.py",
        label="Converter",
        help="Return to the numeral converter"
    )