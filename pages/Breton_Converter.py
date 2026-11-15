import difflib
import re

import streamlit as st

from ui import apply_global_styles, language_nav, CONV_CSS_ADDITIONS, footer_nav

# ============================================================
# BRETON NUMERAL CONVERTER
#
# Standard written Breton (peurunvan spelling). Counting goes by
# twenties up to 100: 40 is daou-ugent "two twenties", 60 tri-ugent,
# 80 pevar-ugent. 30 (tregont) and 50 (hanter-kant, "half a hundred")
# are the exceptions, and 18 is triwec'h, "three sixes". The unit
# comes first: unan warn-ugent, "one on twenty", is 21.
#
# The range is 0 to 9,999. Press (2009) gives the rules up to 1,999
# and the round thousands to 9,000. No source used here gives a rule
# for a number such as 25,000, where the noun-like mil could split the
# numeral the way a noun does (pemp kador ha tregont, "35 chairs"), so
# the converter stops rather than guess.
#
# Where the grammars give more than one form (ha or hag before
# hanter-kant, kant tri or tri ha kant, c'hwec'h-ugent for 120,
# daouzek kant for 1200, Vannetais daou gant) the main output is the
# form Press lists first, and the others are shown beside it.
#
# Sources: Press (2009); Favereau (1997); Jouitteau, ARBRES;
# pronunciation from Gwendal Denis, in Chan's numeral database.
# ============================================================

MAX_N = 9999
ZERO = "mann"

UNITS = {
    1: "unan", 2: "daou", 3: "tri", 4: "pevar", 5: "pemp",
    6: "c'hwec'h", 7: "seizh", 8: "eizh", 9: "nav", 10: "dek",
    11: "unnek", 12: "daouzek", 13: "trizek", 14: "pevarzek", 15: "pemzek",
    16: "c'hwezek", 17: "seitek", 18: "triwec'h", 19: "naontek",
}

# Only 2, 3 and 4 have feminine forms, used with a feminine noun.
FEMININE = {2: "div", 3: "teir", 4: "peder"}

TENS = {
    20: "ugent", 30: "tregont", 40: "daou-ugent",
    50: "hanter-kant", 60: "tri-ugent", 80: "pevar-ugent",
}

# kant becomes c'hant after daou, tri, pevar and nav.
HUNDREDS = {
    1: "kant", 2: "daou c'hant", 3: "tri c'hant", 4: "pevar c'hant",
    5: "pemp kant", 6: "c'hwec'h kant", 7: "seizh kant", 8: "eizh kant",
    9: "nav c'hant",
}

# mil becomes vil after daou.
THOUSANDS = {
    1: "mil", 2: "daou vil", 3: "tri mil", 4: "pevar mil", 5: "pemp mil",
    6: "c'hwec'h mil", 7: "seizh mil", 8: "eizh mil", 9: "nav mil",
}

# 120 to 199 can also be counted in twenties (Press 2009; Gourmelon 2014).
# Twelve twenties is attested once, for 240, in Favereau's spelling.
SCORES = {6: "c'hwec'h-ugent", 7: "seizh-ugent", 8: "eizh-ugent", 9: "nav-ugent",
          12: "daouzeg-ugent"}

UNIT_GLOSS = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
    7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven",
    12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
    16: "sixteen", 17: "seventeen", 18: "three sixes", 19: "nineteen",
}
TENS_GLOSS = {
    20: "twenty", 30: "thirty", 40: "two twenties", 50: "half a hundred",
    60: "three twenties", 80: "four twenties",
}

# Gwendal Denis (Rennes 2), in Chan's database. Two bracketed forms
# for 10-17 are Denis's own pair. Unbalanced brackets in his 24 and
# 40 are repaired; 26 and the numbers he did not record have none.
IPA = {
    1: "[ˈyːnɑ̃n]",
    2: "[dou̯]",
    3: "[triː]",
    4: "[ˈpɛːvar]",
    5: "[pɛm(p)]",
    6: "[xwɛːx]",
    7: "[sei̯s]",
    8: "[ei̯s]",
    9: "[nao̯]",
    10: "[dek] ~ [deːɡ]",
    11: "[ˈœ̃nɛk] ~ [ˈœ̃nɛɡ]",
    12: "[ˈdɔu̯zɛk] ~ [ˈdɔu̯zɛɡ]",
    13: "[ˈtriːzɛk] ~ [ˈtriːzɛɡ]",
    14: "[pɛˈvarzɛk] ~ [pɛˈvarzɛɡ]",
    15: "[ˈpɛmzɛk] ~ [ˈpɛmzɛɡ]",
    16: "[ˈxweːzɛk] ~ [ˈxweːzɛɡ]",
    17: "[ˈsei̯tɛk] ~ [ˈsei̯tɛɡ]",
    18: "[ˈtriwɛx]",
    19: "[ˈnao̯tɛk]",
    20: "[ˈyːɡɛn(t)]",
    21: "[ˈyːnɑ̃n warˈnyːɡɛn(t)]",
    22: "[ˈdou̯ warˈnyːɡɛn(t)]",
    23: "[ˈtriː warˈnyːɡɛn(t)]",
    24: "[ˈpɛvar warˈnyːɡɛn(t)]",
    25: "[ˈpɛmp warˈnyːɡɛnt]",
    27: "[ˈsei̯z warˈnyːɡɛn(t)]",
    28: "[ˈei̯z warˈnyːɡɛn(t)]",
    29: "[ˈnao̯ warˈnyːɡɛn(t)]",
    30: "[ˈtreːɡɔn]",
    40: "[dou̯ˈyːɡɛn]",
    50: "[ˈhɑ̃ntɛr ˈkɑ̃n]",
    60: "[ˈtriˈyːɡɛn]",
    70: "[ˈdɛɡ a triˈyːɡɛn]",
    80: "[ˈpɛːvar ˈyːɡɛn]",
    90: "[ˈdɛɡ a pɛːvar ˈyːɡɛn]",
    100: "[kɑ̃n]",
    200: "[ˈdou̯ ˈxɑ̃n]",
    1000: "[ˈmil]",
    2000: "[dou̯ ˈvil]",
}
IPA_FEMININE = {2: "[diw]", 3: "[tei̯r]", 4: "[ˈpeːdɛr]"}

# What each tag on an accepted form means, for the reverse direction.
VARIANT_NOTES = {
    "feminine": "Feminine form, used with a feminine noun",
    "hag": "hag before hanter-kant: Press writes ha(g); Favereau gives ha and hag as regional variants",
    "un": "un, the shortened form of unan (Press 2009; Favereau 1997)",
    "eitek": "eitek, a regular form of 18 that Favereau (1997) reports as attested",
    "ha kant": "Unit before kant, the alternative order Press and Favereau give for 101 to 119",
    "score": "Counted in twenties past 100: Press (2009) and Gourmelon (2014) give 120 to 199, and Favereau (1997) cites 240",
    "hundreds": "Counted in hundreds, which Press (2009) calls normal between 1001 and 1999",
    "gwenedeg": "daou gant, the Gwenedeg (Vannetais) form of 200 (Press 2009; Favereau 1997)",
    "half": "hanter 'half' added to the hundreds, as in Favereau's trizek kant hanter, 1,350 (1997, §870)",
}

# Forms attested for one value only, offered for that value alone:
# hundreds plus hanter "half", and twelve twenties.
SINGLE_ATTESTATIONS = {
    150: ("kant hanter", "a hundred and a half (Verdier 2010; cf. Favereau 1997, §870)", "half"),
    240: ("daouzeg-ugent", "twelve twenties (Favereau 1997, citing Trépos)", "score"),
    1350: ("trizek kant hanter", "thirteen hundred and a half (Favereau 1997, §870)", "half"),
}


def check_range(n):
    if n < 0:
        raise ValueError("Enter a whole number from 0 to 9,999.")
    if n > MAX_N:
        raise ValueError(
            f"{n:,} is above this converter's range of 0 to 9,999. Breton writes round "
            f"thousands such as dek mil (10,000) and kant mil (100,000), but the grammars "
            f"used here give no rule for a number like 25,000. A noun can split a Breton "
            f"numeral (pemp kador ha tregont, '35 chairs'), and mil often behaves like a "
            f"noun, so the converter stops rather than guess where it goes."
        )


def split_tens(r):
    """1-99 as (unit, tens): the tens word a unit is added to."""
    for base in (80, 60, 50, 40, 30, 20):
        if r >= base:
            return r - base, base
    return r, 0


def unit_word(u, feminine=False):
    return FEMININE[u] if feminine and u in FEMININE else UNITS[u]


def below_100(r, feminine=False, hag=False):
    u, t = split_tens(r)
    if t == 0:
        return unit_word(u, feminine)
    if u == 0:
        return TENS[t]
    if t == 20:
        return f"{unit_word(u, feminine)} warn-ugent"
    link = "hag" if hag and t == 50 else "ha"
    return f"{unit_word(u, feminine)} {link} {TENS[t]}"


def number_to_breton(n, feminine=False):
    """The main written form, as Press (2009) lists it first."""
    check_range(n)
    if n == 0:
        return ZERO
    th, rest = divmod(n, 1000)
    h, r = divmod(rest, 100)
    parts = []
    if th:
        parts.append(THOUSANDS[th])
    if h:
        parts.append(HUNDREDS[h])
    if r:
        parts.append(below_100(r, feminine))
    return " ".join(parts)


def final_unit(n):
    """The unit that agrees with a following noun, or None."""
    r = n % 100
    if r == 0:
        return None
    u, _ = split_tens(r)
    return u or None


def has_feminine(n):
    return final_unit(n) in FEMININE


def score_form(n, feminine=False):
    s, r = divmod(n, 20)
    if r == 0:
        return SCORES[s]
    return f"{unit_word(r, feminine)} ha {SCORES[s]}"


def hundreds_form(n, feminine=False):
    h, r = divmod(n, 100)
    head = f"{UNITS[h]} kant"
    return head if r == 0 else f"{head} {below_100(r, feminine)}"


def breton_alternatives(n):
    """Other attested forms of n, each with what makes it different."""
    check_range(n)
    th, rest = divmod(n, 1000)
    h, r = divmod(rest, 100)
    out = []
    if n == 18:
        out.append(("eitek", "regular form, attested (Favereau 1997)"))
    if 51 <= r <= 59:
        main = number_to_breton(n)
        out.append((main.replace(" ha hanter-kant", " hag hanter-kant"),
                    "hag before hanter-kant, a regional variant (Press 2009; Favereau 1997)"))
    if th == 0 and h == 1 and 1 <= r <= 19:
        out.append((f"{UNITS[r]} ha kant", "unit before kant (Press 2009; Favereau 1997)"))
    if 120 <= n <= 199:
        out.append((score_form(n), "counted in twenties (Press 2009; Gourmelon 2014)"))
    if n in SINGLE_ATTESTATIONS:
        out.append(SINGLE_ATTESTATIONS[n][:2])
    if th == 1 and h >= 1:
        out.append((hundreds_form(n), "counted in hundreds, normal from 1001 to 1999 (Press 2009)"))
    if h == 2:
        out.append((number_to_breton(n).replace("daou c'hant", "daou gant"),
                    "Gwenedeg (Vannetais) daou gant (Press 2009; Favereau 1997)"))
    return out


def breton_alternative_forms(n):
    return [form for form, _ in breton_alternatives(n)]


# ── Reverse direction ──────────────────────────────────────
def _unit_variants(u, allow_un=True):
    yield UNITS[u], frozenset()
    if u in FEMININE:
        yield FEMININE[u], frozenset({"feminine"})
    if u == 1 and allow_un:
        yield "un", frozenset({"un"})


def _below_100_variants(r):
    u, t = split_tens(r)
    if t == 0:
        yield from _unit_variants(u)
        return
    if u == 0:
        yield TENS[t], frozenset()
        return
    links = [("ha", frozenset()), ("hag", frozenset({"hag"}))] if t == 50 else [("ha", frozenset())]
    for word, tags in _unit_variants(u):
        if t == 20:
            yield f"{word} warn-ugent", tags
        else:
            for link, ltags in links:
                yield f"{word} {link} {TENS[t]}", tags | ltags


def all_forms(n):
    """Every form of n that the parser accepts, with its variant tags."""
    if n == 0:
        return [(ZERO, frozenset())]
    th, rest = divmod(n, 1000)
    h, r = divmod(rest, 100)
    heads = [([], frozenset())]
    if th:
        heads = [([THOUSANDS[th]], frozenset())]
    if h:
        hundred_words = [(HUNDREDS[h], frozenset())]
        if h == 2:
            hundred_words.append(("daou gant", frozenset({"gwenedeg"})))
        new_heads = [(p + [w], t | wt) for p, t in heads for w, wt in hundred_words]
        if th == 1:
            new_heads.append(([f"{UNITS[10 + h]} kant"], frozenset({"hundreds"})))
        heads = new_heads
    tails = list(_below_100_variants(r)) if r else [("", frozenset())]
    forms = []
    for p, pt in heads:
        for w, wt in tails:
            forms.append((" ".join(p + ([w] if w else [])), pt | wt))
    if th == 0 and h == 1 and 1 <= r <= 19:
        for word, tags in _unit_variants(r):
            forms.append((f"{word} ha kant", tags | {"ha kant"}))
    if 120 <= n <= 199:
        s, rr = divmod(n, 20)
        if rr == 0:
            forms.append((SCORES[s], frozenset({"score"})))
        else:
            for word, tags in _unit_variants(rr):
                forms.append((f"{word} ha {SCORES[s]}", tags | {"score"}))
    if n == 18:
        forms.append(("eitek", frozenset({"eitek"})))
    if n in SINGLE_ATTESTATIONS:
        form, _, tag = SINGLE_ATTESTATIONS[n]
        forms.append((form, frozenset({tag})))
    return forms


APOSTROPHES = "\u2019\u02bc\u2018\u00b4`"


def normalise(text):
    t = text.strip().lower()
    for a in APOSTROPHES:
        t = t.replace(a, "'")
    t = t.replace("\u0261", "g")  # script g, as in Chan's transcriptions
    t = re.sub(r"[-\u2010-\u2014]", " ", t)
    t = re.sub(r"\bhanterkant\b", "hanter kant", t)  # Favereau's one-word spelling
    # -g for -k in the tens and teens, as Favereau and older texts write them
    t = re.sub(r"\b(d|unn|daouz|triz|pevarz|pemz|c'hwez|seit|naont)eg\b", r"\1ek", t)
    t = re.sub(r"[.,;:!?]+$", "", t)
    return re.sub(r"\s+", " ", t).strip()


def _build_accept():
    table = {}
    for n in range(MAX_N + 1):
        for form, tags in all_forms(n):
            key = normalise(form)
            if key in table and table[key][0] != n:
                raise RuntimeError(f"'{form}' would mean both {table[key][0]} and {n}")
            table.setdefault(key, (n, tags))
    return table


ACCEPT = _build_accept()
VOCAB = {w for key in ACCEPT for w in key.split()}

# Common slips, each with the rule it breaks.
HINTS = [
    (r"\b(daou|tri|pevar|nav) kant\b",
     "kant changes to c'hant after daou, tri, pevar and nav: daou c'hant (200), "
     "tri c'hant (300), nav c'hant (900)."),
    (r"\bdaou mil\b", "mil changes to vil after daou: daou vil (2,000)."),
    (r"\b(tri|pevar|nav) vil\b", "Only daou changes mil to vil: tri mil, pevar mil, nav mil."),
    (r"\b(div|teir|peder) (ugent|c'hant|kant|mil|vil)\b",
     "ugent, kant and mil are masculine, so they take daou, tri, pevar: daou-ugent (40), "
     "tri c'hant (300), pevar mil (4,000)."),
    (r"\b(ugent|tregont|daou ugent|hanter kant|tri ugent|pevar ugent) (ha |warn )?(unan|daou|tri|pevar|pemp|c'hwec'h|seizh|eizh|nav|dek)$",
     "Breton puts the unit first: unan warn-ugent (21), pemp ha tregont (35), "
     "dek ha pevar-ugent (90)."),
]


def parse_breton(text):
    """Returns (n, tags) for a Breton numeral, or raises ValueError."""
    key = normalise(text)
    if not key:
        raise ValueError("Enter a Breton numeral, for example pemp ha tregont.")
    if re.search(r"\d", key):
        raise ValueError("That contains digits. Switch the direction to Arabic → Breton to convert a number.")
    if key in ACCEPT:
        return ACCEPT[key]
    tokens = key.split()
    if "milion" in tokens or "miliard" in tokens:
        raise ValueError(
            "milion and miliard are nouns in Breton (ur milion a dud, 'a million people'), "
            "and numbers that large are outside this converter's range of 0 to 9,999."
        )
    if "mil" in tokens:
        left = " ".join(tokens[:tokens.index("mil")])
        if left in ACCEPT and ACCEPT[left][0] >= 10:
            check_range(ACCEPT[left][0] * 1000)
    for pattern, hint in HINTS:
        if re.search(pattern, key):
            raise ValueError(hint)
    unknown = [w for w in tokens if w not in VOCAB]
    if unknown:
        guesses = []
        for w in unknown:
            close = difflib.get_close_matches(w, VOCAB, n=1, cutoff=0.75)
            if close:
                guesses.append(f"{w} → {close[0]}")
        msg = f"Not a Breton numeral word: {', '.join(unknown)}."
        if guesses:
            msg += f" Did you mean {'; '.join(guesses)}?"
        raise ValueError(msg)
    raise ValueError(
        "Every word is a Breton numeral, but not in an order the grammars give. Thousands "
        "come first, then hundreds, then the rest, and the unit comes before its twenty: "
        "mil nav c'hant pevar ha pevar-ugent (1984)."
    )


def breton_to_number(text):
    return parse_breton(text)[0]


# ── Explanations ───────────────────────────────────────────
def literal(n, style="main"):
    """An English word-for-word reading of the form shown."""
    if n == 0:
        return "nothing"

    def small(r):
        u, t = split_tens(r)
        if t == 0:
            return UNIT_GLOSS[u]
        if u == 0:
            return TENS_GLOSS[t]
        if t == 20:
            return f"{UNIT_GLOSS[u]} on twenty"
        return f"{UNIT_GLOSS[u]} and {TENS_GLOSS[t]}"

    th, rest = divmod(n, 1000)
    h, r = divmod(rest, 100)
    if style == "score":
        s, rr = divmod(n, 20)
        twenties = f"{UNIT_GLOSS[s]} twenties"
        return twenties if rr == 0 else f"{UNIT_GLOSS[rr]} and {twenties}"
    if style == "ha kant":
        return f"{UNIT_GLOSS[r]} and a hundred"
    if style == "half":
        hundreds = n // 100
        return f"{'a' if hundreds == 1 else UNIT_GLOSS[hundreds]} hundred and a half"
    parts = []
    if style == "hundreds":
        parts.append(f"{UNIT_GLOSS[10 + h]} hundred")
    else:
        if th:
            parts.append("a thousand" if th == 1 else f"{UNIT_GLOSS[th]} thousand")
        if h:
            parts.append("a hundred" if h == 1 else f"{UNIT_GLOSS[h]} hundred")
    if r:
        parts.append(small(r))
    return ", ".join(parts)


def breakdown(n, style="main", feminine=False):
    """Rows of (Breton, how it counts, value) for the form shown."""
    rows = []

    def unit_row(u):
        how = "3 × 6" if u == 18 else ""
        rows.append((unit_word(u, feminine), how, u))

    def small(r):
        u, t = split_tens(r)
        if t == 0:
            unit_row(u)
            return
        if u == 0:
            how = {40: "2 × 20", 50: "½ × 100", 60: "3 × 20", 80: "4 × 20"}.get(t, "")
            rows.append((TENS[t], how, t))
            return
        unit_row(u)
        if t == 20:
            rows.append(("warn-ugent", "on 20", 20))
        else:
            how = {30: "and 30", 40: "and 2 × 20", 50: "and ½ × 100",
                   60: "and 3 × 20", 80: "and 4 × 20"}[t]
            rows.append((f"ha {TENS[t]}", how, t))

    th, rest = divmod(n, 1000)
    h, r = divmod(rest, 100)
    if n == 0:
        return [(ZERO, "", 0)]
    if style == "score":
        s, rr = divmod(n, 20)
        if rr:
            unit_row(rr)
            rows.append((f"ha {SCORES[s]}", f"and {s} × 20", s * 20))
        else:
            rows.append((SCORES[s], f"{s} × 20", n))
        return rows
    if style == "ha kant":
        unit_row(r)
        rows.append(("ha kant", "and 100", 100))
        return rows
    if style == "half":
        hundreds = n // 100
        head = SINGLE_ATTESTATIONS[n][0].rsplit(" ", 1)[0]
        rows.append((head, f"{hundreds} × 100" if hundreds > 1 else "", hundreds * 100))
        rows.append(("hanter", "half of 100", 50))
        return rows
    if style == "hundreds":
        rows.append((f"{UNITS[10 + h]} kant", f"{10 + h} × 100", (10 + h) * 100))
    else:
        if th:
            rows.append((THOUSANDS[th], f"{th} × 1,000" if th > 1 else "", th * 1000))
        if h:
            word = "daou gant" if style == "gwenedeg" and h == 2 else HUNDREDS[h]
            rows.append((word, f"{h} × 100" if h > 1 else "", h * 100))
    if r:
        small(r)
    return rows


def style_of(tags):
    for s in ("score", "ha kant", "half", "hundreds", "gwenedeg"):
        if s in tags:
            return s
    return "main"


def pronunciation(n):
    if n not in IPA:
        return None
    if n in IPA_FEMININE:
        return (f"{IPA[n]} <span class='bre-muted'>masc.</span> &nbsp;·&nbsp; "
                f"{IPA_FEMININE[n]} <span class='bre-muted'>fem.</span>")
    return IPA[n]


# ============================================================
# PAGE CONFIG & STYLES
# ============================================================
st.set_page_config(page_title="Breton Numeral Converter", layout="wide")
apply_global_styles()

CONV_CSS = """<style>
/* Charis SIL subset to the IPA characters used; the default subsets omit U+032F. */
@import url('https://fonts.googleapis.com/css2?family=Charis+SIL&text=%20%28%29%5B%5Dadehiklmnoprstuvwxyz~%C5%93%C9%91%C9%94%C9%9B%C9%A1%CB%88%CB%90%CC%83%CC%AF%E2%80%94&display=swap');
.conv-masthead{border-top:3px solid var(--ink);border-bottom:1px solid var(--rule);padding:1.75rem 0 1.4rem 0;margin-bottom:1.75rem}
.conv-masthead-eyebrow{font-family:'DM Sans',sans-serif;font-size:.68rem;font-weight:700;text-transform:uppercase;letter-spacing:.18em;color:var(--accent);display:flex;align-items:center;gap:.65rem;margin-bottom:.65rem}
.conv-masthead-eyebrow::before{content:'';display:inline-block;width:1.75rem;height:1.5px;background:var(--accent);flex-shrink:0}
.conv-masthead-title{font-family:'Crimson Pro',Georgia,serif;font-size:3rem;font-weight:700;color:var(--ink);letter-spacing:-.04em;line-height:1.05;margin-bottom:.5rem}
.conv-masthead-desc{font-family:'Crimson Pro',Georgia,serif;font-style:italic;font-size:1.05rem;color:var(--ink-muted);line-height:1.55;margin:0}
.conv-section-label{font-family:'DM Sans',sans-serif;font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.16em;color:var(--ink-soft);display:flex;align-items:center;gap:1rem;margin:2rem 0 1rem 0}
.conv-section-label::before{content:'';display:inline-block;width:2rem;height:1px;background:var(--ink-muted);flex-shrink:0}
.conv-section-label::after{content:'';flex:1;height:1px;background:var(--rule)}
div[data-testid="stRadio"]>div{display:flex;gap:0;background:var(--card-bg);border:1px solid var(--card-border);border-radius:6px;padding:.35rem;box-shadow:0 1px 3px rgba(26,22,18,.05),0 4px 14px rgba(26,22,18,.04),inset 0 1px 0 rgba(255,255,255,.65);width:fit-content;flex-wrap:wrap}
div[data-testid="stRadio"] label{display:flex!important;align-items:center!important;font-family:'DM Sans',sans-serif!important;font-size:.9rem!important;font-weight:600!important;letter-spacing:.02em!important;text-transform:none!important;color:var(--ink-soft)!important;background:transparent!important;border:1.5px solid transparent!important;border-radius:4px!important;padding:.55rem 1.35rem!important;cursor:pointer!important;transition:all .18s cubic-bezier(.4,0,.2,1)!important;white-space:nowrap!important}
div[data-testid="stRadio"] label>span:first-child{display:none!important}
div[data-testid="stRadio"] label:hover{background:var(--parchment-3)!important;border-color:var(--rule-strong)!important;color:var(--ink)!important}
div[data-testid="stRadio"] label:has(input:checked){background:var(--ink)!important;border-color:var(--ink)!important;box-shadow:3px 3px 0 var(--accent)!important;transform:translate(-1px,-1px)!important}
div[data-testid="stRadio"] label:has(input:checked) p,div[data-testid="stRadio"] label:has(input:checked) span{color:var(--parchment)!important}
div[data-testid="stRadio"] label p{font-family:'DM Sans',sans-serif!important;font-size:.9rem!important;font-weight:600!important;margin:0!important;line-height:1!important}
.conv-presets-sublabel{font-family:'DM Sans',sans-serif;font-size:.65rem;font-weight:700;text-transform:uppercase;letter-spacing:.14em;color:var(--ink-faint);margin-bottom:.65rem;margin-top:0}
.conv-input-card{background:var(--card-bg);border:1px solid var(--card-border);border-radius:6px;padding:1.3rem 1.5rem 1.4rem;margin-bottom:.5rem;box-shadow:0 1px 3px rgba(26,22,18,.05),0 6px 20px rgba(26,22,18,.06),inset 0 1px 0 rgba(255,255,255,.7)}
.conv-input-title{font-family:'Crimson Pro',Georgia,serif;font-size:1.3rem;font-weight:600;color:var(--ink);letter-spacing:-.02em;margin:0 0 .25rem 0;line-height:1.2}
.conv-input-hint{font-family:'Crimson Pro',Georgia,serif;font-style:italic;font-size:.93rem;color:var(--ink-faint);margin:0 0 .8rem 0;line-height:1.4}
.conv-result-card{background:rgba(46,107,122,.04);border:1px solid rgba(46,107,122,.18);border-left:3px solid var(--teal);border-radius:0 4px 4px 0;padding:.85rem 1.1rem;margin-top:.8rem}
.conv-result-label{font-family:'DM Sans',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.14em;color:var(--teal);margin-bottom:.55rem}
.conv-result-row{display:grid;grid-template-columns:7.5rem 1fr;gap:.35rem .9rem;align-items:baseline;padding:.15rem 0}
.conv-result-sublabel{font-family:'DM Sans',sans-serif;font-size:.62rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--ink-faint)}
.conv-result-subvalue{font-family:'Crimson Pro',Georgia,serif;font-size:1.05rem;font-weight:400;color:var(--ink);line-height:1.55;word-break:break-word}
.conv-error-card{background:rgba(184,92,56,.05);border:1px solid rgba(184,92,56,.2);border-left:3px solid var(--accent);border-radius:0 4px 4px 0;padding:.75rem 1.1rem;margin-top:.8rem}
.conv-error-text{font-family:'Crimson Pro',Georgia,serif;font-size:1rem;color:var(--accent);font-style:italic;margin:0}
.conv-empty-state{font-family:'Crimson Pro',Georgia,serif;font-style:italic;color:var(--ink-faint);padding:1.1rem 0}
.conv-caption{font-family:'DM Sans',sans-serif;font-size:.75rem;color:var(--ink-faint);line-height:1.55;margin-top:1rem}
.bre-main{font-size:1.95rem;font-weight:600;letter-spacing:-.01em;line-height:1.25}
.bre-muted{font-family:'DM Sans',sans-serif;font-size:.72rem;color:var(--ink-faint);letter-spacing:.02em}
.bre-ipa{font-family:'Charis SIL',serif;font-size:1.2rem}
.bre-nw{white-space:nowrap}
.bre-tag{font-size:1.12rem;line-height:1.45;color:var(--ink-muted)}
.bre-alt{display:block;padding:.15rem 0;font-size:1.25rem;line-height:1.4}
.bre-alt .bre-muted{font-size:.74rem}
.bre-parts{background:var(--card-bg);border:1px solid var(--card-border);border-radius:6px;padding:.9rem 1.1rem;margin-top:.8rem}
.bre-parts-label{font-family:'DM Sans',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.13em;color:var(--ink-faint);margin-bottom:.5rem}
.bre-parts-row{display:grid;grid-template-columns:minmax(7rem,1.4fr) minmax(5rem,1fr) 4.5rem;gap:.3rem .8rem;align-items:baseline;padding:.3rem 0;border-bottom:1px solid var(--rule)}
.bre-parts-row:last-child{border-bottom:none}
.bre-parts-head{font-family:'DM Sans',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--ink-faint)}
.bre-parts-word{font-family:'Crimson Pro',Georgia,serif;font-style:italic;font-size:1.05rem;color:var(--ink)}
.bre-parts-how{font-family:'DM Sans',sans-serif;font-size:.82rem;color:var(--ink-muted)}
.bre-parts-val{font-family:'DM Mono','Courier New',monospace;font-size:.92rem;color:var(--ink);text-align:right}
.bre-parts-total .bre-parts-val{font-weight:700}
.bre-note{border:1px solid var(--rule);border-left:3px solid var(--ink-muted);background:var(--parchment-2);border-radius:0 4px 4px 0;padding:.7rem 1.05rem;margin-top:.8rem}
.bre-note-label{font-family:'DM Sans',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.13em;color:var(--ink-soft);margin-bottom:.3rem}
.bre-note p{font-family:'Crimson Pro',Georgia,serif;font-size:.97rem;color:var(--ink-muted);line-height:1.55;margin:0}
</style>"""
st.markdown(CONV_CSS, unsafe_allow_html=True)
st.markdown(CONV_CSS_ADDITIONS, unsafe_allow_html=True)

st.markdown("""
<div class="conv-masthead">
    <div class="conv-masthead-eyebrow">Numeral Converter</div>
    <div class="conv-masthead-title">Breton</div>
    <div class="conv-masthead-desc">Convert between Arabic numerals and Breton, a Celtic language of Brittany that counts in twenties, calls fifty “half a hundred” and eighteen “three sixes”.</div>
</div>
""", unsafe_allow_html=True)

language_nav("Breton", "converter")


# ── Result rendering ────────────────────────────────────────
def keep_whole(text):
    """Stop a hyphenated word such as pevar-ugent breaking at its hyphen."""
    return re.sub(r"(\S+-\S+)", r'<span class="bre-nw">\1</span>', text)


def rows_html(rows):
    return "".join(
        f'<div class="conv-result-row">'
        f'<span class="conv-result-sublabel">{label}</span>'
        f'<span class="conv-result-subvalue">{value}</span>'
        f"</div>"
        for label, value in rows
    )


def as_typed(word, tags):
    """Show the spelling variants the reader typed in the part-by-part table."""
    if "hag" in tags:
        word = word.replace("ha hanter-kant", "hag hanter-kant")
    if "un" in tags and word == "unan":
        word = "un"
    return word


def parts_html(n, style="main", feminine=False, tags=frozenset()):
    body = "".join(
        f'<div class="bre-parts-row">'
        f'<span class="bre-parts-word">{keep_whole(as_typed(word, tags))}</span>'
        f'<span class="bre-parts-how">{how}</span>'
        f'<span class="bre-parts-val">{value:,}</span>'
        f"</div>"
        for word, how, value in breakdown(n, style, feminine)
    )
    head = (
        '<div class="bre-parts-row">'
        '<span class="bre-parts-head">Breton</span>'
        '<span class="bre-parts-head">Counts as</span>'
        '<span class="bre-parts-head" style="text-align:right">Value</span></div>'
    )
    total = (
        '<div class="bre-parts-row bre-parts-total">'
        '<span class="bre-parts-head">Total</span><span></span>'
        f'<span class="bre-parts-val">{n:,}</span></div>'
    )
    return (
        f'<div class="bre-parts"><div class="bre-parts-label">Part by part</div>'
        f"{head}{body}{total}</div>"
    )


def note_html(label, text):
    return (
        f'<div class="bre-note"><div class="bre-note-label">{label}</div>'
        f"<p>{text}</p></div>"
    )


def error_html(msg):
    return f'<div class="conv-error-card"><p class="conv-error-text">{msg}</p></div>'


def notes_html(n, style="main"):
    out = []
    r = n % 100
    u, t = split_tens(r) if r else (0, 0)
    if style == "main" and u and t and n < 100:
        first, rest = below_100(r).split(" ", 1)
        out.append(note_html(
            "With a noun",
            f"A noun goes straight after the unit, splitting the numeral: "
            f"<em>{first} <strong>[noun]</strong> {keep_whole(rest)}</em>. Jouin's example is "
            f"<em>pemp kador ha tregont</em>, 'thirty-five chairs'; the noun stays "
            f"singular after any numeral."
            + (" Before a noun, <em>unan</em> becomes the article <em>ur</em>, <em>un</em> "
               "or <em>ul</em>: <em>ur bloaz ha tregont</em>, 'thirty-one years'."
               if u == 1 else ""),
        ))
    if u == 18 or (style == "score" and n % 20 == 18):
        out.append(note_html(
            "Eighteen",
            "<em>triwec'h</em> is <em>tri</em> 'three' and <em>c'hwec'h</em> 'six': three "
            "sixes. Old Breton had a regular 'eight-ten', <em>eithnec</em> (Greene 1992), "
            "and Favereau (1997) reports a regular <em>eitek</em> as attested. Welsh says "
            "<em>deunaw</em>, 'two nines'.",
        ))
    if 50 <= r <= 59 and style == "main":
        out.append(note_html(
            "Half a hundred",
            "<em>hanter-kant</em> is literally 'half a hundred'. Welsh has the same word, "
            "<em>hanner cant</em>. The other tens up to 100 are built on twenties, except "
            "<em>tregont</em>, 30.",
        ))
    h = (n // 100) % 10
    th = n // 1000
    if style in ("main", "gwenedeg") and (h in (2, 3, 4, 9) or th == 2):
        bits = []
        if h in (2, 3, 4, 9):
            bits.append(
                "<em>kant</em> becomes <em>c'hant</em> after <em>daou</em>, <em>tri</em>, "
                "<em>pevar</em> and <em>nav</em>; after <em>daou</em> this is an archaic "
                "mutation, and Gwenedeg (Vannetais) says <em>daou gant</em>"
                if h == 2 else
                "<em>kant</em> becomes <em>c'hant</em> after <em>tri</em>, <em>pevar</em> "
                "and <em>nav</em>"
            )
        if th == 2:
            bits.append("<em>mil</em> becomes <em>vil</em> after <em>daou</em>")
        out.append(note_html(
            "Mutation",
            "Breton changes the first sound of a word after certain other words. "
            + "; ".join(bits) + ".",
        ))
    if 101 <= n <= 199 and style == "main":
        out.append(note_html(
            "Which order?",
            "Press (2009) lists <em>kant</em> first, then the rest. He and Favereau (1997) "
            "also give the reverse for small additions (<em>tri ha kant</em>, 103), and "
            "Press gives twenties for 120 to 199 (<em>c'hwec'h-ugent</em>, 'six twenties'). "
            "All are shown under <em>Also written</em>.",
        ))
    return "".join(out)


def alternatives_html(n, skip=None):
    alts = [(f, why) for f, why in breton_alternatives(n) if normalise(f) != skip]
    if not alts:
        return None
    return "".join(
        f"<span class='bre-alt'><em>{keep_whole(f)}</em> <span class='bre-muted'>· {why}</span></span>"
        for f, why in alts
    )


direction = st.radio(
    "Direction",
    ["Arabic → Breton", "Breton → Arabic"],
    horizontal=True,
    label_visibility="collapsed",
    key="breton_direction",
)

left_col, right_col = st.columns([1, 1], gap="large")

arabic_input = ""
breton_input = ""

with left_col:
    st.markdown('<div class="conv-section-label">Preset Examples</div>', unsafe_allow_html=True)

    if direction == "Arabic → Breton":
        presets = ["18", "23", "50", "55", "70", "99", "120", "180", "200", "1499", "1984", "2024"]
        st.markdown('<p class="conv-presets-sublabel">Click a value to load it</p>', unsafe_allow_html=True)
        cols = st.columns(4)
        for i, val in enumerate(presets):
            if cols[i % 4].button(val, key=f"p_a_{i}", use_container_width=True):
                st.session_state["breton_arabic_input"] = val
        st.markdown("""
<div class="conv-caption" style="margin-top:.2rem">
<strong>1499</strong> — Jehan Lagadeuc's <em>Catholicon</em>, a Breton–French–Latin dictionary &nbsp;·&nbsp;
<strong>1984</strong> — the year Press (2009) spells out &nbsp;·&nbsp;
<strong>2024</strong> — the regional survey that counted 107,000 speakers
</div>""", unsafe_allow_html=True)

        st.markdown('<div class="conv-section-label">Convert</div>', unsafe_allow_html=True)
        st.markdown("""
<div class="conv-input-card">
    <div class="conv-input-title">Enter an Arabic numeral</div>
    <div class="conv-input-hint">A whole number from 0 to 9,999.</div>
</div>""", unsafe_allow_html=True)
        arabic_input = st.text_input(
            "Enter an Arabic numeral",
            key="breton_arabic_input",
            placeholder="e.g. 75",
            label_visibility="collapsed",
        )
    else:
        presets = [
            "triwec'h", "teir warn-ugent", "hanter-kant", "pemp hag hanter-kant",
            "dek ha pevar-ugent", "c'hwec'h-ugent", "nav-ugent", "daou c'hant",
            "pevarzek kant naontek ha pevar-ugent", "mil nav c'hant pevar ha pevar-ugent",
        ]
        st.markdown('<p class="conv-presets-sublabel">Click a value to load it</p>', unsafe_allow_html=True)
        cols = st.columns(2)
        for i, val in enumerate(presets):
            # A non-breaking hyphen in the label only, so pevar-ugent stays on one line.
            if cols[i % 2].button(val.replace("-", "\u2011"), key=f"p_b_{i}", use_container_width=True):
                st.session_state["breton_word_input"] = val

        st.markdown('<div class="conv-section-label">Convert</div>', unsafe_allow_html=True)
        st.markdown("""
<div class="conv-input-card">
    <div class="conv-input-title">Enter a Breton numeral</div>
    <div class="conv-input-hint">Standard spelling, such as <em>pemp ha tregont</em>. Feminine forms, regional variants and the other orders the grammars give are accepted too.</div>
</div>""", unsafe_allow_html=True)
        breton_input = st.text_input(
            "Enter a Breton numeral",
            key="breton_word_input",
            placeholder="e.g. pemp ha tregont",
            label_visibility="collapsed",
        )

with right_col:
    if direction == "Arabic → Breton":
        if arabic_input:
            try:
                s = arabic_input.strip().replace(",", "").replace(" ", "")
                if not re.fullmatch(r"-?\d+", s):
                    raise ValueError("Enter a whole number from 0 to 9,999.")
                n = int(s)
                main = number_to_breton(n)
                rows = [("Breton", f'<span class="bre-main">{keep_whole(main)}</span>')]
                if has_feminine(n):
                    rows.append(("Feminine", f"{keep_whole(number_to_breton(n, feminine=True))} "
                                             f"<span class='bre-muted'>· with a feminine noun</span>"))
                rows.append(("Literally", literal(n)))
                ipa = pronunciation(n)
                if ipa:
                    rows.append(("Pronunciation", f'<span class="bre-ipa">{ipa}</span>'))
                alts = alternatives_html(n)
                if alts:
                    rows.append(("Also written", alts))
                st.markdown(
                    f'<div class="conv-result-card"><div class="conv-result-label">Breton</div>'
                    f"{rows_html(rows)}</div>",
                    unsafe_allow_html=True,
                )
                st.markdown(parts_html(n), unsafe_allow_html=True)
                st.markdown(notes_html(n), unsafe_allow_html=True)
            except ValueError as exc:
                st.markdown(error_html(exc), unsafe_allow_html=True)
        else:
            st.markdown(
                '<div class="conv-empty-state"><p>Enter a value on the left to see the result.</p></div>',
                unsafe_allow_html=True,
            )
    else:
        if breton_input:
            try:
                n, tags = parse_breton(breton_input)
                style = style_of(tags)
                feminine = "feminine" in tags
                main = number_to_breton(n)
                rows = [("Arabic numeral", f'<span class="bre-main">{n:,}</span>')]
                if normalise(breton_input) != normalise(main):
                    rows.append(("Main form", keep_whole(main)))
                for tag in sorted(tags):
                    rows.append(("Your form", f'<span class="bre-tag">{VARIANT_NOTES[tag]}</span>'))
                rows.append(("Literally", literal(n, style)))
                ipa = pronunciation(n)
                if ipa and style == "main":
                    rows.append(("Pronunciation", f'<span class="bre-ipa">{ipa}</span>'))
                alts = alternatives_html(n, skip=normalise(breton_input))
                if alts:
                    rows.append(("Also written", alts))
                st.markdown(
                    f'<div class="conv-result-card"><div class="conv-result-label">Arabic numeral</div>'
                    f"{rows_html(rows)}</div>",
                    unsafe_allow_html=True,
                )
                st.markdown(parts_html(n, style, feminine, tags), unsafe_allow_html=True)
                st.markdown(notes_html(n, style), unsafe_allow_html=True)
            except ValueError as exc:
                st.markdown(error_html(exc), unsafe_allow_html=True)
        else:
            st.markdown(
                '<div class="conv-empty-state"><p>Enter a value on the left to see the result.</p></div>',
                unsafe_allow_html=True,
            )

    st.markdown("""
<div class="conv-caption">
Standard written Breton as described in Press (2009) and Favereau (1997), with the syntax of
numerals from Jouitteau's ARBRES atlas. Pronunciations are Gwendal Denis's transcriptions in
Chan's numeral database, given only for the numbers he recorded. Spoken Breton varies by region
in vowels, in mutations after numerals, and in which of the alternative forms is preferred.
</div>
""", unsafe_allow_html=True)

footer_nav("Breton", "converter")
