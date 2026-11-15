"""
numerals.py — Production numeral converter for Inuktitut, Yupik, Quechua.

Research basis:
  Inuktitut : Dorais (2010), Spalding (1998 Nunavut dict), Tusaalanga
  Yupik     : Jacobson (2012 ANLC dictionary); Chan's database (Kaplan 2007,
              from Jacobson 1995; Rubino & Charles 1999)
  Quechua   : Parker (1969), Cerrón-Palomino (1987), Soto Ruiz (1976)

Confidence tiers are marked per language — see research_notes.md.
"""

from __future__ import annotations
import re


# ══════════════════════════════════════════════════════════════════════════════
# INUKTITUT (South Baffin / Nunavut standard)
# Base-20 vigesimal.
# Confidence: MEDIUM — implemented range 1–99 with noted limitations.
# ══════════════════════════════════════════════════════════════════════════════

# Core atoms 1–10 (Spalding / Dorais verified)
_IU_ATOMS: dict[int, str] = {
    1: "atausiq",
    2: "marruuk",
    3: "pingasut",
    4: "sitamat",
    5: "tallimat",
    6: "arfinillit",
    7: "arvinillit",
    8: "arvissamik",
    9: "qulingiluinnamik",
    10: "qulit",
}

# Genitive/instrumental forms used in additive compounds (11–19)
# Pattern verified in Dorais & Tusaalanga: qulit + [oblique unit]
_IU_OBLIQUE: dict[int, str] = {
    1: "atausirmik",
    2: "marruungnik",
    3: "pingasunik",
    4: "sitamanik",
    5: "tallimanik",
    6: "arfinilingnik",
    7: "arvinilingnik",
    8: "arvissamingnik",
    9: "qulingiluinnanik",
}

# Vigesimal multiples
_IU_SCORES: dict[int, str] = {
    20: "avatit",       # 1×20 — HIGH confidence
    40: "arvinik",      # 2×20 — documented; some sources: marluk avatittik
    60: "pingasuujunik avatittik",   # 3×20 — compositional
    80: "sitamat avatittik",         # 4×20 — compositional
}


def _iu_remainder(unit: int) -> str:
    """
    Return the oblique/additive form for a remainder of 1–19 after a score base.

    1–9:  direct oblique form from _IU_OBLIQUE
    10:   'qulit' (the ten base in additive position)
    11–19: 'qulit' + oblique form of (unit-10)
    """
    assert 1 <= unit <= 19, f"unit out of range: {unit}"
    if unit <= 9:
        return _IU_OBLIQUE[unit]
    if unit == 10:
        return "qulit"
    # 11–19: recursive — qulit + oblique of (unit-10)
    return f"qulit {_IU_OBLIQUE[unit - 10]}"


def number_to_inuktitut(n: int) -> str:
    """
    Convert a non-negative integer to South Baffin Inuktitut numerals.

    Supported range: 0–99.
    Numbers >= 100 raise ValueError (insufficient verified data for 100+).
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"Expected int, got {type(n).__name__}")
    if n < 0:
        raise ValueError("Negative numbers are not supported.")
    if n == 0:
        # Inuktitut traditionally has no standalone zero numeral;
        # 'sunauvva' (nothing) is the closest; we use it cautiously.
        return "sunauvva"
    if n > 99:
        raise ValueError(
            f"Inuktitut conversion is limited to 1–99 due to insufficient "
            f"verified data for numbers ≥ 100."
        )

    if n in _IU_ATOMS:
        return _IU_ATOMS[n]

    # 11–19: qulit + remainder
    if 11 <= n <= 19:
        return f"qulit {_iu_remainder(n - 10)}"

    # 20: avatit (the single verified score)
    if n == 20:
        return "avatit"

    # 21–39: avatit + remainder (1–19)
    if 21 <= n <= 39:
        return f"avatit {_iu_remainder(n - 20)}"

    # 40: arvinik (2×20)
    if n == 40:
        return "arvinik"

    # 41–59: arvinik + remainder (1–19)
    if 41 <= n <= 59:
        return f"arvinik {_iu_remainder(n - 40)}"

    # 60: pingasuujunik avatittik (3×20) — compositional
    if n == 60:
        return "pingasuujunik avatittik"

    # 61–79
    if 61 <= n <= 79:
        return f"pingasuujunik avatittik {_iu_remainder(n - 60)}"

    # 80: sitamat avatittik (4×20)
    if n == 80:
        return "sitamat avatittik"

    # 81–99
    if 81 <= n <= 99:
        return f"sitamat avatittik {_iu_remainder(n - 80)}"

    # Should not reach here given guards above
    raise ValueError(f"Cannot convert {n} to Inuktitut.")


def inuktitut_to_number(text: str) -> int:
    """
    Parse a South Baffin Inuktitut numeral string to an integer.

    Accepts the forms produced by number_to_inuktitut().
    Raises ValueError for unrecognised or unsupported forms.
    """
    text = text.strip().lower()
    if not text:
        raise ValueError("Empty input.")

    # Zero
    if text == "sunauvva":
        return 0

    _atoms_rev = {v.lower(): k for k, v in _IU_ATOMS.items()}
    _oblique_rev = {v.lower(): k for k, v in _IU_OBLIQUE.items()}

    # Single atom (1–10)
    if text in _atoms_rev:
        return _atoms_rev[text]

    # Exact score words
    score_map = {
        "avatit": 20,
        "arvinik": 40,
        "pingasuujunik avatittik": 60,
        "sitamat avatittik": 80,
    }
    if text in score_map:
        return score_map[text]

    def _parse_remainder(s: str) -> int:
        """
        Parse a remainder string (produced by _iu_remainder) back to 1–19.
        Handles: single oblique (1–9), 'qulit' (10), 'qulit <oblique>' (11–19).
        """
        s = s.strip()
        # oblique 1–9
        if s in _oblique_rev:
            return _oblique_rev[s]
        # bare qulit = 10
        if s == "qulit":
            return 10
        # qulit + oblique = 11–19
        m2 = re.fullmatch(r"qulit\s+(\S+)", s)
        if m2:
            obl = m2.group(1)
            if obl in _oblique_rev:
                return 10 + _oblique_rev[obl]
        raise ValueError(f"Cannot parse remainder: '{s}'")

    # "<score_base> <remainder>" patterns
    # We need to try longest score prefix first (pingasuujunik avatittik is 3 words)
    score_prefixes = [
        ("pingasuujunik avatittik", 60),
        ("sitamat avatittik", 80),
        ("avatit", 20),
        ("arvinik", 40),
    ]
    for prefix, base_val in score_prefixes:
        if text.startswith(prefix + " "):
            remainder_str = text[len(prefix):].strip()
            return base_val + _parse_remainder(remainder_str)

    # "qulit <remainder>" = 10 + remainder (teens 11–19)
    m = re.fullmatch(r"qulit\s+(.+)", text)
    if m:
        obl = m.group(1)
        if obl in _oblique_rev:
            return 10 + _oblique_rev[obl]
        raise ValueError(f"Unknown oblique form after 'qulit': '{obl}'")

    raise ValueError(
        f"Cannot parse Inuktitut numeral: '{text}'. "
        f"Only forms in the range 0–99 generated by number_to_inuktitut() "
        f"are supported."
    )


# ══════════════════════════════════════════════════════════════════════════════
# YUPIK (Central Alaskan Yup'ik / Yugtun)
# Base 20, with 10 and 15 inside each twenty. 9, 14 and 19 are 'not quite'
# forms of the next pivot (qulngunritaraan 'not quite ten').
# Source: Jacobson, Yup'ik Eskimo Dictionary, 2nd ed. (ANLC 2012), Appendix 6
# and the numeral entries; Kaplan's list in Chan's database (from Jacobson
# 1995) for 60-100 and the qula-based teens.
# Implemented range: 1-199 and 400. No source gives multiples of twenty from
# ten twenties up, and a two-word multiplier would make forms ambiguous
# (yuinaat qula atauciq: 201 or 220?). No word for zero is recorded.
# ══════════════════════════════════════════════════════════════════════════════

YU_MAX = 199
YU_FOUR_HUNDRED = 400

# Standalone forms, Jacobson (2012) Appendix 6
_YU_UNITS: dict[int, str] = {
    1:  "atauciq",
    2:  "malruk",
    3:  "pingayun",
    4:  "cetaman",
    5:  "talliman",
    6:  "arvinlegen",
    7:  "malrunlegen",
    8:  "pingayunlegen",
    9:  "qulngunritaraan",
    10: "qula",
    11: "qula atauciq",
    12: "qula malruk",
    13: "qula pingayun",
    14: "akimiarunritaraan",
    15: "akimiaq",
    16: "akimiaq atauciq",
    17: "akimiaq malruk",
    18: "akimiaq pingayun",
    19: "yuinaunritaraan",
}

# Inside a larger number the appendix uses other forms for 9, 14 and 19:
# 29 yuinaq qulngunrita'ar, 34 yuinaq qula cetaman, 39 yuinaq akimiaq cetaman.
_YU_IN_COMPOUND: dict[int, str] = {
    9:  "qulngunrita'ar",
    14: "qula cetaman",
    19: "akimiaq cetaman",
}

# Each multiple of twenty: yuinaak (dual) for two twenties, yuinaat (plural)
# from three. Jacobson's appendix prints 60 as yuinaak pingayun, but Kaplan's
# list and the dictionary's own example (KIP 1998:319) have yuinaat pingayun.
_YU_TWENTIES: dict[int, str] = {
    2: "yuinaak malruk",
    3: "yuinaat pingayun",
    4: "yuinaat cetaman",
    5: "yuinaat talliman",
    6: "yuinaat arvinlegen",
    7: "yuinaat malrunlegen",
    8: "yuinaat pingayunlegen",
    9: "yuinaat qulngunritaraan",
}

_YU_400 = "yuinaam yuum ipia"

_QULA_NOTE = ("built on ten, as in Rubino and Charles (1999) and in Kaplan's "
              "list from Jacobson (1995), both in Chan's database")
_SPELLING = "variant spelling (Jacobson 2012)"

# Recorded alternatives for a number said on its own
_YU_ALT_ALONE: dict[int, list[tuple[str, str]]] = {
    6:  [("arvinelgen", _SPELLING)],
    7:  [("malrunelgen", _SPELLING)],
    8:  [("pingayunelgen", _SPELLING),
         ("inglulgen", "Bristol Bay, Nushagak River, Lake Iliamna and Egegik (Jacobson 2012)")],
    9:  [("qulngunrita'ar", "the form used when counting aloud (Jacobson 2012)")],
    10: [("qulen", "variant of qula (Jacobson 2012)")],
    14: [("akimiarunrita'ar", "variant (Jacobson 2012)"), ("qula cetaman", _QULA_NOTE)],
    15: [("qula talliman", _QULA_NOTE)],
    16: [("qula arvinlegen", _QULA_NOTE)],
    17: [("qula malrunlegen", _QULA_NOTE)],
    18: [("qula pingayunlegen", _QULA_NOTE)],
    19: [("yuinaunrita'ar", "variant (Jacobson 2012)"), ("qula qulngunritaraan", _QULA_NOTE)],
}

# Recorded alternatives for the remainder inside a larger number
_YU_ALT_INSIDE: dict[int, list[tuple[str, str]]] = {
    6:  _YU_ALT_ALONE[6],
    7:  _YU_ALT_ALONE[7],
    8:  _YU_ALT_ALONE[8],
    9:  [("qulngunritaraan", "as in 29 in Rubino and Charles (1999), in Chan's database")],
    10: [("qulen", "as in 50, yuinaak malruk qulen (Jacobson 2012)")],
}

_IPIAQ_NOTE = "ipiaq 'unit of twenty', used from 40 on (Jacobson 2012)"


def _yu_check(n: int) -> None:
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"Expected int, got {type(n).__name__}")
    if n < 0:
        raise ValueError("Negative numbers are not supported.")
    if n == 0:
        raise ValueError(
            "Jacobson's Yup'ik Eskimo Dictionary records no word for zero, "
            "so none is given here."
        )
    if YU_MAX < n < YU_FOUR_HUNDRED:
        raise ValueError(
            f"{n} needs ten or more twenties. The sources give no such "
            f"multiples apart from 400, and a two-word multiplier would be "
            f"ambiguous: yuinaat qula atauciq could mean 201 or 220."
        )
    if n > YU_FOUR_HUNDRED:
        raise ValueError(
            "Above 400 the sources give only scattered forms, such as talliman "
            "kavluutet 'five hundred' and tiissitsaaq 'one thousand' (a Russian "
            "loan word), so the converter stops at 400."
        )


def _yu_remainder(r: int) -> str:
    return _YU_IN_COMPOUND.get(r, _YU_UNITS[r])


def number_to_yupik(n: int) -> str:
    """Central Alaskan Yup'ik for 1-199 and 400 (Jacobson 2012)."""
    _yu_check(n)
    if n == YU_FOUR_HUNDRED:
        return _YU_400
    if n < 20:
        return _YU_UNITS[n]
    scores, r = divmod(n, 20)
    head = "yuinaq" if scores == 1 else _YU_TWENTIES[scores]
    return head if r == 0 else f"{head} {_yu_remainder(r)}"


def yupik_literal(n: int) -> str:
    """Word-for-word reading, e.g. 37 -> 'twenty + fifteen + two'. Empty for 400,
    which Jacobson records without a gloss."""
    _yu_check(n)
    if n == YU_FOUR_HUNDRED:
        return ""
    words = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
             6: "six ('crossing over' to the other hand)", 7: "seven", 8: "eight",
             9: "not quite ten", 10: "ten", 14: "not quite fifteen",
             15: "fifteen", 19: "not quite twenty"}

    def part(r: int, inside: bool) -> str:
        if inside and r == 6:
            return "six"
        if inside and r == 14:
            return "ten + four"
        if inside and r == 19:
            return "fifteen + four"
        if r in words:
            return words[r]
        return f"ten + {words[r - 10]}" if r < 15 else f"fifteen + {words[r - 15]}"

    if n < 20:
        return part(n, False)
    scores, r = divmod(n, 20)
    if scores == 1:
        head = "twenty"
    elif scores == 9:
        head = "nine ('not quite ten') twenties"
    else:
        head = f"{words[scores].split(' (')[0]} twenties"
    return head if r == 0 else f"{head} + {part(r, True)}"


def yupik_alternatives(n: int) -> list[tuple[str, str]]:
    """Recorded alternatives to the main form, each with its source."""
    _yu_check(n)
    main = number_to_yupik(n)
    out: list[tuple[str, str]] = []

    def add(form: str, note: str) -> None:
        if form != main and form not in [f for f, _ in out]:
            out.append((form, note))

    if n == YU_FOUR_HUNDRED:
        add("yuinaat yuinaat", "'twenty twenties', in a text quoted by Jacobson (2012)")
        return out
    if n < 20:
        for form, note in _YU_ALT_ALONE.get(n, []):
            add(form, note)
        return out
    scores, r = divmod(n, 20)
    head = "yuinaq" if scores == 1 else _YU_TWENTIES[scores]
    tail = "" if r == 0 else _yu_remainder(r)
    join = (lambda h, t: f"{h} {t}".strip())
    for form, note in _YU_ALT_INSIDE.get(r, []):
        add(join(head, form), note)
    if scores >= 2:
        stem = _YU_UNITS[scores]
        if scores == 3:
            add(join("yuinaak pingayun", tail), "as printed in Jacobson's numeral appendix (2012)")
        add(join(f"{stem} ipiaq", tail), _IPIAQ_NOTE)
        for form, note in _YU_ALT_ALONE.get(scores, []):
            if scores in (6, 7, 8):
                add(join(f"yuinaat {form}", tail), note)
    if n == 100:
        add("kavluun", "Lower Yukon and Nunivak (Jacobson 2012)")
        add("negavaq", "Bristol Bay and Nushagak River (Jacobson 2012)")
    return out


def yupik_alternative_forms(n: int) -> list[str]:
    """The recorded alternatives as plain strings (used by the page checks)."""
    return [form for form, _ in yupik_alternatives(n)]


def _yu_unit_forms(r: int) -> list[str]:
    """Every form accepted for 1-19 when reading Yup'ik (a superset of the
    recorded alternatives, so that a reader's spelling choices combine)."""
    forms = [_YU_UNITS[r]]
    forms += [f for f, _ in _YU_ALT_ALONE.get(r, []) + _YU_ALT_INSIDE.get(r, [])]
    if r in _YU_IN_COMPOUND:
        forms.append(_YU_IN_COMPOUND[r])
    tens = ("qula", "qulen")
    if 11 <= r <= 14:
        forms += [f"{t} {w}" for t in tens for w in _yu_unit_forms(r - 10)]
    if 16 <= r <= 18:
        forms += [f"akimiaq {w}" for w in _yu_unit_forms(r - 15)]
    if 15 <= r <= 19:
        forms += [f"{t} {w}" for t in tens for w in _yu_unit_forms(r - 10)]
    return list(dict.fromkeys(forms))


def yupik_forms(n: int) -> list[str]:
    """Every form accepted for n when reading Yup'ik, main form first."""
    _yu_check(n)
    if n == YU_FOUR_HUNDRED:
        return [_YU_400, "yuinaat yuinaat"]
    if n < 20:
        return list(dict.fromkeys([number_to_yupik(n)] + _yu_unit_forms(n)))
    scores, r = divmod(n, 20)
    if scores == 1:
        heads = ["yuinaq"]
    else:
        stems = _yu_unit_forms(scores)
        nouns = ["yuinaak"] if scores == 2 else ["yuinaat"] + (["yuinaak"] if scores == 3 else [])
        heads = [f"{a} {s}" for a in nouns for s in stems] + [f"{s} ipiaq" for s in stems]
    if n == 100:
        heads += ["kavluun", "negavaq"]
    tails = [""] if r == 0 else _yu_unit_forms(r)
    return list(dict.fromkeys([number_to_yupik(n)] + [f"{h} {t}".strip() for h in heads for t in tails]))


_YU_APOSTROPHES = "\u2019\u02bc\u2018`\u00b4"


def _yu_normalise(text: str) -> str:
    t = text.strip().lower()
    for a in _YU_APOSTROPHES:
        t = t.replace(a, "'")
    t = t.replace("-", " ")
    return re.sub(r"\s+", " ", t)


_YU_READ: dict[str, int] = {}
for _n in list(range(1, YU_MAX + 1)) + [YU_FOUR_HUNDRED]:
    for _f in yupik_forms(_n):
        _k = _yu_normalise(_f)
        assert _YU_READ.get(_k, _n) == _n, (_f, _YU_READ.get(_k), _n)
        _YU_READ[_k] = _n
_YU_WORDS = {w for k in _YU_READ for w in k.split()}


def yupik_to_number(text: str) -> int:
    """Read any recorded Central Alaskan Yup'ik form for 1-199 or 400."""
    t = _yu_normalise(text)
    if not t:
        raise ValueError("Empty input.")
    if t in _YU_READ:
        return _YU_READ[t]
    if t in ("imkuk",):
        raise ValueError(
            "imkuk is a demonstrative ('those two'), not a numeral; "
            "Jacobson records no Yup'ik word for zero."
        )
    if "kavluutet" in t:
        raise ValueError(
            "kavluutet is the plural of kavluun 'one hundred' (talliman kavluutet "
            "'five hundred'); counts of hundreds are beyond the converter's range."
        )
    if t.startswith("tiis") or t.startswith("tiic"):
        raise ValueError(
            "tiissitsaaq 'one thousand' (a Russian loan word) is beyond the "
            "converter's range of 1-199 and 400."
        )
    unknown = [w for w in t.split() if w not in _YU_WORDS]
    if unknown:
        import difflib
        hints = []
        for w in unknown:
            close = difflib.get_close_matches(w, sorted(_YU_WORDS), n=1, cutoff=0.75)
            hints.append(f"'{w}'" + (f" (did you mean '{close[0]}'?)" if close else ""))
        raise ValueError("Not a recorded Yup'ik numeral word: " + ", ".join(hints) + ".")
    raise ValueError(
        f"'{text.strip()}' uses Yup'ik numeral words, but not in a combination "
        f"the sources record. Multiples of twenty come first (yuinaq, "
        f"yuinaak malruk, yuinaat pingayun ...), then the remainder."
    )


# ══════════════════════════════════════════════════════════════════════════════
# QUECHUA (Ayacucho / Chanka)
# Base-10, fully regular, agglutinative.
# Sources: Parker (1969), Cerrón-Palomino (1987) — HIGH confidence.
# Implemented range: 0–9999.
# ══════════════════════════════════════════════════════════════════════════════

_QU_DIGITS: dict[int, str] = {
    1: "huk",
    2: "iskay",
    3: "kimsa",
    4: "tawa",
    5: "pichqa",
    6: "suqta",
    7: "qanchis",
    8: "pusaq",
    9: "isqun",
}

# Suffix for units in compound tens (chunka X-niyuq)
# Using -niyuq throughout — most conservative and broadly supported (Parker)
_QU_SUFFIX: dict[int, str] = {
    1: "hukniyuq",
    2: "iskayniyuq",
    3: "kimsayuq",
    4: "tawayuq",
    5: "pichqayuq",
    6: "suqtayuq",
    7: "qanchisyuq",
    8: "pusaqniyuq",
    9: "isqunniyuq",
}


def number_to_quechua(n: int) -> str:
    """
    Convert a non-negative integer to Ayacucho Quechua numerals.

    Supported range: 0–9999.
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"Expected int, got {type(n).__name__}")
    if n < 0:
        raise ValueError("Negative numbers are not supported.")
    if n > 9999:
        raise ValueError(
            "Quechua conversion is limited to 0–9999."
        )
    if n == 0:
        # 'empty'; Ayacucho spelling of Cusco ch'usaq (AMLQ 2005), the word for 0
        # in the University of Texas Quechua Tinkuy course
        return "chusaq"

    parts: list[str] = []

    # Thousands
    if n >= 1000:
        thousands = n // 1000
        parts.append(_QU_DIGITS[thousands] + " waranqa")
        n %= 1000

    # Hundreds
    if n >= 100:
        hundreds = n // 100
        parts.append(_QU_DIGITS[hundreds] + " pachak")
        n %= 100

    # Tens + units
    if n >= 10:
        tens = n // 10
        units = n % 10
        if tens == 1:
            tens_word = "chunka"
        else:
            tens_word = _QU_DIGITS[tens] + " chunka"
        if units == 0:
            parts.append(tens_word)
        else:
            parts.append(tens_word + " " + _QU_SUFFIX[units])
        n = 0

    # Bare units (no tens component)
    if n > 0:
        parts.append(_QU_DIGITS[n])

    return " ".join(parts)


def quechua_to_number(text: str) -> int:
    """
    Parse an Ayacucho Quechua numeral string to an integer.

    Handles all forms produced by number_to_quechua().
    Raises ValueError for unrecognised strings.
    """
    text = text.strip().lower()
    if not text:
        raise ValueError("Empty input.")

    if text in ("chusaq", "ch'usaq", "ch’usaq"):
        return 0

    # Build reverse maps
    _digits_rev: dict[str, int] = {v.lower(): k for k, v in _QU_DIGITS.items()}
    _suffix_rev: dict[str, int] = {v.lower(): k for k, v in _QU_SUFFIX.items()}

    tokens = text.split()
    total = 0
    i = 0

    # Thousands: "<digit> waranqa"
    if i < len(tokens) - 1 and tokens[i + 1] == "waranqa":
        d = _digits_rev.get(tokens[i])
        if d is None:
            raise ValueError(f"Unknown thousands digit: '{tokens[i]}'")
        total += d * 1000
        i += 2

    # Hundreds: "<digit> pachak"
    if i < len(tokens) - 1 and tokens[i + 1] == "pachak":
        d = _digits_rev.get(tokens[i])
        if d is None:
            raise ValueError(f"Unknown hundreds digit: '{tokens[i]}'")
        total += d * 100
        i += 2

    # Tens + optional unit suffix
    if i < len(tokens):
        # Could be "chunka" (10) or "<digit> chunka" (20–90)
        # possibly followed by a unit suffix word
        remaining = tokens[i:]

        # Case A: "<digit> chunka <suffix>" or "<digit> chunka"
        if len(remaining) >= 2 and remaining[1] == "chunka":
            d = _digits_rev.get(remaining[0])
            if d is None:
                raise ValueError(f"Unknown tens digit: '{remaining[0]}'")
            total += d * 10
            if len(remaining) == 3:
                u = _suffix_rev.get(remaining[2])
                if u is None:
                    raise ValueError(
                        f"Unknown unit suffix: '{remaining[2]}'"
                    )
                total += u
            elif len(remaining) > 3:
                raise ValueError(
                    f"Unexpected tokens after tens: {remaining[2:]}"
                )

        # Case B: "chunka" alone (10) or "chunka <suffix>"
        elif remaining[0] == "chunka":
            total += 10
            if len(remaining) == 2:
                u = _suffix_rev.get(remaining[1])
                if u is None:
                    raise ValueError(
                        f"Unknown unit suffix after 'chunka': '{remaining[1]}'"
                    )
                total += u
            elif len(remaining) > 2:
                raise ValueError(
                    f"Unexpected tokens after 'chunka': {remaining[1:]}"
                )

        # Case C: bare digit (1–9, no tens)
        elif len(remaining) == 1:
            d = _digits_rev.get(remaining[0])
            if d is None:
                raise ValueError(f"Unrecognised token: '{remaining[0]}'")
            total += d

        else:
            raise ValueError(
                f"Cannot parse Quechua structure from: '{' '.join(remaining)}'"
            )

    return total
