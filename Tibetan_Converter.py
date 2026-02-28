import streamlit as st

# ============================================================
# TIBETAN NUMERAL SYSTEM
# Arabic → Tibetan (script + romanisation)
# ============================================================

# ------------------------------------------------------------
# 1. ATOMS (0–9)
# ------------------------------------------------------------
ATOMS = {
    0: ("ཀླད་ཀོར་", "laykor"),
    1: ("གཅིག་", "chig"),
    2: ("གཉིས་", "nyi"),
    3: ("གསུམ་", "sum"),
    4: ("བཞི་", "shi"),
    5: ("ལྔ་", "nga"),
    6: ("དྲུག་", "trug"),
    7: ("བདུན་", "dün"),
    8: ("བརྒྱད་", "gyay"),
    9: ("དགུ་", "gu"),
}

# ------------------------------------------------------------
# 2. TEENS (10–19)
# ------------------------------------------------------------
TEENS = {
    10: ("བཅུ་", "chu"),
    11: ("བཅུ་གཅིག་", "chu chig"),
    12: ("བཅུ་གཉིས་", "chu nyi"),
    13: ("བཅུ་གསུམ་", "chu sum"),
    14: ("བཅུ་བཞི་", "chu shi"),
    15: ("བཅོ་ལྔ་", "cho nga"),
    16: ("བཅུ་དྲུག་", "chu trug"),
    17: ("བཅུ་བདུན་", "chu dün"),
    18: ("བཅོ་བརྒྱད་", "cho gyay"),
    19: ("བཅུ་དགུ་", "chu gu"),
}

# ------------------------------------------------------------
# 3. DECADES (20–90) + LINKERS
# ------------------------------------------------------------
DECADES = {
    20: ("ཉི་ཤུ་", "nyi shu"),
    30: ("སུམ་ཅུ", "sum ju"),
    40: ("བཞི་བཅུ", "shi ju"),
    50: ("ལྔ་བཅུ", "nga ju"),
    60: ("དྲུག་ཅུ", "trug chu"),
    70: ("བདུན་ཅུ", "dün ju"),
    80: ("བརྒྱད་ཅུ", "gyay ju"),
    90: ("དགུ་བཅུ", "gu ju"),
}

DECADE_LINKERS = {
    20: ("རྩ་", "tsa"),
    30: ("སོ་", "so"),
    40: ("ཞེ་", "shey"),
    50: ("ང་", "nga"),
    60: ("རེ་", "rey"),
    70: ("དོན་", "dön"),
    80: ("གྱ་", "gya"),
    90: ("གོ་", "go"),
}

# ------------------------------------------------------------
# 4. MAGNITUDES
# ------------------------------------------------------------
MAGNITUDES = [
    (10**12, ("ཁྲག་ཁྲིག་ཆེན་པོ་", "thrag trig chen po")),
    (10**11, ("ཁྲག་ཁྲིག་", "thrag trig")),
    (10**10, ("ཐེར་འབུམ་ཆེན་པོ་", "ther pum chen po")),
    (10**9,  ("ཐེར་འབུམ་", "ther pum")),
    (10**8,  ("དུང་ཕྱུར་", "dung chur")),
    (10**7,  ("བྱེ་བ་", "che wa")),
    (10**6,  ("ས་ཡ་", "sa ya")),
    (10**4,  ("ཁྲི་", "thri")),
    (10**3,  ("སྟོང་", "tong")),
    (100,    ("བརྒྱ་", "gya")),
]

# ------------------------------------------------------------
# 5. ARABIC → TIBETAN
# ------------------------------------------------------------
def number_to_tibetan(n):
    if n < 0:
        raise ValueError("Negative numbers not supported")

    if n in ATOMS:
        return ATOMS[n]

    if n in TEENS:
        return TEENS[n]

    if n in DECADES:
        return DECADES[n]

    if n < 100:
        decade = (n // 10) * 10
        unit = n % 10
        d_word, d_rom = DECADES[decade]
        l_word, l_rom = DECADE_LINKERS[decade]
        u_word, u_rom = ATOMS[unit]
        return (
            f"{d_word}{l_word}{u_word}",
            f"{d_rom} {l_rom} {u_rom}"
        )

    for value, (mag_word, mag_rom) in MAGNITUDES:
        if n >= value:
            multiplier = n // value
            remainder = n % value

            if multiplier == 1:
                head_word, head_rom = mag_word, mag_rom
            else:
                m_word, m_rom = number_to_tibetan(multiplier)
                head_word = f"{m_word}{mag_word}"
                head_rom = f"{m_rom} {mag_rom}"

            if remainder == 0:
                return head_word, head_rom

            r_word, r_rom = number_to_tibetan(remainder)
            return (
                f"{head_word}དང་{r_word}",
                f"{head_rom} dang {r_rom}"
            )

# ============================================================
# STREAMLIT UI
# ============================================================

st.set_page_config(page_title="Tibetan Numeral Converter", layout="centered")

st.title("Tibetan Numeral Converter")

st.write(
    "Convert **Arabic numerals** into **Tibetan numerals**, "
    "showing both Tibetan script and standard romanisation."
)

st.markdown("---")

# ------------------------------------------------------------
# Presets
# ------------------------------------------------------------
st.subheader("Preset Examples")

arabic_presets = [3, 10, 21, 45, 108, 256, 1000, 4032]
cols = st.columns(4)

for i, n in enumerate(arabic_presets):
    if cols[i % 4].button(str(n)):
        st.session_state["arabic_input"] = str(n)

st.markdown("---")

# ------------------------------------------------------------
# Input & output
# ------------------------------------------------------------
arabic_input = st.text_input(
    "Enter an Arabic numeral:",
    key="arabic_input",
    placeholder="e.g. 256"
)

if arabic_input:
    if arabic_input.isdigit():
        tib, rom = number_to_tibetan(int(arabic_input))
        st.success(f"{tib}  ({rom})")
    else:
        st.error("Please enter a valid non-negative integer.")

st.markdown("---")
st.caption(
    "Implements the Tibetan numeral system. "
    "Source data retrieved from Omniglot at https://www.omniglot.com/language/numbers/tibetan.htm. "
    "Converter algorithm created by Yi Zou. "
    "Grammar explained in the Linguistics section."
)

# --------------------------------------------------
# Related Pages Navigation
# --------------------------------------------------
st.markdown("---")
st.subheader("Explore More")

nav_cols = st.columns(3)

with nav_cols[0]:
    st.page_link(
        "pages/Tibetan_Linguistics.py",
        label="Linguistics",
        help="Structure, grammar, and historical development of the numeral system"
    )

with nav_cols[1]:
    st.page_link(
        "pages/Tibetan_Olympiad_Problems.py",
        label="Olympiad Problems",
        help="Competition-style problems involving Tibetan numerals"
    )

with nav_cols[2]:
    st.page_link(
        "pages/Tibetan_Converter.py",
        label="Converter",
        help="Return to the numeral converter"
    )