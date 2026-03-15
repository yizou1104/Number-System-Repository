import streamlit as st
from ui import apply_global_styles

st.set_page_config(page_title="Bengali Numerals — Linguistics", layout="centered")

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
    font-family: 'DM Sans', sans-serif; font-size: 0.68rem; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.18em; color: var(--accent);
    display: flex; align-items: center; gap: 0.65rem; margin-bottom: 0.65rem;
}
.ling-masthead-eyebrow::before {
    content: ''; display: inline-block; width: 1.75rem; height: 1.5px;
    background: var(--accent); flex-shrink: 0;
}
.ling-masthead-title {
    font-family: 'Crimson Pro', Georgia, serif; font-size: 3rem; font-weight: 700;
    color: var(--ink); letter-spacing: -0.04em; line-height: 1.05; margin-bottom: 0.9rem;
}
.ling-masthead-sub { display: none; }
.ling-tags { display: flex; flex-wrap: wrap; gap: 0.45rem; }
.ling-tag {
    font-family: 'DM Sans', sans-serif; font-size: 0.68rem; font-weight: 600;
    letter-spacing: 0.07em; text-transform: uppercase; padding: 0.22rem 0.7rem;
    border: 1.5px solid var(--rule-strong); border-radius: 2px; color: var(--ink-soft); background: transparent;
}
.ling-section-label {
    font-family: 'DM Sans', sans-serif; font-size: 0.72rem; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.16em; color: var(--ink-soft);
    display: flex; align-items: center; gap: 1rem; margin: 2.25rem 0 1.1rem 0;
}
.ling-section-label::before { content: ''; display: inline-block; width: 2rem; height: 1px; background: var(--ink-muted); flex-shrink: 0; }
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
    box-shadow: 0 1px 3px rgba(26,22,18,0.05),0 3px 10px rgba(26,22,18,0.04),inset 0 1px 0 rgba(255,255,255,0.65);
    transition: transform 0.22s cubic-bezier(0.4,0,0.2,1),box-shadow 0.22s cubic-bezier(0.4,0,0.2,1),border-color 0.22s ease;
}
.ling-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 2px 6px rgba(26,22,18,0.07),0 8px 24px rgba(26,22,18,0.09),inset 0 1px 0 rgba(255,255,255,0.8);
    border-color: rgba(26,22,18,0.16);
}
.ling-card p, .ling-card li { font-family: 'Crimson Pro', Georgia, serif; font-size: 1.08rem; color: var(--ink-soft); line-height: 1.72; margin-bottom: 0.45rem; }
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
.ling-callout-label { font-family: 'DM Sans', sans-serif; font-size: 0.6rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.14em; color: var(--accent); margin-bottom: 0.4rem; }
.ling-callout p { font-family: 'Crimson Pro', Georgia, serif; font-size: 1.1rem; font-style: italic; color: var(--ink); line-height: 1.6; margin: 0; }
.ling-info { background: rgba(46,107,122,0.05); border: 1px solid rgba(46,107,122,0.18); border-left: 3px solid var(--teal); border-radius: 4px; padding: 0.95rem 1.35rem; margin-bottom: 0.85rem; }
.ling-info p { font-family: 'Crimson Pro', Georgia, serif; font-size: 1.05rem; color: var(--ink-soft); line-height: 1.68; margin: 0; }
.ling-formula { background: var(--parchment-2); border: 1px solid var(--rule-strong); border-radius: 4px; padding: 1.05rem 1.4rem; margin-bottom: 0.85rem; display: flex; align-items: flex-start; gap: 1.2rem; }
.ling-formula-label { font-family: 'DM Sans', sans-serif; font-size: 0.6rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; color: var(--ink-faint); flex-shrink: 0; padding-top: 0.2rem; min-width: 3.5rem; text-align: right; }
.ling-formula-rule { font-family: 'DM Mono', 'Courier New', monospace; font-size: 0.98rem; color: var(--ink); line-height: 1.6; flex: 1; }
.ling-formula-rule em { font-style: normal; color: var(--accent); font-weight: 500; }
.ling-examples { background: var(--parchment-2); border: 1px solid var(--rule); border-left: 3px solid var(--ink-faint); border-radius: 4px; padding: 0.95rem 1.35rem; margin-bottom: 0.85rem; }
.ling-examples-label { font-family: 'DM Sans', sans-serif; font-size: 0.6rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.13em; color: var(--ink-faint); margin-bottom: 0.5rem; }
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
.ling-nav-btn { font-family: 'DM Sans', sans-serif; font-size: 0.78rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.09em; color: var(--ink); background: var(--parchment-2); border: 1.5px solid var(--rule-strong); border-radius: 3px; padding: 0.55rem 1.1rem; text-decoration: none; display: inline-flex; align-items: center; gap: 0.4rem; white-space: nowrap; cursor: pointer; box-shadow: 2px 2px 0 rgba(26,22,18,0.08); transition: all 0.18s cubic-bezier(0.4,0,0.2,1); }
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

# ══════════════════════════════════════════════════════════════
# NAVIGATION
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="ling-nav-footer">
    <a class="ling-nav-btn" href="/Bengali_Converter">← Bengali Converter</a>
    <a class="ling-nav-btn active" href="/Bengali_Linguistics">Bengali Linguistics</a>
</div>
""", unsafe_allow_html=True)