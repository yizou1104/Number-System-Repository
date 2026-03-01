import streamlit as st

st.set_page_config(page_title="Yoruba Numerals — Linguistics", layout="centered")

st.title("Yoruba Numerals — Linguistic Structure")

st.markdown("""
The Yoruba numeral system is structurally complex and typologically distinctive.

Before You Read, Yoruba is: 
- **Primarily base-20 (vigesimal)**
- **Multiplicative in scaling**
- **Additive in restricted environments**
- **Systematically subtractive**
- **Morphologically invariant**
- **Tonal (phonemic tone distinctions)**

Unlike strictly decimal systems, Yoruba integrates multiplication, addition, and subtraction within a vigesimal framework.
""")

st.divider()

# --------------------------------------------------
# Basic Digits
# --------------------------------------------------

st.header("Basic Digits (1–10)")

st.table({
    "Number": [1,2,3,4,5,6,7,8,9,10],
    "Form": ["ọ̀kan","èjì","ẹ̀ta","ẹ̀rin","àrún","ẹ̀fà","èje","ẹ̀jọ","ẹ̀sán","ẹ̀wá"]
})

st.markdown("""
Yoruba is written in the Latin alphabet with phonemic tone marking.
Tone distinctions are linguistically meaningful.
""")

st.markdown("#### Bases")

st.table({
    "Value": [
        "20","30","40","50","60","70",
        "80","90","100","200","400","10,000"
    ],
    "Form": [
        "ogún","ọgbọ̀n","ogójì","àádọ́ta","ọgọ́ta","àádọ́rin",
        "ọgọ́rin","àádọ́rùn-ún","ọgọ́rùn-ún","igba","irinwo","ẹgbẹ̀rún"
    ],
    "Structure": [
        "Base unit",
        "Lexicalized decade",
        "2 × 20",
        "10 less than 60",
        "3 × 20",
        "10 less than 80",
        "4 × 20",
        "10 less than 100",
        "5 × 20",
        "10 × 20",
        "20 × 20",
        "Higher unit"
    ]
})

st.divider()

# --------------------------------------------------
# Structural Explanation
# --------------------------------------------------

st.header("Structure")

st.markdown("""
**Primary Base:** 20  
**System Type:** Mixed (Multiplicative + Additive + Subtractive)  
**Secondary Influence:** Decimal elements in limited contexts
""")

# --------------------------------------------------
# Multiplicative
# --------------------------------------------------

st.markdown("#### Multiplicative Structure")

st.markdown("""
**General form:**
Multiplier × 20  
(or higher multiplier × vigesimal base)
""")

st.code("""
ogójì       = 2 × 20   = 40
ọgọ́ta       = 3 × 20   = 60
ọgọ́rin      = 4 × 20   = 80
ọgọ́rùn-ún   = 5 × 20   = 100

igba        = 10 × 20  = 200
irinwo      = 20 × 20  = 400
""", language="text")

st.markdown("""
Multiplication scales hierarchically within the vigesimal system.
""")

# --------------------------------------------------
# Additive
# --------------------------------------------------

st.markdown("#### Additive Structure")

st.markdown("""
Addition appears in restricted environments:
- 11–14
- 21–24
- Units (1–4) above vigesimal bases
""")

st.markdown("""
**General form:**
Unit (1–4) + lé / lá + Base
""")

st.code("""
11  = ọ̀kanlá   (1 + 10)
12  = èjìlá     (2 + 10)
13  = ẹ̀tàlá     (3 + 10)
14  = ẹ̀rìnlá   (4 + 10)

21  = ọ̀kan lé ogún
22  = èjìlélógún
23  = ẹ̀tàlélógún
24  = ẹ̀rìnlélógún
""", language="text")

# --------------------------------------------------
# Subtractive
# --------------------------------------------------

st.markdown("#### Subtractive Structure")

st.markdown("""
Used for:
- 15–19 (relative to 20)
- 25–29 (relative to 30)
- 50 (relative to 60)
- 70 (relative to 80)
- 90 (relative to 100)
""")

st.markdown("""
**General form:**
[Subtracted quantity] + dín + Base
""")

st.code("""
15 = ẹ̀ẹ́dógún        (5 from 20)
16 = ẹ̀rìndínlógún    (4 less than 20)
17 = ẹ̀tàdínlógún
18 = ẹ̀jìdínlógún
19 = ọ̀kàndínlógún

50 = àádọ́ta         (10 less than 60)
70 = àádọ́rin        (10 less than 80)
90 = àádọ́rùn-ún     (10 less than 100)
""", language="text")

st.divider()

# --------------------------------------------------
# Special Characters / Connectors
# --------------------------------------------------

st.header("Special Characters / Connectors")

st.markdown("""
Yoruba uses the Latin alphabet with phonemic tone marks.
There are no indigenous numeral glyphs.
""")

st.table({
    "Element": ["lé / lá", "dín", "àádọ́-"],
    "Function": [
        "Additive connector ('plus')",
        "Subtractive marker ('less than')",
        "Fossilized subtractive prefix (10 less than base)"
    ]
})

st.markdown("#### Zero")

st.markdown("""
Traditional Yoruba counting has no indigenous zero term.

Modern mathematical contexts use borrowed or adapted forms.
Zero is not structurally integrated into the traditional vigesimal grammar.
""")

st.divider()

# --------------------------------------------------
# Special Syntactic Cases
# --------------------------------------------------

st.header("Special Syntactic Cases")

st.markdown("""
### Lexicalization

Some forms are historically compositional, but with time become lexicalized:

- 30 — ọgbọ̀n
- 50 — àádọ́ta
""")

st.markdown("""
### Tone Sensitivity

Yoruba is a three-level tonal language (High, Mid, Low).
Tone distinctions are phonemic and integral to numeral identity.
""")

st.markdown("""
### Simplification

In urban or commercial contexts:
- Subtractive constructions may be simplified.
- Decimal-style counting may appear.

An interesting source can be found here, which proposes a new decimal-based system for modern use: https://scienceinyoruba.org/2024/11/18/the-new-adeniyan-adebayo-yoruba-numbering-system-python-codes/

""")

st.divider()

# --------------------------------------------------
# Morphology & Inflection
# --------------------------------------------------

st.header("Morphology & Inflection")

st.markdown("""
Inflection on numerals: **Absent**

- No grammatical gender
- No case marking
- No agreement morphology
- No plural marking

Numerals function as invariant lexical items.
""")

st.markdown("### Ordinal Formation")

st.code("""
First   = àkọ́kọ́
Second  = èkejì
Third   = ẹ̀kẹta
""", language="text")

st.markdown("""
Common pattern:
Ordinal prefix è-/ẹ̀- + cardinal root (derivational, not inflectional).
""")
# --------------------------------------------------
# Special Phenomena
# --------------------------------------------------

st.markdown("---")
st.markdown("### Navigation")

col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/Yoruba_Converter.py", label="Converter")

with col2:
    st.page_link("pages/Yoruba_Linguistics.py", label="Linguistics")