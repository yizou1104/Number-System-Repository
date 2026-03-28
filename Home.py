import streamlit as st
from ui import apply_global_styles

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(
    page_title="The Number System Repository",
    layout="wide"
)

apply_global_styles()

# --------------------------------------------------
# Page-specific styles — Home only
# --------------------------------------------------
st.markdown(
    """
    <style>
    /* ── HERO ─────────────────────────────────────── */
    .nsr-hero {
        position: relative;
        padding: 3rem 3.5rem;
        margin-bottom: 3rem;
        border-top: 3px solid var(--ink);
        border-bottom: 1px solid var(--rule);
        overflow: hidden;
    }

    .nsr-hero::before {
        content: "∑";
        position: absolute;
        right: 3rem;
        top: 50%;
        transform: translateY(-50%);
        font-family: 'Crimson Pro', Georgia, serif;
        font-size: 14rem;
        font-weight: 700;
        color: rgba(26,22,18,0.04);
        line-height: 1;
        pointer-events: none;
        user-select: none;
    }

    .nsr-hero-eyebrow {
        font-family: 'DM Sans', sans-serif;
        font-size: 0.72rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.18em;
        color: var(--accent);
        margin-bottom: 1.1rem;
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }

    .nsr-hero-eyebrow::before {
        content: '';
        display: inline-block;
        width: 2rem;
        height: 1.5px;
        background: var(--accent);
    }

    .nsr-hero-title {
        font-family: 'Crimson Pro', Georgia, serif;
        font-size: 4rem;
        font-weight: 700;
        color: var(--ink);
        line-height: 1.05;
        letter-spacing: -0.04em;
        margin-bottom: 1.1rem;
        max-width: 720px;
    }

    .nsr-hero-sub {
        font-family: 'Crimson Pro', Georgia, serif;
        font-size: 1.2rem;
        font-style: italic;
        color: var(--ink-muted);
        line-height: 1.65;
        max-width: 580px;
        margin-bottom: 1.75rem;
    }

    .nsr-chips {
        display: flex;
        gap: 0.45rem;
        flex-wrap: wrap;
    }

    /* ── TAGS ─────────────────────────────────────────
       Flat filled chips — no border, no hover, no cursor.
       Deliberately inert so they read as labels, not buttons. */
    .nsr-chip {
        font-family: 'DM Sans', sans-serif;
        font-size: 0.68rem;
        font-weight: 600;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        padding: 0.22rem 0.7rem;
        border-radius: 2px;
        color: var(--ink-muted);
        background: var(--parchment-3);
        border: none;
        cursor: default;
        user-select: none;
        pointer-events: none;
    }

    /* ── SECTION LABEL ────────────────────────────── */
    .nsr-section-label {
        font-family: 'DM Sans', sans-serif;
        font-size: 0.7rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.16em;
        color: var(--ink-faint);
        margin-bottom: 1.5rem;
        margin-top: 2.5rem;
        display: flex;
        align-items: center;
        gap: 1rem;
    }

    .nsr-section-label::after {
        content: '';
        flex: 1;
        height: 1px;
        background: var(--rule);
    }

    /* ── FAMILY HEADER ────────────────────────────── */
    .nsr-family-header {
        display: flex;
        align-items: baseline;
        gap: 1rem;
        margin-bottom: 1.1rem;
        padding-bottom: 0.65rem;
        border-bottom: 1px solid var(--rule);
    }

    .nsr-family-title {
        font-family: 'Crimson Pro', Georgia, serif;
        font-size: 1.45rem;
        font-weight: 600;
        color: var(--ink);
        letter-spacing: -0.02em;
        line-height: 1.2;
    }

    .nsr-family-count {
        font-family: 'DM Sans', sans-serif;
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: var(--ink-faint);
    }

    /* ── LANGUAGE CARD ────────────────────────────── */
    .nsr-lang-card {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0.9rem 1.1rem;
        margin-bottom: 0.5rem;
        background: var(--card-bg);
        border: 1px solid var(--card-border);
        border-radius: 4px;
        cursor: pointer;
        text-decoration: none;
        transition: all 0.22s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 1px 3px rgba(26,22,18,0.05);
        position: relative;
        overflow: hidden;
    }

    .nsr-lang-card::before {
        content: '';
        position: absolute;
        left: 0; top: 0; bottom: 0;
        width: 0;
        background: var(--accent);
        transition: width 0.22s cubic-bezier(0.4, 0, 0.2, 1);
        border-radius: 4px 0 0 4px;
    }

    .nsr-lang-card:hover::before { width: 3px; }

    .nsr-lang-card:hover {
        transform: translateY(-2px) translateX(2px);
        box-shadow: 0 6px 20px rgba(26,22,18,0.10);
        border-color: rgba(26,22,18,0.18);
        background: rgba(255,255,255,0.98);
    }

    .nsr-lang-name {
        font-family: 'Crimson Pro', Georgia, serif;
        font-size: 1.1rem;
        font-weight: 500;
        color: var(--ink);
        letter-spacing: -0.01em;
    }

    .nsr-lang-arrow {
        font-family: 'DM Sans', sans-serif;
        font-size: 0.8rem;
        color: var(--ink-faint);
        opacity: 0;
        transform: translateX(-6px);
        transition: all 0.2s ease;
    }

    .nsr-lang-card:hover .nsr-lang-arrow {
        opacity: 1;
        transform: translateX(0);
    }

    /* ── FAMILY CARD WRAPPER ──────────────────────── */
    .nsr-family-card {
        background: var(--parchment);
        border: 1px solid var(--card-border);
        border-radius: 6px;
        padding: 1.5rem 1.6rem;
        box-shadow:
            0 1px 3px rgba(26,22,18,0.05),
            0 4px 16px rgba(26,22,18,0.04),
            inset 0 1px 0 rgba(255,255,255,0.6);
        transition: box-shadow 0.25s ease;
        height: 100%;
    }

    .nsr-family-card:hover {
        box-shadow:
            0 2px 6px rgba(26,22,18,0.07),
            0 10px 28px rgba(26,22,18,0.08),
            inset 0 1px 0 rgba(255,255,255,0.8);
    }

    /* ── OLYMPIAD CARD ────────────────────────────── */
    .nsr-olympiad {
        position: relative;
        padding: 2.5rem 3rem;
        margin: 1rem 0 2rem 0;
        background: var(--ink);
        border-radius: 6px;
        color: var(--parchment);
        overflow: hidden;
        box-shadow: 6px 6px 0 var(--accent);
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .nsr-olympiad:hover {
        box-shadow: 10px 10px 0 var(--accent);
        transform: translate(-2px, -2px);
    }

    .nsr-olympiad::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background-image:
            repeating-linear-gradient(
                0deg,
                rgba(250,247,242,0.04) 0px,
                rgba(250,247,242,0.04) 1px,
                transparent 1px,
                transparent 28px
            );
        pointer-events: none;
    }

    .nsr-olympiad-eyebrow {
        font-family: 'DM Sans', sans-serif;
        font-size: 0.7rem;
        font-weight: 700;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        color: var(--accent-light);
        margin-bottom: 0.85rem;
    }

    .nsr-olympiad-title {
        font-family: 'Crimson Pro', Georgia, serif;
        font-size: 2.5rem;
        font-weight: 700;
        color: var(--parchment);
        line-height: 1.1;
        letter-spacing: -0.03em;
        margin-bottom: 0.6rem;
    }

    .nsr-olympiad-sub {
        font-family: 'Crimson Pro', Georgia, serif;
        font-size: 1.1rem;
        font-style: italic;
        color: rgba(250,247,242,0.7);
        margin-bottom: 1.75rem;
        max-width: 520px;
    }

    .nsr-olympiad-stats {
        display: flex;
        gap: 2.5rem;
        flex-wrap: wrap;
    }

    .nsr-stat {
        display: flex;
        flex-direction: column;
        gap: 0.15rem;
    }

    .nsr-stat-num {
        font-family: 'Crimson Pro', Georgia, serif;
        font-size: 2rem;
        font-weight: 700;
        color: var(--parchment);
        line-height: 1;
        letter-spacing: -0.03em;
    }

    .nsr-stat-label {
        font-family: 'DM Sans', sans-serif;
        font-size: 0.7rem;
        font-weight: 600;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: rgba(250,247,242,0.5);
    }

    /* ── OLYMPIAD CTA BUTTON ──────────────────────────
       Sits inside the dark ink card. Parchment fill with
       an explicit 2px parchment border makes the outline
       clearly visible against the dark background.
       On hover: fills transparent, text inverts to parchment,
       so it reads as an outlined ghost button. */
    .nsr-olympiad-cta {
        display: inline-flex;
        align-items: center;
        gap: 0.6rem;
        margin-top: 1.75rem;
        font-family: 'DM Sans', sans-serif;
        font-size: 0.82rem;
        font-weight: 700;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: var(--ink);
        background: var(--parchment);
        padding: 0.7rem 1.5rem;
        border-radius: 3px;
        border: 2px solid var(--parchment);
        text-decoration: none;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 3px 3px 0 var(--accent);
    }

    .nsr-olympiad-cta:hover {
        background: transparent;
        color: var(--parchment) !important;
        border-color: var(--parchment);
        box-shadow: 5px 5px 0 var(--accent);
        transform: translate(-1px, -1px);
        text-decoration: none !important;
    }

    /* ── PURPOSE BLOCK ────────────────────────────── */
    .nsr-purpose {
        display: flex;
        gap: 2rem;
        padding: 1.75rem 2rem;
        background: var(--parchment-2);
        border: 1px solid var(--rule);
        border-left: 3px solid var(--accent);
        border-radius: 4px;
        margin-bottom: 2.5rem;
    }

    .nsr-purpose-icon {
        font-size: 2rem;
        line-height: 1;
        flex-shrink: 0;
        margin-top: 0.1rem;
    }

    .nsr-purpose-text {
        font-family: 'Crimson Pro', Georgia, serif;
        font-size: 1.15rem;
        font-style: italic;
        color: var(--ink-soft);
        line-height: 1.7;
    }

    .nsr-purpose-text strong {
        font-style: normal;
        font-weight: 600;
        color: var(--ink);
    }

    /* ── BOTTOM-ROW CARD WRAPPER ──────────────────── */
    .nsr-isolate-wrapper {
        background: var(--parchment);
        border: 1px solid var(--card-border);
        border-radius: 6px;
        padding: 1.5rem 1.6rem;
        box-shadow:
            0 1px 3px rgba(26,22,18,0.05),
            0 4px 16px rgba(26,22,18,0.04),
            inset 0 1px 0 rgba(255,255,255,0.6);
        transition: box-shadow 0.25s ease;
        margin-bottom: 1rem;
    }

    .nsr-isolate-wrapper:hover {
        box-shadow:
            0 2px 6px rgba(26,22,18,0.07),
            0 10px 28px rgba(26,22,18,0.08),
            inset 0 1px 0 rgba(255,255,255,0.8);
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# ──────────────────────────────────────────────────────
# HERO
# ──────────────────────────────────────────────────────
st.markdown(
    """
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
            <span class="nsr-chip">14 Languages</span>
            <span class="nsr-chip">6 Families</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ──────────────────────────────────────────────────────
# PURPOSE
# ──────────────────────────────────────────────────────
st.markdown(
    """
    <div class="nsr-purpose">
        <div class="nsr-purpose-icon">§</div>
        <div class="nsr-purpose-text">
            Explore how different cultures represent numbers — through <strong>script, word, and rule</strong>.
            Each entry pairs a working converter with an explanation of the numeral grammar,
            alongside problems drawn from real linguistics olympiads.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ──────────────────────────────────────────────────────
# OLYMPIAD CARD
# The CTA button is a plain HTML anchor styled via
# .nsr-olympiad-cta — avoids the outline-less st.page_link.
# ──────────────────────────────────────────────────────
st.markdown('<div class="nsr-section-label">Featured</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="nsr-olympiad">
        <div class="nsr-olympiad-eyebrow">Competition Repository</div>
        <div class="nsr-olympiad-title">Olympiad Problems</div>
        <div class="nsr-olympiad-sub">
            Curated problems from IOL, UKLO, NACLO, PLO and other linguistics olympiads —
            with full worked solutions.
        </div>
        <div class="nsr-olympiad-stats">
            <div class="nsr-stat">
                <div class="nsr-stat-num">6</div>
                <div class="nsr-stat-label">Problems</div>
            </div>
            <div class="nsr-stat">
                <div class="nsr-stat-num">5</div>
                <div class="nsr-stat-label">Competitions</div>
            </div>
            <div class="nsr-stat">
                <div class="nsr-stat-num">3</div>
                <div class="nsr-stat-label">Difficulty levels</div>
            </div>
        </div>
        <a class="nsr-olympiad-cta" href="/Olympiad_Problems">
            Enter the Problems Repository →
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")

# ──────────────────────────────────────────────────────
# LANGUAGE FAMILIES — main 2 × 2 grid
# ──────────────────────────────────────────────────────
st.markdown('<div class="nsr-section-label">Language Families</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown(
        """
        <div class="nsr-family-card">
            <div class="nsr-family-header">
                <span class="nsr-family-title">Sino-Tibetan &amp; East Asian</span>
                <span class="nsr-family-count">3 languages</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    with st.container(border=True):
        st.page_link("pages/Chinese_Converter.py",  label="Chinese")
        st.page_link("pages/Tibetan_Converter.py",  label="Tibetan")
        st.page_link("pages/Thai_Converter.py",     label="Thai")

    st.markdown(
        """
        <div class="nsr-family-card">
            <div class="nsr-family-header">
                <span class="nsr-family-title">Niger-Congo — Africa</span>
                <span class="nsr-family-count">3 languages</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    with st.container(border=True):
        st.page_link("pages/Yoruba_Converter.py",  label="Yoruba")
        st.page_link("pages/Igbo_Converter.py",    label="Igbo")
        st.page_link("pages/Swahili_Converter.py", label="Swahili")

with col2:
    st.markdown(
        """
        <div class="nsr-family-card">
            <div class="nsr-family-header">
                <span class="nsr-family-title">Indo-Aryan &amp; Dravidian</span>
                <span class="nsr-family-count">3 languages</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    with st.container(border=True):
        st.page_link("pages/Hindi_Converter.py",   label="Hindi")
        st.page_link("pages/Bengali_Converter.py", label="Bengali")
        st.page_link("pages/Tamil_Converter.py",   label="Tamil")

    st.markdown(
        """
        <div class="nsr-family-card">
            <div class="nsr-family-header">
                <span class="nsr-family-title">Ancient &amp; Classical</span>
                <span class="nsr-family-count">2 languages</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    with st.container(border=True):
        st.page_link("pages/Roman_Converter.py", label="Roman")
        st.page_link("pages/Greek_Converter.py", label="Greek")


# ──────────────────────────────────────────────────────
# BOTTOM ROW — Independent Systems + Indigenous / Pacific
# Placed side-by-side in a matching two-column grid.
# ──────────────────────────────────────────────────────

bot1, bot2 = st.columns(2, gap="large")

with bot1:
    st.markdown(
        """
        <div class="nsr-isolate-wrapper">
            <div class="nsr-family-header">
                <span class="nsr-family-title">Independent Systems</span>
                <span class="nsr-family-count">1 language</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    with st.container(border=True):
        st.page_link(
            "pages/Basque_Converter.py",
            label="Basque",
        )

with bot2:
    st.markdown(
        """
        <div class="nsr-isolate-wrapper">
            <div class="nsr-family-header">
                <span class="nsr-family-title">Indigenous — Pacific &amp; Americas</span>
                <span class="nsr-family-count">3 languages</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    with st.container(border=True):
        st.page_link(
            "pages/Inuktitut_Converter.py",
            label="Inuktitut",
        )
        st.page_link(
            "pages/Yupik_Converter.py",
            label="Yupik",
        )
        st.page_link(
            "pages/Quechua_Converter.py",
            label="Quechua",
        )


# ──────────────────────────────────────────────────────
# FOOTER
# ──────────────────────────────────────────────────────
st.markdown("---")
st.caption(
    "Numeral systems explored for linguistic structure, cultural context, and Olympiad-level problem solving. "
    "Converter algorithms by Yi Zou. Data sourced from Omniglot, Wikipedia, and primary linguistic references."
)