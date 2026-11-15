import re
from fractions import Fraction

import streamlit as st

from ui import apply_global_styles, language_nav, CONV_CSS_ADDITIONS, footer_nav

# ============================================================
# BABYLONIAN SEXAGESIMAL CONVERTER
#
# The place-value notation of Old Babylonian mathematics,
# c. 2000-1600 BCE.
#
# Base 60, positional. Each place holds 1-59, written additively
# with two signs: the vertical wedge (1) and the corner wedge (10).
# There is no zero digit: an empty place was left blank, and from
# c. 300 BCE marked by a placeholder, but only between two written
# places. There is no sexagesimal point either, so the absolute size
# of a number was inferred from context.
#
# Transliteration follows Neugebauer: commas between places and a
# semicolon between whole and fractional parts, as in 1;24,51,10.
#
# Sources: Neugebauer (1957); Robson (2008); Chrisomalis (2010)
# 247-248; Fowler & Robson (1998); Boyer (1944).
# ============================================================

# Units 1-6 from the GESH2 series; 7-9 in their three-row variant
# forms (3+3+1, 3+3+2, 3+3+3), the arrangement usual on Old
# Babylonian tablets.
UNITS = {
    1: "\U00012415", 2: "\U00012416", 3: "\U00012417",
    4: "\U00012418", 5: "\U00012419", 6: "\U0001241A",
    7: "\U00012442", 8: "\U00012444", 9: "\U00012446",
}

# Corner wedges: 10, 20, 30, then the stacked forms of 40 and 50.
TENS = {
    1: "\U0001230B", 2: "\U00012399", 3: "\U0001230D",
    4: "\U0001240F", 5: "\U00012410",
}

# Late Babylonian placeholder: two slanted wedges, a punctuation sign
# repurposed to mark an empty place inside a number.
PLACEHOLDER = "\U00012472"

# Every sign accepted on input, including alternative encodings of
# the same values (the plain DISH wedge, the four-over-three 7-9).
GLYPH_VALUES = {g: v for v, g in UNITS.items()}
GLYPH_VALUES.update({g: 10 * v for v, g in TENS.items()})
GLYPH_VALUES.update({
    "\U00012079": 1,
    "\U0001241B": 7, "\U0001241C": 8, "\U0001241D": 9,
    "\U00012443": 7,
})

MAX_WHOLE = 60 ** 7 - 1
FRACTION_PLACE_LIMIT = 12

SUPERSCRIPT = str.maketrans("0123456789-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻")


def to_places(value):
    """
    Split a non-negative Fraction into sexagesimal places.

    Returns (whole, fraction, repeat_from, complete). whole and fraction
    are lists of digits 0-59. If the expansion repeats, fraction[repeat_from:]
    is the block that recurs forever; complete is False if the expansion
    was cut off at FRACTION_PLACE_LIMIT places without terminating or
    repeating.
    """
    q, rem = divmod(value.numerator, value.denominator)
    whole = []
    while q:
        q, d = divmod(q, 60)
        whole.insert(0, d)
    whole = whole or [0]

    fraction, seen = [], {}
    while rem:
        if rem in seen:
            return whole, fraction, seen[rem], True
        if len(fraction) == FRACTION_PLACE_LIMIT:
            return whole, fraction, None, False
        seen[rem] = len(fraction)
        d, rem = divmod(rem * 60, value.denominator)
        fraction.append(d)
    return whole, fraction, None, True


def transliterate(whole, fraction=()):
    """Neugebauer notation: 1;24,51,10."""
    s = ",".join(str(d) for d in whole)
    if fraction:
        s += ";" + ",".join(str(d) for d in fraction)
    return s


def digit_glyphs(d):
    """One place, 1-59: corner wedges for the tens, then vertical wedges."""
    tens, units = divmod(d, 10)
    return TENS.get(tens, "") + UNITS.get(units, "")


def _written_span(places):
    """Indices of the first and last non-empty place, or None."""
    filled = [i for i, d in enumerate(places) if d]
    if not filled:
        return None
    return filled[0], filled[-1]


def to_cuneiform(places, late=False):
    """
    Places as cuneiform text, one group per place. Leading and trailing
    empty places are never written. An empty place in between is left
    blank (two spaces) or, with late=True, marked by the placeholder.
    """
    span = _written_span(places)
    if span is None:
        return ""
    first, last = span
    groups = []
    for d in places[first:last + 1]:
        if d:
            groups.append(digit_glyphs(d))
        else:
            groups.append(PLACEHOLDER if late else "")
    return " ".join(groups)


def number_to_babylonian(n):
    """Whole number to Neugebauer transliteration: 2024 -> '33,44'."""
    if not isinstance(n, int) or n <= 0:
        raise ValueError("The notation has no numeral for zero or for negative numbers.")
    if n > MAX_WHOLE:
        raise ValueError(f"Supported range is up to {MAX_WHOLE:,} (seven places).")
    whole, _, _, _ = to_places(Fraction(n))
    return transliterate(whole)


def number_to_cuneiform(n, late=False):
    """Whole number to cuneiform signs: 2024 -> 𒌍𒐗 𒐏𒐘."""
    if not isinstance(n, int) or n <= 0:
        raise ValueError("The notation has no numeral for zero or for negative numbers.")
    whole, _, _, _ = to_places(Fraction(n))
    return to_cuneiform(whole, late)


def parse_value(text):
    """Arabic input: a whole number, a decimal or a fraction ('1.5', '1/7')."""
    s = text.strip().replace(",", "").replace(" ", "")
    try:
        v = Fraction(s)
    except (ValueError, ZeroDivisionError):
        raise ValueError(
            "Enter a whole number, a decimal such as 1.5, or a fraction such as 1/7."
        )
    if v < 0:
        raise ValueError("The notation has no sign for negative numbers.")
    if v == 0:
        raise ValueError(
            "There is no Babylonian numeral for zero. An empty place inside a "
            "number could be left blank or, much later, marked — but a number "
            "could not consist of nothing."
        )
    if v.numerator // v.denominator > MAX_WHOLE:
        raise ValueError(f"Supported range is up to {MAX_WHOLE:,} (seven whole places).")
    return v


def _split_places(s):
    parts = [p for p in re.split(r"[,:\s]+", s.strip()) if p]
    places = []
    for p in parts:
        if not p.isdigit():
            raise ValueError(f"'{p}' is not a sexagesimal digit.")
        d = int(p)
        if d > 59:
            raise ValueError(
                f"{d} cannot fill a single place: each place holds 0 to 59. "
                "Separate places with commas, as in 1,24,51,10."
            )
        places.append(d)
    return places


def parse_transliteration(text):
    """
    '1;24,51,10' -> (whole, fraction, has_point). Places may be separated by
    commas, colons or spaces; a semicolon marks the start of the fraction.
    """
    s = text.strip()
    if s.count(";") > 1:
        raise ValueError("Use at most one semicolon, to mark where the fraction begins.")
    whole_s, point, frac_s = s.partition(";")
    whole = _split_places(whole_s)
    while len(whole) > 1 and whole[0] == 0:
        whole.pop(0)
    whole = whole or [0]
    fraction = _split_places(frac_s)
    if point and not fraction:
        raise ValueError("Add the fractional places after the semicolon, as in 0;30.")
    if not any(whole) and not any(fraction):
        raise ValueError("There is no Babylonian numeral for zero.")
    return whole, fraction, bool(point)


def parse_cuneiform(text):
    """Cuneiform signs, one place per space-separated group, read as a whole number."""
    places = []
    for group in text.split():
        if group == PLACEHOLDER:
            places.append(0)
            continue
        total = 0
        for ch in group:
            if ch not in GLYPH_VALUES:
                raise ValueError(f"'{ch}' is not a recognised numeral sign.")
            total += GLYPH_VALUES[ch]
        if total > 59:
            raise ValueError(f"A group adds up to {total}; a single place holds at most 59.")
        places.append(total)
    if not places:
        raise ValueError("Enter at least one sign.")
    return places


def is_cuneiform(text):
    return any(ch in GLYPH_VALUES or ch == PLACEHOLDER for ch in text)


def places_value(whole, fraction=()):
    v = Fraction(0)
    for d in whole:
        v = v * 60 + d
    for k, d in enumerate(fraction, start=1):
        v += Fraction(d, 60 ** k)
    return v


def babylonian_to_number(text):
    """Transliteration or cuneiform to a number; whole results come back as int."""
    if is_cuneiform(text):
        v = places_value(parse_cuneiform(text))
    else:
        whole, fraction, _ = parse_transliteration(text)
        v = places_value(whole, fraction)
    return v.numerator if v.denominator == 1 else v


def decimal_text(v):
    """Exact decimal where one exists (1/8 -> 0.125); otherwise the fraction."""
    if v.denominator == 1:
        return f"{v.numerator:,}"
    d, twos, fives = v.denominator, 0, 0
    while d % 2 == 0:
        d //= 2
        twos += 1
    while d % 5 == 0:
        d //= 5
        fives += 1
    if d == 1:
        places = max(twos, fives)
        whole, frac = divmod(v.numerator * 10 ** places // v.denominator, 10 ** places)
        return f"{whole:,}.{frac:0{places}d}"
    return f"{v.numerator:,}/{v.denominator:,} ≈ {float(v):,.6f}"


def place_label(k):
    """Worth of a place k positions above the units place."""
    if k == 0:
        return "1"
    if k == 1:
        return "60"
    if k > 1:
        return "60" + str(k).translate(SUPERSCRIPT)
    if k == -1:
        return "1/60"
    return "1/60" + str(-k).translate(SUPERSCRIPT)


def alternative_readings(whole, fraction):
    """
    The same written signs at other scales. Only the non-empty run of places
    is visible on the tablet, so 60 (1,0) and 1 are indistinguishable.
    """
    places = whole + list(fraction)
    span = _written_span(places)
    first, last = span
    significand = places_value(places[first:last + 1])
    # Exponent of 60 that the last written place currently carries.
    shift = len(whole) - 1 - last
    exponents = [shift - 1, shift + 1]
    # Always offer the whole-number reading, the most natural one to a modern eye.
    exponents.append(0 if 0 not in exponents and shift != 0 else shift + 2)
    return [significand * Fraction(60) ** k for k in sorted(exponents)]


# ============================================================
# PAGE CONFIG & STYLES
# ============================================================
st.set_page_config(page_title="Babylonian Numeral Converter", layout="wide")
apply_global_styles()

CONV_CSS = """<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Cuneiform&display=swap');
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
div[data-testid="stTextInput"] input{font-family:'DM Sans','Noto Sans Cuneiform',sans-serif!important}
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
.bab-cuneiform{font-family:'Noto Sans Cuneiform',sans-serif;font-size:2.3rem;line-height:1.35;color:var(--ink);display:flex;flex-wrap:wrap;align-items:flex-end;gap:.35rem 1.1rem}
.bab-place{white-space:nowrap}
.bab-gap{display:inline-block;width:1.6rem;border-bottom:1px dashed var(--rule-strong);align-self:center}
.bab-mono{font-family:'DM Mono','Courier New',monospace;font-size:1rem;color:var(--ink)}
.bab-places{background:var(--card-bg);border:1px solid var(--card-border);border-radius:6px;padding:.9rem 1.1rem;margin-top:.8rem}
.bab-places-label{font-family:'DM Sans',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.13em;color:var(--ink-faint);margin-bottom:.5rem}
.bab-places-row{display:grid;grid-template-columns:5.5rem 3rem 4.5rem 1fr;gap:.3rem .9rem;align-items:center;padding:.3rem 0;border-bottom:1px solid var(--rule)}
.bab-places-row:last-child{border-bottom:none}
.bab-places-head{font-family:'DM Sans',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--ink-faint)}
.bab-places-sign{font-family:'Noto Sans Cuneiform',sans-serif;font-size:1.45rem;color:var(--ink);white-space:nowrap}
.bab-places-val{font-family:'DM Mono','Courier New',monospace;font-size:.92rem;color:var(--ink)}
.bab-note{border:1px solid var(--rule);border-left:3px solid var(--ink-muted);background:var(--parchment-2);border-radius:0 4px 4px 0;padding:.7rem 1.05rem;margin-top:.8rem}
.bab-note-label{font-family:'DM Sans',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.13em;color:var(--ink-soft);margin-bottom:.3rem}
.bab-note p{font-family:'Crimson Pro',Georgia,serif;font-size:.97rem;color:var(--ink-muted);line-height:1.55;margin:0}
</style>"""
st.markdown(CONV_CSS, unsafe_allow_html=True)
st.markdown(CONV_CSS_ADDITIONS, unsafe_allow_html=True)

st.markdown("""
<div class="conv-masthead">
    <div class="conv-masthead-eyebrow">Numeral Converter</div>
    <div class="conv-masthead-title">Babylonian Numerals</div>
    <div class="conv-masthead-desc">Convert between Arabic numerals and Babylonian sexagesimal notation — base 60, written in cuneiform with just two signs, and with no zero and no point to fix a number's size.</div>
</div>
""", unsafe_allow_html=True)

language_nav("Babylonian", "converter")


# ── Result rendering ────────────────────────────────────────
def cuneiform_html(places, late):
    span = _written_span(places)
    first, last = span
    cells = []
    for d in places[first:last + 1]:
        if d:
            cells.append(f'<span class="bab-place">{digit_glyphs(d)}</span>')
        elif late:
            cells.append(f'<span class="bab-place">{PLACEHOLDER}</span>')
        else:
            cells.append('<span class="bab-gap" title="empty place"></span>')
    return f'<div class="bab-cuneiform">{"".join(cells)}</div>'


def rows_html(rows):
    return "".join(
        f'<div class="conv-result-row">'
        f'<span class="conv-result-sublabel">{label}</span>'
        f'<span class="conv-result-subvalue">{value}</span>'
        f"</div>"
        for label, value in rows
    )


def places_table_html(whole, fraction, late):
    places = whole + list(fraction)
    first, last = _written_span(places)
    units = len(whole) - 1
    rows = []
    # Run down to the units place even when it is empty, so 3600 shows
    # its two unwritten places rather than looking like 1.
    for i in range(first, max(last, units) + 1):
        d = places[i]
        k = units - i
        if d:
            sign = digit_glyphs(d)
        elif late and i < last:
            sign = PLACEHOLDER
        else:
            sign = "—"
        worth = decimal_text(d * Fraction(60) ** k)
        rows.append(
            f'<div class="bab-places-row">'
            f'<span class="bab-places-sign">{sign}</span>'
            f'<span class="bab-places-val">{d}</span>'
            f'<span class="bab-places-val">× {place_label(k)}</span>'
            f'<span class="bab-places-val">= {worth}</span>'
            f"</div>"
        )
    head = (
        '<div class="bab-places-row">'
        '<span class="bab-places-head">Sign</span>'
        '<span class="bab-places-head">Digit</span>'
        '<span class="bab-places-head">Place</span>'
        '<span class="bab-places-head">Worth</span></div>'
    )
    return (
        f'<div class="bab-places"><div class="bab-places-label">Place by place</div>'
        f"{head}{''.join(rows)}</div>"
    )


def note_html(label, text):
    return (
        f'<div class="bab-note"><div class="bab-note-label">{label}</div>'
        f"<p>{text}</p></div>"
    )


def _reading_text(v):
    """Short form for the readings note: exact where tidy, else approximate."""
    text = decimal_text(v)
    return f"about {float(v):,.6g}" if "≈" in text else text


def readings_note(whole, fraction, own_value=None):
    alts = [f"<strong>{_reading_text(a)}</strong>"
            for a in alternative_readings(whole, fraction)]
    listed = f"{', '.join(alts[:-1])} or {alts[-1]}"
    lead = "These signs" if own_value is None else f"The signs for {own_value}"
    return note_html(
        "No point, no fixed size",
        f"{lead} could equally be read as {listed} — or at any other power of "
        f"sixty. Nothing on the tablet marks where the whole number ends, so a "
        f"scribe fixed the scale from context.",
    )


def error_html(msg):
    return f'<div class="conv-error-card"><p class="conv-error-text">{msg}</p></div>'


direction = st.radio(
    "Direction",
    ["Arabic → Babylonian", "Babylonian → Arabic"],
    horizontal=True,
    label_visibility="collapsed",
)

left_col, right_col = st.columns([1, 1], gap="large")

arabic_input = ""
bab_input = ""

with left_col:
    st.markdown('<div class="conv-section-label">Preset Examples</div>', unsafe_allow_html=True)

    if direction == "Arabic → Babylonian":
        presets = ["1", "59", "60", "61", "1000", "2024", "3600", "3601",
                   "1/2", "1/3", "1/7", "1.5"]
        st.markdown('<p class="conv-presets-sublabel">Click a value to load it</p>', unsafe_allow_html=True)
        cols = st.columns(4)
        for i, val in enumerate(presets):
            if cols[i % 4].button(val, key=f"p_a_{i}", use_container_width=True):
                st.session_state["bab_arabic_input"] = val

        st.markdown('<div class="conv-section-label">Convert</div>', unsafe_allow_html=True)
        st.markdown("""
<div class="conv-input-card">
    <div class="conv-input-title">Enter a number</div>
    <div class="conv-input-hint">A whole number, a decimal such as 1.5, or a fraction such as 1/7.</div>
</div>""", unsafe_allow_html=True)
        arabic_input = st.text_input(
            "Enter a number",
            key="bab_arabic_input",
            placeholder="e.g. 2024 or 1/3",
            label_visibility="collapsed",
        )
    else:
        presets = ["1;24,51,10", "42;25,35", "1,59", "2,49", "0;30", "1,0"]
        st.markdown('<p class="conv-presets-sublabel">Click a value to load it</p>', unsafe_allow_html=True)
        cols = st.columns(2)
        for i, val in enumerate(presets):
            if cols[i % 2].button(val, key=f"p_b_{i}", use_container_width=True):
                st.session_state["bab_word_input"] = val
        st.markdown("""
<div class="conv-caption" style="margin-top:.2rem">
<strong>1;24,51,10</strong> — √2 on tablet YBC 7289 &nbsp;·&nbsp;
<strong>42;25,35</strong> — the same tablet's diagonal for a side of 30 &nbsp;·&nbsp;
<strong>1,59</strong> and <strong>2,49</strong> — Plimpton 322, row 1 &nbsp;·&nbsp;
<strong>0;30</strong> — one half &nbsp;·&nbsp; <strong>1,0</strong> — sixty
</div>""", unsafe_allow_html=True)

        st.markdown('<div class="conv-section-label">Convert</div>', unsafe_allow_html=True)
        st.markdown("""
<div class="conv-input-card">
    <div class="conv-input-title">Enter a sexagesimal number</div>
    <div class="conv-input-hint">Places separated by commas, with a semicolon where the fraction begins — <em>1;24,51,10</em>. Cuneiform signs work too, one place per group, separated by spaces.</div>
</div>""", unsafe_allow_html=True)
        bab_input = st.text_input(
            "Enter a sexagesimal number",
            key="bab_word_input",
            placeholder="e.g. 1;24,51,10",
            label_visibility="collapsed",
        )

    st.markdown('<div class="conv-section-label">Scribal Convention</div>', unsafe_allow_html=True)
    convention = st.radio(
        "Empty places",
        ["Old Babylonian · c. 1800 BCE", "Late Babylonian · c. 300 BCE"],
        horizontal=True,
        label_visibility="collapsed",
        key="bab_convention",
    )
    late = convention.startswith("Late")
    st.markdown(
        '<div class="conv-caption" style="margin-top:.4rem">Affects only a number with an '
        'empty place in the middle, such as 3601 (1,0,1). Old Babylonian scribes left a gap; '
        'later scribes wrote a placeholder there, but never at the end of a number.</div>',
        unsafe_allow_html=True,
    )

with right_col:
    if direction == "Arabic → Babylonian":
        if arabic_input:
            try:
                v = parse_value(arabic_input)
                whole, fraction, repeat_from, complete = to_places(v)
                rows = [
                    ("Cuneiform", cuneiform_html(whole + fraction, late)),
                    ("Sexagesimal", f'<span class="bab-mono">{transliterate(whole, fraction)}'
                                    f'{"…" if repeat_from is not None or not complete else ""}</span>'),
                ]
                if v.denominator != 1:
                    rows.append(("Value", decimal_text(v)))
                st.markdown(
                    f'<div class="conv-result-card">'
                    f'<div class="conv-result-label">Babylonian numeral</div>'
                    f"{rows_html(rows)}</div>",
                    unsafe_allow_html=True,
                )
                st.markdown(places_table_html(whole, fraction, late), unsafe_allow_html=True)

                if repeat_from is not None:
                    block = ",".join(str(d) for d in fraction[repeat_from:])
                    st.markdown(note_html(
                        "Never ends",
                        f"The block <strong>{block}</strong> repeats forever. Its denominator, "
                        f"{v.denominator}, has a prime factor other than 2, 3 or 5, so no finite "
                        f"sexagesimal fraction equals it. Babylonian reciprocal tables simply "
                        f"leave such numbers out.",
                    ), unsafe_allow_html=True)
                elif not complete:
                    st.markdown(note_html(
                        "Cut off",
                        f"Shown to {FRACTION_PLACE_LIMIT} fractional places; the expansion "
                        f"continues beyond that.",
                    ), unsafe_allow_html=True)
                else:
                    if v.denominator % 3 == 0:
                        st.markdown(note_html(
                            "Finite in base 60",
                            f"This fraction never ends in decimal ({decimal_text(v)}), but it "
                            f"terminates in base 60 — sixty is divisible by 3, ten is not.",
                        ), unsafe_allow_html=True)
                    st.markdown(readings_note(whole, fraction, arabic_input.strip()),
                                unsafe_allow_html=True)
            except ValueError as exc:
                st.markdown(error_html(exc), unsafe_allow_html=True)
        else:
            st.markdown(
                '<div class="conv-empty-state"><p>Enter a value on the left to see the result.</p></div>',
                unsafe_allow_html=True,
            )
    else:
        if bab_input:
            try:
                if is_cuneiform(bab_input):
                    whole, fraction, has_point = parse_cuneiform(bab_input), [], False
                else:
                    whole, fraction, has_point = parse_transliteration(bab_input)
                v = places_value(whole, fraction)
                rows = [
                    ("Value", decimal_text(v)),
                    ("Sexagesimal", f'<span class="bab-mono">{transliterate(whole, fraction)}</span>'),
                    ("Cuneiform", cuneiform_html(whole + fraction, late)),
                ]
                st.markdown(
                    f'<div class="conv-result-card">'
                    f'<div class="conv-result-label">Arabic numeral</div>'
                    f"{rows_html(rows)}</div>",
                    unsafe_allow_html=True,
                )
                st.markdown(places_table_html(whole, fraction, late), unsafe_allow_html=True)
                if not has_point:
                    st.markdown(note_html(
                        "Read as a whole number",
                        "No semicolon was given, so the last place is taken as units. "
                        "Add one to place the fraction, as in 1;30 for one and a half.",
                    ), unsafe_allow_html=True)
                st.markdown(readings_note(whole, fraction), unsafe_allow_html=True)
            except ValueError as exc:
                st.markdown(error_html(exc), unsafe_allow_html=True)
        else:
            st.markdown(
                '<div class="conv-empty-state"><p>Enter a value on the left to see the result.</p></div>',
                unsafe_allow_html=True,
            )

    st.markdown("""
<div class="conv-caption">
Implements Old Babylonian sexagesimal place-value notation as described in Neugebauer (1957),
Robson (2008) and Chrisomalis (2010). Transliteration follows Neugebauer's convention of commas
between places and a semicolon before the fraction — a modern addition; the tablets mark neither.
Cuneiform is set in Noto Sans Cuneiform, a standardised typeface: wedge arrangements on real
tablets vary from scribe to scribe.
</div>
""", unsafe_allow_html=True)

footer_nav("Babylonian", "converter")
