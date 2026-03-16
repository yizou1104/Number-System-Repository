import streamlit as st
from ui import apply_global_styles, home_nav
 
# ============================================================
# IGBO NUMERAL SYSTEM
# Bidirectional: Arabic ↔ Igbo
# Two output systems: modern decimal + traditional vigesimal
# ============================================================
 
IGBO_DIGITS = {
    0: "efu",    1: "otu",    2: "abụọ",  3: "atọ",
    4: "anọ",    5: "ise",    6: "isii",  7: "asaa",
    8: "asatọ",  9: "itoolu", 10: "iri",
}
 
# Reverse lookup for parser
ATOMS = {v: k for k, v in IGBO_DIGITS.items()}
 
VIG_BASE  = "ọgụ"   # one score = 20
VIG_SUPER = "nnu"   # superbase = 400
CONNECTOR = "na"
 
# ── Arabic → Igbo (decimal) ────────────────────────────────────────────────
def number_to_igbo_decimal(n: int) -> str:
    if n < 0:
        raise ValueError("Negative numbers not supported")
    if n == 0:
        return IGBO_DIGITS[0]
    if n <= 10:
        return IGBO_DIGITS[n]
    if n < 100:
        tens, units = n // 10, n % 10
        result = f"iri {IGBO_DIGITS[tens]}" if tens > 1 else "iri"
        if units:
            result += f" na {IGBO_DIGITS[units]}"
        return result
    if n < 1000:
        hundreds, rem = n // 100, n % 100
        result = "otu narị" if hundreds == 1 else f"{IGBO_DIGITS[hundreds]} narị"
        if rem:
            result += f" na {number_to_igbo_decimal(rem)}"
        return result
    thousands, rem = n // 1000, n % 1000
    result = "otu puku" if thousands == 1 else f"{number_to_igbo_decimal(thousands)} puku"
    if rem:
        result += f" na {number_to_igbo_decimal(rem)}"
    return result
 
 
# ── Arabic → Igbo (vigesimal) ──────────────────────────────────────────────
def _multiplier_word(m: int) -> str:
    """Express a score-multiplier (1–19) in Igbo words."""
    if m in IGBO_DIGITS:
        return IGBO_DIGITS[m]
    if 11 <= m <= 19:
        return f"iri na {IGBO_DIGITS[m - 10]}"
    raise ValueError(f"Multiplier {m} out of expected range (1–19)")
 
def number_to_igbo_vigesimal(n: int) -> str:
    """
    Convert n to traditional Igbo vigesimal form.
    Range: 0–1999.
    ọgụ = 20 (one score), nnu = 400 (one superbase, 20²).
    Subtractive for 11–19 (from 20), 30–39 (from 40),
    and proximity-based for remainders 11–19 within score groups.
    """
    if n < 0:
        raise ValueError("Negative numbers not supported")
    if n > 1999:
        return "not defined (beyond traditional vigesimal range)"
    if n in IGBO_DIGITS:
        return IGBO_DIGITS[n]
    # 11–19: subtractive from 20
    if 10 < n < 20:
        return f"{IGBO_DIGITS[20 - n]} na iri abụọ"
    if n == 20:
        return VIG_BASE
    # 21–29: additive to one score
    if 20 < n < 30:
        return f"{VIG_BASE} na {IGBO_DIGITS[n - 20]}"
    # 30–39: subtractive from 40
    if 30 <= n < 40:
        return f"{IGBO_DIGITS[40 - n]} na {VIG_BASE} abụọ"
    # 40–399: score multiples
    if n < 400:
        multiple, remainder = n // 20, n % 20
        head = VIG_BASE if multiple == 1 else f"{VIG_BASE} {_multiplier_word(multiple)}"
        if remainder == 0:
            return head
        if remainder <= 10:
            return f"{head} na {IGBO_DIGITS[remainder]}"
        # Subtractive remainder 11–19: short of next score
        next_multiple = multiple + 1
        next_head = VIG_SUPER if next_multiple == 20 else f"{VIG_BASE} {_multiplier_word(next_multiple)}"
        return f"{IGBO_DIGITS[20 - remainder]} na {next_head}"
    if n == 400:
        return VIG_SUPER
    if n < 800:
        return f"{VIG_SUPER} na {number_to_igbo_vigesimal(n - 400)}"
    # 800–1999: nnu multiples
    multiple, remainder = n // 400, n % 400
    head = f"{VIG_SUPER} {IGBO_DIGITS[multiple]}"
    return head if remainder == 0 else f"{head} na {number_to_igbo_vigesimal(remainder)}"
 
 
# ── Igbo → Arabic (parser) ─────────────────────────────────────────────────
def igbo_to_number(text: str) -> int:
    """
    Parse an Igbo numeral string (decimal or vigesimal) into an integer.
 
    Decimal uses: iri (×10 as tens), narị (×100), puku (×1000)
    Vigesimal uses: ọgụ (×20), nnu (×400)
    Connector: na
 
    Subtractive patterns detected:
      X na iri abụọ  → 20 − X  (vigesimal teens 11–19)
      X na ọgụ N    → N×20 − X (vigesimal proximity 30–39 and others)
      X na nnu [N]  → N×400 − X (e.g. otu na nnu = 399)
    """
    text = text.strip()
    if not text:
        raise ValueError("Empty input")
    tokens = text.split()
 
    # Detect subtractive teen (X na iri abụọ) — vigesimal but no ọgụ/nnu token
    if len(tokens) >= 4 and tokens[-2:] == ["iri", "abụọ"] and tokens[-3] == CONNECTOR:
        pre = tokens[:-3]
        if pre and all(t in ATOMS for t in pre):
            return 20 - ATOMS[pre[0]]
 
    is_vigesimal = VIG_BASE in tokens or VIG_SUPER in tokens
    return _parse_vigesimal(tokens) if is_vigesimal else _parse_decimal(tokens)
 
 
def _parse_vigesimal(tokens: list) -> int:
    if not tokens:
        raise ValueError("Empty")
    if len(tokens) == 1:
        t = tokens[0]
        if t in ATOMS:    return ATOMS[t]
        if t == VIG_BASE: return 20
        if t == VIG_SUPER: return 400
        raise ValueError(f"Unknown token: {t!r}")
 
    # Subtractive teen: X na iri abụọ
    if tokens[-2:] == ["iri", "abụọ"] and CONNECTOR in tokens:
        na_i = next(i for i, t in enumerate(tokens) if t == CONNECTOR)
        left = tokens[:na_i]
        if left and left[0] in ATOMS:
            return 20 - ATOMS[left[0]]
 
    # Subtractive to ọgụ/nnu: X na [VIG_BASE or VIG_SUPER] ...
    if len(tokens) >= 3 and tokens[1] == CONNECTOR and tokens[2] in (VIG_BASE, VIG_SUPER):
        sub = ATOMS.get(tokens[0])
        if sub is not None:
            return _parse_vigesimal(tokens[2:]) - sub
 
    if tokens[0] == VIG_SUPER:
        return _parse_vig_base(tokens, VIG_SUPER, 400)
    if tokens[0] == VIG_BASE:
        return _parse_vig_base(tokens, VIG_BASE, 20)
 
    if CONNECTOR in tokens:
        i = tokens.index(CONNECTOR)
        return _parse_vigesimal(tokens[:i]) + _parse_vigesimal(tokens[i + 1:])
 
    raise ValueError(f"Cannot parse vigesimal: {' '.join(tokens)!r}")
 
 
def _parse_vig_base(tokens: list, base_word: str, base_value: int) -> int:
    """
    tokens[0] == base_word.
    Format: base_word [multiplier]? (na [remainder])?
    The multiplier may itself contain 'na' (e.g. 'iri na otu' = 11), so we
    only split on a 'na' that is NOT immediately preceded by 'iri'.
    """
    rest = tokens[1:]
    if not rest:
        return base_value
 
    # Find the additive separator: first 'na' NOT preceded by 'iri'
    split_at = len(rest)
    for i, t in enumerate(rest):
        if t == CONNECTOR and not (i > 0 and rest[i - 1] == "iri"):
            split_at = i
            break
 
    mult_tokens = rest[:split_at]
    rem_tokens  = rest[split_at + 1:]  # skip the 'na'
 
    mult  = _parse_vigesimal(mult_tokens) if mult_tokens else 1
    total = mult * base_value
    if rem_tokens:
        total += _parse_vigesimal(rem_tokens)
    return total
 
 
def _parse_decimal(tokens: list) -> int:
    if not tokens:
        raise ValueError("Empty")
    if len(tokens) == 1:
        t = tokens[0]
        if t in ATOMS: return ATOMS[t]
        raise ValueError(f"Unknown token: {t!r}")
 
    if "puku" in tokens:
        i = tokens.index("puku")
        lt, rt = tokens[:i], tokens[i + 1:]
        total = (_parse_decimal(lt) if lt else 1) * 1000
        if rt:
            if rt[0] == CONNECTOR: rt = rt[1:]
            total += _parse_decimal(rt)
        return total
 
    if "narị" in tokens:
        i = tokens.index("narị")
        lt, rt = tokens[:i], tokens[i + 1:]
        total = (_parse_decimal(lt) if lt else 1) * 100
        if rt:
            if rt[0] == CONNECTOR: rt = rt[1:]
            total += _parse_decimal(rt)
        return total
 
    if "iri" in tokens:
        i = tokens.index("iri")
        rt = tokens[i + 1:]
        # If the next token is a digit (not a connector), it's the tens multiplier
        if rt and rt[0] != CONNECTOR and rt[0] in ATOMS:
            total = ATOMS[rt[0]] * 10
            rem = rt[1:]
            if rem:
                if rem[0] == CONNECTOR: rem = rem[1:]
                total += _parse_decimal(rem)
            return total
        # iri alone or iri na [unit]
        total = 10
        if rt:
            if rt[0] == CONNECTOR: rt = rt[1:]
            if rt: total += _parse_decimal(rt)
        return total
 
    if CONNECTOR in tokens:
        i = tokens.index(CONNECTOR)
        return _parse_decimal(tokens[:i]) + _parse_decimal(tokens[i + 1:])
 
    raise ValueError(f"Cannot parse decimal: {' '.join(tokens)!r}")
 
 
# ============================================================
# PAGE CONFIG & STYLES
# ============================================================
st.set_page_config(page_title="Igbo Numeral Converter", layout="centered")
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
 
# ── MASTHEAD ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="conv-masthead">
    <div class="conv-masthead-eyebrow">Numeral Converter</div>
    <div class="conv-masthead-title">Igbo Numerals</div>
    <div class="conv-masthead-desc">
        Bidirectional conversion between Arabic numerals and Igbo —
        modern decimal system and traditional vigesimal system
        (<em>ọgụ</em> = 20, <em>nnu</em> = 400).
    </div>
</div>
""", unsafe_allow_html=True)
 
# ── DIRECTION SELECTOR ──────────────────────────────────────────────────────
st.markdown('<div class="conv-section-label">Conversion Direction</div>', unsafe_allow_html=True)
 
direction = st.radio(
    "Conversion direction",
    ["Arabic → Igbo", "Igbo → Arabic"],
    horizontal=True,
    label_visibility="collapsed",
    key="igbo_direction",
)
 
# ── PRESET EXAMPLES ─────────────────────────────────────────────────────────
st.markdown('<div class="conv-section-label">Preset Examples</div>', unsafe_allow_html=True)
 
# Arabic presets cover: atom, subtractive teen, exact score, additive, subtractive-to-next,
# exact double-score, large decimal, 400-range
arabic_presets = [5, 11, 20, 30, 40, 59, 100, 400]
 
# Igbo presets: mix of decimal and vigesimal forms
igbo_presets = [
    "ise",               # 5
    "itoolu na iri abụọ", # 11 (vigesimal teen)
    "ọgụ",              # 20
    "iri na ọgụ abụọ",  # 30 (vigesimal subtractive)
    "ọgụ abụọ",         # 40
    "otu na ọgụ atọ",   # 59 (vigesimal proximity subtractive)
    "otu narị",          # 100 (decimal)
    "nnu",              # 400
]
 
with st.container(border=True):
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
 
# ── INPUT & CONVERSION ──────────────────────────────────────────────────────
st.markdown('<div class="conv-section-label">Convert</div>', unsafe_allow_html=True)
 
if direction == "Arabic → Igbo":
    st.markdown("""
    <div class="conv-input-card">
        <div class="conv-input-title">Enter an Arabic numeral</div>
        <div class="conv-input-hint">
            Returns both decimal and vigesimal forms.
            Vigesimal range is 0–1999.
        </div>
    </div>
    """, unsafe_allow_html=True)
    arabic_input = st.text_input(
        "Arabic numeral", key="arabic_input",
        placeholder="e.g. 59", label_visibility="collapsed",
    )
    if arabic_input:
        if arabic_input.lstrip("-").isdigit():
            try:
                n   = int(arabic_input)
                dec = number_to_igbo_decimal(n)
                vig = number_to_igbo_vigesimal(n)
                st.markdown(f"""
                <div class="conv-result-card">
                    <div class="conv-result-label">Igbo numeral</div>
                    <div class="conv-result-row">
                        <span class="conv-result-sublabel">Decimal</span>
                        <span class="conv-result-subvalue">{dec}</span>
                    </div>
                    <div class="conv-result-row">
                        <span class="conv-result-sublabel">Vigesimal</span>
                        <span class="conv-result-subvalue">{vig}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            except Exception as e:
                st.markdown(f'<div class="conv-error-card"><p class="conv-error-text">{e}</p></div>',
                            unsafe_allow_html=True)
        else:
            st.markdown('<div class="conv-error-card"><p class="conv-error-text">Please enter a valid whole number.</p></div>',
                        unsafe_allow_html=True)
 
else:  # Igbo → Arabic
    st.markdown("""
    <div class="conv-input-card">
        <div class="conv-input-title">Enter an Igbo numeral</div>
        <div class="conv-input-hint">
            Accepts both decimal forms (<em>iri, narị, puku</em>) and vigesimal forms
            (<em>ọgụ, nnu</em>), including subtractive constructions.
        </div>
    </div>
    """, unsafe_allow_html=True)
    igbo_input = st.text_input(
        "Igbo numeral", key="igbo_input",
        placeholder="e.g. ọgụ abụọ na iri",
        label_visibility="collapsed",
    )
    if igbo_input:
        try:
            result = str(igbo_to_number(igbo_input))
            st.markdown(f"""
            <div class="conv-result-card">
                <div class="conv-result-label">Arabic numeral</div>
                <div class="conv-result-single">{result}</div>
            </div>
            """, unsafe_allow_html=True)
        except Exception as e:
            st.markdown(f'<div class="conv-error-card"><p class="conv-error-text">{e}</p></div>',
                        unsafe_allow_html=True)
 
# ── CAPTION & NAVIGATION ────────────────────────────────────────────────────
st.markdown("""
<div class="conv-caption">
    Implements both modern decimal Igbo and the traditional vigesimal system
    (<em>ọgụ</em> = 20, <em>nnu</em> = 400). Vigesimal uses subtractive construction
    for 11–19, 30–39, and proximity-based subtraction within score groups.
    Reverse parser handles decimal and vigesimal forms, including subtractive patterns.
    Data from <a href="https://www.omniglot.com/language/numbers/igbo.htm" target="_blank">Omniglot</a>.
    Algorithm by Yi Zou.
</div>
""", unsafe_allow_html=True)
 
st.markdown("""
<div class="conv-nav-footer">
    <a class="conv-nav-btn active" href="/Igbo_Converter">Igbo Converter</a>
    <a class="conv-nav-btn" href="/Igbo_Linguistics">Igbo Linguistics →</a>
</div>
""", unsafe_allow_html=True)
home_nav()