import streamlit as st
from ui import apply_global_styles, language_nav, CONV_CSS_ADDITIONS, footer_nav

# ============================================================
# IGBO NUMERAL SYSTEM
# Bidirectional: Arabic ↔ Igbo
# Standard Igbo decimal numerals, 1-9,999 (Asonye & Okwaraji 2018 and
# Kari 1997, in Chan's numeral database): the multiplier follows narị and
# puku, as it follows iri (iri abụọ 20, narị abụọ 200, puku abụọ 2,000).
# The vigesimal row gives Ndimele's (2010) forms for Échiè, an Igboid
# variety, only for the numbers he recorded, in his transcription.
# ============================================================
import re
import unicodedata

IGBO_DIGITS = {
    1: "otu",    2: "abụọ",  3: "atọ",   4: "anọ",
    5: "ise",    6: "isii",  7: "asaa",  8: "asatọ",
    9: "itoolu", 10: "iri",
}
CONNECTOR = "na"    # additive conjunction, "and"
IGBO_MAX = 9999

# Recorded alternatives for numbers said alone (Welmers & Welmers 1964)
IGBO_ALTERNATIVES = {
    1:  [("ofu", "Onitsha area, often heard elsewhere (Welmers and Welmers 1964)")],
    9:  [("iteghete", "used in fairly large areas (Welmers and Welmers 1964)")],
    20: [("ọgụ", "a noun, 'score' (Welmers and Welmers 1964); Onitsha ọrụ")],
}

# Échiè, Ndimele (2010) in Chan's database. His 80 and 90 repeat the forms
# for 60 and 70 (atɔ 'three' where four is meant), so they are left out.
ECHIE = {
    1: "ot\u00f9",
    2: "\u00e0b\u028a\u0300\u0254\u0301 ~ m\u0300b\u028a\u0300\u0254\u0300 ~ nam\u0300",
    3: "t\u0254 ~ \u00e0t\u0254",
    4: "(\u01f9)n\u0254 ~ \u00e0n\u0254",
    5: "se ~ \u00ecse",
    6: "\u0283i\u00ec ~ \u00ec\u0283i\u00ec",
    7: "sa\u00e0 ~ \u00e0sa\u00e0",
    8: "sat\u0254\u0304 ~ \u00e0sat\u0254\u0304",
    9: "tot\u016b ~ \u00ectol\u016b",
    10: "\u00ecri",
    11: "\u00ecri n\u0101 ot\u00f9",
    12: "\u00ecri n\u00e0 \u00e0b\u028a\u0300\u0254\u0300",
    13: "\u00ecri n\u00e0 \u00e0t\u0254",
    14: "\u00ecri n\u00e0 \u00e0n\u0254",
    15: "\u00ecri n\u00e0 \u00ecse",
    16: "\u00ecri n\u00e0 \u00ec\u0283i\u00ec",
    17: "\u00ecri n\u00e0 \u00e0sa\u00e0",
    18: "\u00ecri n\u00e0 \u00e0sat\u0254\u0304",
    19: "\u00ecri n\u00e0 \u00ectol\u016b",
    20: "\u0254\u0263\u02b0\u028a\u0304",
    21: "\u0254\u0263\u02b0\u028a\u0304 na ot\u00f9",
    22: "\u0254\u0263\u02b0\u028a\u0304 n\u00e0 \u00e0b\u028a\u0300\u0254\u0301",
    23: "\u0254\u0263\u02b0\u028a\u0304 n\u00e0 \u00e0t\u0254",
    24: "\u0254\u0263\u02b0\u028a\u0304 n\u00e0 \u00e0n\u0254",
    25: "\u0254\u0263\u02b0\u028a\u0304 n\u00e0 \u00ecse",
    26: "\u0254\u0263\u02b0\u028a\u0304 n\u00e0 \u00ec\u0283i\u00ec",
    27: "\u0254\u0263\u02b0\u028a\u0304 n\u00e0 \u00e0sa\u00e0",
    28: "\u0254\u0263\u02b0\u028a\u0304 n\u00e0 \u00e0sat\u0254\u0300",
    29: "\u0254\u0263\u02b0\u028a\u0304 n\u00e0 \u00ectol\u016b",
    30: "\u0254\u0263\u02b0\u028a\u0304 na \u00ecri",
    40: "\u0254\u0263\u02b0\u028a\u0304 nam\u0300",
    50: "\u0254\u0263\u02b0\u028a\u0304 nam\u0300 na \u00ecri",
    60: "\u0254\u0263\u02b0\u028a\u0304 at\u0254",
    70: "\u0254\u0263\u02b0\u028a\u0304 at\u0254 na \u00ecri",
    100: "\u0254\u0263\u02b0\u028a\u0304 ise",
    200: "\u0254\u0263\u02b0\u028a\u0304 \u00ecri",
    400: "nn\u028a\u0300",
    800: "nn\u028a\u0300 nam\u0300",
    1000: "nn\u028a\u0300 nam\u0300 n\u00e0 \u0254\u0263\u02b0\u028a\u0304 \u00ecri"
}


def _igbo_check(n: int) -> None:
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"Expected int, got {type(n).__name__}")
    if n < 0:
        raise ValueError("Negative numbers are not supported.")
    if n == 0:
        raise ValueError(
            "None of the sources consulted gives an Igbo word for zero, so none "
            "is given here. Popular lists offer efu and others."
        )
    if n > IGBO_MAX:
        raise ValueError(
            "The converter covers 1 to 9,999: the sources give narị (100) and "
            "puku (1,000) but no word above a thousand."
        )


def _below_100(n: int) -> str:
    if n <= 10:
        return IGBO_DIGITS[n]
    tens, units = divmod(n, 10)
    head = "iri" if tens == 1 else f"iri {IGBO_DIGITS[tens]}"
    return head if units == 0 else f"{head} {CONNECTOR} {IGBO_DIGITS[units]}"


def number_to_igbo_decimal(n: int) -> str:
    """Standard Igbo for 1-9,999."""
    _igbo_check(n)
    thousands, rest = divmod(n, 1000)
    hundreds, rem = divmod(rest, 100)
    parts = []
    if thousands:
        parts.append("puku" if thousands == 1 else f"puku {IGBO_DIGITS[thousands]}")
    if hundreds:
        parts.append("narị" if hundreds == 1 else f"narị {IGBO_DIGITS[hundreds]}")
    if rem:
        parts.append(_below_100(rem))
    return f" {CONNECTOR} ".join(parts)


def igbo_alternatives(n: int) -> list:
    """Recorded alternatives to the main form, each with its source."""
    _igbo_check(n)
    return list(IGBO_ALTERNATIVES.get(n, []))


def number_to_igbo_vigesimal(n: int) -> str:
    """Ndimele's Échiè form for n; only the numbers he recorded."""
    _igbo_check(n)
    if n not in ECHIE:
        raise ValueError(f"Ndimele (2010) does not record {n} in Échiè.")
    return ECHIE[n]


def _fold(text: str) -> str:
    """Lowercase, unify apostrophes and spacing, and drop tone marks and dots
    below, so that abuo matches abụọ."""
    t = unicodedata.normalize("NFD", text.strip().lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = t.replace("\u2019", "'")
    return re.sub(r"\s+", " ", t)


def _nfc(text: str) -> str:
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", text.strip().lower()))


_IGBO_READ = {}
for _n in range(1, IGBO_MAX + 1):
    _forms = [number_to_igbo_decimal(_n)] + [f for f, _ in IGBO_ALTERNATIVES.get(_n, [])]
    for _f in _forms:
        assert _IGBO_READ.get(_fold(_f), _n) == _n, (_f, _n)
        _IGBO_READ[_fold(_f)] = _n
_ECHIE_READ = {}
for _n, _f in ECHIE.items():
    for _v in _f.split(" ~ ") if _n < 10 else [_f]:
        _ECHIE_READ[_nfc(_v)] = _n


def igbo_to_number(text: str) -> int:
    """Read a Standard Igbo numeral (1-9,999), a recorded alternative, or one
    of Ndimele's Échiè forms."""
    if not text.strip():
        raise ValueError("Empty input.")
    if _nfc(text) in _ECHIE_READ:
        return _ECHIE_READ[_nfc(text)]
    t = _fold(text)
    if t in _IGBO_READ:
        return _IGBO_READ[t]
    words = t.split()
    digits = {_fold(v) for v in IGBO_DIGITS.values()}
    for big in ("nari", "puku"):
        if big in words:
            i = words.index(big)
            if i > 0 and words[i - 1] == "otu":
                raise ValueError(
                    "The sources give 100 as narị and 1,000 as puku, without otu."
                )
            if i > 0 and words[i - 1] in digits:
                raise ValueError(
                    f"The multiplier follows {'narị' if big == 'nari' else 'puku'} in Igbo, "
                    f"as it follows iri: narị abụọ is 200, puku abụọ 2,000."
                )
    if t in ("efu", "oruoghoro", "ncha", "adigi", "okpokoro"):
        raise ValueError("None of the sources consulted gives an Igbo word for zero.")
    if t.startswith("bere "):
        raise ValueError(
            "None of the sources consulted records counting by subtraction with bere; "
            "they count up from each score (Échiè ɔɣʰʊ̄ nà ìse, 25)."
        )
    if "nde" in words:
        raise ValueError("The converter stops at 9,999; nde (a million) is not covered.")
    raise ValueError(
        "Not a recorded Igbo numeral. Standard forms join parts with na, "
        "largest first: puku na narị abụọ na iri atọ na anọ is 1,234."
    )


# ============================================================
# PAGE CONFIG & STYLES
# ============================================================
st.set_page_config(page_title="Igbo Numeral Converter", layout="wide")
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
div[data-testid="stRadio"]>div{display:flex;gap:0;background:var(--card-bg);border:1px solid var(--card-border);border-radius:6px;padding:.35rem;box-shadow:0 1px 3px rgba(26,22,18,.05),0 4px 14px rgba(26,22,18,.04),inset 0 1px 0 rgba(255,255,255,.65);width:fit-content}
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
.conv-result-row{display:grid;grid-template-columns:7rem 1fr;gap:.35rem .9rem;align-items:baseline}
.conv-result-sublabel{font-family:'DM Sans',sans-serif;font-size:.62rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--ink-faint)}
.conv-result-subvalue{font-family:'Crimson Pro',Georgia,serif;font-size:1.05rem;font-weight:400;color:var(--ink);line-height:1.55;word-break:break-word}
.conv-result-single{font-family:'Crimson Pro',Georgia,serif;font-size:1.05rem;font-weight:400;color:var(--ink);line-height:1.55;word-break:break-word}
.conv-error-card{background:rgba(184,92,56,.05);border:1px solid rgba(184,92,56,.2);border-left:3px solid var(--accent);border-radius:0 4px 4px 0;padding:.75rem 1.1rem;margin-top:.8rem}
.conv-error-text{font-family:'Crimson Pro',Georgia,serif;font-size:1rem;color:var(--accent);font-style:italic;margin:0}
.conv-nav-footer{display:flex;gap:.75rem;padding:1.4rem 0 .5rem 0;border-top:1px solid var(--rule);margin-top:2.5rem;flex-wrap:wrap}
.conv-nav-btn{font-family:'DM Sans',sans-serif;font-size:.78rem;font-weight:700;text-transform:uppercase;letter-spacing:.09em;color:var(--ink);background:var(--parchment-2);border:1.5px solid var(--rule-strong);border-radius:3px;padding:.55rem 1.1rem;text-decoration:none;display:inline-flex;align-items:center;gap:.4rem;white-space:nowrap;cursor:pointer;box-shadow:2px 2px 0 rgba(26,22,18,.08);transition:all .18s cubic-bezier(.4,0,.2,1)}
.conv-nav-btn:hover{background:var(--ink);color:var(--parchment);border-color:var(--ink);box-shadow:3px 3px 0 var(--accent);transform:translate(-1px,-1px);text-decoration:none}
.conv-nav-btn.active{background:var(--parchment-3);color:var(--ink-muted);cursor:default;box-shadow:none}
.conv-nav-btn.active:hover{transform:none;background:var(--parchment-3);color:var(--ink-muted);border-color:var(--rule-strong);box-shadow:none}
.conv-caption{font-family:'DM Sans',sans-serif;font-size:.75rem;color:var(--ink-faint);line-height:1.55;margin-top:1rem}
.conv-caption a{color:var(--accent)!important;text-decoration:underline!important;text-decoration-color:rgba(184,92,56,.35)!important}
.conv-caption a:hover{text-decoration-color:var(--accent)!important}
</style>"""
st.markdown(CONV_CSS, unsafe_allow_html=True)
st.markdown(CONV_CSS_ADDITIONS, unsafe_allow_html=True)
st.markdown("""<style>
/* Charis SIL, subset to the characters in Ndimele's Échiè transcriptions */
@import url('https://fonts.googleapis.com/css2?family=Charis+SIL&text=%20%28%29abeilmnorstu~%C3%A0%C3%AC%C3%B9%C4%81%C5%AB%C7%B9%C9%94%C9%A3%CA%83%CA%8A%CA%B0%CC%80%CC%81%CC%84&display=swap');
.ig-ipa{font-family:'Charis SIL',serif;font-size:1.1rem}
</style>""", unsafe_allow_html=True)

# ── MASTHEAD ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="conv-masthead">
    <div class="conv-masthead-eyebrow">Numeral Converter</div>
    <div class="conv-masthead-title">Igbo Numerals</div>
    <div class="conv-masthead-desc">
        Convert between Arabic numerals and Standard Igbo, which counts in tens, with the
        older counting by scores shown for Échiè, an Igboid variety, wherever its forms
        are recorded.
    </div>
</div>
""", unsafe_allow_html=True)

language_nav("Igbo", "converter")

# ── INITIALIZE INPUT VARS ─────────────────────────────────────────────────────
arabic_input = ""
igbo_input = ""

# ── TWO COLUMN LAYOUT ─────────────────────────────────────────────────────────
left_col, right_col = st.columns([1, 1], gap="large")

with right_col:
    # ── DIRECTION SELECTOR ──────────────────────────────────────────────────
    st.markdown('<div class="conv-section-label conv-direction-label">Conversion Direction</div>', unsafe_allow_html=True)

    direction = st.radio(
        "Conversion direction",
        ["Arabic → Igbo", "Igbo → Arabic"],
        horizontal=True,
        label_visibility="collapsed",
        key="igbo_direction",
    )

with left_col:
    # ── PRESET EXAMPLES ─────────────────────────────────────────────────────
    st.markdown('<div class="conv-section-label">Preset Examples</div>', unsafe_allow_html=True)

    # Arabic presets: Échiè forms recorded for 9, 20, 25, 40, 100, 400 and 1000
    arabic_presets = [9, 20, 25, 40, 47, 100, 200, 400, 1000, 1234, 2000, 9999]

    # Igbo presets: Standard decimal forms, a recorded alternative, Échiè forms
    igbo_presets = [
        "iri na ise", "iri abụọ na ise", "narị abụọ", "puku na narị abụọ na iri atọ na anọ",
        "iteghete", "ọgụ", "ɔɣʰʊ̄ nà ìse", "nnʊ̀ nam̀",
    ]

    with st.container(border=False):
        st.markdown('<p class="conv-presets-sublabel">Click a value to load it</p>', unsafe_allow_html=True)
        cols = st.columns(4)
        if direction == "Arabic → Igbo":
            for i, num in enumerate(arabic_presets):
                if cols[i % 4].button(str(num), key=f"p_a_{i}", use_container_width=True):
                    st.session_state["arabic_input"] = str(num)
        else:
            for i, txt in enumerate(igbo_presets):
                if cols[i % 4].button(txt, key=f"p_b_{i}", use_container_width=True):
                    st.session_state["igbo_input"] = txt

    # ── INPUT & CONVERSION ──────────────────────────────────────────────────
    st.markdown('<div class="conv-section-label">Convert</div>', unsafe_allow_html=True)

    if direction == "Arabic → Igbo":
        st.markdown("""
        <div class="conv-input-card">
            <div class="conv-input-title">Enter an Arabic numeral</div>
            <div class="conv-input-hint">
                A whole number from 1 to 9,999. The Échiè form is shown for the numbers
                Ndimele recorded.
            </div>
        </div>
        """, unsafe_allow_html=True)
        arabic_input = st.text_input(
            "Arabic numeral", key="arabic_input",
            placeholder="e.g. 25", label_visibility="collapsed",
        )
    else:  # Igbo → Arabic
        st.markdown("""
        <div class="conv-input-card">
            <div class="conv-input-title">Enter an Igbo numeral</div>
            <div class="conv-input-hint">
                Standard forms such as <em>narị abụọ na iri atọ</em> (230), with or without
                the dots and tone marks, or one of Ndimele's Échiè forms.
            </div>
        </div>
        """, unsafe_allow_html=True)
        igbo_input = st.text_input(
            "Igbo numeral", key="igbo_input",
            placeholder="e.g. narị abụọ na iri atọ",
            label_visibility="collapsed",
        )

def rows_html(rows):
    return "".join(
        f'<div class="conv-result-row">'
        f'<span class="conv-result-sublabel">{label}</span>'
        f'<span class="conv-result-subvalue">{value}</span>'
        f"</div>"
        for label, value in rows
    )


def alternatives_html(n):
    return "".join(
        f"<span style='display:block'><em>{form}</em> "
        f"<span style='font-family:DM Sans,sans-serif;font-size:.74rem;color:var(--ink-faint)'>· {why}</span></span>"
        for form, why in igbo_alternatives(n)
    )


def error_html(msg):
    return f'<div class="conv-error-card"><p class="conv-error-text">{msg}</p></div>'


EMPTY = '<div class="conv-empty-state"><p>Enter a value on the left to see the result.</p></div>'

with right_col:
    if direction == "Arabic → Igbo":
        if arabic_input:
            try:
                s_in = arabic_input.strip().replace(",", "")
                if not s_in.lstrip("-").isdigit():
                    raise ValueError("Please enter a valid whole number.")
                n = int(s_in)
                rows = [("Standard Igbo", number_to_igbo_decimal(n))]
                alts = alternatives_html(n)
                if alts:
                    rows.append(("Also recorded", alts))
                if n in ECHIE:
                    rows.append(("Échiè (by scores)", f'<span class="ig-ipa">{ECHIE[n]}</span>'))
                st.markdown(
                    f'<div class="conv-result-card"><div class="conv-result-label">Igbo numeral</div>'
                    f"{rows_html(rows)}</div>",
                    unsafe_allow_html=True,
                )
            except ValueError as e:
                st.markdown(error_html(e), unsafe_allow_html=True)
        else:
            st.markdown(EMPTY, unsafe_allow_html=True)
    else:
        if igbo_input:
            try:
                n = igbo_to_number(igbo_input)
                rows = [("Arabic numeral", f"{n:,}"), ("Standard Igbo", number_to_igbo_decimal(n))]
                if n in ECHIE:
                    rows.append(("Échiè (by scores)", f'<span class="ig-ipa">{ECHIE[n]}</span>'))
                st.markdown(
                    f'<div class="conv-result-card"><div class="conv-result-label">Arabic numeral</div>'
                    f"{rows_html(rows)}</div>",
                    unsafe_allow_html=True,
                )
            except ValueError as e:
                st.markdown(error_html(e), unsafe_allow_html=True)
        else:
            st.markdown(EMPTY, unsafe_allow_html=True)


    # ── CAPTION ───────────────────────────────────────────────────────────────
    st.markdown("""
<div class="conv-caption">
    Standard Igbo numerals as recorded by Emma Asonye and Queenette Okwaraji (2018) and by
    Ethelbert Kari (1997) in Chan's <em>Numeral Systems of the World's Languages</em>, with
    alternatives from Welmers and Welmers's Peace Corps course (1964). Counting by scores is shown
    in Ozo-mekuri Ndimele's transcription of Échiè (2010), only for the numbers he recorded.
    Algorithm by Yi Zou.
</div>
""", unsafe_allow_html=True)

# ── NAVIGATION ──────────────────────────────────────────────
footer_nav("Igbo", "converter")
