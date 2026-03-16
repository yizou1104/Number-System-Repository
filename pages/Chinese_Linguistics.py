import streamlit as st
from ui import apply_global_styles, home_nav

st.set_page_config(page_title="Chinese Numerals — Linguistics", layout="centered")
apply_global_styles()

LING_CSS = """<style>
.ling-masthead{border-top:3px solid var(--ink);border-bottom:1px solid var(--rule);padding:1.75rem 0 1.4rem 0;margin-bottom:1.75rem}
.ling-masthead-eyebrow{font-family:'DM Sans',sans-serif;font-size:.68rem;font-weight:700;text-transform:uppercase;letter-spacing:.18em;color:var(--accent);display:flex;align-items:center;gap:.65rem;margin-bottom:.65rem}
.ling-masthead-eyebrow::before{content:'';display:inline-block;width:1.75rem;height:1.5px;background:var(--accent);flex-shrink:0}
.ling-masthead-title{font-family:'Crimson Pro',Georgia,serif;font-size:3rem;font-weight:700;color:var(--ink);letter-spacing:-.04em;line-height:1.05;margin-bottom:.9rem}
.ling-masthead-sub{display:none}
.ling-tags{display:flex;flex-wrap:wrap;gap:.45rem}
.ling-tag{font-family:'DM Sans',sans-serif;font-size:.68rem;font-weight:600;letter-spacing:.07em;text-transform:uppercase;padding:.22rem .7rem;border:1.5px solid var(--rule-strong);border-radius:2px;color:var(--ink-soft);background:transparent}
.ling-section-label{font-family:'DM Sans',sans-serif;font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.16em;color:var(--ink-soft);display:flex;align-items:center;gap:1rem;margin:2.25rem 0 1.1rem 0}
.ling-section-label::before{content:'';display:inline-block;width:2rem;height:1px;background:var(--ink-muted);flex-shrink:0}
.ling-section-label::after{content:'';flex:1;height:1px;background:var(--rule)}
.ling-section-title{font-family:'Crimson Pro',Georgia,serif;font-size:1.85rem;font-weight:600;color:var(--ink);letter-spacing:-.025em;line-height:1.15;margin-bottom:1.1rem;padding-bottom:.45rem;border-bottom:1px solid var(--rule)}
.ling-subsection-title{font-family:'Crimson Pro',Georgia,serif;font-size:1.25rem;font-weight:600;color:var(--ink-soft);letter-spacing:-.01em;margin-bottom:.7rem;margin-top:0}
.ling-card{background:var(--card-bg);border:1px solid var(--card-border);border-radius:5px;padding:1.3rem 1.55rem;margin-bottom:.85rem;box-shadow:0 1px 3px rgba(26,22,18,.05),0 3px 10px rgba(26,22,18,.04),inset 0 1px 0 rgba(255,255,255,.65);transition:transform .22s cubic-bezier(.4,0,.2,1),box-shadow .22s cubic-bezier(.4,0,.2,1),border-color .22s ease}
.ling-card:hover{transform:translateY(-2px);box-shadow:0 2px 6px rgba(26,22,18,.07),0 8px 24px rgba(26,22,18,.09),inset 0 1px 0 rgba(255,255,255,.8);border-color:rgba(26,22,18,.16)}
.ling-card p,.ling-card li{font-family:'Crimson Pro',Georgia,serif;font-size:1.08rem;color:var(--ink-soft);line-height:1.72;margin-bottom:.45rem}
.ling-card p:last-child,.ling-card li:last-child{margin-bottom:0}
.ling-card ul{padding-left:1.3rem;margin:0}
.ling-card li::marker{color:var(--accent)}
.ling-callout{background:var(--accent-pale);border:1px solid rgba(184,92,56,.2);border-left:3px solid var(--accent);border-radius:4px;padding:1.05rem 1.45rem;margin-bottom:.85rem;transition:transform .2s ease,box-shadow .2s ease}
.ling-callout:hover{transform:translateY(-1px);box-shadow:0 4px 16px rgba(184,92,56,.1)}
.ling-callout-label{font-family:'DM Sans',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.14em;color:var(--accent);margin-bottom:.4rem}
.ling-callout p{font-family:'Crimson Pro',Georgia,serif;font-size:1.1rem;font-style:italic;color:var(--ink);line-height:1.6;margin:0}
.ling-info{background:rgba(46,107,122,.05);border:1px solid rgba(46,107,122,.18);border-left:3px solid var(--teal);border-radius:4px;padding:.95rem 1.35rem;margin-bottom:.85rem}
.ling-info p{font-family:'Crimson Pro',Georgia,serif;font-size:1.05rem;color:var(--ink-soft);line-height:1.68;margin:0}
.ling-formula{background:var(--parchment-2);border:1px solid var(--rule-strong);border-radius:4px;padding:1.05rem 1.4rem;margin-bottom:.85rem;display:flex;align-items:flex-start;gap:1.2rem}
.ling-formula-label{font-family:'DM Sans',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.12em;color:var(--ink-faint);flex-shrink:0;padding-top:.2rem;min-width:3.5rem;text-align:right}
.ling-formula-rule{font-family:'DM Mono','Courier New',monospace;font-size:.98rem;color:var(--ink);line-height:1.6;flex:1}
.ling-formula-rule em{font-style:normal;color:var(--accent);font-weight:500}
.ling-examples{background:var(--parchment-2);border:1px solid var(--rule);border-left:3px solid var(--ink-faint);border-radius:4px;padding:.95rem 1.35rem;margin-bottom:.85rem}
.ling-examples-label{font-family:'DM Sans',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.13em;color:var(--ink-faint);margin-bottom:.5rem}
.ling-ex-line{font-family:'DM Mono','Courier New',monospace;font-size:.95rem;color:var(--ink-soft);line-height:1.75}
.ling-ex-line .num{color:var(--accent);font-weight:500;display:inline-block;min-width:2.5rem}
.ling-ex-line .word{color:var(--ink)}
.ling-ex-line .gloss{color:var(--ink-muted);font-style:italic;font-family:'Crimson Pro',Georgia,serif;font-size:.92rem;margin-left:.75rem}
.ling-grid-2{display:grid;grid-template-columns:1fr 1fr;gap:.75rem;margin-bottom:.85rem}
@media(max-width:600px){.ling-grid-2{grid-template-columns:1fr}}
.ling-props{display:grid;grid-template-columns:auto 1fr;gap:.5rem 1.25rem;align-items:baseline;margin:0;padding:0}
.ling-prop-key{font-family:'DM Sans',sans-serif;font-size:.68rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--ink-faint);white-space:nowrap}
.ling-prop-val{font-family:'Crimson Pro',Georgia,serif;font-size:1.05rem;color:var(--ink-soft);line-height:1.45}
.ling-prop-val strong{color:var(--ink);font-weight:600}
.ling-morph-table{margin-bottom:0}
.ling-morph-row{display:grid;grid-template-columns:6rem 1.5rem 6rem 1fr;align-items:center;gap:.5rem 1rem;padding:.45rem 0;border-bottom:1px solid var(--rule)}
.ling-morph-row:last-child{border-bottom:none}
.ling-morph-source{font-family:'DM Mono','Courier New',monospace;font-size:.93rem;color:var(--ink)}
.ling-morph-arrow{color:var(--ink-faint);font-size:.85rem;text-align:center}
.ling-morph-target{font-family:'DM Mono','Courier New',monospace;font-size:.93rem;color:var(--accent);font-weight:500}
.ling-morph-gloss{font-family:'Crimson Pro',Georgia,serif;font-style:italic;font-size:.92rem;color:var(--ink-muted)}
.ling-nav-footer{display:flex;gap:.75rem;padding:1.4rem 0 .5rem 0;border-top:1px solid var(--rule);margin-top:2.5rem;flex-wrap:wrap}
.ling-nav-btn{font-family:'DM Sans',sans-serif;font-size:.78rem;font-weight:700;text-transform:uppercase;letter-spacing:.09em;color:var(--ink);background:var(--parchment-2);border:1.5px solid var(--rule-strong);border-radius:3px;padding:.55rem 1.1rem;text-decoration:none;display:inline-flex;align-items:center;gap:.4rem;white-space:nowrap;cursor:pointer;box-shadow:2px 2px 0 rgba(26,22,18,.08);transition:all .18s cubic-bezier(.4,0,.2,1)}
.ling-nav-btn:hover{background:var(--ink);color:var(--parchment);border-color:var(--ink);box-shadow:3px 3px 0 var(--accent);transform:translate(-1px,-1px);text-decoration:none}
.ling-nav-btn.active{background:var(--parchment-3);color:var(--ink-muted);cursor:default;box-shadow:none}
.ling-nav-btn.active:hover{transform:none;background:var(--parchment-3);color:var(--ink-muted);border-color:var(--rule-strong);box-shadow:none}
</style>"""
st.markdown(LING_CSS, unsafe_allow_html=True)

st.markdown("""
<div class="ling-masthead">
    <div class="ling-masthead-eyebrow">Linguistic Structure</div>
    <div class="ling-masthead-title">Chinese Numerals</div>
    <div class="ling-tags">
        <span class="ling-tag">Decimal</span>
        <span class="ling-tag">Fully Multiplicative</span>
        <span class="ling-tag">Compositional</span>
        <span class="ling-tag">Morphologically Invariant</span>
        <span class="ling-tag">10,000-Based Grouping</span>
        <span class="ling-tag">Financial Numeral System</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-section-label">System Overview</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Structural Properties</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Key Fact</div>
    <p>Chinese is the most structurally transparent numeral system in this repository — almost every number above 10 is composed by explicit, fully productive rules. Irregularity is minimal, and the system groups by ten-thousands (10⁴), not thousands.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-props">
        <span class="ling-prop-key">Primary base</span>
        <span class="ling-prop-val"><strong>10 (decimal)</strong></span>
        <span class="ling-prop-key">System type</span>
        <span class="ling-prop-val">Fully Multiplicative–Additive</span>
        <span class="ling-prop-key">Grouping pivot</span>
        <span class="ling-prop-val">10⁴ (万 wàn) — not 10³ as in Western systems</span>
        <span class="ling-prop-key">Higher pivot</span>
        <span class="ling-prop-val">10⁸ (亿 yì) — groups of ten-thousands above 万</span>
        <span class="ling-prop-key">Morphophonology</span>
        <span class="ling-prop-val">Invariant — numerals never inflect</span>
        <span class="ling-prop-key">Zero</span>
        <span class="ling-prop-val">零 (líng) — marks skipped place values, not stand-alone quantity</span>
        <span class="ling-prop-key">Script</span>
        <span class="ling-prop-val">Chinese characters (standard); separate financial numeral set for formal documents</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-section-label">Digits &amp; Bases</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Basic Digits (0–9)</div>', unsafe_allow_html=True)

st.table({
    "Number":    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    "Character": ["零","一","二","三","四","五","六","七","八","九"],
    "Pinyin":    ["líng","yī","èr","sān","sì","wǔ","liù","qī","bā","jiǔ"]
})

st.markdown("""
<div class="ling-info">
    <p>Each digit is a single morpheme that never inflects. Chinese, as a monosyllabic logographic language, does not exhibit morphological variation in numerals — the character and its reading are invariant across all contexts.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Base Morphemes</div>', unsafe_allow_html=True)

st.table({
    "Power":     ["10¹","10²","10³","10⁴","10⁸"],
    "Value":     ["10","100","1,000","10,000","100,000,000"],
    "Character": ["十","百","千","万","亿"],
    "Pinyin":    ["shí","bǎi","qiān","wàn","yì"]
})

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Ten-Thousand Grouping</div>
    <p>Unlike English (which groups by 10³), Chinese groups by 10⁴. The number 100,000 is 十万 (10 × 10,000), not "one hundred thousand." This means 10⁵–10⁷ are expressed within the 万 layer, and the next primary boundary is 10⁸ (亿).</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-section-label">Compositional Rules</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Multiplicative &amp; Additive Structure</div>', unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title">Multiplicative Rule</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Rule</span>
    <span class="ling-formula-rule">Digit always precedes base morpheme · [Digit] × [Base]</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Multiplicative examples</div>
    <div class="ling-ex-line"><span class="num">20</span><span class="word">二十</span><span class="gloss">2 × 10</span></div>
    <div class="ling-ex-line"><span class="num">300</span><span class="word">三百</span><span class="gloss">3 × 100</span></div>
    <div class="ling-ex-line"><span class="num">4,000</span><span class="word">四千</span><span class="gloss">4 × 1,000</span></div>
    <div class="ling-ex-line"><span class="num">50,000</span><span class="word">五万</span><span class="gloss">5 × 10,000</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Additive Rule</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Rule</span>
    <span class="ling-formula-rule">Multiply each component, then <em>add left-to-right</em> in descending magnitude order</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Compound examples</div>
    <div class="ling-ex-line"><span class="num">23</span><span class="word">二十三</span><span class="gloss">(2×10) + 3</span></div>
    <div class="ling-ex-line"><span class="num">456</span><span class="word">四百五十六</span><span class="gloss">(4×100) + (5×10) + 6</span></div>
    <div class="ling-ex-line"><span class="num">12,345</span><span class="word">一万二千三百四十五</span><span class="gloss">(1×10⁴) + (2×10³) + (3×10²) + (4×10) + 5</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>The digit 一 (yī, one) is typically omitted before 十 (shí, ten) when forming numbers in the teens and when 十 begins a numeral: <em>十 = 10</em>, <em>十一 = 11</em>, <em>十五 = 15</em>. This is the main irregular feature of the otherwise fully regular system.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-section-label">Zero &amp; Special Cases</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">零 (líng) — Structural Zero</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Grammatical Role of Zero</div>
    <p>In Chinese, 零 does not represent quantity in isolation — it marks a <em>skipped place value</em> between two expressed digits. This is a grammatical placeholder rule, not just a numeric symbol.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Three constraints govern the use of 零:</p>
    <ul>
        <li>零 never appears twice consecutively</li>
        <li>零 never appears at the end of a numeral</li>
        <li>零 only appears when a lower non-zero place value follows</li>
    </ul>
    <div class="ling-examples" style="margin-top:.75rem;margin-bottom:0">
        <div class="ling-examples-label">Zero usage examples</div>
        <div class="ling-ex-line"><span class="num">103</span><span class="word">一百零三</span><span class="gloss">hundreds + zero-marker + units</span></div>
        <div class="ling-ex-line"><span class="num">1,020</span><span class="word">一千零二十</span><span class="gloss">hundreds skipped → zero-marker</span></div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-section-label">Financial Numerals</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Formal Financial Characters</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Because standard numeral characters have few strokes, they are vulnerable to fraudulent alteration in legal and financial documents. A parallel set of complex characters — the financial numerals — is used in formal contexts.</p>
</div>
""", unsafe_allow_html=True)

st.table({
    "Standard":  ["一","二","三","十","百","千"],
    "Financial": ["壹","贰","叁","拾","佰","仟"],
    "Pinyin":    ["yī","èr","sān","shí","bǎi","qiān"]
})

st.markdown("""
<div class="ling-info">
    <p>Financial numerals are <strong>context-restricted</strong> — they appear exclusively in legal documents, cheques, and formal financial instruments. They do not replace standard numerals in everyday, educational, or literary usage.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-nav-footer">
    <a class="ling-nav-btn" href="/Chinese_Converter">← Chinese Converter</a>
    <a class="ling-nav-btn active" href="/Chinese_Linguistics">Chinese Linguistics</a>
</div>
""", unsafe_allow_html=True)
home_nav()