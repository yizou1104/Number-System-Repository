import streamlit as st

# ============================================================
# HINDI NUMERAL SYSTEM
# Bidirectional: Arabic ↔ Hindi (Devanagari digits, words, romanized)
# ============================================================

# ------------------------------------------------------------
# 1. ATOMIC NUMERALS (0–99) – Hindi words (Devanagari + Romanized)
# ------------------------------------------------------------
DEVANAGARI_ATOMS = {
    0: "शून्य",
    1: "एक",
    2: "दो",
    3: "तीन",
    4: "चार",
    5: "पाँच",
    6: "छह",
    7: "सात",
    8: "आठ",
    9: "नौ",
    10: "दस",
    11: "ग्यारह",
    12: "बारह",
    13: "तेरह",
    14: "चौदह",
    15: "पंद्रह",
    16: "सोलह",
    17: "सत्रह",
    18: "अठारह",
    19: "उन्नीस",
    20: "बीस",
    21: "इक्कीस",
    22: "बाईस",
    23: "तेईस",
    24: "चौबीस",
    25: "पच्चीस",
    26: "छब्बीस",
    27: "सत्ताईस",
    28: "अट्ठाईस",
    29: "उनतीस",
    30: "तीस",
    31: "इकतीस",
    32: "बत्तीस",
    33: "तैंतीस",
    34: "चौंतीस",
    35: "पैंतीस",
    36: "छत्तीस",
    37: "सैंतीस",
    38: "अड़तीस",
    39: "उनतालीस",
    40: "चालीस",
    41: "इकतालीस",
    42: "बयालीस",
    43: "तैंतालीस",
    44: "चौवालीस",
    45: "पैंतालीस",
    46: "छियालीस",
    47: "सैंतालीस",
    48: "अड़तालीस",
    49: "उनचास",
    50: "पचास",
    51: "इक्यावन",
    52: "बावन",
    53: "तिरेपन",
    54: "चौवन",
    55: "पचपन",
    56: "छप्पन",
    57: "सत्तावन",
    58: "अट्ठावन",
    59: "उनसठ",
    60: "साठ",
    61: "इकसठ",
    62: "बासठ",
    63: "तिरेसठ",
    64: "चौंसठ",
    65: "पैंसठ",
    66: "छियासठ",
    67: "सड़सठ",
    68: "अड़सठ",
    69: "उनहत्तर",
    70: "सत्तर",
    71: "इकहत्तर",
    72: "बहत्तर",
    73: "तिहत्तर",
    74: "चौहत्तर",
    75: "पचहत्तर",
    76: "छिहत्तर",
    77: "सतहत्तर",
    78: "अठहत्तर",
    79: "उनासी",
    80: "अस्सी",
    81: "इक्यासी",
    82: "बयासी",
    83: "तिरासी",
    84: "चौरासी",
    85: "पचासी",
    86: "छियासी",
    87: "सत्तासी",
    88: "अट्ठासी",
    89: "नवासी",
    90: "नब्बे",
    91: "इक्यानवे",
    92: "बानवे",
    93: "तिरानवे",
    94: "चौरानवे",
    95: "पंचानवे",
    96: "छियानवे",
    97: "सत्तानवे",
    98: "अट्ठानवे",
    99: "निन्यानवे",
}

ROMANIZED_ATOMS = {
    0: "shoonya",
    1: "ek",
    2: "do",
    3: "teen",
    4: "chaar",
    5: "paanch",
    6: "chhah",
    7: "saat",
    8: "aath",
    9: "nau",
    10: "das",
    11: "gyaarah",
    12: "baarah",
    13: "terah",
    14: "chaudah",
    15: "pandrah",
    16: "solah",
    17: "satrah",
    18: "athaarah",
    19: "unnees",
    20: "bees",
    21: "ikkees",
    22: "baaees",
    23: "teis",
    24: "chaubees",
    25: "pachchees",
    26: "chhabbees",
    27: "sattaais",
    28: "atthaais",
    29: "unatees",
    30: "tees",
    31: "ikatees",
    32: "batees",
    33: "taintees",
    34: "chauntees",
    35: "paiñtees",
    36: "chhattees",
    37: "saiñtees",
    38: "adatees",
    39: "unataalees",
    40: "chaalees",
    41: "ikataalees",
    42: "bayaalees",
    43: "taintaalees",
    44: "chauvaalees",
    45: "paiñtaalees",
    46: "chiyaalees",
    47: "saiñtaalees",
    48: "adataalees",
    49: "unachaas",
    50: "pachaas",
    51: "ikyaavan",
    52: "baavan",
    53: "tirepan",
    54: "chauvan",
    55: "pachapan",
    56: "chhappan",
    57: "sattaavan",
    58: "atthaavan",
    59: "unsath",
    60: "saath",
    61: "ikasath",
    62: "baasath",
    63: "tiresath",
    64: "chausath",
    65: "paiñsath",
    66: "chiyaasath",
    67: "sadasath",
    68: "adasath",
    69: "unahtarr",
    70: "sattar",
    71: "ikahtarr",
    72: "bahtarr",
    73: "tihtarr",
    74: "chauhtarr",
    75: "pachahtarr",
    76: "chhihtarr",
    77: "satahtarr",
    78: "athahtarr",
    79: "unaasee",
    80: "assee",
    81: "ikyaasee",
    82: "bayaasee",
    83: "tiraasee",
    84: "chauraasee",
    85: "pachaasee",
    86: "chiyaasee",
    87: "sattaasee",
    88: "atthaasee",
    89: "navaasee",
    90: "nabbe",
    91: "ikyaanave",
    92: "baanave",
    93: "tiraanave",
    94: "chauraanave",
    95: "panchaanave",
    96: "chiyaanave",
    97: "sattaanave",
    98: "atthaanave",
    99: "ninyaanave",
}

# Reverse mappings for parsing
DEVANAGARI_VALUES = {v: k for k, v in DEVANAGARI_ATOMS.items()}
ROMANIZED_VALUES = {v: k for k, v in ROMANIZED_ATOMS.items()}

# ------------------------------------------------------------
# 2. BASE UNITS (Indian numbering system)
# ------------------------------------------------------------
BASE_UNITS = [
    ("करोड़", "crore", 10_000_000),
    ("लाख", "lakh", 100_000),
    ("हज़ार", "hazaar", 1_000),
    ("सौ", "sau", 100),
]

# For conversion to words, we keep the list of tuples.
# For parsing, we need direct value maps.
DEVANAGARI_BASE_VALUES = {deva: value for deva, roman, value in BASE_UNITS}
ROMANIZED_BASE_VALUES = {roman: value for _, roman, value in BASE_UNITS}

# Special entry for "एक सौ" (100) – common alternative
DEVANAGARI_BASE_VALUES["एक सौ"] = 100
ROMANIZED_BASE_VALUES["ek sau"] = 100

# ------------------------------------------------------------
# 3. ARABIC → HINDI
# ------------------------------------------------------------
def number_to_hindi_digits(n: int) -> str:
    """Convert integer to Devanagari digits."""
    trans = str.maketrans("0123456789", "०१२३४५६७८९")
    return str(n).translate(trans)

def number_to_hindi_words(n: int, romanized: bool = False) -> str:
    """Convert integer to Hindi words (Devanagari if romanized=False, else romanized)."""
    if n < 0:
        raise ValueError("Negative numbers are not supported")
    if n == 0:
        return (ROMANIZED_ATOMS[0] if romanized else DEVANAGARI_ATOMS[0])

    atom_map = ROMANIZED_ATOMS if romanized else DEVANAGARI_ATOMS

    # Direct atomic (0-99)
    if n <= 99 and n in atom_map:
        return atom_map[n]

    # Special handling for 100-199 (use "एक सौ" for 101-199, "सौ" for 100)
    if 100 <= n < 200:
        if n == 100:
            return ("sau" if romanized else "सौ")
        else:
            one = ("ek" if romanized else "एक")
            hundred = ("sau" if romanized else "सौ")
            remainder = number_to_hindi_words(n - 100, romanized)
            return f"{one} {hundred} {remainder}"

    # General case: split by largest base unit
    for deva, roman, value in BASE_UNITS:
        if n >= value:
            quotient = n // value
            remainder = n % value
            unit_name = roman if romanized else deva
            if quotient == 1:
                # For thousand and above, we include "एक"
                if value >= 1000:
                    one = ("ek" if romanized else "एक")
                    prefix = f"{one} {unit_name}"
                else:
                    prefix = unit_name  # e.g., "सौ" for 100 (already handled)
            else:
                prefix = number_to_hindi_words(quotient, romanized) + " " + unit_name
            if remainder == 0:
                return prefix
            else:
                return prefix + " " + number_to_hindi_words(remainder, romanized)

    return ""  # never reached

# ------------------------------------------------------------
# 4. HINDI → ARABIC
# ------------------------------------------------------------
def hindi_digits_to_number(text: str) -> int:
    """Convert Devanagari digit string to integer."""
    cleaned = text.strip().replace(" ", "")
    trans = str.maketrans("०१२३४५६७८९", "0123456789")
    arabic_str = cleaned.translate(trans)
    try:
        return int(arabic_str)
    except ValueError:
        raise ValueError("Invalid Devanagari digit sequence")

def _parse_words(tokens, value_map, base_map):
    """
    Generic parser for word-based numerals.
    value_map: atomic word -> number (0-99)
    base_map: base unit word -> number (100, 1000, ...)
    """
    if not tokens:
        return None

    full = " ".join(tokens)
    if full in value_map:
        return value_map[full]

    # Try largest base unit first (sort descending by value)
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

def hindi_words_to_number(text: str) -> int:
    """Parse Devanagari words to integer."""
    tokens = text.strip().split()
    result = _parse_words(tokens, DEVANAGARI_VALUES, DEVANAGARI_BASE_VALUES)
    if result is None:
        raise ValueError("Invalid Devanagari numeral")
    return result

def romanized_words_to_number(text: str) -> int:
    """Parse romanized Hindi words to integer."""
    tokens = text.strip().split()
    result = _parse_words(tokens, ROMANIZED_VALUES, ROMANIZED_BASE_VALUES)
    if result is None:
        raise ValueError("Invalid romanized Hindi numeral")
    return result

def hindi_to_number(text: str) -> int:
    """Convert Hindi representation (digits, Devanagari words, or romanized words) to integer."""
    text = text.strip()
    if not text:
        raise ValueError("Empty input")

    # Check if it's Devanagari digits (०-९)
    devanagari_digits = set("०१२३४५६७८९")
    if all(ch in devanagari_digits or ch.isspace() for ch in text):
        return hindi_digits_to_number(text)

    # Check if it contains Devanagari characters (Unicode range for Devanagari)
    if any('\u0900' <= ch <= '\u097F' for ch in text):
        return hindi_words_to_number(text)

    # Otherwise try romanized
    return romanized_words_to_number(text)

# ============================================================
# STREAMLIT INTERFACE
# ============================================================

st.set_page_config(
    page_title="Hindi Numeral Converter",
    layout="centered"
)

st.title("Hindi Numeral Converter")
st.write(
    "Convert between **Arabic numerals** and **Hindi representations**: "
    "Devanagari digits, Devanagari words, and romanized words."
)

st.markdown("---")

# ------------------------------------------------------------
# Direction selector
# ------------------------------------------------------------
direction = st.radio(
    "Choose conversion direction:",
    ["Arabic → Hindi", "Hindi → Arabic"],
    horizontal=True
)

st.markdown("---")

# ------------------------------------------------------------
# Preset examples
# ------------------------------------------------------------
st.subheader("Preset Examples")

arabic_presets = [0, 5, 12, 21, 100, 325, 12345, 10000000]
hindi_presets = [
    "शून्य",
    "पाँच",
    "बारह",
    "इक्कीस",
    "सौ",
    "तीन सौ पच्चीस",
    "बारह हज़ार तीन सौ पैंतालीस",
    "एक करोड़",
]
romanized_presets = [
    "shoonya",
    "paanch",
    "baarah",
    "ikkees",
    "sau",
    "teen sau pachchees",
    "baarah hazaar teen sau paiñtaalees",
    "ek crore",
]

cols = st.columns(4)

if direction == "Arabic → Hindi":
    for i, num in enumerate(arabic_presets):
        if cols[i % 4].button(str(num)):
            st.session_state["arabic_input"] = str(num)
else:
    combined_presets = hindi_presets + romanized_presets
    for i, txt in enumerate(combined_presets):
        if cols[i % 4].button(txt, key=f"preset_{i}"):
            st.session_state["hindi_input"] = txt

st.markdown("---")

# ------------------------------------------------------------
# Input & conversion
# ------------------------------------------------------------
if direction == "Arabic → Hindi":
    arabic_input = st.text_input(
        "Enter an Arabic numeral:",
        key="arabic_input",
        placeholder="e.g. 325"
    )

    if arabic_input:
        if arabic_input.lstrip('-').isdigit():
            try:
                n = int(arabic_input)
                digits = number_to_hindi_digits(n)
                deva_words = number_to_hindi_words(n, romanized=False)
                roman_words = number_to_hindi_words(n, romanized=True)
                st.success(
                    f"**Devanagari digits:** {digits}\n\n"
                    f"**Devanagari words:** {deva_words}\n\n"
                    f"**Romanized words:** {roman_words}"
                )
            except Exception as e:
                st.error(str(e))
        else:
            st.error("Please enter a valid integer.")

else:  # Hindi → Arabic
    hindi_input = st.text_input(
        "Enter a Hindi numeral (digits, Devanagari words, or romanized words):",
        key="hindi_input",
        placeholder="e.g. तीन सौ पच्चीस or ३२५ or teen sau pachchees"
    )

    if hindi_input:
        try:
            result = hindi_to_number(hindi_input)
            st.success(str(result))
        except Exception as e:
            st.error(str(e))

st.markdown("---")
st.caption(
    "Implements the Indian numbering system (lakhs, crores) with standard Hindi number names. "
    "Supports Devanagari digits (०-९), Devanagari words, and romanized words. "
    "Converter algorithm created by Yi Zou. "
    "Grammar explained in the Linguistics section."
)

# ------------------------------------------------------------
# Related Pages Navigation
# ------------------------------------------------------------
st.markdown("---")
st.subheader("Explore More")

nav_cols = st.columns(3)

with nav_cols[0]:
    st.page_link(
        "pages/Hindi_Linguistics.py",
        label="Linguistics",
        help="Structure, grammar, and historical development of the numeral system"
    )

with nav_cols[1]:
    st.page_link(
        "pages/Hindi_Olympiad_Problems.py",
        label="Olympiad Problems",
        help="Competition-style problems involving Hindi numerals"
    )

with nav_cols[2]:
    st.page_link(
        "pages/Hindi_Converter.py",
        label="Converter",
        help="Return to the numeral converter"
    )