import streamlit as st

# ============================================================
# IGBO NUMERAL CONVERTER
# Arabic → Igbo (Decimal + Traditional Vigesimal)
# ============================================================

# ------------------------------------------------------------
# 1. ATOMIC NUMERALS
# ------------------------------------------------------------
ATOMS = {
    0: "oroghoro",
    1: "otu",
    2: "abụọ",
    3: "atọ",
    4: "anọ",
    5: "ise",
    6: "isii",
    7: "asaa",
    8: "asatọ",
    9: "itoolu",
    10: "iri",
}

# ============================================================
# 2. DECIMAL IGBO (BASE-10, MODERN SYSTEM)
# ============================================================
def number_to_igbo_decimal(n: int) -> str:
    if n < 0:
        raise ValueError("Negative numbers not supported")

    if n in ATOMS:
        return ATOMS[n]

    # 11–19
    if 10 < n < 20:
        return f"iri na {ATOMS[n - 10]}"

    # 20–99
    if n < 100:
        tens = n // 10
        remainder = n % 10
        head = f"iri {ATOMS[tens]}"
        return head if remainder == 0 else f"{head} na {ATOMS[remainder]}"

    # 100–999
    if n < 1000:
        hundreds = n // 100
        remainder = n % 100
        head = "otu narị" if hundreds == 1 else f"narị {ATOMS[hundreds]}"
        return head if remainder == 0 else f"{head} na {number_to_igbo_decimal(remainder)}"

    # 1000+
    thousands = n // 1000
    remainder = n % 1000
    head = "otu puku" if thousands == 1 else f"puku {number_to_igbo_decimal(thousands)}"
    return head if remainder == 0 else f"{head} na {number_to_igbo_decimal(remainder)}"


# ============================================================
# 3. TRADITIONAL IGBO VIGESIMAL (BASE-20)
# ============================================================
VIG_BASE_WORD = "ọgụ"      # 20
VIG_SUPERBASE_WORD = "nnụ" # 400

def number_to_igbo_vigesimal(n: int) -> str:
    """
    Traditional Igbo vigesimal system.
    Supported range: 0–1999
    """
    if n < 0:
        raise ValueError("Negative numbers not supported")

    if n > 1999:
        return "not defined (beyond traditional vigesimal range)"

    if n in ATOMS:
        return ATOMS[n]

    # 11–19: subtractive from 20
    if 10 < n < 20:
        return f"{ATOMS[20 - n]} na iri abụọ"

    # 20
    if n == 20:
        return VIG_BASE_WORD

    # 21–29: additive to 20
    if 20 < n < 30:
        return f"{VIG_BASE_WORD} na {ATOMS[n - 20]}"

    # 30–39: subtractive from 40
    if 30 <= n < 40:
        return f"{ATOMS[40 - n]} na {number_to_igbo_decimal(2)} na {VIG_BASE_WORD}"

    # Multiples of 20 below 400
    if n < 400:
        multiple = n // 20
        remainder = n % 20

        multiplier_word = number_to_igbo_decimal(multiple)
        head = f"{multiplier_word} na {VIG_BASE_WORD}"

        if remainder == 0:
            return head

        if remainder <= 10:
            return f"{head} na {ATOMS[remainder]}"
        else:
            return (
                f"{ATOMS[20 - remainder]} na "
                f"{number_to_igbo_decimal(multiple + 1)} na {VIG_BASE_WORD}"
            )

    # 400
    if n == 400:
        return VIG_SUPERBASE_WORD

    # 401–799
    if n < 800:
        return f"{VIG_SUPERBASE_WORD} na {number_to_igbo_vigesimal(n - 400)}"

    # Multiples of 400
    multiple = n // 400
    remainder = n % 400

    multiplier_word = number_to_igbo_decimal(multiple)
    head = f"{multiplier_word} na {VIG_SUPERBASE_WORD}"

    return head if remainder == 0 else f"{head} na {number_to_igbo_vigesimal(remainder)}"


# ============================================================
# STREAMLIT UI
# ============================================================
st.set_page_config(
    page_title="Igbo Numeral Converter",
    layout="centered"
)

st.title("Igbo Numeral Converter")

st.write(
    "Convert **Arabic numerals** into **Igbo numerals**, showing:\n\n"
    "- the **modern decimal system** (*base-10*), and\n"
    "- the **traditional vigesimal system** (*base-20*).\n\n"
    "Each output is explicitly labelled."
)

st.markdown("---")

# ------------------------------------------------------------
# Preset examples
# ------------------------------------------------------------
st.subheader("Preset Examples")

presets = [
    0, 5, 11, 19,
    20, 25, 30, 39,
    40, 59, 79,
    100, 256, 399,
    400, 555, 800,
    1200, 1999, 2000
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
    "Enter an Arabic numeral:",
    key="arabic_input",
    placeholder="e.g. 256"
)

if arabic_input:
    if arabic_input.isdigit():
        n = int(arabic_input)

        st.markdown("### Results")

        st.markdown(
            f"**Igbo (Decimal system — base-10):**  \n"
            f"→ {number_to_igbo_decimal(n)}"
        )

        st.markdown(
            f"**Igbo (Traditional system — base-20):**  \n"
            f"→ {number_to_igbo_vigesimal(n)}"
        )
    else:
        st.error("Please enter a valid non-negative integer.")

st.markdown("---")
st.caption(
    "The decimal system reflects modern Standard Igbo usage. "
    "The vigesimal system reflects the traditional base-20 structure. "
    "Both are presented side-by-side for linguistic comparison."
)

# ------------------------------------------------------------
# Related Pages Navigation
# ------------------------------------------------------------
st.markdown("---")
st.subheader("Explore More")

nav_cols = st.columns(3)

with nav_cols[0]:
    st.page_link(
        "pages/Igbo_Linguistics.py",
        label="Linguistics",
        help="Explanation of decimal vs vigesimal Igbo numeral systems"
    )

with nav_cols[1]:
    st.page_link(
        "pages/Igbo_Olympiad_Problems.py",
        label="Olympiad Problems",
        help="Competition-style problems involving Igbo numerals"
    )

with nav_cols[2]:
    st.page_link(
        "pages/Igbo_Converter.py",
        label="Converter",
        help="Return to the numeral converter"
    )
