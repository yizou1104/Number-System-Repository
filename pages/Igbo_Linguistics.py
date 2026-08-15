import streamlit as st
from ui import apply_global_styles, LING_CSS, LING_WIDTH_CSS, language_nav, footer_nav

st.set_page_config(page_title="Igbo Numerals — Linguistics", layout="wide")
apply_global_styles()

st.markdown(LING_CSS, unsafe_allow_html=True)
st.markdown(LING_WIDTH_CSS, unsafe_allow_html=True)
language_nav("Igbo", "linguistics")

# ══════════════════════════════════════════════════════════════
# MASTHEAD
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="ling-masthead">
    <div class="ling-masthead-eyebrow">Linguistic Structure</div>
    <div class="ling-masthead-title">Igbo Numerals</div>
    <div class="ling-tags">
        <span class="ling-tag">Decimal (Modern)</span>
        <span class="ling-tag">Historically Vigesimal</span>
        <span class="ling-tag">Multiplicative–Additive</span>
        <span class="ling-tag">Morphologically Invariant</span>
        <span class="ling-tag">Dual System</span>
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
    <div class="ling-callout-label">Dual System</div>
    <p>Igbo contains two coexisting numeral systems: a modern decimal system used in education and commerce, and an older traditional vigesimal system with roots in the base-20 ọgụ structure still encountered in cultural and regional contexts.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-props">
        <span class="ling-prop-key">Modern base</span>
        <span class="ling-prop-val"><strong>10 (decimal)</strong></span>
        <span class="ling-prop-key">Traditional base</span>
        <span class="ling-prop-val">20 (vigesimal) — <em>ọgụ</em> = 20</span>
        <span class="ling-prop-key">System type</span>
        <span class="ling-prop-val">Multiplicative–Additive (modern); historically subtractive in vigesimal forms</span>
        <span class="ling-prop-key">Additive connector</span>
        <span class="ling-prop-val"><em>na</em> — links tens and units in compound numbers</span>
        <span class="ling-prop-key">Inflection</span>
        <span class="ling-prop-val">Absent — numerals are invariant lexical items</span>
        <span class="ling-prop-key">Zero</span>
        <span class="ling-prop-val">Multiple variant spoken forms: <em>efu, oruoghoro, ncha, adịgị, okpokoro</em></span>
        <span class="ling-prop-key">Script</span>
        <span class="ling-prop-val">Latin alphabet with diacritics for tone and vowel quality</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 2 — DIGITS & BASES
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Digits &amp; Bases</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Basic Digits (0–10)</div>', unsafe_allow_html=True)

st.table({
    "Number": ["0","1","2","3","4","5","6","7","8","9","10"],
    "Form":   ["efu / oruoghoro / ncha","otu","abụọ","atọ","anọ","ise",
               "isii","asaa","asatọ","itoolu / iteghète","iri"]
})

st.markdown("""
<div class="ling-info">
    <p>Zero has no single standardized form in Igbo. The existence of multiple spoken variants (<em>efu, oruoghoro, ncha, adịgị, okpokoro</em>) reflects regional dialectal diversity rather than systematic alternation. Different dialects also show variation in the form for 9.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Modern Decimal Bases</div>', unsafe_allow_html=True)

st.table({
    "Value":     ["10","20","30","100","1,000","1,000,000"],
    "Form":      ["iri","iri abụọ","iri atọ","otu narị","otu puku","otu nde"],
    "Structure": ["Base unit","2 × 10","3 × 10","1 × 100","1 × 1,000","1 × 1,000,000"]
})

# ══════════════════════════════════════════════════════════════
# SECTION 3 — COMPOSITIONAL RULES
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Compositional Rules</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">How Numbers Are Built</div>', unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title">Modern Decimal — Multiplicative</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">Digit × <em>iri</em> (tens) · Digit × <em>narị / puku / nde</em> (higher)</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Multiplicative examples</div>
    <div class="ling-ex-line"><span class="num">20</span><span class="word">iri abụọ</span><span class="gloss">2 × 10</span></div>
    <div class="ling-ex-line"><span class="num">40</span><span class="word">iri anọ</span><span class="gloss">4 × 10</span></div>
    <div class="ling-ex-line"><span class="num">100</span><span class="word">otu narị</span><span class="gloss">1 × 100</span></div>
    <div class="ling-ex-line"><span class="num">1,000,000</span><span class="word">otu nde</span><span class="gloss">1 × 1,000,000</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Modern Decimal — Additive</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[Tens base] + <em>na</em> + [Unit]</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Additive examples</div>
    <div class="ling-ex-line"><span class="num">11</span><span class="word">iri na otu</span><span class="gloss">10 + 1</span></div>
    <div class="ling-ex-line"><span class="num">12</span><span class="word">iri na abụọ</span><span class="gloss">10 + 2</span></div>
    <div class="ling-ex-line"><span class="num">25</span><span class="word">iri abụọ na ise</span><span class="gloss">20 + 5</span></div>
    <div class="ling-ex-line"><span class="num">47</span><span class="word">iri anọ na asaa</span><span class="gloss">40 + 7</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>The conjunction <em>na</em> always immediately precedes the unit element. It does not vary for phonological environment and is obligatory in compound numbers — omission is ungrammatical in standard modern Igbo.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Traditional Vigesimal System</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>The traditional system uses <em>ọgụ</em> (20) as its base. Some older forms express numbers relative to the next vigesimal pivot using subtraction — a pattern no longer productive in modern educational usage but present in oral tradition and regional speech.</p>
    <div class="ling-examples" style="margin-top:.75rem;margin-bottom:0">
        <div class="ling-examples-label">Traditional base</div>
        <div class="ling-ex-line"><span class="word">ọgụ = 20</span><span class="gloss">vigesimal base unit</span></div>
        <div class="ling-ex-line"><span class="word">ọgụ abụọ = 40</span><span class="gloss">2 × 20</span></div>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 4 — MORPHOLOGY
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Morphology</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Inflection &amp; Ordinals</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:.5rem">Cardinals</div>
        <ul>
            <li>Invariant — no inflection of any kind</li>
            <li>No gender, case, or number marking</li>
            <li>No agreement morphology</li>
            <li>Numerals function as uninflected lexical items</li>
        </ul>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:.5rem">Ordinals</div>
        <p>Ordinals are formed analytically with the prefix <em>nke</em> followed by the cardinal.</p>
        <div class="ling-morph-table" style="margin-top:.65rem">
            <div class="ling-morph-row">
                <span class="ling-morph-source">1st</span>
                <span class="ling-morph-arrow">→</span>
                <span class="ling-morph-target">nke mbụ</span>
                <span class="ling-morph-gloss">or nke izizi</span>
            </div>
            <div class="ling-morph-row">
                <span class="ling-morph-source">2nd</span>
                <span class="ling-morph-arrow">→</span>
                <span class="ling-morph-target">nke abụọ</span>
                <span class="ling-morph-gloss">nke + cardinal</span>
            </div>
            <div class="ling-morph-row">
                <span class="ling-morph-source">3rd</span>
                <span class="ling-morph-arrow">→</span>
                <span class="ling-morph-target">nke atọ</span>
                <span class="ling-morph-gloss">nke + cardinal</span>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── NAVIGATION ──────────────────────────────────────────────
footer_nav("Igbo", "linguistics")
