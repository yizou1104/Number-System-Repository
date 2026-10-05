import streamlit as st

from ui import apply_global_styles, LING_CSS, LING_WIDTH_CSS, language_nav, footer_nav

st.set_page_config(page_title="Tamil Numerals — Linguistics", layout="wide")
apply_global_styles()
st.markdown(LING_CSS, unsafe_allow_html=True)
st.markdown(LING_WIDTH_CSS, unsafe_allow_html=True)
language_nav("Tamil", "linguistics")

# ══════════════════════════════════════════════════════════════
# MASTHEAD
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="ling-masthead">
    <div class="ling-masthead-eyebrow">Linguistic Structure</div>
    <div class="ling-masthead-title">Tamil Numerals</div>
    <div class="ling-tags">
        <span class="ling-tag">Decimal</span>
        <span class="ling-tag">Multiplicative–Additive</span>
        <span class="ling-tag">Non-Subtractive</span>
        <span class="ling-tag">Morphophonemically Conditioned</span>
        <span class="ling-tag">Linker-Dependent</span>
        <span class="ling-tag">Distinct Script Numerals</span>
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
    <p>Tamil is distinctive among the languages in this repository for possessing a dedicated classical numeral script with unique glyphs for 10, 100, and 1000 — in addition to individual digits 0–9.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-props">
        <span class="ling-prop-key">Primary base</span>
        <span class="ling-prop-val"><strong>10 (decimal)</strong></span>
        <span class="ling-prop-key">System type</span>
        <span class="ling-prop-val">Multiplicative–Additive</span>
        <span class="ling-prop-key">Subtractive</span>
        <span class="ling-prop-val">Absent — no productive subtractive forms</span>
        <span class="ling-prop-key">Morphophonology</span>
        <span class="ling-prop-val">Extensive stem alternation in tens and hundreds</span>
        <span class="ling-prop-key">Linkers</span>
        <span class="ling-prop-val">Required between compound components: <em>-த்து</em>, <em>-ற்று</em></span>
        <span class="ling-prop-key">Script</span>
        <span class="ling-prop-val">Tamil script with dedicated classical numeral glyphs</span>
        <span class="ling-prop-key">Large-number pivot</span>
        <span class="ling-prop-val">Indic lakh (10⁵) and crore (10⁷) system</span>
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
    "Glyph":  ["௦","௧","௨","௩","௪","௫","௬","௭","௮","௯","௰"],
    "Form":   ["பூஜ்யம் / சுழியம்","ஒன்று","இரண்டு","மூன்று","நான்கு",
               "ஐந்து","ஆறு","ஏழு","எட்டு","ஒன்பது","பத்து"]
})

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:.5rem">Classical Glyphs</div>
        <p>Tamil possesses dedicated glyphs for 10 (௰), 100 (௱), and 1000 (௲), enabling compact classical notation: <em>௲௱௰௧ = 1,111</em>. These appear in manuscripts, stone inscriptions, and religious texts.</p>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:.5rem">Zero</div>
        <p>Two terms for zero coexist: <em>பூஜ்யம்</em> (Sanskrit loan, mathematical contexts) and <em>சுழியம்</em> (native, meaning "circle" — describing the glyph's shape).</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Teens ──────────────────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">11–19 (Teens)</div>', unsafe_allow_html=True)

st.table({
    "Number": ["11","12","13","14","15","16","17","18","19"],
    "Form":   ["பதினொன்று","பன்னிரண்டு","பதின்மூன்று","பதினான்கு","பதினைந்து",
               "பதினாறு","பதினேழு","பதினெட்டு","பத்தொன்பது"]
})

st.markdown("""
<div class="ling-info">
    <p>Teens use the prefix <em>பதி-</em> (derived from <em>பத்து</em>, ten), but the attachment triggers sandhi and gemination at the boundary. Compare <em>பதினொன்று</em> (11) vs <em>பன்னிரண்டு</em> (12) — the same prefix but different phonological outcomes.</p>
</div>
""", unsafe_allow_html=True)

# ── Tens ────────────────────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Tens</div>', unsafe_allow_html=True)

st.table({
    "Value": ["20","30","40","50","60","70","80","90"],
    "Form":  ["இருபது","முப்பது","நாற்பது","ஐம்பது","அறுபது","எழுபது","எண்பது","தொண்ணூறு"]
})

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Stem Alternation</div>
    <p>Tamil tens are formed by <em>[digit stem] + பது</em>, but digit stems undergo predictable morphophonemic reduction: <em>மூன்று → முப்-</em>, <em>ஐந்து → ஐம்-</em>, <em>எட்டு → எண்-</em>. These alternations are systematic, not idiosyncratic.</p>
</div>
""", unsafe_allow_html=True)

# ── Higher Bases ─────────────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Higher Bases</div>', unsafe_allow_html=True)

st.table({
    "Value":     ["100","1,000","10,000","1,00,000","1,00,00,000"],
    "Form":      ["நூறு","ஆயிரம்","பத்தாயிரம்","இலட்சம்","கோடி"],
    "Structure": ["Independent hundred","Independent thousand","10 × 1,000","Indic lakh (10⁵)","Indic crore (10⁷)"]
})

# ══════════════════════════════════════════════════════════════
# SECTION 3 — COMPOSITIONAL RULES
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Compositional Rules</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">How Numbers Are Built</div>', unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title">Tens Formation</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[Digit stem] + <em>பது</em> (patu, "ten") · with stem alternation</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>The digit stem alternates before <em>-பது</em>. Below are the systematic alternations for the irregular stems:</p>
    <div class="ling-morph-table" style="margin-top:.75rem">
        <div class="ling-morph-row">
            <span class="ling-morph-source">மூன்று</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">முப்-</span>
            <span class="ling-morph-gloss">முப்பது (30)</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">ஐந்து</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">ஐம்-</span>
            <span class="ling-morph-gloss">ஐம்பது (50)</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">எட்டு</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">எண்-</span>
            <span class="ling-morph-gloss">எண்பது (80)</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Additive Structure — Compounds</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[Tens] + <em>-த்து</em> (linker) + [Unit]</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Additive examples</div>
    <div class="ling-ex-line"><span class="num">21</span><span class="word">இருபத்தி ஒன்று</span><span class="gloss">20 + linker + 1</span></div>
    <div class="ling-ex-line"><span class="num">35</span><span class="word">முப்பத்தி ஐந்து</span><span class="gloss">30 + linker + 5</span></div>
    <div class="ling-ex-line"><span class="num">78</span><span class="word">எழுபத்தி எட்டு</span><span class="gloss">70 + linker + 8</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Hundreds Formation</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[Digit stem] + <em>நூறு</em> · gemination and nasal insertion at boundary</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Hundreds with boundary changes</div>
    <div class="ling-ex-line"><span class="num">300</span><span class="word">முந்நூறு</span><span class="gloss">மூன்று + nasal insertion</span></div>
    <div class="ling-ex-line"><span class="num">500</span><span class="word">ஐந்நூறு</span><span class="gloss">ஐந்து + gemination</span></div>
    <div class="ling-ex-line"><span class="num">800</span><span class="word">எண்ணூறு</span><span class="gloss">எட்டு → எண் + நூறு</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Thousands and Full Compounds</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[Higher unit] + <em>-த்து / -ற்று</em> (linker) + [Lower unit]</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Full compound example</div>
    <div class="ling-ex-line"><span class="num">1,234</span><span class="word">ஆயிரத்து இருநூற்றி முப்பத்தி நான்கு</span></div>
    <div class="ling-ex-line" style="padding-left:5rem;font-style:italic;color:var(--ink-muted);font-family:'Crimson Pro',serif;font-size:.9rem">1000 + linker + 200 + linker + 30 + linker + 4</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>The linker <em>-த்து</em> is the standard form; <em>-ற்று</em> appears in certain phonological environments, particularly after alveolar consonants. Both are grammatically obligatory — compounds without them are ungrammatical in formal Tamil.</p>
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
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:.5rem">Cardinals</div>
        <ul>
            <li>No gender marking on numerals</li>
            <li>No case marking on numeral stem</li>
            <li>Noun carries all grammatical marking</li>
            <li>Plural may appear on noun even after numeral</li>
        </ul>
        <p style="font-family:'DM Mono',monospace;font-size:.88rem;color:var(--ink-muted);margin-top:.5rem">மூன்று புத்தகங்கள்</p>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:.5rem">Attributive "One"</div>
        <p>The standalone form <em>ஒன்று</em> (one) is replaced by the attributive form <em>ஒரு</em> when directly modifying a noun. This is a lexical alternation, not inflection.</p>
        <p style="font-family:'DM Mono',monospace;font-size:.88rem;color:var(--ink-muted)">ஒரு புத்தகம் <em style="font-family:'Crimson Pro',serif">(one book)</em></p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Ordinal Formation</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>The first ordinal is suppletive. From 2 onward, the suffix <em>-ஆம்</em> (-ām) attaches productively to the cardinal.</p>
    <div class="ling-morph-table" style="margin-top:.75rem">
        <div class="ling-morph-row">
            <span class="ling-morph-source">1 (ஒன்று)</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">முதல்</span>
            <span class="ling-morph-gloss">suppletive</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">இரண்டு</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">இரண்டாம்</span>
            <span class="ling-morph-gloss">-ஆம் suffix</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">மூன்று</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">மூன்றாம்</span>
            <span class="ling-morph-gloss">-ஆம் suffix</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">நான்கு</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">நான்காம்</span>
            <span class="ling-morph-gloss">-ஆம் suffix</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>Tamil does not use a productive classifier system, distinguishing it from Bengali. Optional measure words (<em>மரம்</em>, <em>படம்</em>, etc.) may appear in context but are not grammatically required by the numeral itself.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# NAVIGATION
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="ling-nav-footer">
    <a class="ling-nav-btn" href="/Tamil_Converter">← Tamil Converter</a>
    <a class="ling-nav-btn active" href="/Tamil_Linguistics">Tamil Linguistics</a>
</div>
""", unsafe_allow_html=True)

footer_nav("Tamil", "linguistics")
