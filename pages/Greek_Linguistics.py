import streamlit as st
from ui import apply_global_styles

st.set_page_config(page_title="Greek Numerals — Linguistics", layout="centered")

apply_global_styles()


st.title("Greek Numerals — Linguistic Structure (Modern Greek)")

st.markdown("""
The Modern Greek numeral system is fully integrated into the language’s inflectional grammar.

It is:
- **Base-10 (decimal)**
- **Multiplicative–additive**
- **Non-subtractive**
- **Gender-sensitive**
- **Case-inflecting**
- **Morphologically integrated**
""")

st.divider()

# --------------------------------------------------
# Basic Digits
# --------------------------------------------------

st.header("Basic Digits (0–10)")

st.table({
    "Number": ["0","1","2","3","4","5","6","7","8","9","10"],
    "Form": [
        "μηδέν",
        "ένας / μία / ένα",
        "δύο",
        "τρία",
        "τέσσερα",
        "πέντε",
        "έξι",
        "επτά",
        "οκτώ",
        "εννέα",
        "δέκα"
    ]
})

st.markdown("""
The numeral “1” inflects for gender:

Masculine: ένας  
Feminine: μία  
Neuter: ένα
""")

st.markdown("#### 11–19")

st.table({
    "Number": ["11","12","13","14","15","16","17","18","19"],
    "Form": [
        "έντεκα",
        "δώδεκα",
        "δεκατρία",
        "δεκατέσσερα",
        "δεκαπέντε",
        "δεκαέξι",
        "δεκαεπτά",
        "δεκαοκτώ",
        "δεκαεννέα"
    ]
})

st.markdown("""
General pattern:
δεκα- (10) + unit  

Exceptions:
11 (έντεκα) and 12 (δώδεκα) are historically contracted forms.
""")

st.markdown("#### Tens")

st.table({
    "Value": ["20","30","40","50","60","70","80","90"],
    "Form": [
        "είκοσι",
        "τριάντα",
        "σαράντα",
        "πενήντα",
        "εξήντα",
        "εβδομήντα",
        "ογδόντα",
        "ενενήντα"
    ]
})

st.markdown("""
All decades are lexicalized forms.
""")

st.markdown("#### Hundreds and Higher")

st.table({
    "Value": ["100","200","300","1,000","1,000,000"],
    "Form": [
        "εκατό(ν)",
        "διακόσια",
        "τριακόσια",
        "χίλια",
        "ένα εκατομμύριο"
    ],
    "Structure": [
        "Independent base",
        "Digit stem + -κόσια",
        "Digit stem + -κόσια",
        "Plural noun form",
        "Lexical noun"
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
**Inflectional Agreement:** Present
""")

# --------------------------------------------------
# Teens
# --------------------------------------------------

st.markdown("#### 11–19 Formation")

st.markdown("""
**General form:**
δεκα + unit
""")

st.code("""
16 = δεκαέξι
19 = δεκαεννέα
""", language="text")

# --------------------------------------------------
# Tens + Units
# --------------------------------------------------

st.markdown("#### Tens + Units (Additive)")

st.markdown("""
**General form:**
[Tens] + [Unit]
""")

st.code("""
21 = είκοσι ένα
32 = τριάντα δύο
""", language="text")

st.markdown("""
No conjunction equivalent to English “and” is used.
""")

# --------------------------------------------------
# Hundreds
# --------------------------------------------------

st.markdown("#### Hundreds")

st.markdown("""
**General form:**
[Digit stem] + -κόσια
""")

st.code("""
300 = τριακόσια
580 = πεντακόσια ογδόντα
""", language="text")

st.markdown("""
Hundreds behave as neuter plural forms when standalone.
""")

# --------------------------------------------------
# Thousands and Millions
# --------------------------------------------------

st.markdown("#### Thousands and Millions")

st.markdown("""
**General form:**
[Thousands] + [Hundreds] + [Tens] + [Units]
""")

st.code("""
1,234
= χίλια διακόσια τριάντα τέσσερα
""", language="text")

st.markdown("""
Millions behave as lexical nouns and require agreement:
""")

st.code("""
1,000,000 = ένα εκατομμύριο
2,000,000 = δύο εκατομμύρια
""", language="text")

st.divider()

# --------------------------------------------------
# Special Characters (Historical Layer)
# --------------------------------------------------

st.header("Special Characters (Historical Alphabetic Numerals)")

st.markdown("""
Greek historically used alphabetic numerals:

αʹ = 1  
βʹ = 2  
ιʹ = 10  
κʹ = 20  
ρʹ = 100
""")

st.markdown("""
Thousands marked with left keraia:

͵α = 1000
""")

st.markdown("""
These survive in church, legal, and chapter numbering contexts.
""")

st.markdown("#### Zero")

st.markdown("""
Modern zero:
μηδέν
""")

st.divider()

# --------------------------------------------------
# Special Syntactic Cases
# --------------------------------------------------

st.header("Special Syntactic Cases")

st.markdown("""
### Gender Agreement

“1” agrees with noun gender:

ένας άντρας  
μία γυναίκα  
ένα παιδί
""")

st.markdown("""
Hundreds also inflect:
""")

st.code("""
διακόσιοι άντρες
διακόσιες γυναίκες
διακόσια παιδιά
""", language="text")

st.markdown("""
### Plural Noun Interaction

After numerals greater than 1, nouns appear in nominative plural:

δύο βιβλία  
πέντε άντρες
""")

st.markdown("""
### Ordinals
""")

st.code("""
πρώτος
δεύτερος
τρίτος
τέταρτος
πέμπτος
""", language="text")

st.markdown("""
Ordinals decline fully for gender, number, and case.
""")

st.markdown("""
### Case Inflection

Numerals decline in formal contexts:

του ενός  
των δύο
""")

st.divider()

# --------------------------------------------------
# Morphology & Inflection
# --------------------------------------------------

st.header("Morphology & Inflection")

st.markdown("""
Cardinals:
• Gender agreement (notably with 1)  
• Hundreds inflect  
• Large magnitudes behave as nouns  

Greek numerals integrate into the full inflectional system.
""")

st.markdown("""
In compound numerals, agreement typically appears on the final element:

διακόσια τριάντα τρία βιβλία
""")

st.divider()

# --------------------------------------------------
# Navigation
# --------------------------------------------------

st.markdown("---")
st.markdown("### Navigation")

col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/Greek_Converter.py", label="Converter")

with col2:
    st.page_link("pages/Greek_Linguistics.py", label="Linguistics")