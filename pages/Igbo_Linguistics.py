import streamlit as st
from ui import apply_global_styles

st.set_page_config(page_title="Igbo Numerals — Linguistics", layout="centered")

apply_global_styles()


st.title("Igbo Numerals — Linguistic Structure")

st.markdown("""
The Igbo numeral system contains both a modern decimal system and an older traditional vigesimal system.

Before You Read, Igbo is:
- **Primarily decimal (modern usage)**
- **Historically vigesimal (base-20)**
- **Multiplicative in higher units**
- **Additive within decades**
- **Subtractive in older vigesimal forms**
- **Morphologically invariant**
- **Written in the Latin alphabet**
""")

st.divider()

# --------------------------------------------------
# Basic Digits
# --------------------------------------------------

st.header("Basic Digits (0–10)")

st.table({
    "Number": ["0","1","2","3","4","5","6","7","8","9","10"],
    "Form": [
        "efu / oruoghoro / ncha / adịgị / okpokoro",
        "otu",
        "abụọ",
        "atọ",
        "anọ",
        "ise",
        "isii",
        "asaa",
        "asatọ",
        "itoolu / iteghète",
        "iri"
    ]
})

st.markdown("""
Igbo uses the Latin alphabet with diacritics marking tone and vowel quality.
Arabic numerals are used in writing.
""")

st.markdown("#### Bases (Modern Decimal System)")

st.table({
    "Value": [
        "20","30","40","50","60","70","80","90",
        "100","1,000","10,000","100,000","1,000,000"
    ],
    "Form": [
        "iri abụọ",
        "iri atọ",
        "iri anọ",
        "iri ise",
        "iri isii",
        "iri asaa",
        "iri asatọ",
        "iri itoolu",
        "otu narị",
        "otu puku",
        "puku iri",
        "otu narọ puku",
        "otu nde"
    ],
    "Structure": [
        "2 × 10",
        "3 × 10",
        "4 × 10",
        "5 × 10",
        "6 × 10",
        "7 × 10",
        "8 × 10",
        "9 × 10",
        "1 × 100",
        "1 × 1,000",
        "10 × 1,000",
        "100 × 1,000",
        "1 × 1,000,000"
    ]
})

st.divider()

# --------------------------------------------------
# Structural Explanation
# --------------------------------------------------

st.header("Structure")

st.markdown("""
**Primary Base (Modern):** 10  
**Secondary Base (Traditional):** 20  
**System Type:** Multiplicative–Additive (Modern)  
**Subtractive Formation:** Present historically (vigesimal system)
""")

# --------------------------------------------------
# Multiplicative (Modern Decimal)
# --------------------------------------------------

st.markdown("#### Multiplicative Structure (Modern Decimal)")

st.markdown("""
**General form:**
Digit × iri (for tens)  
Digit × magnitude noun (for hundreds and above)
""")

st.code("""
20 = iri abụọ
30 = iri atọ
40 = iri anọ

100 = otu narị
1,000 = otu puku
1,000,000 = otu nde
""", language="text")

st.markdown("""
Higher magnitudes combine multiplicatively with narị, puku, and nde.
""")

# --------------------------------------------------
# Additive (Modern)
# --------------------------------------------------

st.markdown("#### Additive Structure (Modern)")

st.markdown("""
Compound numbers use the conjunction “na”.
""")

st.markdown("""
**General form:**
[Tens base] + na + [Unit]
""")

st.code("""
11 = iri na otu
12 = iri na abụọ
25 = iri abụọ na ise
47 = iri anọ na asaa
""", language="text")

# --------------------------------------------------
# Subtractive (Traditional)
# --------------------------------------------------

st.markdown("#### Subtractive Structure (Traditional Vigesimal)")

st.markdown("""
Present in older counting patterns based on base-20.
""")

st.markdown("""
**General form:**
[Subtracted quantity] relative to vigesimal base (e.g., 20 = ọgụ)
""")

st.markdown("""
Traditional 20 = ọgụ  

Some older forms express numbers relative to the next vigesimal pivot.
These are not standard in modern educational usage.
""")

st.divider()

# --------------------------------------------------
# Special Characters / Connectors
# --------------------------------------------------

st.header("Special Characters / Connectors")

st.markdown("""
Igbo has multiple lexical terms for zero:
""")

st.code("""
efu
oruoghoro
ncha
adịgị
okpokoro
""", language="text")

st.markdown("""
These are variant spoken forms rather than a single standardized term.
""")

st.markdown("#### Additive Connector")

st.markdown("""
na — links tens and units in compound numbers.
""")

st.divider()

# --------------------------------------------------
# Special Syntactic Cases
# --------------------------------------------------

st.header("Special Syntactic Cases")

st.markdown("""
#### Decimal vs. Traditional Vigesimal

Modern Igbo primarily uses decimal formations.
Traditional forms, however, retain vigesimal roots such as ọgụ (20).
""")

st.markdown("""
#### Conjunction Placement

The conjunction “na” appears immediately before the unit element in compound numbers.
            
Aside from all this, different dialects may also exhibit variant lexical forms, especially for zero and nine.
""")

st.divider()

# --------------------------------------------------
# Morphology & Inflection
# --------------------------------------------------

st.header("Morphology & Inflection")

st.markdown("""
Inflection on numerals: **Absent**

Numerals function as invariant lexical items.
""")

st.markdown("#### Ordinal Formation")

st.code("""
nke mbụ / nke izizi   (first)
nke abụọ              (second)
nke atọ               (third)
""", language="text")

st.markdown("""
General pattern:
nke + cardinal numeral
""")

st.divider()

# --------------------------------------------------
# Navigation
# --------------------------------------------------

st.markdown("---")
st.markdown("### Navigation")

col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/Igbo_Converter.py", label="Converter")

with col2:
    st.page_link("pages/Igbo_Linguistics.py", label="Linguistics")