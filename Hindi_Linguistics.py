import streamlit as st

st.set_page_config(page_title="Hindi Numerals — Linguistics", layout="centered")

st.title("Hindi Numerals — Linguistic Structure")

st.markdown("""
The Hindi numeral system is decimal, but the numbers are largely lexical and irregular between 1–99.

Before You Read, Hindi is: 
- **Base-10 (decimal)**
- **Lexicalized from 1–99**
- **Multiplicative–additive from 100 upward**
- **Non-subtractive**
- **Lakh-based in large-number grouping**
- **Partially inflectional in ordinal forms**
""")

st.divider()

# --------------------------------------------------
# Basic Digits
# --------------------------------------------------

st.header("Basic Digits (0–10)")

st.table({
    "Number": ["0","1","2","3","4","5","6","7","8","9","10"],
    "Glyph": ["०","१","२","३","४","५","६","७","८","९","१०"],
    "Form": [
        "शून्य / सिफ़र",
        "एक",
        "दो",
        "तीन",
        "चार",
        "पाँच",
        "छह",
        "सात",
        "आठ",
        "नौ",
        "दस"
    ]
})

st.markdown("""
Hindi uses Devanagari numeral glyphs, though Arabic numerals (0–9) are common in modern usage.
""")

st.markdown("#### Irregular 11–19")

st.table({
    "Number": ["11","12","13","14","15","16","17","18","19"],
    "Form": [
        "ग्यारह","बारह","तेरह","चौदह",
        "पंद्रह","सोलह","सत्रह","अठारह","उन्नीस"
    ]
})

st.markdown("""
Forms from 11–19 are synchronically irregular and must be memorized.
""")

st.markdown("#### Tens")

st.table({
    "Value": ["20","30","40","50","60","70","80","90"],
    "Form": [
        "बीस","तीस","चालीस","पचास",
        "साठ","सत्तर","अस्सी","नब्बे"
    ]
})

st.markdown("""
All decades are lexicalized and not transparently “digit × 10”.
""")

st.markdown("#### Higher Bases")

st.table({
    "Value": ["100","1,000","100,000","10,000,000","1,000,000,000","100,000,000,000"],
    "Form": [
        "सौ",
        "हज़ार",
        "लाख",
        "करोड़",
        "अरब",
        "खरब"
    ],
    "Structure": [
        "Independent hundred unit",
        "Independent thousand unit",
        "10⁵ pivot (Indian grouping)",
        "10⁷ pivot",
        "10⁹ unit",
        "10¹¹ unit"
    ]
})

st.divider()

# --------------------------------------------------
# Structure
# --------------------------------------------------

st.header("Structure")

st.markdown("""
**Primary Base:** 10  
**Large-Number Pivot:** 10⁵ (lakh system)  
**System Type:** Lexicalized decimal (1–99), Multiplicative–Additive (100+)  
**Subtractive Formation:** Absent
""")

# --------------------------------------------------
# 1–99 Structure
# --------------------------------------------------

st.markdown("#### 1–99 Structure (Lexicalized)")

st.markdown("""
**General form:**
Memorized lexical items with internal morphophonological alternations.
""")

st.code("""
21 = इक्कीस
25 = पच्चीस
29 = उनतीस
59 = उनसठ
""", language="text")

st.markdown("""
Features include:
• Prefix alternations  
• Consonant gemination  
• “Un-” forms in some decades  

These patterns are historically derived but not synchronically productive.
""")

# --------------------------------------------------
# 100 and Above
# --------------------------------------------------

st.markdown("#### Multiplicative–Additive Structure (100+)")

st.markdown("""
**General form:**
[Digit] + Base Unit + [Lower components]
""")

st.code("""
125 = एक सौ पच्चीस
250 = दो सौ पचास

5,432
= पाँच हज़ार चार सौ बत्तीस
""", language="text")

st.markdown("""
Structure follows descending magnitude order.
""")

st.markdown("""
Lakhs and crores follow Indian grouping:
""")

st.code("""
1,23,45,678
= 1 करोड़ 23 लाख 45 हज़ार 678
""", language="text")

st.markdown("""
Digit grouping pattern:
3-2-2-2 (Indian system)
""")

# --------------------------------------------------
# Subtractive
# --------------------------------------------------

st.markdown("#### Subtractive Structure")

st.markdown("""
Hindi does not employ subtractive numeral formation.

19 (उन्नीस) is lexical, not structurally “20 − 1”.
""")

st.divider()

# --------------------------------------------------
# Special Characters
# --------------------------------------------------

st.header("Special Characters")

st.markdown("""
Devanagari numeral glyphs:

० १ २ ३ ४ ५ ६ ७ ८ ९
""")

st.markdown("#### Zero")

st.markdown("""
Two lexical forms exist:

शून्य — Sanskrit origin  
सिफ़र — Persian/Arabic origin  

“सिफ़र” is common in financial contexts.
""")

st.markdown("""
Indian digit grouping differs from Western systems:

1,00,000  
1,00,00,000
""")

st.divider()

# --------------------------------------------------
# Special Syntactic Cases
# --------------------------------------------------

st.header("Special Syntactic Cases")

st.markdown("""
### Agreement (Limited)

Cardinals are largely invariant.

“एक” behaves syntactically like an adjective:
""")

st.code("""
एक आदमी
एक किताब
""", language="text")

st.markdown("""
### Compound Number Order

Descending magnitude order:

[Crore] + [Lakh] + [Thousand] + [Hundred] + [1–99]

No internal conjunction equivalent to English “and”.
""")

st.markdown("""
### Ordinals

Irregular forms:
""")

st.code("""
पहला
दूसरा
तीसरा
चौथा
""", language="text")

st.markdown("""
From 5 onward often:
""")

st.code("""
पाँचवाँ
छठा
""", language="text")

st.markdown("""
Ordinals inflect for gender and number.
""")

st.divider()

# --------------------------------------------------
# Morphology & Inflection
# --------------------------------------------------

st.header("Morphology & Inflection")

st.markdown("""
Cardinals:
• Invariant  
• No case marking  
• No plural marking  

Plural marking may be suppressed after numerals:
""")

st.code("""
तीन आदमी
""", language="text")

st.markdown("""
Ordinals:
• Fully adjectival  
• Agree in gender and number
""")

st.code("""
पहला लड़का
पहली लड़की
पहले लड़के
""", language="text")

st.divider()

# --------------------------------------------------
# Navigation
# --------------------------------------------------

st.markdown("---")
st.markdown("### Navigation")

col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/Hindi_Converter.py", label="Converter")

with col2:
    st.page_link("pages/Hindi_Linguistics.py", label="Linguistics")

with col3:
    st.page_link("pages/Hindi_Olympiad_Problems.py", label="Olympiad Problems")