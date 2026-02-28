import streamlit as st

st.set_page_config(page_title="Tibetan Numerals — Linguistics", layout="centered")

st.title("Tibetan Numerals — Linguistic Structure")

st.markdown("""
The Tibetan numeral system is structurally transparent and strictly decimal.

Before You Read, Tibetan is: 
- **Base-10 (decimal)**
- **Multiplicative in tens and higher units**
- **Additive within decades**
- **Non-subtractive**
- **Morphologically invariant**
- **Classifier-interacting**
- **Written in an independent numeral script**

Tibetan combines multiplicative scaling with additive composition.
""")

st.divider()

# --------------------------------------------------
# Basic Digits
# --------------------------------------------------

st.header("Basic Digits (0–10)")

st.table({
    "Number": ["0","1","2","3","4","5","6","7","8","9","10"],
    "Glyph": ["༠","༡","༢","༣","༤","༥","༦","༧","༨","༩","༡༠"],
    "Form": [
        "ཀླད་ཀོར / སྟོང་",
        "གཅིག",
        "གཉིས",
        "གསུམ",
        "བཞི",
        "ལྔ",
        "དྲུག",
        "བདུན",
        "བརྒྱད",
        "དགུ",
        "བཅུ"
    ]
})

st.markdown("""
Written Tibetan preserves historical consonant clusters.
Spoken forms often simplify these significantly.
""")

st.markdown("#### Bases")

st.table({
    "Value": [
        "20","30","40","50","60","70","80","90",
        "100","1,000","10,000","100,000"
    ],
    "Form": [
        "ཉི་ཤུ","སུམ་ཅུ","བཞི་བཅུ","ལྔ་བཅུ","དྲུག་བཅུ",
        "བདུན་བཅུ","བརྒྱད་བཅུ","དགུ་བཅུ",
        "བརྒྱ","སྟོང","ཁྲི","འབུམ"
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
        "Independent hundred unit",
        "Independent thousand unit",
        "Independent 10⁴ unit",
        "Independent 10⁵ unit"
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
Digit (2–9) + “ten”  
Digit + higher base unit
""")

st.code("""
20  = ཉི་ཤུ       (2 × 10)
30  = སུམ་ཅུ     (3 × 10)
40  = བཞི་བཅུ     (4 × 10)

200  = གཉིས བརྒྱ   (2 × 100)
300  = གསུམ བརྒྱ

2,000 = གཉིས སྟོང
""", language="text")

st.markdown("""
Higher numerals scale multiplicatively:

[number] + [unit]
""")

# --------------------------------------------------
# Additive
# --------------------------------------------------

st.markdown("#### Additive Structure")

st.markdown("""
Used within decades.
""")

st.markdown("""
**General form:**
[Tens expression] + [Unit digit]
""")

st.code("""
21 = ཉི་ཤུ གཅིག      (20 + 1)
37 = སུམ་ཅུ བདུན      (30 + 7)

19 = བཅུ དགུ           (10 + 9)
99 = དགུ་བཅུ དགུ       (9×10 + 9)
""", language="text")

st.markdown("""
Within decades, addition is typically expressed by simple juxtaposition.

Example:
ཉི་ཤུ གཅིག  (20 + 1)

No constant conjunction is used at this level.

At larger structural boundaries, Tibetan may employ དང་ (dang) as a coordinating particle between major units.
""")

# --------------------------------------------------
# Subtractive
# --------------------------------------------------

st.divider()

# --------------------------------------------------
# Special Characters
# --------------------------------------------------

st.header("Special Characters")

st.markdown("""
Tibetan has its own numeral glyphs:
""")

st.markdown("༠ ༡ ༢ ༣ ༤ ༥ ༦ ༧ ༨ ༩")

st.markdown("""
These appear in manuscripts, folio numbering, calendars, and religious texts.
Modern contexts also use Arabic numerals.
""")

st.markdown("#### Zero")

st.markdown("""
Symbol: ༠  

Zero is used in modern arithmetic contexts.
Traditional texts often conceptualized numerical absence lexically rather than structurally.
""")

st.divider()

# --------------------------------------------------
# Special Syntactic Cases
# --------------------------------------------------

st.header("Special Syntactic Cases")

st.markdown("""
### Numeral–Noun Order

Standard order:
Numeral + Classifier + Noun
""")

st.markdown("""
Example:
གཅིག མི  
(gcig mi — “one person”)
""")

st.markdown("""
### Classifier Usage

Tibetan employs classifiers, especially in colloquial speech.
Classifier omission is possible in formal enumerations.
""")

st.markdown("""
### Orthography vs Pronunciation

Written forms preserve historical consonant clusters.
Spoken Lhasa Tibetan simplifies many clusters.

Example:
བརྒྱད → gyé (spoken)
""")

st.divider()

# --------------------------------------------------
# Morphology & Inflection
# --------------------------------------------------

st.header("Morphology & Inflection")

st.markdown("""
Inflection on numerals: **Absent**
            
Plural marking is independent of numerals.
            
However, Tibetan numerals exhibit divergence between written orthography and spoken pronunciation.

Examples:

བརྒྱད → gyé  
གཅིག → chik  

These changes reflect historical consonant clusters and sandhi processes, which is not inflectional morphology but is a morphological change nevertheless.
""")

st.markdown("#### Ordinal Formation")

st.markdown("""
Often formed with ordinal suffixes.
""")

st.code("""
First   = དང་པོ་ (dang po)
Second  = གཉིས་པ་ (gnyis pa)
Third   = གསུམ་པ་ (gsum pa)
""", language="text")

st.markdown("""
General pattern:
[Cardinal] + ordinal suffix (-pa / -ba / -ma)
""")

st.markdown("---")
st.markdown("### Navigation")

col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/Tibetan_Converter.py", label="Converter")

with col2:
    st.page_link("pages/Tibetan_Linguistics.py", label="Linguistics")

with col3:
    st.page_link("pages/Tibetan_Olympiad_Problems.py", label="Olympiad Problems")