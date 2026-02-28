import streamlit as st

st.set_page_config(page_title="Thai Numerals — Linguistics", layout="centered")

st.title("Thai Numerals — Linguistic Structure")

st.markdown("""
The Thai numeral system is structurally regular and strictly decimal.

Before You Read, Thai is: 
- **Base-10 (decimal)**
- **Multiplicative in scaling**
- **Additive within units**
- **Non-subtractive**
- **Morphologically invariant**
- **Classifier-dependent in syntax**
- **Position-sensitive in specific forms**

Thai combines multiplicative base formation with additive sequencing.
""")

st.divider()

# --------------------------------------------------
# Basic Digits
# --------------------------------------------------

st.header("Basic Digits (0–10)")

st.table({
    "Number": ["0","1","2","3","4","5","6","7","8","9","10"],
    "Glyph": ["๐","๑","๒","๓","๔","๕","๖","๗","๘","๙","๑๐"],
    "Form": [
        "ศูนย์",
        "หนึ่ง",
        "สอง",
        "สาม",
        "สี่",
        "ห้า",
        "หก",
        "เจ็ด",
        "แปด",
        "เก้า",
        "สิบ"
    ]
})

st.markdown("""
Thai uses its own numeral glyphs, though Arabic numerals are common in modern usage.
""")

st.markdown("#### Bases")

st.table({
    "Value": [
        "20","30","40","50","60","70","80","90",
        "100","1,000","10,000","100,000","1,000,000"
    ],
    "Form": [
        "ยี่สิบ","สามสิบ","สี่สิบ","ห้าสิบ","หกสิบ",
        "เจ็ดสิบ","แปดสิบ","เก้าสิบ",
        "ร้อย","พัน","หมื่น","แสน","ล้าน"
    ],
    "Structure": [
        "2 × 10 (special form)",
        "3 × 10",
        "4 × 10",
        "5 × 10",
        "6 × 10",
        "7 × 10",
        "8 × 10",
        "9 × 10",
        "Independent hundred unit",
        "Independent thousand unit",
        "Independent 10⁴ unit",
        "Independent 10⁵ unit",
        "Independent 10⁶ unit (recursive pivot)"
    ]
})

st.divider()

# --------------------------------------------------
# Structural Explanation
# --------------------------------------------------

st.header("Structure")

st.markdown("""
**Primary Base:** 10  
**System Type:** Multiplicative–Additive  
**Subtractive Formation:** Absent
""")

# --------------------------------------------------
# Multiplicative
# --------------------------------------------------

st.markdown("#### Multiplicative Structure")

st.markdown("""
**General form:**
Digit + Base Unit
""")

st.code("""
20  = ยี่ + สิบ
30  = สาม + สิบ

200 = สองร้อย
500 = ห้าร้อย

3,000 = สามพัน
""", language="text")

st.markdown("""
Large units stack multiplicatively:

[number] + หมื่น  
[number] + แสน  
[number] + ล้าน
""")

st.markdown("""
ล้าน (1,000,000) functions recursively.
""")

st.code("""
1,000,000      = ล้าน
10,000,000     = สิบล้าน
100,000,000    = ร้อยล้าน
1,000,000,000  = หนึ่งพันล้าน
""", language="text")

# --------------------------------------------------
# Additive
# --------------------------------------------------

st.markdown("#### Additive Structure")

st.markdown("""
Used within decades and across compound numbers.
""")

st.markdown("""
**General form:**
[Higher unit] + [Lower unit] (descending order)
""")

st.code("""
21  = ยี่สิบเอ็ด     (20 + 1)
32  = สามสิบสอง     (30 + 2)

1,234
= หนึ่งพันสองร้อยสามสิบสี่
""", language="text")

st.markdown("""
Compound numbers follow strict descending unit order:
Millions → Hundred-thousands → Ten-thousands → Thousands → Hundreds → Tens → Units
""")

# --------------------------------------------------
# Position-Sensitive Variants
# --------------------------------------------------

st.markdown("#### Position-Sensitive Variants")

st.markdown("""
**Special form for “2” in tens:**
ยี่ used instead of สอง in the tens position.
""")

st.code("""
20 = ยี่สิบ
""", language="text")

st.markdown("""
**Special form for final “1”:**
เอ็ด replaces หนึ่ง when 1 appears at the end of compound numbers.
""")

st.code("""
21  = ยี่สิบเอ็ด
101 = หนึ่งร้อยเอ็ด
""", language="text")

st.divider()

# --------------------------------------------------
# Special Characters
# --------------------------------------------------

st.header("Special Characters")

st.markdown("""
Thai numeral glyphs:

๐ ๑ ๒ ๓ ๔ ๕ ๖ ๗ ๘ ๙
""")

st.markdown("""
Arabic numerals are widely used in modern contexts.
""")

st.markdown("#### Zero")

st.markdown("""
ศูนย์ (sǔun) — borrowed from Sanskrit śūnya.

Used in mathematics, administrative numbering, and telephone reading.
""")

st.divider()

# --------------------------------------------------
# Special Syntactic Cases
# --------------------------------------------------

st.header("Special Syntactic Cases")

st.markdown("""
### Numeral–Classifier Order

Standard structure:
Numeral + Classifier + Noun
""")

st.markdown("""
Examples:

หนึ่งคน  
สามเล่ม
""")

st.markdown("""
Classifier usage is obligatory in most counted noun phrases.
""")

st.markdown("""
### Digit-by-Digit Reading

Telephone numbers and serial numbers are often read digit-by-digit.
""")

st.code("""
1984 → หนึ่ง เก้า แปด สี่
""", language="text")

st.markdown("""
### Approximation by Reduplication

ร้อย ๆ   (“hundreds”)  
พัน ๆ    (“thousands”)
""")

st.divider()

# --------------------------------------------------
# Morphology & Inflection
# --------------------------------------------------

st.header("Morphology & Inflection")

st.markdown("""
Inflection on numerals: **Absent**

- No gender marking
- No case marking
- No agreement morphology

Plurality is expressed through classifiers or noun marking.
""")

st.markdown("### Ordinal Formation")

st.markdown("""
Ordinals formed analytically.
""")

st.code("""
ที่หนึ่ง
ที่สอง
ที่สาม
""", language="text")

st.markdown("""
General pattern:
ที่ + Cardinal
""")

st.divider()

# --------------------------------------------------
# Navigation
# --------------------------------------------------

st.markdown("---")
st.markdown("### Navigation")

col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/Thai_Converter.py", label="Converter")

with col2:
    st.page_link("pages/Thai_Linguistics.py", label="Linguistics")

with col3:
    st.page_link("pages/Thai_Olympiad_Problems.py", label="Olympiad Problems")