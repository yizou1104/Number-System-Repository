import streamlit as st
# ------------------------------------------------------------
# 1. TAMIL DIGITS (0-9, plus special symbols for 10,100,1000)
# ------------------------------------------------------------
TAMIL_DIGITS = {
    0: "௦",
    1: "௧",
    2: "௨",
    3: "௩",
    4: "௪",
    5: "௫",
    6: "௬",
    7: "௭",
    8: "௮",
    9: "௯",
    10: "௰",
    100: "௱",
    1000: "௲",
}

# Reverse mapping for parsing digit strings
DIGIT_TO_ARABIC = {v: k for k, v in TAMIL_DIGITS.items()}

# ------------------------------------------------------------
# 2. ATOMIC NUMERALS 0–99 – Tamil words and romanized
#    (compiled from Wikipedia and Omniglot)
# ------------------------------------------------------------
TAMIL_ATOMS = {
    0: "சுழியம்",
    1: "ஒன்று",
    2: "இரண்டு",
    3: "மூன்று",
    4: "நான்கு",
    5: "ஐந்து",
    6: "ஆறு",
    7: "ஏழு",
    8: "எட்டு",
    9: "ஒன்பது",
    10: "பத்து",
    11: "பதினொன்று",
    12: "பன்னிரண்டு",
    13: "பதின்மூன்று",
    14: "பதினான்கு",
    15: "பதினைந்து",
    16: "பதினாறு",
    17: "பதினேழு",
    18: "பதினெட்டு",
    19: "பத்தொன்பது",
    20: "இருபது",
    21: "இருபத்தி ஒன்று",
    22: "இருபத்தி இரண்டு",
    23: "இருபத்தி மூன்று",
    24: "இருபத்தி நான்கு",
    25: "இருபத்தி ஐந்து",
    26: "இருபத்தி ஆறு",
    27: "இருபத்தி ஏழு",
    28: "இருபத்தி எட்டு",
    29: "இருபத்தி ஒன்பது",
    30: "முப்பது",
    31: "முப்பத்தி ஒன்று",
    32: "முப்பத்தி இரண்டு",
    33: "முப்பத்தி மூன்று",
    34: "முப்பத்தி நான்கு",
    35: "முப்பத்தி ஐந்து",
    36: "முப்பத்தி ஆறு",
    37: "முப்பத்தி ஏழு",
    38: "முப்பத்தி எட்டு",
    39: "முப்பத்தி ஒன்பது",
    40: "நாற்பது",
    41: "நாற்பத்தி ஒன்று",
    42: "நாற்பத்தி இரண்டு",
    43: "நாற்பத்தி மூன்று",
    44: "நாற்பத்தி நான்கு",
    45: "நாற்பத்தி ஐந்து",
    46: "நாற்பத்தி ஆறு",
    47: "நாற்பத்தி ஏழு",
    48: "நாற்பத்தி எட்டு",
    49: "நாற்பத்தி ஒன்பது",
    50: "ஐம்பது",
    51: "ஐம்பத்தி ஒன்று",
    52: "ஐம்பத்தி இரண்டு",
    53: "ஐம்பத்தி மூன்று",
    54: "ஐம்பத்தி நான்கு",
    55: "ஐம்பத்தி ஐந்து",
    56: "ஐம்பத்தி ஆறு",
    57: "ஐம்பத்தி ஏழு",
    58: "ஐம்பத்தி எட்டு",
    59: "ஐம்பத்தி ஒன்பது",
    60: "அறுபது",
    61: "அறுபத்தி ஒன்று",
    62: "அறுபத்தி இரண்டு",
    63: "அறுபத்தி மூன்று",
    64: "அறுபத்தி நான்கு",
    65: "அறுபத்தி ஐந்து",
    66: "அறுபத்தி ஆறு",
    67: "அறுபத்தி ஏழு",
    68: "அறுபத்தி எட்டு",
    69: "அறுபத்தி ஒன்பது",
    70: "எழுபது",
    71: "எழுபத்தி ஒன்று",
    72: "எழுபத்தி இரண்டு",
    73: "எழுபத்தி மூன்று",
    74: "எழுபத்தி நான்கு",
    75: "எழுபத்தி ஐந்து",
    76: "எழுபத்தி ஆறு",
    77: "எழுபத்தி ஏழு",
    78: "எழுபத்தி எட்டு",
    79: "எழுபத்தி ஒன்பது",
    80: "எண்பது",
    81: "எண்பத்தி ஒன்று",
    82: "எண்பத்தி இரண்டு",
    83: "எண்பத்தி மூன்று",
    84: "எண்பத்தி நான்கு",
    85: "எண்பத்தி ஐந்து",
    86: "எண்பத்தி ஆறு",
    87: "எண்பத்தி ஏழு",
    88: "எண்பத்தி எட்டு",
    89: "எண்பத்தி ஒன்பது",
    90: "தொன்னூறு",
    91: "தொன்னூற்றி ஒன்று",
    92: "தொன்னூற்றி இரண்டு",
    93: "தொன்னூற்றி மூன்று",
    94: "தொன்னூற்றி நான்கு",
    95: "தொன்னூற்றி ஐந்து",
    96: "தொன்னூற்றி ஆறு",
    97: "தொன்னூற்றி ஏழு",
    98: "தொன்னூற்றி எட்டு",
    99: "தொன்னூற்றி ஒன்பது",
}

ROMANIZED_ATOMS = {
    0: "suzhiyam",
    1: "onru",
    2: "irandu",
    3: "munru",
    4: "nanku",
    5: "ainthu",
    6: "aaru",
    7: "ezhu",
    8: "ettu",
    9: "onpathu",
    10: "paththu",
    11: "pathinonru",
    12: "pannirandu",
    13: "pathinmunru",
    14: "pathinanku",
    15: "pathiainthu",
    16: "pathinaaru",
    17: "pathinezhu",
    18: "pathinettu",
    19: "paththonpathu",
    20: "irupathu",
    21: "irupathi onru",
    22: "irupathi irandu",
    23: "irupathi munru",
    24: "irupathi nanku",
    25: "irupathi ainthu",
    26: "irupathi aaru",
    27: "irupathi ezhu",
    28: "irupathi ettu",
    29: "irupathi onpathu",
    30: "muppathu",
    31: "muppathi onru",
    32: "muppathi irandu",
    33: "muppathi munru",
    34: "muppathi nanku",
    35: "muppathi ainthu",
    36: "muppathi aaru",
    37: "muppathi ezhu",
    38: "muppathi ettu",
    39: "muppathi onpathu",
    40: "narpathu",
    41: "narpathi onru",
    42: "narpathi irandu",
    43: "narpathi munru",
    44: "narpathi nanku",
    45: "narpathi ainthu",
    46: "narpathi aaru",
    47: "narpathi ezhu",
    48: "narpathi ettu",
    49: "narpathi onpathu",
    50: "aimpathu",
    51: "aimpathi onru",
    52: "aimpathi irandu",
    53: "aimpathi munru",
    54: "aimpathi nanku",
    55: "aimpathi ainthu",
    56: "aimpathi aaru",
    57: "aimpathi ezhu",
    58: "aimpathi ettu",
    59: "aimpathi onpathu",
    60: "arupathu",
    61: "arupathi onru",
    62: "arupathi irandu",
    63: "arupathi munru",
    64: "arupathi nanku",
    65: "arupathi ainthu",
    66: "arupathi aaru",
    67: "arupathi ezhu",
    68: "arupathi ettu",
    69: "arupathi onpathu",
    70: "ezhupathu",
    71: "ezhupathi onru",
    72: "ezhupathi irandu",
    73: "ezhupathi munru",
    74: "ezhupathi nanku",
    75: "ezhupathi ainthu",
    76: "ezhupathi aaru",
    77: "ezhupathi ezhu",
    78: "ezhupathi ettu",
    79: "ezhupathi onpathu",
    80: "enpathu",
    81: "enpathi onru",
    82: "enpathi irandu",
    83: "enpathi munru",
    84: "enpathi nanku",
    85: "enpathi ainthu",
    86: "enpathi aaru",
    87: "enpathi ezhu",
    88: "enpathi ettu",
    89: "enpathi onpathu",
    90: "thonnuru",
    91: "thonnurri onru",
    92: "thonnurri irandu",
    93: "thonnurri munru",
    94: "thonnurri nanku",
    95: "thonnurri ainthu",
    96: "thonnurri aaru",
    97: "thonnurri ezhu",
    98: "thonnurri ettu",
    99: "thonnurri onpathu",
}

# Reverse mappings for parsing
TAMIL_VALUES = {v: k for k, v in TAMIL_ATOMS.items()}
ROMANIZED_VALUES = {v: k for k, v in ROMANIZED_ATOMS.items()}

# ------------------------------------------------------------
# 3. BASE UNITS – Powers of ten and larger (Indian system)
# ------------------------------------------------------------
BASE_UNITS = [
    # Tamil system (TS) and Sanskrit system (SS) – we include both common forms
    ("கோடி", "kodi", 10_000_000),        # crore
    ("இலட்சம்", "ilatcham", 100_000),      # lakh
    ("ஆயிரம்", "ayiram", 1_000),           # thousand
    ("நூறு", "nuru", 100),                  # hundred
]

# Value maps for parsing
TAMIL_BASE_VALUES = {tam: value for tam, roman, value in BASE_UNITS}
ROMANIZED_BASE_VALUES = {roman: value for _, roman, value in BASE_UNITS}

# Also include "பத்து" (ten) – but numbers 10–99 are handled by atomic map
# Include the special Tamil digits for 10,100,1000? Parsing digit strings is separate.

# ------------------------------------------------------------
# 4. ARABIC → TAMIL
# ------------------------------------------------------------
def number_to_tamil_digits(n: int) -> str:
    """Convert integer to Tamil script digits (uses special symbols for 10,100,1000)."""
    if n == 0:
        return TAMIL_DIGITS[0]
    # Handle special symbols for exact powers of ten
    if n == 10:
        return TAMIL_DIGITS[10]
    if n == 100:
        return TAMIL_DIGITS[100]
    if n == 1000:
        return TAMIL_DIGITS[1000]
    # For other numbers, use standard decimal representation with Tamil digits 0-9
    # (special symbols are not combined further)
    trans = str.maketrans("0123456789", "௦௧௨௩௪௫௬௭௮௯")
    return str(n).translate(trans)

def number_to_tamil_words(n: int, romanized: bool = False) -> str:
    """Convert integer to Tamil words (Tamil script if romanized=False, else romanized)."""
    if n < 0:
        raise ValueError("Negative numbers are not supported")
    if n == 0:
        return (ROMANIZED_ATOMS[0] if romanized else TAMIL_ATOMS[0])

    atom_map = ROMANIZED_ATOMS if romanized else TAMIL_ATOMS

    # Direct atomic (0-99)
    if n <= 99:
        return atom_map[n]

    # Handle numbers 100–999
    if 100 <= n < 1000:
        hundreds = n // 100
        remainder = n % 100
        hundred_word = ("nuru" if romanized else "நூறு")
        if hundreds == 1:
            prefix = hundred_word
        else:
            prefix = atom_map[hundreds] + " " + hundred_word
        if remainder == 0:
            return prefix
        else:
            return prefix + " " + atom_map[remainder]

    # Handle thousands and above
    for tam, roman, value in BASE_UNITS:
        if n >= value:
            quotient = n // value
            remainder = n % value
            unit_name = roman if romanized else tam
            # For lakh and crore, the multiplier word is attached directly
            # e.g., "இருபது இலட்சம்" (20 lakhs)
            prefix = number_to_tamil_words(quotient, romanized) + " " + unit_name
            if remainder == 0:
                return prefix
            else:
                return prefix + " " + number_to_tamil_words(remainder, romanized)

    return ""  # never reached

# ------------------------------------------------------------
# 5. TAMIL → ARABIC
# ------------------------------------------------------------
def tamil_digits_to_number(text: str) -> int:
    """Convert Tamil digit string to integer.
       Handles both standard digits ௦-௯ and special symbols ௰,௱,௲."""
    # Remove spaces
    cleaned = text.strip().replace(" ", "")
    if not cleaned:
        raise ValueError("Empty input")

    # Check for special symbols
    if cleaned in TAMIL_DIGITS.values():
        return [k for k, v in TAMIL_DIGITS.items() if v == cleaned][0]

    # Otherwise, map each character (standard digits)
    result_str = ""
    for ch in cleaned:
        if ch in DIGIT_TO_ARABIC:
            result_str += str(DIGIT_TO_ARABIC[ch])
        else:
            # Could be a special symbol like ௰௲ for 10,000? We'll treat as decimal digits only.
            raise ValueError(f"Invalid Tamil digit character: {ch}")
    try:
        return int(result_str)
    except ValueError:
        raise ValueError("Invalid Tamil digit sequence")

def _parse_words(tokens, value_map, base_map):
    """Generic parser for word-based numerals (Tamil or Romanized)."""
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

def tamil_words_to_number(text: str) -> int:
    """Parse Tamil script words to integer."""
    tokens = text.strip().split()
    result = _parse_words(tokens, TAMIL_VALUES, TAMIL_BASE_VALUES)
    if result is None:
        raise ValueError("Invalid Tamil numeral")
    return result

def romanized_words_to_number(text: str) -> int:
    """Parse romanized Tamil words to integer."""
    tokens = text.strip().split()
    result = _parse_words(tokens, ROMANIZED_VALUES, ROMANIZED_BASE_VALUES)
    if result is None:
        raise ValueError("Invalid romanized Tamil numeral")
    return result

def tamil_to_number(text: str) -> int:
    """Convert Tamil representation (digits, Tamil words, or romanized words) to integer."""
    text = text.strip()
    if not text:
        raise ValueError("Empty input")

    # Check if it's Tamil digits (includes special symbols)
    # Tamil Unicode range: \u0B80-\u0BFF
    tamil_chars = set("௦௧௨௩௪௫௬௭௮௯௰௱௲")
    if all(ch in tamil_chars or ch.isspace() for ch in text):
        return tamil_digits_to_number(text)

    # Check if it contains Tamil script characters (words)
    if any('\u0B80' <= ch <= '\u0BFF' for ch in text):
        return tamil_words_to_number(text)

    # Otherwise try romanized
    return romanized_words_to_number(text)

st.set_page_config(
    page_title="Hindi Numeral Converter",
    layout="centered"
)

st.title("Tamil Numeral Converter")
st.write(
    "Convert between **Arabic numerals** and **Hindi representations**: "
    "Devanagari digits, Devanagari words, and romanized words."
)

st.markdown("---")

direction = st.radio("Choose direction:", ["Arabic → Tamil", "Tamil → Arabic"], horizontal=True)

st.markdown("---")
st.subheader("Preset Examples")

arabic_presets = [0, 1, 5, 10, 21, 100, 325, 10000000]
tamil_presets = [
    "சுழியம்",
    "ஒன்று",
    "ஐந்து",
    "பத்து",
    "இருபத்தி ஒன்று",
    "நூறு",
    "முந்நூறு இருபத்தி ஐந்து",
    "ஒரு கோடி",
]
romanized_presets = [
    "suzhiyam",
    "onru",
    "ainthu",
    "paththu",
    "irupathi onru",
    "nuru",
    "munuru irupathi ainthu",
    "oru kodi",
]

cols = st.columns(4)
if direction == "Arabic → Tamil":
    for i, num in enumerate(arabic_presets):
        if cols[i % 4].button(str(num)):
            st.session_state["arabic_input"] = str(num)
else:
    combined = tamil_presets + romanized_presets
    for i, txt in enumerate(combined):
        if cols[i % 4].button(txt, key=f"preset_{i}"):
            st.session_state["tamil_input"] = txt

st.markdown("---")

if direction == "Arabic → Tamil":
    arabic_input = st.text_input("Enter an Arabic numeral:", key="arabic_input", placeholder="e.g. 325")
    if arabic_input:
        if arabic_input.lstrip('-').isdigit():
            n = int(arabic_input)
            digits = number_to_tamil_digits(n)
            tamil_words = number_to_tamil_words(n, romanized=False)
            roman_words = number_to_tamil_words(n, romanized=True)
            st.success(f"**Tamil digits:** {digits}\n\n**Tamil words:** {tamil_words}\n\n**Romanized words:** {roman_words}")
        else:
            st.error("Please enter a valid integer.")
else:
    tamil_input = st.text_input("Enter Tamil (digits, words, or romanized):", key="tamil_input", placeholder="e.g. முந்நூறு இருபத்தி ஐந்து")
    if tamil_input:
        try:
            result = tamil_to_number(tamil_input)
            st.success(str(result))
        except Exception as e:
            st.error(str(e))

st.markdown("---")
st.caption("Implements the Tamil numeral system. "
    "Supports Tamil digits, Tamil words, and romanized words. "
    "Data sourced from Omniglot: [Omniglot](https://www.omniglot.com/language/numbers/tamil.htm). "
    "Converter algorithm created by Yi Zou. "
    "Grammar explained in the Linguistics section.")

nav_cols = st.columns(3)
with nav_cols[0]:
    st.page_link("pages/Tamil_Linguistics.py", label="Linguistics")
with nav_cols[1]:
    st.page_link("pages/Tamil_Olympiad_Problems.py", label="Olympiad Problems")
with nav_cols[2]:
    st.page_link("pages/Tamil_Converter.py", label="Converter")