import streamlit as st
from ui import apply_global_styles, home_nav
from pages.Basque_Linguistics import LING_CSS

st.set_page_config(page_title="Quechua Numerals — Linguistics", layout="centered")

apply_global_styles()
st.markdown(LING_CSS, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# MASTHEAD
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="ling-masthead">
    <div class="ling-masthead-eyebrow">Linguistic Structure</div>
    <div class="ling-masthead-title">Quechua Numerals</div>
    <div class="ling-tags">
        <span class="ling-tag">Decimal</span>
        <span class="ling-tag">Multiplicative–Additive</span>
        <span class="ling-tag">Agglutinative</span>
        <span class="ling-tag">Suffix-Based</span>
        <span class="ling-tag">Quechuan</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# OVERVIEW
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">System Overview</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Structural Properties</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Key Fact</div>
    <p>Quechua numerals form a fully regular decimal system where addition is expressed through possessive suffixes rather than simple concatenation.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-props">
        <span class="ling-prop-key">Base</span>
        <span class="ling-prop-val"><strong>10 (decimal)</strong></span>
        <span class="ling-prop-key">System type</span>
        <span class="ling-prop-val">Multiplicative–Additive</span>
        <span class="ling-prop-key">Additive marking</span>
        <span class="ling-prop-val">Suffix (-yuq / -niyuq)</span>
        <span class="ling-prop-key">Subtractive</span>
        <span class="ling-prop-val">Absent</span>
        <span class="ling-prop-key">Morphology</span>
        <span class="ling-prop-val">Agglutinative</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# DIGITS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Digits &amp; Bases</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Basic Digits (1–10)</div>', unsafe_allow_html=True)

st.table({
    "Number": ["0","1","2","3","4","5","6","7","8","9","10"],
    "Form": [
        "cero","huk","iskay","kimsa","tawa","pichqa",
        "soqta","qanchis","pusaq","isqun","chunka"
    ]
})

st.markdown("""
<div class="ling-info">
    <p>Zero (<em>cero</em>) is a Spanish loan; there is no indigenous pre-contact term.</p>
</div>
""", unsafe_allow_html=True)

# ── Teens ─────────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.75rem">11–19 (Additive with Suffix)</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">10 + unit + -yuq / -niyuq</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Examples</div>
    <div class="ling-ex-line"><span class="num">11</span><span class="word">chunka hukniyuq</span></div>
    <div class="ling-ex-line"><span class="num">15</span><span class="word">chunka pichqayuq</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>The suffix <strong>-yuq / -niyuq</strong> encodes possession: “having X more”.</p>
</div>
""", unsafe_allow_html=True)

# ── Bases ─────────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.75rem">Core Bases</div>', unsafe_allow_html=True)

st.table({
    "Value": ["10","100","1,000","10,000","1,000,000"],
    "Form": ["chunka","pachak","waranqa","chunka waranqa","hunu"],
    "Structure": ["Base","Base","Base","10 × 1000","Traditional large unit"]
})

# ══════════════════════════════════════════════════════════════
# STRUCTURE
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Compositional Rules</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">How Numbers Are Built</div>', unsafe_allow_html=True)

# ── Multiplicative ─────────────────────────────────
st.markdown('<div class="ling-subsection-title">Multiplicative Structure</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[Digit] × Base</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Examples</div>
    <div class="ling-ex-line"><span class="num">20</span><span class="word">iskay chunka</span></div>
    <div class="ling-ex-line"><span class="num">300</span><span class="word">kimsa pachak</span></div>
</div>
""", unsafe_allow_html=True)

# ── Additive ───────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.75rem">Additive Structure</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[Tens] + [Unit + -yuq]</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Example</div>
    <div class="ling-ex-line"><span class="num">25</span><span class="word">iskay chunka pichqayuq</span></div>
</div>
""", unsafe_allow_html=True)

# ── Hierarchy ──────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.75rem">Hierarchical Composition</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">1000 + 100 + 10 + unit</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Example</div>
    <div class="ling-ex-line"><span class="num">256</span><span class="word">iskay pachak pichqa chunka soqta</span></div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# WRITING
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Writing &amp; Zero</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Script</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title">Writing System</div>
        <p>Latin alphabet (standard Quechua orthography).</p>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title">Numerals</div>
        <p>No indigenous numeral glyph system; Arabic numerals used.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SYNTAX
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Syntax</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Usage in Sentences</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <ul>
        <li>Numeral precedes noun: <em>kimsa wasi</em> (three houses)</li>
        <li>Plural often omitted after numerals</li>
        <li>Case marking attaches to noun phrase: <em>kimsa wasipi</em></li>
    </ul>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# MORPHOLOGY
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Morphology</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Suffix Systems</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-subsection-title">Additive Suffix</div>
    <p><strong>-yuq / -niyuq</strong> expresses addition via possession.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-subsection-title">Ordinal Formation</div>
    <p>[Cardinal] + <strong>-ñiqin</strong></p>
    <ul>
        <li>iskay ñiqin (second)</li>
        <li>kimsa ñiqin (third)</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# NAVIGATION
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="ling-nav-footer">
    <a class="ling-nav-btn" href="/Quechua_Converter">← Quechua Converter</a>
    <a class="ling-nav-btn active" href="/Quechua_Linguistics">Quechua Linguistics</a>
</div>
""", unsafe_allow_html=True)

home_nav()