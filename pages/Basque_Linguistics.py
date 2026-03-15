import streamlit as st
from ui import apply_global_styles
 
st.set_page_config(page_title="Basque Numerals — Linguistics", layout="centered")
 
apply_global_styles()
 
# ──────────────────────────────────────────────────────────────
# LINGUISTICS STYLESHEET (reusable across all linguistics pages)
# ──────────────────────────────────────────────────────────────
LING_CSS = """
<style>
/* ─────────────────────────────────────────────────────────────
   PAGE MASTHEAD
───────────────────────────────────────────────────────────── */
.ling-masthead {
    border-top: 3px solid var(--ink);
    border-bottom: 1px solid var(--rule);
    padding: 1.75rem 0 1.4rem 0;
    margin-bottom: 1.75rem;
}
.ling-masthead-eyebrow {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.68rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.18em;
    color: var(--accent);
    display: flex;
    align-items: center;
    gap: 0.65rem;
    margin-bottom: 0.65rem;
}
.ling-masthead-eyebrow::before {
    content: '';
    display: inline-block;
    width: 1.75rem;
    height: 1.5px;
    background: var(--accent);
    flex-shrink: 0;
}
.ling-masthead-title {
    font-family: 'Crimson Pro', Georgia, serif;
    font-size: 3rem;
    font-weight: 700;
    color: var(--ink);
    letter-spacing: -0.04em;
    line-height: 1.05;
    margin-bottom: 0.9rem;
}
.ling-masthead-sub { display: none; }
.ling-tags { display: flex; flex-wrap: wrap; gap: 0.45rem; }
.ling-tag {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 0.07em;
    text-transform: uppercase;
    padding: 0.22rem 0.7rem;
    border: 1.5px solid var(--rule-strong);
    border-radius: 2px;
    color: var(--ink-soft);
    background: transparent;
}
.ling-tag.accent {
    border-color: var(--accent);
    color: var(--accent);
    background: var(--accent-pale);
}
 
/* ─────────────────────────────────────────────────────────────
   SECTION DIVIDER
───────────────────────────────────────────────────────────── */
.ling-section-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.16em;
    color: var(--ink-soft);
    display: flex;
    align-items: center;
    gap: 1rem;
    margin: 2.25rem 0 1.1rem 0;
}
.ling-section-label::before {
    content: '';
    display: inline-block;
    width: 2rem;
    height: 1px;
    background: var(--ink-muted);
    flex-shrink: 0;
}
.ling-section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--rule);
}
 
/* ─────────────────────────────────────────────────────────────
   SECTION TITLE
───────────────────────────────────────────────────────────── */
.ling-section-title {
    font-family: 'Crimson Pro', Georgia, serif;
    font-size: 1.85rem;
    font-weight: 600;
    color: var(--ink);
    letter-spacing: -0.025em;
    line-height: 1.15;
    margin-bottom: 1.1rem;
    padding-bottom: 0.45rem;
    border-bottom: 1px solid var(--rule);
}
.ling-subsection-title {
    font-family: 'Crimson Pro', Georgia, serif;
    font-size: 1.25rem;
    font-weight: 600;
    color: var(--ink-soft);
    letter-spacing: -0.01em;
    margin-bottom: 0.7rem;
    margin-top: 0;
}
 
/* ─────────────────────────────────────────────────────────────
   CONTENT CARD
───────────────────────────────────────────────────────────── */
.ling-card {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 5px;
    padding: 1.3rem 1.55rem;
    margin-bottom: 0.85rem;
    box-shadow:
        0 1px 3px rgba(26,22,18,0.05),
        0 3px 10px rgba(26,22,18,0.04),
        inset 0 1px 0 rgba(255,255,255,0.65);
    transition: transform 0.22s cubic-bezier(0.4,0,0.2,1),
                box-shadow 0.22s cubic-bezier(0.4,0,0.2,1),
                border-color 0.22s ease;
}
.ling-card:hover {
    transform: translateY(-2px);
    box-shadow:
        0 2px 6px rgba(26,22,18,0.07),
        0 8px 24px rgba(26,22,18,0.09),
        inset 0 1px 0 rgba(255,255,255,0.8);
    border-color: rgba(26,22,18,0.16);
}
.ling-card p, .ling-card li {
    font-family: 'Crimson Pro', Georgia, serif;
    font-size: 1.08rem;
    color: var(--ink-soft);
    line-height: 1.72;
    margin-bottom: 0.45rem;
}
.ling-card p:last-child, .ling-card li:last-child { margin-bottom: 0; }
.ling-card ul { padding-left: 1.3rem; margin: 0; }
.ling-card li::marker { color: var(--accent); }
 
/* ─────────────────────────────────────────────────────────────
   HIGHLIGHT CALLOUT (terracotta accent)
───────────────────────────────────────────────────────────── */
.ling-callout {
    background: var(--accent-pale);
    border: 1px solid rgba(184,92,56,0.2);
    border-left: 3px solid var(--accent);
    border-radius: 4px;
    padding: 1.05rem 1.45rem;
    margin-bottom: 0.85rem;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.ling-callout:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 16px rgba(184,92,56,0.1);
}
.ling-callout-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.6rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.14em;
    color: var(--accent);
    margin-bottom: 0.4rem;
}
.ling-callout p {
    font-family: 'Crimson Pro', Georgia, serif;
    font-size: 1.1rem;
    font-style: italic;
    color: var(--ink);
    line-height: 1.6;
    margin: 0;
}
 
/* ─────────────────────────────────────────────────────────────
   INFO PANEL (teal, neutral observation)
───────────────────────────────────────────────────────────── */
.ling-info {
    background: rgba(46,107,122,0.05);
    border: 1px solid rgba(46,107,122,0.18);
    border-left: 3px solid var(--teal);
    border-radius: 4px;
    padding: 0.95rem 1.35rem;
    margin-bottom: 0.85rem;
}
.ling-info p {
    font-family: 'Crimson Pro', Georgia, serif;
    font-size: 1.05rem;
    color: var(--ink-soft);
    line-height: 1.68;
    margin: 0;
}
 
/* ─────────────────────────────────────────────────────────────
   FORMULA CARD
───────────────────────────────────────────────────────────── */
.ling-formula {
    background: var(--parchment-2);
    border: 1px solid var(--rule-strong);
    border-radius: 4px;
    padding: 1.05rem 1.4rem;
    margin-bottom: 0.85rem;
    display: flex;
    align-items: flex-start;
    gap: 1.2rem;
}
.ling-formula-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.6rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: var(--ink-faint);
    flex-shrink: 0;
    padding-top: 0.2rem;
    min-width: 3.5rem;
    text-align: right;
}
.ling-formula-rule {
    font-family: 'DM Mono', 'Courier New', monospace;
    font-size: 0.98rem;
    color: var(--ink);
    line-height: 1.6;
    flex: 1;
}
.ling-formula-rule em {
    font-style: normal;
    color: var(--accent);
    font-weight: 500;
}
 
/* ─────────────────────────────────────────────────────────────
   EXAMPLE BLOCK
───────────────────────────────────────────────────────────── */
.ling-examples {
    background: var(--parchment-2);
    border: 1px solid var(--rule);
    border-left: 3px solid var(--ink-faint);
    border-radius: 4px;
    padding: 0.95rem 1.35rem;
    margin-bottom: 0.85rem;
}
.ling-examples-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.6rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.13em;
    color: var(--ink-faint);
    margin-bottom: 0.5rem;
}
.ling-ex-line {
    font-family: 'DM Mono', 'Courier New', monospace;
    font-size: 0.95rem;
    color: var(--ink-soft);
    line-height: 1.75;
}
.ling-ex-line .num {
    color: var(--accent);
    font-weight: 500;
    display: inline-block;
    min-width: 2.5rem;
}
.ling-ex-line .word { color: var(--ink); }
.ling-ex-line .gloss {
    color: var(--ink-muted);
    font-style: italic;
    font-family: 'Crimson Pro', Georgia, serif;
    font-size: 0.92rem;
    margin-left: 0.75rem;
}
 
/* ─────────────────────────────────────────────────────────────
   TWO-COLUMN GRID
───────────────────────────────────────────────────────────── */
.ling-grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.75rem;
    margin-bottom: 0.85rem;
}
@media (max-width: 600px) { .ling-grid-2 { grid-template-columns: 1fr; } }
 
/* ─────────────────────────────────────────────────────────────
   PROPERTY LIST
───────────────────────────────────────────────────────────── */
.ling-props {
    display: grid;
    grid-template-columns: auto 1fr;
    gap: 0.5rem 1.25rem;
    align-items: baseline;
    margin: 0;
    padding: 0;
}
.ling-prop-key {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.68rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--ink-faint);
    white-space: nowrap;
}
.ling-prop-val {
    font-family: 'Crimson Pro', Georgia, serif;
    font-size: 1.05rem;
    color: var(--ink-soft);
    line-height: 1.45;
}
.ling-prop-val strong { color: var(--ink); font-weight: 600; }
 
/* ─────────────────────────────────────────────────────────────
   MORPHEME ROW
───────────────────────────────────────────────────────────── */
.ling-morph-table { margin-bottom: 0; }
.ling-morph-row {
    display: grid;
    grid-template-columns: 6rem 1.5rem 6rem 1fr;
    align-items: center;
    gap: 0.5rem 1rem;
    padding: 0.45rem 0;
    border-bottom: 1px solid var(--rule);
}
.ling-morph-row:last-child { border-bottom: none; }
.ling-morph-source {
    font-family: 'DM Mono', 'Courier New', monospace;
    font-size: 0.93rem;
    color: var(--ink);
}
.ling-morph-arrow {
    color: var(--ink-faint);
    font-size: 0.85rem;
    text-align: center;
}
.ling-morph-target {
    font-family: 'DM Mono', 'Courier New', monospace;
    font-size: 0.93rem;
    color: var(--accent);
    font-weight: 500;
}
.ling-morph-gloss {
    font-family: 'Crimson Pro', Georgia, serif;
    font-style: italic;
    font-size: 0.92rem;
    color: var(--ink-muted);
}
 
/* ─────────────────────────────────────────────────────────────
   NAVIGATION FOOTER
───────────────────────────────────────────────────────────── */
.ling-nav-footer {
    display: flex;
    gap: 0.75rem;
    padding: 1.4rem 0 0.5rem 0;
    border-top: 1px solid var(--rule);
    margin-top: 2.5rem;
    flex-wrap: wrap;
}
.ling-nav-btn {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.78rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.09em;
    color: var(--ink);
    background: var(--parchment-2);
    border: 1.5px solid var(--rule-strong);
    border-radius: 3px;
    padding: 0.55rem 1.1rem;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    white-space: nowrap;
    cursor: pointer;
    box-shadow: 2px 2px 0 rgba(26,22,18,0.08);
    transition: all 0.18s cubic-bezier(0.4,0,0.2,1);
}
.ling-nav-btn:hover {
    background: var(--ink);
    color: var(--parchment);
    border-color: var(--ink);
    box-shadow: 3px 3px 0 var(--accent);
    transform: translate(-1px, -1px);
    text-decoration: none;
}
.ling-nav-btn.active {
    background: var(--parchment-3);
    color: var(--ink-muted);
    cursor: default;
    box-shadow: none;
}
.ling-nav-btn.active:hover {
    transform: none;
    background: var(--parchment-3);
    color: var(--ink-muted);
    border-color: var(--rule-strong);
    box-shadow: none;
}
</style>
"""
 
st.markdown(LING_CSS, unsafe_allow_html=True)
 
# ══════════════════════════════════════════════════════════════
# PAGE MASTHEAD
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="ling-masthead">
    <div class="ling-masthead-eyebrow">Linguistic Structure</div>
    <div class="ling-masthead-title">Basque Numerals</div>
    <div class="ling-masthead-sub">
        A survey of the Basque (Euskara) numeral grammar — its vigesimal base,
        multiplicative–additive composition, and morphosyntactic properties.
    </div>
    <div class="ling-tags">
        <span class="ling-tag">Vigesimal</span>
        <span class="ling-tag">Multiplicative–Additive</span>
        <span class="ling-tag">Non-Subtractive</span>
        <span class="ling-tag">Gender-Neutral</span>
        <span class="ling-tag">Language Isolate</span>
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
    <p>Basque is one of the few fully productive vigesimal numeral systems surviving in modern Europe, structurally unrelated to any Indo-European language.</p>
</div>
""", unsafe_allow_html=True)
 
st.markdown("""
<div class="ling-card">
    <div class="ling-props">
        <span class="ling-prop-key">Primary base</span>
        <span class="ling-prop-val"><strong>20 (vigesimal)</strong></span>
        <span class="ling-prop-key">Secondary base</span>
        <span class="ling-prop-val">Decimal layer from 100 upward</span>
        <span class="ling-prop-key">System type</span>
        <span class="ling-prop-val">Multiplicative–Additive</span>
        <span class="ling-prop-key">Subtractive</span>
        <span class="ling-prop-val">Absent</span>
        <span class="ling-prop-key">Gender marking</span>
        <span class="ling-prop-val">None — system is gender-neutral</span>
        <span class="ling-prop-key">Script</span>
        <span class="ling-prop-val">Latin alphabet; no indigenous numeral glyphs</span>
    </div>
</div>
""", unsafe_allow_html=True)
 
# ══════════════════════════════════════════════════════════════
# SECTION 2 — BASIC DIGITS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Digits &amp; Bases</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Basic Digits (0–10)</div>', unsafe_allow_html=True)
 
st.table({
    "Number": ["0","1","2","3","4","5","6","7","8","9","10"],
    "Form":   ["zero","bat","bi","hiru","lau","bost","sei","zazpi","zortzi","bederatzi","hamar"]
})
 
st.markdown("""
<div class="ling-info">
    <p>Basque uses the Latin script throughout. Zero is a Latin loanword (<em>zero</em>); the remaining digits are native Basque roots with no documented external etymology.</p>
</div>
""", unsafe_allow_html=True)
 
# ── Teens ────────────────────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.75rem">11–19 (Teens)</div>', unsafe_allow_html=True)
 
st.table({
    "Number": ["11","12","13","14","15","16","17","18","19"],
    "Form":   ["hamaika","hamabi","hamahiru","hamalau","hamabost",
               "hamasei","hamazazpi","hemezortzi","hemeretzi"]
})
 
st.markdown("""
<div style="display:flex; gap:0.75rem; margin-bottom:0.85rem; align-items:flex-start; flex-wrap:wrap;">
    <div class="ling-formula" style="margin-bottom:0; flex:0 0 auto; min-width:0;">
        <span class="ling-formula-label">Pattern</span>
        <span class="ling-formula-rule"><em>hamar</em> + unit<br>(10 + digit)</span>
    </div>
    <div class="ling-card" style="margin-bottom:0; flex:1 1 220px;">
        <p>Several teens show phonological contraction at the boundary. 18 and 19 use the reduced stem <em>heme-</em> rather than <em>hama-</em>, a historical assimilation.</p>
    </div>
</div>
""", unsafe_allow_html=True)
 
# ── Vigesimal Bases ──────────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.75rem">Core Vigesimal Bases</div>', unsafe_allow_html=True)
 
st.table({
    "Value":     ["20","40","60","80","100"],
    "Form":      ["hogei","berrogei","hirurogei","laurogei","ehun"],
    "Structure": ["Base unit","2 × 20","3 × 20","4 × 20","Decimal pivot"]
})
 
st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Vigesimal Structure</div>
    <p>40, 60, and 80 are formed multiplicatively: a modified digit stem fuses with <em>-rogei</em> (from <em>hogei</em>, 20). The base itself, <em>hogei</em>, is the sole undecomposed score.</p>
</div>
""", unsafe_allow_html=True)
 
# ══════════════════════════════════════════════════════════════
# SECTION 3 — COMPOSITIONAL RULES
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Compositional Rules</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">How Numbers Are Built</div>', unsafe_allow_html=True)
 
# ── Vigesimal Multiplication ─────────────────────────────────
st.markdown('<div class="ling-subsection-title">Vigesimal Multiplication</div>', unsafe_allow_html=True)
 
st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[Multiplier stem] + <em>rogei</em></span>
</div>
""", unsafe_allow_html=True)
 
st.markdown("""
<div class="ling-card">
    <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">Morphophonemic Alternations</div>
    <p>Digit stems undergo reduction when prefixing the vigesimal base:</p>
    <div class="ling-morph-table">
        <div class="ling-morph-row">
            <span class="ling-morph-source">bi</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">ber-</span>
            <span class="ling-morph-gloss">berrogei (40)</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">hiru</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">hirur-</span>
            <span class="ling-morph-gloss">hirurogei (60)</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">lau</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">laur-</span>
            <span class="ling-morph-gloss">laurogei (80)</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
 
# ── Additive Structure ───────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.75rem">Additive Structure — Within Scores</div>', unsafe_allow_html=True)
 
st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule"><em>hogei</em> + <em>ta</em> + unit</span>
</div>
""", unsafe_allow_html=True)
 
st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Examples — 21 to 40 range</div>
    <div class="ling-ex-line"><span class="num">21</span><span class="word">hogeita bat</span><span class="gloss">twenty + connector + one</span></div>
    <div class="ling-ex-line"><span class="num">25</span><span class="word">hogeita bost</span><span class="gloss">twenty + connector + five</span></div>
    <div class="ling-ex-line"><span class="num">37</span><span class="word">hogeita hamazazpi</span><span class="gloss">twenty + connector + seventeen</span></div>
</div>
""", unsafe_allow_html=True)
 
st.markdown("""
<div class="ling-info">
    <p>The connector <strong>-ta</strong> is a phonologically reduced form of <em>eta</em> ("and"), clitised directly to the vigesimal base when the remainder is a teen or small unit.</p>
</div>
""", unsafe_allow_html=True)
 
# ── Structure Above 40 ───────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.75rem">Structure Above 40</div>', unsafe_allow_html=True)
 
st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[Score multiple] + <em>ta</em> + [remainder]</span>
</div>
""", unsafe_allow_html=True)
 
st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Examples — higher scores</div>
    <div class="ling-ex-line"><span class="num">50</span><span class="word">berrogeita hamar</span><span class="gloss">40 + ten</span></div>
    <div class="ling-ex-line"><span class="num">67</span><span class="word">hirurogeita zazpi</span><span class="gloss">60 + seven</span></div>
    <div class="ling-ex-line"><span class="num">90</span><span class="word">laurogeita hamar</span><span class="gloss">80 + ten</span></div>
</div>
""", unsafe_allow_html=True)
 
# ── Decimal Layer ────────────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.75rem">Hundreds and Above — Decimal Layer</div>', unsafe_allow_html=True)
 
st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[Digit stem] + <em>-ehun</em> · · · <em>eta</em> · · · [remainder]</span>
</div>
""", unsafe_allow_html=True)
 
st.table({
    "Value": ["100","200","300","400"],
    "Form":  ["ehun","berrehun","hirurehun","laurehun"],
    "Analysis": ["base","2 × ehun","3 × ehun","4 × ehun"]
})
 
st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Extended Example</div>
    <div class="ling-ex-line"><span class="num">256</span><span class="word">berrehun eta berrogeita hamasei</span></div>
    <div class="ling-ex-line" style="padding-left:5rem;font-size:0.88rem;color:var(--ink-muted);font-style:italic">200 + and + 40 + 16</div>
</div>
""", unsafe_allow_html=True)
 
st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">System Shift</div>
    <p>At 100, Basque switches from vigesimal to decimal organisation. The hundreds layer is strictly multiplicative-decimal; the vigesimal structure re-appears only within each hundred's remainder.</p>
</div>
""", unsafe_allow_html=True)
 
# ══════════════════════════════════════════════════════════════
# SECTION 4 — CONNECTORS & SPECIAL FORMS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Connectors &amp; Special Forms</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Special Characters &amp; Connectors</div>', unsafe_allow_html=True)
 
st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">-ta</div>
        <p>Clitic additive connector. Attaches directly to a vigesimal score base when followed by a remainder. Phonologically reduced from <em>eta</em>.</p>
        <p style="font-family:'DM Mono',monospace;font-size:0.9rem;color:var(--ink-muted)">hogei<strong>ta</strong> bat = 21</p>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">eta</div>
        <p>Full additive conjunction ("and"). Used between hundreds and sub-hundred remainders, and between thousands and smaller components.</p>
        <p style="font-family:'DM Mono',monospace;font-size:0.9rem;color:var(--ink-muted)">berrehun <strong>eta</strong> hogei = 220</p>
    </div>
</div>
""", unsafe_allow_html=True)
 
st.markdown("""
<div class="ling-info">
    <p><strong>Zero</strong> is expressed as <em>zero</em> — a Latin loanword with no native Basque equivalent in the traditional counting system.</p>
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
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.55rem">Numeral–Noun Order</div>
        <p>Numerals precede the noun they quantify, consistent with Basque's head-final typology.</p>
        <p style="font-family:'DM Mono',monospace;font-size:0.93rem;color:var(--ink-muted)">bi etxe &nbsp;·&nbsp; <em>two houses</em></p>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.55rem">Plural Suppression</div>
        <p>After a cardinal numeral, the noun typically remains in its singular (absolutive) form. The numeral itself carries the plurality information.</p>
        <p style="font-family:'DM Mono',monospace;font-size:0.93rem;color:var(--ink-muted)">bi etxe &nbsp;(not <s>bi etxeak</s>)</p>
    </div>
</div>
""", unsafe_allow_html=True)
 
st.markdown("""
<div class="ling-card">
    <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.55rem">Case Marking — Ergative–Absolutive</div>
    <p>Basque is an ergative–absolutive language. Case suffixes attach to the noun phrase as a whole, not to the numeral stem. The numeral is invariable; case is borne by the head noun.</p>
    <div class="ling-examples" style="margin-top:0.75rem;margin-bottom:0">
        <div class="ling-examples-label">Case on noun phrase</div>
        <div class="ling-ex-line"><span class="word">bi etxe</span><span class="gloss">two houses (absolutive)</span></div>
        <div class="ling-ex-line"><span class="word">bi etxe-tan</span><span class="gloss">in two houses (inessive)</span></div>
        <div class="ling-ex-line"><span class="word">bi etxe-k</span><span class="gloss">two houses (ergative subject)</span></div>
    </div>
</div>
""", unsafe_allow_html=True)
 
# ── Ordinals ─────────────────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.75rem">Ordinal Formation</div>', unsafe_allow_html=True)
 
st.markdown("""
<div class="ling-card">
    <p>Ordinals are formed by suffixing <strong>-garren</strong> to the cardinal stem. The first three ordinals have irregular or suppletive forms.</p>
    <div class="ling-morph-table" style="margin-top:0.75rem">
        <div class="ling-morph-row">
            <span class="ling-morph-source">1</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">lehen</span>
            <span class="ling-morph-gloss">first (suppletive)</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">bi</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">bigarren</span>
            <span class="ling-morph-gloss">second</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">hiru</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">hirugarren</span>
            <span class="ling-morph-gloss">third</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">lau</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">laugarren</span>
            <span class="ling-morph-gloss">fourth</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">bost</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">bosgarren</span>
            <span class="ling-morph-gloss">fifth</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
 
# ── Inflection Summary ───────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.75rem">Morphological Summary</div>', unsafe_allow_html=True)
 
st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.55rem">Cardinals</div>
        <ul>
            <li>No gender marking</li>
            <li>Invariable — no case inflection on numeral</li>
            <li>Case carried by the noun phrase</li>
            <li>Morphophonemic stem changes in vigesimal multiplication only</li>
        </ul>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.55rem">Ordinals</div>
        <ul>
            <li>Productive suffix <strong>-garren</strong></li>
            <li>Ordinals function as adjectives</li>
            <li>Follow agreement patterns with the noun phrase</li>
            <li><em>lehen</em> (first) is suppletive</li>
        </ul>
    </div>
</div>
""", unsafe_allow_html=True)
 
st.markdown("""
<div class="ling-info">
    <p>The collective loanform <em>dozena</em> (dozen) has entered colloquial Basque from Romance. It does not participate in the native vigesimal compositional system.</p>
</div>
""", unsafe_allow_html=True)
 
# ══════════════════════════════════════════════════════════════
# NAVIGATION FOOTER
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="ling-nav-footer">
    <a class="ling-nav-btn" href="/Basque_Converter">← Basque Converter</a>
    <a class="ling-nav-btn active" href="/Basque_Linguistics">Basque Linguistics</a>
</div>
""", unsafe_allow_html=True)