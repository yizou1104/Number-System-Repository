import streamlit as st
from ui import apply_global_styles, LING_CSS, LING_WIDTH_CSS, language_nav, footer_nav

st.set_page_config(page_title="Hebrew Numerals — Linguistics", layout="wide")
apply_global_styles()
st.markdown(LING_CSS, unsafe_allow_html=True)
st.markdown(LING_WIDTH_CSS, unsafe_allow_html=True)
language_nav("Hebrew", "linguistics")

# ══════════════════════════════════════════════════════════════
# MASTHEAD
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="ling-masthead">
    <div class="ling-masthead-eyebrow">Linguistic Structure</div>
    <div class="ling-masthead-title">Hebrew Numerals</div>
    <div class="ling-tags">
        <span class="ling-tag">Alphabetic</span>
        <span class="ling-tag">Additive</span>
        <span class="ling-tag">Zero-less</span>
        <span class="ling-tag">Right-to-Left</span>
        <span class="ling-tag">Gender-Inflecting</span>
        <span class="ling-tag">Gematria</span>
        <span class="ling-tag accent">Divine-Name Exceptions</span>
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
    <p>Hebrew uses an alphabetic numeral system — each of the 22 letters of the Hebrew
    alphabet doubles as a digit. Numbers are written as strings of letters whose values
    are summed, with no concept of positional place-value or zero.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-props">
        <span class="ling-prop-key">System type</span>
        <span class="ling-prop-val"><strong>Alphabetic additive</strong></span>
        <span class="ling-prop-key">Base</span>
        <span class="ling-prop-val">None (non-positional)</span>
        <span class="ling-prop-key">Zero</span>
        <span class="ling-prop-val">Absent in classical system; modern אֶפֶס (efes) is a later loanword</span>
        <span class="ling-prop-key">Script</span>
        <span class="ling-prop-val">Hebrew abjad — right-to-left, 22 consonant letters</span>
        <span class="ling-prop-key">Range (standard)</span>
        <span class="ling-prop-val">1 – 9,999; extended with thousands geresh marker</span>
        <span class="ling-prop-key">Punctuation</span>
        <span class="ling-prop-val">Gershayim ״ and geresh ׳ mark numerals in text</span>
        <span class="ling-prop-key">Spoken system</span>
        <span class="ling-prop-val">Separate decimal word system with gender agreement</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 2 — THE LETTER-VALUE TABLE
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Letter Values</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">The 22-Letter Correspondence</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>The 22 letters of the Hebrew alphabet map onto three tiers of value: units (1–9),
    tens (10–90), and hundreds (100–400). All other values are formed by additive
    combination — 500 = 400 + 100 = תק, 900 = 400 + 400 + 100 = תתק.</p>
</div>
""", unsafe_allow_html=True)

st.table({
    "Letter": ['א','ב','ג','ד','ה','ו','ז','ח','ט','י','כ','ל','מ','נ','ס','ע','פ','צ','ק','ר','ש','ת'],
    "Name":   ['Aleph','Bet','Gimel','Dalet','He','Vav','Zayin','Chet','Tet',
               'Yod','Kaf','Lamed','Mem','Nun','Samech','Ayin','Pe','Tsadi',
               'Qof','Resh','Shin','Tav'],
    "Value":  ['1','2','3','4','5','6','7','8','9','10','20','30','40','50',
               '60','70','80','90','100','200','300','400'],
})

st.markdown("""
<div class="ling-card">
    <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.5rem">Values Above 400</div>
    <p>Because the alphabet ends at Tav (400), higher hundreds are formed additively:</p>
    <div class="ling-examples" style="margin-top:0.65rem;margin-bottom:0">
        <div class="ling-examples-label">Extended hundreds</div>
        <div class="ling-ex-line"><span class="num" style="min-width:3rem">500</span><span class="word" style="direction:rtl;unicode-bidi:embed">תק</span><span class="gloss">tav (400) + qof (100)</span></div>
        <div class="ling-ex-line"><span class="num" style="min-width:3rem">600</span><span class="word" style="direction:rtl;unicode-bidi:embed">תר</span><span class="gloss">tav (400) + resh (200)</span></div>
        <div class="ling-ex-line"><span class="num" style="min-width:3rem">700</span><span class="word" style="direction:rtl;unicode-bidi:embed">תש</span><span class="gloss">tav (400) + shin (300)</span></div>
        <div class="ling-ex-line"><span class="num" style="min-width:3rem">800</span><span class="word" style="direction:rtl;unicode-bidi:embed">תת</span><span class="gloss">tav (400) + tav (400)</span></div>
        <div class="ling-ex-line"><span class="num" style="min-width:3rem">900</span><span class="word" style="direction:rtl;unicode-bidi:embed">תתק</span><span class="gloss">tav + tav + qof</span></div>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 3 — GERSHAYIM PUNCTUATION
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Punctuation</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Gershayim Notation</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Why punctuate?</div>
    <p>Because Hebrew letters serve dual roles as both letters and numerals, gershayim
    marks are inserted to signal to the reader that a sequence of letters should be
    read as a number rather than as a word.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.5rem">Single-letter number</div>
        <p>A single letter receives a <em>geresh</em> (׳) placed <strong>after</strong> it.</p>
        <div class="ling-examples" style="margin-top:0.65rem;margin-bottom:0">
            <div class="ling-examples-label">Examples</div>
            <div class="ling-ex-line"><span class="num">1</span><span class="word" style="direction:rtl;unicode-bidi:embed">א׳</span></div>
            <div class="ling-ex-line"><span class="num">7</span><span class="word" style="direction:rtl;unicode-bidi:embed">ז׳</span></div>
            <div class="ling-ex-line"><span class="num">100</span><span class="word" style="direction:rtl;unicode-bidi:embed">ק׳</span></div>
        </div>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.5rem">Multi-letter number</div>
        <p>A <em>gershayim</em> (״) is placed <strong>before the last letter</strong> of the sequence.</p>
        <div class="ling-examples" style="margin-top:0.65rem;margin-bottom:0">
            <div class="ling-examples-label">Examples</div>
            <div class="ling-ex-line"><span class="num">14</span><span class="word" style="direction:rtl;unicode-bidi:embed">י״ד</span></div>
            <div class="ling-ex-line"><span class="num">35</span><span class="word" style="direction:rtl;unicode-bidi:embed">ל״ה</span></div>
            <div class="ling-ex-line"><span class="num">248</span><span class="word" style="direction:rtl;unicode-bidi:embed">רמ״ח</span></div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.5rem">Thousands separator</div>
    <p>For numbers 1,000–9,999, the thousands digit is written first with a geresh acting
    as a separator between the thousands and the remainder.</p>
    <div class="ling-examples" style="margin-top:0.65rem;margin-bottom:0">
        <div class="ling-examples-label">Examples</div>
        <div class="ling-ex-line"><span class="num">1000</span><span class="word" style="direction:rtl;unicode-bidi:embed">א׳</span></div>
        <div class="ling-ex-line"><span class="num">5784</span><span class="word" style="direction:rtl;unicode-bidi:embed">ה׳תשפ״ד</span><span class="gloss">he-geresh + 784</span></div>
        <div class="ling-ex-line"><span class="num">5785</span><span class="word" style="direction:rtl;unicode-bidi:embed">ה׳תשפ״ה</span><span class="gloss">current Hebrew year (2024–25 CE)</span></div>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 4 — DIVINE NAME EXCEPTIONS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Special Exceptions</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">The 15 and 16 Rules</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Religious convention</div>
    <p>The numbers 15 and 16 are written with non-standard letter combinations to avoid
    spelling abbreviations of divine names, which Jewish religious law prohibits writing
    casually.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.5rem">15 — the Yah exception</div>
        <p>10 + 5 = yod (י) + he (ה) = יה, an abbreviation of <em>Yah</em>, a divine name.
        Instead, 15 is written as 9 + 6:</p>
        <div class="ling-morph-table" style="margin-top:0.6rem">
            <div class="ling-morph-row">
                <span class="ling-morph-source">Standard</span>
                <span class="ling-morph-arrow">→</span>
                <span class="ling-morph-target" style="direction:rtl;unicode-bidi:embed">י״ה</span>
                <span class="ling-morph-gloss">forbidden (spells יה)</span>
            </div>
            <div class="ling-morph-row">
                <span class="ling-morph-source">Used</span>
                <span class="ling-morph-arrow">→</span>
                <span class="ling-morph-target" style="direction:rtl;unicode-bidi:embed">ט״ו</span>
                <span class="ling-morph-gloss">tet (9) + vav (6)</span>
            </div>
        </div>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.5rem">16 — the Yaho exception</div>
        <p>10 + 6 = yod (י) + vav (ו) = יו, the beginning of the Tetragrammaton.
        Instead, 16 is written as 9 + 7:</p>
        <div class="ling-morph-table" style="margin-top:0.6rem">
            <div class="ling-morph-row">
                <span class="ling-morph-source">Standard</span>
                <span class="ling-morph-arrow">→</span>
                <span class="ling-morph-target" style="direction:rtl;unicode-bidi:embed">י״ו</span>
                <span class="ling-morph-gloss">forbidden (spells יו)</span>
            </div>
            <div class="ling-morph-row">
                <span class="ling-morph-source">Used</span>
                <span class="ling-morph-arrow">→</span>
                <span class="ling-morph-target" style="direction:rtl;unicode-bidi:embed">ט״ז</span>
                <span class="ling-morph-gloss">tet (9) + zayin (7)</span>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>These exceptions propagate throughout the number system: 115 uses ט״ו for its
    last two digits (קט״ו), and 416 becomes תט״ז. No other numbers require such
    substitutions.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 5 — MODERN SPOKEN HEBREW
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Modern Spoken System</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Decimal Word Numerals</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Modern spoken Hebrew uses a completely separate decimal system of number words —
    distinct from the alphabetic notation. These words inflect for gender and agree
    with the noun they modify.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Digits 1–10</div>', unsafe_allow_html=True)

st.table({
    "Number": ["1","2","3","4","5","6","7","8","9","10"],
    "Masc. form (with fem. nouns)": [
        "אֶחָד echad",
        "שְנַיִם shnayim",
        "שְלֹשָה shlosha",
        "אַרְבָעָה arba'a",
        "חֲמִשָּה chamisha",
        "שִשָּה shisha",
        "שִבְעָה shiv'a",
        "שְמֹנָה shmonah",
        "תִשְעָה tish'a",
        "עֲשָרָה asara",
    ],
    "Fem. form (with masc. nouns)": [
        "אַחַת achat",
        "שְתַּיִם shtayim",
        "שָלֹש shalosh",
        "אַרְבַע arba",
        "חָמֵש chamesh",
        "שֵש shesh",
        "שֶבַע sheva",
        "שְמֹנֶה shmoneh",
        "תֵשַע tesha",
        "עֶשֶר eser",
    ],
})

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.5rem">Teens (11–19)</div>
        <p>Formed as <em>unit + asar/esre</em> (ten). The masculine unit form precedes
        masculine <em>asar</em>; the feminine unit form precedes feminine <em>esre</em>.</p>
        <div class="ling-examples" style="margin-top:0.65rem;margin-bottom:0">
            <div class="ling-examples-label">Masc. teens</div>
            <div class="ling-ex-line"><span class="num">11</span><span class="word">אַחַד עָשָר achad asar</span></div>
            <div class="ling-ex-line"><span class="num">17</span><span class="word">שִבְעָה עָשָר shiv'a asar</span></div>
        </div>
        <div class="ling-examples" style="margin-top:0.5rem;margin-bottom:0">
            <div class="ling-examples-label">Fem. teens</div>
            <div class="ling-ex-line"><span class="num">11</span><span class="word">אַחַת עֶשְרֵה achat esre</span></div>
            <div class="ling-ex-line"><span class="num">17</span><span class="word">שְבַע עֶשְרֵה shva esre</span></div>
        </div>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.5rem">Tens &amp; Compounds</div>
        <p>Decade words are gender-invariant. Compound numbers join tens and units
        with the conjunction <em>ve-</em> (and).</p>
        <div class="ling-examples" style="margin-top:0.65rem;margin-bottom:0">
            <div class="ling-examples-label">Tens</div>
            <div class="ling-ex-line"><span class="num">20</span><span class="word">עֶשְרִים esrim</span></div>
            <div class="ling-ex-line"><span class="num">30</span><span class="word">שְלֹשִים shloshim</span></div>
            <div class="ling-ex-line"><span class="num">50</span><span class="word">חֲמִשִּים chamishim</span></div>
        </div>
        <div class="ling-examples" style="margin-top:0.5rem;margin-bottom:0">
            <div class="ling-examples-label">Compound</div>
            <div class="ling-ex-line"><span class="num">34</span><span class="word">שְלֹשִים וְאַרְבָעָה</span></div>
            <div class="ling-ex-line"><span class="num">99</span><span class="word">תִשְעִים וְתִשְעָה</span></div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Hundreds &amp; Thousands</div>', unsafe_allow_html=True)

st.table({
    "Value":   ["100","200","300","1,000","2,000","3,000"],
    "Form":    ["מֵאָה meah","מָאתַיִם matayim","שְלֹש מֵאוֹת shlosh meot",
                "אֶלֶף elef","אַלְפַּיִם alpayim","שְלֹשֶת אֲלָפִים shloshet alafim"],
    "Structure": ["base","dual","fem. 3 + meot (pl.)","base","dual",
                  "construct state + alafim (pl.)"],
})

st.markdown("""
<div class="ling-info">
    <p>200 (matayim) and 2,000 (alpayim) use the <strong>dual number</strong> — a
    morphological form for pairs that exists alongside singular and plural in Hebrew.
    These are not regular plurals; they are lexically stored dual forms.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 6 — GENDER POLARITY
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Syntax &amp; Morphology</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Gender Polarity — The Great Reversal</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Typological Anomaly</div>
    <p>Hebrew numbers 3–10 display <strong>gender polarity</strong> — the "masculine" form
    of the numeral is used with <em>feminine</em> nouns, and the "feminine" form
    with <em>masculine</em> nouns. This is one of the most discussed puzzles in
    Semitic linguistics.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>The form ending in <em>-ah</em> (e.g., <em>shlosha</em>, <em>arba'a</em>) looks feminine
    morphologically (the <em>-ah</em> suffix is the standard feminine marker in Hebrew), yet
    it is used when counting masculine nouns. The bare form without <em>-ah</em>
    (e.g., <em>shalosh</em>, <em>arba</em>) looks masculine, yet accompanies feminine nouns.</p>
    <div class="ling-examples" style="margin-top:0.85rem;margin-bottom:0">
        <div class="ling-examples-label">Gender polarity in context</div>
        <div class="ling-ex-line">
            <span class="word">שְלֹשָה יְלָדִים</span>
            <span class="gloss">shlosha yeladim — three boys (masc. noun → -ah form)</span>
        </div>
        <div class="ling-ex-line">
            <span class="word">שָלֹש יְלָדוֹת</span>
            <span class="gloss">shalosh yeladot — three girls (fem. noun → bare form)</span>
        </div>
        <div class="ling-ex-line">
            <span class="word">אַרְבָעָה אֲנָשִים</span>
            <span class="gloss">arba'a anashim — four men (masc. noun → -ah form)</span>
        </div>
        <div class="ling-ex-line">
            <span class="word">אַרְבַע נָשִים</span>
            <span class="gloss">arba nashim — four women (fem. noun → bare form)</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.5rem">Exceptions: 1 and 2</div>
        <p>The numerals 1 and 2 follow <em>normal</em> agreement — the form matches the
        grammatical gender of the noun.</p>
        <p style="font-family:'DM Mono',monospace;font-size:0.9rem;color:var(--ink-muted)">
        אִישׁ אֶחָד — one man (masc.)<br>
        אִשָּה אַחַת — one woman (fem.)
        </p>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.5rem">Hundreds use feminine forms</div>
        <p>The noun מֵאָה (meah, hundred) is grammatically feminine, so numbers 3–9 before
        מֵאוֹת use the feminine (bare) form: שָלֹש מֵאוֹת (shalosh meot = 300), not *שְלֹשָה.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 7 — ORDINALS & CONSTRUCT STATE
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Further Morphology</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Ordinals &amp; Construct State</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.5rem">Ordinal Formation</div>
        <p>Ordinals for 1–10 are separate adjective forms, agreeing in gender and
        definiteness with the noun. From 11 onward, cardinals typically serve as ordinals.</p>
        <div class="ling-morph-table" style="margin-top:0.65rem">
            <div class="ling-morph-row">
                <span class="ling-morph-source">1st</span>
                <span class="ling-morph-arrow">→</span>
                <span class="ling-morph-target">רִאשׁוֹן</span>
                <span class="ling-morph-gloss">rishon (masc.)</span>
            </div>
            <div class="ling-morph-row">
                <span class="ling-morph-source">2nd</span>
                <span class="ling-morph-arrow">→</span>
                <span class="ling-morph-target">שֵנִי</span>
                <span class="ling-morph-gloss">sheni (masc.)</span>
            </div>
            <div class="ling-morph-row">
                <span class="ling-morph-source">3rd</span>
                <span class="ling-morph-arrow">→</span>
                <span class="ling-morph-target">שְלִישִי</span>
                <span class="ling-morph-gloss">shlishi (masc.)</span>
            </div>
            <div class="ling-morph-row">
                <span class="ling-morph-source">4th</span>
                <span class="ling-morph-arrow">→</span>
                <span class="ling-morph-target">רְבִיעִי</span>
                <span class="ling-morph-gloss">revi'i (masc.)</span>
            </div>
            <div class="ling-morph-row">
                <span class="ling-morph-source">5th</span>
                <span class="ling-morph-arrow">→</span>
                <span class="ling-morph-target">חֲמִישִי</span>
                <span class="ling-morph-gloss">chamishi (masc.)</span>
            </div>
        </div>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.5rem">Construct State with Thousands</div>
        <p>When numerals 3–9 precede a plural noun, they take the <em>construct state</em>
        (smichut), which reduces the word and drops the final vowel.</p>
        <div class="ling-examples" style="margin-top:0.65rem;margin-bottom:0">
            <div class="ling-examples-label">Construct state (before alafim)</div>
            <div class="ling-ex-line"><span class="num">3,000</span><span class="word">שְלֹשֶׁת אֲלָפִים</span></div>
            <div class="ling-ex-line"><span class="gloss">shloshet — construct of shalosh</span></div>
            <div class="ling-ex-line"><span class="num">5,000</span><span class="word">חֲמֵשֶׁת אֲלָפִים</span></div>
            <div class="ling-ex-line"><span class="gloss">chameshet — construct of chamesh</span></div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 8 — GEMATRIA & CULTURAL CONTEXT
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Cultural &amp; Religious Context</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Gematria — Numbers as Meaning</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Gematria</div>
    <p>Because every Hebrew word has a numeric value (the sum of its letter values),
    Jewish tradition uses <strong>gematria</strong> to find numerological connections
    between words and texts. The technique has been applied in Biblical interpretation,
    Kabbalah, and popular culture for over two millennia.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Notable gematria values embedded in tradition:</p>
    <div class="ling-examples" style="margin-top:0.75rem;margin-bottom:0">
        <div class="ling-examples-label">Famous values</div>
        <div class="ling-ex-line">
            <span class="num" style="min-width:2.5rem">18</span>
            <span class="word" style="direction:rtl;unicode-bidi:embed">חַי</span>
            <span class="gloss">chai — "life" (ח=8, י=10). Gifts in multiples of 18 are traditional.</span>
        </div>
        <div class="ling-ex-line">
            <span class="num" style="min-width:2.5rem">26</span>
            <span class="word" style="direction:rtl;unicode-bidi:embed">יהוה</span>
            <span class="gloss">the Tetragrammaton — the four-letter divine name</span>
        </div>
        <div class="ling-ex-line">
            <span class="num" style="min-width:2.5rem">248</span>
            <span class="word" style="direction:rtl;unicode-bidi:embed">רמ״ח</span>
            <span class="gloss">number of positive commandments (mitzvot aseh) in the Torah</span>
        </div>
        <div class="ling-ex-line">
            <span class="num" style="min-width:2.5rem">365</span>
            <span class="word" style="direction:rtl;unicode-bidi:embed">שס״ה</span>
            <span class="gloss">number of negative commandments — one per day of the solar year</span>
        </div>
        <div class="ling-ex-line">
            <span class="num" style="min-width:2.5rem">613</span>
            <span class="word" style="direction:rtl;unicode-bidi:embed">תרי״ג</span>
            <span class="gloss">total commandments (mitzvot) in the Torah</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.5rem">The Hebrew Calendar</div>
        <p>Hebrew calendar years are written in alphabetic notation. The current year
        5785 (תשפ״ה) corresponds to 2024–2025 CE. In everyday contexts, the thousands
        digit is often dropped — תשפ״ה rather than ה׳תשפ״ה.</p>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.5rem">Synagogue &amp; Religious Use</div>
        <p>Alphabetic numerals appear in Torah scrolls, mezuzot, prayer books (siddurim),
        and grave inscriptions. Chapter and verse references in religious texts universally
        use the gematria system rather than Arabic numerals.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Compound example: 5,785</div>
    <div class="ling-ex-line">
        <span class="num" style="min-width:5rem">Alphabetic</span>
        <span class="word" style="direction:rtl;unicode-bidi:embed">ה׳תשפ״ה</span>
    </div>
    <div class="ling-ex-line">
        <span class="num" style="min-width:5rem">Spoken</span>
        <span class="word">חֲמֵשֶת אֲלָפִים שְבַע מֵאוֹת שְמֹנִים וְחֲמִשָּה</span>
    </div>
    <div class="ling-ex-line">
        <span class="num" style="min-width:5rem">Romanized</span>
        <span class="word">chameshet alafim shva meot shmonim ve-chamisha</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── NAVIGATION ──────────────────────────────────────────────
footer_nav("Hebrew", "linguistics")
