import re
from datetime import date

import streamlit as st

from ui import apply_global_styles, language_nav, CONV_CSS_ADDITIONS, footer_nav

# ============================================================
# MAYA LONG COUNT CONVERTER
#
# The positional bar-and-dot notation of Classic Maya
# inscriptions, c. 250-909 CE, used to count days.
#
# Each place holds a digit from 0 to 19, built from dots (1),
# bars (5) and a zero sign. The places are worth 1, 20, 360,
# 7,200 and 144,000 days: base 20 everywhere except the third
# place, where 18 winals make one 360-day tun.
#
# Every surviving place-value number counts days. No written
# example of a pure base-20 place system (1, 20, 400, 8,000)
# exists, so the converter does not offer one (Stuart 2012;
# Chrisomalis 2010).
#
# Dates use the GMT correlation, JDN 584283. The modified GMT
# constant, 584285, used by Kettunen & Helmke (2025), is offered as
# the alternative. Radiocarbon supports the GMT family (Kennett et
# al. 2013) but cannot separate constants a few days apart.
#
# Spellings of periods, days and months follow Kettunen & Helmke.
#
# Sources: Kettunen & Helmke (2025); Lounsbury (1978);
# Stuart (2012); Kennett et al. (2013).
# ============================================================

# U+1D2E0 MAYAN NUMERAL ZERO to U+1D2F3 MAYAN NUMERAL NINETEEN.
GLYPH_BASE = 0x1D2E0
GLYPHS = {d: chr(GLYPH_BASE + d) for d in range(20)}
GLYPH_VALUES = {g: d for d, g in GLYPHS.items()}

# Highest place first, as the inscriptions read.
PERIODS = [
    ("bak'tun", 144_000),
    ("k'atun", 7_200),
    ("tun", 360),
    ("winal", 20),
    ("k'in", 1),
]
PLACES = len(PERIODS)
# Digit limit for each place: twenty everywhere except the winal,
# where eighteen make the next unit.
LIMITS = [20, 20, 20, 18, 20]
MAX_DAYS = 20 * 144_000 - 1          # 19.19.19.17.19
ERA = 13 * 144_000                   # 13.0.0.0.0

CORRELATIONS = {"GMT · 584283": 584_283, "Modified GMT · 584285": 584_285}
DEFAULT_CORRELATION = 584_283

TZOLKIN = ["Imix", "Ik'", "Ak'bal", "K'an", "Chikchan", "Kimi", "Manik'",
           "Lamat", "Muluk", "Ok", "Chuwen", "Eb", "Ben", "Ix", "Men",
           "K'ib", "Kaban", "Etz'nab", "Kawak", "Ajaw"]
HAAB = ["Pop", "Wo", "Sip", "Sotz'", "Sek", "Xul", "Yaxk'in", "Mol",
        "Ch'en", "Yax", "Sak", "Keh", "Mak", "K'ank'in", "Muwan", "Pax",
        "K'ayab", "Kumk'u", "Wayeb"]
# The base date, 13.0.0.0.0, fell on 4 Ajaw 8 Kumk'u.
TZOLKIN_NUMBER_OFFSET = 3            # day 0 is coefficient 4
TZOLKIN_NAME_OFFSET = 19             # day 0 is Ajaw
HAAB_OFFSET = 17 * 20 + 8            # day 0 is 8 Kumk'u

MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
SOLAR_YEAR = 365.2422


def long_count(n):
    """Days to the five Long Count digits, bak'tun first."""
    if not isinstance(n, int) or n < 0:
        raise ValueError(
            "The Long Count has no sign for negative numbers. A count runs forward "
            "from the base date; earlier days belong to the previous era."
        )
    if n > MAX_DAYS:
        raise ValueError(
            f"The five-place Long Count reaches {MAX_DAYS:,} days (19.19.19.17.19). "
            "Larger counts need places above the bak'tun, which appear only in a few "
            "cosmological texts and whose names (piktun, kalabtun…) are modern coinages."
        )
    digits = []
    for _, worth in PERIODS:
        d, n = divmod(n, worth)
        digits.append(d)
    return digits


def dotted(digits):
    return ".".join(str(d) for d in digits)


def number_to_maya(n):
    """Days to a Long Count in modern notation: 1386478 -> '9.12.11.5.18'."""
    return dotted(long_count(n))


def number_to_glyphs(n, minimal=False):
    """
    Days to Maya numerals, highest place first, places separated by spaces.
    minimal drops leading empty places, as a distance number would.
    """
    digits = long_count(n)
    if minimal:
        while len(digits) > 1 and digits[0] == 0:
            digits.pop(0)
    return " ".join(GLYPHS[d] for d in digits)


def digits_value(digits):
    """Right-aligned digits, k'in last, to days."""
    worths = [w for _, w in PERIODS][-len(digits):]
    return sum(d * w for d, w in zip(digits, worths))


def is_glyphs(text):
    return any(ch in GLYPH_VALUES for ch in text)


def parse_long_count(text):
    """
    '9.12.11.5.18' or Maya numeral glyphs to five digits. Fewer than five
    places are read from the right, k'in last, as a distance number is.
    """
    s = text.strip()
    if not s:
        raise ValueError("Enter a Long Count, such as 9.12.11.5.18.")
    if is_glyphs(s):
        digits = []
        for ch in s:
            if ch.isspace() or ch in ".,":
                continue
            if ch not in GLYPH_VALUES:
                raise ValueError(f"'{ch}' is not a Maya numeral.")
            digits.append(GLYPH_VALUES[ch])
    else:
        parts = [p for p in re.split(r"[.,:\s]+", s) if p]
        digits = []
        for p in parts:
            if not p.isdigit():
                raise ValueError(f"'{p}' is not a Long Count digit.")
            digits.append(int(p))
    if len(digits) > PLACES:
        raise ValueError(
            "The Long Count has five places, bak'tun to k'in. Places above the "
            "bak'tun appear only in a few cosmological texts and are not supported."
        )
    limits = LIMITS[-len(digits):]
    names = [name for name, _ in PERIODS][-len(digits):]
    for d, limit, name in zip(digits, limits, names):
        if d >= limit:
            if name == "winal":
                raise ValueError(
                    f"The winal place holds 0 to 17, not {d}: eighteen winals make one "
                    "tun of 360 days. This is the one place that is not base 20."
                )
            raise ValueError(f"The {name} place holds 0 to {limit - 1}, not {d}.")
    return [0] * (PLACES - len(digits)) + digits


def maya_to_number(text):
    """Long Count or glyphs to a count of days."""
    return digits_value(parse_long_count(text))


def pure_vigesimal(digits):
    """The same digits read in plain base 20, for comparison."""
    v = 0
    for d in digits:
        v = v * 20 + d
    return v


# ── Calendar ────────────────────────────────────────────────
def gregorian_to_jdn(y, m, d):
    """Proleptic Gregorian date (astronomical year) to Julian Day Number."""
    a = (14 - m) // 12
    yy, mm = y + 4800 - a, m + 12 * a - 3
    return d + (153 * mm + 2) // 5 + 365 * yy + yy // 4 - yy // 100 + yy // 400 - 32045


def julian_to_jdn(y, m, d):
    a = (14 - m) // 12
    yy, mm = y + 4800 - a, m + 12 * a - 3
    return d + (153 * mm + 2) // 5 + 365 * yy + yy // 4 - 32083


def jdn_to_gregorian(jdn):
    a = jdn + 32044
    b = (4 * a + 3) // 146097
    c = a - 146097 * b // 4
    d = (4 * c + 3) // 1461
    e = c - 1461 * d // 4
    m = (5 * e + 2) // 153
    return (100 * b + d - 4800 + m // 10, m + 3 - 12 * (m // 10),
            e - (153 * m + 2) // 5 + 1)


def jdn_to_julian(jdn):
    c = jdn + 32082
    d = (4 * c + 3) // 1461
    e = c - 1461 * d // 4
    m = (5 * e + 2) // 153
    return (d - 4800 + m // 10, m + 3 - 12 * (m // 10),
            e - (153 * m + 2) // 5 + 1)


def date_text(ymd):
    """(astronomical year, month, day) -> '11 August 3114 BCE'."""
    y, m, d = ymd
    era = f"{y} CE" if y > 0 else f"{1 - y} BCE"
    return f"{d} {MONTHS[m - 1]} {era}"


def calendar_round(n):
    """Tzolk'in and Haab' positions of day n (n may be negative)."""
    number = (n + TZOLKIN_NUMBER_OFFSET) % 13 + 1
    name = TZOLKIN[(n + TZOLKIN_NAME_OFFSET) % 20]
    pos = (n + HAAB_OFFSET) % 365
    return f"{number} {name} {pos % 20} {HAAB[pos // 20]}"


def parse_date(text):
    """
    'YYYY-MM-DD', with BCE marked by a suffix ('3114-08-11 BCE') or by a
    negative astronomical year ('-3113-08-11'). Returns (y, m, d).
    """
    s = text.strip()
    if s.lower() == "today":
        t = date.today()
        return t.year, t.month, t.day
    bce = bool(re.search(r"\s*(BCE|BC)\s*$", s, re.I))
    s = re.sub(r"\s*(BCE|BC|CE|AD)\s*$", "", s, flags=re.I)
    m = re.fullmatch(r"(-?\d{1,4})-(\d{1,2})-(\d{1,2})", s)
    if not m:
        raise ValueError(
            "Enter a date as year-month-day, such as 683-08-29, or 3114-08-11 BCE."
        )
    y, mo, d = (int(g) for g in m.groups())
    if bce:
        if y <= 0:
            raise ValueError("Use either a BCE suffix or a negative year, not both.")
        y = 1 - y
    elif y == 0 and not s.startswith("-"):
        raise ValueError("There is no year 0 CE: 1 BCE is followed by 1 CE.")
    if not 1 <= mo <= 12:
        raise ValueError(f"There is no month {mo}.")
    return y, mo, d


def date_to_days(y, m, d, correlation=DEFAULT_CORRELATION, julian=False):
    to_jdn = julian_to_jdn if julian else gregorian_to_jdn
    from_jdn = jdn_to_julian if julian else jdn_to_gregorian
    jdn = to_jdn(y, m, d)
    if from_jdn(jdn) != (y, m, d):
        raise ValueError(f"{date_text((y, m, d))} does not exist in that calendar.")
    return jdn - correlation


def days_to_dates(n, correlation=DEFAULT_CORRELATION):
    jdn = n + correlation
    return date_text(jdn_to_gregorian(jdn)), date_text(jdn_to_julian(jdn))


def previous_era(n):
    """
    The same digits read in the era before the base date, which ended at
    13.0.0.0.0. Offered for bak'tun 12 and for 13.0.0.0.0 itself.
    """
    if 12 * 144_000 <= n <= ERA:
        return n - ERA
    return None


# ============================================================
# PAGE CONFIG & STYLES
# ============================================================
st.set_page_config(page_title="Maya Numeral Converter", layout="wide")
apply_global_styles()

CONV_CSS = """<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Mayan+Numerals&display=swap');
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
div[data-testid="stTextInput"] input{font-family:'DM Sans','Noto Sans Mayan Numerals',sans-serif!important}
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
.maya-stack{display:inline-flex;flex-direction:column;align-items:stretch;padding:.2rem 0}
.maya-glyph{font-family:'Noto Sans Mayan Numerals',sans-serif;font-size:2.4rem;line-height:1;color:var(--ink);display:flex;align-items:center;justify-content:center;height:2.9rem;padding:0 .6rem;border-bottom:1px dashed var(--rule)}
.maya-glyph:last-child{border-bottom:none}
.maya-mono{font-family:'DM Mono','Courier New',monospace;font-size:1rem;color:var(--ink)}
.maya-places{background:var(--card-bg);border:1px solid var(--card-border);border-radius:6px;padding:.9rem 1.1rem;margin-top:.8rem}
.maya-places-label{font-family:'DM Sans',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.13em;color:var(--ink-faint);margin-bottom:.5rem}
.maya-places-row{display:grid;grid-template-columns:3.2rem 2.6rem 4.6rem 6.2rem 1fr;gap:.3rem .8rem;align-items:center;padding:.3rem 0;border-bottom:1px solid var(--rule)}
.maya-places-row:last-child{border-bottom:none}
.maya-places-head{font-family:'DM Sans',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--ink-faint)}
.maya-places-sign{font-family:'Noto Sans Mayan Numerals',sans-serif;font-size:1.6rem;line-height:1.1;color:var(--ink)}
.maya-places-val{font-family:'DM Mono','Courier New',monospace;font-size:.92rem;color:var(--ink)}
.maya-places-name{font-family:'Crimson Pro',Georgia,serif;font-style:italic;font-size:1rem;color:var(--ink)}
.maya-note{border:1px solid var(--rule);border-left:3px solid var(--ink-muted);background:var(--parchment-2);border-radius:0 4px 4px 0;padding:.7rem 1.05rem;margin-top:.8rem}
.maya-note-label{font-family:'DM Sans',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.13em;color:var(--ink-soft);margin-bottom:.3rem}
.maya-note p{font-family:'Crimson Pro',Georgia,serif;font-size:.97rem;color:var(--ink-muted);line-height:1.55;margin:0}
</style>"""
st.markdown(CONV_CSS, unsafe_allow_html=True)
st.markdown(CONV_CSS_ADDITIONS, unsafe_allow_html=True)

st.markdown("""
<div class="conv-masthead">
    <div class="conv-masthead-eyebrow">Numeral Converter</div>
    <div class="conv-masthead-title">Maya Numerals</div>
    <div class="conv-masthead-desc">Convert between Arabic numerals and the Maya Long Count — bars, dots and a zero sign stacked in places worth 1, 20, 360, 7,200 and 144,000 days.</div>
</div>
""", unsafe_allow_html=True)

language_nav("Maya", "converter")


# ── Result rendering ────────────────────────────────────────
def stack_html(digits):
    cells = "".join(f'<span class="maya-glyph">{GLYPHS[d]}</span>' for d in digits)
    return f'<div class="maya-stack">{cells}</div>'


def rows_html(rows):
    return "".join(
        f'<div class="conv-result-row">'
        f'<span class="conv-result-sublabel">{label}</span>'
        f'<span class="conv-result-subvalue">{value}</span>'
        f"</div>"
        for label, value in rows
    )


def places_table_html(digits):
    rows = []
    for d, (name, worth) in zip(digits, PERIODS):
        rows.append(
            f'<div class="maya-places-row">'
            f'<span class="maya-places-sign">{GLYPHS[d]}</span>'
            f'<span class="maya-places-val">{d}</span>'
            f'<span class="maya-places-name">{name}</span>'
            f'<span class="maya-places-val">× {worth:,}</span>'
            f'<span class="maya-places-val">= {d * worth:,}</span>'
            f"</div>"
        )
    head = (
        '<div class="maya-places-row">'
        '<span class="maya-places-head">Sign</span>'
        '<span class="maya-places-head">Digit</span>'
        '<span class="maya-places-head">Period</span>'
        '<span class="maya-places-head">Days each</span>'
        '<span class="maya-places-head">Worth</span></div>'
    )
    return (
        f'<div class="maya-places"><div class="maya-places-label">Place by place</div>'
        f"{head}{''.join(rows)}</div>"
    )


def note_html(label, text):
    return (
        f'<div class="maya-note"><div class="maya-note-label">{label}</div>'
        f"<p>{text}</p></div>"
    )


def error_html(msg):
    return f'<div class="conv-error-card"><p class="conv-error-text">{msg}</p></div>'


def length_text(n):
    if n < 365:
        return f"{n:,} day{'s' if n != 1 else ''}"
    return f"{n:,} days — about {n / SOLAR_YEAR:,.1f} solar years"


def result_rows(n, digits, correlation, lead):
    greg, jul = days_to_dates(n, correlation)
    rows = lead + [
        ("Glyphs", stack_html(digits)),
        ("As a date", f"{greg} <span style='color:var(--ink-faint)'>· Gregorian</span>"),
        ("Julian", jul),
        ("Calendar Round", calendar_round(n)),
    ]
    return rows_html(rows)


def notes_html(n, digits, correlation):
    out = []
    if n >= 360:
        pv = pure_vigesimal(digits)
        out.append(note_html(
            "Not plain base 20",
            f"Read in plain base 20, the same digits would mean <strong>{pv:,}</strong>, "
            f"not {n:,}. The third place counts tuns of 18 × 20 = 360 days, so every place "
            f"from there up is worth 18/20 of a power of twenty.",
        ))
    alt = previous_era(n)
    if alt is not None:
        greg, _ = days_to_dates(alt, correlation)
        lead = ("13.0.0.0.0 is also how the Maya wrote the base date itself: the "
                "completion of thirteen bak'tuns of the previous era"
                if alt == 0 else
                "Mythological texts also count toward the base date from the era before "
                "it, which ended at 13.0.0.0.0")
        out.append(note_html(
            "Which era?",
            f"{lead}. Read that way, these digits fall on <strong>{greg}</strong>, "
            f"<strong>{calendar_round(alt)}</strong>. An inscription tells the two "
            f"readings apart by the Calendar Round that follows the Long Count.",
        ))
    return "".join(out)


direction = st.radio(
    "Direction",
    ["Arabic → Maya", "Maya → Arabic", "Date → Maya"],
    horizontal=True,
    label_visibility="collapsed",
)

left_col, right_col = st.columns([1, 1], gap="large")

arabic_input = ""
maya_input = ""
date_input = ""

with left_col:
    st.markdown('<div class="conv-section-label">Preset Examples</div>', unsafe_allow_html=True)

    if direction == "Arabic → Maya":
        presets = ["7", "19", "20", "359", "360", "400", "7200",
                   "144000", "1386478", "1872000"]
        st.markdown('<p class="conv-presets-sublabel">Click a value to load it</p>', unsafe_allow_html=True)
        cols = st.columns(4)
        for i, val in enumerate(presets):
            if cols[i % 4].button(val, key=f"p_a_{i}", use_container_width=True):
                st.session_state["maya_arabic_input"] = val

        st.markdown('<div class="conv-section-label">Convert</div>', unsafe_allow_html=True)
        st.markdown(f"""
<div class="conv-input-card">
    <div class="conv-input-title">Enter a number of days</div>
    <div class="conv-input-hint">A whole number from 0 to {MAX_DAYS:,}. The Long Count only ever counted days.</div>
</div>""", unsafe_allow_html=True)
        arabic_input = st.text_input(
            "Enter a number of days",
            key="maya_arabic_input",
            placeholder="e.g. 1386478",
            label_visibility="collapsed",
        )
    elif direction == "Maya → Arabic":
        presets = ["9.12.11.5.18", "9.8.9.13.0", "8.12.14.8.15", "7.16.3.2.13",
                   "13.0.0.0.0", "12.19.13.4.0", "10.4.0.0.0", "1.0.0"]
        st.markdown('<p class="conv-presets-sublabel">Click a value to load it</p>', unsafe_allow_html=True)
        cols = st.columns(2)
        for i, val in enumerate(presets):
            if cols[i % 2].button(val, key=f"p_b_{i}", use_container_width=True):
                st.session_state["maya_word_input"] = val
        st.markdown("""
<div class="conv-caption" style="margin-top:.2rem">
<strong>9.12.11.5.18</strong> — death of K'inich Janaab Pakal, Palenque &nbsp;·&nbsp;
<strong>9.8.9.13.0</strong> — his birth &nbsp;·&nbsp;
<strong>8.12.14.8.15</strong> — Tikal Stela 29 &nbsp;·&nbsp;
<strong>7.16.3.2.13</strong> — Chiapa de Corzo Stela 2, the earliest known Long Count &nbsp;·&nbsp;
<strong>13.0.0.0.0</strong> — the base date, and 2012 &nbsp;·&nbsp;
<strong>12.19.13.4.0</strong> — Palenque, Temple of the Cross, before creation &nbsp;·&nbsp;
<strong>10.4.0.0.0</strong> — Toniná Monument 101 &nbsp;·&nbsp;
<strong>1.0.0</strong> — one tun
</div>""", unsafe_allow_html=True)

        st.markdown('<div class="conv-section-label">Convert</div>', unsafe_allow_html=True)
        st.markdown("""
<div class="conv-input-card">
    <div class="conv-input-title">Enter a Long Count</div>
    <div class="conv-input-hint">Places separated by dots, bak'tun first — <em>9.12.11.5.18</em>. Fewer than five places are read from the right. Maya numeral characters work too.</div>
</div>""", unsafe_allow_html=True)
        maya_input = st.text_input(
            "Enter a Long Count",
            key="maya_word_input",
            placeholder="e.g. 9.12.11.5.18",
            label_visibility="collapsed",
        )
    else:
        presets = ["today", "2012-12-21", "683-08-29", "292-07-06", "3114-08-11 BCE"]
        st.markdown('<p class="conv-presets-sublabel">Click a value to load it</p>', unsafe_allow_html=True)
        cols = st.columns(3)
        for i, val in enumerate(presets):
            if cols[i % 3].button(val, key=f"p_b_date_{i}", use_container_width=True):
                st.session_state["maya_date_input"] = val

        st.markdown('<div class="conv-section-label">Convert</div>', unsafe_allow_html=True)
        st.markdown("""
<div class="conv-input-card">
    <div class="conv-input-title">Enter a date</div>
    <div class="conv-input-hint">Year-month-day, such as <em>683-08-29</em>; add BCE for earlier years. Dates before 11 August 3114 BCE precede the count.</div>
</div>""", unsafe_allow_html=True)
        date_input = st.text_input(
            "Enter a date",
            key="maya_date_input",
            placeholder="e.g. 2012-12-21",
            label_visibility="collapsed",
        )
        calendar = st.radio(
            "Calendar",
            ["Gregorian", "Julian"],
            horizontal=True,
            label_visibility="collapsed",
            key="maya_calendar",
        )

    st.markdown('<div class="conv-section-label">Correlation</div>', unsafe_allow_html=True)
    corr_label = st.radio(
        "Correlation",
        list(CORRELATIONS),
        horizontal=True,
        label_visibility="collapsed",
        key="maya_correlation",
    )
    correlation = CORRELATIONS[corr_label]
    st.markdown(
        '<div class="conv-caption" style="margin-top:.4rem">Affects only the European dates. '
        'The correlation is the Julian Day Number of the base date; scholars disagree by a '
        'few days, and 584285 puts every date two days later than 584283. The Long Count '
        'and the Calendar Round do not change.</div>',
        unsafe_allow_html=True,
    )

with right_col:
    if direction == "Arabic → Maya":
        if arabic_input:
            try:
                s = arabic_input.strip().replace(",", "").replace(" ", "")
                if not re.fullmatch(r"-?\d+", s):
                    raise ValueError(
                        "Enter a whole number of days. The Long Count has no fractions: "
                        "its smallest unit is the day."
                    )
                n = int(s)
                digits = long_count(n)
                st.markdown(
                    f'<div class="conv-result-card">'
                    f'<div class="conv-result-label">Maya Long Count</div>'
                    + result_rows(n, digits, correlation, [
                        ("Long Count", f'<span class="maya-mono">{dotted(digits)}</span>'),
                        ("Length", length_text(n)),
                    ])
                    + "</div>",
                    unsafe_allow_html=True,
                )
                st.markdown(places_table_html(digits), unsafe_allow_html=True)
                st.markdown(notes_html(n, digits, correlation), unsafe_allow_html=True)
            except ValueError as exc:
                st.markdown(error_html(exc), unsafe_allow_html=True)
        else:
            st.markdown(
                '<div class="conv-empty-state"><p>Enter a value on the left to see the result.</p></div>',
                unsafe_allow_html=True,
            )
    elif direction == "Maya → Arabic":
        if maya_input:
            try:
                digits = parse_long_count(maya_input)
                n = digits_value(digits)
                st.markdown(
                    f'<div class="conv-result-card">'
                    f'<div class="conv-result-label">Arabic numeral</div>'
                    + result_rows(n, digits, correlation, [
                        ("Days", f"{n:,}"),
                        ("Long Count", f'<span class="maya-mono">{dotted(digits)}</span>'),
                    ])
                    + "</div>",
                    unsafe_allow_html=True,
                )
                st.markdown(places_table_html(digits), unsafe_allow_html=True)
                st.markdown(notes_html(n, digits, correlation), unsafe_allow_html=True)
            except ValueError as exc:
                st.markdown(error_html(exc), unsafe_allow_html=True)
        else:
            st.markdown(
                '<div class="conv-empty-state"><p>Enter a value on the left to see the result.</p></div>',
                unsafe_allow_html=True,
            )
    else:
        if date_input:
            try:
                y, m, d = parse_date(date_input)
                julian = calendar == "Julian"
                n = date_to_days(y, m, d, correlation, julian)
                if n < 0:
                    raise ValueError(
                        f"{date_text((y, m, d))} is before the base date, 13.0.0.0.0 "
                        f"4 Ajaw 8 Kumk'u. The Long Count does not count backwards."
                    )
                digits = long_count(n)
                st.markdown(
                    f'<div class="conv-result-card">'
                    f'<div class="conv-result-label">Maya Long Count</div>'
                    + result_rows(n, digits, correlation, [
                        ("Long Count", f'<span class="maya-mono">{dotted(digits)}</span>'),
                        ("Days", f"{n:,} since the base date"),
                    ])
                    + "</div>",
                    unsafe_allow_html=True,
                )
                st.markdown(places_table_html(digits), unsafe_allow_html=True)
                st.markdown(notes_html(n, digits, correlation), unsafe_allow_html=True)
            except ValueError as exc:
                st.markdown(error_html(exc), unsafe_allow_html=True)
        else:
            st.markdown(
                '<div class="conv-empty-state"><p>Enter a date on the left to see the result.</p></div>',
                unsafe_allow_html=True,
            )

    st.markdown("""
<div class="conv-caption">
Implements the five-place Long Count of Classic Maya inscriptions as described in Kettunen &amp;
Helmke (2025) and Lounsbury (1978). Dates use the GMT correlation unless the alternative is
selected, in the proleptic Gregorian calendar with the Julian equivalent below; Haab days are
numbered from 0. Glyphs are set in Noto Sans Mayan Numerals, the bar-and-dot forms of the
codices: monuments may carve the same digits as heads instead, and write zero with
other signs.
</div>
""", unsafe_allow_html=True)

footer_nav("Maya", "converter")
