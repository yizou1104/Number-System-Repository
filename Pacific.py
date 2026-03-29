"""
numerals.py — Production numeral converter for Inuktitut, Yupik, Quechua.

Research basis:
  Inuktitut : Dorais (2010), Spalding (1998 Nunavut dict), Tusaalanga
  Yupik     : Jacobson (1984/2012 ANLC), Miyaoka (2012)
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
    4: "sisamat",
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
    4: "sisamanik",
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
    80: "sisamat avatittik",         # 4×20 — compositional
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

    # 80: sisamat avatittik (4×20)
    if n == 80:
        return "sisamat avatittik"

    # 81–99
    if 81 <= n <= 99:
        return f"sisamat avatittik {_iu_remainder(n - 80)}"

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
        "sisamat avatittik": 80,
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
        ("sisamat avatittik", 80),
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
# Base-20 with 5/10/15 sub-pivots.  Subtractive form for 9.
# Sources: Jacobson (1984/2012), Miyaoka (2012) — HIGH confidence.
# Implemented range: 0–400 (20² = one full vigesimal cycle).
# ══════════════════════════════════════════════════════════════════════════════

# Core verified atoms
_YU_ATOMS: dict[int, str] = {
    1:  "atauciq",
    2:  "malruk",
    3:  "pingayun",
    4:  "cetaman",
    5:  "talliman",
    6:  "arvinlegen",
    7:  "malrunlegen",
    8:  "pingayunlegen",
    9:  "qulngunritaraan",   # subtractive "almost ten" — Jacobson primary form
    10: "qula",
    15: "akimiaq",           # lexicalized pivot
    20: "yuinaq",
}


def _yu_1_to_19(n: int) -> str:
    """Return Yup'ik word(s) for 1–19."""
    assert 1 <= n <= 19
    if n in _YU_ATOMS:
        return _YU_ATOMS[n]
    # 11–14: qula + unit
    if 11 <= n <= 14:
        return f"qula {_YU_ATOMS[n - 10]}"
    # 16–19: akimiaq + unit
    if 16 <= n <= 19:
        return f"akimiaq {_YU_ATOMS[n - 15]}"
    raise AssertionError(f"Unreachable: {n}")


def number_to_yupik(n: int) -> str:
    """
    Convert a non-negative integer to Central Alaskan Yup'ik numerals.

    Supported range: 0–400 (complete verified vigesimal cycle).
    Numbers > 400 raise ValueError.
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"Expected int, got {type(n).__name__}")
    if n < 0:
        raise ValueError("Negative numbers are not supported.")
    if n == 0:
        # Yup'ik: "nallunriamek" / "imkuk" — no standard zero; use descriptor
        return "imkuk"
    if n > 400:
        raise ValueError(
            f"Yup'ik conversion is limited to 1–400 (one full 20² cycle). "
            f"Forms above 400 are not sufficiently verified."
        )

    # 1–19: handled by helper
    if 1 <= n <= 19:
        return _yu_1_to_19(n)

    # 20: yuinaq
    if n == 20:
        return "yuinaq"

    # 21–39: yuinaq + unit
    if 21 <= n <= 39:
        return f"yuinaq {_yu_1_to_19(n - 20)}"

    # 40–400: [multiplier] yuinaak [+ remainder]
    # yuinaak = combining form of yuinaq for multiples
    if 40 <= n <= 400:
        scores = n // 20
        remainder = n % 20
        # scores can be 2–20; _yu_1_to_19 handles 1–19; 20=yuinaq
        if scores == 20:
            mult_word = "yuinaq"
        else:
            mult_word = _yu_1_to_19(scores)
        base = f"yuinaak {mult_word}"
        if remainder == 0:
            return base
        return f"{base} {_yu_1_to_19(remainder)}"

    raise ValueError(f"Cannot convert {n} to Yup'ik.")


def yupik_to_number(text: str) -> int:
    """
    Parse a Central Alaskan Yup'ik numeral string to an integer.

    Handles all forms produced by number_to_yupik().
    Raises ValueError for unrecognised strings.
    """
    text = text.strip().lower()
    if not text:
        raise ValueError("Empty input.")

    if text == "imkuk":
        return 0

    # Build reverse lookups
    _atoms_rev: dict[str, int] = {v.lower(): k for k, v in _YU_ATOMS.items()}

    # Add compound 1–19 forms
    _1_19_rev: dict[str, int] = {}
    for i in range(1, 20):
        _1_19_rev[_yu_1_to_19(i).lower()] = i

    # Exact match in 1–19
    if text in _1_19_rev:
        return _1_19_rev[text]

    # Exact "yuinaq"
    if text == "yuinaq":
        return 20

    # "yuinaq <1–19>" → 20 + unit
    m = re.fullmatch(r"yuinaq\s+(.+)", text)
    if m:
        tail = m.group(1)
        if tail in _1_19_rev:
            return 20 + _1_19_rev[tail]
        raise ValueError(f"Unrecognised unit after 'yuinaq': '{tail}'")

    # "yuinaak <multiplier>" or "yuinaak <multiplier> <remainder>"
    # multiplier can be 1–19 (via _1_19_rev) or "yuinaq" (=20 scores = 400)
    if text.startswith("yuinaak "):
        tail = text[len("yuinaak"):].strip()

        # Special case: yuinaak yuinaq = 400
        if tail == "yuinaq":
            return 400
        if tail.startswith("yuinaq "):
            # yuinaak yuinaq <remainder> — would be 400+x but we cap at 400
            raise ValueError(
                f"Yup'ik values above 400 are not supported: '{text}'"
            )

        # Try to extract multiplier (possibly 2-word like "qula atauciq")
        # Strategy: greedily match known 1–19 forms from the start of the tail
        mult = None
        remainder_str = ""
        for length in [3, 2, 1]:  # word counts to try
            candidate = " ".join(tail.split()[:length])
            rest = " ".join(tail.split()[length:])
            if candidate in _1_19_rev:
                mult = _1_19_rev[candidate]
                remainder_str = rest
                break
        if mult is None:
            raise ValueError(f"Cannot parse multiplier in Yup'ik: '{tail}'")
        base_val = mult * 20
        if not remainder_str:
            return base_val
        if remainder_str in _1_19_rev:
            return base_val + _1_19_rev[remainder_str]
        raise ValueError(
            f"Cannot parse remainder in Yup'ik: '{remainder_str}'"
        )

    raise ValueError(
        f"Cannot parse Yup'ik numeral: '{text}'. "
        f"Only forms produced by number_to_yupik() (range 0–400) are supported."
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
        return "ch'usaq"   # "empty" — the accepted zero equivalent

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

    if text == "ch'usaq":
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
