import streamlit as st
from ui import apply_global_styles, language_nav, CONV_CSS_ADDITIONS, footer_nav

# ============================================================
# SWAHILI NUMERAL SYSTEM (Kiswahili Sanifu)
# Bidirectional: Arabic ↔ Swahili
#
# Rules:
#   1. Digits 0–10: base vocabulary (Bantu 1–5,8; Arabic loans 6,7,9,10+)
#   2. Teens 11–19: kumi na [digit]
#   3. Tens 20–90: invariable Arabic loanwords (ishirini … tisini)
#   4. Compound tens: [tens] na [unit]
#   5. Hundreds: mia [digit]  (mia moja=100, mia mbili=200 …)
#   6. Thousands: elfu [multiplier]  (elfu moja=1000, elfu kumi=10,000 …)
#   7. Millions: milioni [multiplier]
#   8. Major parts joined by na
#
# Note: "elfu kumi na moja" is structurally ambiguous in Swahili
# (could be 10,001 or 11,000). This converter uses the greedy
# convention: the elfu multiplier is read in full first, so
# "elfu kumi na moja" = 11,000. Numbers like 10,001 produce
# the same string and are documented as such.
#
# Sources: Ashton (1944) "Swahili Grammar", Perrot "Teach Yourself
#          Swahili", omniglot.com/language/numbers/swahili.htm
# ============================================================

# ── Backend ──────────────────────────────────────────────────────────────────

_ONES: dict[int, str] = {
    0: "sifuri", 1: "moja",  2: "mbili", 3: "tatu", 4: "nne",
    5: "tano",   6: "sita",  7: "saba",  8: "nane", 9: "tisa",
    10: "kumi",
}

_TENS: dict[int, str] = {
    2: "ishirini", 3: "thelathini", 4: "arobaini",  5: "hamsini",
    6: "sitini",   7: "sabini",     8: "themanini",  9: "tisini",
}

_ONES_REV: dict[str, int] = {v: k for k, v in _ONES.items()}
_TENS_REV: dict[str, int] = {v: k for k, v in _TENS.items()}


def _sub_hundred(n: int) -> str:
    assert 1 <= n <= 99
    if n <= 10:
        return _ONES[n]
    if n <= 19:
        return f"kumi na {_ONES[n - 10]}"
    t, u = divmod(n, 10)
    return _TENS[t] if u == 0 else f"{_TENS[t]} na {_ONES[u]}"


def _sub_thousand(n: int) -> str:
    assert 1 <= n <= 999
    if n < 100:
        return _sub_hundred(n)
    h, r = divmod(n, 100)
    base = f"mia {_ONES[h]}"
    return base if r == 0 else f"{base} na {_sub_hundred(r)}"


def number_to_swahili(n: int) -> str:
    """Convert 0–999,999,999 to Swahili words."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"Expected int, got {type(n).__name__}")
    if n < 0:
        raise ValueError("Negative numbers are not supported.")
    if n > 999_999_999:
        raise ValueError("Supported range is 0–999,999,999.")
    if n == 0:
        return "sifuri"

    parts: list[str] = []
    rem = n
    if rem >= 1_000_000:
        parts.append(f"milioni {_sub_thousand(rem // 1_000_000)}")
        rem %= 1_000_000
    if rem >= 1_000:
        parts.append(f"elfu {_sub_thousand(rem // 1_000)}")
        rem %= 1_000
    if rem > 0:
        parts.append(_sub_thousand(rem))
    return " na ".join(parts)


def _parse_sub_hundred(tokens: list[str]) -> tuple[int, list[str]]:
    if not tokens:
        return 0, tokens
    if tokens[0] in _TENS_REV:
        val = _TENS_REV[tokens[0]] * 10
        rest = tokens[1:]
        if len(rest) >= 2 and rest[0] == "na" and rest[1] in _ONES_REV and _ONES_REV[rest[1]] > 0:
            return val + _ONES_REV[rest[1]], rest[2:]
        return val, rest
    if tokens[0] == "kumi":
        rest = tokens[1:]
        if len(rest) >= 2 and rest[0] == "na" and rest[1] in _ONES_REV and _ONES_REV[rest[1]] > 0:
            return 10 + _ONES_REV[rest[1]], rest[2:]
        return 10, rest
    if tokens[0] in _ONES_REV and _ONES_REV[tokens[0]] > 0:
        return _ONES_REV[tokens[0]], tokens[1:]
    return 0, tokens


def _parse_sub_thousand(tokens: list[str]) -> tuple[int, list[str]]:
    if not tokens:
        return 0, tokens
    if tokens[0] == "mia":
        if len(tokens) < 2 or tokens[1] not in _ONES_REV or _ONES_REV[tokens[1]] == 0:
            raise ValueError(f"Expected digit after 'mia'.")
        h = _ONES_REV[tokens[1]]
        rest = tokens[2:]
        if len(rest) >= 2 and rest[0] == "na":
            sub, rest = _parse_sub_hundred(rest[1:])
            return h * 100 + sub, rest
        return h * 100, rest
    return _parse_sub_hundred(tokens)


def swahili_to_number(text: str) -> int:
    """Parse a Swahili numeral string to an integer."""
    text = text.strip().lower()
    if not text:
        raise ValueError("Empty input.")
    if text == "sifuri":
        return 0
    tokens = text.split()
    total = 0
    if tokens and tokens[0] == "milioni":
        m, tokens = _parse_sub_thousand(tokens[1:])
        if m == 0:
            raise ValueError("Expected multiplier after 'milioni'.")
        total += m * 1_000_000
        if tokens and tokens[0] == "na":
            tokens = tokens[1:]
    if tokens and tokens[0] == "elfu":
        t, tokens = _parse_sub_thousand(tokens[1:])
        if t == 0:
            raise ValueError("Expected multiplier after 'elfu'.")
        total += t * 1_000
        if tokens and tokens[0] == "na":
            tokens = tokens[1:]
    if tokens:
        sub, tokens = _parse_sub_thousand(tokens)
        total += sub
    if tokens:
        raise ValueError(f"Unexpected tokens: {tokens}")
    return total


# ============================================================
# PAGE CONFIG & STYLES
# ============================================================
st.set_page_config(page_title="Swahili Numeral Converter", layout="wide")
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
.conv-result-card{background:rgba(46,107,122,.04);border:1px solid rgba(46,107,122,.18);border-left:3px solid var(--teal);border-radius:0 4px 4px 0;padding:.75rem 1.1rem;margin-top:.8rem}
.conv-result-label{font-family:'DM Sans',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.14em;color:var(--teal);margin-bottom:.3rem}
.conv-result-value{font-family:'Crimson Pro',Georgia,serif;font-size:1.05rem;font-weight:400;color:var(--ink);line-height:1.55;word-break:break-word}
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

# ── MASTHEAD ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="conv-masthead">
    <div class="conv-masthead-eyebrow">Numeral Converter</div>
    <div class="conv-masthead-title">Swahili Numerals</div>
    <div class="conv-masthead-desc">
        Bidirectional conversion between Arabic numerals and Swahili (Kiswahili Sanifu),
        with correct handling of mia, elfu, and the na connector structure.
    </div>
</div>
""", unsafe_allow_html=True)

language_nav("Swahili", "converter")

arabic_input = ""
swahili_input = ""

left_col, right_col = st.columns([1, 1], gap="large")

with right_col:
    # ── DIRECTION SELECTOR ──────────────────────────────────────────────────
    st.markdown('<div class="conv-section-label conv-direction-label">Conversion Direction</div>', unsafe_allow_html=True)

    direction = st.radio(
        "Conversion direction",
        ["Arabic → Swahili", "Swahili → Arabic"],
        horizontal=True,
        label_visibility="collapsed",
        key="swahili_direction",
    )

with left_col:
    # ── PRESET EXAMPLES ──────────────────────────────────────────────────────────
    st.markdown('<div class="conv-section-label">Preset Examples</div>', unsafe_allow_html=True)

    arabic_presets  = [0, 11, 35, 100, 321, 1000, 11000, 1000000]
    swahili_presets = [
        "sifuri", "kumi na moja", "thelathini na tano",
        "mia moja", "mia tatu na ishirini na moja",
        "elfu moja", "elfu kumi na moja", "milioni moja",
    ]

    with st.container(border=True):
        st.markdown('<p class="conv-presets-sublabel">Click a value to load it</p>', unsafe_allow_html=True)
        cols = st.columns(4)
        if direction == "Arabic → Swahili":
            for i, num in enumerate(arabic_presets):
                if cols[i % 4].button(str(num), key=f"p_a_{i}", use_container_width=True):
                    st.session_state["arabic_input"] = str(num)
        else:
            for i, txt in enumerate(swahili_presets):
                if cols[i % 4].button(txt, key=f"p_b_{i}", use_container_width=True):
                    st.session_state["swahili_input"] = txt

    # ── INPUT & CONVERSION ───────────────────────────────────────────────────────
    st.markdown('<div class="conv-section-label">Convert</div>', unsafe_allow_html=True)

    if direction == "Arabic → Swahili":
        st.markdown("""
        <div class="conv-input-card">
            <div class="conv-input-title">Enter an Arabic numeral</div>
            <div class="conv-input-hint">Whole number from 0 to 999,999,999.</div>
        </div>
        """, unsafe_allow_html=True)
        arabic_input = st.text_input(
            "Arabic numeral", key="arabic_input",
            placeholder="e.g. 321", label_visibility="collapsed",
        )
    else:
        st.markdown("""
        <div class="conv-input-card">
            <div class="conv-input-title">Enter a Swahili numeral</div>
            <div class="conv-input-hint">Standard Swahili, e.g. <em>mia tatu na ishirini na moja</em>.</div>
        </div>
        """, unsafe_allow_html=True)
        swahili_input = st.text_input(
            "Swahili numeral", key="swahili_input",
            placeholder="e.g. mia tatu na ishirini na moja", label_visibility="collapsed",
        )

with right_col:
    if direction == "Arabic → Swahili":
        if arabic_input:
            if arabic_input.isdigit():
                try:
                    result = number_to_swahili(int(arabic_input))
                    st.markdown(f"""
                    <div class="conv-result-card">
                        <div class="conv-result-label">Swahili numeral</div>
                        <div class="conv-result-value">{result}</div>
                    </div>
                    """, unsafe_allow_html=True)
                except Exception as e:
                    st.markdown(f'<div class="conv-error-card"><p class="conv-error-text">{e}</p></div>',
                                unsafe_allow_html=True)
            else:
                st.markdown('<div class="conv-error-card"><p class="conv-error-text">Please enter a valid whole number.</p></div>',
                            unsafe_allow_html=True)
        else:
            st.markdown("""
<div class="conv-empty-state">
    <p>Enter a value on the left to see the result.</p>
</div>
""", unsafe_allow_html=True)
    else:
        if swahili_input:
            try:
                result = str(swahili_to_number(swahili_input))
                st.markdown(f"""
                <div class="conv-result-card">
                    <div class="conv-result-label">Arabic numeral</div>
                    <div class="conv-result-value">{result}</div>
                </div>
                """, unsafe_allow_html=True)
            except Exception as e:
                st.markdown(f'<div class="conv-error-card"><p class="conv-error-text">{e}</p></div>',
                            unsafe_allow_html=True)
        else:
            st.markdown("""
<div class="conv-empty-state">
    <p>Enter a value on the left to see the result.</p>
</div>
""", unsafe_allow_html=True)


# ── NAVIGATION ──────────────────────────────────────────────
footer_nav("Swahili", "converter")
