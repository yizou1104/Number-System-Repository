import streamlit as st
from ui import apply_global_styles, home_nav
from cn2an import cn2an, an2cn

# ============================================================
# PAGE CONFIG & STYLES
# ============================================================
st.set_page_config(page_title='Chinese Numeral Converter', layout='centered')
apply_global_styles()

CONV_CSS = '<style>\n.conv-masthead{border-top:3px solid var(--ink);border-bottom:1px solid var(--rule);padding:1.75rem 0 1.4rem 0;margin-bottom:1.75rem}\n.conv-masthead-eyebrow{font-family:\'DM Sans\',sans-serif;font-size:.68rem;font-weight:700;text-transform:uppercase;letter-spacing:.18em;color:var(--accent);display:flex;align-items:center;gap:.65rem;margin-bottom:.65rem}\n.conv-masthead-eyebrow::before{content:\'\';display:inline-block;width:1.75rem;height:1.5px;background:var(--accent);flex-shrink:0}\n.conv-masthead-title{font-family:\'Crimson Pro\',Georgia,serif;font-size:3rem;font-weight:700;color:var(--ink);letter-spacing:-.04em;line-height:1.05;margin-bottom:.5rem}\n.conv-masthead-desc{font-family:\'Crimson Pro\',Georgia,serif;font-style:italic;font-size:1.05rem;color:var(--ink-muted);line-height:1.55;margin:0}\n.conv-section-label{font-family:\'DM Sans\',sans-serif;font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.16em;color:var(--ink-soft);display:flex;align-items:center;gap:1rem;margin:2rem 0 1rem 0}\n.conv-section-label::before{content:\'\';display:inline-block;width:2rem;height:1px;background:var(--ink-muted);flex-shrink:0}\n.conv-section-label::after{content:\'\';flex:1;height:1px;background:var(--rule)}\ndiv[data-testid="stRadio"]>div{display:flex;gap:0;background:var(--card-bg);border:1px solid var(--card-border);border-radius:6px;padding:.35rem;box-shadow:0 1px 3px rgba(26,22,18,.05),0 4px 14px rgba(26,22,18,.04),inset 0 1px 0 rgba(255,255,255,.65);width:fit-content}\ndiv[data-testid="stRadio"] label{display:flex!important;align-items:center!important;font-family:\'DM Sans\',sans-serif!important;font-size:.9rem!important;font-weight:600!important;letter-spacing:.02em!important;text-transform:none!important;color:var(--ink-soft)!important;background:transparent!important;border:1.5px solid transparent!important;border-radius:4px!important;padding:.55rem 1.35rem!important;cursor:pointer!important;transition:all .18s cubic-bezier(.4,0,.2,1)!important;white-space:nowrap!important}\ndiv[data-testid="stRadio"] label>span:first-child{display:none!important}\ndiv[data-testid="stRadio"] label:hover{background:var(--parchment-3)!important;border-color:var(--rule-strong)!important;color:var(--ink)!important}\ndiv[data-testid="stRadio"] label:has(input:checked){background:var(--ink)!important;border-color:var(--ink)!important;box-shadow:3px 3px 0 var(--accent)!important;transform:translate(-1px,-1px)!important}\ndiv[data-testid="stRadio"] label:has(input:checked) p,div[data-testid="stRadio"] label:has(input:checked) span{color:var(--parchment)!important}\ndiv[data-testid="stRadio"] label p{font-family:\'DM Sans\',sans-serif!important;font-size:.9rem!important;font-weight:600!important;margin:0!important;line-height:1!important}\n.conv-presets-sublabel{font-family:\'DM Sans\',sans-serif;font-size:.65rem;font-weight:700;text-transform:uppercase;letter-spacing:.14em;color:var(--ink-faint);margin-bottom:.65rem;margin-top:0}\n.conv-input-card{background:var(--card-bg);border:1px solid var(--card-border);border-radius:6px;padding:1.3rem 1.5rem 1.4rem;margin-bottom:.5rem;box-shadow:0 1px 3px rgba(26,22,18,.05),0 6px 20px rgba(26,22,18,.06),inset 0 1px 0 rgba(255,255,255,.7)}\n.conv-input-title{font-family:\'Crimson Pro\',Georgia,serif;font-size:1.3rem;font-weight:600;color:var(--ink);letter-spacing:-.02em;margin:0 0 .25rem 0;line-height:1.2}\n.conv-input-hint{font-family:\'Crimson Pro\',Georgia,serif;font-style:italic;font-size:.93rem;color:var(--ink-faint);margin:0 0 .8rem 0;line-height:1.4}\n.conv-result-card{background:rgba(46,107,122,.04);border:1px solid rgba(46,107,122,.18);border-left:3px solid var(--teal);border-radius:0 4px 4px 0;padding:.75rem 1.1rem;margin-top:.8rem}\n.conv-result-label{font-family:\'DM Sans\',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.14em;color:var(--teal);margin-bottom:.3rem}\n.conv-result-value{font-family:\'Crimson Pro\',Georgia,serif;font-size:1.05rem;font-weight:400;color:var(--ink);line-height:1.55;word-break:break-word}\n.conv-error-card{background:rgba(184,92,56,.05);border:1px solid rgba(184,92,56,.2);border-left:3px solid var(--accent);border-radius:0 4px 4px 0;padding:.75rem 1.1rem;margin-top:.8rem}\n.conv-error-text{font-family:\'Crimson Pro\',Georgia,serif;font-size:1rem;color:var(--accent);font-style:italic;margin:0}\n.conv-nav-footer{display:flex;gap:.75rem;padding:1.4rem 0 .5rem 0;border-top:1px solid var(--rule);margin-top:2.5rem;flex-wrap:wrap}\n.conv-nav-btn{font-family:\'DM Sans\',sans-serif;font-size:.78rem;font-weight:700;text-transform:uppercase;letter-spacing:.09em;color:var(--ink);background:var(--parchment-2);border:1.5px solid var(--rule-strong);border-radius:3px;padding:.55rem 1.1rem;text-decoration:none;display:inline-flex;align-items:center;gap:.4rem;white-space:nowrap;cursor:pointer;box-shadow:2px 2px 0 rgba(26,22,18,.08);transition:all .18s cubic-bezier(.4,0,.2,1)}\n.conv-nav-btn:hover{background:var(--ink);color:var(--parchment);border-color:var(--ink);box-shadow:3px 3px 0 var(--accent);transform:translate(-1px,-1px);text-decoration:none}\n.conv-nav-btn.active{background:var(--parchment-3);color:var(--ink-muted);cursor:default;box-shadow:none}\n.conv-nav-btn.active:hover{transform:none;background:var(--parchment-3);color:var(--ink-muted);border-color:var(--rule-strong);box-shadow:none}\n.conv-caption{font-family:\'DM Sans\',sans-serif;font-size:.75rem;color:var(--ink-faint);line-height:1.55;margin-top:1rem}\n.conv-caption a{color:var(--accent)!important;text-decoration:underline!important;text-decoration-color:rgba(184,92,56,.35)!important}\n.conv-caption a:hover{text-decoration-color:var(--accent)!important}\n</style>'
st.markdown(CONV_CSS, unsafe_allow_html=True)

st.markdown('''
<div class="conv-masthead">
    <div class="conv-masthead-eyebrow">Numeral Converter</div>
    <div class="conv-masthead-title">Chinese Numerals</div>
    <div class="conv-masthead-desc">Bidirectional conversion between Arabic numerals and standard Simplified Chinese (Mandarin).</div>
</div>
''', unsafe_allow_html=True)

st.markdown('<div class="conv-section-label">Conversion Direction</div>', unsafe_allow_html=True)

direction = st.radio(
    "Conversion direction",
    ['Arabic → Chinese', 'Chinese → Arabic'],
    horizontal=True,
    label_visibility="collapsed",
    key='chinese_direction',
)

st.markdown('<div class="conv-section-label">Preset Examples</div>', unsafe_allow_html=True)

arabic_presets = [3, 10, 15, 36, 123, 325, 1008, 40030]
other_presets  = ['三', '十', '十五', '三十六', '一百二十三', '三百二十五', '一千零八', '四万零三十']

with st.container(border=True):
    st.markdown('<p class="conv-presets-sublabel">Click a value to load it</p>', unsafe_allow_html=True)
    cols = st.columns(4)
    if direction == 'Arabic → Chinese':
        for i, num in enumerate(arabic_presets):
            if cols[i % 4].button(str(num), key=f'p_a_{i}', use_container_width=True):
                st.session_state['arabic_input'] = str(num)
    else:
        for i, txt in enumerate(other_presets):
            if cols[i % 4].button(txt, key=f'p_b_{i}', use_container_width=True):
                st.session_state['chinese_input'] = txt

st.markdown('<div class="conv-section-label">Convert</div>', unsafe_allow_html=True)

if direction == 'Arabic → Chinese':
    st.markdown('''
    <div class="conv-input-card">
        <div class="conv-input-title">Enter an Arabic numeral</div>
        <div class="conv-input-hint">Type a whole number, or click a preset above.</div>
    </div>''', unsafe_allow_html=True)
    arabic_input = st.text_input('Enter an Arabic numeral', key='arabic_input', placeholder='e.g. 325', label_visibility="collapsed")
    if arabic_input:
        val = arabic_input.strip()
        if val.lstrip('-').isdigit():
            try:
                result = an2cn(int(val))
                st.markdown(f'''<div class="conv-result-card">
        <div class="conv-result-label">Chinese numeral</div>
        <div class="conv-result-value">{result}</div>
    </div>''', unsafe_allow_html=True)
            except Exception as e:
                st.markdown(f'<div class="conv-error-card"><p class="conv-error-text">{e}</p></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="conv-error-card"><p class="conv-error-text">Please enter a valid whole number.</p></div>', unsafe_allow_html=True)
else:
    st.markdown('''
    <div class="conv-input-card">
        <div class="conv-input-title">Enter a Chinese numeral</div>
        <div class="conv-input-hint">Simplified Chinese characters, e.g. 三百二十五.</div>
    </div>''', unsafe_allow_html=True)
    chinese_input = st.text_input('Enter a Chinese numeral', key='chinese_input', placeholder='e.g. 三百二十五', label_visibility="collapsed")
    if chinese_input:
        val = chinese_input.strip()
        if bool(val.strip()):
            try:
                result = str(cn2an(val))
                st.markdown(f'''<div class="conv-result-card">
        <div class="conv-result-label">Arabic numeral</div>
        <div class="conv-result-value">{result}</div>
    </div>''', unsafe_allow_html=True)
            except Exception as e:
                st.markdown(f'<div class="conv-error-card"><p class="conv-error-text">{e}</p></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="conv-error-card"><p class="conv-error-text">Invalid input — please check the format.</p></div>', unsafe_allow_html=True)

st.markdown('''
<div class="conv-caption">Uses the cn2an library. Financial numerals and historical forms discussed in the Linguistics section.</div>
''', unsafe_allow_html=True)

st.markdown('''
<div class="conv-nav-footer">
    <a class="conv-nav-btn active" href="/Chinese_Converter">Chinese Numerals Converter</a>
    <a class="conv-nav-btn" href="/Chinese_Linguistics">Chinese Linguistics →</a>
</div>
''', unsafe_allow_html=True)
home_nav()