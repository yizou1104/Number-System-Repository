import streamlit as st
from ui import apply_global_styles, LING_CSS, LING_WIDTH_CSS, language_nav, footer_nav

st.set_page_config(page_title="Tulu Numerals — Linguistics", layout="wide")
apply_global_styles()
st.markdown(LING_CSS, unsafe_allow_html=True)
st.markdown(LING_WIDTH_CSS, unsafe_allow_html=True)
st.markdown("""
<style>
/* Kannada script for Tulu; Charis SIL, subset to the IPA characters used, for pronunciations */
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+Kannada:wght@400;600&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Charis+SIL&text=%20abdeilmnoprstu~%C9%96%C9%AF%C9%B2%C9%B3%C9%BE%CA%8B%CA%92%CB%90%CC%AA%CD%A1%E2%81%B1&display=swap');
.tu-kn { font-family: 'Noto Serif Kannada', 'Crimson Pro', serif; }
.tu-digits { font-family: 'Noto Serif Kannada', serif; font-size: 1.6rem; letter-spacing: .35em; }
div[data-testid="stTable"] td, div[data-testid="stTable"] td p {
    font-family: 'Crimson Pro', 'Noto Serif Kannada', 'Charis SIL', serif !important; }
/* the 1-20 table is the only one with 20 rows; its last column holds IPA */
div[data-testid="stTable"]:has(tbody tr:nth-child(20)) td:last-child,
div[data-testid="stTable"]:has(tbody tr:nth-child(20)) td:last-child p { font-family: 'Charis SIL', serif !important; }
</style>
""", unsafe_allow_html=True)

language_nav("Tulu", "linguistics")

# ══════════════════════════════════════════════════════════════
# MASTHEAD
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="ling-masthead">
    <div class="ling-masthead-eyebrow">Linguistic Structure</div>
    <div class="ling-masthead-title">Tulu Numerals</div>
    <div class="ling-tags">
        <span class="ling-tag">Decimal</span>
        <span class="ling-tag">Kannada Script</span>
        <span class="ling-tag">Kannada Digits</span>
        <span class="ling-tag">Joining Forms</span>
        <span class="ling-tag">Words for Counting People</span>
        <span class="ling-tag">Dravidian</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 1 — OVERVIEW
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">System Overview</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Structural Properties</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Key Fact</div>
    <p>Tulu counts in tens and builds larger numbers by joining words, each in a special
    joining form: <span class="tu-kn">ನೂದು</span> <em>nūdu</em> 'hundred' becomes
    <span class="tu-kn">ನೂತ</span> <em>nūta-</em> in 101, <span class="tu-kn">ನೂತವೊಂಜಿ</span>
    <em>nūtavonji</em>. It is written in the Kannada script, and so are its numbers: Tulu
    has no digits of its own in Unicode.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-props">
        <span class="ling-prop-key">Base</span>
        <span class="ling-prop-val"><strong>10</strong> — <span class="tu-kn">ಪತ್ತ್</span> <em>pattụ</em></span>
        <span class="ling-prop-key">Higher units</span>
        <span class="ling-prop-val">100 <em>nūdu</em>, 1,000 <em>sāra</em>, 1,00,000 <em>lakša</em>, 1,00,00,000 <em>kōṭi</em></span>
        <span class="ling-prop-key">Joining</span>
        <span class="ling-prop-val">tens take <em>-t-</em>; 100 and 1,000 become <em>nūta-</em> and <em>sārata-</em></span>
        <span class="ling-prop-key">Script</span>
        <span class="ling-prop-val">Kannada</span>
        <span class="ling-prop-key">Digits</span>
        <span class="ling-prop-val">Kannada digits <span class="tu-kn">೦–೯</span>; none of Tulu's own are encoded</span>
        <span class="ling-prop-key">Speakers</span>
        <span class="ling-prop-val">18,46,427 in the 2011 Census of India</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>Tulu is a Dravidian language of the coastal districts of Karnataka and of Kasaragod in
    Kerala. The forms on this page come from J. Brigel's <em>A Grammar of the Tulu Language</em>
    (1872), published at the Basel Mission in Mangalore, in Kannada script with Brigel's
    romanisation; pronunciations are from Royson Norman D'Souza's 2019 list in Chan's numeral
    database. Brigel's preface calls his book the "first attempt at treating the Tulu Language
    grammatically".</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 2 — DIGITS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Digits</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Written with Kannada Digits</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="tu-digits" style="margin-bottom:.5rem">೦ ೧ ೨ ೩ ೪ ೫ ೬ ೭ ೮ ೯</div>
    <p>The digits the converter shows for Tulu are the Kannada digits above, 0 to 9. Tulu's
    historical script, Tulu-Tigalari, entered Unicode in version 16.0 (2024) with 80 characters
    and no digits; Unicode's own data lists the Kannada digits as digits of that script, and
    still does in version 18.0 (2026). The script's proposers, Vaishnavi Murthy and Vinodh Rajan,
    state that it "uses numbers from the Kannada script". Brigel's grammar of 1872 already prints
    every Tulu number with Kannada digits — <span class="tu-kn">೧ನೆ</span> for 'first'.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-subsection-title">How Tulu Came to Use Kannada Script</div>
    <p>Männer's dictionary of 1886 explains that Tulu was once written in "a modification of the
    Malayalam alphabet", which "was in vogue till the Basel Mission Press employed Canarese
    characters in printing" — Canarese being the older English name for Kannada. Brigel's
    grammar, from the same mission, uses Kannada digits throughout its numeral tables.</p>
</div>
""", unsafe_allow_html=True)

L2 = "https://www.unicode.org/L2/"
st.markdown(f"""
<div class="ling-card">
    <div class="ling-subsection-title">Proposals for Tulu Digits</div>
    <p>Seven proposals sent to Unicode since 2021 have asked for digits of Tulu's own, 0 to 9.
    All but one also ask for signs for 10 and 100, which the Karnataka Tulu Sahitya Academy's
    proposals compare with Malayalam's. The first three were part of the Academy's proposals
    for a separate modern Tulu script; the 2025 ones ask for the digits to be added to the
    Tulu-Tigalari block that Unicode encoded in 2024. None has been accepted. Each link opens
    the document on Unicode's site.</p>
    <ul>
        <li><a href="{L2}L2021/21019-tulu.pdf" target="_blank" rel="noopener">L2/21-019</a>
        — U. B. Pavanaja for the Karnataka Tulu Sahitya Academy, "Proposal to encode Tulu":
        0–9, 10 and 100.</li>
        <li><a href="{L2}L2022/22034-tulu-ktsa-proposal.pdf" target="_blank" rel="noopener">L2/22-034</a>
        — Karnataka Tulu Sahitya Academy (Akash Raj Jain), "Proposal to Encode Tulu Script in
        Unicode": 0–9, 10 and 100.</li>
        <li><a href="{L2}L2023/23021-tulu-additional.pdf" target="_blank" rel="noopener">L2/23-021</a>
        — Akash Raj Jain for the Academy, "Additional Document for Unicode Tulu Proposal": 0–9,
        10 and 100.</li>
        <li><a href="{L2}L2025/25020-tulu-tigalari-numerals.pdf" target="_blank" rel="noopener">L2/25-020</a>
        — Biswajit Mandal, "Proposal to encode Tulu-Tigalari numerals": 0–9, 10 and 100, with
        examples from manuscripts, print, handwriting and non-Unicode Tulu fonts.</li>
        <li><a href="{L2}L2025/25063-tulu-tigalari-characters.pdf" target="_blank" rel="noopener">L2/25-063</a>
        — Pravinraj S. Rao, Radhakrishna Bellur, Guru Prasad and Kekunnayya, "Proposal to Encode 4
        Characters and 1 Half-Vowel, and 12 Numerals in Tulu-Tigalari": 0–9, 10 and 100, citing
        manuscripts, alphabet books and Tulu calendars.</li>
        <li><a href="{L2}L2025/25082-tulu-tigalari-additions.pdf" target="_blank" rel="noopener">L2/25-082</a>
        — Akash Raj Jain, "Continued Proposal Document to Encode Tulu": 0–9.</li>
        <li><a href="{L2}L2025/25095-updated-tulu-proposal.pdf" target="_blank" rel="noopener">L2/25-095</a>
        — Akash Raj Jain, "Updated Proposal to Encode Modern Tulu in Unicode", which gathers the
        earlier requests: 0–9, 10 and 100.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="ling-info">
    <p><strong>What Unicode has said.</strong> Murthy and Rajan's proposal for Tulu-Tigalari,
    the one Unicode encoded, recommends the Kannada digits and says the "Tulu Numbers" shown in
    script charts "need further study before encoding them"
    (<a href="{L2}L2022/22031-tulu-tigalari-prop.pdf" target="_blank" rel="noopener">L2/22-031</a>, §7).
    In 2023 they replied that these numbers appear "only in 1 palm leaf manuscript"
    (<a href="{L2}L2023/23055-tulu-tigalari-reply.pdf" target="_blank" rel="noopener">L2/23-055</a>).
    Unicode's script working group recommended no action on Mandal's proposal in January 2025:
    the Academy had asked it to hold off on the digits, and it asked for as much manuscript
    evidence as possible in any future proposal
    (<a href="{L2}L2025/25010-script-wg-report.pdf" target="_blank" rel="noopener">L2/25-010</a>, §6.3).
    In April 2025 it again recommended no action on the 2025 proposals, until their authors
    answer the questions raised in L2/25-096 about adding modern Tulu to the Tulu-Tigalari block
    (<a href="{L2}L2025/25091r-sew-recommendations-utc183.pdf" target="_blank" rel="noopener">L2/25-091R</a>, §5.5).
    No Tulu digits are in Unicode 18.0 or in
    <a href="https://www.unicode.org/alloc/Pipeline.html" target="_blank" rel="noopener">Unicode's
    pipeline</a> of characters accepted for later versions (checked November 2026), so the
    converter uses Kannada digits and says so on every result.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 3 — ONE TO TWENTY
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Digits &amp; Bases</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">One to Twenty</div>', unsafe_allow_html=True)

st.table({
    "Number": ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
    "Tulu": ['ಒಂಜಿ', 'ರಡ್ಡ್', 'ಮೂಜಿ', 'ನಾಲ್', 'ಐನ್', 'ಆಜಿ', 'ಏಳ್', 'ಎಣ್ಮ', 'ಒರ್ಮ್ಬ', 'ಪತ್ತ್', 'ಪತ್ತೊಂಜಿ', 'ಪದ್ರಾಡ್', 'ಪದ್ಮೂಜಿ', 'ಪದ್ನಾಲ್', 'ಪದ್ನೈನ್', 'ಪದ್ನಾಜಿ', 'ಪದ್ನೇಳ್', 'ಪದ್ನೆಣ್ಮ', 'ಪದ್ನೊರ್ಮ್ಬ', 'ಇರ್ವ'],
    "Brigel (1872)": ['wonji', 'raḍḍụ', 'mūji', 'nālụ', 'einụ', 'āji', 'yēḷụ', 'yeṇma', 'wormba', 'pattụ', 'pattonji', 'padụrāḍụ', 'padụmūji', 'padụnālụ', 'padụneinụ', 'padụnāji', 'padụnēḷụ', 'padụneṇma', 'padụnormba', 'irva'],
    "Pronunciation (2019)": ['oɲd͡ʒi', 'ɾaɖɖɯ', 'muːd͡ʒi', 'naːlɯ', 'aⁱnɯ', 'aːd͡ʒi', 'eːlɯ', 'eɖma ~ enma ~ eɳma', 'oɾmba', 'pat̪t̪ɯ', 'pat̪t̪oɲd͡ʒi ~ pad̪inoɲd͡ʒi', 'pad̪ɾaːɖɯ ~ pad̪iɾaːɖɯ', 'pad̪muːd͡ʒi ~ pad̪imuːd͡ʒi', 'pad̪naːlɯ ~ pad̪inaːlɯ', 'pad̪naⁱnɯ ~ pad̪inaⁱnɯ', 'pad̪naːd͡ʒi ~ pad̪inaːd͡ʒi', 'pad̪neːlɯ ~ pad̪ineːlɯ', 'pad̪neɖma ~ pad̪ineɖma', 'pad̪noɾmba ~ pad̪inoɾmba', 'iɾʋa'],
})

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title">The Final Vowel</div>
        <p>Brigel calls it the "indefinite" vowel, "sounded nearly as the French <em>e</em> in
        <em>je</em>". He writes it with the virama, <span class="tu-kn">್</span>, and romanises
        it <em>ụ</em> after Lepsius's Standard Alphabet: <span class="tu-kn">ರಡ್ಡ್</span>
        <em>raḍḍụ</em> 'two'. D'Souza transcribes the same vowel as [ɯ].</p>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title">Eleven to Nineteen</div>
        <p>From 12 the teens begin with <em>padụ-</em>:
        <span class="tu-kn">ಪದ್ಮೂಜಿ</span> <em>padụmūji</em> 13. Eleven keeps
        <em>pattụ</em>: <em>pattonji</em>. Today D'Souza records both <em>pad-</em> and
        <em>padi-</em>, including <em>padinoɲd͡ʒi</em> beside <em>pattoɲd͡ʒi</em> for 11.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 4 — TENS AND JOINING
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Compositional Rules</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Tens and Joining Forms</div>', unsafe_allow_html=True)

st.table({
    "Value": ['20', '30', '40', '50', '60', '70', '80', '90'],
    "Tulu": ['ಇರ್ವ', 'ಮುಪ್ಪ', 'ನಾಲ್ಪ', 'ಐವ', 'ಅಜಿಪ', 'ಎಳ್ಪ', 'ಎಣ್ಪ', 'ಸೊಣ್ಪ'],
    "Brigel (1872)": ['irva', 'muppa', 'nālpa', 'eiva', 'ajipa', 'yeḷpa', 'yeṇpa', 'soṇpa'],
    "Pronunciation (2019)": ['iɾʋa', 'muppa', 'nalpa', 'aⁱʋa', 'ad͡ʒpa', 'elpa', 'eɳpa', 'soɳpa ~ sonpa'],
})

st.markdown("""
<div class="ling-info">
    <p>Männer's dictionary (1886) also records <em>yerpa</em> for 70, and <em>ajippa</em> beside
    <em>ajipa</em> for 60, "also" <span class="tu-kn">ಆಜಿಪ</span> <em>ājipa</em>. The converter
    shows them as other recorded forms.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[ten]-t-[unit] &nbsp;·&nbsp; nūta-[rest] &nbsp;·&nbsp; [how many] sāra · sārata-[rest]</span>
</div>
""", unsafe_allow_html=True)

st.table({
    "Number": ['21', '22', '25', '39', '101', '150', '1,001', '1,020', '1,200', '11,000'],
    "Tulu": ['ಇರ್ವತೊಂಜಿ', 'ಇರ್ವತ್ರಡ್ಡ್', 'ಇರ್ವತ್ಐನ್', 'ಮುಪ್ಪತೊರ್ಮ್ಬ', 'ನೂತವೊಂಜಿ', 'ನೂತಐವ', 'ಸಾರತವೊಂಜಿ', 'ಸಾರತಇರ್ವ', 'ಸಾರತಇರ್ನೂದು', 'ಪತ್ತೊಂಜಿಸಾರ'],
    "Brigel (1872)": ['irvatonji', 'irvatụraḍḍụ', 'irvatụeinụ', 'muppatormba', 'nūtavonji', 'nūtaeiva', 'sāratavonji', 'sāratairva', 'sāratairnūdu', 'pattonjisāra'],
    "Built as": ['20 + 1', '20 + 2', '20 + 5', '30 + 9', '100 + 1', '100 + 50', '1,000 + 1', '1,000 + 20', '1,000 + 200', '11 × 1,000'],
})

st.markdown("""
<div class="ling-card">
    <p>A ten joins its unit with <em>-t-</em>: <em>irvatụraḍḍụ</em> 22. Brigel explains that a
    word beginning with <em>o</em> or <em>e</em> is pronounced with <em>wo</em> or <em>ye</em>, so
    he romanises one and nine as <em>wonji</em> and <em>wormba</em>, though the Kannada spelling
    has no <em>w</em>. After the <em>-t-</em> of a ten the glide drops (<em>irvatonji</em> 21),
    and after <em>nūta-</em> or <em>sārata-</em> it becomes <em>v</em> (<em>nūtavonji</em> 101). Brigel stops at 25 with
    "etc.", but Männer's dictionary gives 39 as <em>muppa</em> plus <em>tormba</em>, the same
    pattern in the thirties. All the forms in this table except 39 are printed by Brigel; 39 is
    Männer's.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 5 — HUNDREDS AND ABOVE
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Larger Numbers</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Hundreds, Thousands, Lakh and Crore</div>', unsafe_allow_html=True)

st.table({
    "Value": ['100', '200', '300', '400', '500', '600', '700', '800', '900', '1,000', '10,000', '1,00,000', '1,00,00,000'],
    "Tulu": ['ನೂದು', 'ಇರ್ನೂದು', 'ಮುನ್ನೂದು', 'ನಾಲ್ನೂದು', 'ಐನೂದು', 'ಆಜಿನೂದು', 'ಏಳ್ನೂದು', 'ಎಣ್ಮನೂದು', 'ಒರ್ಮ್ಬನೂದು', 'ಸಾರ', 'ಪತ್ತ್ಸಾರ', 'ಲಕ್ಷ', 'ಕೋಟಿ'],
    "Brigel (1872)": ['nūdu', 'irnūdu', 'munnūdu', 'nālụnūdu', 'einūdu', 'ājinūdu', 'yēḷụnūdu', 'yeṇmanūdu', 'wormbanūdu', 'sāra', 'pattụsāra', 'lakša', 'kōṭi'],
})

st.markdown("""
<div class="ling-info">
    <p>Brigel also gives <em>nānūdu</em> for 400, and prints large numbers with Indian grouping
    (1,00,000). For 1,000 both lists in Chan's database, from 1995 and 2019, give
    <em>saːvira</em> or <em>saːʋiɾa</em> rather than Brigel's <em>sāra</em>, though the 1995
    list keeps <em>saːra</em> in 2,000. Zero is <span class="tu-kn">ಸೊನ್ನೆ</span>
    <em>sonnè</em>, 'the nought, cipher', in Männer's dictionary — the same word names the
    small circle <span class="tu-kn">ಂ</span> of the script.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 6 — PEOPLE, ORDER, TIMES
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Syntax &amp; Morphology</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Counting People, Ordinals and Times</div>', unsafe_allow_html=True)

st.table({
    "Value": ["1", "1", "2", "3", "4", "5", "6", "7", "8"],
    "Form": ["ಒರಿ", "ಒರ್ತಿ", "ಇರ್ವೆರ್", "ಮೂವೆರ್", "ನಾಲ್ವೆರ್", "ಐವೆರ್", "ಆಜ್ವೆರ್", "ಏಳ್ವೆರ್", "ಎಣ್ಮ ಮಂದೆ"],
    "Romanised (Brigel 1872)": ["wori", "worti", "irverụ", "mūverụ", "nālverụ", "eiverụ", "ājverụ",
                      "yēḷverụ", "yeṇma mande"],
    "Meaning": ["one (man)", "one (woman)", "two people", "three people", "four people",
                "five people", "six people", "seven people", "eight people"],
})

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title">People and Things</div>
        <p>Brigel's "substantive numerals" count people with their own words: one man is
        <em>wori</em>, one woman <em>worti</em>, one thing <em>wonji</em>, and two to seven
        take <em>-verụ</em>. From seven upwards, he notes, <em>mande</em> 'people' is added to
        the number: <em>yeṇma mande</em> 'eight people', <em>pattụ mande</em> 'ten people'.</p>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title">First, Second, Once, Twice</div>
        <p>Ordinals add <em>-ane</em>: <em>wonjane</em> 'first', <em>raḍḍane</em> 'second',
        <em>pattane</em> 'tenth'. For 'times' Brigel gives three sets: <em>wora</em>,
        <em>irvoḷu</em>, <em>mukkoḷu</em> (only up to five); <em>worvāra</em>,
        <em>irvāra</em>, <em>muttāra</em> (only these three); and <em>wonji sarti</em>,
        <em>raḍḍụ sarti</em>, <em>mūji sarti</em>, which go on.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 7 — SPEAKERS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Speakers</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Tulu in the Census of India</div>', unsafe_allow_html=True)

st.table({
    "Census": ["1971", "1981", "1991", "2001", "2011"],
    "Speakers": ["11,58,419", "14,17,224", "15,52,259", "17,22,768", "18,46,427"],
    "Growth over the decade": ["—", "22.34%", "9.53%", "10.98%", "7.18%"],
})

st.markdown("""
<div class="ling-info">
    <p>From the Census of India 2011, Paper 1 of 2018 (Language), which lists Tulu among the
    non-scheduled languages. The number of speakers is still rising, though more slowly than
    in the 1970s. In 1886 Männer put it at half a million. UNESCO's <em>Atlas of the World's
    Languages in Danger</em> (third edition, 2010) marks Tulu as vulnerable on its map of the
    Indian subcontinent (Map 21), the least severe of the five categories in its legend,
    which run from vulnerable to extinct.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 8 — LIMITS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Limits of the Converter</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">What Is and Is Not Implemented</div>', unsafe_allow_html=True)

st.table({
    "Feature": ["0 to 99,999", "Lakh and crore", "Multiples of a lakh", "Kannada digits",
                "Alternative forms", "Pronunciation", "Counting people, ordinals, times"],
    "Status": ["Implemented", "Implemented", "Not implemented", "Shown and accepted",
               "Shown and accepted", "Partial", "Described above"],
    "Basis": ["Brigel's forms and patterns; 39 from Männer",
              "Brigel prints both words",
              "No example of how lakh combines",
              "Unicode 18.0; Brigel (1872)",
              "nānūdu 400 (Brigel); ajippa and ājipa 60, yerpa 70 (Männer)",
              "D'Souza (2019), for the numbers in that list",
              "Brigel (1872), §§77–80"],
})

# ══════════════════════════════════════════════════════════════
# SECTION 9 — SOURCES
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Sources</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">References</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p><strong>Brigel, J.</strong> 1872. <em>A Grammar of the Tulu Language</em>. Mangalore:
    C. Stolz, Basel Mission Book &amp; Tract Depository. §§3 and 6 on the vowels, §§76–80,
    pp. 41–43, on the numerals; forms transcribed from the page images.</p>
    <p><strong>Männer, A.</strong> 1886. <em>Tulu–English Dictionary</em>. Mangalore: Basel
    Mission Press. Preface; entries <em>muppa</em> (p. 551), <em>sonnè</em> (p. 661),
    <em>yerpa</em>, <em>ajipa</em> (p. 11).</p>
    <p><strong>D'Souza, Royson Norman.</strong> 2019; and <strong>Shetty, Ramakrishna T.</strong>
    1995. Tulu. In Eugene S. L. Chan, <em>Numeral Systems of the World's Languages</em>. Max
    Planck Institute for Evolutionary Anthropology.</p>
    <p><strong>Office of the Registrar General, India.</strong> 2018. <em>Census of India 2011,
    Paper 1 of 2018: Language</em>.</p>
    <p><strong>Moseley, Christopher</strong> (ed.). 2010. <em>Atlas of the World's Languages in
    Danger</em>, 3rd edition. Paris: UNESCO. Map 21, Indian Subcontinent.</p>
    <p><strong>Unicode Consortium.</strong> <em>Unicode 18.0.0</em> (2026): UnicodeData.txt and
    ScriptExtensions.txt; the Unicode pipeline, checked November 2026. <strong>Script Encoding
    Working Group.</strong> 2025. Recommendations to UTC #182 (L2/25-010) and #183
    (L2/25-091R). <strong>Murthy, Vaishnavi &amp; Vinodh Rajan.</strong> 2022. "Updated proposal
    to encode the Tulu-Tigalari script in Unicode", L2/22-031; 2023. "Disunification of
    Tulu-Tigalari script &amp; Invented Tulu Script", L2/23-055. The seven proposals for Tulu
    digits are listed, with links, under <em>Proposals for Tulu Digits</em> above.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p><strong>A note on claims not used.</strong> The
    standard modern grammars, by D. N. S. Bhat (1967 and 1998), were not available and were not
    consulted. Brigel's type writes the <em>m</em> of <em>wormba</em> (9) as the circle
    <span class="tu-kn">ಂ</span>; Unicode text cannot place the <em>r</em>-sign after that
    circle, so the converter writes <span class="tu-kn">ಒರ್ಮ್ಬ</span>, which looks almost the
    same.</p>
</div>
""", unsafe_allow_html=True)

footer_nav("Tulu", "linguistics")
