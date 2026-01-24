import streamlit as st

# ============================================================
# BASQUE NUMERAL SYSTEM (STANDARD BATUA)
# Bidirectional: Arabic ↔ Basque
# ============================================================


# ------------------------------------------------------------
# 1. ATOMIC NUMERALS (1–19)
# ------------------------------------------------------------
ATOMS = {
    0: "zero",
    1: "bat",
    2: "bi",
    3: "hiru",
    4: "lau",
    5: "bost",
    6: "sei",
    7: "zazpi",
    8: "zortzi",
    9: "bederatzi",
    10: "hamar",
    11: "hamaika",
    12: "hamabi",
    13: "hamahiru",
    14: "hamalau",
    15: "hamabost",
    16: "hamasei",
    17: "hamazazpi",
    18: "hemezortzi",
    19: "hemeretzi",
}

ATOM_VALUES = {v: k for k, v in ATOMS.items()}

# ------------------------------------------------------------
# 2. BASE UNITS
# ------------------------------------------------------------
BASE_20 = "hogei"
HUNDRED = "ehun"
THOUSAND = "mila"

# ------------------------------------------------------------
# 3. LEXICAL BLOCKING
# ------------------------------------------------------------
LEXICAL = {
    40: "berrogei",
    60: "hirurogei",
    80: "laurogei",
}

LEXICAL_VALUES = {
    "hogei": 20,
    "berrogei": 40,
    "hirurogei": 60,
    "laurogei": 80,
    "ehun": 100,
    "mila": 1000,
}

# ------------------------------------------------------------
# 4. MORPHOLOGICAL OPERATORS
# ------------------------------------------------------------
def additive(x, y):
    return f"{x} eta {y}"


def multiplicative(x, base):
    return f"{x} {base}"

# ------------------------------------------------------------
# 5. ARABIC → BASQUE
# ------------------------------------------------------------
def number_to_basque(n):
    if n < 0:
        raise ValueError("Negative numbers are not supported")

    if n in ATOMS:
        return ATOMS[n]

    if n in LEXICAL:
        return LEXICAL[n]

    if n >= 1000:
        thousands = n // 1000
        remainder = n % 1000
        head = THOUSAND if thousands == 1 else multiplicative(number_to_basque(thousands), THOUSAND)
        return head if remainder == 0 else f"{head} {number_to_basque(remainder)}"

    if n >= 100:
        hundreds = n // 100
        remainder = n % 100
        head = HUNDRED if hundreds == 1 else multiplicative(number_to_basque(hundreds), HUNDRED)
        return head if remainder == 0 else additive(head, number_to_basque(remainder))

    if n >= 20:
        twenties = n // 20
        remainder = n % 20
        head = BASE_20 if twenties == 1 else multiplicative(number_to_basque(twenties), BASE_20)
        return head if remainder == 0 else additive(head, number_to_basque(remainder))


# ------------------------------------------------------------
# 6. BASQUE → ARABIC
# ------------------------------------------------------------
def basque_to_number(text):
    tokens = text.strip().lower().split()

    if "eta" in tokens:
        idx = tokens.index("eta")
        return (
            basque_to_number(" ".join(tokens[:idx])) +
            basque_to_number(" ".join(tokens[idx + 1:]))
        )

    if "mila" in tokens:
        idx = tokens.index("mila")
        left = tokens[:idx]
        right = tokens[idx + 1:]
        multiplier = 1 if not left else basque_to_number(" ".join(left))
        value = multiplier * 1000
        return value if not right else value + basque_to_number(" ".join(right))

    if "ehun" in tokens:
        idx = tokens.index("ehun")
        left = tokens[:idx]
        right = tokens[idx + 1:]
        multiplier = 1 if not left else basque_to_number(" ".join(left))
        value = multiplier * 100
        return value if not right else value + basque_to_number(" ".join(right))

    if "hogei" in tokens:
        idx = tokens.index("hogei")
        left = tokens[:idx]
        right = tokens[idx + 1:]
        multiplier = 1 if not left else basque_to_number(" ".join(left))
        value = multiplier * 20
        return value if not right else value + basque_to_number(" ".join(right))

    if text in ATOM_VALUES:
        return ATOM_VALUES[text]

    if text in LEXICAL_VALUES:
        return LEXICAL_VALUES[text]

    raise ValueError("Invalid Basque numeral")

# ============================================================
# STREAMLIT INTERFACE
# ============================================================

st.set_page_config(
    page_title="Basque Numeral Converter",
    layout="centered"
)

st.title("Basque Numeral Converter")
st.write(
    "Convert between **Basque numerals (Batua)** and **Arabic numerals**, "
    "using a fully rule-based vigesimal grammar."
)

st.markdown("---")

# ------------------------------------------------------------
# Direction selector
# ------------------------------------------------------------
direction = st.radio(
    "Choose conversion direction:",
    ["Arabic → Basque", "Basque → Arabic"],
    horizontal=True
)

st.markdown("---")

# ------------------------------------------------------------
# Presets
# ------------------------------------------------------------
st.subheader("Preset Examples")

arabic_presets = [5, 12, 20, 25, 36, 100, 325, 1046]
basque_presets = [
    "bost",
    "hamabi",
    "hogei",
    "hogei eta bost",
    "hogei eta hamasei",
    "ehun",
    "hiru ehun eta hogei eta bost",
    "mila berrogei eta sei",
]

cols = st.columns(4)

if direction == "Arabic → Basque":
    for i, num in enumerate(arabic_presets):
        if cols[i % 4].button(str(num)):
            st.session_state["arabic_input"] = str(num)
else:
    for i, txt in enumerate(basque_presets):
        if cols[i % 4].button(txt):
            st.session_state["basque_input"] = txt

st.markdown("---")

# ------------------------------------------------------------
# Input & conversion
# ------------------------------------------------------------
if direction == "Arabic → Basque":
    arabic_input = st.text_input(
        "Enter an Arabic numeral:",
        key="arabic_input",
        placeholder="e.g. 325"
    )

    if arabic_input:
        if arabic_input.isdigit():
            try:
                st.success(number_to_basque(int(arabic_input)))
            except Exception as e:
                st.error(str(e))
        else:
            st.error("Please enter a valid integer.")

else:
    basque_input = st.text_input(
        "Enter a Basque numeral:",
        key="basque_input",
        placeholder="e.g. hogei eta bost"
    )

    if basque_input:
        try:
            st.success(str(basque_to_number(basque_input)))
        except Exception:
            st.error("Invalid Basque numeral.")

st.markdown("---")
st.caption(
    "Implements standard Batua vigesimal structure with lexical blocking. "
    "Source data retrieved from Omniglot at https://www.omniglot.com/language/numbers/basque.html. "
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
        "pages/Basque_Linguistics.py",
        label="Linguistics",
        help="Structure, grammar, and historical development of the numeral system"
    )

with nav_cols[1]:
    st.page_link(
        "pages/Basque_Olympiad_Problems.py",
        label="Olympiad Problems",
        help="Competition-style problems involving Basque numerals"
    )

with nav_cols[2]:
    st.page_link(
        "pages/Basque_Converter.py",
        label="Converter",
        help="Return to the numeral converter"
    )
