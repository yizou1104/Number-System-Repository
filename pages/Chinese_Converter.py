import streamlit as st
from ui import apply_global_styles, home_nav

# ============================================================
# CHINESE NUMERAL SYSTEM (Simplified / Mandarin)
# Bidirectional: Arabic ↔ Chinese
#
# Rules:
#   1. 两 (liǎng) replaces 二 (èr) before 百/千/万/亿
#   2. 零 (líng) inserted once for any run of internal zeros
#   3. Standalone 10 and leading tens in 11–19: 十 not 一十
#   4. Grouping by 万 (10,000) and 亿 (100,000,000)
#
# Sources: chineseclass101.com, omniglot, Yip & Rimmington
#          "Chinese: A Comprehensive Grammar"
# ============================================================

# ── Backend ──────────────────────────────────────────────────────────────────

_DIGITS: dict[int, str] = {
    0: "零", 1: "一", 2: "二", 3: "三", 4: "四",
    5: "五", 6: "六", 7: "七", 8: "八", 9: "九",
}

_DIGIT_VALUES: dict[str, int] = {v: k for k, v in _DIGITS.items()}
_DIGIT_VALUES["两"] = 2

_UNIT_VALUES: dict[str, int] = {
    "亿": 100_000_000, "万": 10_000,
    "千": 1_000, "百": 100, "十": 10,
}


def _segment(n: int, force_yi: bool = False) -> str:
    """Convert 1–9999 to Chinese. force_yi=True keeps 一十 in compounds."""
    assert 1 <= n <= 9999
    parts: list[str] = []
    rem = n
    if rem >= 1000:
        d = rem // 1000
        parts.append(("两" if d == 2 else _DIGITS[d]) + "千")
        rem %= 1000
        if 0 < rem < 100:
            parts.append("零")
    if rem >= 100:
        d = rem // 100
        parts.append(("两" if d == 2 else _DIGITS[d]) + "百")
        rem %= 100
        if 0 < rem < 10:
            parts.append("零")
    if rem >= 10:
        d = rem // 10
        if d == 1 and not parts and not force_yi:
            parts.append("十")
        else:
            parts.append(_DIGITS[d] + "十")
        rem %= 10
    if rem > 0:
        parts.append(_DIGITS[rem])
    return "".join(parts)


def number_to_chinese(n: int) -> str:
    """Convert 0–999,999,999 to Simplified Chinese."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"Expected int, got {type(n).__name__}")
    if n < 0:
        raise ValueError("Negative numbers are not supported.")
    if n > 999_999_999:
        raise ValueError("Supported range is 0–999,999,999.")
    if n == 0:
        return "零"
    if n < 10_000:
        return _segment(n)

    parts: list[str] = []
    rem = n

    if rem >= 100_000_000:
        yi = rem // 100_000_000
        rem %= 100_000_000
        parts.append(("两" if yi == 2 else _segment(yi, force_yi=True)) + "亿")
        if 0 < rem < 10_000_000:
            parts.append("零")

    if rem >= 10_000:
        wan = rem // 10_000
        rem %= 10_000
        parts.append((_segment(wan, force_yi=False)) + "万")
        if 0 < rem < 1_000:
            parts.append("零")

    if rem > 0:
        parts.append(_segment(rem, force_yi=True))

    return "".join(parts)


def chinese_to_number(text: str) -> int:
    """Parse Simplified Chinese numeral string to int."""
    text = text.strip()
    if not text:
        raise ValueError("Empty input.")
    if text == "零":
        return 0

    def _parse_seg(chars: str) -> int:
        if not chars:
            return 0
        total = 0
        cur = 0
        for ch in chars:
            if ch == "零":
                continue
            if ch in _DIGIT_VALUES:
                cur = _DIGIT_VALUES[ch]
            elif ch in _UNIT_VALUES:
                u = _UNIT_VALUES[ch]
                if u == 10 and cur == 0:
                    cur = 1
                total += cur * u
                cur = 0
            else:
                raise ValueError(f"Unrecognised character: '{ch}'")
        total += cur
        return total

    total = 0
    yi = text.find("亿")
    if yi != -1:
        total += _parse_seg(text[:yi]) * 100_000_000
        text = text[yi + 1:]
    wan = text.find("万")
    if wan != -1:
        total += _parse_seg(text[:wan]) * 10_000
        text = text[wan + 1:]
    total += _parse_seg(text)
    return total


# ============================================================
# PAGE CONFIG & STYLES
# ============================================================
st.set_page_config(page_title="Chinese Numeral Converter", layout="centered")
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

# ── MASTHEAD ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="conv-masthead">
    <div class="conv-masthead-eyebrow">Numeral Converter</div>
    <div class="conv-masthead-title">Chinese Numerals</div>
    <div class="conv-masthead-desc">
        Bidirectional conversion between Arabic numerals and Simplified Chinese,
        with correct handling of 两, 零 placeholders, and 万/亿 grouping.
    </div>
</div>
""", unsafe_allow_html=True)

# ── DIRECTION SELECTOR ───────────────────────────────────────────────────────
st.markdown('<div class="conv-section-label">Conversion Direction</div>', unsafe_allow_html=True)

direction = st.radio(
    "Conversion direction",
    ["Arabic → Chinese", "Chinese → Arabic"],
    horizontal=True,
    label_visibility="collapsed",
    key="chinese_direction",
)

# ── PRESET EXAMPLES ──────────────────────────────────────────────────────────
st.markdown('<div class="conv-section-label">Preset Examples</div>', unsafe_allow_html=True)

arabic_presets  = [0, 10, 101, 200, 1010, 10000, 100000, 12345678]
chinese_presets = ["零", "十", "一百零一", "两百", "一千零一十", "一万", "十万", "一千两百三十四万五千六百七十八"]

with st.container(border=True):
    st.markdown('<p class="conv-presets-sublabel">Click a value to load it</p>', unsafe_allow_html=True)
    cols = st.columns(4)
    if direction == "Arabic → Chinese":
        for i, num in enumerate(arabic_presets):
            if cols[i % 4].button(str(num), key=f"p_a_{i}", use_container_width=True):
                st.session_state["arabic_input"] = str(num)
    else:
        for i, txt in enumerate(chinese_presets):
            if cols[i % 4].button(txt, key=f"p_b_{i}", use_container_width=True):
                st.session_state["chinese_input"] = txt

# ── INPUT & CONVERSION ───────────────────────────────────────────────────────
st.markdown('<div class="conv-section-label">Convert</div>', unsafe_allow_html=True)

if direction == "Arabic → Chinese":
    st.markdown("""
    <div class="conv-input-card">
        <div class="conv-input-title">Enter an Arabic numeral</div>
        <div class="conv-input-hint">Whole number from 0 to 999,999,999.</div>
    </div>
    """, unsafe_allow_html=True)
    arabic_input = st.text_input(
        "Arabic numeral", key="arabic_input",
        placeholder="e.g. 10100", label_visibility="collapsed",
    )
    if arabic_input:
        if arabic_input.isdigit():
            try:
                result = number_to_chinese(int(arabic_input))
                st.markdown(f"""
                <div class="conv-result-card">
                    <div class="conv-result-label">Chinese numeral</div>
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
    <div class="conv-input-card">
        <div class="conv-input-title">Enter a Chinese numeral</div>
        <div class="conv-input-hint">Simplified Chinese characters, e.g. <em>一千零一十</em>.</div>
    </div>
    """, unsafe_allow_html=True)
    chinese_input = st.text_input(
        "Chinese numeral", key="chinese_input",
        placeholder="e.g. 一千零一十", label_visibility="collapsed",
    )
    if chinese_input:
        try:
            result = str(chinese_to_number(chinese_input))
            st.markdown(f"""
            <div class="conv-result-card">
                <div class="conv-result-label">Arabic numeral</div>
                <div class="conv-result-value">{result}</div>
            </div>
            """, unsafe_allow_html=True)
        except Exception as e:
            st.markdown(f'<div class="conv-error-card"><p class="conv-error-text">{e}</p></div>',
                        unsafe_allow_html=True)

# ── NAVIGATION ──────────────────────────────────────────────
st.markdown('<div class="nav-row">', unsafe_allow_html=True)
st.page_link("pages/Chinese_Linguistics.py", label="Chinese Linguistics →")
st.page_link("Home.py", label="← Home")
st.markdown('</div>', unsafe_allow_html=True)