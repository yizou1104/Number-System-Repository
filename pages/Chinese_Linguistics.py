import streamlit as st
from ui import apply_global_styles, LING_CSS, LING_WIDTH_CSS, language_nav, footer_nav

st.set_page_config(page_title="Chinese Numerals — Linguistics", layout="wide")
apply_global_styles()

st.markdown(LING_CSS, unsafe_allow_html=True)
st.markdown(LING_WIDTH_CSS, unsafe_allow_html=True)
language_nav("Chinese", "linguistics")

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

# ── NAVIGATION ──────────────────────────────────────────────
footer_nav("Chinese", "linguistics")
