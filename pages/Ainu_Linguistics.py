import streamlit as st

from ui import apply_global_styles, LING_CSS, LING_WIDTH_CSS, language_nav, footer_nav

st.set_page_config(page_title="Ainu Numerals — Linguistics", layout="wide")
apply_global_styles()
st.markdown(LING_CSS, unsafe_allow_html=True)
st.markdown(LING_WIDTH_CSS, unsafe_allow_html=True)
language_nav("Ainu", "linguistics")

# ══════════════════════════════════════════════════════════════
# MASTHEAD
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="ling-masthead">
    <div class="ling-masthead-eyebrow">Linguistic Structure</div>
    <div class="ling-masthead-title">Ainu Numerals</div>
    <div class="ling-masthead-sub">
        A survey of the Hokkaido Ainu numeral grammar — a vigesimal system that
        runs four different arithmetic operations in a single counting sequence.
    </div>
    <div class="ling-tags">
        <span class="ling-tag">Vigesimal</span>
        <span class="ling-tag">Subtractive</span>
        <span class="ling-tag">Overcounting</span>
        <span class="ling-tag">Classifier-Sensitive</span>
        <span class="ling-tag">Language Isolate</span>
        <span class="ling-tag">Critically Endangered</span>
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
    <p>Most numeral systems lean on one or two arithmetic operations. Ainu uses four in a
    single unbroken run from 1 to 40: <strong>subtraction</strong> builds 6 through 9,
    <strong>addition</strong> builds the teens, <strong>multiplication</strong> builds the
    scores, and <strong>overcounting</strong> — naming a number by the multiple it is
    approaching rather than the one it has passed — builds 30. That last operation is rare
    enough worldwide that Ainu specialists spent a century misreading it as subtraction.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-props">
        <span class="ling-prop-key">Primary base</span>
        <span class="ling-prop-val"><strong>20 (vigesimal)</strong>, on <em>hot</em> 'score, set'</span>
        <span class="ling-prop-key">Sub-base</span>
        <span class="ling-prop-val">10 (<em>wan</em>) organises everything below 20</span>
        <span class="ling-prop-key">Operations used</span>
        <span class="ling-prop-val">Subtraction, addition, multiplication, overcounting</span>
        <span class="ling-prop-key">Zero</span>
        <span class="ling-prop-val">No attested traditional form</span>
        <span class="ling-prop-key">Classifier sensitivity</span>
        <span class="ling-prop-val">Four distinct paradigms by what is counted</span>
        <span class="ling-prop-key">Documented ceiling</span>
        <span class="ling-prop-val">About 200 in practice; Batchelor records forms to 1,000</span>
        <span class="ling-prop-key">Genetic affiliation</span>
        <span class="ling-prop-val">Language isolate — no demonstrated relatives</span>
        <span class="ling-prop-key">Script</span>
        <span class="ling-prop-val">Katakana in Japan; Latin transcription in linguistic sources</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>Ainu is a language isolate of Hokkaido, formerly also spoken in Sakhalin and the Kuril
    Islands. UNESCO classifies Hokkaido Ainu as <strong>critically endangered</strong>; the
    Sakhalin and Kuril varieties are gone. This page describes Southern and Southwestern
    Hokkaido Ainu, the varieties for which the numeral system is best documented.</p>
    <p>The forms here use the Latin transcription standard in the linguistic literature
    (<em>sine</em>, <em>asikne</em>, <em>hotne</em>). Batchelor's 1905 dictionary writes the
    same words with English spelling conventions (<em>shine</em>, <em>ashikne</em>,
    <em>hot ne</em>); where his forms are quoted below, they are marked as his.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 2 — DIGITS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Digits &amp; Bases</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Basic Digits (1–10)</div>', unsafe_allow_html=True)

st.table({
    "Number":    ["1","2","3","4","5","6","7","8","9","10","20"],
    "Adnominal": ["sine","tu","re","ine","asikne","iwan","arwan",
                  "tupesan","sinepesan","wan","hotne"],
    "Operation": ["—","—","—","—","—","10 − 4","10 − 3","10 − 2","10 − 1","—","—"],
})

st.markdown("""
<div class="ling-info">
    <p>There is no word for zero. The documented system begins at one, and the converter
    reports this rather than supplying an invented form.</p>
</div>
""", unsafe_allow_html=True)

# ── Internal morphology ──────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.75rem">Internal Morphology of the Simplex Numerals</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-morph-table">
        <div class="ling-morph-row">
            <span class="ling-morph-source">sine</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">si-ne</span>
            <span class="ling-morph-gloss">'truly / oneself' + copula</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">ine</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">i-ne</span>
            <span class="ling-morph-gloss">four (cf. <em>inne</em> 'many') + copula</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">asikne</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">asik-ne</span>
            <span class="ling-morph-gloss">from <em>aske</em> 'hand' + copula — five is one hand</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">wan</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">w-an</span>
            <span class="ling-morph-gloss">reciprocal + 'exist' — both hands are there</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">hotne</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">hot-ne</span>
            <span class="ling-morph-gloss"><em>hot</em> 'a set' — fingers and toes together + copula</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>The body is visible straight through the lexicon. <em>Five</em> is a hand, <em>ten</em>
    is both hands, and <em>twenty</em> is the set of fingers and toes — which is also the
    reason the base is 20 rather than 10. Only <em>tu</em> 'two' and <em>re</em> 'three' are
    monomorphemic; the rest contain a verb.</p>
    <p>Decompositions follow Tamura (1988/2000), Kindaichi &amp; Chiri (1936/1974) and
    Refsing (1986), as summarised in Dékány (2025).</p>
</div>
""", unsafe_allow_html=True)

# ── Subtractive 6-9 ─────────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.75rem">Subtraction: 6, 7, 8, 9</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[subtrahend] + [<em>wan</em> 10] — juxtaposed, no connector</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">The upper half of the first decade counts down</div>
    <div class="ling-ex-line"><span class="num">6</span><span class="word">i-wan</span><span class="gloss">four–ten → 10 − 4</span></div>
    <div class="ling-ex-line"><span class="num">7</span><span class="word">ar-wan</span><span class="gloss">three–ten → 10 − 3</span></div>
    <div class="ling-ex-line"><span class="num">8</span><span class="word">tupesan</span><span class="gloss">lacking two → 10 − 2</span></div>
    <div class="ling-ex-line"><span class="num">9</span><span class="word">sinepesan</span><span class="gloss">lacking one → 10 − 1</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>In 6 the numeral <em>ine</em> 'four' appears as bare <em>i-</em>, dropping its copula —
    independent evidence that <em>-ne</em> really is a separate morpheme. In 7 the stem for
    'three' surfaces as <em>ar-</em> rather than <em>re</em>, an alternation nobody has
    satisfactorily explained; Ochiai (2021) proposes an original <em>ar-i-wan</em>
    'the other six', contracted.</p>
    <p>8 and 9 are agreed to be subtractive but their internal segmentation is still disputed.
    Their shapes differ by context: <em>tupes</em> when reciting, <em>tupesan</em> before a
    noun, where the extra <em>-an</em> is the singular existential verb.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 3 — FORM CLASSES
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Form Classes</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">One Number, Four Shapes</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>An Ainu numeral changes form according to what it counts and whether it is being
    recited in the abstract. All four paradigms below are independently attested; the
    converter shows them side by side for any value up to twenty.</p>
</div>
""", unsafe_allow_html=True)

st.table({
    "Value":              ["1","2","3","4","5","6","7","8","9","10","20"],
    "Adnominal":          ["sine","tu","re","ine","asikne","iwan","arwan",
                           "tupesan","sinepesan","wan","hotne"],
    "Serial counting":    ["sinep","tup","rep","inep","asik","iwan","arwan",
                           "tupes","sinepes","wan","hot"],
    "Things (-p / -pe)":  ["sinep","tup","rep","inep","asiknep","iwanpe","arwanpe",
                           "tupesanpe","sinepesanpe","wanpe","hotnep"],
    "People (-n / -iw)":  ["sinen","tun","ren","inen","asiknen","iwaniw","arwaniw",
                           "tupesaniw","sinepesaniw","waniw","hotne niw"],
})

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card" style="margin-bottom:0">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">The two suffixes</div>
        <p><em>-p</em> / <em>-pe</em> is a light noun meaning 'thing'; <em>niw</em> means
        'person', reducing to <em>-n</em> after a vowel and <em>-iw</em> after a consonant.
        Refsing notes these are nominalisers rather than part of the numeral itself — closer
        to Japanese <em>-tsu</em> than to a true gender ending.</p>
    </div>
    <div class="ling-card" style="margin-bottom:0">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">A third classifier</div>
        <p>Batchelor records <em>pish</em> for quadrupeds, but only with 'two' and 'three':
        <em>seta tup pish</em> 'two dogs' beside plain <em>seta inep</em> 'four dogs'. He adds
        that no further classifiers exist in the language — the inventory is three items deep
        and defective.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Consequence</div>
    <p>The bare adnominal form cannot stand alone as an answer to a question. Asked "how
    many?", a speaker must use one of the substantive forms, because the numeral is
    syntactically a clause missing its noun.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 4 — COMPOSITIONAL RULES
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Compositional Rules</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">How Numbers Are Built</div>', unsafe_allow_html=True)

# ── Addition ────────────────────────────────────────────────
st.markdown('<div class="ling-subsection-title">Addition — <em>ikasma</em> \'exceed\'</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[addend] + <em>ikasma</em> + [base]</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Examples — teens and the twenties</div>
    <div class="ling-ex-line"><span class="num">11</span><span class="word">sine ikasma wan</span><span class="gloss">one exceeds ten</span></div>
    <div class="ling-ex-line"><span class="num">17</span><span class="word">arwan ikasma wan</span><span class="gloss">seven exceeds ten</span></div>
    <div class="ling-ex-line"><span class="num">26</span><span class="word">iwan ikasma hotne</span><span class="gloss">six exceeds a score</span></div>
    <div class="ling-ex-line"><span class="num">28</span><span class="word">tupesan ikasma hotne</span><span class="gloss">eight exceeds a score</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p><em>ikasma</em> is a verb meaning 'exceed, be in excess, remain over', and it keeps its
    verbal syntax inside the numeral: it takes the addend as its subject and follows it.
    Ainu never groups the two halves of an additive numeral into a unit that excludes the
    counted noun — which is why Batchelor's substantive forms repeat the classifier on each
    part: <em>sinep ikasma wanpe</em> 'eleven things', literally 'one thing exceeds ten
    things'.</p>
</div>
""", unsafe_allow_html=True)

# ── Multiplication ──────────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.75rem">Multiplication — scores of <em>hot</em></div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[multiplier] + <em>hotne</em></span>
</div>
""", unsafe_allow_html=True)

st.table({
    "Value":     ["20","40","60","80","100","200"],
    "Form":      ["hotne","tu hotne","re hotne","ine hotne","asikne hotne","sine wan hotne"],
    "Structure": ["1 × 20","2 × 20","3 × 20","4 × 20","5 × 20","one ten-score (10 × 20)"],
})

st.markdown("""
<div class="ling-info">
    <p>There is no word for 'hundred'. 100 is simply <em>asikne hotne</em>, five scores, and
    200 introduces a higher unit <em>sine wan hotne</em>, 'one ten-score', on which
    Batchelor's larger numerals are built. Twenty itself also appears as <em>sine hot</em>
    'one score' in some sources, and as bare <em>hot</em> without the copula.</p>
</div>
""", unsafe_allow_html=True)

# ── Overcounting ────────────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.75rem">Overcounting — <em>e</em> \'towards\'</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">The unusual operation</div>
    <p>Ainu has no word built on 'thirty'. 30 is named by looking <em>forward</em> to forty:
    <em>wan e tu hotne</em>, "ten towards two scores". The number is identified by how far it
    has travelled into the span that ends at the next multiple of twenty.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[10–19] + <em>e</em> + [next multiple of 20]</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Examples — the odd tens and their interiors</div>
    <div class="ling-ex-line"><span class="num">30</span><span class="word">wan e tu hotne</span><span class="gloss">ten towards forty</span></div>
    <div class="ling-ex-line"><span class="num">36</span><span class="word">iwan ikasma wan e tu hotne</span><span class="gloss">sixteen towards forty</span></div>
    <div class="ling-ex-line"><span class="num">50</span><span class="word">wan e re hotne</span><span class="gloss">ten towards sixty</span></div>
    <div class="ling-ex-line"><span class="num">70</span><span class="word">wan e ine hotne</span><span class="gloss">ten towards eighty</span></div>
    <div class="ling-ex-line"><span class="num">90</span><span class="word">wan e asikne hotne</span><span class="gloss">ten towards a hundred</span></div>
    <div class="ling-ex-line"><span class="num">99</span><span class="word">sinepesan ikasma wan e asikne hotne</span><span class="gloss">nineteen towards a hundred</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Note that the overcounting numeral is built on a <em>teen</em>, not a unit: 36 is
    "sixteen towards forty", with an additive numeral nested inside the overcounting frame.
    The smaller numeral is the head, and the <em>e</em>-phrase modifies it.</p>
</div>
""", unsafe_allow_html=True)

# ── The split ───────────────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.75rem">The Switch Inside Every Score</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>Each twenty-wide span is counted in two halves. The first nine values look
    <em>backwards</em> to the score just passed; from the tenth onward they look
    <em>forwards</em> to the score ahead. Ochiai (2021) calls these undercounting and
    overcounting, and shows the switch recurs in every span.</p>
</div>
""", unsafe_allow_html=True)

st.table({
    "Position in span": ["+1 to +9", "+10 to +19"],
    "Operation":        ["Undercounting (additive)", "Overcounting (lative)"],
    "Reference point":  ["The score already passed", "The score still ahead"],
    "Example":          ["26 = iwan ikasma hotne", "36 = iwan ikasma wan e tu hotne"],
    "Literal":          ["six exceeds twenty", "sixteen towards forty"],
})

# ══════════════════════════════════════════════════════════════
# SECTION 5 — THE DISAGREEMENT
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Analysis</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">A Century-Long Misreading</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>Whether <em>wan e tu hotne</em> means "ten <em>from</em> forty" or "ten
    <em>towards</em> forty" does not change the answer — both give 30. It changes what kind
    of system Ainu is. The two readings have been in print for over a century, and the older
    one is now considered wrong.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card" style="margin-bottom:0">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">Batchelor (1905): subtraction</div>
        <p>"The particle <em>e</em> signifies 'to subtract', 'to take away from'." He adds an
        explicit warning: do not confuse this with the <em>other</em> <em>e</em>, the
        preposition meaning 'to, towards'. On his reading, 30 is forty minus ten, and Ainu
        patterns with Latin <em>duodeviginti</em> 'two from twenty' for 18.</p>
    </div>
    <div class="ling-card" style="margin-bottom:0">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">Ochiai (2021), Dékány (2025): overcounting</div>
        <p>It is the lative <em>e</em> after all — the very morpheme Batchelor told readers to
        rule out. <em>e-</em> carries 'towards' throughout the language, well outside the
        numerals, and reading it that way makes Ainu an overcounting language, the same type
        as Northern Mansi, where 21 is 'one towards thirty'.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Evidence from Batchelor's own pages</div>
    <p>A few lines after his warning, Batchelor lists the fractions <em>e-tup</em> 'one and a
    half', <em>e-rep</em> 'two and a half', <em>e-inep</em> 'three and a half'. These only work
    with the lative reading: <em>e-tup</em> is a quantity <em>heading towards</em> two.
    Subtraction from two cannot yield one and a half. The data that undercuts his analysis is
    on the same page as the analysis.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Dékány (2025) suggests why the error persisted: overcounting is rare and was simply not
    on the radar of either Japanese or Western Ainu specialists, while the Latin subtractive
    pattern was familiar to all of them. A known template was available and an unknown one
    was not, so the data was fitted to the known one. The pattern has been misidentified the
    same way in other languages, including Paiwan.</p>
    <p>This repository follows the modern analysis. The converter generates overcounting forms
    and glosses 30 as "ten towards forty".</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 6 — SYNTAX
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Syntax &amp; Morphology</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Grammatical Integration</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Most Ainu numerals are not adjectives — they are clauses</div>
    <p>Only <em>tu</em> 'two' and <em>re</em> 'three' attach directly to a noun. Every other
    numeral is built around a verb, and reaches the noun through it. <em>asikne utar</em>
    'five people' is literally closer to "people such that they are five".</p>
</div>
""", unsafe_allow_html=True)

st.table({
    "Numeral":       ["2, 3", "1, 4, 5, 20", "10"],
    "Modification":  ["Direct", "Indirect", "Indirect"],
    "Mediated by":   ["— attaches to the noun itself",
                      "Relative clause with the copula 'ne'",
                      "Saturated clause with the existential 'an'"],
})

st.markdown("""
<div class="ling-info">
    <p>Dékány (2025) argues this split matches the direct-versus-indirect division Cinque
    proposed for adjectives, extending it to a modifier class not previously known to show it.
    It is the reason the numerals carry copulas at all: <em>si-ne</em>, <em>i-ne</em>,
    <em>asik-ne</em> and <em>hot-ne</em> all end in the copula <em>ne</em>, and <em>wan</em>
    contains the existential <em>an</em>.</p>
</div>
""", unsafe_allow_html=True)

# ── Ordinals and adverbials ─────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.75rem">Ordinals and Adverbials</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card" style="margin-bottom:0">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">Ordinals — <em>ikinne</em></div>
        <p><em>sine ikinne</em> 'first', <em>tu ikinne</em> 'second', <em>wan ikinne</em>
        'tenth'. A second series with <em>otutanu</em> exists but stops at ten. Batchelor notes
        the ordinals "are rarely met with".</p>
    </div>
    <div class="ling-card" style="margin-bottom:0">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">Adverbials — <em>suine</em></div>
        <p><em>tu suine</em> 'twice', <em>re suine</em> 'thrice'. From <em>sui</em> 'again' plus
        the copula <em>ne</em> — so 'twice' is built as "to be two again".</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Pairs sit outside the numeral system entirely. <em>uren</em> 'both' marks a natural
    pair — <em>uren kisara</em> 'both ears' — and <em>oara</em> marks one of a pair:
    <em>oara teke</em> 'one hand', <em>oara siki</em> 'one eye'. Neither uses a numeral.</p>
</div>
""", unsafe_allow_html=True)

# ── Day counting ────────────────────────────────────────────
st.markdown('<div class="ling-subsection-title" style="margin-top:1.75rem">Counting Days: a Separate, Irregular System</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Days do not use the ordinary numerals</div>
    <div class="ling-ex-line"><span class="num">1</span><span class="word">sine to</span><span class="gloss">regular</span></div>
    <div class="ling-ex-line"><span class="num">2</span><span class="word">tut ko</span><span class="gloss">suppletive — not <em>tu to</em></span></div>
    <div class="ling-ex-line"><span class="num">3</span><span class="word">rere ko</span><span class="gloss">suppletive — not <em>re to</em></span></div>
    <div class="ling-ex-line"><span class="num">4</span><span class="word">ine rere ko</span><span class="gloss">built on the form for three</span></div>
    <div class="ling-ex-line"><span class="num">10</span><span class="word">wan to</span><span class="gloss">regular again</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>A handful of nouns — <em>to</em> 'day', <em>tokap</em> 'daytime', <em>kunne</em> 'night',
    <em>kamuy</em> 'god' — are excluded from the ordinary classifier paradigms and take their
    own counting forms, with irregular shapes at 2, 3 and 4 that then propagate upward. Nights
    are counted with <em>ancikara</em>, not <em>to</em>. This sub-system is not implemented in
    the converter; it is a distinct paradigm rather than a variant of the main one.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 7 — LIMITS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Limits of the Record</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Where the Documentation Stops</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Why this section exists</div>
    <p>Ainu numerals can be generated far past the point where anyone is recorded using them.
    Printing those forms without saying so would misrepresent a critically endangered language
    as better documented than it is, so the boundaries are set out here and enforced in the
    converter.</p>
</div>
""", unsafe_allow_html=True)

st.table({
    "Range":      ["1–20", "21–99", "100–119", "120–199", "200", "201–1000"],
    "Status":     ["Core inventory", "Well documented", "Documented",
                   "Dialect split", "Practical ceiling", "Batchelor only"],
    "Basis":      ["Identical across all sources consulted",
                   "Batchelor's full table, corroborated by Refsing and Ochiai",
                   "100 directly attested; interiors follow the attested rule",
                   "Two competing forms — see below",
                   "Reported as the upper limit of real use",
                   "In Batchelor (1905), uncorroborated since"],
})

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card" style="margin-bottom:0">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">The split at 120</div>
        <p>Ochiai (2021: 104) reports that from 120 most dialects abandon the vigesimal
        multiplier and add a score onto a hundred instead: <em>hotnep ikasma asikne hot</em>,
        'twenty exceeds five scores'. The Saru dialect permits both that and the
        multiplicative <em>iwan hot</em>, six scores. The converter shows the multiplicative
        form with the additive variant beside it.</p>
    </div>
    <div class="ling-card" style="margin-bottom:0">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">Above 200</div>
        <p>Batchelor gives round hundreds up to 1,000, built on the 200-unit — 400 is
        <em>tu sine wan hotne</em>, two ten-scores. He gives no intermediate values, so the
        converter generates multiples of 100 and refuses the rest rather than inventing forms
        no source attests.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Three independent observations mark the real ceiling. Batchelor (1905) wrote that
    "twenty &mdash; more literally a 'score' &mdash; is the highest unit ever present to the
    Ainu mind when counting", and that larger numbers "are rarely, if ever, met with". Refsing,
    supplying data in 2013, stated that she did not believe numbers above twenty were ever
    used in speech, only constructed on request. Tamura (1999: 58) records that the system
    could reach two hundred in principle, but that Ainu elders in the 1950s did not understand
    what "two hundred" meant, because counting that high was not customary &mdash; not even
    for ages.</p>
    <p>A fourth data point comes from the collection process itself: the Chitose-dialect
    speaker consulted for Chan's database supplied little beyond ten, because in her
    generation Japanese had already taken over everyday counting. The shrinking of this
    numeral system is visible in the sources that document it.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 8 — SOURCES
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Sources</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">References</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p><strong>Batchelor, John.</strong> 1905. <em>An Ainu–English–Japanese Dictionary
    (including a Grammar of the Ainu Language)</em>, ch. VII "Numerals". The earliest complete
    numeral table, 1 to 1,000, and the source of the subtractive analysis of <em>e</em>.</p>

    <p><strong>Ochiai, Izumi.</strong> 2021. "Ainu Numerals Revisited: The Shift from
    Undercounting to Overcounting in the Vigesimal System." <em>Northern Language Studies</em>
    11: 99–121. Reconstructs the vigesimal system across the Hokkaido, Sakhalin and Kuril
    dialects, and establishes the undercounting/overcounting split.</p>

    <p><strong>Dékány, Éva.</strong> 2025. "The syntax of numeral modification in Ainu."
    <em>Acta Linguistica Academica</em> 72(4): 455–515. Open access. The first syntactic
    analysis of the overcounting numerals, and the direct/indirect modification split.</p>

    <p><strong>Tamura, Suzuko.</strong> 1988/2000. <em>The Ainu Language</em>; and 1999,
    on the practical limits of the numeral system.</p>

    <p><strong>Refsing, Kirsten.</strong> 1986. <em>The Ainu Language: The Morphology and
    Syntax of the Shizunai Dialect</em>.</p>

    <p><strong>Chan, Eugene S. L.</strong> <em>Numeral Systems of the World's Languages</em>,
    Ainu page (Max Planck Institute). Three independent informant sets: Tomomi Sato (2013,
    Chitose dialect), Kirsten Refsing (2013), and Jiro Ikegami with Toshiyuki Shinozaki (1983).
    The disagreements between them are the basis of the attestation tiers above.</p>

    <p><strong>Alonso de la Fuente, José Andrés.</strong> "Counting days in Hokkaidō Ainu:
    Some thoughts on internal reconstruction and etymology." On the suppletive day-counting
    forms.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p><strong>A note on sources not used.</strong> Several popular numeral sites give Ainu
    native words for 1,000 and 10,000. No academic source consulted here supports them, and
    they are hard to reconcile with Tamura's report that speakers did not recognise "two
    hundred". They are omitted. Katakana spellings are likewise omitted: Ainu is written in
    katakana in Japan, but the forms could not be verified against a source of the standard
    used elsewhere on this page.</p>
</div>
""", unsafe_allow_html=True)

footer_nav("Ainu", "linguistics")
