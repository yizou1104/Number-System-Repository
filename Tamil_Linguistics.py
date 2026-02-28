import streamlit as st

st.set_page_config(page_title="Tamil Numerals — Linguistics", layout="centered")

st.title("Tamil Numerals — Linguistic Structure")

st.markdown("""
The Tamil numeral system is decimal with extensive morphophonemic alternation.

It is:
- **Base-10 (decimal)**
- **Multiplicative–additive**
- **Non-subtractive**
- **Morphophonemically conditioned**
- **Linker-dependent in compound formation**
- **Written in a distinct Tamil numeral script**
""")

st.divider()

# --------------------------------------------------
# Basic Digits
# --------------------------------------------------

st.header("Basic Digits (0–10)")

st.table({
    "Number": ["0","1","2","3","4","5","6","7","8","9","10"],
    "Glyph": ["௦","௧","௨","௩","௪","௫","௬","௭","௮","௯","௰"],
    "Form": [
        "பூஜ்யம் / சுழியம்",
        "ஒன்று",
        "இரண்டு",
        "மூன்று",
        "நான்கு",
        "ஐந்து",
        "ஆறு",
        "ஏழு",
        "எட்டு",
        "ஒன்பது",
        "பத்து"
    ]
})

st.markdown("""
Tamil possesses dedicated glyphs for 10 (௰), 100 (௱), and 1000 (௲) in addition to digits 0–9.
""")

st.markdown("#### 11–19")

st.table({
    "Number": ["11","12","13","14","15","16","17","18","19"],
    "Form": [
        "பதினொன்று",
        "பன்னிரண்டு",
        "பதிமூன்று",
        "பதினான்கு",
        "பதினைந்து",
        "பதினாறு",
        "பதினேழு",
        "பதினெட்டு",
        "பத்தொன்பது"
    ]
})

st.markdown("""
These forms show sandhi and gemination driven by the prefix derived from “ten” (பதி-).
""")

st.markdown("#### Tens")

st.table({
    "Value": ["20","30","40","50","60","70","80","90"],
    "Form": [
        "இருபது",
        "முப்பது",
        "நாற்பது",
        "ஐம்பது",
        "அறுபது",
        "எழுபது",
        "எண்பது",
        "தொண்ணூறு"
    ]
})

st.markdown("""
Tens involve stem reduction and consonant assimilation.
""")

st.markdown("#### Higher Bases")

st.table({
    "Value": ["100","1,000","10,000","100,000","10,000,000"],
    "Form": [
        "நூறு",
        "ஆயிரம்",
        "பத்தாயிரம்",
        "இலட்சம்",
        "கோடி"
    ],
    "Structure": [
        "Independent hundred unit",
        "Independent thousand unit",
        "10 × 1,000",
        "Indic lakh (10⁵)",
        "Indic crore (10⁷)"
    ]
})

st.divider()

# --------------------------------------------------
# Structure
# --------------------------------------------------

st.header("Structure")

st.markdown("""
**Primary Base:** 10  
**System Type:** Multiplicative–Additive  
**Subtractive Formation:** Absent  
**Morphophonemic Alternation:** Extensive
""")

# --------------------------------------------------
# Tens Formation
# --------------------------------------------------

st.markdown("#### Tens Formation")

st.markdown("""
**General form:**
[Digit stem] + பது (patu, “ten”)
""")

st.code("""
20 = இருபது
30 = முப்பது
50 = ஐம்பது
80 = எண்பது
""", language="text")

st.markdown("""
Digit stems undergo predictable alternation:

மூன்று → முப்-  
ஐந்து → ஐம்-  
எட்டு → எண்-
""")

# --------------------------------------------------
# Compound Numbers
# --------------------------------------------------

st.markdown("#### Compound Numbers (Additive)")

st.markdown("""
**General form:**
[Tens] + [Linker] + [Unit]
""")

st.code("""
21 = இருபத்து ஒன்று
35 = முப்பத்து ஐந்து
""", language="text")

st.markdown("""
Linking suffix:
-த்து (-ttu)
""")

# --------------------------------------------------
# Hundreds
# --------------------------------------------------

st.markdown("#### Hundreds")

st.markdown("""
**General form:**
[Digit stem] + நூறு
""")

st.code("""
300 = முன்னூறு
500 = ஐந்நூறு
""", language="text")

st.markdown("""
Gemination and nasal insertion occur during combination.
""")

# --------------------------------------------------
# Thousands and Higher
# --------------------------------------------------

st.markdown("#### Thousands and Higher")

st.markdown("""
**General form:**
[Higher unit] + [Linker] + [Lower unit]
""")

st.code("""
1,234
= ஆயிரத்து இருநூற்று முப்பத்து நான்கு
""", language="text")

st.markdown("""
Linkers:
-த்து (-ttu)
-ற்று (-ṟṟu)
""")

# --------------------------------------------------
# Subtractive
# --------------------------------------------------

st.markdown("#### Subtractive Structure")

st.markdown("""
Tamil does not productively form numbers via subtraction.

19 is structurally “ten + nine,” though phonologically merged.
""")

st.divider()

# --------------------------------------------------
# Special Characters
# --------------------------------------------------

st.header("Special Characters")

st.markdown("""
Tamil numeral glyphs:

௦ ௧ ௨ ௩ ௪ ௫ ௬ ௭ ௮ ௯  
௰ (10)  
௱ (100)  
௲ (1000)
""")

st.markdown("""
Example of classical notation:

௲௱௰௧  = 1111
""")

st.markdown("#### Zero")

st.markdown("""
Modern zero terms:

பூஜ்யம் (Sanskrit origin)  
சுழியம் (“circle”)
""")

st.divider()

# --------------------------------------------------
# Special Syntactic Cases
# --------------------------------------------------

st.header("Special Syntactic Cases")

st.markdown("""
### Linking Morphemes

Compound numerals require overt linking suffixes:

-த்து (-ttu)  
-ற்று (-ṟṟu)
""")

st.markdown("""
### Attributive “One”

Standalone:
ஒன்று  

Before noun:
ஒரு புத்தகம்
""")

st.markdown("""
### Classifier Interaction

Tamil does not use a productive classifier system,
though optional measure words may appear.
""")

st.markdown("""
### Ordinals
""")

st.code("""
முதல்
இரண்டாம்
மூன்றாம்
நான்காம்
""", language="text")

st.markdown("""
Suffix:
-ஆம் (-ām) attaches productively from 2 onward.
""")

st.divider()

# --------------------------------------------------
# Morphology & Inflection
# --------------------------------------------------

st.header("Morphology & Inflection")

st.markdown("""
Cardinals:
• No gender marking  
• No case marking on numeral  
• Noun carries grammatical marking  

Plural marking may appear on noun even after numeral.
""")

st.code("""
மூன்று புத்தகங்கள்
""", language="text")

st.markdown("""
Systematic morphophonemic alternations include:

மூன்று → முன்-/முப்-  
ஐந்து → ஐம்-  
Consonant doubling in compound forms
""")

st.divider()

# --------------------------------------------------
# Navigation
# --------------------------------------------------

st.markdown("---")
st.markdown("### Navigation")

col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/Tamil_Converter.py", label="Converter")

with col2:
    st.page_link("pages/Tamil_Linguistics.py", label="Linguistics")

with col3:
    st.page_link("pages/Tamil_Olympiad_Problems.py", label="Olympiad Problems")