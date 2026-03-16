import streamlit as st
from ui import apply_global_styles, home_nav

# ============================================================
# THAI NUMERAL SYSTEM
# Bidirectional: Arabic ↔ Thai
# ============================================================

THAI_DIGITS = {
    0:"ศูนย์", 1:"หนึ่ง", 2:"สอง", 3:"สาม", 4:"สี่",
    5:"ห้า",   6:"หก",    7:"เจ็ด", 8:"แปด", 9:"เก้า",
}

THAI_VALUES = {
    "ศูนย์":1, "หนึ่ง":1, "เอ็ด":1, "สอง":2, "ยี่":2,
    "สาม":3,  "สี่":4,   "ห้า":5,  "หก":6,  "เจ็ด":7,
    "แปด":8,  "เก้า":9,
}
THAI_VALUES["ศูนย์"] = 0  # fix zero

THAI_UNITS = [
    (10**6, "ล้าน"),
    (10**5, "แสน"),
    (10**4, "หมื่น"),
    (10**3, "พัน"),
    (10**2, "ร้อย"),
    (10,    "สิบ"),
]

UNIT_VALUES = {
    "สิบ":10, "ร้อย":100, "พัน":1000,
    "หมื่น":10000, "แสน":100000, "ล้าน":1000000,
}

def number_to_thai(n: int) -> str:
    if n < 0:
        raise ValueError("Negative numbers not supported")
    if n == 0:
        return THAI_DIGITS[0]
    result = ""
    remaining = n
    for value, unit in THAI_UNITS:
        digit = remaining // value
        remaining %= value
        if digit == 0:
            continue
        if value == 10:
            if digit == 1:
                result += "สิบ"
            elif digit == 2:
                result += "ยี่สิบ"
            else:
                result += THAI_DIGITS[digit] + "สิบ"
        else:
            if digit == 1:
                result += unit
            else:
                result += THAI_DIGITS[digit] + unit
    if remaining > 0:
        result += "เอ็ด" if remaining == 1 and result else THAI_DIGITS[remaining]
    return result

def thai_to_number(text: str) -> int:
    total = 0
    current = 0
    i = 0
    while i < len(text):
        matched = False
        for unit, value in UNIT_VALUES.items():
            if text.startswith(unit, i):
                if current == 0:
                    current = 1
                current *= value
                total += current
                current = 0
                i += len(unit)
                matched = True
                break
        if matched:
            continue
        for word, value in THAI_VALUES.items():
            if text.startswith(word, i):
                current += value
                i += len(word)
                matched = True
                break
        if not matched:
            raise ValueError("Invalid Thai numeral format")
    return total + current


# ============================================================
# PAGE CONFIG & STYLES
# ============================================================
st.set_page_config(page_title="Thai Numeral Converter", layout="centered")
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

# ── MASTHEAD ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="conv-masthead">
    <div class="conv-masthead-eyebrow">Numeral Converter</div>
    <div class="conv-masthead-title">Thai Numerals</div>
    <div class="conv-masthead-desc">
        Bidirectional conversion between Arabic numerals and Thai numerals,
        with explicit handling of irregular forms like ยี่ and เอ็ด.
    </div>
</div>
""", unsafe_allow_html=True)

# ── DIRECTION SELECTOR ──────────────────────────────────────────────────────
st.markdown('<div class="conv-section-label">Conversion Direction</div>', unsafe_allow_html=True)

direction = st.radio(
    "Conversion direction",
    ["Arabic → Thai", "Thai → Arabic"],
    horizontal=True,
    label_visibility="collapsed",
    key="thai_direction",
)

# ── PRESET EXAMPLES ─────────────────────────────────────────────────────────
st.markdown('<div class="conv-section-label">Preset Examples</div>', unsafe_allow_html=True)

arabic_presets = [0, 5, 11, 21, 45, 100, 256, 2024]
thai_presets   = [
    "ศูนย์", "ห้า", "สิบเอ็ด", "ยี่สิบเอ็ด",
    "สี่สิบห้า", "หนึ่งร้อย", "สองร้อยห้าสิบหก", "สองพันยี่สิบสี่",
]

with st.container(border=True):
    st.markdown('<p class="conv-presets-sublabel">Click a value to load it</p>', unsafe_allow_html=True)
    cols = st.columns(4)
    if direction == "Arabic → Thai":
        for i, num in enumerate(arabic_presets):
            if cols[i % 4].button(str(num), key=f"p_a_{i}", use_container_width=True):
                st.session_state["arabic_input"] = str(num)
    else:
        for i, txt in enumerate(thai_presets):
            if cols[i % 4].button(txt, key=f"p_b_{i}", use_container_width=True):
                st.session_state["thai_input"] = txt

# ── INPUT & CONVERSION ──────────────────────────────────────────────────────
st.markdown('<div class="conv-section-label">Convert</div>', unsafe_allow_html=True)

if direction == "Arabic → Thai":
    st.markdown("""
    <div class="conv-input-card">
        <div class="conv-input-title">Enter an Arabic numeral</div>
        <div class="conv-input-hint">Type a whole number, or click a preset above.</div>
    </div>
    """, unsafe_allow_html=True)
    arabic_input = st.text_input(
        "Arabic numeral", key="arabic_input",
        placeholder="e.g. 256", label_visibility="collapsed",
    )
    if arabic_input:
        if arabic_input.isdigit():
            try:
                result = number_to_thai(int(arabic_input))
                st.markdown(f"""
                <div class="conv-result-card">
                    <div class="conv-result-label">Thai numeral</div>
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
        <div class="conv-input-title">Enter a Thai numeral</div>
        <div class="conv-input-hint">Standard Thai script, e.g. <em>สองร้อยห้าสิบหก</em>.</div>
    </div>
    """, unsafe_allow_html=True)
    thai_input = st.text_input(
        "Thai numeral", key="thai_input",
        placeholder="e.g. สองร้อยห้าสิบหก", label_visibility="collapsed",
    )
    if thai_input:
        try:
            result = str(thai_to_number(thai_input))
            st.markdown(f"""
            <div class="conv-result-card">
                <div class="conv-result-label">Arabic numeral</div>
                <div class="conv-result-value">{result}</div>
            </div>
            """, unsafe_allow_html=True)
        except Exception as e:
            st.markdown(f'<div class="conv-error-card"><p class="conv-error-text">{e}</p></div>',
                        unsafe_allow_html=True)

# ── CAPTION & NAVIGATION ────────────────────────────────────────────────────
st.markdown("""
<div class="conv-caption">
    Implements a rule-based Thai numeral system. Irregular forms (ยี่ for 20s, เอ็ด for final 1)
    handled explicitly. Converter algorithm by Yi Zou. Grammar detail in the Linguistics section.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="conv-nav-footer">
    <a class="conv-nav-btn active" href="/Thai_Converter">Thai Converter</a>
    <a class="conv-nav-btn" href="/Thai_Linguistics">Thai Linguistics →</a>
</div>
""", unsafe_allow_html=True)
home_nav()