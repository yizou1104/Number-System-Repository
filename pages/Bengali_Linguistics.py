import streamlit as st
from ui import apply_global_styles, LING_CSS, LING_WIDTH_CSS, language_nav, footer_nav

st.set_page_config(page_title="Bengali Numerals — Linguistics", layout="wide")

apply_global_styles()

# ─────────────────────────────────────────────────────────────
# SHARED LINGUISTICS STYLESHEET
# ─────────────────────────────────────────────────────────────
st.markdown(LING_CSS, unsafe_allow_html=True)
st.markdown(LING_WIDTH_CSS, unsafe_allow_html=True)
language_nav("Bengali", "linguistics")

# ══════════════════════════════════════════════════════════════
# MASTHEAD
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="ling-masthead">
    <div class="ling-masthead-eyebrow">Linguistic Structure</div>
    <div class="ling-masthead-title">Bengali Numerals</div>
    <div class="ling-tags">
        <span class="ling-tag">Decimal</span>
        <span class="ling-tag">Lexicalized 1–99</span>
        <span class="ling-tag">Multiplicative–Additive</span>
        <span class="ling-tag">Non-Subtractive</span>
        <span class="ling-tag">Classifier System</span>
        <span class="ling-tag">Gender-Neutral</span>
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
    <p>Bengali shares the lexicalized 1–99 structure of Hindi, but is distinguished by its active classifier system — numerals typically co-occur with a classifier morpheme that fuses with the numeral in rapid speech.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-props">
        <span class="ling-prop-key">Primary base</span>
        <span class="ling-prop-val"><strong>10 (decimal)</strong></span>
        <span class="ling-prop-key">1–99 structure</span>
        <span class="ling-prop-val">Lexicalized with morphophonological alternations</span>
        <span class="ling-prop-key">100+ structure</span>
        <span class="ling-prop-val">Multiplicative–Additive (regular)</span>
        <span class="ling-prop-key">Large-number pivot</span>
        <span class="ling-prop-val">10⁵ (lakh system) — Indian grouping: 3-2-2-2</span>
        <span class="ling-prop-key">Subtractive</span>
        <span class="ling-prop-val">Historically present; not productive in modern Bengali</span>
        <span class="ling-prop-key">Gender marking</span>
        <span class="ling-prop-val">Absent — Bengali lacks grammatical gender</span>
        <span class="ling-prop-key">Script</span>
        <span class="ling-prop-val">Bengali script glyphs (০ – ৯); Arabic numerals common in modern use</span>
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
    "Glyph":  ["০","১","২","৩","৪","৫","৬","৭","৮","৯","১০"],
    "Form":   ["শূন্য","এক","দুই","তিন","চার","পাঁচ","ছয়","সাত","আট","নয়","দশ"]
})

st.markdown("""
<div class="ling-info">
    <p>Bengali uses its own script glyphs, though Arabic digits are standard in modern printed and digital contexts. <em>শূন্য</em> (zero) is a Sanskrit loanword meaning "empty".</p>
</div>
""", unsafe_allow_html=True)

# ── Teens ──────────────────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">11–19 (Teens)</div>', unsafe_allow_html=True)

st.table({
    "Number": ["11","12","13","14","15","16","17","18","19"],
    "Form":   ["এগারো","বারো","তেরো","চোদ্দো","পনেরো","ষোলো","সতেরো","আঠারো","উনিশ"]
})

st.markdown("""
<div class="ling-card">
    <p>Teens are lexicalized. <em>উনিশ</em> (19) historically derives from "one less than twenty" — a vestige of a once-productive subtractive pattern that is no longer active in modern Bengali.</p>
</div>
""", unsafe_allow_html=True)

# ── Tens ────────────────────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Tens</div>', unsafe_allow_html=True)

st.table({
    "Value": ["20","30","40","50","60","70","80","90"],
    "Form":  ["বিশ","ত্রিশ","চল্লিশ","পঞ্চাশ","ষাট","সত্তর","আশি","নব্বই"]
})

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Internal Patterns in 1–99</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Numbers from 1–99 show characteristic morphophonological alternations that are historically derived but not synchronically productive.</p>
    <ul>
        <li>Consonant gemination</li>
        <li>Nasalization</li>
        <li><em>উন-</em> prefix in certain sub-decade positions</li>
        <li>Internal vowel alternations</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Selected compounds</div>
    <div class="ling-ex-line"><span class="num">21</span><span class="word">একুশ</span><span class="gloss">internal alternation</span></div>
    <div class="ling-ex-line"><span class="num">24</span><span class="word">চব্বিশ</span><span class="gloss">consonant gemination</span></div>
    <div class="ling-ex-line"><span class="num">25</span><span class="word">পঁচিশ</span><span class="gloss">nasalization</span></div>
    <div class="ling-ex-line"><span class="num">29</span><span class="word">উনত্রিশ</span><span class="gloss">উন- prefix form</span></div>
</div>
""", unsafe_allow_html=True)

# ── Higher Bases ─────────────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Hundreds and Higher</div>', unsafe_allow_html=True)

st.table({
    "Value":     ["100","1,000","1,00,000","1,00,00,000"],
    "Form":      ["একশো / শত","হাজার","লাখ","কোটি"],
    "Structure": ["Hundred unit","Thousand unit","10⁵ pivot","10⁷ pivot"]
})

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[Digit] + <em>Base unit</em> + [Lower components] · descending magnitude order</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Compound Examples</div>
    <div class="ling-ex-line"><span class="num">125</span><span class="word">একশো পঁচিশ</span></div>
    <div class="ling-ex-line"><span class="num">300</span><span class="word">তিনশো</span></div>
    <div class="ling-ex-line"><span class="num">5,432</span><span class="word">পাঁচ হাজার চারশো বত্রিশ</span></div>
    <div class="ling-ex-line"><span class="num">1,23,45,678</span><span class="word">১ কোটি ২৩ লাখ ৪৫ হাজার ৬৭৮</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Indian Digit Grouping</div>
    <p>Bengali uses the same 3-2-2-2 grouping system as Hindi — one lakh is 1,00,000, not 100,000. No internal conjunction is used between magnitude components.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 3 — CLASSIFIER SYSTEM
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Classifier System</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Numeral Classifiers</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Distinctive Feature</div>
    <p>Bengali commonly employs classifier morphemes between numerals and nouns. This distinguishes Bengali from Hindi and most other Indo-Aryan languages in the project.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>The classifier <em>-টা</em> (informal) or <em>-টি</em> (formal) is the most common general-purpose classifier, used with inanimate and countable objects.</p>
    <div class="ling-examples" style="margin-top:0.75rem;margin-bottom:0">
        <div class="ling-examples-label">Classifier forms</div>
        <div class="ling-ex-line"><span class="word">একটা বই</span><span class="gloss">one book (informal)</span></div>
        <div class="ling-ex-line"><span class="word">দুটো বই</span><span class="gloss">two books (informal)</span></div>
        <div class="ling-ex-line"><span class="word">দুটি বই</span><span class="gloss">two books (formal)</span></div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Classifier Fusion</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>In rapid/colloquial speech, classifiers fuse with the numeral, producing morphophonemic contractions:</p>
    <div class="ling-morph-table" style="margin-top:0.75rem">
        <div class="ling-morph-row">
            <span class="ling-morph-source">দুই + টা</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">দুটো</span>
            <span class="ling-morph-gloss">vowel reduction + fusion</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">এক + টা</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">একটা</span>
            <span class="ling-morph-gloss">direct attachment</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">তিন + টা</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">তিনটা</span>
            <span class="ling-morph-gloss">direct attachment</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 4 — SYNTAX & MORPHOLOGY
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Syntax &amp; Morphology</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Grammatical Integration</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.5rem">Cardinals</div>
        <ul>
            <li>Invariant — no gender, case, or agreement marking</li>
            <li>Noun plurality handled independently</li>
            <li>Plural often omitted after numerals</li>
        </ul>
        <p style="font-family:'DM Mono',monospace;font-size:0.88rem;color:var(--ink-muted);margin-top:0.5rem">তিন বই <em style="font-family:'Crimson Pro',serif;font-size:0.9rem">(three books)</em></p>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.5rem">Ordinals</div>
        <ul>
            <li>Often Sanskrit-derived adjectival forms</li>
            <li>No gender inflection (Bengali lacks grammatical gender)</li>
            <li>Written abbreviations: <em>১ম</em>, <em>২য়</em></li>
        </ul>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Ordinals ────────────────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Ordinal Formation</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>The first several ordinals are Sanskrit-derived. Written numerals use the abbreviation suffix <em>-ম</em> (1st) and <em>-য়</em> (2nd onward).</p>
    <div class="ling-morph-table" style="margin-top:0.75rem">
        <div class="ling-morph-row">
            <span class="ling-morph-source">1 (এক)</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">প্রথম</span>
            <span class="ling-morph-gloss">Sanskrit: pratham</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">2 (দুই)</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">দ্বিতীয়</span>
            <span class="ling-morph-gloss">Sanskrit: dvitiya</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">3 (তিন)</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">তৃতীয়</span>
            <span class="ling-morph-gloss">Sanskrit: tritiya</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">5 (পাঁচ)</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">পঞ্চম</span>
            <span class="ling-morph-gloss">Sanskrit: pancham</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">6 (ছয়)</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">ষষ্ঠ</span>
            <span class="ling-morph-gloss">Sanskrit: shashtha</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>Classifier interaction produces morphophonemic contraction in colloquial speech. This is a uniquely Bengali grammatical feature absent in Hindi or Tamil.</p>
</div>
""", unsafe_allow_html=True)

# ── NAVIGATION ──────────────────────────────────────────────
footer_nav("Bengali", "linguistics")
