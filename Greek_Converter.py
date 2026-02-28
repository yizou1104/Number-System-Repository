import streamlit as st

# ------------------------------------------------------------
# 1. ATOMIC NUMERALS (0–19)
# ------------------------------------------------------------
GREEK_ATOMS = {
    0: "μηδέν",
    1: "ένα",
    2: "δύο",
    3: "τρία",
    4: "τέσσερα",
    5: "πέντε",
    6: "έξι",
    7: "επτά",
    8: "οκτώ",
    9: "εννιά",
    10: "δέκα",
    11: "έντεκα",
    12: "δώδεκα",
    13: "δεκατρία",
    14: "δεκατέσσερα",
    15: "δεκαπέντε",
    16: "δεκαέξι",
    17: "δεκαεπτά",
    18: "δεκαοκτώ",
    19: "δεκαεννιά",
}

ROMANIZED_ATOMS = {
    0: "midén",
    1: "éna",
    2: "dýo",
    3: "tría",
    4: "téssera",
    5: "pénte",
    6: "éxi",
    7: "eptá",
    8: "októ",
    9: "enniá",
    10: "déka",
    11: "énteka",
    12: "dódéka",
    13: "dekatría",
    14: "dekatéssera",
    15: "dekapénte",
    16: "dekaéxi",
    17: "dekaeptá",
    18: "dekaoktó",
    19: "dekaenniá",
}

# ------------------------------------------------------------
# 2. TENS (20–90) and HUNDREDS
# ------------------------------------------------------------
TENS_MAP = {
    20: ("είκοσι", "eikósi"),
    30: ("τριάντα", "triánta"),
    40: ("σαράντα", "saránta"),
    50: ("πενήντα", "penínta"),
    60: ("εξήντα", "exínta"),
    70: ("εβδομήντα", "ebdomínta"),
    80: ("ογδόντα", "ogdónta"),
    90: ("ενενήντα", "enenínta"),
}

# Special handling for 100 and above
HUNDRED = ("εκατό", "ekató")
THOUSAND = ("χίλια", "chília")
MILLION = ("εκατομμύριο", "ekatommýrio")  # ένα εκατομμύριο for 1,000,000

# For parsing, we need reverse mappings
GREEK_VALUES = {v: k for k, v in GREEK_ATOMS.items()}
GREEK_VALUES.update({v: k for k, (v, _) in TENS_MAP.items()})
GREEK_VALUES[HUNDRED[0]] = 100
GREEK_VALUES[THOUSAND[0]] = 1000
GREEK_VALUES[MILLION[0]] = 1_000_000
# Note: "χιλιάδες" (plural) handled separately in words formation

ROMANIZED_VALUES = {v: k for k, v in ROMANIZED_ATOMS.items()}
ROMANIZED_VALUES.update({v: k for k, (_, v) in TENS_MAP.items()})
ROMANIZED_VALUES[HUNDRED[1]] = 100
ROMANIZED_VALUES[THOUSAND[1]] = 1000
ROMANIZED_VALUES[MILLION[1]] = 1_000_000

# ------------------------------------------------------------
# 3. ARABIC → GREEK
# ------------------------------------------------------------
def number_to_greek_words(n: int, romanized: bool = False) -> str:
    """
    Convert an integer to Greek words.
    If romanized=True, output is transliterated (Latin script).
    """
    if n < 0:
        raise ValueError("Negative numbers are not supported")
    if n == 0:
        return (ROMANIZED_ATOMS[0] if romanized else GREEK_ATOMS[0])

    # Helper to select the correct word from a tuple (greek, romanized)
    def _w(greek_word, romanized_word):
        return romanized_word if romanized else greek_word

    # ---- 1–19 ----
    if n <= 19:
        return (ROMANIZED_ATOMS[n] if romanized else GREEK_ATOMS[n])

    # ---- 20–99 ----
    if 20 <= n <= 99:
        ten = (n // 10) * 10
        unit = n % 10
        ten_word = _w(*TENS_MAP[ten])
        if unit == 0:
            return ten_word
        else:
            # Greek uses "είκοσι ένα" (no 'και' like in some languages)
            return ten_word + " " + (ROMANIZED_ATOMS[unit] if romanized else GREEK_ATOMS[unit])

    # ---- 100–999 ----
    if 100 <= n <= 999:
        hundreds = n // 100
        remainder = n % 100
        if hundreds == 1:
            hundred_word = _w(*HUNDRED)  # "εκατό" / "ekató"
        else:
            # For 200–900, we use the plural "διακόσια", "τριακόσια", etc.
            # Omniglot only gives 100, but standard Modern Greek:
            hundreds_map = {
                2: ("διακόσια", "diakósia"),
                3: ("τριακόσια", "triakósia"),
                4: ("τετρακόσια", "tetrakósia"),
                5: ("πεντακόσια", "pentakósia"),
                6: ("εξακόσια", "exakósia"),
                7: ("επτακόσια", "eptakósia"),
                8: ("οκτακόσια", "oktakósia"),
                9: ("εννιακόσια", "enniakósia"),
            }
            hundred_word = _w(*hundreds_map[hundreds])
        if remainder == 0:
            return hundred_word
        else:
            return hundred_word + " " + number_to_greek_words(remainder, romanized)

    # ---- 1000–999,999 ----
    if 1000 <= n <= 999_999:
        thousands = n // 1000
        remainder = n % 1000
        if thousands == 1:
            thousand_word = _w(*THOUSAND)  # "χίλια" / "chília"
        else:
            # For multiple thousands, use "δύο χιλιάδες", "τρεις χιλιάδες", etc.
            # The word for "thousand" becomes "χιλιάδες" (plural)
            thousand_plural = ("χιλιάδες", "chiliádes")
            # The multiplier word itself:
            mult_word = number_to_greek_words(thousands, romanized)
            thousand_word = mult_word + " " + _w(*thousand_plural)
        if remainder == 0:
            return thousand_word
        else:
            return thousand_word + " " + number_to_greek_words(remainder, romanized)

    # ---- 1,000,000 and above ----
    if n >= 1_000_000:
        millions = n // 1_000_000
        remainder = n % 1_000_000
        if millions == 1:
            million_word = _w(*MILLION)  # "εκατομμύριο" / "ekatommýrio"
        else:
            # Plural: "εκατομμύρια" / "ekatommýria"
            million_plural = ("εκατομμύρια", "ekatommýria")
            mult_word = number_to_greek_words(millions, romanized)
            million_word = mult_word + " " + _w(*million_plural)
        if remainder == 0:
            return million_word
        else:
            return million_word + " " + number_to_greek_words(remainder, romanized)

    return ""  # fallback (should never reach)

# ------------------------------------------------------------
# 4. GREEK → ARABIC
# ------------------------------------------------------------
def _parse_greek_tokens(tokens, value_map):
    """
    Recursive parser for Greek numerals (both Greek script and romanized).
    Assumes tokens are already split by spaces.
    """
    if not tokens:
        return None

    # Try to match the entire token list as a known phrase
    full = " ".join(tokens)
    if full in value_map:
        return value_map[full]

    # Strategy: look for the largest known word (by length) that appears,
    # then split around it. This handles "χιλιάδες" / "chiliádes", "εκατομμύρια", etc.

    # Words we consider as "base units" (plural forms included)
    base_units = {
        "εκατομμύρια": 1_000_000,
        "εκατομμύριο": 1_000_000,
        "χιλιάδες": 1000,
        "χίλια": 1000,
        "εκατό": 100,
        "διακόσια": 200,
        "τριακόσια": 300,
        "τετρακόσια": 400,
        "πεντακόσια": 500,
        "εξακόσια": 600,
        "επτακόσια": 700,
        "οκτακόσια": 800,
        "εννιακόσια": 900,
        # Romanized versions
        "ekatommýria": 1_000_000,
        "ekatommýrio": 1_000_000,
        "chiliádes": 1000,
        "chília": 1000,
        "ekató": 100,
        "diakósia": 200,
        "triakósia": 300,
        "tetrakósia": 400,
        "pentakósia": 500,
        "exakósia": 600,
        "eptakósia": 700,
        "oktakósia": 800,
        "enniakósia": 900,
    }

    # Also include tens (20–90) as possible split points, but only if they are the first word?
    # Actually, tens are always followed by a unit (or nothing) and are in value_map.

    # First, look for known base unit words
    for word, value in sorted(base_units.items(), key=lambda x: -len(x[0])):
        if word in tokens:
            idx = tokens.index(word)
            left_tokens = tokens[:idx]
            right_tokens = tokens[idx + 1:]

            # Determine multiplier from left
            if left_tokens:
                mult = _parse_greek_tokens(left_tokens, value_map)
                if mult is None:
                    continue  # try next base word
            else:
                mult = 1

            # Determine remainder from right
            if right_tokens:
                rem = _parse_greek_tokens(right_tokens, value_map)
                if rem is None:
                    continue
            else:
                rem = 0

            return mult * value + rem

    # If no base unit found, try parsing as a simple atomic or tens combination
    if len(tokens) == 1:
        return value_map.get(tokens[0], None)

    # For two-word combinations like "είκοσι ένα" (20 + 1), we need to split after the first word
    # The first word should be a tens or hundreds word.
    first = tokens[0]
    rest = tokens[1:]
    if first in value_map:
        first_val = value_map[first]
        rest_val = _parse_greek_tokens(rest, value_map)
        if rest_val is not None:
            return first_val + rest_val

    return None

def greek_words_to_number(text: str, romanized: bool = False) -> int:
    """Parse Greek words (script or romanized) to integer."""
    tokens = text.strip().split()
    value_map = ROMANIZED_VALUES if romanized else GREEK_VALUES
    result = _parse_greek_tokens(tokens, value_map)
    if result is None:
        raise ValueError(f"Invalid {'romanized ' if romanized else ''}Greek numeral: '{text}'")
    return result

def greek_to_number(text: str) -> int:
    """Convert Greek representation (words in Greek script or romanized) to integer."""
    text = text.strip()
    if not text:
        raise ValueError("Empty input")

    # Check if the text contains Greek script characters (Unicode range: \u0370-\u03FF)
    if any('\u0370' <= ch <= '\u03FF' for ch in text):
        return greek_words_to_number(text, romanized=False)
    else:
        # Assume romanized
        return greek_words_to_number(text, romanized=True)


st.set_page_config(
    page_title="Greek Numeral Converter",
    layout="centered"
)

st.title("Greek Numeral Converter")
st.write(
    "Convert between **Arabic numerals** and **Greek words**. "
    "Includes both Greek script and romanized forms. "
    "(Greek uses standard Western digits 0‑9, so digit conversion is trivial.)"
)

st.markdown("---")

# ------------------------------------------------------------
# Direction selector
# ------------------------------------------------------------
direction = st.radio(
    "Choose conversion direction:",
    ["Arabic → Greek", "Greek → Arabic"],
    horizontal=True
)

st.markdown("---")

# ------------------------------------------------------------
# Preset examples
# ------------------------------------------------------------
st.subheader("Preset Examples")

arabic_presets = [0, 1, 5, 12, 21, 100, 325, 1234, 1000000]
greek_presets = [
    "μηδέν",
    "ένα",
    "πέντε",
    "δώδεκα",
    "είκοσι ένα",
    "εκατό",
    "τριακόσια είκοσι πέντε",
    "χίλια διακόσια τριάντα τέσσερα",
    "ένα εκατομμύριο",
]
romanized_presets = [
    "midén",
    "éna",
    "pénte",
    "dódéka",
    "eikósi éna",
    "ekató",
    "triakósia eíkosi pénte",
    "chília diakósia triánta téssera",
    "éna ekatommýrio",
]

cols = st.columns(4)

if direction == "Arabic → Greek":
    for i, num in enumerate(arabic_presets):
        if cols[i % 4].button(str(num)):
            st.session_state["arabic_input"] = str(num)
else:
    combined = greek_presets + romanized_presets
    for i, txt in enumerate(combined):
        if cols[i % 4].button(txt, key=f"preset_{i}"):
            st.session_state["greek_input"] = txt

st.markdown("---")

# ------------------------------------------------------------
# Input & conversion
# ------------------------------------------------------------
if direction == "Arabic → Greek":
    arabic_input = st.text_input(
        "Enter an Arabic numeral:",
        key="arabic_input",
        placeholder="e.g. 325"
    )

    if arabic_input:
        if arabic_input.lstrip('-').isdigit():
            try:
                n = int(arabic_input)
                greek_words = number_to_greek_words(n, romanized=False)
                roman_words = number_to_greek_words(n, romanized=True)
                st.success(
                    f"**Greek words:** {greek_words}\n\n"
                    f"**Romanized words:** {roman_words}"
                )
            except Exception as e:
                st.error(str(e))
        else:
            st.error("Please enter a valid integer.")

else:  # Greek → Arabic
    greek_input = st.text_input(
        "Enter Greek (words in Greek script or romanized):",
        key="greek_input",
        placeholder="e.g. τριακόσια είκοσι πέντε or triakósia eíkosi pénte"
    )

    if greek_input:
        try:
            result = greek_to_number(greek_input)
            st.success(str(result))
        except Exception as e:
            st.error(str(e))

st.markdown("---")
st.caption(
    "Implements the Greek numeral system. "
    "Supports Greek words and romanized forms. "
    "Data sourced from Omniglot: [Greek numerals](https://www.omniglot.com/language/numbers/greek.htm). "
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
        "pages/Greek_Linguistics.py",
        label="Linguistics",
        help="Structure, grammar, and historical development of the Greek numeral system"
    )

with nav_cols[1]:
    st.page_link(
        "pages/Greek_Olympiad_Problems.py",
        label="Olympiad Problems",
        help="Competition-style problems involving Greek numerals"
    )

with nav_cols[2]:
    st.page_link(
        "pages/Greek_Converter.py",
        label="Converter",
        help="Return to the numeral converter"
    )