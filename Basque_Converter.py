import streamlit as st

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

# ------------------------------------------------------------
# 2. BASE UNITS AND FUSED FORMS
# ------------------------------------------------------------
BASE_20 = "hogei"

# Fused vigesimal bases (20, 40, 60, 80)
TWENTIES_MAP = {
    1: "hogei",
    2: "berrogei",
    3: "hirurogei",
    4: "laurogei",
}

# Fused hundreds (100, 200, ..., 900)
HUNDREDS_MAP = {
    1: "ehun",
    2: "berrehun",
    3: "hirurehun",
    4: "laurehun",
    5: "bostehun",
    6: "seiehun",
    7: "zazpiehun",
    8: "zortziehun",
    9: "bederatziehun",
}

THOUSAND = "mila"

# ------------------------------------------------------------
# 3. MORPHOLOGICAL OPERATORS
# ------------------------------------------------------------
def additive(x, y):
    """x + y (additive construction)"""
    return f"{x} eta {y}"

def multiplicative(x, base):
    """x × base (multiplicative construction)"""
    return f"{x} {base}"

# ------------------------------------------------------------
# 4. CORE GENERATOR (ARABIC → BASQUE)
# ------------------------------------------------------------
def number_to_basque(n):
    """
    Convert a non‑negative integer to standard Basque numeral (Batua).
    """
    if n < 0:
        raise ValueError("Negative numbers are not supported")

    # ---- Atomic (0–19) ----
    if n in ATOMS:
        return ATOMS[n]

    # ---- Thousands (≥ 1000) ----
    if n >= 1000:
        thousands = n // 1000
        remainder = n % 1000
        if thousands == 1:
            head = THOUSAND
        else:
            head = multiplicative(number_to_basque(thousands), THOUSAND)
        if remainder == 0:
            return head
        else:
            return additive(head, number_to_basque(remainder))

    # ---- Hundreds (100–999) ----
    if n >= 100:
        hundreds = n // 100
        remainder = n % 100
        head = HUNDREDS_MAP[hundreds]          # fused form
        if remainder == 0:
            return head
        else:
            return additive(head, number_to_basque(remainder))

    # ---- Vigesimal (20–99) ----
    # (numbers 20–99 are handled here; note that 40,60,80 are included)
    if n >= 20:
        twenties = n // 20
        remainder = n % 20
        head = TWENTIES_MAP[twenties]          # fused vigesimal base
        if remainder == 0:
            return head
        else:
            return additive(head, number_to_basque(remainder))

    # Should never reach here because 0–19 already covered
    raise RuntimeError(f"Unexpected number: {n}")

# ------------------------------------------------------------
# 5. REVERSE PARSER (BASQUE → ARABIC)
# ------------------------------------------------------------

# Reverse lookup for atomic numerals
ATOM_VALUES = {v: k for k, v in ATOMS.items()}

# Lexical values for fused bases and special forms
LEXICAL_VALUES = {
    "hogei": 20,
    "berrogei": 40,
    "hirurogei": 60,
    "laurogei": 80,
    "ehun": 100,
    "berrehun": 200,
    "hirurehun": 300,
    "laurehun": 400,
    "bostehun": 500,
    "seiehun": 600,
    "zazpiehun": 700,
    "zortziehun": 800,
    "bederatziehun": 900,
    "mila": 1000,
}

def basque_to_number(text):
    """
    Convert a Basque numeral (Batua) to an Arabic integer.
    """
    text = text.strip()
    if not text:
        raise ValueError("Empty input")

    tokens = text.split()

    # ---- Addition (eta) ----
    if "eta" in tokens:
        idx = tokens.index("eta")
        left = " ".join(tokens[:idx])
        right = " ".join(tokens[idx + 1 :])
        return basque_to_number(left) + basque_to_number(right)

    # ---- Thousands ----
    if "mila" in tokens:
        idx = tokens.index("mila")
        left = tokens[:idx]
        right = tokens[idx + 1 :]
        multiplier = 1 if not left else basque_to_number(" ".join(left))
        value = multiplier * 1000
        if right:
            value += basque_to_number(" ".join(right))
        return value

    # ---- Hundreds ----
    # Look for any of the hundred words (including fused forms)
    hundred_words = set(HUNDREDS_MAP.values())
    for word in hundred_words:
        if word in tokens:
            idx = tokens.index(word)
            left = tokens[:idx]
            right = tokens[idx + 1 :]
            multiplier = 1 if not left else basque_to_number(" ".join(left))
            # Determine the hundred value from LEXICAL_VALUES
            base_value = LEXICAL_VALUES[word]
            value = multiplier * base_value
            if right:
                value += basque_to_number(" ".join(right))
            return value

    # ---- Vigesimal bases (hogei, berrogei, hirurogei, laurogei) ----
    vigesimal_words = {"hogei", "berrogei", "hirurogei", "laurogei"}
    for word in vigesimal_words:
        if word in tokens:
            idx = tokens.index(word)
            left = tokens[:idx]
            right = tokens[idx + 1 :]
            multiplier = 1 if not left else basque_to_number(" ".join(left))
            base_value = LEXICAL_VALUES[word]
            value = multiplier * base_value
            if right:
                value += basque_to_number(" ".join(right))
            return value

    # ---- Simple atomic or lexical ----
    if text in ATOM_VALUES:
        return ATOM_VALUES[text]
    if text in LEXICAL_VALUES:
        return LEXICAL_VALUES[text]

    raise ValueError(f"Unrecognised Basque numeral: '{text}'")

# ============================================================
# STREAMLIT INTERFACE
# ============================================================

st.set_page_config(
    page_title="Basque Numeral Converter",
    layout="centered"
)

st.title("Basque Numeral Converter (Batua)")
st.write(
    "Convert between **Arabic numerals** and **Basque numerals** (Batua). "
    "Implements vigesimal system with lexical blocking and additive `eta`."
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
# Preset examples
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
    "hirurehun eta hogeita bost",
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
        if arabic_input.lstrip('-').isdigit():
            try:
                n = int(arabic_input)
                result = number_to_basque(n)
                st.success(result)
            except Exception as e:
                st.error(str(e))
        else:
            st.error("Please enter a valid integer.")

else:  # Basque → Arabic
    basque_input = st.text_input(
        "Enter a Basque numeral:",
        key="basque_input",
        placeholder="e.g. hogei eta bost"
    )

    if basque_input:
        try:
            result = basque_to_number(basque_input)
            st.success(str(result))
        except Exception as e:
            st.error(str(e))

st.markdown("---")
st.caption(
    "Implements standard Batua vigesimal structure with lexical blocking. "
    "Source data retrieved from Omniglot at https://www.omniglot.com/language/numbers/basque.html. "
    "Converter algorithm created by Yi Zou. "
    "Grammar explained in the Linguistics section."
)

# ------------------------------------------------------------
# Related Pages Navigation
# ------------------------------------------------------------
st.markdown("---")
st.subheader("Explore More")

nav_cols = st.columns(3)

with nav_cols[0]:
    st.page_link(
        "pages/Basque_Linguistics.py",
        label="Linguistics",
        help="Structure, grammar, and historical development of the Basque numeral system"
    )

with nav_cols[1]:
    st.page_link(
        "pages/Olympiad_Problems.py",
        label="Olympiad Problems",
        help="Olympiad Problems"
    )

with nav_cols[2]:
    st.page_link(
        "pages/Basque_Converter.py",
        label="Converter",
        help="Return to the numeral converter"
    )