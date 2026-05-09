import streamlit as st
from ui import apply_global_styles, home_nav

st.set_page_config(page_title="High Valyrian Numerals — Linguistics", layout="centered")
apply_global_styles()

LING_CSS = """<style>
.ling-masthead{border-top:3px solid var(--ink);border-bottom:1px solid var(--rule);padding:1.75rem 0 1.4rem 0;margin-bottom:1.75rem}
.ling-masthead-eyebrow{font-family:'DM Sans',sans-serif;font-size:.68rem;font-weight:700;text-transform:uppercase;letter-spacing:.18em;color:var(--accent);display:flex;align-items:center;gap:.65rem;margin-bottom:.65rem}
.ling-masthead-eyebrow::before{content:'';display:inline-block;width:1.75rem;height:1.5px;background:var(--accent);flex-shrink:0}
.ling-masthead-title{font-family:'Crimson Pro',Georgia,serif;font-size:3rem;font-weight:700;color:var(--ink);letter-spacing:-.04em;line-height:1.05;margin-bottom:.9rem}
.ling-tags{display:flex;flex-wrap:wrap;gap:.45rem}
.ling-tag{font-family:'DM Sans',sans-serif;font-size:.68rem;font-weight:600;letter-spacing:.07em;text-transform:uppercase;padding:.22rem .7rem;border:1.5px solid var(--rule-strong);border-radius:2px;color:var(--ink-soft);background:transparent}
.ling-section-label{font-family:'DM Sans',sans-serif;font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.16em;color:var(--ink-soft);display:flex;align-items:center;gap:1rem;margin:2.25rem 0 1.1rem 0}
.ling-section-label::before{content:'';display:inline-block;width:2rem;height:1px;background:var(--ink-muted);flex-shrink:0}
.ling-section-label::after{content:'';flex:1;height:1px;background:var(--rule)}
.ling-section-title{font-family:'Crimson Pro',Georgia,serif;font-size:1.85rem;font-weight:600;color:var(--ink);letter-spacing:-.025em;line-height:1.15;margin-bottom:1.1rem;padding-bottom:.45rem;border-bottom:1px solid var(--rule)}
.ling-subsection-title{font-family:'Crimson Pro',Georgia,serif;font-size:1.25rem;font-weight:600;color:var(--ink-soft);letter-spacing:-.01em;margin-bottom:.7rem;margin-top:0}
.ling-card{background:var(--card-bg);border:1px solid var(--card-border);border-radius:5px;padding:1.3rem 1.55rem;margin-bottom:.85rem;box-shadow:0 1px 3px rgba(26,22,18,.05),0 3px 10px rgba(26,22,18,.04),inset 0 1px 0 rgba(255,255,255,.65)}
.ling-card p,.ling-card li{font-family:'Crimson Pro',Georgia,serif;font-size:1.08rem;color:var(--ink-soft);line-height:1.72;margin-bottom:.45rem}
.ling-card p:last-child,.ling-card li:last-child{margin-bottom:0}
.ling-card ul{padding-left:1.3rem;margin:0}
.ling-card li::marker{color:var(--accent)}
.ling-callout{background:var(--accent-pale);border:1px solid rgba(184,92,56,.2);border-left:3px solid var(--accent);border-radius:4px;padding:1.05rem 1.45rem;margin-bottom:.85rem}
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
.ling-props{display:grid;grid-template-columns:auto 1fr;gap:.5rem 1.25rem;align-items:baseline;margin:0;padding:0}
.ling-prop-key{font-family:'DM Sans',sans-serif;font-size:.68rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--ink-faint);white-space:nowrap}
.ling-prop-val{font-family:'Crimson Pro',Georgia,serif;font-size:1.05rem;color:var(--ink-soft);line-height:1.45}
.ling-prop-val strong{color:var(--ink);font-weight:600}
.ling-nav-footer{display:flex;gap:.75rem;padding:1.4rem 0 .5rem 0;border-top:1px solid var(--rule);margin-top:2.5rem;flex-wrap:wrap}
.ling-nav-btn{font-family:'DM Sans',sans-serif;font-size:.78rem;font-weight:700;text-transform:uppercase;letter-spacing:.09em;color:var(--ink);background:var(--parchment-2);border:1.5px solid var(--rule-strong);border-radius:3px;padding:.55rem 1.1rem;text-decoration:none;display:inline-flex;align-items:center;gap:.4rem;white-space:nowrap;cursor:pointer;box-shadow:2px 2px 0 rgba(26,22,18,.08);transition:all .18s cubic-bezier(.4,0,.2,1)}
.ling-nav-btn:hover{background:var(--ink);color:var(--parchment);border-color:var(--ink);box-shadow:3px 3px 0 var(--accent);transform:translate(-1px,-1px);text-decoration:none}
.ling-nav-btn.active{background:var(--parchment-3);color:var(--ink-muted);cursor:default;box-shadow:none}
</style>"""
st.markdown(LING_CSS, unsafe_allow_html=True)

# ── MASTHEAD ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="ling-masthead">
    <div class="ling-masthead-eyebrow">Linguistic Structure</div>
    <div class="ling-masthead-title">High Valyrian Numerals</div>
    <div class="ling-tags">
        <span class="ling-tag">Constructed Language</span>
        <span class="ling-tag">Limited Canon</span>
        <span class="ling-tag">Inflectional</span>
        <span class="ling-tag">Macron Vowels</span>
        <span class="ling-tag">Range 1–10 only</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── SECTION 1 — SYSTEM OVERVIEW ──────────────────────────────────────────────
st.markdown('<div class="ling-section-label">System Overview</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">A Language With Limited Numbers</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Honest Caveat</div>
    <p>High Valyrian (Valyrio) is the most extensively-developed of the
    languages created for HBO's <em>Game of Thrones</em>, but its numeral
    system is sparse. Numerals 1–10 are documented; <strong>no canonical
    compositional system has been published for numbers above 10</strong>.
    This page restricts itself to the published canon — we do not invent
    forms.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-props">
        <span class="ling-prop-key">Created by</span>
        <span class="ling-prop-val"><strong>David J. Peterson</strong>, 2012 — for HBO's <em>Game of Thrones</em></span>
        <span class="ling-prop-key">Native name</span>
        <span class="ling-prop-val">Valyrio · Valyrio Eglio ("High Valyrian")</span>
        <span class="ling-prop-key">In-fiction status</span>
        <span class="ling-prop-val">Liturgical and historical language of the Targaryen dynasty</span>
        <span class="ling-prop-key">Real-world status</span>
        <span class="ling-prop-val">Active development; Duolingo course since 2017</span>
        <span class="ling-prop-key">Numeral range published</span>
        <span class="ling-prop-val">1–10 attested · 11+ not canonically defined</span>
        <span class="ling-prop-key">Morphology</span>
        <span class="ling-prop-val">Heavily inflectional — numerals likely take case in real use</span>
        <span class="ling-prop-key">Orthography</span>
        <span class="ling-prop-val">Latin-based with macrons (ē, ā, ī, ō, ū) for long vowels; ñ for palatal nasal</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── SECTION 2 — NUMERALS ─────────────────────────────────────────────────────
st.markdown('<div class="ling-section-label">Attested Numerals</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">The Published Forms</div>', unsafe_allow_html=True)

st.table({
    "Number": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Valyrian": ["mēre", "tymptir", "hāre", "rytsas", "tōme",
                 "byssa", "jēdar", "ōñoso", "glaeson", "vōre"],
    "Confidence": ["HIGH", "HIGH", "HIGH",
                   "MEDIUM", "MEDIUM", "MEDIUM",
                   "MEDIUM", "MEDIUM", "MEDIUM", "MEDIUM"],
})

st.markdown("""
<div class="ling-info">
    <p>HIGH-confidence forms (1–3) appear directly in Peterson's published
    materials and the Duolingo course. MEDIUM-confidence forms (4–10) are
    consistent across community sources but with less direct attestation.
    Where a form has dialect variants in the sources (e.g. <em>tymptir</em> /
    <em>tymī</em> in compound contexts), the most commonly cited
    citation form is shown.</p>
</div>
""", unsafe_allow_html=True)

# ── SECTION 3 — PHONOLOGY ────────────────────────────────────────────────────
st.markdown('<div class="ling-section-label">Phonology &amp; Orthography</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Reading the Forms</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Valyrian phonology uses a set of features unfamiliar to many natural
    European languages, including:</p>
    <ul>
        <li><strong>Long vowels marked with macrons</strong> — <em>mēre</em>,
        <em>hāre</em>, <em>tōme</em>, <em>jēdar</em>, <em>ōñoso</em>,
        <em>vōre</em>. Vowel length is phonemic — <em>ē</em> is a different
        phoneme from <em>e</em>.</li>
        <li><strong>The palatal nasal <em>ñ</em></strong> — appears in
        <em>ōñoso</em> ("eight"). Sounds like the Spanish <em>ñ</em> in
        <em>mañana</em>, or the <em>ny</em> in English "canyon."</li>
        <li><strong>Consonant clusters</strong> — <em>tymptir</em> for "two"
        contains the cluster /mpt/, which is phonotactically marked in many
        languages.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>Peterson designed Valyrian's phonology to feel "ancient" and
    "ceremonial" — appropriate for a language whose in-fiction role is
    similar to that of Latin in medieval Europe (a learned, liturgical,
    and high-prestige language no longer in everyday spoken use).</p>
</div>
""", unsafe_allow_html=True)

# ── SECTION 4 — INFLECTION ───────────────────────────────────────────────────
st.markdown('<div class="ling-section-label">Inflection</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Numerals in Sentences</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Caveat for converter use</div>
    <p>This converter shows citation (uninflected) forms only. In actual
    Valyrian sentences, numerals from 1–4 are reported by Peterson to inflect
    for case, number, and gender of the noun they modify, while higher numbers
    behave somewhat like nouns. Specifics for numerals are not fully published —
    inflectional output is intentionally not attempted here.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Valyrian has eight noun classes (referred to as "genders" in Peterson's
    grammar): lunar, solar, terrestrial, aquatic, plus four collective and
    paucal forms. Numerals 1–4 agreeing with a noun should match the noun's
    class — meaning <em>mēre</em> "one" appears in different forms depending
    on whether you are counting dragons, stars, ships, or fires. A complete
    inflectional paradigm for the lower numerals has not been published,
    though Peterson has discussed the system in general terms.</p>
</div>
""", unsafe_allow_html=True)

# ── SECTION 5 — DEVELOPMENT HISTORY ──────────────────────────────────────────
st.markdown('<div class="ling-section-label">Development</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">From Page to Screen to Duolingo</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>George R. R. Martin used a few Valyrian phrases in <em>A Song of Ice
    and Fire</em> (e.g. <em>valar morghulis</em> "all men must die",
    <em>valar dohaeris</em> "all men must serve"), but did not develop a
    grammar. When HBO commissioned a full language for the TV adaptation,
    they hired David J. Peterson, who had earlier built Dothraki for the
    same series.</p>
    <p>Peterson reverse-engineered the canonical phrases into a grammatical
    system, then expanded the language with several thousand vocabulary items.
    The Duolingo High Valyrian course launched in 2017, with Peterson's
    direct involvement, and remains the most accessible introduction.
    Peterson continues to publish material on his blog and via interviews,
    occasionally clarifying or extending the documented language.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>Compared to Esperanto (135 years old, 2 million speakers) or Klingon
    (40 years, an active institute and translated literature), High Valyrian
    is young — but it has the advantage of a steady stream of new content
    from a still-active creator. Its numeral system above 10 may yet receive
    a canonical extension. For now, this converter respects the published
    boundaries.</p>
</div>
""", unsafe_allow_html=True)

# ── NAVIGATION ──────────────────────────────────────────────
st.markdown('<div class="nav-row">', unsafe_allow_html=True)
st.page_link("pages/High_Valyrian_Converter.py", label="← High Valyrian Converter")
st.page_link("Home.py", label="← Home")
st.markdown('</div>', unsafe_allow_html=True)
