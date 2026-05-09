import streamlit as st
from ui import apply_global_styles, home_nav

st.set_page_config(page_title="Klingon Numerals — Linguistics", layout="centered")
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
    <div class="ling-masthead-title">Klingon Numerals</div>
    <div class="ling-tags">
        <span class="ling-tag">Decimal</span>
        <span class="ling-tag">Constructed Language</span>
        <span class="ling-tag">Magnitude Suffix</span>
        <span class="ling-tag">Case-Sensitive</span>
        <span class="ling-tag">Retconned History</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── SECTION 1 — SYSTEM OVERVIEW ──────────────────────────────────────────────
st.markdown('<div class="ling-section-label">System Overview</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Structural Properties</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Key Fact</div>
    <p>Klingon has no standalone word for "ten" — instead, magnitude is
    expressed by suffixes (<em>maH</em> = 10, <em>vatlh</em> = 100, <em>SaD</em>
    = 1,000) attached directly to digit roots. Compound numbers like
    <em>cha'maH</em> ("two-ten" = 20) are single phonological words formed
    by suffixation, not by separate digit + place-name.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-props">
        <span class="ling-prop-key">Created by</span>
        <span class="ling-prop-val"><strong>Marc Okrand</strong>, 1984 (for <em>Star Trek III</em>)</span>
        <span class="ling-prop-key">Native name</span>
        <span class="ling-prop-val">tlhIngan Hol — "Klingon language"</span>
        <span class="ling-prop-key">System type</span>
        <span class="ling-prop-val">Decimal (post-1992 retcon — see history below)</span>
        <span class="ling-prop-key">Base</span>
        <span class="ling-prop-val">10</span>
        <span class="ling-prop-key">Magnitude marking</span>
        <span class="ling-prop-val">Suffixes attached to digit roots — no standalone "ten"</span>
        <span class="ling-prop-key">Word formation</span>
        <span class="ling-prop-val">Each magnitude unit = one word; multi-magnitude numbers use spaces</span>
        <span class="ling-prop-key">Orthography</span>
        <span class="ling-prop-val">Strictly case-sensitive — capitals denote phonemes</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── SECTION 2 — DIGITS & SUFFIXES ────────────────────────────────────────────
st.markdown('<div class="ling-section-label">Digits &amp; Magnitude Suffixes</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">The Building Blocks</div>', unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title">Digit Roots (0–9)</div>', unsafe_allow_html=True)
st.table({
    "Number": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    "Klingon": ["pagh", "wa'", "cha'", "wej", "loS",
                "vagh", "jav", "Soch", "chorgh", "Hut"],
})

st.markdown("""
<div class="ling-info">
    <p>Note the apostrophe <em>'</em> in <em>wa'</em> and <em>cha'</em> — this
    is the glottal stop, a full consonant in Klingon (not punctuation). Capital
    letters mark distinct phonemes: <em>S</em> is a retroflex sibilant,
    <em>H</em> is a uvular fricative, <em>Q</em> is a different sound from
    <em>q</em>, <em>D</em> is retroflex. The orthography is unforgiving —
    typing "soch" is incorrect; only "Soch" parses as the digit 7.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Magnitude Suffixes</div>', unsafe_allow_html=True)
st.table({
    "Value": ["10", "100", "1,000", "10,000", "100,000", "1,000,000"],
    "Suffix": ["maH", "vatlh", "SaD", "netlh", "bIp", "'uy'"],
})

st.markdown("""
<div class="ling-info">
    <p>Klingon's magnitude system is unique among the languages here:
    powers of ten 10¹–10⁶ each have their own dedicated suffix (no
    grouping by 10⁴ as in Chinese, no decimal-only as in Esperanto).
    The suffix <em>'uy'</em> for "million" begins and ends with glottal stops —
    a phonologically marked form for a phonologically marked magnitude.</p>
</div>
""", unsafe_allow_html=True)

# ── SECTION 3 — COMPOSITIONAL RULES ──────────────────────────────────────────
st.markdown('<div class="ling-section-label">Compositional Rules</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">How Numbers Are Built</div>', unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title">Single Magnitude</div>', unsafe_allow_html=True)
st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[digit] + <em>[suffix]</em> · written as ONE word</span>
</div>
""", unsafe_allow_html=True)
st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Multiplicative</div>
    <div class="ling-ex-line"><span class="num">10</span><span class="word">wa'maH</span><span class="gloss">one-ten</span></div>
    <div class="ling-ex-line"><span class="num">30</span><span class="word">wejmaH</span><span class="gloss">three-ten</span></div>
    <div class="ling-ex-line"><span class="num">200</span><span class="word">cha'vatlh</span><span class="gloss">two-hundred</span></div>
    <div class="ling-ex-line"><span class="num">5,000</span><span class="word">vaghSaD</span><span class="gloss">five-thousand</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Multiple Magnitudes</div>', unsafe_allow_html=True)
st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[high segment] [middle segment] [low segment] · descending order, space-separated</span>
</div>
""", unsafe_allow_html=True)
st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Compound numbers</div>
    <div class="ling-ex-line"><span class="num">21</span><span class="word">cha'maH wa'</span><span class="gloss">two-ten one</span></div>
    <div class="ling-ex-line"><span class="num">234</span><span class="word">cha'vatlh wejmaH loS</span><span class="gloss">two-hundred three-ten four</span></div>
    <div class="ling-ex-line"><span class="num">1,234</span><span class="word">wa'SaD cha'vatlh wejmaH loS</span><span class="gloss">one-thousand two-hundred three-ten four</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>When a magnitude is "skipped" (i.e. that place is zero), no token
    appears in its position. So 101 = <em>wa'vatlh wa'</em> (one-hundred one),
    not <em>wa'vatlh pagh wa'</em>. The zero word <em>pagh</em> appears only
    when the whole number is zero.</p>
</div>
""", unsafe_allow_html=True)

# ── SECTION 4 — HISTORY ──────────────────────────────────────────────────────
st.markdown('<div class="ling-section-label">History</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">The 1992 Retcon</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>In <em>The Klingon Dictionary</em> (1985), Marc Okrand presented a
    relatively conventional decimal numeral system. In the 1992 second-edition
    addendum, he revised it: the numbers in the original edition were now said
    to belong to a "scholarly" or "ceremonial" register, while everyday spoken
    Klingon used the magnitude-suffix system documented here.</p>
    <p>This in-universe explanation lets the language evolve while preserving
    older fan-published material. It is rare in linguistics — natural languages
    don't get retconned — but it reflects the hybrid status of Klingon as a
    crafted artifact maintained over decades by an actively-engaged author.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Cultural framing</div>
    <p>Okrand designed Klingon to feel "alien" and "warlike" through phonology
    (heavy use of guttural consonants, retroflexes, glottal stops) and
    morphology (object-verb-subject word order, agglutinative suffix stacking).
    The numeral system reflects this — magnitude suffixes are dense, sounds
    are harsh, and even the digits themselves include glottal-stopped forms
    like <em>wa'</em>, <em>cha'</em>, and the millions suffix <em>'uy'</em>.</p>
</div>
""", unsafe_allow_html=True)

# ── SECTION 5 — STATUS ───────────────────────────────────────────────────────
st.markdown('<div class="ling-section-label">Community &amp; Status</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">A Living Constructed Language</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Klingon is one of the most-developed fictional languages, sustained by
    the Klingon Language Institute (KLI), founded in 1992. KLI publishes the
    journal <em>HolQeD</em>, organises annual <em>qep'a'</em> meetings, and has
    overseen translations of Shakespeare's <em>Hamlet</em> and <em>Much Ado
    About Nothing</em>, the <em>Tao Te Ching</em>, and <em>Gilgamesh</em> into
    Klingon.</p>
    <p>Estimates of fluent speakers are low — perhaps 20–30 worldwide — but the
    language has a few children raised partially with Klingon, making it one of
    very few constructed languages with native-like learners besides Esperanto.</p>
</div>
""", unsafe_allow_html=True)

# ── NAVIGATION ──────────────────────────────────────────────
st.markdown('<div class="nav-row">', unsafe_allow_html=True)
st.page_link("pages/Klingon_Converter.py", label="← Klingon Converter")
st.page_link("Home.py", label="← Home")
st.markdown('</div>', unsafe_allow_html=True)