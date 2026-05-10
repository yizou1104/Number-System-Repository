import streamlit as st
from ui import apply_global_styles, home_nav

# ============================================================
# TRADITIONAL YORUBA NUMERAL GENERATOR (FINAL)
# ============================================================

ATOMS = {
    1:"ọ̀kan",2:"èjì",3:"ẹ̀ta",4:"ẹ̀rin",5:"àrún",
    6:"ẹ̀fà",7:"èje",8:"ẹ̀jọ",9:"ẹ̀sán",10:"ẹ̀wá",
}

BASES = {
    20:"ogún",30:"ọgbọ̀n",40:"ogójì",50:"àádọ́ta",
    60:"ọgọ́ta",70:"àádọ́rin",80:"ọgọ́rin",90:"àádọ́rùn",
}

THOUSAND = "ẹgbẹ̀rún"

LEXICAL = {
    11:"ọ̀kanlá",12:"èjìlá",13:"ẹ̀talá",14:"ẹ̀rinlá",
    15:"ẹ́ẹdógún",16:"ẹẹ́rìndílógún",17:"eétàdílógún",
    18:"eéjìdílógún",19:"oókàndílógún",
    110:"àádọ́fà",120:"ọgọ́fà",
    200:"igba",300:"ọ̀ọ́dúrún",400:"irinwó",
    500:"ọ̀ọ́dẹ́gbẹ̀ta",600:"ẹgbẹ̀ta",700:"ọ̀ọ́dẹ́gbẹ̀rin",
    800:"ẹgbẹ̀rin",900:"ẹ̀ẹ́dẹ́gbẹ̀rún",
}

def additive(x, base): return f"{x} lélọ́ {base}"
def subtractive(x, base): return f"{x} dín lọ́ {base}"
def select_base(n): return max(b for b in BASES if b < n)

_LEX_HUNDREDS = sorted(k for k in {110, 120, 200, 300, 400, 500, 600, 700, 800, 900})

def number_to_yoruba(n):
    if n < 0 or n >= 2000:
        raise ValueError("Supported range is 0–1999")
    if n == 0:
        return "òdo"
    if n >= 1000:
        remainder = n - 1000
        if remainder == 0:
            return THOUSAND
        return additive(number_to_yoruba(remainder), THOUSAND)
    if n in LEXICAL:
        return LEXICAL[n]
    if n in ATOMS:
        return ATOMS[n]
    if n in BASES:
        return BASES[n]
    if n <= 109:
        base = select_base(n)
        remainder = n - base
        if remainder <= base / 2:
            return additive(number_to_yoruba(remainder), BASES[base])
        higher_bases = [b for b in BASES if b > base]
        if not higher_bases:
            return additive(number_to_yoruba(remainder), BASES[base])
        next_base = min(higher_bases)
        diff = next_base - n
        return subtractive(number_to_yoruba(diff), BASES[next_base])
    # 110-999: decompose against LEXICAL hundreds
    below = [k for k in _LEX_HUNDREDS if k < n]
    above = [k for k in _LEX_HUNDREDS if k > n]
    if not below:
        h = min(above)
        return subtractive(number_to_yoruba(h - n), LEXICAL[h])
    if not above:
        h = max(below)
        return additive(number_to_yoruba(n - h), LEXICAL[h])
    prev_h, next_h = max(below), min(above)
    rem_below, rem_above = n - prev_h, next_h - n
    if rem_below <= (next_h - prev_h) / 2:
        return additive(number_to_yoruba(rem_below), LEXICAL[prev_h])
    return subtractive(number_to_yoruba(rem_above), LEXICAL[next_h])

# ============================================================
# PAGE CONFIG & STYLES
# ============================================================
st.set_page_config(page_title='Yoruba Numeral Converter', layout='centered')
apply_global_styles()

CONV_CSS = '<style>\n.conv-masthead{border-top:3px solid var(--ink);border-bottom:1px solid var(--rule);padding:1.75rem 0 1.4rem 0;margin-bottom:1.75rem}\n.conv-masthead-eyebrow{font-family:\'DM Sans\',sans-serif;font-size:.68rem;font-weight:700;text-transform:uppercase;letter-spacing:.18em;color:var(--accent);display:flex;align-items:center;gap:.65rem;margin-bottom:.65rem}\n.conv-masthead-eyebrow::before{content:\'\';display:inline-block;width:1.75rem;height:1.5px;background:var(--accent);flex-shrink:0}\n.conv-masthead-title{font-family:\'Crimson Pro\',Georgia,serif;font-size:3rem;font-weight:700;color:var(--ink);letter-spacing:-.04em;line-height:1.05;margin-bottom:.5rem}\n.conv-masthead-desc{font-family:\'Crimson Pro\',Georgia,serif;font-style:italic;font-size:1.05rem;color:var(--ink-muted);line-height:1.55;margin:0}\n.conv-section-label{font-family:\'DM Sans\',sans-serif;font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.16em;color:var(--ink-soft);display:flex;align-items:center;gap:1rem;margin:2rem 0 1rem 0}\n.conv-section-label::before{content:\'\';display:inline-block;width:2rem;height:1px;background:var(--ink-muted);flex-shrink:0}\n.conv-section-label::after{content:\'\';flex:1;height:1px;background:var(--rule)}\ndiv[data-testid="stRadio"]>div{display:flex;gap:0;background:var(--card-bg);border:1px solid var(--card-border);border-radius:6px;padding:.35rem;box-shadow:0 1px 3px rgba(26,22,18,.05),0 4px 14px rgba(26,22,18,.04),inset 0 1px 0 rgba(255,255,255,.65);width:fit-content}\ndiv[data-testid="stRadio"] label{display:flex!important;align-items:center!important;font-family:\'DM Sans\',sans-serif!important;font-size:.9rem!important;font-weight:600!important;letter-spacing:.02em!important;text-transform:none!important;color:var(--ink-soft)!important;background:transparent!important;border:1.5px solid transparent!important;border-radius:4px!important;padding:.55rem 1.35rem!important;cursor:pointer!important;transition:all .18s cubic-bezier(.4,0,.2,1)!important;white-space:nowrap!important}\ndiv[data-testid="stRadio"] label>span:first-child{display:none!important}\ndiv[data-testid="stRadio"] label:hover{background:var(--parchment-3)!important;border-color:var(--rule-strong)!important;color:var(--ink)!important}\ndiv[data-testid="stRadio"] label:has(input:checked){background:var(--ink)!important;border-color:var(--ink)!important;box-shadow:3px 3px 0 var(--accent)!important;transform:translate(-1px,-1px)!important}\ndiv[data-testid="stRadio"] label:has(input:checked) p,div[data-testid="stRadio"] label:has(input:checked) span{color:var(--parchment)!important}\ndiv[data-testid="stRadio"] label p{font-family:\'DM Sans\',sans-serif!important;font-size:.9rem!important;font-weight:600!important;margin:0!important;line-height:1!important}\n.conv-presets-sublabel{font-family:\'DM Sans\',sans-serif;font-size:.65rem;font-weight:700;text-transform:uppercase;letter-spacing:.14em;color:var(--ink-faint);margin-bottom:.65rem;margin-top:0}\n.conv-input-card{background:var(--card-bg);border:1px solid var(--card-border);border-radius:6px;padding:1.3rem 1.5rem 1.4rem;margin-bottom:.5rem;box-shadow:0 1px 3px rgba(26,22,18,.05),0 6px 20px rgba(26,22,18,.06),inset 0 1px 0 rgba(255,255,255,.7)}\n.conv-input-title{font-family:\'Crimson Pro\',Georgia,serif;font-size:1.3rem;font-weight:600;color:var(--ink);letter-spacing:-.02em;margin:0 0 .25rem 0;line-height:1.2}\n.conv-input-hint{font-family:\'Crimson Pro\',Georgia,serif;font-style:italic;font-size:.93rem;color:var(--ink-faint);margin:0 0 .8rem 0;line-height:1.4}\n.conv-result-card{background:rgba(46,107,122,.04);border:1px solid rgba(46,107,122,.18);border-left:3px solid var(--teal);border-radius:0 4px 4px 0;padding:.75rem 1.1rem;margin-top:.8rem}\n.conv-result-label{font-family:\'DM Sans\',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.14em;color:var(--teal);margin-bottom:.3rem}\n.conv-result-value{font-family:\'Crimson Pro\',Georgia,serif;font-size:1.05rem;font-weight:400;color:var(--ink);line-height:1.55;word-break:break-word}\n.conv-error-card{background:rgba(184,92,56,.05);border:1px solid rgba(184,92,56,.2);border-left:3px solid var(--accent);border-radius:0 4px 4px 0;padding:.75rem 1.1rem;margin-top:.8rem}\n.conv-error-text{font-family:\'Crimson Pro\',Georgia,serif;font-size:1rem;color:var(--accent);font-style:italic;margin:0}\n.conv-nav-footer{display:flex;gap:.75rem;padding:1.4rem 0 .5rem 0;border-top:1px solid var(--rule);margin-top:2.5rem;flex-wrap:wrap}\n.conv-nav-btn{font-family:\'DM Sans\',sans-serif;font-size:.78rem;font-weight:700;text-transform:uppercase;letter-spacing:.09em;color:var(--ink);background:var(--parchment-2);border:1.5px solid var(--rule-strong);border-radius:3px;padding:.55rem 1.1rem;text-decoration:none;display:inline-flex;align-items:center;gap:.4rem;white-space:nowrap;cursor:pointer;box-shadow:2px 2px 0 rgba(26,22,18,.08);transition:all .18s cubic-bezier(.4,0,.2,1)}\n.conv-nav-btn:hover{background:var(--ink);color:var(--parchment);border-color:var(--ink);box-shadow:3px 3px 0 var(--accent);transform:translate(-1px,-1px);text-decoration:none}\n.conv-nav-btn.active{background:var(--parchment-3);color:var(--ink-muted);cursor:default;box-shadow:none}\n.conv-nav-btn.active:hover{transform:none;background:var(--parchment-3);color:var(--ink-muted);border-color:var(--rule-strong);box-shadow:none}\n.conv-caption{font-family:\'DM Sans\',sans-serif;font-size:.75rem;color:var(--ink-faint);line-height:1.55;margin-top:1rem}\n.conv-caption a{color:var(--accent)!important;text-decoration:underline!important;text-decoration-color:rgba(184,92,56,.35)!important}\n.conv-caption a:hover{text-decoration-color:var(--accent)!important}\n</style>'
st.markdown(CONV_CSS, unsafe_allow_html=True)

st.markdown('''
<div class="conv-masthead">
    <div class="conv-masthead-eyebrow">Numeral Converter</div>
    <div class="conv-masthead-title">Yoruba Numerals</div>
    <div class="conv-masthead-desc">Convert Arabic numerals into traditional Yoruba numerals using the classical subtractive–additive vigesimal system.</div>
</div>
''', unsafe_allow_html=True)

direction = 'Arabic → Yoruba'
st.markdown('<div class="conv-section-label">Preset Examples</div>', unsafe_allow_html=True)

arabic_presets = [1, 5, 15, 19, 20, 29, 40, 100, 256, 400, 999, 1500]

with st.container(border=True):
    st.markdown('<p class="conv-presets-sublabel">Click a value to load it</p>', unsafe_allow_html=True)
    cols = st.columns(4)
    for i, num in enumerate(arabic_presets):
        if cols[i % 4].button(str(num), key=f'p_a_{i}', use_container_width=True):
            st.session_state['arabic_input'] = str(num)

st.markdown('<div class="conv-section-label">Convert</div>', unsafe_allow_html=True)

st.markdown('''
<div class="conv-input-card">
    <div class="conv-input-title">Enter an Arabic numeral (0–1999)</div>
    <div class="conv-input-hint">Type a whole number in the supported range, or click a preset above.</div>
</div>''', unsafe_allow_html=True)
arabic_input = st.text_input('Enter an Arabic numeral (0–1999)', key='arabic_input', placeholder='e.g. 256', label_visibility="collapsed")
if arabic_input:
    val = arabic_input.strip()
    if val.lstrip('-').isdigit():
        try:
            result = number_to_yoruba(int(val))
            st.markdown(f'''<div class="conv-result-card">
    <div class="conv-result-label">Yoruba</div>
    <div class="conv-result-value">{result}</div>
</div>''', unsafe_allow_html=True)
        except Exception as e:
            st.markdown(f'<div class="conv-error-card"><p class="conv-error-text">{e}</p></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="conv-error-card"><p class="conv-error-text">Please enter a valid whole number.</p></div>', unsafe_allow_html=True)


st.markdown('''
<div class="conv-caption">Implements the traditional Yoruba vigesimal system with subtractive dominance. Algorithm by Yi Zou.</div>
''', unsafe_allow_html=True)

# ── NAVIGATION ──────────────────────────────────────────────
st.markdown('<div class="nav-row">', unsafe_allow_html=True)
st.page_link("pages/Yoruba_Linguistics.py", label="Yoruba Linguistics →")
st.page_link("Home.py", label="← Home")
st.markdown('</div>', unsafe_allow_html=True)