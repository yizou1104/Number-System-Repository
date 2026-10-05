import re

import streamlit as st

from ui import apply_global_styles, language_nav, CONV_CSS_ADDITIONS, footer_nav

# ============================================================
# AINU NUMERAL GENERATOR
#
# Hokkaido Ainu, modern linguistic transcription.
#
# The system combines four distinct arithmetic operations:
#   subtraction     6-9      i-wan  '4-from-10'
#   addition        teens    ikasma 'exceed'
#   multiplication  scores   hot    'score, set'
#   overcounting    30s etc. e      lative 'towards'
#
# Sources: Batchelor (1905) ch. VII; Chan (Numeral Systems of the
# World's Languages, data from Sato 2013, Refsing 2013, Ikegami &
# Shinozaki 1983); Ochiai (2021); Dekany (2025); Tamura (1999).
# ============================================================

# Adnominal forms — the shape used in every source's numeral table,
# and the base for all compound numerals.
ADNOMINAL = {
    1: "sine", 2: "tu", 3: "re", 4: "ine", 5: "asikne",
    6: "iwan", 7: "arwan", 8: "tupesan", 9: "sinepesan",
    10: "wan", 20: "hotne",
}

# Serial (abstract reciting) forms — Dekany (2025) ex. 47.
SERIAL = {
    1: "sinep", 2: "tup", 3: "rep", 4: "inep", 5: "asik",
    6: "iwan", 7: "arwan", 8: "tupes", 9: "sinepes",
    10: "wan", 20: "hot",
}

# Nominal forms counting things, with the light noun -p / -pe.
THING = {
    1: "sinep", 2: "tup", 3: "rep", 4: "inep", 5: "asiknep",
    6: "iwanpe", 7: "arwanpe", 8: "tupesanpe", 9: "sinepesanpe",
    10: "wanpe", 20: "hotnep",
}

# Nominal forms counting people: -n after a vowel, -iw after a consonant.
HUMAN = {
    1: "sinen", 2: "tun", 3: "ren", 4: "inen", 5: "asiknen",
    6: "iwaniw", 7: "arwaniw", 8: "tupesaniw", 9: "sinepesaniw",
    10: "waniw", 20: "hotne niw",
}

PARADIGMS = {
    "Adnominal": ADNOMINAL,
    "Serial counting": SERIAL,
    "Things (-p / -pe)": THING,
    "People (-n / -iw)": HUMAN,
}

# Batchelor's higher unit: 'one ten-score' = 200.
TWO_HUNDRED = "sine wan hotne"

MAX_SUPPORTED = 1000


def _unit(d):
    return ADNOMINAL[d]


def _teen(r):
    """10-19: additive over wan 'ten'."""
    if r == 10:
        return "wan"
    return f"{ADNOMINAL[r - 10]} ikasma wan"


def _score(k):
    """Multiples of twenty, k = 1..10."""
    if k == 1:
        return "hotne"
    if k == 10:
        return TWO_HUNDRED
    return f"{ADNOMINAL[k]} hotne"


def _hundreds(n):
    """Batchelor's 201-1000, built on the 200-unit. Multiples of 100 only."""
    m = n // 100
    if m % 2 == 0:
        pairs = m // 2
        prefix = "" if pairs == 1 else f"{ADNOMINAL[pairs]} "
        return f"{prefix}{TWO_HUNDRED}"
    return f"asikne hot ikasma {_hundreds((m - 1) * 100)}"


def number_to_ainu(n):
    """Arabic numeral to Ainu, adnominal form."""
    if n == 0:
        raise ValueError(
            "Ainu has no attested traditional word for zero. "
            "The documented system begins at one."
        )
    if n < 0:
        raise ValueError("Only positive whole numbers are supported.")
    if n > MAX_SUPPORTED:
        raise ValueError(
            "Supported range is 1-1000. Tamura (1999) records that the system "
            "was not used beyond about 200 in practice."
        )

    if n <= 10:
        return ADNOMINAL[n]
    if n <= 19:
        return _teen(n)
    if n <= 199:
        k, r = divmod(n, 20)
        if r == 0:
            return _score(k)
        if r <= 9:
            # Undercounting: r exceeds the lower multiple of twenty.
            return f"{_unit(r)} ikasma {_score(k)}"
        # Overcounting: the teen runs towards the next multiple of twenty.
        return f"{_teen(r)} e {_score(k + 1)}"
    if n % 100 == 0:
        return _hundreds(n)
    raise ValueError(
        f"{n} is not documented. Above 200 the only recorded forms are exact "
        "multiples of 100 (Batchelor 1905); intermediate values were never "
        "attested, and this converter will not invent them."
    )


def additive_variant(n):
    """
    Ochiai (2021: 104): from 120 most dialects abandon the vigesimal
    multiplier and add a score onto 'five scores' (100) instead.
    Returns None where no such variant applies.
    """
    if n < 120 or n > 180 or n % 20 != 0:
        return None
    k = n // 20
    prefix = "" if k - 5 == 1 else f"{ADNOMINAL[k - 5]} "
    return f"{prefix}hotnep ikasma asikne hot"


def gloss(n):
    """Literal word-by-word reading of the generated form."""
    if n <= 10:
        literal = {
            1: "truly-be", 2: "two", 3: "three", 4: "four-be",
            5: "hand-be", 6: "four-from-ten", 7: "three-from-ten",
            8: "lacking-two(-from-ten)", 9: "lacking-one(-from-ten)",
            10: "both(-hands)-exist",
        }
        return literal[n]
    if n <= 19:
        return f"{n - 10} exceeds 10"
    if n <= 199:
        k, r = divmod(n, 20)
        if r == 0:
            if k == 1:
                return "score-be"
            if k == 10:
                return "one ten-score"
            return f"{k} score"
        if r <= 9:
            return f"{r} exceeds {k * 20}"
        return f"{r} towards {(k + 1) * 20}"
    m = n // 100
    if m % 2 == 0:
        pairs = m // 2
        return "one ten-score" if pairs == 1 else f"{pairs} x one ten-score"
    return f"five scores exceed {(m - 1) * 100}"


CONFIDENCE = [
    (10, "Core inventory", "Attested identically in every source consulted."),
    (99, "Well documented",
     "Given in full by Batchelor (1905) and corroborated by Refsing, "
     "Ochiai (2021) and Dékány (2025)."),
    (119, "Documented",
     "Follows the attested rule; 100 (asikne hotne) is directly attested."),
    (199, "Dialect split",
     "Ochiai (2021) reports that most dialects prefer the additive variant "
     "shown below from 120 upward."),
    (200, "Practical ceiling",
     "Tamura (1999: 58) records that Ainu elders in the 1950s did not "
     "understand what 'two hundred' meant."),
    (MAX_SUPPORTED, "Batchelor only",
     "Recorded in Batchelor (1905) but not corroborated by later fieldwork. "
     "Treat as elicited rather than current usage."),
]


def confidence(n):
    for ceiling, label, note in CONFIDENCE:
        if n <= ceiling:
            return label, note
    return "Unsupported", ""


# ── Reverse direction ───────────────────────────────────────
# Batchelor's 1905 orthography and other attested spellings, mapped
# onto the modern transcription used above.
_TOKEN_VARIANTS = {
    "shine": "sine", "shinep": "sinep", "shinen": "sinen",
    "ashikne": "asikne", "ashik": "asik", "ashiknep": "asiknep",
    "arawan": "arwan", "arawa": "arwan", "iwa": "iwan",
    "ikashima": "ikasma", "kasma": "ikasma",
    "shinepesan": "sinepesan", "shinepes": "sinepes",
    "niu": "niw", "wa": "wan",
}


def _normalise(text):
    s = text.lower().strip()
    s = s.replace("-", " ").replace(",", " ").replace(".", " ")
    s = re.sub(r"\s+", " ", s)
    # Multi-word spellings collapse to the single-word modern forms.
    for old, new in (
        ("hot ne p", "hotnep"), ("hot nep", "hotnep"),
        ("hot ne", "hotne"), ("tupe san", "tupesan"),
        ("shinepe san", "sinepesan"), ("sinepe san", "sinepesan"),
        ("tupe sanpe", "tupesanpe"), ("tupe saniw", "tupesaniw"),
    ):
        s = s.replace(old, new)
    tokens = [_TOKEN_VARIANTS.get(t, t) for t in s.split()]
    return " ".join(tokens)


def _build_index():
    index = {}
    for n in list(range(1, 200)) + [m * 100 for m in range(2, 11)]:
        index.setdefault(_normalise(number_to_ainu(n)), n)
        variant = additive_variant(n)
        if variant:
            index.setdefault(_normalise(variant), n)
    # Documented alternatives for twenty: hot 'score' with or without copula.
    index.setdefault(_normalise("sine hot"), 20)
    index.setdefault(_normalise("hot"), 20)
    # Serial, thing and human paradigms for the simplex numerals.
    for table in (SERIAL, THING, HUMAN):
        for value, form in table.items():
            index.setdefault(_normalise(form), value)
    return index


_INDEX = _build_index()


def ainu_to_number(text):
    if not text or not text.strip():
        raise ValueError("Enter an Ainu numeral.")
    key = _normalise(text)
    if key in _INDEX:
        return _INDEX[key]
    raise ValueError(
        "Not recognised. Expected a documented Ainu numeral such as "
        "'wan e tu hotne' (30) or 'iwan ikasma hotne' (26)."
    )


# ============================================================
# PAGE CONFIG & STYLES
# ============================================================
st.set_page_config(page_title="Ainu Numeral Converter", layout="wide")
apply_global_styles()

CONV_CSS = """<style>
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
.conv-result-row{display:grid;grid-template-columns:7.5rem 1fr;gap:.35rem .9rem;align-items:baseline}
.conv-result-sublabel{font-family:'DM Sans',sans-serif;font-size:.62rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--ink-faint)}
.conv-result-subvalue{font-family:'Crimson Pro',Georgia,serif;font-size:1.05rem;font-weight:400;color:var(--ink);line-height:1.55;word-break:break-word}
.conv-result-single{font-family:'Crimson Pro',Georgia,serif;font-size:1.05rem;font-weight:400;color:var(--ink);line-height:1.55;word-break:break-word}
.conv-error-card{background:rgba(184,92,56,.05);border:1px solid rgba(184,92,56,.2);border-left:3px solid var(--accent);border-radius:0 4px 4px 0;padding:.75rem 1.1rem;margin-top:.8rem}
.conv-error-text{font-family:'Crimson Pro',Georgia,serif;font-size:1rem;color:var(--accent);font-style:italic;margin:0}
.conv-empty-state{font-family:'Crimson Pro',Georgia,serif;font-style:italic;color:var(--ink-faint);padding:1.1rem 0}
.conv-caption{font-family:'DM Sans',sans-serif;font-size:.75rem;color:var(--ink-faint);line-height:1.55;margin-top:1rem}
.conv-caption a{color:var(--accent)!important;text-decoration:underline!important;text-decoration-color:rgba(184,92,56,.35)!important}
.ainu-conf{border:1px solid var(--rule);border-left:3px solid var(--ink-muted);background:var(--parchment-2);border-radius:0 4px 4px 0;padding:.7rem 1.05rem;margin-top:.8rem}
.ainu-conf-label{font-family:'DM Sans',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.13em;color:var(--ink-soft);margin-bottom:.3rem}
.ainu-conf-note{font-family:'Crimson Pro',Georgia,serif;font-size:.93rem;font-style:italic;color:var(--ink-muted);line-height:1.5;margin:0}
.ainu-para{background:var(--card-bg);border:1px solid var(--card-border);border-radius:6px;padding:.9rem 1.1rem;margin-top:.8rem}
.ainu-para-label{font-family:'DM Sans',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.13em;color:var(--ink-faint);margin-bottom:.5rem}
.ainu-para-row{display:grid;grid-template-columns:9.5rem 1fr;gap:.3rem .9rem;align-items:baseline;padding:.3rem 0;border-bottom:1px solid var(--rule)}
.ainu-para-row:last-child{border-bottom:none}
.ainu-para-key{font-family:'DM Sans',sans-serif;font-size:.68rem;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--ink-soft)}
.ainu-para-val{font-family:'DM Mono','Courier New',monospace;font-size:.95rem;color:var(--ink)}
</style>"""
st.markdown(CONV_CSS, unsafe_allow_html=True)
st.markdown(CONV_CSS_ADDITIONS, unsafe_allow_html=True)

st.markdown("""
<div class="conv-masthead">
    <div class="conv-masthead-eyebrow">Numeral Converter</div>
    <div class="conv-masthead-title">Ainu Numerals</div>
    <div class="conv-masthead-desc">Convert between Arabic numerals and Hokkaido Ainu — a vigesimal system that combines subtraction, addition, multiplication and overcounting in a single sequence.</div>
</div>
""", unsafe_allow_html=True)

language_nav("Ainu", "converter")

direction = st.radio(
    "Direction",
    ["Arabic → Ainu", "Ainu → Arabic"],
    horizontal=True,
    label_visibility="collapsed",
)

left_col, right_col = st.columns([1, 1], gap="large")

arabic_input = ""
ainu_input = ""

with left_col:
    st.markdown('<div class="conv-section-label">Preset Examples</div>', unsafe_allow_html=True)

    if direction == "Arabic → Ainu":
        presets = [1, 6, 8, 10, 15, 20, 26, 30, 36, 76, 99, 100, 120, 190, 200, 1000]
        st.markdown('<p class="conv-presets-sublabel">Click a value to load it</p>', unsafe_allow_html=True)
        cols = st.columns(4)
        for i, num in enumerate(presets):
            if cols[i % 4].button(str(num), key=f"ainu_p_{i}", use_container_width=True):
                st.session_state["ainu_arabic_input"] = str(num)

        st.markdown('<div class="conv-section-label">Convert</div>', unsafe_allow_html=True)
        st.markdown("""
<div class="conv-input-card">
    <div class="conv-input-title">Enter an Arabic numeral (1–1000)</div>
    <div class="conv-input-hint">Whole numbers only. Above 200, just multiples of 100 are documented.</div>
</div>""", unsafe_allow_html=True)
        arabic_input = st.text_input(
            "Enter an Arabic numeral",
            key="ainu_arabic_input",
            placeholder="e.g. 36",
            label_visibility="collapsed",
        )
    else:
        presets = [
            "sine", "iwan", "wan", "sine ikasma wan", "hotne",
            "iwan ikasma hotne", "wan e tu hotne", "tu hotne",
            "asikne hotne", "sine wan hotne",
        ]
        st.markdown('<p class="conv-presets-sublabel">Click a form to load it</p>', unsafe_allow_html=True)
        cols = st.columns(2)
        for i, form in enumerate(presets):
            if cols[i % 2].button(form, key=f"ainu_rp_{i}", use_container_width=True):
                st.session_state["ainu_word_input"] = form

        st.markdown('<div class="conv-section-label">Convert</div>', unsafe_allow_html=True)
        st.markdown("""
<div class="conv-input-card">
    <div class="conv-input-title">Enter an Ainu numeral</div>
    <div class="conv-input-hint">Batchelor's 1905 spellings are accepted too — <em>shine ikashima wa</em> resolves as readily as <em>sine ikasma wan</em>.</div>
</div>""", unsafe_allow_html=True)
        ainu_input = st.text_input(
            "Enter an Ainu numeral",
            key="ainu_word_input",
            placeholder="e.g. wan e tu hotne",
            label_visibility="collapsed",
        )

with right_col:
    if direction == "Arabic → Ainu":
        if arabic_input:
            val = arabic_input.strip()
            if val.lstrip("-").isdigit():
                try:
                    n = int(val)
                    result = number_to_ainu(n)
                    rows = [("Ainu", result), ("Literal", gloss(n))]
                    variant = additive_variant(n)
                    if variant:
                        rows.append(("Variant", variant))
                    body = "".join(
                        f'<div class="conv-result-row">'
                        f'<span class="conv-result-sublabel">{label}</span>'
                        f'<span class="conv-result-subvalue">{value}</span>'
                        f"</div>"
                        for label, value in rows
                    )
                    st.markdown(
                        f'<div class="conv-result-card">'
                        f'<div class="conv-result-label">Ainu numeral</div>'
                        f"{body}</div>",
                        unsafe_allow_html=True,
                    )

                    label, note = confidence(n)
                    st.markdown(
                        f'<div class="ainu-conf">'
                        f'<div class="ainu-conf-label">Attestation — {label}</div>'
                        f'<p class="ainu-conf-note">{note}</p>'
                        f"</div>",
                        unsafe_allow_html=True,
                    )

                    if n in PARADIGMS["Adnominal"]:
                        para_rows = "".join(
                            f'<div class="ainu-para-row">'
                            f'<span class="ainu-para-key">{name}</span>'
                            f'<span class="ainu-para-val">{table[n]}</span>'
                            f"</div>"
                            for name, table in PARADIGMS.items()
                        )
                        st.markdown(
                            f'<div class="ainu-para">'
                            f'<div class="ainu-para-label">Form classes — this numeral changes shape by what it counts</div>'
                            f"{para_rows}</div>",
                            unsafe_allow_html=True,
                        )
                except ValueError as exc:
                    st.markdown(
                        f'<div class="conv-error-card"><p class="conv-error-text">{exc}</p></div>',
                        unsafe_allow_html=True,
                    )
            else:
                st.markdown(
                    '<div class="conv-error-card"><p class="conv-error-text">Please enter a valid whole number.</p></div>',
                    unsafe_allow_html=True,
                )
        else:
            st.markdown(
                '<div class="conv-empty-state"><p>Enter a value on the left to see the result.</p></div>',
                unsafe_allow_html=True,
            )
    else:
        if ainu_input:
            try:
                n = ainu_to_number(ainu_input)
                st.markdown(
                    f'<div class="conv-result-card">'
                    f'<div class="conv-result-label">Arabic numeral</div>'
                    f'<div class="conv-result-row">'
                    f'<span class="conv-result-sublabel">Value</span>'
                    f'<span class="conv-result-subvalue">{n}</span></div>'
                    f'<div class="conv-result-row">'
                    f'<span class="conv-result-sublabel">Literal</span>'
                    f'<span class="conv-result-subvalue">{gloss(n)}</span></div>'
                    f"</div>",
                    unsafe_allow_html=True,
                )
            except ValueError as exc:
                st.markdown(
                    f'<div class="conv-error-card"><p class="conv-error-text">{exc}</p></div>',
                    unsafe_allow_html=True,
                )
        else:
            st.markdown(
                '<div class="conv-empty-state"><p>Enter a form on the left to see the result.</p></div>',
                unsafe_allow_html=True,
            )

    st.markdown("""
<div class="conv-caption">
Implements Hokkaido Ainu as described in Batchelor (1905), Ochiai (2021) and Dékány (2025).
Odd tens are generated as overcounting forms (<em>wan e tu hotne</em>, "ten towards forty"),
following the modern analysis rather than Batchelor's subtractive reading. Algorithm by Yi Zou.
</div>
""", unsafe_allow_html=True)

footer_nav("Ainu", "converter")
