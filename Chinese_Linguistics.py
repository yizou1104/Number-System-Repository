import streamlit as st

st.set_page_config(page_title="Chinese Numerals — Linguistics", layout="centered")

st.title("Chinese Numerals — Linguistic Structure")

st.markdown("""
The Chinese number system is one of the most structurally transparent numeral systems in the world.

Before You Read, Chinese is: 
- **Explicitly base-10**
- **Fully multiplicative**
- **Compositional and deterministic**
- **Morphologically invariant**

Numerals are built by combining fixed morphemes according to strict grammatical rules rather than by inflection or positional notation.
""")

st.divider()

# --------------------------------------------------
# Basic Digits
# --------------------------------------------------

st.header("Basic Digits (1–9)")

st.markdown("""
Each digit from 1 to 9 has a distinct morpheme.  
These morphemes **never inflect**.

Chinese, as a largely monosyllabic and logographic language, does not exhibit morphological variation in numerals in the way alphabetic languages sometimes do.
""")

st.table({
    "Number": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "Character": ["一", "二", "三", "四", "五", "六", "七", "八", "九"],
    "Pinyin": ["yī", "èr", "sān", "sì", "wǔ", "liù", "qī", "bā", "jiǔ"]
})

st.markdown("""

Chinese uses explicit morphemes for powers of ten.  
Unlike English, which groups by thousands (10³), Chinese groups by **ten-thousands (10⁴)**.
""")

st.table({
    "Power": ["10¹", "10²", "10³", "10⁴", "10⁸"],
    "Value": ["10", "100", "1,000", "10,000", "100,000,000"],
    "Character": ["十", "百", "千", "万", "亿"],
    "Pinyin": ["shí", "bǎi", "qiān", "wàn", "yì"]
})

st.markdown("""
Every power of ten up to 10⁴ has its own morpheme, followed by a new grouping unit at 10⁸.

In practice, **万 (10⁴)** functions as the primary grouping boundary:
- 10⁵ → 十万 = (10)(10⁴)
- 10⁷ → 千万 = (10³)(10⁴)
""")

st.divider()

# --------------------------------------------------
# Multiplicative Construction
# --------------------------------------------------

st.header("Multiplicative Structure")

st.markdown("""
Numbers are constructed using a **digit × base** rule.

The digit always precedes the base morpheme.
""")

st.code("""
二十   = 2 × 10   = 20
三百   = 3 × 100  = 300
四千   = 4 × 1000 = 4000
""", language="text")

st.divider()

# --------------------------------------------------
# Additive Composition
# --------------------------------------------------

st.header("Additive Structure")

st.markdown("""
After multiplication, values are **added left-to-right**.

Formally:
1. Multiply the base morpheme by the digit before it.
2. Add any remaining digits or lower-order constructions.
""")

st.code("""
二十三       = (2 × 10) + 3
四百五十六   = (4 × 100) + (5 × 10) + 6
""", language="text")

st.markdown("""
This structure closely parallels English and the Hindu-Arabic system, but remains explicitly grammatical rather than positional.
""")

st.divider()

# --------------------------------------------------
# Zero
# --------------------------------------------------

st.header("Zero (零)")

st.markdown("""
零 (*líng*) does **not** represent quantity in isolation.  
Instead, it marks a **skipped place value** between expressed numerals.

This is similar to the role of 0 in Arabic numerals, but with stricter usage constraints.
""")

st.code("""
一百零三     = 103
一千零二十   = 1020
""", language="text")

st.markdown("""
In **一千零二十**, the final zero is already implied by 二十 (20),  
so only the missing hundreds place is explicitly marked.
""")

st.markdown("""
Chinese enforces strict grammatical constraints on 零:
- 零 **never appears twice consecutively**
- 零 **never appears at the end of a numeral**
- 零 **only appears when a lower place value exists**
""")

st.divider()

# --------------------------------------------------
# Special Cases
# --------------------------------------------------

st.header("Special Syntactic Cases")

st.markdown("""
The digit 一 (*yī*) is often omitted before 十 (*shí*).
""")

st.code("""
十      = 10      (not 一十)
十一    = 11
十五    = 15
""", language="text")

st.divider()

# --------------------------------------------------
# Financial Numerals
# --------------------------------------------------

st.header("Financial (Formal) Numerals")

st.markdown("""
Because many standard numeral characters have very few strokes, they are vulnerable to alteration in legal and financial contexts.

Chinese therefore uses a **separate set of financial numerals** in formal documents.
""")

st.table({
    "Normal": ["一", "二", "三", "十", "百", "千"],
    "Financial": ["壹", "贰", "叁", "拾", "佰", "仟"]
})

st.markdown("""
These forms are **context-restricted** and do not replace standard numerals in everyday usage.
""")

# --------------------------------------------------
# Navigation
# --------------------------------------------------

st.markdown("---")
st.markdown("### Navigation")

col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/Chinese_Converter.py", label="Converter")

with col2:
    st.page_link("pages/Chinese_Linguistics.py", label="Linguistics")