import streamlit as st
from ui import apply_global_styles

# ============================================================
# BENGALI NUMERAL SYSTEM
# Bidirectional: Arabic ↔ Bengali (Digits, Words, Romanized)
# Based on: https://en.wikipedia.org/wiki/Bengali_numerals
# ============================================================

# ------------------------------------------------------------
# 1. ATOMIC NUMERALS (0–99) – Bengali words + Romanized
# ------------------------------------------------------------
BENGALI_ATOMS = {
    0: "শূন্য",
    1: "এক",
    2: "দুই",
    3: "তিন",
    4: "চার",
    5: "পাঁচ",
    6: "ছয়",
    7: "সাত",
    8: "আট",
    9: "নয়",
    10: "দশ",
    11: "এগারো",
    12: "বারো",
    13: "तेरो",
    14: "চৌদ্দ",
    15: "পনেরো",
    16: "ষোলো",
    17: "সতেরো",
    18: "আঠারো",
    19: "ঊনিশ",
    20: "বিশ",
    21: "একুশ",
    30: "ত্রিশ",
    40: "চল্লিশ",
    50: "পঞ্চাশ",
    60: "ষাট",
    70: "সত্তর",
    80: "আশি",
    90: "নব্বই",
}

ROMANIZED_ATOMS = {
    0: "shunnô",
    1: "æk",
    2: "dui",
    3: "tin",
    4: "char",
    5: "pãch",
    6: "chhôy",
    7: "shat",
    8: "aṭ",
    9: "nôy",
    10: "dôsh",
    11: "ægaro",
    12: "baro",
    13: "tero",
    14: "choddô",
    15: "pônero",
    16: "sholo",
    17: "shôtero",
    18: "aṭharo",
    19: "unish",
    20: "bish",
    21: "ekush",
    30: "trish",
    40: "chôllish",
    50: "pônchash",
    60: "shaṭ",
    70: "shôttôr",
    80: "ashi",
    90: "nôbbôi",
}

# Reverse mappings for parsing
BENGALI_VALUES = {v: k for k, v in BENGALI_ATOMS.items()}
ROMANIZED_VALUES = {v: k for k, v in ROMANIZED_ATOMS.items()}

# ------------------------------------------------------------
# 2. BASE UNITS (Indian numbering system) – Bengali + Romanized
# ------------------------------------------------------------
BASE_UNITS = [
    ("কোটি", "koṭi", 10_000_000),
    ("লাখ", "lakh", 100_000),
    ("হাজার", "hajar", 1_000),
    ("শত", "shôtô", 100),
]

# Value maps for parsing
BENGALI_BASE_VALUES = {beng: value for beng, roman, value in BASE_UNITS}
ROMANIZED_BASE_VALUES = {roman: value for _, roman, value in BASE_UNITS}

# Special entries for common forms
BENGALI_BASE_VALUES["একশ"] = 100
ROMANIZED_BASE_VALUES["ækshô"] = 100

# ------------------------------------------------------------
# 3. ARABIC → BENGALI
# ------------------------------------------------------------
def number_to_bengali_digits(n: int) -> str:
    """Convert integer to Bengali script digits."""
    trans = str.maketrans("0123456789", "০১২৩৪৫৬৭৮৯")
    return str(n).translate(trans)

def number_to_bengali_words(n: int, romanized: bool = False) -> str:
    """Convert integer to Bengali words (Bengali script if romanized=False, else romanized)."""
    if n < 0:
        raise ValueError("Negative numbers are not supported")
    if n == 0:
        return (ROMANIZED_ATOMS[0] if romanized else BENGALI_ATOMS[0])

    atom_map = ROMANIZED_ATOMS if romanized else BENGALI_ATOMS

    if n <= 99 and n in atom_map:
        return atom_map[n]

    # Special handling for 100-199 (use "একশ" / "ækshô" for 101-199, "একশ" / "ækshô" for 100)
    if 100 <= n < 200:
        if n == 100:
            return ("ækshô" if romanized else "একশ")
        else:
            one = ("æk" if romanized else "এক")
            hundred = ("shôtô" if romanized else "শত")  # "একশ" already used for 100
            # But for 101, common is "একশ এক" (not "এক শত এক") – use "ækshô" for romanized as well
            if romanized:
                hundred = "ækshô"
            else:
                hundred = "একশ"
            remainder = number_to_bengali_words(n - 100, romanized)
            return f"{one} {hundred} {remainder}" if remainder else f"{one} {hundred}"

    # General case: split by largest base unit
    for beng, roman, value in BASE_UNITS:
        if n >= value:
            quotient = n // value
            remainder = n % value
            unit_name = roman if romanized else beng
            if quotient == 1:
                # For thousand and above, include "এক" / "æk"
                if value >= 1000:
                    one = ("æk" if romanized else "এক")
                    prefix = f"{one} {unit_name}"
                else:
                    prefix = unit_name  # e.g., "শত" for 100 (but 100 already handled)
            else:
                prefix = number_to_bengali_words(quotient, romanized) + " " + unit_name
            if remainder == 0:
                return prefix
            else:
                return prefix + " " + number_to_bengali_words(remainder, romanized)

    return ""  # never reached

# ------------------------------------------------------------
# 4. BENGALI → ARABIC
# ------------------------------------------------------------
def bengali_digits_to_number(text: str) -> int:
    """Convert Bengali digit string to integer."""
    cleaned = text.strip().replace(" ", "")
    trans = str.maketrans("০১২৩৪৫৬৭৮৯", "0123456789")
    arabic_str = cleaned.translate(trans)
    try:
        return int(arabic_str)
    except ValueError:
        raise ValueError("Invalid Bengali digit sequence")

def _parse_words(tokens, value_map, base_map):
    """Generic parser for word-based numerals (Bengali or Romanized)."""
    if not tokens:
        return None

    full = " ".join(tokens)
    if full in value_map:
        return value_map[full]

    # Try largest base unit first
    for base_word, base_value in sorted(base_map.items(), key=lambda x: -x[1]):
        if base_word in tokens:
            idx = tokens.index(base_word)
            left_tokens = tokens[:idx]
            right_tokens = tokens[idx + 1:]

            multiplier = 1
            if left_tokens:
                left_val = _parse_words(left_tokens, value_map, base_map)
                if left_val is None:
                    return None
                multiplier = left_val

            remainder = 0
            if right_tokens:
                rem_val = _parse_words(right_tokens, value_map, base_map)
                if rem_val is None:
                    return None
                remainder = rem_val

            return multiplier * base_value + remainder

    return None

def bengali_words_to_number(text: str) -> int:
    """Parse Bengali script words to integer."""
    tokens = text.strip().split()
    result = _parse_words(tokens, BENGALI_VALUES, BENGALI_BASE_VALUES)
    if result is None:
        raise ValueError("Invalid Bengali numeral")
    return result

def romanized_words_to_number(text: str) -> int:
    """Parse romanized Bengali words to integer."""
    tokens = text.strip().split()
    result = _parse_words(tokens, ROMANIZED_VALUES, ROMANIZED_BASE_VALUES)
    if result is None:
        raise ValueError("Invalid romanized Bengali numeral")
    return result

def bengali_to_number(text: str) -> int:
    """Convert Bengali representation (digits, Bengali words, or romanized words) to integer."""
    text = text.strip()
    if not text:
        raise ValueError("Empty input")

    # Check if it's Bengali digits (০-৯)
    bengali_digits = set("০১২৩৪৫৬৭৮৯")
    if all(ch in bengali_digits or ch.isspace() for ch in text):
        return bengali_digits_to_number(text)

    # Check if it contains Bengali characters (Unicode range for Bengali)
    if any('\u0980' <= ch <= '\u09FF' for ch in text):
        return bengali_words_to_number(text)

    # Otherwise try romanized
    return romanized_words_to_number(text)

# ============================================================
# STREAMLIT INTERFACE
# ============================================================

st.set_page_config(
    page_title="Bengali Numeral Converter",
    layout="centered"
)

apply_global_styles()


st.title("Bengali Numeral Converter")
st.write(
    "Convert between **Arabic numerals** and **Bengali representations**: "
    "Bengali script digits, Bengali words, and romanized words."
)

st.markdown("---")

# ------------------------------------------------------------
# Direction selector
# ------------------------------------------------------------
direction = st.radio(
    "Choose conversion direction:",
    ["Arabic → Bengali", "Bengali → Arabic"],
    horizontal=True
)

st.markdown("---")

# ------------------------------------------------------------
# Preset examples
# ------------------------------------------------------------
st.subheader("Preset Examples")

arabic_presets = [0, 5, 12, 21, 100, 325, 12345, 10000000]
bengali_presets = [
    "শূন্য",
    "পাঁচ",
    "বারো",
    "একুশ",
    "একশ",
    "তিনশ পঁচিশ",
    "বারো হাজার তিনশ পঁয়তাল্লিশ",
    "এক কোটি",
]
romanized_presets = [
    "shunnô",
    "pãch",
    "baro",
    "ekush",
    "ækshô",
    "tin shô pônchish",
    "baro hajar tin shô põytallish",
    "æk koṭi",
]

cols = st.columns(4)

if direction == "Arabic → Bengali":
    for i, num in enumerate(arabic_presets):
        if cols[i % 4].button(str(num)):
            st.session_state["arabic_input"] = str(num)
else:
    combined_presets = bengali_presets + romanized_presets
    for i, txt in enumerate(combined_presets):
        if cols[i % 4].button(txt, key=f"preset_{i}"):
            st.session_state["bengali_input"] = txt

st.markdown("---")

# ------------------------------------------------------------
# Input & conversion
# ------------------------------------------------------------
if direction == "Arabic → Bengali":
    arabic_input = st.text_input(
        "Enter an Arabic numeral:",
        key="arabic_input",
        placeholder="e.g. 325"
    )

    if arabic_input:
        if arabic_input.lstrip('-').isdigit():
            try:
                n = int(arabic_input)
                digits = number_to_bengali_digits(n)
                bengali_words = number_to_bengali_words(n, romanized=False)
                roman_words = number_to_bengali_words(n, romanized=True)
                st.success(
                    f"**Bengali digits:** {digits}\n\n"
                    f"**Bengali words:** {bengali_words}\n\n"
                    f"**Romanized words:** {roman_words}"
                )
            except Exception as e:
                st.error(str(e))
        else:
            st.error("Please enter a valid integer.")

else:  # Bengali → Arabic
    bengali_input = st.text_input(
        "Enter a Bengali numeral (digits, Bengali words, or romanized words):",
        key="bengali_input",
        placeholder="e.g. তিনশ পঁচিশ or ৩২৫ or tin shô pônchish"
    )

    if bengali_input:
        try:
            result = bengali_to_number(bengali_input)
            st.success(str(result))
        except Exception as e:
            st.error(str(e))

st.markdown("---")
st.caption(
    "Implements the Indian numbering system (lakhs, crores) with standard Bengali number names. "
    "Supports Bengali digits (০-৯), Bengali words, and romanized words. "
    "Data sourced from Wikipedia: [Bengali numerals](https://en.wikipedia.org/wiki/Bengali_numerals). "
    "Converter algorithm created by Yi Zou. "
    "Grammar explained in the Linguistics section."
)

# ------------------------------------------------------------
# Related Pages Navigation
# ------------------------------------------------------------
st.markdown("---")
st.subheader("Explore More")

nav_cols = st.columns(2)

with nav_cols[0]:
    st.page_link(
        "pages/Bengali_Linguistics.py",
        label="Linguistics",
        help="Structure, grammar, and historical development of the Bengali numeral system"
    )

with nav_cols[1]:
    st.page_link(
        "pages/Bengali_Converter.py",
        label="Converter",
        help="Return to the numeral converter"
    )
