import streamlit as st
from ui import apply_global_styles

st.set_page_config(page_title="The Number System Repository", layout="wide")
apply_global_styles()

# ── HOME-SPECIFIC STYLES ──────────────────────────────────────
st.markdown("""
<style>
/* ── HERO (hoverable card) ── */
.nsr-hero {
    position: relative;
    padding: 3.5rem 3.5rem 3rem 3.5rem;
    margin-bottom: 2.5rem;
    background: linear-gradient(135deg, rgba(255,255,255,.97) 0%, var(--parchment-2) 100%);
    border: 1px solid var(--card-border);
    border-top: 3px solid var(--ink);
    border-radius: 8px;
    overflow: hidden;
    box-shadow:
        0 1px 3px rgba(26,22,18,.05),
        0 8px 28px rgba(26,22,18,.07),
        inset 0 1px 0 rgba(255,255,255,.85);
    transition: transform .28s cubic-bezier(.4,0,.2,1),
                box-shadow .28s cubic-bezier(.4,0,.2,1),
                border-color .28s ease;
}
.nsr-hero:hover {
    transform: translateY(-3px);
    border-color: rgba(26,22,18,.17);
    box-shadow:
        0 2px 6px rgba(26,22,18,.06),
        0 16px 44px rgba(26,22,18,.12),
        inset 0 1px 0 rgba(255,255,255,.92);
}
.nsr-hero::before {
    content: "∑";
    position: absolute;
    right: 3rem; top: 50%;
    transform: translateY(-50%);
    font-family: 'Crimson Pro', Georgia, serif;
    font-size: 16rem; font-weight: 700;
    color: rgba(26,22,18,0.035);
    line-height: 1;
    pointer-events: none; user-select: none;
    transition: color .3s ease, transform .3s cubic-bezier(.4,0,.2,1);
}
.nsr-hero:hover::before {
    color: rgba(184,92,56,.085);
    transform: translateY(-50%) scale(1.05);
}
.nsr-hero-eyebrow {
    font-family: 'DM Sans', sans-serif;
    font-size: .72rem; font-weight: 700;
    text-transform: uppercase; letter-spacing: .18em;
    color: var(--accent);
    margin-bottom: 1rem;
    display: flex; align-items: center; gap: .75rem;
}
.nsr-hero-eyebrow::before {
    content: ''; display: inline-block;
    width: 2rem; height: 1.5px; background: var(--accent);
}
.nsr-hero-title {
    font-family: 'Crimson Pro', Georgia, serif;
    font-size: 4.2rem; font-weight: 700;
    color: var(--ink); line-height: 1.05;
    letter-spacing: -0.04em;
    margin-bottom: 1rem; max-width: 780px;
}
.nsr-hero-sub {
    font-family: 'Crimson Pro', Georgia, serif;
    font-size: 1.2rem; font-style: italic;
    color: var(--ink-muted); line-height: 1.65;
    max-width: 580px; margin-bottom: 1.75rem;
}
.nsr-chips { display: flex; gap: .45rem; flex-wrap: wrap; }
.nsr-chip {
    font-family: 'DM Sans', sans-serif;
    font-size: .68rem; font-weight: 600;
    letter-spacing: .08em; text-transform: uppercase;
    padding: .22rem .7rem; border-radius: 2px;
    color: var(--ink-muted); background: var(--parchment-3);
    border: none; cursor: default;
    user-select: none; pointer-events: none;
}
.nsr-chip.link {
    cursor: pointer; pointer-events: auto;
    border: 1.5px solid var(--rule-strong);
    background: transparent;
    text-decoration: none !important;
    transition: all .18s ease;
}
.nsr-chip.link:hover {
    background: var(--ink); color: var(--parchment);
    border-color: var(--ink);
    text-decoration: none !important;
}

/* ── SECTION LABEL ── */
.nsr-section-label {
    font-family: 'DM Sans', sans-serif;
    font-size: .7rem; font-weight: 700;
    text-transform: uppercase; letter-spacing: .16em;
    color: var(--ink-faint);
    margin-bottom: 1.25rem; margin-top: 2.75rem;
    display: flex; align-items: center; gap: 1rem;
}
.nsr-section-label::after { content: ''; flex: 1; height: 1px; background: var(--rule); }

/* ── FAMILY HEADING ── */
.nsr-family-heading {
    display: flex; align-items: baseline; gap: .75rem;
    margin-bottom: .85rem;
    padding-bottom: .5rem;
    border-bottom: 1px solid var(--rule);
}
.nsr-family-name {
    font-family: 'Crimson Pro', Georgia, serif;
    font-size: 1.35rem; font-weight: 600;
    color: var(--ink); letter-spacing: -.02em;
}
.nsr-family-count {
    font-family: 'DM Sans', sans-serif;
    font-size: .7rem; font-weight: 600;
    letter-spacing: .08em; text-transform: uppercase;
    color: var(--ink-faint);
}

/* ── LANGUAGE TILE GRID ── */
/* auto-fit (not auto-fill) collapses empty tracks, so a row of 3 tiles
   stretches to fill the full width instead of leaving dead space at right */
.nsr-lang-tiles {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1rem;
    margin-bottom: 2.5rem;
}
@media (max-width: 900px) {
    .nsr-lang-tiles { grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); }
}
.nsr-tile {
    display: flex; flex-direction: column;
    justify-content: space-between;
    padding: 1.6rem 1.8rem 1.35rem 1.8rem;
    min-height: 145px;
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 6px;
    text-decoration: none !important;
    cursor: pointer;
    transition: all .22s cubic-bezier(.4,0,.2,1);
    box-shadow: 0 1px 3px rgba(26,22,18,.04), inset 0 1px 0 rgba(255,255,255,.6);
    position: relative; overflow: hidden;
}
.nsr-tile::before {
    content: '';
    position: absolute; left: 0; top: 0; bottom: 0;
    width: 0;
    background: var(--accent);
    transition: width .22s cubic-bezier(.4,0,.2,1);
    border-radius: 6px 0 0 6px;
}
.nsr-tile:hover::before { width: 3px; }
.nsr-tile:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 22px rgba(26,22,18,.10);
    border-color: rgba(26,22,18,.17);
    background: rgba(255,255,255,.98);
    text-decoration: none !important;
}
.nsr-tile-name {
    font-family: 'Crimson Pro', Georgia, serif;
    font-size: 1.6rem; font-weight: 600;
    color: var(--ink); letter-spacing: -.02em;
    margin-bottom: .35rem; line-height: 1.15;
}
.nsr-tile-meta {
    font-family: 'DM Sans', sans-serif;
    font-size: .72rem; font-weight: 500;
    color: var(--ink-faint);
    text-transform: uppercase; letter-spacing: .07em;
    line-height: 1.35;
}
.nsr-tile-arrow {
    font-size: 1.1rem; color: var(--accent);
    opacity: 0; transition: opacity .2s ease, transform .2s ease;
    margin-top: .6rem; align-self: flex-end;
}
.nsr-tile:hover .nsr-tile-arrow { opacity: 1; transform: translateX(3px); }

/* ── PURPOSE BLOCK ── */
.nsr-purpose {
    display: flex; gap: 1.75rem;
    padding: 1.6rem 2rem;
    background: var(--parchment-2);
    border: 1px solid var(--rule);
    border-left: 3px solid var(--accent);
    border-radius: 4px;
    margin-bottom: 2.5rem;
}
.nsr-purpose-icon { font-size: 2rem; line-height: 1; flex-shrink: 0; margin-top: .1rem; }
.nsr-purpose-text { max-width: 90ch; font-family: 'Crimson Pro', Georgia, serif; font-size: 1.15rem; font-style: italic; color: var(--ink-soft); line-height: 1.7; }
.nsr-purpose-text strong { font-style: normal; font-weight: 600; color: var(--ink); }

/* ── OLYMPIAD CARD ── */
.nsr-olympiad {
    position: relative;
    padding: 2.5rem 3rem;
    margin: .5rem 0 2rem 0;
    background: var(--ink);
    border-radius: 6px;
    color: var(--parchment);
    overflow: hidden;
    box-shadow: 6px 6px 0 var(--accent);
    transition: all .25s cubic-bezier(.4,0,.2,1);
}
.nsr-olympiad:hover { box-shadow: 10px 10px 0 var(--accent); transform: translate(-2px,-2px); }
.nsr-olympiad::before {
    content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
    background-image: repeating-linear-gradient(0deg, rgba(250,247,242,.04) 0px, rgba(250,247,242,.04) 1px, transparent 1px, transparent 28px);
    pointer-events: none;
}
.nsr-olympiad-eyebrow { font-family: 'DM Sans', sans-serif; font-size: .7rem; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; color: var(--accent-light); margin-bottom: .85rem; }
.nsr-olympiad-title { font-family: 'Crimson Pro', Georgia, serif; font-size: 2.5rem; font-weight: 700; color: var(--parchment); line-height: 1.1; letter-spacing: -.03em; margin-bottom: .6rem; }
.nsr-olympiad-sub { font-family: 'Crimson Pro', Georgia, serif; font-size: 1.1rem; font-style: italic; color: rgba(250,247,242,.7); margin-bottom: 1.75rem; max-width: 520px; }
.nsr-olympiad-stats { display: flex; gap: 2.5rem; flex-wrap: wrap; }
.nsr-stat { display: flex; flex-direction: column; gap: .15rem; }
.nsr-stat-num { font-family: 'Crimson Pro', Georgia, serif; font-size: 2rem; font-weight: 700; color: var(--parchment); line-height: 1; letter-spacing: -.03em; }
.nsr-stat-label { font-family: 'DM Sans', sans-serif; font-size: .7rem; font-weight: 600; letter-spacing: .1em; text-transform: uppercase; color: rgba(250,247,242,.5); }
.nsr-olympiad-cta {
    display: inline-flex; align-items: center; gap: .6rem;
    margin-top: 1.75rem;
    font-family: 'DM Sans', sans-serif; font-size: .82rem; font-weight: 700;
    letter-spacing: .1em; text-transform: uppercase;
    color: var(--ink); background: var(--parchment);
    padding: .7rem 1.5rem; border-radius: 3px;
    border: 2px solid var(--parchment);
    text-decoration: none;
    transition: all .2s cubic-bezier(.4,0,.2,1);
    box-shadow: 3px 3px 0 var(--accent);
}
.nsr-olympiad-cta:hover {
    background: transparent; color: var(--parchment) !important;
    border-color: var(--parchment);
    box-shadow: 5px 5px 0 var(--accent);
    transform: translate(-1px,-1px);
    text-decoration: none !important;
}
</style>
""", unsafe_allow_html=True)

# ── HERO ──────────────────────────────────────────────────────
st.markdown("""
<div class="nsr-hero">
    <div class="nsr-hero-eyebrow">Number Systems Studio</div>
    <div class="nsr-hero-title">How cultures count, speak, and reason with numbers.</div>
    <div class="nsr-hero-sub">
        A structured repository combining numeral converters, linguistic grammars,
        and Olympiad-style problems — built for deep learning and careful exploration.
    </div>
    <div class="nsr-chips">
        <span class="nsr-chip">Converters</span>
        <span class="nsr-chip">Linguistics</span>
        <span class="nsr-chip">Olympiad Problems</span>
        <span class="nsr-chip">19 Languages</span>
        <span class="nsr-chip">7 Families</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── PURPOSE ───────────────────────────────────────────────────
st.markdown("""
<div class="nsr-purpose">
    <div class="nsr-purpose-icon">§</div>
    <div class="nsr-purpose-text">
        Explore how different cultures represent numbers.
        Each entry pairs a working <strong>converter</strong> with an explanation of the numeral grammar,
        alongside problems drawn from real linguistics olympiads.
    </div>
</div>
""", unsafe_allow_html=True)

# ── OLYMPIAD CARD ─────────────────────────────────────────────
st.markdown('<div class="nsr-section-label">Featured</div>', unsafe_allow_html=True)
st.markdown("""
<div class="nsr-olympiad">
    <div class="nsr-olympiad-eyebrow">Competition Repository</div>
    <div class="nsr-olympiad-title">Olympiad Problems</div>
    <div class="nsr-olympiad-sub">
        Curated problems from IOL, UKLO, NACLO, PLO and other linguistics olympiads —
        with full worked solutions.
    </div>
    <div class="nsr-olympiad-stats">
        <div class="nsr-stat"><div class="nsr-stat-num">13</div><div class="nsr-stat-label">Problems</div></div>
        <div class="nsr-stat"><div class="nsr-stat-num">5</div><div class="nsr-stat-label">Competitions</div></div>
        <div class="nsr-stat"><div class="nsr-stat-num">3</div><div class="nsr-stat-label">Difficulty levels</div></div>
    </div>
    <a class="nsr-olympiad-cta" href="/Olympiad_Problems" target="_self">Enter the Problems Repository →</a>
</div>
""", unsafe_allow_html=True)

# ── LANGUAGE FAMILIES ─────────────────────────────────────────
st.markdown('<div class="nsr-section-label">Language Families</div>', unsafe_allow_html=True)

st.markdown("""
<div class="nsr-family-heading">
    <span class="nsr-family-name">Sino-Tibetan &amp; East Asian</span>
    <span class="nsr-family-count">3 languages</span>
</div>
<div class="nsr-lang-tiles">
    <a class="nsr-tile" href="/Chinese_Converter" target="_self">
        <div class="nsr-tile-name">Chinese</div>
        <div class="nsr-tile-meta">Sino-Tibetan · Decimal</div>
        <div class="nsr-tile-arrow">→</div>
    </a>
    <a class="nsr-tile" href="/Tibetan_Converter" target="_self">
        <div class="nsr-tile-name">Tibetan</div>
        <div class="nsr-tile-meta">Sino-Tibetan · Decimal</div>
        <div class="nsr-tile-arrow">→</div>
    </a>
    <a class="nsr-tile" href="/Thai_Converter" target="_self">
        <div class="nsr-tile-name">Thai</div>
        <div class="nsr-tile-meta">Sino-Tibetan · Decimal</div>
        <div class="nsr-tile-arrow">→</div>
    </a>
</div>

<div class="nsr-family-heading">
    <span class="nsr-family-name">Niger-Congo — Africa</span>
    <span class="nsr-family-count">3 languages</span>
</div>
<div class="nsr-lang-tiles">
    <a class="nsr-tile" href="/Yoruba_Converter" target="_self">
        <div class="nsr-tile-name">Yoruba</div>
        <div class="nsr-tile-meta">Niger-Congo · Vigesimal</div>
        <div class="nsr-tile-arrow">→</div>
    </a>
    <a class="nsr-tile" href="/Igbo_Converter" target="_self">
        <div class="nsr-tile-name">Igbo</div>
        <div class="nsr-tile-meta">Niger-Congo · Decimal</div>
        <div class="nsr-tile-arrow">→</div>
    </a>
    <a class="nsr-tile" href="/Swahili_Converter" target="_self">
        <div class="nsr-tile-name">Swahili</div>
        <div class="nsr-tile-meta">Niger-Congo · Decimal</div>
        <div class="nsr-tile-arrow">→</div>
    </a>
</div>

<div class="nsr-family-heading">
    <span class="nsr-family-name">Indo-Aryan &amp; Dravidian</span>
    <span class="nsr-family-count">3 languages</span>
</div>
<div class="nsr-lang-tiles">
    <a class="nsr-tile" href="/Hindi_Converter" target="_self">
        <div class="nsr-tile-name">Hindi</div>
        <div class="nsr-tile-meta">Indo-Aryan · Decimal</div>
        <div class="nsr-tile-arrow">→</div>
    </a>
    <a class="nsr-tile" href="/Bengali_Converter" target="_self">
        <div class="nsr-tile-name">Bengali</div>
        <div class="nsr-tile-meta">Indo-Aryan · Decimal</div>
        <div class="nsr-tile-arrow">→</div>
    </a>
    <a class="nsr-tile" href="/Tamil_Converter" target="_self">
        <div class="nsr-tile-name">Tamil</div>
        <div class="nsr-tile-meta">Dravidian · Decimal</div>
        <div class="nsr-tile-arrow">→</div>
    </a>
</div>

<div class="nsr-family-heading">
    <span class="nsr-family-name">Ancient &amp; Classical</span>
    <span class="nsr-family-count">3 languages</span>
</div>
<div class="nsr-lang-tiles">
    <a class="nsr-tile" href="/Roman_Converter" target="_self">
        <div class="nsr-tile-name">Roman</div>
        <div class="nsr-tile-meta">Ancient · Subtractive</div>
        <div class="nsr-tile-arrow">→</div>
    </a>
    <a class="nsr-tile" href="/Greek_Converter" target="_self">
        <div class="nsr-tile-name">Greek</div>
        <div class="nsr-tile-meta">Ancient · Alphabetic</div>
        <div class="nsr-tile-arrow">→</div>
    </a>
    <a class="nsr-tile" href="/Hebrew_Converter" target="_self">
        <div class="nsr-tile-name">Hebrew</div>
        <div class="nsr-tile-meta">Ancient · Alphabetic</div>
        <div class="nsr-tile-arrow">→</div>
    </a>
</div>
""", unsafe_allow_html=True)

# ── OTHER SYSTEMS ─────────────────────────────────────────────
st.markdown('<div class="nsr-section-label">Other Systems</div>', unsafe_allow_html=True)

st.markdown("""
<div class="nsr-family-heading">
    <span class="nsr-family-name">Independent Systems</span>
    <span class="nsr-family-count">1 language</span>
</div>
<div class="nsr-lang-tiles">
    <a class="nsr-tile" href="/Basque_Converter" target="_self">
        <div class="nsr-tile-name">Basque</div>
        <div class="nsr-tile-meta">Language isolate · Vigesimal</div>
        <div class="nsr-tile-arrow">→</div>
    </a>
</div>

<div class="nsr-family-heading">
    <span class="nsr-family-name">Pacific &amp; Americas</span>
    <span class="nsr-family-count">3 languages</span>
</div>
<div class="nsr-lang-tiles">
    <a class="nsr-tile" href="/Inuktitut_Converter" target="_self">
        <div class="nsr-tile-name">Inuktitut</div>
        <div class="nsr-tile-meta">Eskimo-Aleut · Vigesimal</div>
        <div class="nsr-tile-arrow">→</div>
    </a>
    <a class="nsr-tile" href="/Yupik_Converter" target="_self">
        <div class="nsr-tile-name">Yupik</div>
        <div class="nsr-tile-meta">Eskimo-Aleut · Vigesimal</div>
        <div class="nsr-tile-arrow">→</div>
    </a>
    <a class="nsr-tile" href="/Quechua_Converter" target="_self">
        <div class="nsr-tile-name">Quechua</div>
        <div class="nsr-tile-meta">Quechuan · Decimal</div>
        <div class="nsr-tile-arrow">→</div>
    </a>
</div>

<div class="nsr-family-heading">
    <span class="nsr-family-name">Constructed Languages</span>
    <span class="nsr-family-count">3 languages</span>
</div>
<div class="nsr-lang-tiles">
    <a class="nsr-tile" href="/Esperanto_Converter" target="_self">
        <div class="nsr-tile-name">Esperanto</div>
        <div class="nsr-tile-meta">Constructed · Decimal</div>
        <div class="nsr-tile-arrow">→</div>
    </a>
    <a class="nsr-tile" href="/Klingon_Converter" target="_self">
        <div class="nsr-tile-name">Klingon</div>
        <div class="nsr-tile-meta">Constructed · Senary (base-6)</div>
        <div class="nsr-tile-arrow">→</div>
    </a>
    <a class="nsr-tile" href="/High_Valyrian_Converter" target="_self">
        <div class="nsr-tile-name">High Valyrian</div>
        <div class="nsr-tile-meta">Constructed · Decimal</div>
        <div class="nsr-tile-arrow">→</div>
    </a>
</div>
""", unsafe_allow_html=True)

# ── FOOTER ────────────────────────────────────────────────────
st.markdown("---")
st.caption(
    "Numeral systems explored for linguistic structure, cultural context, and Olympiad-level problem solving. "
    "Converter algorithms by Yi Zou. Data sourced from Omniglot, Wikipedia, and primary linguistic references."
)
