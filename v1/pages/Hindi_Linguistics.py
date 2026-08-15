import streamlit as st
from ui import apply_global_styles, home_nav, LING_CSS

st.set_page_config(page_title="Hindi Numerals — Linguistics", layout="centered")

apply_global_styles()

# ─────────────────────────────────────────────────────────────
# SHARED LINGUISTICS STYLESHEET
# ─────────────────────────────────────────────────────────────
st.markdown(LING_CSS, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# MASTHEAD
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="ling-masthead">
    <div class="ling-masthead-eyebrow">Linguistic Structure</div>
    <div class="ling-masthead-title">Hindi Numerals</div>
    <div class="ling-tags">
        <span class="ling-tag">Decimal</span>
        <span class="ling-tag">Lexicalized 1–99</span>
        <span class="ling-tag">Multiplicative–Additive</span>
        <span class="ling-tag">Non-Subtractive</span>
        <span class="ling-tag">Lakh-Based Grouping</span>
        <span class="ling-tag">Partially Inflectional</span>
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
    <p>Hindi numbers from 1–99 are largely lexicalized — they must be memorized and do not follow transparent compositional rules. Regularity only begins from 100 upward.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-props">
        <span class="ling-prop-key">Primary base</span>
        <span class="ling-prop-val"><strong>10 (decimal)</strong></span>
        <span class="ling-prop-key">1–99 structure</span>
        <span class="ling-prop-val">Lexicalized — memorized forms with internal alternations</span>
        <span class="ling-prop-key">100+ structure</span>
        <span class="ling-prop-val">Multiplicative–Additive (regular)</span>
        <span class="ling-prop-key">Large-number pivot</span>
        <span class="ling-prop-val">10⁵ (lakh system) — Indian grouping: 3-2-2-2</span>
        <span class="ling-prop-key">Subtractive</span>
        <span class="ling-prop-val">Absent — <em>उन्नीस</em> (19) is lexical, not "20 − 1"</span>
        <span class="ling-prop-key">Script</span>
        <span class="ling-prop-val">Devanagari glyphs (० – ९); Arabic numerals used in modern contexts</span>
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
    "Glyph":  ["०","१","२","३","४","५","६","७","८","९","१०"],
    "Form":   ["शून्य / सिफ़र","एक","दो","तीन","चार","पाँच","छह","सात","आठ","नौ","दस"]
})

st.markdown("""
<div class="ling-info">
    <p>Hindi uses Devanagari numeral glyphs, though Arabic numerals (0–9) are now common in everyday usage. Two words for zero exist: <em>शून्य</em> (Sanskrit origin) is mathematical; <em>सिफ़र</em> (Persian/Arabic) is used in financial contexts.</p>
</div>
""", unsafe_allow_html=True)

# ── Teens ──────────────────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">11–19 (Irregular Teens)</div>', unsafe_allow_html=True)

st.table({
    "Number": ["11","12","13","14","15","16","17","18","19"],
    "Form":   ["ग्यारह","बारह","तेरह","चौदह","पंद्रह","सोलह","सत्रह","अठारह","उन्नीस"]
})

st.markdown("""
<div class="ling-card">
    <p>Forms from 11–19 are <strong>synchronically irregular</strong> and must be memorized individually. They show historical derivation from Sanskrit but the patterns are not productively applicable.</p>
</div>
""", unsafe_allow_html=True)

# ── Tens ────────────────────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Tens</div>', unsafe_allow_html=True)

st.table({
    "Value": ["20","30","40","50","60","70","80","90"],
    "Form":  ["बीस","तीस","चालीस","पचास","साठ","सत्तर","अस्सी","नब्बे"]
})

st.markdown("""
<div class="ling-info">
    <p>All decades are fully lexicalized — none is transparently "digit × 10". The internal structure of 1–99 includes prefix alternations, consonant gemination, and <em>un-</em> prefix forms in certain sub-decade positions.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">1–99 Internal Patterns</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Selected irregular compounds</div>
    <div class="ling-ex-line"><span class="num">21</span><span class="word">इक्कीस</span><span class="gloss">consonant gemination</span></div>
    <div class="ling-ex-line"><span class="num">25</span><span class="word">पच्चीस</span><span class="gloss">internal alternation</span></div>
    <div class="ling-ex-line"><span class="num">29</span><span class="word">उनतीस</span><span class="gloss">un- prefix form</span></div>
    <div class="ling-ex-line"><span class="num">59</span><span class="word">उनसठ</span><span class="gloss">un- prefix form</span></div>
</div>
""", unsafe_allow_html=True)

# ── Higher Bases ─────────────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Higher Bases — Indian Grouping</div>', unsafe_allow_html=True)

st.table({
    "Value":     ["100","1,000","1,00,000","1,00,00,000","1,00,00,00,000","1,00,00,00,00,000"],
    "Form":      ["सौ","हज़ार","लाख","करोड़","अरब","खरब"],
    "Structure": ["Hundred unit","Thousand unit","10⁵ pivot","10⁷ pivot","10⁹ unit","10¹¹ unit"]
})

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Indian Digit Grouping</div>
    <p>Hindi uses a 3-2-2-2 digit grouping pattern, not the Western 3-3-3. One crore is written 1,00,00,000 — not 10,000,000. This reflects the lakh and crore pivot points native to South Asian mathematics.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 3 — COMPOSITIONAL RULES
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Compositional Rules</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">How Numbers Are Built (100+)</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[Digit] + <em>Base unit</em> + [Lower components] · descending magnitude order</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Compound Examples</div>
    <div class="ling-ex-line"><span class="num">125</span><span class="word">एक सौ पच्चीस</span></div>
    <div class="ling-ex-line"><span class="num">250</span><span class="word">दो सौ पचास</span></div>
    <div class="ling-ex-line"><span class="num">5,432</span><span class="word">पाँच हज़ार चार सौ बत्तीस</span></div>
    <div class="ling-ex-line"><span class="num">1,23,45,678</span><span class="word">एक करोड़ तेईस लाख पैंतालीस हज़ार छह सौ अठहत्तर</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>No internal conjunction equivalent to English "and" is used. The compound simply follows descending magnitude order: [Crore] + [Lakh] + [Thousand] + [Hundred] + [1–99].</p>
</div>
""", unsafe_allow_html=True)

# ── Agreement on "एक" ───────────────────────────────────────
st.markdown("""
<div class="ling-card">
    <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.5rem">Agreement — <em>एक</em></div>
    <p>Cardinals are largely invariant, but <em>एक</em> (one) behaves syntactically like an adjective and may show agreement patterns in certain constructions.</p>
    <p style="font-family:'DM Mono',monospace;font-size:0.9rem;color:var(--ink-muted)">एक आदमी &nbsp;·&nbsp; एक किताब</p>
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
            <li>Invariant — no case marking</li>
            <li>No plural marking on numeral</li>
            <li>Plural may be suppressed on noun after numeral</li>
        </ul>
        <p style="font-family:'DM Mono',monospace;font-size:0.88rem;color:var(--ink-muted);margin-top:0.5rem">तीन आदमी <em style="font-family:'Crimson Pro',serif;font-size:0.9rem">(three men)</em></p>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.5rem">Ordinals</div>
        <ul>
            <li>Fully adjectival — agree in gender and number</li>
            <li>First four are suppletive/irregular</li>
            <li>From 5 onward: cardinal + <em>-वाँ</em> suffix</li>
        </ul>
        <p style="font-family:'DM Mono',monospace;font-size:0.88rem;color:var(--ink-muted);margin-top:0.5rem">पाँचवाँ · छठा</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Ordinal forms ────────────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Ordinal Formation</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>The first four ordinals are suppletive. From 5 onward, the productive suffix <em>-वाँ</em> attaches to the cardinal.</p>
    <div class="ling-morph-table" style="margin-top:0.75rem">
        <div class="ling-morph-row">
            <span class="ling-morph-source">1 (एक)</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">पहला</span>
            <span class="ling-morph-gloss">suppletive; inflects masc./fem.</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">2 (दो)</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">दूसरा</span>
            <span class="ling-morph-gloss">suppletive</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">3 (तीन)</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">तीसरा</span>
            <span class="ling-morph-gloss">semi-regular</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">4 (चार)</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">चौथा</span>
            <span class="ling-morph-gloss">suppletive</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">5+ (पाँच…)</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">पाँचवाँ…</span>
            <span class="ling-morph-gloss">productive -वाँ suffix</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Ordinal gender agreement</div>
    <div class="ling-ex-line"><span class="word">पहला लड़का</span><span class="gloss">first boy (masc.)</span></div>
    <div class="ling-ex-line"><span class="word">पहली लड़की</span><span class="gloss">first girl (fem.)</span></div>
    <div class="ling-ex-line"><span class="word">पहले लड़के</span><span class="gloss">first boys (masc. pl.)</span></div>
</div>
""", unsafe_allow_html=True)

# ── NAVIGATION ──────────────────────────────────────────────
st.markdown('<div class="nav-row">', unsafe_allow_html=True)
st.page_link("pages/Hindi_Converter.py", label="← Hindi Converter")
st.page_link("Home.py", label="← Home")
st.markdown('</div>', unsafe_allow_html=True)