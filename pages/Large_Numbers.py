import streamlit as st
from ui import apply_global_styles, LING_CSS, LING_WIDTH_CSS

# ============================================================
# LARGE NUMBER NAMING TRADITIONS
# Comparative page: which values get named, and how.
#
# Four independent traditions for naming high values:
#   - International    3-3-3   (thousand, million, billion ...)
#   - Indian           3-2-2-2 (hazar, lakh, karor, arab ...)
#   - East Asian       4-4-4   (wan, yi, zhao, jing ...)
#   - Mayan Long Count vigesimal, modified to 18 at the second
#                      position so that 20^2 = 360, not 400
#
# Sources: Comrie (2005, p.c. 2026); Chrisomalis (2010) Numerical
# Notation; Menninger (1969) Number Words and Number Symbols;
# Coe & Van Stone (2005) Reading the Maya Glyphs.
# ============================================================

# ── Backend ──────────────────────────────────────────────────────────────────

# Each tradition is a descending list of (value, name) pivots.
SHORT_SCALE = [
    (10**18, "quintillion"), (10**15, "quadrillion"), (10**12, "trillion"),
    (10**9, "billion"), (10**6, "million"), (10**3, "thousand"),
]

LONG_SCALE = [
    (10**18, "trillion"), (10**15, "billiard"), (10**12, "billion"),
    (10**9, "milliard"), (10**6, "million"), (10**3, "thousand"),
]

INDIAN = [
    (10**17, "shankh"), (10**15, "padma"), (10**13, "nil"),
    (10**11, "kharab"), (10**9, "arab"), (10**7, "karor"),
    (10**5, "lakh"), (10**3, "hazar"),
]

EAST_ASIAN = [
    (10**16, "jing"), (10**12, "zhao"), (10**8, "yi"), (10**4, "wan"),
]

EAST_ASIAN_SCRIPT = {
    "jing": ("京", "kei", "gyeong"),
    "zhao": ("兆", "chō", "jo"),
    "yi":   ("億", "oku", "eok"),
    "wan":  ("萬", "man", "man"),
}

# Classical Nahuatl: a PURE vigesimal series, every pivot a true power of 20.
# Stems are given bare; the prefix cem- / cen- means "one", so cempohualli = 20.
# Compare the Mayan Long Count below, which bends the same base for the calendar.
NAHUATL = [
    (64_000_000, "poaltzonxiquipilli"),   # 20 x 400 x 8000
    (3_200_000, "tzonxiquipilli"),        # 400 x 8000
    (160_000, "poalxiquipilli"),          # 20^4
    (8_000, "xiquipilli"),                # 20^3  "a bag"
    (400, "tzontli"),                     # 20^2  "a head of hair"
    (20, "pohualli"),                     # 20^1  "one whole count"
]


def name_by_pivots(n, pivots):
    """Greedy decomposition of n against a descending pivot list."""
    if n == 0:
        return "zero"
    parts = []
    rem = n
    for value, word in pivots:
        if rem >= value:
            count = rem // value
            rem %= value
            parts.append("{:,} {}".format(count, word))
    if rem:
        parts.append("{:,}".format(rem))
    return " ".join(parts)


def group_international(n):
    """123456789 -> 123,456,789"""
    return "{:,}".format(n)


def group_indian(n):
    """123456789 -> 12,34,56,789  (last three digits, then pairs)"""
    s = str(n)
    if len(s) <= 3:
        return s
    head, tail = s[:-3], s[-3:]
    out = []
    while len(head) > 2:
        out.insert(0, head[-2:])
        head = head[:-2]
    if head:
        out.insert(0, head)
    return ",".join(out) + "," + tail


def group_myriad(n):
    """123456789 -> 1,2345,6789  (groups of four from the right)"""
    s = str(n)
    out = []
    while len(s) > 4:
        out.insert(0, s[-4:])
        s = s[:-4]
    if s:
        out.insert(0, s)
    return ",".join(out)


# ── Mayan Long Count ─────────────────────────────────────────────────────────
# Positional and vigesimal, EXCEPT that the second position carries 18 rather
# than 20, so that a tun is 360 days rather than 400 - an approximation to the
# solar year. This is the cultural modification Comrie highlights.
MAYAN_UNITS = [
    ("b'ak'tun", 144000),
    ("k'atun", 7200),
    ("tun", 360),
    ("winal", 20),
    ("k'in", 1),
]


def mayan_long_count(n):
    """Return (dotted notation, [(unit, count, value), ...])."""
    rem = n
    rows = []
    for unit, value in MAYAN_UNITS:
        count = rem // value
        rem %= value
        rows.append((unit, count, value))
    dotted = ".".join(str(c) for _, c, _ in rows)
    return dotted, rows


# ── Page ─────────────────────────────────────────────────────────────────────
st.set_page_config(page_title="Naming Large Numbers — Comparative", layout="wide")
apply_global_styles()
st.markdown(LING_CSS, unsafe_allow_html=True)
st.markdown(LING_WIDTH_CSS, unsafe_allow_html=True)

st.markdown("""
<style>
.xl-grouping { display:flex; flex-direction:column; gap:.55rem; margin:.4rem 0 0 0; }
.xl-grouping-row {
    display:flex; align-items:baseline; gap:1rem; flex-wrap:wrap;
    padding:.6rem .85rem; background:var(--parchment-2);
    border:1px solid var(--rule); border-left:3px solid var(--accent);
    border-radius:0 4px 4px 0;
}
.xl-grouping-label {
    font-family:'DM Sans',sans-serif; font-size:.64rem; font-weight:700;
    letter-spacing:.12em; text-transform:uppercase; color:var(--ink-faint);
    min-width:9.5rem; flex-shrink:0;
}
.xl-grouping-val {
    font-family:'Crimson Pro',Georgia,serif; font-size:1.4rem; font-weight:600;
    color:var(--ink); letter-spacing:.02em; word-break:break-all;
}
.xl-grouping-note {
    font-family:'DM Sans',sans-serif; font-size:.72rem; color:var(--ink-faint);
    margin-left:auto; flex-shrink:0;
}
.xl-result {
    background:rgba(46,107,122,.04); border:1px solid rgba(46,107,122,.18);
    border-left:3px solid var(--teal); border-radius:0 4px 4px 0;
    padding:.75rem 1.1rem; margin-bottom:.6rem;
}
.xl-result-label {
    font-family:'DM Sans',sans-serif; font-size:.6rem; font-weight:700;
    letter-spacing:.14em; text-transform:uppercase; color:var(--teal);
    margin-bottom:.3rem;
}
.xl-result-value {
    font-family:'Crimson Pro',Georgia,serif; font-size:1.08rem;
    color:var(--ink); line-height:1.55; word-break:break-word;
}
.xl-result-sub {
    font-family:'DM Sans',sans-serif; font-size:.74rem; color:var(--ink-faint);
    margin-top:.25rem;
}
.xl-maya {
    font-family:'Crimson Pro',Georgia,serif; font-size:1.9rem; font-weight:700;
    color:var(--ink); letter-spacing:.06em;
}
/* LING_CSS hides .ling-masthead-sub, so this page carries its own */
.xl-sub {
    font-family:'Crimson Pro',Georgia,serif; font-style:italic;
    font-size:1.05rem; color:var(--ink-muted); line-height:1.55;
    max-width:62ch; margin:.15rem 0 .9rem 0;
}
/* borrowed from the converter pages, which are not imported here */
.conv-presets-sublabel {
    font-family:'DM Sans',sans-serif; font-size:.65rem; font-weight:700;
    text-transform:uppercase; letter-spacing:.14em; color:var(--ink-faint);
    margin:0 0 .65rem 0;
}
.conv-error-card {
    background:rgba(184,92,56,.05); border:1px solid rgba(184,92,56,.2);
    border-left:3px solid var(--accent); border-radius:0 4px 4px 0;
    padding:.75rem 1.1rem; margin-top:.8rem;
}
.conv-error-text {
    font-family:'Crimson Pro',Georgia,serif; font-size:1rem;
    color:var(--accent); font-style:italic; margin:0;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="lang-nav-crumb">'
    '<a href="/" target="_self">Home</a>'
    '<span class="sep">›</span>Cross-Linguistic'
    '<span class="sep">›</span>Naming Large Numbers'
    '</div>',
    unsafe_allow_html=True,
)

st.markdown("""
<div class="ling-masthead">
    <div class="ling-masthead-eyebrow">Cross-Linguistic Comparison</div>
    <div class="ling-masthead-title">Naming Large Numbers</div>
    <div class="xl-sub">Which values get a name of their own, and how those names combine — four traditions that answer the question differently.</div>
    <div class="ling-tags">
        <span class="ling-tag">3–3–3</span>
        <span class="ling-tag">3–2–2–2</span>
        <span class="ling-tag">4–4–4</span>
        <span class="ling-tag">Calendrical Base 20</span>
        <span class="ling-tag">Areal Diffusion</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Overview ─────────────────────────────────────────────────────────────────
st.markdown('<div class="ling-section-label">System Overview</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Four Answers to One Question</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Key Fact</div>
    <p>Every numeral system must decide <em>which</em> powers deserve a dedicated word. The
    choice is not arithmetically determined, and the traditions below arrived at four
    different answers — grouping by threes, by a three-then-twos pattern, by fours, and
    by a base-20 scheme bent to fit the solar year.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-props">
        <span class="ling-prop-key">International</span>
        <span class="ling-prop-val">Names 10<sup>3</sup>, then every 10<sup>3</sup> thereafter — <strong>thousand, million, billion</strong></span>
        <span class="ling-prop-key">Indian</span>
        <span class="ling-prop-val">Names 10<sup>3</sup>, then every 10<sup>2</sup> — <strong>hazar, lakh, karor, arab</strong></span>
        <span class="ling-prop-key">East Asian</span>
        <span class="ling-prop-val">Names every 10<sup>4</sup> — <strong>wan, yi, zhao, jing</strong></span>
        <span class="ling-prop-key">Mayan Long Count</span>
        <span class="ling-prop-val">Vigesimal, but 20<sup>2</sup> = <strong>360</strong>, not 400</span>
        <span class="ling-prop-key">Independence</span>
        <span class="ling-prop-val">The Indian, East Asian and Mayan traditions arose independently of one another</span>
        <span class="ling-prop-key">Relative age</span>
        <span class="ling-prop-val">The Indian system long predates the European <em>million</em> series</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Interactive comparison ───────────────────────────────────────────────────
st.markdown('<div class="ling-section-label">Compare</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">One Value, Four Traditions</div>', unsafe_allow_html=True)

presets = [1_00_000, 10_000, 1_000_000, 12_345_678, 1_00_00_000, 144_000, 10**9, 10**12]
preset_labels = ["100,000 (1 lakh)", "10,000 (1 wan)", "1 million", "12,345,678",
                 "10 million (1 karor)", "144,000 (1 b'ak'tun)", "1 billion", "1 trillion"]

st.markdown('<p class="conv-presets-sublabel">Click a value to load it</p>', unsafe_allow_html=True)
pcols = st.columns(4)
for i, (val, lab) in enumerate(zip(presets, preset_labels)):
    if pcols[i % 4].button(lab, key=f"xl_p_{i}", use_container_width=True):
        st.session_state["xl_input"] = str(val)

raw = st.text_input(
    "Enter a whole number",
    key="xl_input",
    placeholder="e.g. 12345678",
    help="Any whole number from 0 up to 10^18.",
)

if raw:
    cleaned = raw.strip().replace(",", "").replace(" ", "")
    if not cleaned.isdigit():
        st.markdown(
            '<div class="conv-error-card"><p class="conv-error-text">'
            'Please enter a whole number (digits only).</p></div>',
            unsafe_allow_html=True,
        )
    elif int(cleaned) > 10**18:
        st.markdown(
            '<div class="conv-error-card"><p class="conv-error-text">'
            'Supported range is 0 to 10<sup>18</sup>.</p></div>',
            unsafe_allow_html=True,
        )
    else:
        n = int(cleaned)

        # --- how the digits get punctuated ---
        st.markdown('<div class="ling-subsection-title">How the digits are grouped</div>',
                    unsafe_allow_html=True)
        st.markdown(f"""
<div class="xl-grouping">
    <div class="xl-grouping-row">
        <span class="xl-grouping-label">International</span>
        <span class="xl-grouping-val">{group_international(n)}</span>
        <span class="xl-grouping-note">groups of 3</span>
    </div>
    <div class="xl-grouping-row">
        <span class="xl-grouping-label">Indian</span>
        <span class="xl-grouping-val">{group_indian(n)}</span>
        <span class="xl-grouping-note">3, then 2s</span>
    </div>
    <div class="xl-grouping-row">
        <span class="xl-grouping-label">East Asian</span>
        <span class="xl-grouping-val">{group_myriad(n)}</span>
        <span class="xl-grouping-note">groups of 4</span>
    </div>
</div>
""", unsafe_allow_html=True)

        # --- how the value is named ---
        st.markdown('<div class="ling-subsection-title">How the value is named</div>',
                    unsafe_allow_html=True)

        left, right = st.columns(2, gap="large")

        with left:
            st.markdown(f"""
<div class="xl-result">
    <div class="xl-result-label">International — short scale</div>
    <div class="xl-result-value">{name_by_pivots(n, SHORT_SCALE)}</div>
    <div class="xl-result-sub">UK, US, and most international usage today</div>
</div>
<div class="xl-result">
    <div class="xl-result-label">International — long scale</div>
    <div class="xl-result-value">{name_by_pivots(n, LONG_SCALE)}</div>
    <div class="xl-result-sub">Still standard across much of continental Europe</div>
</div>
""", unsafe_allow_html=True)

        with right:
            ea = name_by_pivots(n, EAST_ASIAN)
            st.markdown(f"""
<div class="xl-result">
    <div class="xl-result-label">Indian</div>
    <div class="xl-result-value">{name_by_pivots(n, INDIAN)}</div>
    <div class="xl-result-sub">Hindi, Urdu, Bengali and neighbouring languages</div>
</div>
<div class="xl-result">
    <div class="xl-result-label">East Asian — myriad system</div>
    <div class="xl-result-value">{ea}</div>
    <div class="xl-result-sub">Chinese, with cognate forms in Japanese and Korean</div>
</div>
""", unsafe_allow_html=True)

        # --- Mesoamerica: two treatments of the same base ---
        st.markdown('<div class="ling-subsection-title">Mesoamerica — one base, two treatments</div>',
                    unsafe_allow_html=True)
        st.markdown(f"""
<div class="xl-result">
    <div class="xl-result-label">Nahuatl — pure vigesimal</div>
    <div class="xl-result-value">{name_by_pivots(n, NAHUATL)}</div>
    <div class="xl-result-sub">Every pivot a true power of twenty: pohualli 20, tzontli 400,
    xiquipilli 8,000. The prefix cem- means &ldquo;one&rdquo;.</div>
</div>
""", unsafe_allow_html=True)

        dotted, rows = mayan_long_count(n)
        mc1, mc2 = st.columns([1, 2], gap="large")
        with mc1:
            st.markdown(
                f'<div class="xl-result"><div class="xl-result-label">Long Count</div>'
                f'<div class="xl-maya">{dotted}</div>'
                f'<div class="xl-result-sub">b\'ak\'tun.k\'atun.tun.winal.k\'in, '
                f'reading {n:,} as a count of days</div></div>',
                unsafe_allow_html=True,
            )
        with mc2:
            st.table({
                "Unit": [u for u, _, _ in rows],
                "Days": ["{:,}".format(v) for _, _, v in rows],
                "Count": [str(c) for _, c, _ in rows],
            })

# ── Why the systems differ ───────────────────────────────────────────────────
st.markdown('<div class="ling-section-label">Structure</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Where the Pivots Fall</div>', unsafe_allow_html=True)

st.table({
    "Power": ["10³", "10⁴", "10⁵", "10⁶", "10⁷", "10⁸",
              "10⁹", "10¹²", "10¹⁶"],
    "International": ["thousand", "—", "—", "million", "—", "—",
                      "billion", "trillion", "—"],
    "Indian": ["hazar", "—", "lakh", "—", "karor", "—",
               "arab", "—", "—"],
    "East Asian": ["—", "wan", "—", "—", "—", "yi",
                   "—", "zhao", "jing"],
})

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Read the table down a column</div>
    <p>No two traditions name the same set of powers. The International system skips
    10<sup>4</sup> and 10<sup>5</sup> entirely; the Indian system has no single word for a
    million; the East Asian system has none for a thousand-multiple above 10<sup>3</sup>
    until 10<sup>4</sup>. A speaker converting between them is not translating words but
    <em>re-segmenting the number itself</em>.</p>
</div>
""", unsafe_allow_html=True)

# ── East Asian detail ────────────────────────────────────────────────────────
st.markdown('<div class="ling-subsection-title">The myriad series across three languages</div>',
            unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-morph-table">
        <div class="ling-morph-row">
            <span class="ling-morph-source">10⁴</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">萬 / 万</span>
            <span class="ling-morph-gloss">Chinese <em>wàn</em> · Japanese <em>man</em> · Korean <em>man</em></span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">10⁸</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">億 / 亿</span>
            <span class="ling-morph-gloss">Chinese <em>yì</em> · Japanese <em>oku</em> · Korean <em>eok</em></span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">10¹²</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">兆</span>
            <span class="ling-morph-gloss">Chinese <em>zhào</em> · Japanese <em>chō</em> · Korean <em>jo</em></span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">System borrowed, words adapted</div>
    <p>Japanese and Korean took the myriad structure <em>and</em> the Chinese numeral
    morphemes, but pronounce them according to their own phonology. This is borrowing of
    both system and vocabulary — contrast the Tibetan case on the
    <a href="/Numeral_Contact" target="_self">Contact &amp; Transmission</a> page, where the
    structure travelled but the words did not.</p>
</div>
""", unsafe_allow_html=True)

# ── Mayan detail ─────────────────────────────────────────────────────────────
st.markdown('<div class="ling-section-label">Special Conventions</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">When Culture Overrides Arithmetic</div>',
            unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Key Fact</div>
    <p>The Mayan Long Count is vigesimal at every position <em>except the second</em>, where
    the multiplier is 18 rather than 20. A <em>tun</em> is therefore 18 × 20 = 360 days,
    not 20² = 400.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Expected</span>
    <span class="ling-formula-rule">20 × 20 = 400</span>
</div>
<div class="ling-formula">
    <span class="ling-formula-label">Actual</span>
    <span class="ling-formula-rule">18 × 20 = 360 — an approximation to the solar year</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p style="margin:0">The system was used primarily for calendrical reckoning, and the
    irregularity buys a unit close to a year at the cost of arithmetic regularity. It is a
    clear case of a numeral system shaped by what it was <em>for</em> — the cultural
    function leaving a permanent mark on the mathematical structure. Above the
    <em>tun</em>, regular multiplication by 20 resumes.</p>
</div>
""", unsafe_allow_html=True)

# ── The myriad convergence ───────────────────────────────────────────────────
st.markdown('<div class="ling-section-label">Convergence</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Why So Many Traditions Stop at 10,000</div>',
            unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Key Fact</div>
    <p>Ten thousand is the single most widely recognised pivot above a thousand. It was named
    separately in Greek, in Hebrew and Aramaic, and — with no possibility of contact
    — in Chinese. The international 3–3–3 system is in this respect the
    outlier, not the norm.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-morph-table">
        <div class="ling-morph-row">
            <span class="ling-morph-source">Greek</span>
            <span class="ling-morph-arrow">·</span>
            <span class="ling-morph-target">μύριοι <em>myrioi</em></span>
            <span class="ling-morph-gloss">10⁴ — the source of English <em>myriad</em></span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">Hebrew</span>
            <span class="ling-morph-arrow">·</span>
            <span class="ling-morph-target"><em>revava</em></span>
            <span class="ling-morph-gloss">10⁴, with cognates across Aramaic</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">Chinese</span>
            <span class="ling-morph-arrow">·</span>
            <span class="ling-morph-target">萬 <em>wàn</em></span>
            <span class="ling-morph-gloss">10⁴ — and the whole system built on it</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">Tibetan</span>
            <span class="ling-morph-arrow">·</span>
            <span class="ling-morph-target"><em>khri</em></span>
            <span class="ling-morph-gloss">10⁴, within the Indic-derived scheme</span>
        </div>
    </div>
    <p style="margin:.85rem 0 0 0">The Greek and Semitic traditions were in contact and may
    not be independent of one another, but the Chinese myriad certainly is. Where a tradition
    treats 10<sup>4</sup> as a unit, the square of that unit tends to follow: Chinese names
    10<sup>8</sup> as <em>yì</em>, and Archimedes built the <em>Sand Reckoner</em> on the
    &ldquo;myriad myriad&rdquo;, 10<sup>8</sup>, as the base of a scheme for counting the
    grains of sand that would fill the universe.</p>
</div>
""", unsafe_allow_html=True)

# ── Further traditions ───────────────────────────────────────────────────────
st.markdown('<div class="ling-section-label">Further Traditions</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Beyond the Main Four</div>', unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title">Sanskrit — the deepest named series</div>',
            unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>The modern Indian series stops at everyday values, but the classical Sanskrit
    tradition continued far past them, naming successive powers well beyond any practical
    counting need. Buddhist and Jain cosmological texts extend the sequence further still,
    into powers that exist purely to express scale.</p>
    <p style="margin-bottom:0">This is the tradition that later travelled east, reaching
    Tibetan as a <em>pattern</em> rather than as vocabulary — see the
    <a href="/Numeral_Contact" target="_self">Contact &amp; Transmission</a> repository.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title">Tibetan — Indic structure, native words</div>',
            unsafe_allow_html=True)

st.table({
    "Power": ["10³", "10⁴", "10⁵", "10⁷"],
    "Tibetan": ["stong", "khri", "'bum", "bye ba"],
    "Note": ["thousand", "myriad pivot", "hundred thousand", "ten million"],
})

st.markdown("""
<div class="ling-card">
    <p style="margin:0">Tibetan adopted the Indic habit of naming successive powers while
    keeping its own vocabulary — one of the clearest cases anywhere of a numeral
    structure travelling without its words. Tibetan numerals are in this repository's
    <a href="/Tibetan_Converter" target="_self">converter</a>.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title">Nahuatl — vigesimal all the way up</div>',
            unsafe_allow_html=True)

st.table({
    "Power": ["20¹", "20²", "20³", "20⁴"],
    "Value": ["20", "400", "8,000", "160,000"],
    "Nahuatl": ["cempōhualli", "centzontli", "cenxiquipilli", "cempōhualxiquipilli"],
    "Literally": ["one whole count", "one head of hair", "one bag", "twenty bags"],
})

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">The contrast worth noticing</div>
    <p>Nahuatl and the Mayan Long Count are neighbours in the same linguistic area and share
    the same base. Nahuatl keeps it perfectly regular — 20, 400, 8,000, every pivot a
    true power. The Mayan Long Count bends it at the second position to fit the solar year.
    The base was shared across Mesoamerica by contact; what each culture <em>did</em> with it
    was not.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p style="margin:0">The etymologies are worth reading on their own: a score is
    &ldquo;one whole count&rdquo; — the fingers and toes — four hundred is
    &ldquo;one head of hair&rdquo;, and eight thousand is &ldquo;one bag&rdquo;, reportedly
    of cacao beans. The series records how the quantities were actually encountered.</p>
</div>
""", unsafe_allow_html=True)

# ── Sources ──────────────────────────────────────────────────────────────────
st.markdown('<div class="ling-section-label">Sources</div>', unsafe_allow_html=True)
st.markdown("""
<div class="ling-card">
    <p style="margin:0 0 .5rem 0">Comrie, B. (2005). <em>Endangered numeral systems.</em> In
    Wohlgemuth &amp; Dirksmeyer (eds.), <em>Bedrohte Vielfalt</em>, 203–230. Berlin:
    Weißensee Verlag — and personal communication, 2026.</p>
    <p style="margin:0 0 .5rem 0">Chrisomalis, S. (2010). <em>Numerical Notation: A
    Comparative History.</em> Cambridge University Press.</p>
    <p style="margin:0 0 .5rem 0">Menninger, K. (1969). <em>Number Words and Number
    Symbols.</em> MIT Press.</p>
    <p style="margin:0">Coe, M. &amp; Van Stone, M. (2005). <em>Reading the Maya
    Glyphs.</em> Thames &amp; Hudson.</p>
</div>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="nav-card-footer">'
    '<a class="nav-card" href="/Numeral_Contact" target="_self">'
    '<div class="nav-card-eyebrow">Cross-Linguistic Comparison</div>'
    '<div class="nav-card-title">How numeral systems travel</div>'
    '<div class="nav-card-desc">Borrowed words, borrowed structures, and how to tell '
    'contact apart from common ancestry.</div>'
    '<div class="nav-card-cta">Contact &amp; Transmission →</div>'
    '</a>'
    '<a class="nav-card-home" href="/" target="_self">← Home</a>'
    '</div>',
    unsafe_allow_html=True,
)
