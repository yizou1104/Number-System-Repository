"""
Koraga.py — Koraga numerals: data and logic for the converter page.

Koraga is a Dravidian language of the Koraga people of coastal Karnataka and
Kasaragod in Kerala. No source records how its numbers combine beyond the
teens, or how a hundred joins a smaller number, so this module holds only
forms printed in a source, each with its source, and refuses every other
number.

Sources
  Sharma, S. R. (1990), Korra Koraga, in Chan's Numeral Systems of the World's
      Languages: 1-20, the tens, 100 and 1,000, in IPA.
  Bhat, D. N. S. (1971), The Koraga Language, Deccan College: Comparative
      Vocabulary (pp. 88-118) and comparative study (pp. 42-43), for the Onti,
      Tappu and Mudu dialects, in Bhat's romanisation. Forms read from the
      page images; the scan's text layer drops the diacritics.
  KIRTADS (2019), Pasaru: Koraga language handbook, Kerala, in Latin letters
      and Malayalam script, in two lists: Table 7 (pp. 107-108) and a word list
      (pp. 166-169), and 500 among the examples of vowels (p. 53). The Latin is taken from the PDF's
      text layer; the Malayalam, set in the legacy ML-TT font, was read from
      the page images and checks against that font's encoding.
"""

from __future__ import annotations
import re
import unicodedata

LAKH = 100_000

# ── The sources ──────────────────────────────────────────────────────────────
SOURCES = {
    "korra":       ("Korra Koraga",      "Sharma (1990), in Chan's database"),
    "onti":        ("Onti",              "Bhat (1971)"),
    "tappu":       ("Tappu",             "Bhat (1971)"),
    "mudu":        ("Mudu",              "Bhat (1971)"),
    "kerala":      ("Kerala (Table 7)",   "KIRTADS (2019)"),
    "kerala_list": ("Kerala (word list)", "KIRTADS (2019)"),
    "kerala_other": ("Kerala (elsewhere)", "KIRTADS (2019)"),
}
ORDER = ("korra", "onti", "tappu", "mudu", "kerala", "kerala_list", "kerala_other")
# the sources a number can be missing from ('elsewhere' is a single example)
MAIN = ORDER[:-1]

# ── Sharma (1990), as given in Chan's database, in IPA ──────────────────────
KORRA = {
    1: "oñji", 2: "rəɖɖɨ", 3: "muːjɨ", 4: "naːli", 5: "aynɨ", 6: "aːji", 7: "eːlɨ",
    8: "eɖma", 9: "ormba", 10: "pattɨ", 11: "pattoñjɨ", 12: "pattɨrəɖɖɨ",
    13: "pattimuːjɨ", 14: "pattɨnaːli", 15: "pattɨaynɨ", 16: "pattɨaːji",
    17: "pattɨeːli", 18: "padieɖma", 19: "padnormba", 20: "irwa",
    30: "muppa", 40: "nalpa", 50: "aywa", 60: "aːjipa", 70: "eːlipa",
    80: "eɖmawa", 90: "conpa", 100: "nuːdu", 1000: "caːwra",
}

# ── Bhat (1971): (form, page) for each dialect ───────────────────────────────
BHAT = {
    "onti": {1: ("onji", 92), 2: ("raḍḍɨ", 113), 3: ("mu:ji", 112), 4: ("na:lɨ", 104),
             5: ("aynɨ", 89), 7: ("e:lɨ", 92), 50: ("ayva", 89), 60: ("ajippa", 88)},
    "tappu": {1: ("onji", 92), 2: ("naḍḍɨ", 103), 3: ("mu:ji", 112), 7: ("e:rɨ", 92),
              11: ("hattonji", 115), 12: ("hadra:ḍɨ", 115)},
    "mudu": {1: ("unji", 90), 2: ("eyḍɨ", 91), 3: ("mu:ji", 112), 7: ("yo:ḷu", 112),
             12: ("hanneyḍɨ", 115)},
}
# Words for two people (Bhat 1971, pp. 90-91), and 'times'
PERSON_WORDS = {"irverɨ": ("onti", 2, 90), "eḍḍaḷɨ": ("mudu", 2, 91)}
TIMES_WORD = ("sarti", 113)

# ── KIRTADS (2019), Table 7: (Latin, Malayalam, page) ───────────────────────
KERALA = {
    1: ("oñji", "ഒഞ്ജി", 107), 2: ("reddu", "രെഡ്ഡു", 107), 3: ("muuji", "മൂജി", 107),
    4: ("naalu", "നാലു", 107), 5: ("ayinu", "അയിനു", 107), 6: ("aaji", "ആജി", 107),
    7: ("eelu", "ഏളു", 107), 8: ("enme", "എൺമ", 107), 9: ("orumpa", "ഒരുമ്പ", 107),
    10: ("pattu", "പത്തു", 107), 100: ("nuutu", "നൂതു", 108),
    1000: ("saavira", "സാവിര", 108), 4000: ("nalsaavira", "നൽസവീര", 108),
    5000: ("ayinusaavira", "അയിനുസവീര", 108), 6000: ("aaji saavira", "ആജി സാവിര", 108),
    7000: ("eelu savira", "ഏളു സാവിര", 108), 8000: ("enma saavira", "എൻമ സാവിര", 108),
    9000: ("orumpa saavira", "ഒരുമ്പ സാവിര", 108),
    10000: ("pattu saavira", "പത്തു സാവിര", 108), LAKH: ("lacca", "ലച്ച", 108),
}
# Table 7 writes 8 as enme (എൺമ), but as enma (എൻമ) in 8,000
KERALA_ALSO = {8: ("enma", "എൻമ", 108)}
# 500 outside both lists, among the handbook's examples of vowels
KERALA_OTHER = {500: ("aiņûdu", "ഐനൂഡു", 53)}

# ── KIRTADS (2019), word list, 'words related to numbers' ───────────────────
# Latin as printed, with its alternatives after a slash
KERALA_LIST = {
    1: ("onji", "ഒൻജി", 166), 2: ("rRaḍdu", "റഡ്ഡു", 166), 3: ("mūji", "മൂജി", 166),
    4: ("nāḷu", "നാളു", 166), 5: ("aīṇu", "അയിണു", 166), 6: ("āji", "ആജി", 166),
    7: ("ēḷu", "ഏളു", 166), 8: ("eṇumma", "എണുമ്മ", 166), 9: ("oRumPa", "ഒറുമ്പ", 166),
    10: ("pattu", "പത്തു", 166), 11: ("pattonji", "പത്തെൻജി", 166),
    12: ("patRāḍu/padrādē", "പത്രാണ്ടു", 166), 13: ("patimūji", "പതിമൂജി", 167),
    14: ("patnāḷu", "പത്നാളു", 167), 17: ("patinēḷu", "പതിനേളു", 167),
    18: ("patinenma", "പതിനേന്മ", 167), 19: ("patuRmba/patineRumba", "പതുറുമ്ബ", 167),
    20: ("iRuva", "ഇറുവ", 167), 30: ("muppa", "മുപ്പ", 167), 40: ("naluppa", "നലുപ്പ", 167),
    50: ("aiūva", "അയ്വ", 167), 60: ("ajippa", "അജിപ്പ", 168),
    70: ("ēlippa/elippa", "ഏലിപ്പ", 168), 80: ("eṇippa", "എണിപ്പ", 168),
    90: ("conuppa/soṇuppa", "ചൊണുപ്പ", 168), 100: ("nūdu", "നൂദു", 168),
    200: ("iRnūdu/raḍunūdu", "ഇർനൂദു", 168), 300: ("munnudu/mūjinūdu", "മൂന്നുദു", 168),
    400: ("nalṇudu", "നൽണുദു", 168), 500: ("aīṇudu", "അയ്ണുദു", 168),
    600: ("ājinudu", "അജിനുദു", 168), 700: ("ēḷnudu", "ഏള്നുദു", 168),
    800: ("eṇmanudu", "എൺമനുദു", 169), 900: ("oRmanudu", "ഒർമനുദു", 169),
    1000: ("cāiRam/onjisāiRam/sāviRa", "ചായിറം", 169),
}
# Rows of the word list whose word and gloss disagree; not used as answers
KERALA_LIST_SET_ASIDE = {
    15: ("patnāji/patineni", "പത്നാജി", 167,
         "printed as 'fifteen', though it is built from ten and āji, six"),
    16: ("patinainu", "പതിനായിനു", 167,
         "printed as 'sixteen', though it is built from ten and ainu, five"),
    17: ("patinenma", "", 167,
         "printed beside patinēḷu as 'seventeen', though it is the list's word for eighteen"),
}

RECORDED = sorted(set(KORRA) | set(KERALA) | set(KERALA_LIST) | set(KERALA_OTHER)
                  | {n for d in BHAT.values() for n in d})


def grouped(n: int) -> str:
    """Indian grouping for the lakh, as the sources write it: 1,00,000."""
    return "1,00,000" if n == LAKH else f"{n:,}"


def _check(n: int) -> None:
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"Expected int, got {type(n).__name__}")
    if n < 0:
        raise ValueError("Negative numbers are not supported.")
    if n == 0:
        raise ValueError("No Koraga source records a word for zero.")
    if n > LAKH:
        raise ValueError(
            "The largest Koraga number recorded is lacca, 1,00,000 (a lakh), in the "
            "KIRTADS handbook (2019)."
        )
    if n not in RECORDED:
        raise ValueError(unrecorded_message(n))


def unrecorded_message(n: int) -> str:
    below = max(r for r in RECORDED if r < n)
    above = min(r for r in RECORDED if r > n)
    if 20 < n < 100:
        what = ("Sharma (1990) and the Kerala handbook record 1 to 20 and the tens, but "
                "no number between the tens.")
    elif 100 < n < 1000:
        what = ("The hundreds are recorded only as whole hundreds, 100 to 900; no source "
                "shows how a hundred joins a smaller number.")
    else:
        what = ("The thousands recorded are 1,000 and 4,000 to 10,000 (KIRTADS 2019), "
                "with nothing in between.")
    return (f"No Koraga source records {n:,}. {what} The nearest recorded numbers are "
            f"{grouped(below)} and {grouped(above)}. The converter does not build numbers "
            f"the sources do not give.")


def forms(n: int) -> list[tuple[str, str, str, str]]:
    """Every recorded form of n as (source key, form, Malayalam or '', citation)."""
    _check(n)
    out = []
    if n in KORRA:
        out.append(("korra", KORRA[n], "", SOURCES["korra"][1]))
    for dialect in ("onti", "tappu", "mudu"):
        if n in BHAT[dialect]:
            form, page = BHAT[dialect][n]
            out.append((dialect, form, "", f"Bhat (1971), p. {page}"))
    if n in KERALA:
        lat, mal, page = KERALA[n]
        out.append(("kerala", lat, mal, f"KIRTADS (2019), p. {page}"))
    if n in KERALA_LIST:
        lat, mal, page = KERALA_LIST[n]
        out.append(("kerala_list", lat, mal, f"KIRTADS (2019), p. {page}"))
    if n in KERALA_OTHER:
        lat, mal, page = KERALA_OTHER[n]
        out.append(("kerala_other", lat, mal, f"KIRTADS (2019), p. {page}, an example of vowels"))
    return out


def missing_sources(n: int) -> list[str]:
    """Labels of the sources with no form for n."""
    have = {key for key, *_ in forms(n)}
    return [SOURCES[k][0] for k in MAIN if k not in have]


def number_to_koraga(n: int) -> str:
    """The first recorded form (Sharma's where there is one) — entry point for the audits."""
    return forms(n)[0][1]


def all_forms_strings(n: int) -> list[str]:
    """Every recorded spelling of n, Latin and Malayalam (used by the page checks)."""
    out = []
    for _, form, mal, _ in forms(n):
        out.append(form)
        if "/" in form:
            out += form.split("/")
        if mal:
            out.append(mal)
    if n in KERALA_ALSO:
        out += list(KERALA_ALSO[n][:2])
    return out


# ── Reading Koraga ───────────────────────────────────────────────────────────
_LETTERS = str.maketrans({"ɨ": "i", "ə": "a", "ɖ": "d", "ñ": "n", "ː": "", ":": "",
                          "-": "", " ": "", "’": "", "'": ""})


def _fold(text: str) -> str:
    """Fold the spelling systems together: no diacritics, no length marks."""
    t = unicodedata.normalize("NFC", text.strip().lower()).translate(_LETTERS)
    t = "".join(c for c in unicodedata.normalize("NFD", t) if not unicodedata.combining(c))
    return re.sub(r"([aeiou])\1", r"\1", t)


def _norm_malayalam(text: str) -> str:
    t = unicodedata.normalize("NFC", text)
    # older keyboards type chillu letters as consonant + virama + zero-width joiner
    for cons, chillu in (("ണ", "ൺ"), ("ന", "ൻ"), ("ര", "ർ"), ("ല", "ൽ"), ("ള", "ൾ")):
        t = t.replace(cons + "്‍", chillu)
    return re.sub(r"[\s‌‍]", "", t)


def _is_malayalam(text: str) -> bool:
    return any("ഀ" <= c <= "ൿ" for c in text)


def _build_readings() -> dict[str, list[tuple[int, str]]]:
    table: dict[str, list[tuple[int, str]]] = {}

    def add(key: str, n: int, label: str) -> None:
        entry = table.setdefault(key, [])
        if (n, label) not in entry:
            entry.append((n, label))

    for n in RECORDED:
        for key, form, mal, cite in forms(n):
            label = f"{SOURCES[key][0]} · {cite}"
            for spelling in form.split("/"):
                add(_fold(spelling), n, label)
            if mal:
                add(_norm_malayalam(mal), n, label)
    for n, (lat, mal, page) in KERALA_ALSO.items():
        label = f"{SOURCES['kerala'][0]} · KIRTADS (2019), p. {page}"
        add(_fold(lat), n, label)
        add(_norm_malayalam(mal), n, label)
    return table


READINGS = _build_readings()
_COLLISIONS = {k: v for k, v in READINGS.items() if len({n for n, _ in v}) > 1}
assert not _COLLISIONS, f"one spelling, two values: {_COLLISIONS}"

SET_ASIDE_READINGS = {}
for _n, (_lat, _mal, _page, _why) in KERALA_LIST_SET_ASIDE.items():
    for _s in _lat.split("/"):
        if _fold(_s) not in READINGS:
            SET_ASIDE_READINGS[_fold(_s)] = (_n, _s, _page, _why)
    if _mal:
        SET_ASIDE_READINGS[_norm_malayalam(_mal)] = (_n, _mal, _page, _why)

PERSON_READINGS = {_fold(w): (d, n, p) for w, (d, n, p) in PERSON_WORDS.items()}
KANNADA_WORDS = {"ondu": 1, "eradu": 2, "muru": 3, "nalku": 4, "aidu": 5, "aru": 6,
                 "entu": 8, "ombattu": 9, "hattu": 10, "nuru": 100}


def koraga_lookup(text: str) -> list[tuple[int, str]]:
    """Every (value, source) reading of a recorded form."""
    if not text.strip():
        raise ValueError("Empty input.")
    if re.fullmatch(r"[\d,\s೦-೯]+", text.strip()):
        raise ValueError("Enter a Koraga word here. To look up a number, switch the direction.")
    key = _norm_malayalam(text) if _is_malayalam(text) else _fold(text)
    if key in READINGS:
        return sorted(READINGS[key], key=lambda r: ORDER.index(
            next(k for k in ORDER if r[1].startswith(SOURCES[k][0] + " ·"))))
    if key in SET_ASIDE_READINGS:
        n, form, page, why = SET_ASIDE_READINGS[key]
        raise ValueError(
            f"{form} is in the Kerala handbook's word list (KIRTADS 2019, p. {page}), "
            f"{why}. The converter does not use it."
        )
    if key in PERSON_READINGS:
        dialect, n, page = PERSON_READINGS[key]
        raise ValueError(
            f"This is {SOURCES[dialect][0]} for 'two persons' (Bhat 1971, p. {page}), a word "
            f"for counting people rather than a plain number. The plain {SOURCES[dialect][0]} "
            f"word for {n} is {BHAT[dialect][n][0]}."
        )
    if key == _fold(TIMES_WORD[0]):
        raise ValueError("sarti means 'times' in Onti (Bhat 1971, p. 113): raḍḍɨ sarti is 'twice'.")
    if key in KANNADA_WORDS:
        n = KANNADA_WORDS[key]
        raise ValueError(f"This looks like Kannada for {n}. Use the other direction to see "
                         f"the Koraga forms recorded for {n}.")
    try:
        from Tulu import tulu_to_number
        n = tulu_to_number(text)
    except Exception:
        n = None
    if n is not None:
        recorded = n in RECORDED
        raise ValueError(
            f"This is Tulu for {n:,} (Brigel 1872), not a recorded Koraga form. "
            + (f"Use the other direction to see the Koraga forms for {n:,}." if recorded
               else f"No Koraga source records {n:,}.")
        )
    import difflib
    close = difflib.get_close_matches(key, [k for k in READINGS if not _is_malayalam(k)], n=1, cutoff=0.75)
    hint = ""
    if close:
        n = READINGS[close[0]][0][0]
        hint = f" The closest recorded form is for {n:,}."
    raise ValueError("Not a Koraga number recorded in the sources." + hint)


def koraga_to_number(text: str) -> int:
    """The value of a recorded form — entry point for the audits."""
    return koraga_lookup(text)[0][0]
