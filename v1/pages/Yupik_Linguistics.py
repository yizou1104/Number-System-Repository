import streamlit as st
from ui import apply_global_styles, home_nav
from ui import LING_CSS

st.set_page_config(page_title="Yup’ik Numerals — Linguistics", layout="centered")

apply_global_styles()
st.markdown(LING_CSS, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# MASTHEAD
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="ling-masthead">
    <div class="ling-masthead-eyebrow">Linguistic Structure</div>
    <div class="ling-masthead-title">Yup’ik Numerals</div>
    <div class="ling-tags">
        <span class="ling-tag">Vigesimal</span>
        <span class="ling-tag">Quinary Sub-base</span>
        <span class="ling-tag">Additive–Multiplicative</span>
        <span class="ling-tag">Polysynthetic</span>
        <span class="ling-tag">Eskimo–Aleut</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 1 — OVERVIEW
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">System Overview</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Structural Properties</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Key Fact</div>
    <p>Yup’ik numerals exhibit a hierarchical base system combining 5, 10, and 20, reflecting a body-based counting model integrated into a polysynthetic grammar.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-props">
        <span class="ling-prop-key">Primary base</span>
        <span class="ling-prop-val"><strong>20 (vigesimal)</strong></span>
        <span class="ling-prop-key">Sub-base</span>
        <span class="ling-prop-val">5 (quinary)</span>
        <span class="ling-prop-key">Intermediate base</span>
        <span class="ling-prop-val">10</span>
        <span class="ling-prop-key">System type</span>
        <span class="ling-prop-val">Additive–Multiplicative (hierarchical)</span>
        <span class="ling-prop-key">Subtractive</span>
        <span class="ling-prop-val">Absent</span>
        <span class="ling-prop-key">Morphology</span>
        <span class="ling-prop-val">Polysynthetic</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 2 — DIGITS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Digits &amp; Bases</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Basic Digits (1–10)</div>', unsafe_allow_html=True)

st.table({
    "Number": ["1","2","3","4","5","6","7","8","9","10"],
    "Form": [
        "atausiq","malruk","pingayun","cetaman","talliman",
        "talliman atausiq","talliman malruk","talliman pingayun",
        "talliman cetaman","qula"
    ]
})

st.markdown("""
<div class="ling-info">
    <p>Numbers 6–9 are constructed relative to 5, reflecting a quinary substructure based on one hand.</p>
</div>
""", unsafe_allow_html=True)

# ── Teens ─────────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.75rem">11–19 (Teens)</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">10 + (5 + unit)</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Examples</div>
    <div class="ling-ex-line"><span class="num">13</span><span class="word">qula pingayun</span></div>
    <div class="ling-ex-line"><span class="num">17</span><span class="word">qula talliman malruk</span></div>
</div>
""", unsafe_allow_html=True)

# ── Base 20 ───────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.75rem">Base Unit (20)</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>20 is expressed as <em>yuinaq</em> (“one person”), reflecting a full-body counting system (fingers + toes).</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 3 — STRUCTURE
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Compositional Rules</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">How Numbers Are Built</div>', unsafe_allow_html=True)

# ── Quinary ───────────────────────────────────────
st.markdown('<div class="ling-subsection-title">Quinary Layer</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">5 + unit</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Examples</div>
    <div class="ling-ex-line"><span class="num">6</span><span class="word">talliman atausiq</span></div>
    <div class="ling-ex-line"><span class="num">9</span><span class="word">talliman cetaman</span></div>
</div>
""", unsafe_allow_html=True)

# ── Decimal ───────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.75rem">Decimal Layer</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">10 + remainder</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Numbers above 10 are built additively, embedding the quinary structure inside the decimal layer.</p>
</div>
""", unsafe_allow_html=True)

# ── Vigesimal ─────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.75rem">Vigesimal Multiplication</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[Multiplier] × 20</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Examples</div>
    <div class="ling-ex-line"><span class="num">40</span><span class="word">malruk yuinaq</span></div>
    <div class="ling-ex-line"><span class="num">60</span><span class="word">pingayun yuinaq</span></div>
</div>
""", unsafe_allow_html=True)

# ── Full Structure ────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.75rem">Full Structural Composition</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">(20 × n) + (10 × m) + (5 + unit)</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Example</div>
    <div class="ling-ex-line"><span class="num">37</span><span class="word">yuinaq qula pingayun</span></div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 4 — WRITING
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Writing &amp; Special Forms</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Script &amp; Zero</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title">Writing System</div>
        <p>Yup’ik uses the Latin alphabet in standardized orthography.</p>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title">Numeral Representation</div>
        <p>No indigenous numeral glyph system; Arabic numerals used in modern contexts.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p><strong>Zero</strong> is not part of traditional Yup’ik numeration and is a modern borrowed concept.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 5 — MORPHOLOGY
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Syntax &amp; Morphology</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Grammatical Integration</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title">Polysynthesis</div>
        <p>Numerals can be incorporated into larger morphological words rather than appearing independently.</p>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title">Dual Interaction</div>
        <p>The numeral “2” aligns structurally with the grammatical dual category.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-subsection-title">Ordinal Formation</div>
    <p>Ordinals are derived via suffixation from cardinal stems.</p>
    <ul>
        <li>atausiq → ordinal form</li>
        <li>malruk → ordinal form</li>
        <li>pingayun → ordinal form</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-subsection-title">Morphological Behavior</div>
    <ul>
        <li>Numerals may take case suffixes</li>
        <li>Can participate in derivation</li>
        <li>May integrate into noun or verb structures</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# ── NAVIGATION ──────────────────────────────────────────────
st.markdown('<div class="nav-row">', unsafe_allow_html=True)
st.page_link("pages/Yupik_Converter.py", label="← Yupik Converter")
st.page_link("Home.py", label="← Home")
st.markdown('</div>', unsafe_allow_html=True)