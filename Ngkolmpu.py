"""
Ngkolmpu.py — Ngkolmpu (Kanum) numerals: data and logic for the converter page.

Ngkolmpu, a Yam language of southern Papua, Indonesia, counts in sixes and has
single words for the powers of six up to 6^5 = 7,776.

Sources
  Carroll (2016), The Ngkolmpu Language with special reference to distributed
      exponence, PhD thesis, ANU: Table 1.3 (1-6 and the powers) and section 1.4.
  Carroll (2018), "How to count to 1296 in Ngkolmpu", Surrey Morphology Group
      blog, and his 2019 entry in Chan's Numeral Systems of the World's
      Languages: 7, 8 and 13, and the pattern for 7-35.
  Donohue (2008), from fieldwork in 1996, as reproduced in Carroll (2016)
      Table 1.2 and in Evans (2009) Table 4 and note 11: three older series.

Carroll's speakers use the powers only as powers. In Donohue's data the same
words also counted cycles of six (ptae 6 or 36, tarwmpao 12 or 216 ...);
both are shown, each with its source.
"""

from __future__ import annotations
import re

MAX_COUNT = 35           # k sixes and r, k <= 5
POWERS_OF_SIX = (36, 216, 1296, 7776)

# ── Carroll (2016, 2018, 2019) ───────────────────────────────────────────────
UNITS = {1: "naempr", 2: "yempoka", 3: "yuow", 4: "eser", 5: "tampui", 6: "traowo"}
SIX = UNITS[6]
POWERS = {36: "ptae", 216: "tarumpao", 1296: "ntamnao", 7776: "ulamaeke"}
CARROLL_RECORDED = set(UNITS) | {7, 8, 13} | set(POWERS)

UNIT_GLOSS = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}
POWER_GLOSS = {36: "6²", 216: "6³", 1296: "6⁴", 7776: "6⁵"}

# ── Donohue (2008), in his orthography ───────────────────────────────────────
D_SIMPLE = {1: "naempr", 2: "yempoka", 3: "ywow", 4: "eser", 5: "swabra", 6: "swy"}
D_MODERATE = {1: "aempy", 2: "ynaoaempy", 3: "ylla", 4: "eser", 5: "tampwy", 6: "traowao"}
D_MODERATE_SIX = "psymery"
D_COMPLEX = {1: "aempy", 2: "ynaoaempy", 3: "ylla", 4: "eser", 5: "tamp"}
D_CYCLE = {6: "ptae", 12: "tarwmpao", 18: "ntamnao", 24: "wramaekr"}
D_POWERS = {36: "ptae", 216: "tarwmpao", 1296: "ntamnao", 7776: "wramaekr"}
# Values printed in Carroll's Table 1.2 or as examples in Evans (2009);
# the rest of 13-35 follow Evans's generalisation of Donohue's data.
D_COMPLEX_RECORDED = set(range(1, 13)) | {15, 16, 18, 19, 24, 25, 30, 31} | set(D_POWERS)


def _check(n: int) -> None:
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"Expected int, got {type(n).__name__}")
    if n < 0:
        raise ValueError("Negative numbers are not supported.")
    if n == 0:
        raise ValueError("Carroll records no Ngkolmpu word for zero.")
    if n > 7776:
        raise ValueError(
            "7,776 (ulamaeke, 6⁵) is the highest number word Carroll records. "
            "The related language Komnzo goes one step further, with wi for 46,656."
        )
    if MAX_COUNT < n and n not in POWERS:
        raise ValueError(
            f"Carroll records single words for 36, 216, 1,296 and 7,776 but not how the "
            f"numbers between them are built, so {n:,} is not written out. Speakers he "
            f"worked with count the first 36 yams in Ngkolmpu and go on in Indonesian."
        )


def number_to_ngkolmpu(n: int) -> str:
    """Ngkolmpu as Carroll records it: 1-35 and the powers of six to 7,776."""
    _check(n)
    if n in POWERS:
        return POWERS[n]
    if n <= 6:
        return UNITS[n]
    sixes, rest = divmod(n, 6)
    head = f"{UNITS[sixes]} {SIX}"
    return head if rest == 0 else f"{head} {UNITS[rest]}"


def literal(n: int) -> str:
    """Carroll's style of gloss: 13 -> 'two six and one'."""
    _check(n)
    if n in POWERS:
        return f"{POWER_GLOSS[n]}, a single word"
    if n < 6:
        return UNIT_GLOSS[n]
    if n == 6:
        return "six"
    sixes, rest = divmod(n, 6)
    head = f"{UNIT_GLOSS[sixes]} six"
    return head if rest == 0 else f"{head} and {UNIT_GLOSS[rest]}"


def source_note(n: int) -> str:
    _check(n)
    if n in POWERS or n <= 6:
        return "Carroll (2016), Table 1.3"
    if n in CARROLL_RECORDED:
        return "Carroll (2018; 2019 in Chan's database)"
    return "built by the pattern Carroll describes; he gives 7, 8 and 13"


def base_six(n: int) -> str:
    digits = ""
    while n:
        n, d = divmod(n, 6)
        digits = str(d) + digits
    return digits or "0"


def donohue_forms(n: int) -> list[tuple[str, str, str]]:
    """Donohue's (2008) forms for n as (series, form, note)."""
    _check(n)
    out = []
    if n in D_SIMPLE:
        out.append(("simple", D_SIMPLE[n], "Carroll (2016), Table 1.2"))
    if n <= 12:
        form = D_MODERATE[n] if n <= 6 else f"{D_MODERATE_SIX} {D_MODERATE[n - 6]}"
        out.append(("moderate", form, "Carroll (2016), Table 1.2"))
    complex_form = None
    if n in D_POWERS:
        complex_form = D_POWERS[n]
    elif n <= 5:
        complex_form = D_COMPLEX[n]
    elif n <= MAX_COUNT:
        step, rest = divmod(n, 6)
        if step == 5:
            # 30 is ptae wramaekr, 6 + 24 (Evans 2009, note 11)
            base = f"{D_CYCLE[6]} {D_CYCLE[24]}"
        else:
            base = D_CYCLE[step * 6]
        complex_form = base if rest == 0 else f"{D_COMPLEX[rest]} {base}"
    if complex_form:
        note = ("Carroll (2016), Table 1.2" if n <= 12 or n in (18, 24) or n in D_POWERS
                else "Evans (2009)" if n in D_COMPLEX_RECORDED
                else "following Evans's (2009) account of Donohue's data")
        out.append(("complex", complex_form, note))
    return out


def donohue_strings(n: int) -> list[str]:
    """Donohue's forms as plain strings (used by the page checks)."""
    return [form for _, form, _ in donohue_forms(n)]


def counting_steps(n: int) -> tuple[int, int]:
    """(sixes, ones) for 1-35."""
    return divmod(n, 6)


# ── Reading Ngkolmpu ─────────────────────────────────────────────────────────
def _normalise(text: str) -> str:
    t = text.strip().lower().replace("æ", "ae")
    t = re.sub(r"\s+", " ", t)
    return t.replace("ulam aeke", "ulamaeke")


def _build_readings() -> dict[str, list[tuple[int, str]]]:
    table: dict[str, list[tuple[int, str]]] = {}

    def add(form: str, n: int, label: str) -> None:
        entry = table.setdefault(_normalise(form), [])
        if (n, label) not in entry:
            entry.append((n, label))

    for n in list(range(1, MAX_COUNT + 1)) + list(POWERS):
        add(number_to_ngkolmpu(n), n, "Carroll")
        for series, form, _ in donohue_forms(n):
            add(form, n, f"Donohue, {series} series")
    add(f"{UNITS[1]} {SIX}", 6, "Carroll's pattern")
    return table


READINGS = _build_readings()
VOCABULARY = {w for form in READINGS for w in form.split()}


def ngkolmpu_lookup(text: str) -> list[tuple[int, str]]:
    """Every (value, source) reading of a form, Carroll's first."""
    t = _normalise(text)
    if not t:
        raise ValueError("Empty input.")
    if t in READINGS:
        order = {"Carroll": 0, "Carroll's pattern": 1}
        return sorted(READINGS[t], key=lambda r: (order.get(r[1], 2), r[0]))
    unknown = [w for w in t.split() if w not in VOCABULARY]
    if unknown:
        import difflib
        hints = []
        for w in unknown:
            close = difflib.get_close_matches(w, sorted(VOCABULARY), n=1, cutoff=0.7)
            hints.append(f"'{w}'" + (f" (did you mean '{close[0]}'?)" if close else ""))
        raise ValueError("Not a recorded Ngkolmpu numeral word: " + ", ".join(hints) + ".")
    raise ValueError(
        "These are Ngkolmpu number words, but not in a recorded combination. Carroll's "
        "pattern puts the number of sixes first, then traowo 'six', then the rest: "
        "yempoka traowo naempr is 13."
    )


def ngkolmpu_to_number(text: str) -> int:
    """The main reading (Carroll's where there is one) — entry point for the audits."""
    return ngkolmpu_lookup(text)[0][0]
