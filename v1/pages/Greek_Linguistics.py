import streamlit as st
from ui import apply_global_styles, home_nav, LING_CSS

st.set_page_config(page_title="Greek Numerals — Linguistics", layout="centered")

apply_global_styles()

# ─────────────────────────────────────────────────────────────
# SHARED LINGUISTICS STYLESHEET (identical across all ling pages)
# ─────────────────────────────────────────────────────────────
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

# ── NAVIGATION ──────────────────────────────────────────────
st.markdown('<div class="nav-row">', unsafe_allow_html=True)
st.page_link("pages/Greek_Converter.py", label="← Greek Converter")
st.page_link("Home.py", label="← Home")
st.markdown('</div>', unsafe_allow_html=True)