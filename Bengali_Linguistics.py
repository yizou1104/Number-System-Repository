import streamlit as st

st.set_page_config(page_title="Bengali Numerals — Linguistics", layout="centered")

st.title("Bengali Numerals — Linguistic Structure")

st.markdown("""
The Bengali numeral system is decimal but internally irregular below 100.

Before you read, Bengali is:
- **Base-10 (decimal)**
- **Highly lexicalized from 1–99**
- **Multiplicative–additive from 100 upward**
- **Non-subtractive (in modern usage)**
- **Lakh–koti structured**
- **Classifier-integrated**
- **Written in Eastern Nagari script**
""")

st.divider()

# --------------------------------------------------
# Basic Digits
# --------------------------------------------------

st.header("Basic Digits (0–10)")

st.table({
    "Number": ["0","1","2","3","4","5","6","7","8","9","10"],
    "Glyph": ["০","১","২","৩","৪","৫","৬","৭","৮","৯","১০"],
    "Form": [
        "শূন্য",
        "এক",
        "দুই",
        "তিন",
        "চার",
        "পাঁচ",
        "ছয়",
        "সাত",
        "আট",
        "নয়",
        "দশ"
    ]
})

st.markdown("""
Bengali uses Eastern Nagari numeral glyphs, distinct from Devanagari but historically related.
Arabic numerals are common in modern usage.
""")

st.markdown("#### Irregular 11–19")

st.table({
    "Number": ["11","12","13","14","15","16","17","18","19"],
    "Form": [
        "এগারো","বারো","তেরো","চৌদ্দ",
        "পনেরো","ষোলো","সতেরো","আঠারো","উনিশ"
    ]
})

st.markdown("""
Forms from 11–19 are lexical and synchronically opaque.
""")

st.markdown("#### Tens")

st.table({
    "Value": ["20","30","40","50","60","70","80","90"],
    "Form": [
        "বিশ","ত্রিশ","চল্লিশ","পঞ্চাশ",
        "ষাট","সত্তর","আশি","নব্বই"
    ]
})

st.markdown("""
All decades are lexicalized; they are not transparently “digit × 10”.
""")

st.markdown("#### Higher Bases")

st.table({
    "Value": ["100","1,000","100,000","10,000,000","1,000,000,000"],
    "Form": [
        "একশো / এক শত",
        "হাজার",
        "লাখ",
        "কোটি",
        "বিলিয়ন"
    ],
    "Structure": [
        "Independent hundred unit",
        "Independent thousand unit",
        "10⁵ pivot (Indian grouping)",
        "10⁷ pivot",
        "Western million-based unit"
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
**Subtractive Formation:** Not productive
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
21 = একুশ
24 = চব্বিশ
25 = পঁচিশ
29 = উনত্রিশ
""", language="text")

st.markdown("""
Characteristic patterns include:

• Consonant gemination  
• Nasalization  
• Prefix “উন-” in certain decades  
• Internal vowel alternations  

These are historically derived but not synchronically productive rules.
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
125 = একশো পঁচিশ
300 = তিনশো

5,432
= পাঁচ হাজার চারশো বত্রিশ
""", language="text")

st.markdown("""
Lakhs and crores follow Indian grouping:
""")

st.code("""
1,23,45,678
= ১ কোটি ২৩ লাখ ৪৫ হাজার ৬৭৮
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
Forms such as “উনিশ” historically meant “one less than twenty,”
but subtraction is not productive in modern Bengali.
""")

st.divider()

# --------------------------------------------------
# Special Characters
# --------------------------------------------------

st.header("Special Characters")

st.markdown("""
Bengali numeral glyphs:

০ ১ ২ ৩ ৪ ৫ ৬ ৭ ৮ ৯
""")

st.markdown("#### Zero")

st.markdown("""
শূন্য — Sanskrit origin.

Used in mathematics, administration, and finance.
""")

st.markdown("""
Indian digit grouping is used:

1,00,000  
1,00,00,000
""")

st.divider()

# --------------------------------------------------
# Special Syntactic Cases
# --------------------------------------------------

st.header("Special Syntactic Cases")

st.markdown("""
### Agreement

Bengali lacks grammatical gender.
Cardinal numerals are invariant.
Plural marking often omitted after numerals.
""")

st.code("""
তিন বই
""", language="text")

st.markdown("""
### Classifier System

Bengali commonly uses classifiers.
""")

st.code("""
একটা বই
দুটো বই
দুটি বই (formal)
""", language="text")

st.markdown("""
Classifier fusion produces morphophonemic variation:
""")

st.code("""
দুই + টা → দুটো
এক + টা → একটা
""", language="text")

st.markdown("""
### Ordinals
""")

st.code("""
প্রথম
দ্বিতীয়
তৃতীয়
পঞ্চম
ষষ্ঠ
""", language="text")

st.markdown("""
Written abbreviations:
১ম, ২য়
""")

st.markdown("""
### Compound Number Order

Descending magnitude order:

[Crore] + [Lakh] + [Thousand] + [Hundred] + [1–99]

No internal conjunction equivalent to English “and”.
""")

st.divider()

# --------------------------------------------------
# Morphology & Inflection
# --------------------------------------------------

st.header("Morphology & Inflection")

st.markdown("""
Cardinals:

• Invariant  
• No gender marking  
• No case marking  
• No agreement morphology  

Noun plurality handled independently.
""")

st.markdown("""
Ordinals:

• Often Sanskrit-derived adjectival forms  
• No gender inflection (Bengali lacks grammatical gender)
""")

st.markdown("""
Classifier interaction produces morphophonemic contraction in colloquial speech.
""")

st.divider()

# --------------------------------------------------
# Navigation
# --------------------------------------------------

st.markdown("---")
st.markdown("### Navigation")

col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/Bengali_Converter.py", label="Converter")

with col2:
    st.page_link("pages/Bengali_Linguistics.py", label="Linguistics")