"""
Tulu.py — Tulu numerals: data and logic for the converter page.

Tulu, a Dravidian language of coastal Karnataka and Kerala, is written in the
Kannada script, and its numbers in Kannada digits: Unicode gives the
Tulu-Tigalari script no digits of its own (it lists the Kannada digits under
that script in ScriptExtensions.txt, Unicode 16.0 to 18.0).

Sources
  Brigel (1872), A Grammar of the Tulu Language, sections 76-80, pp. 41-43:
      every form below in Kannada script and romanisation, transcribed from
      the page images; and the patterns for the numbers he leaves as "etc."
  Manner (1886), Tulu-English Dictionary: 0 (sonne), 39 (muppa + tormba),
      and the variants yerpa for 70 and ajippa and ajipa (with long a) for 60.
  D'Souza (2019), in Chan's Numeral Systems of the World's Languages: present-
      day pronunciation in IPA.
"""

from __future__ import annotations
import re
import unicodedata

MAX_N = 99_999
LAKH, CRORE = 100_000, 10_000_000

# ── Brigel (1872): Kannada script and his romanisation ──────────────────────
UNITS = {
    0: ("ಸೊನ್ನೆ", "sonnè"),            # Manner (1886) p. 661: 'the nought, cipher'
    1: ("ಒಂಜಿ", "wonji"), 2: ("ರಡ್ಡ್", "raḍḍụ"), 3: ("ಮೂಜಿ", "mūji"),
    4: ("ನಾಲ್", "nālụ"), 5: ("ಐನ್", "einụ"), 6: ("ಆಜಿ", "āji"),
    7: ("ಏಳ್", "yēḷụ"), 8: ("ಎಣ್ಮ", "yeṇma"), 9: ("ಒರ್ಮ್ಬ", "wormba"),
    10: ("ಪತ್ತ್", "pattụ"), 11: ("ಪತ್ತೊಂಜಿ", "pattonji"),
    12: ("ಪದ್ರಾಡ್", "padụrāḍụ"), 13: ("ಪದ್ಮೂಜಿ", "padụmūji"),
    14: ("ಪದ್ನಾಲ್", "padụnālụ"), 15: ("ಪದ್ನೈನ್", "padụneinụ"),
    16: ("ಪದ್ನಾಜಿ", "padụnāji"),
    17: ("ಪದ್ನೇಳ್", "padụnēḷụ"),      # Brigel prints pādụ-, apparently a misprint
    18: ("ಪದ್ನೆಣ್ಮ", "padụneṇma"), 19: ("ಪದ್ನೊರ್ಮ್ಬ", "padụnormba"),
}
TENS = {
    20: ("ಇರ್ವ", "irva"), 30: ("ಮುಪ್ಪ", "muppa"), 40: ("ನಾಲ್ಪ", "nālpa"),
    50: ("ಐವ", "eiva"), 60: ("ಅಜಿಪ", "ajipa"), 70: ("ಎಳ್ಪ", "yeḷpa"),
    80: ("ಎಣ್ಪ", "yeṇpa"), 90: ("ಸೊಣ್ಪ", "soṇpa"),
}
HUNDREDS = {
    100: ("ನೂದು", "nūdu"), 200: ("ಇರ್ನೂದು", "irnūdu"), 300: ("ಮುನ್ನೂದು", "munnūdu"),
    400: ("ನಾಲ್ನೂದು", "nālụnūdu"), 500: ("ಐನೂದು", "einūdu"), 600: ("ಆಜಿನೂದು", "ājinūdu"),
    700: ("ಏಳ್ನೂದು", "yēḷụnūdu"), 800: ("ಎಣ್ಮನೂದು", "yeṇmanūdu"),
    900: ("ಒರ್ಮ್ಬನೂದು", "wormbanūdu"),
}
THOUSAND = ("ಸಾರ", "sāra")
BIG = {LAKH: ("ಲಕ್ಷ", "lakša"), CRORE: ("ಕೋಟಿ", "kōṭi")}

# Other recorded forms, with their source
ALTERNATIVES = {
    # Manner p. 11: "ajipa, ajippa, num. Sixty; also ಆಜಿಪ" (romanised here in Brigel's way)
    60: [("ಅಜಿಪ್ಪ", "ajippa", "Männer (1886)"), ("ಆಜಿಪ", "ājipa", "Männer (1886)")],
    70: [("ಎರ್ಪ", "yerpa", "Männer (1886)")],
    400: [("ನಾನೂದು", "nānūdu", "Brigel (1872)")],
}

# Brigel (sec. 6): initial o and e are pronounced wo and ye, so he romanises
# 1 and 9 as wonji and wormba. Units Brigel writes with an initial w: the w drops after the -t- of a ten
# (irvatonji 21; Manner's muppa-tormba 39) and becomes v after the -a of nuta
# and sarata (nutavonji 101, saratavonji 1001), as it does for wormbanudu (900).
W_INITIAL = {1, 9}

# Numbers printed in Brigel's table, and the two taken from Manner
PRINTED_BRIGEL = (set(range(1, 26)) | set(TENS) | set(HUNDREDS)
                  | {101, 102, 103, 110, 150, 1000, 1001, 1002, 1010, 1020, 1030,
                     1100, 1200, 10_000, 11_000, LAKH, CRORE})
PRINTED_MANNER = {0, 39}

# D'Souza (2019) in Chan's database. Two spaces inside a word on that web
# page (muː d͡ʒi, irʋat̪ oɲd͡ʒi) are layout artefacts and are closed up.
PRONUNCIATION = {
    1: "oɲd͡ʒi", 2: "ɾaɖɖɯ", 3: "muːd͡ʒi", 4: "naːlɯ", 5: "aⁱnɯ", 6: "aːd͡ʒi",
    7: "eːlɯ", 8: "eɖma ~ enma ~ eɳma", 9: "oɾmba", 10: "pat̪t̪ɯ",
    11: "pat̪t̪oɲd͡ʒi ~ pad̪inoɲd͡ʒi", 12: "pad̪ɾaːɖɯ ~ pad̪iɾaːɖɯ",
    13: "pad̪muːd͡ʒi ~ pad̪imuːd͡ʒi", 14: "pad̪naːlɯ ~ pad̪inaːlɯ",
    15: "pad̪naⁱnɯ ~ pad̪inaⁱnɯ", 16: "pad̪naːd͡ʒi ~ pad̪inaːd͡ʒi",
    17: "pad̪neːlɯ ~ pad̪ineːlɯ", 18: "pad̪neɖma ~ pad̪ineɖma",
    19: "pad̪noɾmba ~ pad̪inoɾmba", 20: "iɾʋa", 21: "irʋat̪oɲd͡ʒi",
    22: "irʋat̪ɾaɖɖɯ", 23: "irʋat̪muːd͡ʒi", 24: "irʋat̪naːlɯ", 25: "irʋat̪aⁱnɯ",
    26: "irʋat̪aːd͡ʒi", 27: "irʋat̪eːlɯ", 28: "irʋat̪eɖma ~ irʋat̪enma",
    29: "irʋat̪oɾmba", 30: "muppa", 40: "nalpa", 50: "aⁱʋa", 60: "ad͡ʒpa",
    70: "elpa", 80: "eɳpa", 90: "soɳpa ~ sonpa", 100: "nuːd̪ɯ", 200: "iɾnuːd̪ɯ",
    400: "naːlnuːd̪ɯ", 800: "eɳmanuːd̪ɯ", 1000: "saːʋiɾa", 2000: "ɾaɖɖɯ saːʋiɾa",
}

KANNADA_DIGITS = str.maketrans("0123456789", "೦೧೨೩೪೫೬೭೮೯")
FROM_KANNADA_DIGITS = str.maketrans("೦೧೨೩೪೫೬೭೮೯", "0123456789")
VOWEL_SIGN_O = "ೊ"


def _check(n: int) -> None:
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"Expected int, got {type(n).__name__}")
    if n < 0:
        raise ValueError("Negative numbers are not supported.")
    if n > MAX_N and n not in BIG:
        raise ValueError(
            "Brigel gives the words for a lakh (1,00,000) and a crore (1,00,00,000) "
            "but no example of how they combine with other numbers, so the converter "
            "covers 0 to 99,999 and those two."
        )


def indian_grouping(n: int) -> str:
    """1234567 -> '12,34,567', the grouping Brigel prints."""
    s = str(n)
    if len(s) <= 3:
        return s
    head, tail = s[:-3], s[-3:]
    groups = []
    while len(head) > 2:
        groups.insert(0, head[-2:])
        head = head[:-2]
    if head:
        groups.insert(0, head)
    return ",".join(groups + [tail])


def kannada_digits(n: int) -> str:
    return indian_grouping(n).translate(KANNADA_DIGITS)


# Each part: (Kannada, romanisation, value, note)
Part = tuple[str, str, int, str]


def _below_100(n: int) -> list[Part]:
    if n in UNITS:
        k, r = UNITS[n]
        return [(k, r, n, "")]
    tens, unit = divmod(n, 10)
    tk, tr = TENS[tens * 10]
    if unit == 0:
        return [(tk, tr, tens * 10, "")]
    uk, ur = UNITS[unit]
    if unit in W_INITIAL:
        # irva + t + onji: the t takes the unit's first vowel
        return [(tk + "ತ", tr + "t", tens * 10, "ten + -t-"),
                (VOWEL_SIGN_O + uk[1:], ur[1:], unit, "w dropped")]
    return [(tk + "ತ್", tr + "tụ", tens * 10, "ten + -t-"), (uk, ur, unit, "")]


def _join(head: Part, rest: list[Part]) -> list[Part]:
    """nuta / sarata followed by the rest (101 nutavonji, 150 nutaeiva)."""
    k, r, v, note = rest[0]
    if r.startswith("w"):
        # wonji, wormba and the 900s (wormbanudu): the w becomes v after -a
        return [(head[0] + "ವ", head[1] + "v", head[2], head[3]),
                (VOWEL_SIGN_O + k[1:], r[1:], v, note or "w becomes v")] + rest[1:]
    return [head] + rest


def _hundreds(n: int) -> list[Part]:
    h, rest = divmod(n, 100)
    if h == 0:
        return _below_100(rest)
    hk, hr = HUNDREDS[h * 100]
    if rest == 0:
        return [(hk, hr, h * 100, "")]
    # nudu -> nuta before the rest
    head = (hk[:-2] + "ತ", hr[:-2] + "ta", h * 100, "joining form of " + hk)
    return _join(head, _below_100(rest))


def tulu_parts(n: int) -> list[Part]:
    """The pieces of n's Tulu form, left to right."""
    _check(n)
    if n in BIG:
        k, r = BIG[n]
        return [(k, r, n, "")]
    th, rest = divmod(n, 1000)
    if th == 0:
        return _hundreds(rest)
    mult = [] if th == 1 else _below_100(th)
    mult = [(k, r, v, "how many thousands") for k, r, v, _ in mult]
    if rest == 0:
        return mult + [(THOUSAND[0], THOUSAND[1], 1000, "")]
    head = (THOUSAND[0] + "ತ", THOUSAND[1] + "ta", 1000, "joining form of " + THOUSAND[0])
    return mult + _join(head, _hundreds(rest))


_VOWEL_SIGNS = set(chr(c) for c in range(0x0CBE, 0x0CCD))


def _word_for(value: int) -> tuple[str, str]:
    for table in (UNITS, TENS, HUNDREDS, BIG):
        if value in table:
            return table[value]
    return THOUSAND


def breakdown(n: int) -> list[tuple[str, str, str, str]]:
    """Rows of (value, dictionary word, romanised word, shape in this number):
    a piece that starts with a vowel sign takes the consonant before it, so
    101 shows ನೂತ- and -ವೊಂಜಿ rather than ನೂತವ- and a bare vowel sign."""
    parts = tulu_parts(n)
    shapes = [p[0] for p in parts]
    for i in range(1, len(shapes)):
        if shapes[i][:1] in _VOWEL_SIGNS:
            shapes[i] = shapes[i - 1][-1] + shapes[i]
            shapes[i - 1] = shapes[i - 1][:-1]
    rows = []
    for i, (k, r, v, note) in enumerate(parts):
        word_k, word_r = _word_for(v)
        label = f"{v:,} ×" if note == "how many thousands" else f"{v:,}"
        shape = ("-" if i else "") + shapes[i] + ("-" if i < len(parts) - 1 else "")
        rows.append((label, word_k, word_r, shape))
    return rows


def number_to_tulu(n: int) -> str:
    """Tulu in Kannada script."""
    return "".join(p[0] for p in tulu_parts(n))


def tulu_romanised(n: int) -> str:
    """Brigel's (1872) romanisation."""
    return "".join(p[1] for p in tulu_parts(n))


def source_note(n: int) -> str:
    _check(n)
    if n in PRINTED_MANNER:
        return "Männer (1886)"
    if n in PRINTED_BRIGEL:
        return "printed by Brigel (1872)"
    return "built by Brigel's patterns"


def alternatives(n: int) -> list[tuple[str, str, str]]:
    _check(n)
    return list(ALTERNATIVES.get(n, []))


def alternative_strings(n: int) -> list[str]:
    """The recorded alternatives as plain strings (used by the page checks)."""
    out = [tulu_romanised(n)]
    for k, r, _ in ALTERNATIVES.get(n, []):
        out += [k, r]
    return out


# ── Reading Tulu ─────────────────────────────────────────────────────────────
def _fold_roman(text: str) -> str:
    t = unicodedata.normalize("NFD", text.strip().lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r"[\s\-]+", "", t)
    # Brigel's glides: wonji ~ onji, yelu ~ elu
    return re.sub(r"(^|[aiu])w(?=o)|(^|[aiu])y(?=e)", lambda m: m.group(1) or m.group(2) or "", t)


def _norm_kannada(text: str) -> str:
    t = unicodedata.normalize("NFC", text.strip())
    return re.sub(r"[\s‌‍]+", "", t)


def _build_reading() -> dict[str, int]:
    table: dict[str, int] = {}

    def add(key: str, n: int) -> None:
        assert table.get(key, n) == n, (key, table.get(key), n)
        table[key] = n

    for n in list(range(0, MAX_N + 1)) + list(BIG):
        add(_norm_kannada(number_to_tulu(n)), n)
        add(_fold_roman(tulu_romanised(n)), n)
        for k, r, _ in ALTERNATIVES.get(n, []):
            add(_norm_kannada(k), n)
            add(_fold_roman(r), n)
    return table


READING = _build_reading()


def tulu_to_number(text: str) -> int:
    """Read Tulu in Kannada script or Brigel's romanisation, or Kannada digits."""
    t = text.strip()
    if not t:
        raise ValueError("Empty input.")
    plain = t.replace(",", "")
    if re.fullmatch(r"[೦-೯]+", plain):
        if len(plain.lstrip("೦")) > 18:
            _check(10 ** 18)
        return int(plain.translate(FROM_KANNADA_DIGITS))
    for key in (_norm_kannada(t), _fold_roman(t)):
        if key in READING:
            return READING[key]
    if re.search(r"[ಀ-೿]", t):
        raise ValueError(
            "Not a Tulu numeral in the spellings of Brigel (1872). Kannada number "
            "words are different words, so they are not read here."
        )
    raise ValueError(
        "Not a recognised Tulu numeral. Type it in Kannada script or in Brigel's "
        "romanisation, with or without accents: irvatụeinụ or irvatueinu (25)."
    )
