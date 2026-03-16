import streamlit as st
from ui import apply_global_styles, home_nav

st.set_page_config(page_title="Greek Numerals — Linguistics", layout="centered")

apply_global_styles()

# ─────────────────────────────────────────────────────────────
# SHARED LINGUISTICS STYLESHEET (identical across all ling pages)
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
.ling-formula-rule em { font-style: normal; color: var(--accent); font-weight: 500; }
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
.ling-ex-line .num { color: var(--accent); font-weight: 500; display: inline-block; min-width: 2.5rem; }
.ling-ex-line .word { color: var(--ink); }
.ling-ex-line .gloss { color: var(--ink-muted); font-style: italic; font-family: 'Crimson Pro', Georgia, serif; font-size: 0.92rem; margin-left: 0.75rem; }
.ling-grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.75rem;
    margin-bottom: 0.85rem;
}
@media (max-width: 600px) { .ling-grid-2 { grid-template-columns: 1fr; } }
.ling-props {
    display: grid;
    grid-template-columns: auto 1fr;
    gap: 0.5rem 1.25rem;
    align-items: baseline;
    margin: 0; padding: 0;
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
.ling-morph-source { font-family: 'DM Mono', 'Courier New', monospace; font-size: 0.93rem; color: var(--ink); }
.ling-morph-arrow { color: var(--ink-faint); font-size: 0.85rem; text-align: center; }
.ling-morph-target { font-family: 'DM Mono', 'Courier New', monospace; font-size: 0.93rem; color: var(--accent); font-weight: 500; }
.ling-morph-gloss { font-family: 'Crimson Pro', Georgia, serif; font-style: italic; font-size: 0.92rem; color: var(--ink-muted); }
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
# MASTHEAD
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="ling-masthead">
    <div class="ling-masthead-eyebrow">Linguistic Structure</div>
    <div class="ling-masthead-title">Greek Numerals</div>
    <div class="ling-tags">
        <span class="ling-tag">Decimal</span>
        <span class="ling-tag">Multiplicative–Additive</span>
        <span class="ling-tag">Non-Subtractive</span>
        <span class="ling-tag">Gender-Sensitive</span>
        <span class="ling-tag">Case-Inflecting</span>
        <span class="ling-tag">Morphologically Integrated</span>
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
    <p>Modern Greek numerals are fully integrated into the language's inflectional grammar — they decline for gender, number, and case, and agree morphologically with the nouns they modify.</p>
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
        <span class="ling-prop-val">Absent</span>
        <span class="ling-prop-key">Gender marking</span>
        <span class="ling-prop-val">Present — 1 and hundreds inflect for gender</span>
        <span class="ling-prop-key">Case inflection</span>
        <span class="ling-prop-val">Present in formal registers</span>
        <span class="ling-prop-key">Script</span>
        <span class="ling-prop-val">Greek alphabet; historical alphabetic numerals also exist</span>
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
    "Form": [
        "μηδέν", "ένας / μία / ένα", "δύο", "τρία", "τέσσερα",
        "πέντε", "έξι", "επτά", "οκτώ", "εννέα", "δέκα"
    ]
})

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Gender Inflection — 1</div>
    <p>The numeral "1" is the only cardinal that inflects for gender in all registers: <em>ένας</em> (masc.) · <em>μία</em> (fem.) · <em>ένα</em> (neut.).</p>
</div>
""", unsafe_allow_html=True)

# ── Teens ──────────────────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">11–19 (Teens)</div>', unsafe_allow_html=True)

st.table({
    "Number": ["11","12","13","14","15","16","17","18","19"],
    "Form": ["έντεκα","δώδεκα","δεκατρία","δεκατέσσερα","δεκαπέντε",
             "δεκαέξι","δεκαεπτά","δεκαοκτώ","δεκαεννέα"]
})

st.markdown("""
<div style="display:flex; gap:0.75rem; align-items:flex-start; flex-wrap:wrap; margin-bottom:0.85rem;">
    <div class="ling-formula" style="margin-bottom:0; flex:0 0 auto;">
        <span class="ling-formula-label">Pattern</span>
        <span class="ling-formula-rule"><em>δεκα-</em> + unit</span>
    </div>
    <div class="ling-card" style="margin-bottom:0; flex:1 1 200px;">
        <p>11 (<em>έντεκα</em>) and 12 (<em>δώδεκα</em>) are historically contracted forms — they do not follow the regular <em>δεκα-</em> + unit pattern.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Tens ────────────────────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Tens</div>', unsafe_allow_html=True)

st.table({
    "Value": ["20","30","40","50","60","70","80","90"],
    "Form": ["είκοσι","τριάντα","σαράντα","πενήντα","εξήντα","εβδομήντα","ογδόντα","ενενήντα"]
})

st.markdown("""
<div class="ling-info">
    <p>All decades are fully lexicalized forms. No conjunction equivalent to English "and" is used between tens and units: <em>είκοσι ένα</em> = 21, <em>τριάντα δύο</em> = 32.</p>
</div>
""", unsafe_allow_html=True)

# ── Hundreds and Higher ────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Hundreds and Higher</div>', unsafe_allow_html=True)

st.table({
    "Value": ["100","200","300","1,000","1,000,000"],
    "Form": ["εκατό(ν)","διακόσια","τριακόσια","χίλια","ένα εκατομμύριο"],
    "Structure": ["Independent base","Digit stem + -κόσια","Digit stem + -κόσια","Plural noun form","Lexical noun"]
})

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.5rem">Hundreds</div>
        <p>Hundreds use the suffix <em>-κόσια</em> fused to the digit stem. They behave as neuter plural adjectives and inflect for gender when modifying a noun.</p>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.5rem">Millions</div>
        <p>Millions behave as lexical nouns and require agreement. <em>ένα εκατομμύριο</em> (1M) · <em>δύο εκατομμύρια</em> (2M) — the noun itself pluralises.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Compound Example</div>
    <div class="ling-ex-line"><span class="num">1,234</span><span class="word">χίλια διακόσια τριάντα τέσσερα</span></div>
    <div class="ling-ex-line"><span class="num">580</span><span class="word">πεντακόσια ογδόντα</span></div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 3 — HISTORICAL LAYER
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Historical Layer</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Alphabetic Numerals</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Greek historically used alphabetic numerals, where each letter of the Greek alphabet represented a specific value. A keraia (ʹ) marked a letter as a numeral.</p>
    <div class="ling-examples" style="margin-top:0.75rem;margin-bottom:0">
        <div class="ling-examples-label">Alphabetic Forms</div>
        <div class="ling-ex-line"><span class="word">αʹ = 1 &nbsp;·&nbsp; βʹ = 2 &nbsp;·&nbsp; ιʹ = 10 &nbsp;·&nbsp; κʹ = 20 &nbsp;·&nbsp; ρʹ = 100</span></div>
        <div class="ling-ex-line"><span class="word">͵α = 1,000</span><span class="gloss">left keraia marks thousands</span></div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>Alphabetic numerals survive in church contexts, legal documents, and chapter/section numbering in formal Greek texts.</p>
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
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.5rem">Gender Agreement</div>
        <p>"1" and the hundreds agree with the noun's gender. In compound numerals, agreement appears on the final element.</p>
        <div class="ling-examples" style="margin-top:0.65rem;margin-bottom:0">
            <div class="ling-examples-label">Examples</div>
            <div class="ling-ex-line"><span class="word">ένας άντρας</span><span class="gloss">masc.</span></div>
            <div class="ling-ex-line"><span class="word">μία γυναίκα</span><span class="gloss">fem.</span></div>
            <div class="ling-ex-line"><span class="word">ένα παιδί</span><span class="gloss">neut.</span></div>
        </div>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.5rem">Hundreds — Gender Inflection</div>
        <p>Hundreds also inflect for gender, producing distinct masculine, feminine, and neuter forms.</p>
        <div class="ling-examples" style="margin-top:0.65rem;margin-bottom:0">
            <div class="ling-examples-label">διακόσι- inflected</div>
            <div class="ling-ex-line"><span class="word">διακόσιοι άντρες</span><span class="gloss">masc. pl.</span></div>
            <div class="ling-ex-line"><span class="word">διακόσιες γυναίκες</span><span class="gloss">fem. pl.</span></div>
            <div class="ling-ex-line"><span class="word">διακόσια παιδιά</span><span class="gloss">neut. pl.</span></div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.5rem">Plural Noun Interaction</div>
        <p>After numerals greater than 1, nouns appear in the nominative plural form.</p>
        <p style="font-family:'DM Mono',monospace;font-size:0.9rem;color:var(--ink-muted)">δύο βιβλία &nbsp;·&nbsp; πέντε άντρες</p>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.5rem">Case Inflection</div>
        <p>In formal registers, numerals decline for case. Genitive forms are most common in modern usage.</p>
        <p style="font-family:'DM Mono',monospace;font-size:0.9rem;color:var(--ink-muted)">του ενός &nbsp;·&nbsp; των δύο</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Ordinals ──────────────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Ordinal Formation</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Ordinals in Greek decline fully for gender, number, and case — they behave as full adjectives. The first few ordinals are suppletive.</p>
    <div class="ling-morph-table" style="margin-top:0.75rem">
        <div class="ling-morph-row">
            <span class="ling-morph-source">1st</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">πρώτος</span>
            <span class="ling-morph-gloss">suppletive</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">2nd</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">δεύτερος</span>
            <span class="ling-morph-gloss">suppletive</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">3rd</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">τρίτος</span>
            <span class="ling-morph-gloss"></span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">4th</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">τέταρτος</span>
            <span class="ling-morph-gloss"></span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">5th</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">πέμπτος</span>
            <span class="ling-morph-gloss"></span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Morphological Summary ────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Morphological Summary</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.5rem">Cardinals</div>
        <ul>
            <li>Gender agreement on 1 and hundreds</li>
            <li>Large magnitudes (millions) behave as nouns</li>
            <li>Thousands (<em>χίλια</em>) use neuter plural form</li>
            <li>Case marking present in formal registers</li>
        </ul>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.5rem">Ordinals</div>
        <ul>
            <li>Fully adjectival — decline for gender, number, case</li>
            <li>First two ordinals are suppletive</li>
            <li>Agreement on the final element in compounds</li>
            <li><em>διακόσια τριάντα τρία βιβλία</em> — agreement on final unit</li>
        </ul>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# NAVIGATION
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="ling-nav-footer">
    <a class="ling-nav-btn" href="/Greek_Converter">← Greek Converter</a>
    <a class="ling-nav-btn active" href="/Greek_Linguistics">Greek Linguistics</a>
</div>
""", unsafe_allow_html=True)
home_nav()