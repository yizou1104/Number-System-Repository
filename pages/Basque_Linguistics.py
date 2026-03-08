import streamlit as st
from ui import apply_global_styles

st.set_page_config(page_title="Basque Numerals — Linguistics", layout="centered")

apply_global_styles()


st.title("Basque Numerals — Linguistic Structure")

st.markdown("""
The Basque numeral system is one of the few fully productive vigesimal systems in Europe.

It is:
- **Primarily base-20 (vigesimal)**
- **Multiplicative–additive**
- **Non-subtractive**
- **Morphophonemically conditioned**
- **Case-marked at the noun phrase level**
- **Gender-neutral**
""")

st.divider()

# --------------------------------------------------
# Basic Digits
# --------------------------------------------------

st.header("Basic Digits (0–10)")

st.table({
    "Number": ["0","1","2","3","4","5","6","7","8","9","10"],
    "Form": [
        "zero",
        "bat",
        "bi",
        "hiru",
        "lau",
        "bost",
        "sei",
        "zazpi",
        "zortzi",
        "bederatzi",
        "hamar"
    ]
})

st.markdown("""
Basque uses the Latin script.  
There are no indigenous numeral glyphs distinct from Latin digits.
""")

st.markdown("#### 11–19")

st.table({
    "Number": ["11","12","13","14","15","16","17","18","19"],
    "Form": [
        "hamaika",
        "hamabi",
        "hamahiru",
        "hamalau",
        "hamabost",
        "hamasei",
        "hamazazpi",
        "hemezortzi",
        "hemeretzi"
    ]
})

st.markdown("""
General pattern:
hamar (10) + unit  

Several forms show phonological contraction.
""")

st.markdown("#### Core Vigesimal Bases")

st.table({
    "Value": ["20","40","60","80","100"],
    "Form": [
        "hogei",
        "berrogei",
        "hirurogei",
        "laurogei",
        "ehun"
    ],
    "Structure": [
        "Base unit",
        "2 × 20",
        "3 × 20",
        "4 × 20",
        "Decimal pivot"
    ]
})

st.divider()

# --------------------------------------------------
# Structure
# --------------------------------------------------

st.header("Structure")

st.markdown("""
**Primary Base:** 20  
**Secondary Layer:** Decimal (100+)  
**System Type:** Multiplicative–Additive  
**Subtractive Formation:** Absent
""")

# --------------------------------------------------
# Vigesimal Multiplication
# --------------------------------------------------

st.markdown("#### Vigesimal Multiplication")

st.markdown("""
**General form:**
[Multiplier stem] + rogei
""")

st.code("""
40 = berrogei
60 = hirurogei
80 = laurogei
""", language="text")

st.markdown("""
Digit stems undergo morphophonemic change:

bi → ber-  
hiru → hirur-  
lau → laur-
""")

# --------------------------------------------------
# Additive Structure
# --------------------------------------------------

st.markdown("#### Additive Structure (Within Scores)")

st.markdown("""
**General form:**
hogei + ta + unit
""")

st.code("""
21 = hogeita bat
37 = hogeita hamazazpi
""", language="text")

st.markdown("""
Connector:
-ta links vigesimal base to remainder.
""")

# --------------------------------------------------
# Above 40
# --------------------------------------------------

st.markdown("#### Structure Above 40")

st.markdown("""
**General form:**
[Score multiple] + ta + [remainder]
""")

st.code("""
50 = berrogeita hamar
67 = hirurogeita zazpi
90 = laurogeita hamar
""", language="text")

# --------------------------------------------------
# Hundreds and Above
# --------------------------------------------------

st.markdown("#### Hundreds and Above (Decimal Layer)")

st.markdown("""
**General form:**
[Digit stem] + rehun
""")

st.code("""
200 = berrehun
300 = hirurehun
400 = laurehun
""", language="text")

st.markdown("""
Connector between hundreds and remainder:
eta (“and”)
""")

st.code("""
256 = berrehun eta berrogeita hamasei
""", language="text")

st.divider()

# --------------------------------------------------
# Special Characters / Connectors
# --------------------------------------------------

st.header("Special Characters / Connectors")

st.markdown("""
Key connectors:

-ta  → links vigesimal base to remainder  
eta  → links hundreds to smaller units
""")

st.markdown("""
Zero:
zero (loanword)
""")

st.divider()

# --------------------------------------------------
# Special Syntactic Cases
# --------------------------------------------------

st.header("Special Syntactic Cases")

st.markdown("""
### Numeral–Noun Order

Numeral precedes noun:
""")

st.code("""
bi etxe
""", language="text")

st.markdown("""
### Plural Interaction

After numerals, noun typically remains singular:

bi etxe
""")

st.markdown("""
### Case Marking

Basque is ergative-absolutive.

Case suffix attaches to noun phrase, not numeral stem:
""")

st.code("""
bi etxetan
""", language="text")

st.markdown("""
### Ordinals
""")

st.code("""
lehen
bigarren
hirugarren
laugarren
bosgarren
""", language="text")

st.markdown("""
Productive suffix:
-garren
""")

st.divider()

# --------------------------------------------------
# Morphology & Inflection
# --------------------------------------------------

st.header("Morphology & Inflection")

st.markdown("""
Cardinals:
• No gender marking  
• Numerals invariable  
• Case marking applied to noun phrase  

Basque lacks grammatical gender.
""")

st.markdown("""
Morphophonemic alternation occurs in multiplication:

bi → ber-  
hiru → hirur-  
lau → laur-
""")

st.markdown("""
Collective loan form:
dozena (dozen)
""")

st.divider()

# --------------------------------------------------
# Navigation
# --------------------------------------------------

st.markdown("---")
st.markdown("### Navigation")

col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/Basque_Converter.py", label="Converter")

with col2:
    st.page_link("pages/Basque_Linguistics.py", label="Linguistics")