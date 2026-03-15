import streamlit as st
from ui import apply_global_styles

st.set_page_config(page_title="Tamil Numerals — Linguistics", layout="centered")
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
    "Form":   ["பதினொன்று","பன்னிரண்டு","பதிமூன்று","பதினான்கு","பதினைந்து",
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
    <div class="ling-ex-line"><span class="num">21</span><span class="word">இருபத்து ஒன்று</span><span class="gloss">20 + linker + 1</span></div>
    <div class="ling-ex-line"><span class="num">35</span><span class="word">முப்பத்து ஐந்து</span><span class="gloss">30 + linker + 5</span></div>
    <div class="ling-ex-line"><span class="num">78</span><span class="word">எழுபத்து எட்டு</span><span class="gloss">70 + linker + 8</span></div>
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
    <div class="ling-ex-line"><span class="num">300</span><span class="word">முன்னூறு</span><span class="gloss">மூன்று + nasal insertion</span></div>
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
    <div class="ling-ex-line"><span class="num">1,234</span><span class="word">ஆயிரத்து இருநூற்று முப்பத்து நான்கு</span></div>
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