import streamlit as st
from ui import apply_global_styles

st.set_page_config(page_title="Hindi Numerals — Linguistics", layout="centered")

apply_global_styles()

# ─────────────────────────────────────────────────────────────
# SHARED LINGUISTICS STYLESHEET
# ─────────────────────────────────────────────────────────────
LING_CSS = """
<style>
.ling-masthead {
    border-top: 3px solid var(--ink);
    border-bottom: 1px solid var(--rule);
    padding: 1.75rem 0 1.4rem 0;
    margin-bottom: 1.75rem;
}
.ling-masthead-eyebrow {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.68rem; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.18em;
    color: var(--accent); display: flex; align-items: center;
    gap: 0.65rem; margin-bottom: 0.65rem;
}
.ling-masthead-eyebrow::before {
    content: ''; display: inline-block;
    width: 1.75rem; height: 1.5px; background: var(--accent); flex-shrink: 0;
}
.ling-masthead-title {
    font-family: 'Crimson Pro', Georgia, serif;
    font-size: 3rem; font-weight: 700; color: var(--ink);
    letter-spacing: -0.04em; line-height: 1.05; margin-bottom: 0.9rem;
}
.ling-masthead-sub { display: none; }
.ling-tags { display: flex; flex-wrap: wrap; gap: 0.45rem; }
.ling-tag {
    font-family: 'DM Sans', sans-serif; font-size: 0.68rem; font-weight: 600;
    letter-spacing: 0.07em; text-transform: uppercase; padding: 0.22rem 0.7rem;
    border: 1.5px solid var(--rule-strong); border-radius: 2px;
    color: var(--ink-soft); background: transparent;
}
.ling-section-label {
    font-family: 'DM Sans', sans-serif; font-size: 0.72rem; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.16em; color: var(--ink-soft);
    display: flex; align-items: center; gap: 1rem; margin: 2.25rem 0 1.1rem 0;
}
.ling-section-label::before {
    content: ''; display: inline-block; width: 2rem; height: 1px;
    background: var(--ink-muted); flex-shrink: 0;
}
.ling-section-label::after { content: ''; flex: 1; height: 1px; background: var(--rule); }
.ling-section-title {
    font-family: 'Crimson Pro', Georgia, serif; font-size: 1.85rem; font-weight: 600;
    color: var(--ink); letter-spacing: -0.025em; line-height: 1.15;
    margin-bottom: 1.1rem; padding-bottom: 0.45rem; border-bottom: 1px solid var(--rule);
}
.ling-subsection-title {
    font-family: 'Crimson Pro', Georgia, serif; font-size: 1.25rem; font-weight: 600;
    color: var(--ink-soft); letter-spacing: -0.01em; margin-bottom: 0.7rem; margin-top: 0;
}
.ling-card {
    background: var(--card-bg); border: 1px solid var(--card-border); border-radius: 5px;
    padding: 1.3rem 1.55rem; margin-bottom: 0.85rem;
    box-shadow: 0 1px 3px rgba(26,22,18,0.05), 0 3px 10px rgba(26,22,18,0.04), inset 0 1px 0 rgba(255,255,255,0.65);
    transition: transform 0.22s cubic-bezier(0.4,0,0.2,1), box-shadow 0.22s cubic-bezier(0.4,0,0.2,1), border-color 0.22s ease;
}
.ling-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 2px 6px rgba(26,22,18,0.07), 0 8px 24px rgba(26,22,18,0.09), inset 0 1px 0 rgba(255,255,255,0.8);
    border-color: rgba(26,22,18,0.16);
}
.ling-card p, .ling-card li {
    font-family: 'Crimson Pro', Georgia, serif; font-size: 1.08rem;
    color: var(--ink-soft); line-height: 1.72; margin-bottom: 0.45rem;
}
.ling-card p:last-child, .ling-card li:last-child { margin-bottom: 0; }
.ling-card ul { padding-left: 1.3rem; margin: 0; }
.ling-card li::marker { color: var(--accent); }
.ling-callout {
    background: var(--accent-pale); border: 1px solid rgba(184,92,56,0.2);
    border-left: 3px solid var(--accent); border-radius: 4px;
    padding: 1.05rem 1.45rem; margin-bottom: 0.85rem;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.ling-callout:hover { transform: translateY(-1px); box-shadow: 0 4px 16px rgba(184,92,56,0.1); }
.ling-callout-label {
    font-family: 'DM Sans', sans-serif; font-size: 0.6rem; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.14em; color: var(--accent); margin-bottom: 0.4rem;
}
.ling-callout p {
    font-family: 'Crimson Pro', Georgia, serif; font-size: 1.1rem; font-style: italic;
    color: var(--ink); line-height: 1.6; margin: 0;
}
.ling-info {
    background: rgba(46,107,122,0.05); border: 1px solid rgba(46,107,122,0.18);
    border-left: 3px solid var(--teal); border-radius: 4px;
    padding: 0.95rem 1.35rem; margin-bottom: 0.85rem;
}
.ling-info p {
    font-family: 'Crimson Pro', Georgia, serif; font-size: 1.05rem;
    color: var(--ink-soft); line-height: 1.68; margin: 0;
}
.ling-formula {
    background: var(--parchment-2); border: 1px solid var(--rule-strong);
    border-radius: 4px; padding: 1.05rem 1.4rem; margin-bottom: 0.85rem;
    display: flex; align-items: flex-start; gap: 1.2rem;
}
.ling-formula-label {
    font-family: 'DM Sans', sans-serif; font-size: 0.6rem; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.12em; color: var(--ink-faint);
    flex-shrink: 0; padding-top: 0.2rem; min-width: 3.5rem; text-align: right;
}
.ling-formula-rule {
    font-family: 'DM Mono', 'Courier New', monospace; font-size: 0.98rem;
    color: var(--ink); line-height: 1.6; flex: 1;
}
.ling-formula-rule em { font-style: normal; color: var(--accent); font-weight: 500; }
.ling-examples {
    background: var(--parchment-2); border: 1px solid var(--rule);
    border-left: 3px solid var(--ink-faint); border-radius: 4px;
    padding: 0.95rem 1.35rem; margin-bottom: 0.85rem;
}
.ling-examples-label {
    font-family: 'DM Sans', sans-serif; font-size: 0.6rem; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.13em; color: var(--ink-faint); margin-bottom: 0.5rem;
}
.ling-ex-line { font-family: 'DM Mono', 'Courier New', monospace; font-size: 0.95rem; color: var(--ink-soft); line-height: 1.75; }
.ling-ex-line .num { color: var(--accent); font-weight: 500; display: inline-block; min-width: 2.5rem; }
.ling-ex-line .word { color: var(--ink); }
.ling-ex-line .gloss { color: var(--ink-muted); font-style: italic; font-family: 'Crimson Pro', Georgia, serif; font-size: 0.92rem; margin-left: 0.75rem; }
.ling-grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem; margin-bottom: 0.85rem; }
@media (max-width: 600px) { .ling-grid-2 { grid-template-columns: 1fr; } }
.ling-props { display: grid; grid-template-columns: auto 1fr; gap: 0.5rem 1.25rem; align-items: baseline; margin: 0; padding: 0; }
.ling-prop-key { font-family: 'DM Sans', sans-serif; font-size: 0.68rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: var(--ink-faint); white-space: nowrap; }
.ling-prop-val { font-family: 'Crimson Pro', Georgia, serif; font-size: 1.05rem; color: var(--ink-soft); line-height: 1.45; }
.ling-prop-val strong { color: var(--ink); font-weight: 600; }
.ling-morph-table { margin-bottom: 0; }
.ling-morph-row { display: grid; grid-template-columns: 6rem 1.5rem 6rem 1fr; align-items: center; gap: 0.5rem 1rem; padding: 0.45rem 0; border-bottom: 1px solid var(--rule); }
.ling-morph-row:last-child { border-bottom: none; }
.ling-morph-source { font-family: 'DM Mono', 'Courier New', monospace; font-size: 0.93rem; color: var(--ink); }
.ling-morph-arrow { color: var(--ink-faint); font-size: 0.85rem; text-align: center; }
.ling-morph-target { font-family: 'DM Mono', 'Courier New', monospace; font-size: 0.93rem; color: var(--accent); font-weight: 500; }
.ling-morph-gloss { font-family: 'Crimson Pro', Georgia, serif; font-style: italic; font-size: 0.92rem; color: var(--ink-muted); }
.ling-nav-footer { display: flex; gap: 0.75rem; padding: 1.4rem 0 0.5rem 0; border-top: 1px solid var(--rule); margin-top: 2.5rem; flex-wrap: wrap; }
.ling-nav-btn {
    font-family: 'DM Sans', sans-serif; font-size: 0.78rem; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.09em; color: var(--ink);
    background: var(--parchment-2); border: 1.5px solid var(--rule-strong);
    border-radius: 3px; padding: 0.55rem 1.1rem; text-decoration: none;
    display: inline-flex; align-items: center; gap: 0.4rem; white-space: nowrap;
    cursor: pointer; box-shadow: 2px 2px 0 rgba(26,22,18,0.08);
    transition: all 0.18s cubic-bezier(0.4,0,0.2,1);
}
.ling-nav-btn:hover { background: var(--ink); color: var(--parchment); border-color: var(--ink); box-shadow: 3px 3px 0 var(--accent); transform: translate(-1px,-1px); text-decoration: none; }
.ling-nav-btn.active { background: var(--parchment-3); color: var(--ink-muted); cursor: default; box-shadow: none; }
.ling-nav-btn.active:hover { transform: none; background: var(--parchment-3); color: var(--ink-muted); border-color: var(--rule-strong); box-shadow: none; }
</style>
"""
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

# ══════════════════════════════════════════════════════════════
# NAVIGATION
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="ling-nav-footer">
    <a class="ling-nav-btn" href="/Hindi_Converter">← Hindi Converter</a>
    <a class="ling-nav-btn active" href="/Hindi_Linguistics">Hindi Linguistics</a>
</div>
""", unsafe_allow_html=True)