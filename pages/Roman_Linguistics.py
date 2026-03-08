import streamlit as st
from ui import apply_global_styles

st.set_page_config(page_title="Roman Numerals — Linguistics", layout="centered")

apply_global_styles()


st.title("Roman Numerals — Linguistic Structure")

st.markdown("""
The Roman numeral system is a non-positional decimal system used in Ancient Rome and later European traditions.

Before You Read, Roman is: 
- **Conceptually decimal**
- **Additive–subtractive**
- **Non-positional**
- **Symbolic rather than morphological**
- **Zero-less**

Value is determined by ordered symbol combination rather than place position.
""")

st.divider()

# --------------------------------------------------
# Basic Digits
# --------------------------------------------------

st.header("Basic Symbols")

st.table({
    "Symbol": ["I","V","X","L","C","D","M"],
    "Value": ["1","5","10","50","100","500","1000"]
})

st.markdown("""
Derived historically from tally marks and Latin abbreviations:
I (tally), V (half of X), X (crossed tally), C (centum), M (mille).
""")

st.markdown("#### Standard Subtractive Forms")

st.table({
    "Form": ["IV","IX","XL","XC","CD","CM"],
    "Value": ["4","9","40","90","400","900"],
    "Structure": [
        "5 − 1",
        "10 − 1",
        "50 − 10",
        "100 − 10",
        "500 − 100",
        "1000 − 100"
    ]
})

st.divider()

# --------------------------------------------------
# Structural Explanation
# --------------------------------------------------

st.header("Structure")

st.markdown("""
**Conceptual Base:** 10  
**System Type:** Additive–Subtractive  
**Positional Value:** Absent
""")

# --------------------------------------------------
# Additive
# --------------------------------------------------

st.markdown("#### Additive Structure")

st.markdown("""
**General form:**
Symbols written left to right in descending value are added.
""")

st.code("""
II   = 1 + 1
VIII = 5 + 3
XIII = 10 + 3
LX   = 50 + 10
CL   = 100 + 50
""", language="text")

st.markdown("""
Rule:
If a symbol is followed by one of equal or lesser value → add.
""")

# --------------------------------------------------
# Subtractive
# --------------------------------------------------

st.markdown("#### Subtractive Structure")

st.markdown("""
**General form:**
Smaller symbol before larger symbol → subtract.
""")

st.code("""
IV = 5 − 1
IX = 10 − 1
XL = 50 − 10
XC = 100 − 10
CD = 500 − 100
CM = 1000 − 100
""", language="text")

st.markdown("""
Valid subtractive pairs:

I before V or X  
X before L or C  
C before D or M
""")

st.markdown("""
Restrictions:

• Only one smaller numeral may precede a larger one  
• Only I, X, C may be subtractive  
• V, L, D are never subtractive
""")

# --------------------------------------------------
# Positional Clarification
# --------------------------------------------------

st.markdown("#### Non-Positional Nature")

st.markdown("""
Roman numerals do not use positional place value.

X always represents 10 regardless of location.

Example:
XII = 12  
IIX (invalid classical form)
""")

st.divider()

# --------------------------------------------------
# Special Characters
# --------------------------------------------------

st.header("Special Characters")

st.markdown("""
Core glyph set:
I, V, X, L, C, D, M
""")

st.markdown("#### Overline (Vinculum)")

st.markdown("""
A bar over a numeral multiplies its value by 1,000.
""")

st.code("""
V̅ = 5,000
X̅ = 10,000
M̅ = 1,000,000
""", language="text")

st.markdown("""
Used in inscriptions and manuscripts for large numbers.
""")

st.markdown("#### Zero")

st.markdown("""
Roman numerals have no zero.

Medieval manuscripts sometimes used “N” (nulla), but this is not classical.
""")

st.divider()

# --------------------------------------------------
# Special Structural Cases
# --------------------------------------------------

st.header("Special Structural Cases")

st.markdown("""
### Repetition Limits

I, X, C, M → may be repeated up to three times consecutively.

V, L, D → never repeated.
""")

st.code("""
III  = 3
XXX  = 30
CCC  = 300
MMM  = 3000
""", language="text")

st.markdown("""
### Maximum Standard Classical Form

3,999 = MMMCMXCIX

Beyond this, overlines or later conventions are required.
""")

st.markdown("""
### Alternative Historical Forms

Earlier inscriptions used additive-only forms:

IIII instead of IV  
VIIII instead of IX  

Subtractive notation became standardized later.
""")

st.divider()

# --------------------------------------------------
# Morphology & Inflection
# --------------------------------------------------

st.header("Morphology & Inflection")

st.markdown("""
Inflection: **None**

Roman numeral symbols are invariant glyphs.
They do not change for case, gender, or number.
""")

st.markdown("""
In Latin text, ordinal numbers are written as fully inflected adjectives (e.g., primus, secundus), not as Roman numeral glyphs.
""")

st.divider()

# --------------------------------------------------
# Navigation
# --------------------------------------------------

st.markdown("---")
st.markdown("### Navigation")

col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/Roman_Converter.py", label="Converter")

with col2:
    st.page_link("pages/Roman_Linguistics.py", label="Linguistics")