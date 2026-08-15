import streamlit as st
from ui import apply_global_styles, home_nav, LING_CSS

st.set_page_config(page_title="Yoruba Numerals — Linguistics", layout="centered")
apply_global_styles()

st.markdown(LING_CSS, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# MASTHEAD
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="ling-masthead">
    <div class="ling-masthead-eyebrow">Linguistic Structure</div>
    <div class="ling-masthead-title">Yoruba Numerals</div>
    <div class="ling-tags">
        <span class="ling-tag">Vigesimal</span>
        <span class="ling-tag">Multiplicative</span>
        <span class="ling-tag">Additive</span>
        <span class="ling-tag">Subtractive</span>
        <span class="ling-tag">Tonal</span>
        <span class="ling-tag">Morphologically Invariant</span>
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
    <p>Yoruba is the only language in this repository that uses all three arithmetic operations — multiplication, addition, and subtraction — as grammatically productive strategies for forming numerals.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-props">
        <span class="ling-prop-key">Primary base</span>
        <span class="ling-prop-val"><strong>20 (vigesimal)</strong></span>
        <span class="ling-prop-key">System type</span>
        <span class="ling-prop-val">Mixed — Multiplicative + Additive + Subtractive</span>
        <span class="ling-prop-key">Subtractive</span>
        <span class="ling-prop-val">Productive — used for 15–19, 25–29, and odd decades (50, 70, 90)</span>
        <span class="ling-prop-key">Additive</span>
        <span class="ling-prop-val">Restricted — units 1–4 above vigesimal bases</span>
        <span class="ling-prop-key">Tone</span>
        <span class="ling-prop-val">Three-level tonal (High, Mid, Low) — phonemically contrastive</span>
        <span class="ling-prop-key">Gender / case</span>
        <span class="ling-prop-val">Absent — numerals are morphologically invariant</span>
        <span class="ling-prop-key">Zero</span>
        <span class="ling-prop-val">No indigenous zero term — modern mathematical contexts use loanforms</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 2 — DIGITS & BASES
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Digits &amp; Bases</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Basic Digits (1–10)</div>', unsafe_allow_html=True)

st.table({
    "Number": [1,2,3,4,5,6,7,8,9,10],
    "Form":   ["ọ̀kan","èjì","ẹ̀ta","ẹ̀rin","àrún","ẹ̀fà","èje","ẹ̀jọ","ẹ̀sán","ẹ̀wá"]
})

st.markdown("""
<div class="ling-info">
    <p>Yoruba is written in the Latin alphabet with tone diacritics. Tone distinctions on numerals are phonemically meaningful — changing the tone of a numeral can alter the word entirely. There are no indigenous numeral glyphs.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Vigesimal Bases</div>', unsafe_allow_html=True)

st.table({
    "Value":     ["20","30","40","60","80","100","200","400"],
    "Form":      ["ogún","ọgbọ̀n","ogójì","ọgọ́ta","ọgọ́rin","ọgọ́rùn-ún","igba","irinwo"],
    "Structure": ["Base unit","Lexicalized decade","2 × 20","3 × 20","4 × 20","5 × 20","10 × 20","20 × 20"]
})

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Odd Decades</div>
    <p>50, 70, and 90 are not formed additively but subtractively: 50 = àádọ́ta ("10 less than 60"), 70 = àádọ́rin ("10 less than 80"), 90 = àádọ́rùn-ún ("10 less than 100"). The prefix <em>àádọ́-</em> is a fossilized subtractive morpheme.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 3 — THREE ARITHMETIC OPERATIONS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Arithmetic Operations</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Multiplication, Addition, Subtraction</div>', unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title">Multiplicative Structure</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">Multiplier × <em>20</em> (or higher vigesimal base)</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Multiplicative examples</div>
    <div class="ling-ex-line"><span class="num">40</span><span class="word">ogójì</span><span class="gloss">2 × 20</span></div>
    <div class="ling-ex-line"><span class="num">60</span><span class="word">ọgọ́ta</span><span class="gloss">3 × 20</span></div>
    <div class="ling-ex-line"><span class="num">200</span><span class="word">igba</span><span class="gloss">10 × 20</span></div>
    <div class="ling-ex-line"><span class="num">400</span><span class="word">irinwo</span><span class="gloss">20 × 20</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Additive Structure</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Addition is restricted to units 1–4 appearing above a vigesimal base. The connector <em>lé / lá</em> links the unit to the base.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">Unit (1–4) + <em>lé / lá</em> + Base</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Additive examples (teens and 20s)</div>
    <div class="ling-ex-line"><span class="num">11</span><span class="word">ọ̀kanlá</span><span class="gloss">1 + 10</span></div>
    <div class="ling-ex-line"><span class="num">12</span><span class="word">èjìlá</span><span class="gloss">2 + 10</span></div>
    <div class="ling-ex-line"><span class="num">21</span><span class="word">ọ̀kan lé ogún</span><span class="gloss">1 + 20</span></div>
    <div class="ling-ex-line"><span class="num">22</span><span class="word">èjìlélógún</span><span class="gloss">2 + 20</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Subtractive Structure</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Subtractive Dominance</div>
    <p>Yoruba strongly prefers subtraction for 15–19 and 25–29. These are not alternative forms — subtraction is the grammatically primary strategy for these numbers.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[Subtracted quantity] + <em>dín</em> + Base</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Subtractive examples</div>
    <div class="ling-ex-line"><span class="num">15</span><span class="word">ẹ̀ẹ́dógún</span><span class="gloss">5 from 20</span></div>
    <div class="ling-ex-line"><span class="num">16</span><span class="word">ẹ̀rìndínlógún</span><span class="gloss">4 less than 20</span></div>
    <div class="ling-ex-line"><span class="num">19</span><span class="word">ọ̀kàndínlógún</span><span class="gloss">1 less than 20</span></div>
    <div class="ling-ex-line"><span class="num">50</span><span class="word">àádọ́ta</span><span class="gloss">10 less than 60</span></div>
    <div class="ling-ex-line"><span class="num">90</span><span class="word">àádọ́rùn-ún</span><span class="gloss">10 less than 100</span></div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 4 — CONNECTORS & SPECIAL FORMS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Connectors &amp; Special Forms</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Operators and Special Cases</div>', unsafe_allow_html=True)

st.table({
    "Element":  ["lé / lá","dín","àádọ́-"],
    "Function": ["Additive connector ('plus')","Subtractive marker ('less than')","Fossilized subtractive prefix (10 less than base)"]
})

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:.5rem">Lexicalization</div>
        <p>Some forms are historically compositional but now lexicalized: <em>ọgbọ̀n</em> (30) no longer transparently means "10 + 20." Lexicalization is most common in the lower decades.</p>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:.5rem">Modern Simplification</div>
        <p>In urban and commercial contexts, subtractive constructions are sometimes replaced with decimal-style counting. This is a contact-driven simplification, not grammatical change.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 5 — MORPHOLOGY
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Morphology</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Inflection &amp; Ordinals</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-props">
        <span class="ling-prop-key">Inflection</span>
        <span class="ling-prop-val">Absent — numerals are invariant lexical items</span>
        <span class="ling-prop-key">Gender</span>
        <span class="ling-prop-val">No grammatical gender</span>
        <span class="ling-prop-key">Case</span>
        <span class="ling-prop-val">No case marking</span>
        <span class="ling-prop-key">Agreement</span>
        <span class="ling-prop-val">No agreement morphology</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Ordinal Formation</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Ordinals are formed derivationally, not inflectionally — the ordinal prefix <em>è-/ẹ̀-</em> attaches to the cardinal root.</p>
    <div class="ling-morph-table" style="margin-top:.75rem">
        <div class="ling-morph-row">
            <span class="ling-morph-source">1st</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">àkọ́kọ́</span>
            <span class="ling-morph-gloss">suppletive</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">2nd</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">èkejì</span>
            <span class="ling-morph-gloss">è- + cardinal root</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">3rd</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">ẹ̀kẹta</span>
            <span class="ling-morph-gloss">ẹ̀- + cardinal root</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── NAVIGATION ──────────────────────────────────────────────
st.markdown('<div class="nav-row">', unsafe_allow_html=True)
st.page_link("pages/Yoruba_Converter.py", label="← Yoruba Converter")
st.page_link("Home.py", label="← Home")
st.markdown('</div>', unsafe_allow_html=True)