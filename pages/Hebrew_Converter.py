import streamlit as st
from ui import apply_global_styles, language_nav, CONV_CSS_ADDITIONS, footer_nav

# ─────────────────────────────────────────────────────────────
# UNICODE CONSTANTS
# ─────────────────────────────────────────────────────────────
GERESH    = '׳'   # modifier letter apostrophe
GERSHAYIM = '״'   # modifier letter double apostrophe

# ─────────────────────────────────────────────────────────────
# 1. LETTER-VALUE TABLE  (descending for greedy decomposition)
# ─────────────────────────────────────────────────────────────
HVALUE_TABLE = [
    (400, 'ת'), (300, 'ש'), (200, 'ר'), (100, 'ק'),
    (90,  'צ'), (80,  'פ'), (70,  'ע'), (60,  'ס'),
    (50,  'נ'), (40,  'מ'), (30,  'ל'), (20,  'כ'), (10, 'י'),
    (9,   'ט'), (8,   'ח'), (7,   'ז'), (6,   'ו'), (5,  'ה'),
    (4,   'ד'), (3,   'ג'), (2,   'ב'), (1,   'א'),
]
# Letters: tav shin resh qof tsadi pe ayin samech nun mem lamed kaf yod
#          tet chet zayin vav he dalet gimel bet aleph

# ─────────────────────────────────────────────────────────────
# 2. REVERSE LOOKUP  (includes final letter forms)
# ─────────────────────────────────────────────────────────────
LETTER_TO_VALUE = {ch: val for val, ch in HVALUE_TABLE}
LETTER_TO_VALUE.update({
    'ך': 20,  # final kaf
    'ם': 40,  # final mem
    'ן': 50,  # final nun
    'ף': 80,  # final pe
    'ץ': 90,  # final tsadi
})

# ─────────────────────────────────────────────────────────────
# 3. HELPER — raw letter list for 1 <= n <= 999
# ─────────────────────────────────────────────────────────────
def _raw_letters(n):
    """
    Decompose 1 <= n <= 999 into Hebrew letters.
    Standard exceptions: 15 -> tet+vav (9+6), 16 -> tet+zayin (9+7)
    These avoid writing yod-he / yod-vav, which abbreviate divine names.
    """
    letters = []
    hundreds = n - (n % 100)
    last_two = n % 100

    h = hundreds
    for val, ch in HVALUE_TABLE:
        while h >= val >= 100:
            letters.append(ch)
            h -= val

    if last_two == 15:
        letters += ['ט', 'ו']   # tet, vav
    elif last_two == 16:
        letters += ['ט', 'ז']   # tet, zayin
    else:
        r = last_two
        for val, ch in HVALUE_TABLE:
            while 0 < val < 100 and r >= val:
                letters.append(ch)
                r -= val

    return letters


# ─────────────────────────────────────────────────────────────
# 4. HELPER — apply gershayim punctuation
# ─────────────────────────────────────────────────────────────
def _apply_punct(letters):
    """
    Standard gershayim notation:
    - 1 letter  -> letter + GERESH
    - 2+ letters -> all-but-last + GERSHAYIM + last
    """
    if not letters:
        return ''
    if len(letters) == 1:
        return letters[0] + GERESH
    return ''.join(letters[:-1]) + GERSHAYIM + letters[-1]


# ─────────────────────────────────────────────────────────────
# 5. ARABIC -> HEBREW ALPHABETIC  (gematria)
# ─────────────────────────────────────────────────────────────
def arabic_to_hebrew_alpha(n):
    """Convert 1-9,999 to Hebrew alphabetic numeral with gershayim."""
    if not (1 <= n <= 9999):
        raise ValueError("Supported range: 1 – 9,999")

    thousands = n // 1000
    remainder = n % 1000

    # Thousands: single unit letter (aleph-tet) + GERESH separator
    thou_str = ''
    if thousands > 0:
        thou_str = ''.join(_raw_letters(thousands)) + GERESH

    if remainder == 0:
        return thou_str   # e.g. 3000 -> gimel + geresh

    return thou_str + _apply_punct(_raw_letters(remainder))


# ─────────────────────────────────────────────────────────────
# 6. HEBREW ALPHABETIC -> ARABIC
# ─────────────────────────────────────────────────────────────
def hebrew_alpha_to_arabic(text):
    """
    Parse a Hebrew alphabetic numeral -> integer.
    A GERESH that is NOT the very last character is the thousands separator.
    """
    text = text.strip()
    if not text:
        raise ValueError("Empty input")

    thou_part = ''
    main_part = text

    for i, ch in enumerate(text):
        if ch == GERESH and i < len(text) - 1:
            thou_part = text[:i]
            main_part = text[i + 1:]
            break

    def _strip(s):
        return s.replace(GERSHAYIM, '').replace(GERESH, '')

    total = 0
    for ch in _strip(thou_part):
        if ch in LETTER_TO_VALUE:
            total += LETTER_TO_VALUE[ch] * 1000
        elif ch.strip():
            raise ValueError(f'Unrecognized character in thousands portion: "{ch}"')

    for ch in _strip(main_part):
        if ch in LETTER_TO_VALUE:
            total += LETTER_TO_VALUE[ch]
        elif ch.strip():
            raise ValueError(f'Unrecognized character: "{ch}"')

    if total == 0:
        raise ValueError("No recognized Hebrew letter values found")
    return total


# ─────────────────────────────────────────────────────────────
# 7. SPOKEN MODERN HEBREW  (masculine abstract counting form)
# ─────────────────────────────────────────────────────────────
_SPOKEN = {
    0:  ('אֶפֶס',  'efes'),
    1:  ('אֶחָד',  'echad'),
    2:  ('שְנַיִם',  'shnayim'),
    3:  ('שְלֹשָה',  'shlosha'),
    4:  ('אַרְבָעָה',  "arba'a"),
    5:  ('חֲמִשָּה',  'chamisha'),
    6:  ('שִשָּה',  'shisha'),
    7:  ('שִבְעָה',  "shiv'a"),
    8:  ('שְמֹנָה',  'shmonah'),
    9:  ('תִשְעָה',  "tish'a"),
    10: ('עֲשָרָה',  'asara'),
    11: ('אַחַד עָשָר',  'achad asar'),
    12: ('שְנֵים עָשָר',  'shneym asar'),
    13: ('שְלֹשָה עָשָר',  'shlosha asar'),
    14: ('אַרְבָעָה עָשָר',  "arba'a asar"),
    15: ('חֲמִשָּה עָשָר',  'chamisha asar'),
    16: ('שִשָּה עָשָר',  'shisha asar'),
    17: ('שִבְעָה עָשָר',  "shiv'a asar"),
    18: ('שְמֹנָה עָשָר',  'shmonah asar'),
    19: ('תִשְעָה עָשָר',  "tish'a asar"),
    20: ('עֶשְרִים',  'esrim'),
    30: ('שְלֹשִים',  'shloshim'),
    40: ('אַרְבָעִים',  "arba'im"),
    50: ('חֲמִשִּים',  'chamishim'),
    60: ('שִשִּים',  'shishim'),
    70: ('שִבְעִים',  "shiv'im"),
    80: ('שְמֹנִים',  'shmonim'),
    90: ('תִשְעִים',  "tish'im"),
}

_HUNDREDS = {
    100: ('מֵאָה',  'meah'),
    200: ('מָאתַיִם',  'matayim'),
    300: ('שְלֹש מֵאוֹת',  'shlosh meot'),
    400: ('אַרְבַע מֵאוֹת',  'arba meot'),
    500: ('חֲמֵש מֵאוֹת',  'chamesh meot'),
    600: ('שֵש מֵאוֹת',  'shesh meot'),
    700: ('שְבַע מֵאוֹת',  "shva meot"),
    800: ('שְמֹנֶה מֵאוֹת',  'shmoneh meot'),
    900: ('תְשַע מֵאוֹת',  'tsha meot'),
}

_THOUSANDS = {
    1000: ('אֶלֶף',  'elef'),
    2000: ('אַלְפַּיִם',  'alpayim'),
    3000: ('שְלֹשֶת אֲלָפִים',  'shloshet alafim'),
    4000: ('אַרְבַעַת אֲלָפִים',  "arba'at alafim"),
    5000: ('חֲמֵשֶת אֲלָפִים',  'chameshet alafim'),
    6000: ('שֵשֶת אֲלָפִים',  'sheshet alafim'),
    7000: ('שִבְעַת אֲלָפִים',  "shiv'at alafim"),
    8000: ('שְמֹנַת אֲלָפִים',  'shmonat alafim'),
    9000: ('תִשְעַת אֲלָפִים',  "tish'at alafim"),
}


def arabic_to_spoken(n):
    """Return (Hebrew script, romanization) for 0-9,999."""
    if n == 0:
        return ('אֶפֶס', 'efes')
    if not (1 <= n <= 9999):
        raise ValueError("Spoken form supported for 0–9,999")

    thousands = n // 1000
    rem       = n % 1000
    hundreds  = (rem // 100) * 100
    sub100    = rem % 100

    parts_he = []
    parts_ro = []

    if thousands > 0:
        t_he, t_ro = _THOUSANDS[thousands * 1000]
        parts_he.append(t_he)
        parts_ro.append(t_ro)

    if hundreds > 0:
        h_he, h_ro = _HUNDREDS[hundreds]
        parts_he.append(h_he)
        parts_ro.append(h_ro)

    if sub100 > 0:
        if sub100 in _SPOKEN:
            s_he, s_ro = _SPOKEN[sub100]
            if parts_he:
                parts_he.append('וְ' + s_he)
                parts_ro.append('ve-' + s_ro)
            else:
                parts_he.append(s_he)
                parts_ro.append(s_ro)
        else:
            # Composite: tens + ve- + unit  (e.g. 34 = shloshim ve-arba'a)
            ten_val  = (sub100 // 10) * 10
            unit_val = sub100 % 10
            t_he, t_ro = _SPOKEN[ten_val]
            u_he, u_ro = _SPOKEN[unit_val]
            if parts_he:
                parts_he.append('וְ' + t_he)
                parts_ro.append('ve-' + t_ro)
            else:
                parts_he.append(t_he)
                parts_ro.append(t_ro)
            parts_he.append('וְ' + u_he)
            parts_ro.append('ve-' + u_ro)

    return (' '.join(parts_he), ' '.join(parts_ro))


# ════════════════════════════════════════════════════════════
# PAGE CONFIG & STYLES
# ════════════════════════════════════════════════════════════
st.set_page_config(page_title="Hebrew Numeral Converter", layout="wide")
apply_global_styles()

CONV_CSS = """
<style>
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
.conv-result-card{background:rgba(46,107,122,.04);border:1px solid rgba(46,107,122,.18);border-left:3px solid var(--teal);border-radius:0 4px 4px 0;padding:.75rem 1.1rem;margin-top:.8rem}
.conv-result-label{font-family:'DM Sans',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.14em;color:var(--teal);margin-bottom:.3rem}
.conv-result-value{font-family:'Crimson Pro',Georgia,serif;font-size:1.05rem;font-weight:400;color:var(--ink);line-height:1.55;word-break:break-word}
.conv-result-row{display:grid;grid-template-columns:7rem 1fr;gap:.35rem .9rem;align-items:baseline;margin-bottom:.25rem}
.conv-result-sublabel{font-family:'DM Sans',sans-serif;font-size:.62rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--ink-faint)}
.conv-result-subvalue{font-family:'Crimson Pro',Georgia,serif;font-size:1.05rem;font-weight:400;color:var(--ink);line-height:1.55;word-break:break-word}
.conv-hebrew{font-size:1.3rem;letter-spacing:.05em;direction:rtl;unicode-bidi:embed;display:inline-block}
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
</style>
"""
st.markdown(CONV_CSS, unsafe_allow_html=True)
st.markdown(CONV_CSS_ADDITIONS, unsafe_allow_html=True)

# ── MASTHEAD ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="conv-masthead">
    <div class="conv-masthead-eyebrow">Numeral Converter</div>
    <div class="conv-masthead-title">Hebrew Numerals</div>
    <div class="conv-masthead-desc">
        Bidirectional conversion between Arabic numerals and Hebrew alphabetic notation
        (gematria), with spoken Modern Hebrew word forms.
    </div>
</div>
""", unsafe_allow_html=True)

language_nav("Hebrew", "converter")

# ── INITIALIZE INPUT VARS ─────────────────────────────────────────────────────
arabic_input = ""
hebrew_input = ""

# ── TWO COLUMN LAYOUT ─────────────────────────────────────────────────────────
left_col, right_col = st.columns([1, 1], gap="large")

with right_col:
    # ── DIRECTION SELECTOR ──────────────────────────────────────────────────
    st.markdown('<div class="conv-section-label conv-direction-label">Conversion Direction</div>', unsafe_allow_html=True)

    direction = st.radio(
        "Conversion direction",
        ["Arabic → Hebrew", "Hebrew → Arabic"],
        horizontal=True,
        label_visibility="collapsed",
        key="hebrew_direction",
    )

with left_col:
    # ── PRESET EXAMPLES ───────────────────────────────────────────────────────
    st.markdown('<div class="conv-section-label">Preset Examples</div>', unsafe_allow_html=True)

    arabic_presets = [7, 15, 16, 18, 100, 248, 613, 5785]
    hebrew_presets = [
        'ז׳',                               # zayin-geresh = 7
        'ט״ו',                         # tet-gershayim-vav = 15
        'ט״ז',                         # tet-gershayim-zayin = 16
        'י״ח',                         # yod-gershayim-chet = 18
        'ק׳',                               # qof-geresh = 100
        'רמ״ח',                   # resh-mem-gershayim-chet = 248
        'תרי״ג',             # tav-resh-yod-gershayim-gimel = 613
        'ה׳תשפ״ה', # he-geresh-tav-shin-pe-gershayim-he = 5785
    ]

    with st.container(border=False):
        st.markdown('<p class="conv-presets-sublabel">Click a value to load it</p>', unsafe_allow_html=True)
        cols = st.columns(4)
        if direction == "Arabic → Hebrew":
            for i, num in enumerate(arabic_presets):
                if cols[i % 4].button(str(num), key=f"p_a_{i}", use_container_width=True):
                    st.session_state["arabic_input_heb"] = str(num)
        else:
            for i, txt in enumerate(hebrew_presets):
                if cols[i % 4].button(txt, key=f"p_b_{i}", use_container_width=True):
                    st.session_state["hebrew_input"] = txt

    # ── INPUT & CONVERSION ────────────────────────────────────────────────────
    st.markdown('<div class="conv-section-label">Convert</div>', unsafe_allow_html=True)

    if direction == "Arabic → Hebrew":
        st.markdown("""
        <div class="conv-input-card">
            <div class="conv-input-title">Enter an Arabic numeral</div>
            <div class="conv-input-hint">A whole number from 1 to 9,999, or click a preset above.</div>
        </div>
        """, unsafe_allow_html=True)
        arabic_input = st.text_input(
            "Arabic numeral", key="arabic_input_heb",
            placeholder="e.g. 613", label_visibility="collapsed",
        )
    else:
        st.markdown("""
        <div class="conv-input-card">
            <div class="conv-input-title">Enter a Hebrew alphabetic numeral</div>
            <div class="conv-input-hint">
                Hebrew letters with or without gershayim punctuation, e.g.
                <span style="direction:rtl;unicode-bidi:embed">רמ״ח</span> (248) or
                <span style="direction:rtl;unicode-bidi:embed">ה׳תשפ״ה</span> (5,785).
            </div>
        </div>
        """, unsafe_allow_html=True)
        hebrew_input = st.text_input(
            "Hebrew numeral", key="hebrew_input",
            placeholder="רמ״ח",
            label_visibility="collapsed",
        )

with right_col:
    if direction == "Arabic → Hebrew":
        if arabic_input:
            if arabic_input.lstrip("-").isdigit():
                try:
                    n = int(arabic_input)
                    alpha        = arabic_to_hebrew_alpha(n)
                    sp_he, sp_ro = arabic_to_spoken(n)
                    st.markdown(f"""
                    <div class="conv-result-card">
                        <div class="conv-result-label">Hebrew numeral</div>
                        <div class="conv-result-row">
                            <span class="conv-result-sublabel">Alphabetic</span>
                            <span class="conv-result-subvalue conv-hebrew">{alpha}</span>
                        </div>
                        <div class="conv-result-row">
                            <span class="conv-result-sublabel">Spoken (Script)</span>
                            <span class="conv-result-subvalue conv-hebrew">{sp_he}</span>
                        </div>
                        <div class="conv-result-row">
                            <span class="conv-result-sublabel">Romanized</span>
                            <span class="conv-result-subvalue">{sp_ro}</span>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                except Exception as e:
                    st.markdown(
                        f'<div class="conv-error-card"><p class="conv-error-text">{e}</p></div>',
                        unsafe_allow_html=True,
                    )
            else:
                st.markdown(
                    '<div class="conv-error-card"><p class="conv-error-text">Please enter a valid whole number.</p></div>',
                    unsafe_allow_html=True,
                )
        else:
            st.markdown("""
<div class="conv-empty-state">
    <p>Enter a value on the left to see the result.</p>
</div>
""", unsafe_allow_html=True)
    else:
        if hebrew_input:
            try:
                result = hebrew_alpha_to_arabic(hebrew_input)
                st.markdown(f"""
                <div class="conv-result-card">
                    <div class="conv-result-label">Arabic numeral</div>
                    <div class="conv-result-value">{result:,}</div>
                </div>
                """, unsafe_allow_html=True)
            except Exception as e:
                st.markdown(
                    f'<div class="conv-error-card"><p class="conv-error-text">{e}</p></div>',
                    unsafe_allow_html=True,
                )
        else:
            st.markdown("""
<div class="conv-empty-state">
    <p>Enter a value on the left to see the result.</p>
</div>
""", unsafe_allow_html=True)


    # ── CAPTION ───────────────────────────────────────────────────────────────
    st.markdown("""
<div class="conv-caption">
    Implements traditional Hebrew alphabetic (gematria) notation with standard
    gershayim punctuation and the divine-name exceptions for 15 and 16.
    Spoken forms use the masculine abstract counting form; gender inflection
    and morphological phenomena are detailed in the Linguistics section.
    Data from <a href="https://en.wikipedia.org/wiki/Hebrew_numerals" target="_blank">Wikipedia</a>.
    Algorithm by Yi Zou.
</div>
""", unsafe_allow_html=True)

# ── NAVIGATION ──────────────────────────────────────────────
footer_nav("Hebrew", "converter")
