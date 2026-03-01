import streamlit as st

st.set_page_config(page_title="Swahili Numerals — Linguistics", layout="centered")

st.title("Swahili Numerals — Linguistic Structure")

st.markdown("""
The Swahili numeral system is decimal and morphologically layered.

Before You Read, Swahili is: 
- **Base-10 (decimal)**
- **Multiplicative in higher units**
- **Additive within compounds**
- **Non-subtractive**
- **Partially agreement-sensitive (1–5)**
- **Lexically influenced by Arabic and European loans**

Swahili combines Bantu noun-class agreement with borrowed decade lexicon.
""")

st.divider()

# --------------------------------------------------
# Basic Digits
# --------------------------------------------------

st.header("Basic Digits (0–10)")

st.table({
    "Number": ["0","1","2","3","4","5","6","7","8","9","10"],
    "Form": [
        "sifuri",
        "moja",
        "mbili",
        "tatu",
        "nne",
        "tano",
        "sita",
        "saba",
        "nane",
        "tisa",
        "kumi"
    ]
})

st.markdown("""
Swahili is written in the Latin alphabet.
Historically, it was also written in Arabic script (Ajami).
""")

st.markdown("#### Bases")

st.table({
    "Value": [
        "20","30","40","50","60","70","80","90",
        "100","1,000","1,000,000","1,000,000,000"
    ],
    "Form": [
        "ishirini","thelathini","arobaini","hamsini",
        "sitini","sabini","themanini","tisini",
        "mia","elfu","milioni","bilioni"
    ],
    "Structure": [
        "Lexical decade (Arabic origin)",
        "Lexical decade (Arabic origin)",
        "Lexical decade (Arabic origin)",
        "Lexical decade (Arabic origin)",
        "Lexical decade (Arabic origin)",
        "Lexical decade (Arabic origin)",
        "Lexical decade (Arabic origin)",
        "Lexical decade (Arabic origin)",
        "mia + digit",
        "elfu + digit",
        "European loan (magnitude noun)",
        "European loan (magnitude noun)"
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
Base noun + Digit
""")

st.code("""
100  = mia moja
200  = mia mbili
300  = mia tatu

1,000  = elfu moja
2,000  = elfu mbili

1,000,000 = milioni moja
2,000,000 = milioni mbili
""", language="text")

st.markdown("""
Decades (20–90) are lexical items of Arabic origin and are not transparently compositional in modern Swahili.
""")

# --------------------------------------------------
# Additive
# --------------------------------------------------

st.markdown("#### Additive Structure")

st.markdown("""
Compound numbers use the conjunction “na”.
""")

st.markdown("""
**General form:**
[Higher unit] + na + [Lower unit]
""")

st.code("""
21   = ishirini na moja
32   = thelathini na mbili
105  = mia moja na tano

1,234
= elfu moja mia mbili thelathini na nne
""", language="text")

st.markdown("""
“na” links the final smaller component within compound numbers.
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
Modern Swahili uses the Latin alphabet.
Arabic numerals (0–9) are standard in writing.
""")

st.markdown("#### Zero")

st.markdown("""
sifuri — loan from Arabic ṣifr.

Used in mathematics and administrative contexts.
""")

st.divider()

# --------------------------------------------------
# Special Syntactic Cases
# --------------------------------------------------

st.header("Special Syntactic Cases")

st.markdown("""
### Noun–Numeral Order

Standard structure:
Noun + Numeral
""")

st.markdown("""
Example:

vitabu vitatu  
(books three)
""")

st.markdown("""
### Numeral–Noun Agreement (1–5)

Numerals 1–5 show noun-class agreement.
""")

st.code("""
Class 7/8:
kitabu kimoja
vitabu viwili

Class 1/2:
mtu mmoja
watu wawili
""", language="text")

st.markdown("""
Numerals 6–9 and higher units generally remain invariant.
""")

st.markdown("""
### Conjunction Placement

“na” appears before the final unit component in compound numbers.
""")

st.markdown("""
### Independent vs. Attributive Use

Counting in isolation:
moja, mbili, tatu

Attributive usage triggers agreement:
kitabu kimoja
""")

st.divider()

# --------------------------------------------------
# Morphology & Inflection
# --------------------------------------------------

st.header("Morphology & Inflection")

st.markdown("""
Inflection: **Present (limited)**

Numerals 1–5 agree with noun classes.
Agreement prefixes vary according to class.
""")

st.markdown("#### Agreement Pattern")

st.code("""
1  = -moja
2  = -wili
3  = -tatu
4  = -nne
5  = -tano
""", language="text")

st.markdown("""
Agreement prefix changes by noun class:

wawili  
viwili  
miwili  
mawili
""")

st.markdown("""
Numerals 6–9, tens, and higher magnitudes are typically invariable.
""")

st.markdown("#### Ordinal Formation")

st.markdown("""
Ordinals are formed analytically.
""")

st.code("""
kwanza       (first)
siku ya pili (second day)
""", language="text")

st.markdown("""
General structure:
Noun + (agreement particle) + ordinal form
""")
# --------------------------------------------------
# Navigation
# --------------------------------------------------

st.markdown("---")
st.markdown("### Navigation")

col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/Swahili_Converter.py", label="Converter")

with col2:
    st.page_link("pages/Swahili_Linguistics.py", label="Linguistics")