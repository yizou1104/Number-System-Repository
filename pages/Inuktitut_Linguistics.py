import streamlit as st
from ui import apply_global_styles, home_nav

st.set_page_config(page_title="Inuktitut Numerals — Linguistics", layout="centered")

apply_global_styles()

# ──────────────────────────────────────────────────────────────
# CSS (same as baseline — reused)
# ──────────────────────────────────────────────────────────────
from pages.Basque_Linguistics import LING_CSS  # reuse exact stylesheet
st.markdown(LING_CSS, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# PAGE MASTHEAD
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="ling-masthead">
    <div class="ling-masthead-eyebrow">Linguistic Structure</div>
    <div class="ling-masthead-title">Inuktitut Numerals</div>
    <div class="ling-tags">
        <span class="ling-tag">Vigesimal</span>
        <span class="ling-tag">Body-Based</span>
        <span class="ling-tag">Additive–Multiplicative</span>
        <span class="ling-tag">Polysynthetic</span>
        <span class="ling-tag">Eskimo–Aleut</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 1 — SYSTEM OVERVIEW
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">System Overview</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Structural Properties</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Key Fact</div>
    <p>Inuktitut numerals are grounded in a body-based counting system, where 20 represents a complete human (hands + feet), forming the basis of a fully vigesimal structure.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-props">
        <span class="ling-prop-key">Primary base</span>
        <span class="ling-prop-val"><strong>20 (vigesimal)</strong></span>
        <span class="ling-prop-key">Sub-base</span>
        <span class="ling-prop-val">5 (hand-based grouping)</span>
        <span class="ling-prop-key">System type</span>
        <span class="ling-prop-val">Multiplicative–Additive</span>
        <span class="ling-prop-key">Subtractive</span>
        <span class="ling-prop-val">Absent</span>
        <span class="ling-prop-key">Morphology</span>
        <span class="ling-prop-val">Polysynthetic integration</span>
        <span class="ling-prop-key">Scripts</span>
        <span class="ling-prop-val">Syllabics + Latin</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 2 — BASIC DIGITS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Digits &amp; Bases</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Basic Digits (1–10)</div>', unsafe_allow_html=True)

st.table({
    "Number": ["1","2","3","4","5","6","7","8","9","10"],
    "Form": ["ᐊᑕᐅᓯᖅ","ᒪᕐᕉᒃ","ᐱᖓᓱᑦ","ᓯᑕᒪᑦ","ᑕᓪᓕᒪᑦ",
             "ᐊᕐᕕᓂᓕᒃ","ᐊᕐᕕᓂᓕᒃ ᒪᕐᕉᒃ","ᐊᕐᕕᓂᓕᒃ ᐱᖓᓱᑦ",
             "ᐊᕐᕕᓂᓕᒃ ᓯᑕᒪᑦ","ᖁᓕᑦ"]
})

st.markdown("""
<div class="ling-info">
    <p>Numbers 6–9 are transparently formed as additions to 5, reflecting a sub-base built on counting one hand.</p>
</div>
""", unsafe_allow_html=True)

# ── Teens ────────────────────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.75rem">11–19 (Teens)</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule"><em>10</em> + unit</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Examples</div>
    <div class="ling-ex-line"><span class="num">11</span><span class="word">ᖁᓕᑦ ᐊᑕᐅᓯᖅ</span></div>
    <div class="ling-ex-line"><span class="num">13</span><span class="word">ᖁᓕᑦ ᐱᖓᓱᑦ</span></div>
    <div class="ling-ex-line"><span class="num">17</span><span class="word">ᖁᓕᑦ ᐊᕐᕕᓂᓕᒃ ᒪᕐᕉᒃ</span></div>
</div>
""", unsafe_allow_html=True)

# ── Base 20 ──────────────────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.75rem">Base Unit (20)</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>20 corresponds to a complete human body (10 fingers + 10 toes). This conceptual mapping drives the entire vigesimal system.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 3 — COMPOSITIONAL RULES
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Compositional Rules</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">How Numbers Are Built</div>', unsafe_allow_html=True)

# ── Base-5 Construction ──────────────────────────────────────
st.markdown('<div class="ling-subsection-title">Sub-base (5) Construction</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">5 + unit</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Examples</div>
    <div class="ling-ex-line"><span class="num">6</span><span class="word">5 + 1</span></div>
    <div class="ling-ex-line"><span class="num">7</span><span class="word">5 + 2</span></div>
    <div class="ling-ex-line"><span class="num">9</span><span class="word">5 + 4</span></div>
</div>
""", unsafe_allow_html=True)

# ── Vigesimal Multiplication ─────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.75rem">Vigesimal Multiplication</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[Multiplier] × 20</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Multiples of 20 correspond conceptually to multiple “persons,” reflecting the body-based counting origin.</p>
</div>
""", unsafe_allow_html=True)

# ── Additive Above 20 ────────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.75rem">Additive Structure Above 20</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[Multiple of 20] + remainder</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Examples</div>
    <div class="ling-ex-line"><span class="num">21</span><span class="word">20 + 1</span></div>
    <div class="ling-ex-line"><span class="num">37</span><span class="word">20 + 17</span></div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 4 — SPECIAL FORMS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Writing &amp; Special Forms</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Scripts &amp; Zero</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;">Syllabics</div>
        <p>Primary writing system in Nunavut. Uses a syllabic script distinct from alphabetic systems.</p>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;">Latin Alphabet</div>
        <p>Used in other regions (Nunavik, Labrador). Coexists with syllabics.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p><strong>Zero</strong> is not indigenous to traditional Inuktitut counting. It is a modern mathematical concept introduced through external systems.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 5 — SYNTAX & MORPHOLOGY
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Syntax &amp; Morphology</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Grammatical Integration</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;">Polysynthesis</div>
        <p>Numerals may integrate into complex words through morphological incorporation, rather than appearing as isolated tokens.</p>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;">Dual Category</div>
        <p>The numeral “2” aligns structurally with a grammatical dual system present in the language.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-subsection-title" style="font-size:1.05rem;">Morphological Behavior</div>
    <ul>
        <li>Numerals may take suffixes</li>
        <li>Case marking can apply depending on syntactic role</li>
        <li>Integration into noun structures is common</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# NAVIGATION
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="ling-nav-footer">
    <a class="ling-nav-btn" href="/Inuktitut_Converter">← Inuktitut Converter</a>
    <a class="ling-nav-btn active" href="/Inuktitut_Linguistics">Inuktitut Linguistics</a>
</div>
""", unsafe_allow_html=True)

home_nav()