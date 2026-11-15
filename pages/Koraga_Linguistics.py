import string
from urllib.parse import quote

import streamlit as st
from ui import apply_global_styles, LING_CSS, LING_WIDTH_CSS, language_nav, footer_nav

st.set_page_config(page_title="Koraga Numerals — Linguistics", layout="wide")
apply_global_styles()
st.markdown(LING_CSS, unsafe_allow_html=True)
st.markdown(LING_WIDTH_CSS, unsafe_allow_html=True)

# ── Tables (defined first so the font subset below covers every character) ──
# Forms as printed: Sharma (1990) in IPA, Bhat (1971) in his romanisation,
# KIRTADS (2019) in Latin letters and Malayalam. The Kerala column gives the
# handbook's word list, or its Table 7 where the list has no form; both lists
# are set out in KERALA_LISTS. Tulu is Brigel's (1872); * marks a Tulu form
# built by Brigel's patterns rather than printed by him.
ONE_TO_TWENTY = {
    "Number": [
        "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16",
        "17", "18", "19", "20",
    ],
    "Korra Koraga (Sharma 1990)": [
        "oñji", "rəɖɖɨ", "muːjɨ", "naːli", "aynɨ", "aːji", "eːlɨ", "eɖma", "ormba", "pattɨ",
        "pattoñjɨ", "pattɨrəɖɖɨ", "pattimuːjɨ", "pattɨnaːli", "pattɨaynɨ", "pattɨaːji",
        "pattɨeːli", "padieɖma", "padnormba", "irwa",
    ],
    "Onti (Bhat 1971)": [
        "onji", "raḍḍɨ", "mu:ji", "na:lɨ", "aynɨ", "—", "e:lɨ", "—", "—", "—", "—", "—", "—",
        "—", "—", "—", "—", "—", "—", "—",
    ],
    "Tappu (Bhat 1971)": [
        "onji", "naḍḍɨ", "mu:ji", "—", "—", "—", "e:rɨ", "—", "—", "—", "hattonji", "hadra:ḍɨ",
        "—", "—", "—", "—", "—", "—", "—", "—",
    ],
    "Mudu (Bhat 1971)": [
        "unji", "eyḍɨ", "mu:ji", "—", "—", "—", "yo:ḷu", "—", "—", "—", "—", "hanneyḍɨ", "—",
        "—", "—", "—", "—", "—", "—", "—",
    ],
    "Kerala (KIRTADS 2019)": [
        "onji", "rRaḍdu", "mūji", "nāḷu", "aīṇu", "āji", "ēḷu", "eṇumma", "oRumPa", "pattu",
        "pattonji", "patRāḍu/padrādē", "patimūji", "patnāḷu", "—", "—", "patinēḷu", "patinenma",
        "patuRmba/patineRumba", "iRuva",
    ],
    "Tulu (Brigel 1872), for reference": [
        "wonji", "raḍḍụ", "mūji", "nālụ", "einụ", "āji", "yēḷụ", "yeṇma", "wormba", "pattụ",
        "pattonji", "padụrāḍụ", "padụmūji", "padụnālụ", "padụneinụ", "padụnāji", "padụnēḷụ",
        "padụneṇma", "padụnormba", "irva",
    ],
}

HIGHER = {
    "Number": [
        "20", "30", "40", "50", "60", "70", "80", "90", "100", "200", "300", "400", "500",
        "600", "700", "800", "900", "1,000", "4,000", "5,000", "6,000", "7,000", "8,000",
        "9,000", "10,000", "1,00,000",
    ],
    "Korra Koraga (Sharma 1990)": [
        "irwa", "muppa", "nalpa", "aywa", "aːjipa", "eːlipa", "eɖmawa", "conpa", "nuːdu", "—",
        "—", "—", "—", "—", "—", "—", "—", "caːwra", "—", "—", "—", "—", "—", "—", "—", "—",
    ],
    "Onti (Bhat 1971)": [
        "—", "—", "—", "ayva", "ajippa", "—", "—", "—", "—", "—", "—", "—", "—", "—", "—", "—",
        "—", "—", "—", "—", "—", "—", "—", "—", "—", "—",
    ],
    "Kerala (KIRTADS 2019)": [
        "iRuva", "muppa", "naluppa", "aiūva", "ajippa", "ēlippa/elippa", "eṇippa",
        "conuppa/soṇuppa", "nūdu", "iRnūdu/raḍunūdu", "munnudu/mūjinūdu", "nalṇudu", "aīṇudu",
        "ājinudu", "ēḷnudu", "eṇmanudu", "oRmanudu", "cāiRam/onjisāiRam/sāviRa", "nalsaavira",
        "ayinusaavira", "aaji saavira", "eelu savira", "enma saavira", "orumpa saavira",
        "pattu saavira", "lacca",
    ],
    "Tulu (Brigel 1872), for reference": [
        "irva", "muppa", "nālpa", "eiva", "ajipa", "yeḷpa", "yeṇpa", "soṇpa", "nūdu", "irnūdu",
        "munnūdu", "nālụnūdu", "einūdu", "ājinūdu", "yēḷụnūdu", "yeṇmanūdu", "wormbanūdu",
        "sāra", "nālụsāra*", "einụsāra*", "ājisāra*", "yēḷụsāra*", "yeṇmasāra*", "wormbasāra*",
        "pattụsāra", "lakša",
    ],
}

DIALECTS = {
    "Number": [
        "1", "2", "7", "11", "12",
    ],
    "Onti": [
        "onji", "raḍḍɨ", "e:lɨ", "—", "—",
    ],
    "Tappu": [
        "onji", "naḍḍɨ", "e:rɨ", "hattonji", "hadra:ḍɨ",
    ],
    "Mudu": [
        "unji", "eyḍɨ", "yo:ḷu", "—", "hanneyḍɨ",
    ],
    "Bhat compares it with": [
        "Tulu oñji", "Tulu raḍḍɨ (beside Onti); Tappu cross-referred", "Kannada e:ḷu",
        "Tulu pattoñji", "Tulu padra:ḍɨ (Tappu); Kannada hanneraḍu (Mudu)",
    ],
}

KERALA_LISTS = {
    "Number": [
        "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "17", "18",
        "19", "20", "30", "40", "50", "60", "70", "80", "90", "100", "200", "300", "400", "500",
        "600", "700", "800", "900", "1,000", "4,000", "5,000", "6,000", "7,000", "8,000",
        "9,000", "10,000", "1,00,000",
    ],
    "Table 7 (pp. 107–108)": [
        "oñji", "reddu", "muuji", "naalu", "ayinu", "aaji", "eelu", "enme", "orumpa", "pattu",
        "—", "—", "—", "—", "—", "—", "—", "—", "—", "—", "—", "—", "—", "—", "—", "nuutu", "—",
        "—", "—", "—", "—", "—", "—", "—", "saavira", "nalsaavira", "ayinusaavira",
        "aaji saavira", "eelu savira", "enma saavira", "orumpa saavira", "pattu saavira",
        "lacca",
    ],
    "Table 7, Malayalam": [
        "ഒഞ്ജി", "രെഡ്ഡു", "മൂജി", "നാലു", "അയിനു", "ആജി", "ഏളു", "എൺമ", "ഒരുമ്പ", "പത്തു", "—",
        "—", "—", "—", "—", "—", "—", "—", "—", "—", "—", "—", "—", "—", "—", "നൂതു", "—", "—",
        "—", "—", "—", "—", "—", "—", "സാവിര", "നൽസവീര", "അയിനുസവീര", "ആജി സാവിര", "ഏളു സാവിര",
        "എൻമ സാവിര", "ഒരുമ്പ സാവിര", "പത്തു സാവിര", "ലച്ച",
    ],
    "Word list (pp. 166–169)": [
        "onji", "rRaḍdu", "mūji", "nāḷu", "aīṇu", "āji", "ēḷu", "eṇumma", "oRumPa", "pattu",
        "pattonji", "patRāḍu/padrādē", "patimūji", "patnāḷu", "patinēḷu", "patinenma",
        "patuRmba/patineRumba", "iRuva", "muppa", "naluppa", "aiūva", "ajippa", "ēlippa/elippa",
        "eṇippa", "conuppa/soṇuppa", "nūdu", "iRnūdu/raḍunūdu", "munnudu/mūjinūdu", "nalṇudu",
        "aīṇudu", "ājinudu", "ēḷnudu", "eṇmanudu", "oRmanudu", "cāiRam/onjisāiRam/sāviRa", "—",
        "—", "—", "—", "—", "—", "—", "—",
    ],
    "Word list, Malayalam": [
        "ഒൻജി", "റഡ്ഡു", "മൂജി", "നാളു", "അയിണു", "ആജി", "ഏളു", "എണുമ്മ", "ഒറുമ്പ", "പത്തു",
        "പത്തെൻജി", "പത്രാണ്ടു", "പതിമൂജി", "പത്നാളു", "പതിനേളു", "പതിനേന്മ", "പതുറുമ്ബ",
        "ഇറുവ", "മുപ്പ", "നലുപ്പ", "അയ്വ", "അജിപ്പ", "ഏലിപ്പ", "എണിപ്പ", "ചൊണുപ്പ", "നൂദു",
        "ഇർനൂദു", "മൂന്നുദു", "നൽണുദു", "അയ്ണുദു", "അജിനുദു", "ഏള്നുദു", "എൺമനുദു", "ഒർമനുദു",
        "ചായിറം", "—", "—", "—", "—", "—", "—", "—", "—",
    ],
}

_TABLE_TEXT = "".join("".join(v) if isinstance(v, list) else "" for t in (ONE_TO_TWENTY, HIGHER, DIALECTS, KERALA_LISTS)
                      for v in t.values())
_CHARIS = "".join(sorted({c for c in _TABLE_TEXT if ord(c) < 0x0D00 or ord(c) > 0x0D7F}
                         | set(string.ascii_letters + string.digits + string.punctuation + " —–·")))

st.markdown("""
<style>
/* Charis SIL, subset to the characters used, for the IPA and romanised forms;
   Malayalam for the Kerala forms */
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+Malayalam:wght@400;600&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Charis+SIL&text=""" + quote(_CHARIS) + """&display=swap');
.ko-f { font-family: 'Charis SIL', 'Crimson Pro', serif; font-size: .9em; }
.ko-ml { font-family: 'Noto Serif Malayalam', serif; }
div[data-testid="stTable"] td, div[data-testid="stTable"] td p {
    font-family: 'Charis SIL', 'Noto Serif Malayalam', 'Crimson Pro', serif !important; }
</style>
""", unsafe_allow_html=True)

language_nav("Koraga", "linguistics")

# ══════════════════════════════════════════════════════════════
# MASTHEAD
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="ling-masthead">
    <div class="ling-masthead-eyebrow">Linguistic Structure</div>
    <div class="ling-masthead-title">Koraga Numerals</div>
    <div class="ling-tags">
        <span class="ling-tag">Decimal</span>
        <span class="ling-tag">Recorded Forms Only</span>
        <span class="ling-tag">Dialects</span>
        <span class="ling-tag">No Script of Its Own</span>
        <span class="ling-tag">Critically Endangered</span>
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
    <p>Koraga's numbers are known only in pieces. Three sources, from 1971 to 2019, record 45
    numbers between them: 1 to 20, the tens, the hundreds, 1,000, the thousands from 4,000 to
    10,000, and a lakh. None records a number between the tens, such as 21, or between the
    hundreds, such as 101, so how Koraga builds them is not documented in any source consulted
    here, and the converter does not guess.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-props">
        <span class="ling-prop-key">Base</span>
        <span class="ling-prop-val"><strong>10</strong> — <span class="ko-f">pattɨ</span> (Sharma), <em>pattu</em> (KIRTADS)</span>
        <span class="ling-prop-key">Recorded</span>
        <span class="ling-prop-val">1–20, the tens, the hundreds, 1,000, 4,000–10,000, 1,00,000</span>
        <span class="ling-prop-key">Dialects</span>
        <span class="ling-prop-val">Onti, Tappu, Mudu and Ande (Bhat 1971)</span>
        <span class="ling-prop-key">Script</span>
        <span class="ling-prop-val">None of its own; the sources use IPA, a romanisation, and Malayalam script</span>
        <span class="ling-prop-key">Digits</span>
        <span class="ling-prop-val">None of its own</span>
        <span class="ling-prop-key">People</span>
        <span class="ling-prop-val">16,477 Koraga in the 2011 Census; speakers of the language not counted</span>
        <span class="ling-prop-key">UNESCO</span>
        <span class="ling-prop-val">Critically endangered (<em>Atlas of the World's Languages in Danger</em>, 2010)</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>Koraga is the language of the Koraga, a Scheduled Tribe of the coast of Karnataka and of
    Kasaragod in Kerala. The 1891 census of Madras counted it as a dialect of Tulu. D. N. S.
    Bhat's sketch of three of its dialects (1971) concludes that Koraga is "a distinct language
    of the Dravidian family", only remotely connected to Tulu, even though its speakers are
    bilingual in Tulu or Kannada.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 2 — SOURCES
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Sources</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Where the Numbers Come From</div>', unsafe_allow_html=True)

st.table({
    "Source": ["Bhat (1971)", "Sharma (1990), in Chan's database", "KIRTADS (2019)"],
    "Variety and place": [
        "Onti (Udupi), Tappu (Hebri) and Mudu (Coondapur), Karnataka",
        "Korra Koraga, Karnataka",
        "Koraga of Kasaragod district, Kerala"],
    "Numbers recorded": [
        "1, 2, 3, 4, 5, 7, 11, 12, 50 and 60, scattered through a comparative vocabulary",
        "1 to 20, the tens, 100 and 1,000",
        "Two lists: Table 7 has 1 to 10, 100, 1,000, 4,000 to 10,000 and 1,00,000; a word list "
        "has 1 to 20, the tens, the hundreds and 1,000"],
    "Written in": ["Bhat's romanisation", "IPA", "Latin letters and Malayalam script"],
})

st.markdown("""
<div class="ling-card">
    <div class="ling-subsection-title">Reading the Sources</div>
    <p>Bhat's monograph has no chapter on numbers; its forms come from his comparative
    vocabulary, where each word is marked o, t or m for Onti, Tappu or Mudu. They were read from
    the page images, because the scanned text drops his diacritics (<span class="ko-f">eyḍɨ</span>
    comes out as <em>eydi</em>). The Kerala handbook, prepared by S. K. Shyam for the Kerala
    Institute for Research, Training and Development Studies of Scheduled Castes and Scheduled
    Tribes (KIRTADS), gives each number in Latin letters and in Malayalam, in two lists set out
    below. Its Latin letters are taken from the PDF's text; its Malayalam, set in an older
    Malayalam font, was read from the page images and checked against that font's
    encoding.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 3 — ONE TO TWENTY
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Digits &amp; Bases</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">One to Twenty</div>', unsafe_allow_html=True)

st.table(ONE_TO_TWENTY)

st.markdown("""
<div class="ling-card">
    <div class="ling-subsection-title">The Teens</div>
    <p>Sharma's teens put ten before the unit: <span class="ko-f">pattɨ</span> + <span
    class="ko-f">rəɖɖɨ</span> gives <span class="ko-f">pattɨrəɖɖɨ</span> 12, and <span
    class="ko-f">pattoñjɨ</span> 11 runs ten and one together. His 18 and 19 begin with
    <em>pad-</em> instead (<span class="ko-f">padieɖma</span>, <span class="ko-f">padnormba</span>),
    and 13 is written <span class="ko-f">pattimuːjɨ</span>, with <em>i</em> where the others have
    <span class="ko-f">ɨ</span>. The Kerala word list also puts ten first, as <em>patt-</em>,
    <em>pat-</em> or <em>pati-</em> (<em>pattonji</em> 11, <em>patimūji</em> 13,
    <em>patinēḷu</em> 17), and Tulu does the same, as <em>patt-</em> in 11 and <em>padụ-</em> in
    12 to 19. Bhat records only Tappu's 11 and 12 and Mudu's 12. The word list's rows for 15 and
    16 are set aside, for the reason given below.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 4 — HIGHER NUMBERS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Higher Numbers</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Tens, Hundreds and Thousands</div>', unsafe_allow_html=True)

st.table(HIGHER)

st.markdown("""
<div class="ling-card">
    <div class="ling-subsection-title">What the Higher Numbers Show</div>
    <p>Sharma's tens end in <em>-pa</em> or <em>-wa</em> (<span class="ko-f">muppa</span>,
    <span class="ko-f">aywa</span>, <span class="ko-f">eɖmawa</span>), as Brigel's Tulu tens end
    in <em>-pa</em> or <em>-va</em>. Sharma's 90, <span class="ko-f">conpa</span>, and 1,000,
    <span class="ko-f">caːwra</span>, begin with <em>c</em> where Tulu has <em>soṇpa</em> and
    <em>sāra</em>, and the Kerala word list, recorded three decades later, has the same
    <em>c</em> in <em>conuppa</em> and <em>cāiRam</em>. Only the word list records the hundreds:
    a unit before <em>nūdu</em>, as in <em>iRnūdu</em> 200 and <em>eṇmanudu</em> 800, the
    pattern of Tulu's <em>irnūdu</em> and <em>yeṇmanūdu</em>. Table 7 builds 4,000 to 10,000
    with the multiplier first, <em>pattu saavira</em> 'ten thousand', as Tulu does with
    <em>pattụsāra</em>. Tulu forms marked * are built by Brigel's patterns; he does not print
    them.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 5 — DIALECTS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Dialects</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">One Language, Two Neighbours</div>', unsafe_allow_html=True)

st.table(DIALECTS)

st.markdown("""
<div class="ling-card">
    <div class="ling-subsection-title">Following Tulu, Following Kannada</div>
    <p>Bhat took Onti from Udupi, Tappu from Hebri and Mudu from Coondapur. He found Ande midway
    between Tappu and Onti, and the speech of Mangalore close to Onti. He reports that all Mudu
    speakers are bilingual in Kannada and all Onti speakers in Tulu, and concludes that each dialect
    has followed its neighbour's sound changes and borrowed its words. The numbers show this:
    Bhat compares Mudu's 7 and 12 with Kannada, and Onti's and Tappu's forms with Tulu. The
    <em>Dravidian Etymological Dictionary</em> lists Mudu <span class="ko-f">eyḍi</span> 'two'
    under the same entry as Kannada <em>eraḍu</em> and Tulu <em>raḍḍů</em> (entry 474).</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-subsection-title">Tappu: p Becomes h</div>
    <p>Bhat sets Tappu <span class="ko-f">hattonji</span> 11 and <span class="ko-f">hadra:ḍɨ</span>
    12 beside Tulu <em>pattoñji</em> and <em>padra:ḍɨ</em>, with other words such as
    <span class="ko-f">he:ri</span> 'milk' beside Tulu <em>pe:ri</em> (p. 42): at the start of a
    word, Tappu has <em>h</em> where Tulu has <em>p</em>. He notes that the same change affected
    all known dialects of Kannada, some time around the tenth century.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 5b — THE KERALA HANDBOOK
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">The Kerala Handbook</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Two Lists, Two Spellings</div>', unsafe_allow_html=True)

st.table(KERALA_LISTS)

st.markdown("""
<div class="ling-card">
    <p>The handbook gives the numbers twice: in Table 7 (pp. 107–108) and in a list of 'words
    related to numbers' (pp. 166–169). The two lists spell differently (<em>reddu</em> and
    <em>rRaḍdu</em> for 2, <em>enme</em> and <em>eṇumma</em> for 8, <em>saavira</em> and
    <em>cāiRam</em>, <em>onjisāiRam</em> or <em>sāviRa</em> for 1,000), and the Latin and
    Malayalam of one entry do not always agree: Table 7 writes 8 as <em>enme</em> but എൺമ, and
    the word list writes 11 as <em>pattonji</em> but പത്തെൻജി. The converter shows every
    spelling as printed. A third spelling of 500, <em>aiņûdu</em> (ഐനൂഡു), appears among the
    handbook's examples of vowels (p. 53).</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p><strong>Rows set aside.</strong> The word list prints <em>patnāji</em> (or
    <em>patineni</em>) as 'fifteen' and <em>patinainu</em> as 'sixteen' (p. 167). Their second
    parts, <em>āji</em> 'six' and <em>ainu</em> 'five', point the other way, so the two rows
    look swapped, and the converter uses neither. The row for 'seventeen' reads
    <em>patinenma/patinēḷu</em>, but its Malayalam has only പതിനേളു (<em>patinēḷu</em>), and
    <em>patinenma</em> is the list's own word for 18, so only <em>patinēḷu</em> is used for
    17.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 6 — PEOPLE AND TIMES
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Counting People</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Two People, Two Times</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Bhat records separate words for 'two persons': Onti <span class="ko-f">irverɨ</span>, the
    same as the Tulu word he cites beside it, and Mudu <span class="ko-f">eḍḍaḷɨ</span>
    (pp. 90–91). Onti <em>sarti</em> means 'times' (p. 113). His Onti story uses them in passing
    (p. 58):</p>
    <ul>
        <li><span class="ko-f">raḍḍɨ sarti</span> 'twice'</li>
        <li><span class="ko-f">raḍḍɨ gante</span> 'two o'clock'</li>
        <li><span class="ko-f">onji ayna:ji janaka</span> 'for five or six people'</li>
        <li><span class="ko-f">onji ayva ajippa jana</span> 'some fifty to sixty people'</li>
    </ul>
    <p style="margin-top:.5rem">Two numbers side by side give a range: 'five or six', 'fifty to
    sixty'.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 7 — KORAGA AND TULU
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Relationships</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Koraga and Tulu</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>The sources disagree about how close Koraga is to Tulu. Glottolog places Koraga in its
    South-Western Dravidian group, with Tulu, Bellari and Kudiya. Bhat (pp. 2–3) argues that the likeness
    to Tulu and Kannada comes from long bilingualism, and lists grammatical features, such as a
    past tense in <em>k</em>, that he says bring Koraga closer to the North Dravidian languages
    Kurux, Malto and Brahui. The numbers cannot settle the question: almost all recorded Koraga
    numerals resemble Tulu's, but the speakers have been bilingual in Tulu or Kannada, by Bhat's
    estimate, for a thousand years or more.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 8 — PEOPLE
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Speakers</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">The Koraga in the Census of India</div>', unsafe_allow_html=True)

st.table({
    "Census": ["1961", "1971", "1981", "1991", "2001", "2011"],
    "Karnataka": ["6,382", "7,620", "15,146", "16,322", "16,071", "14,794"],
    "Kerala": ["—", "1,200", "1,098", "1,651", "1,152", "1,582"],
})

st.markdown("""
<div class="ling-info">
    <p>These figures count the Koraga people, a Scheduled Tribe and a Particularly Vulnerable
    Tribal Group, not speakers of the language; the 2011 Census also counted 101 Koraga in Tamil
    Nadu. The census of languages does not list Koraga, because mother tongues with fewer than
    10,000 speakers are folded into "Others" under a larger language. Bhat (1971, p. 1) put the
    speakers at about a thousand. The Kerala handbook found few speakers in Kasaragod; even
    around Badiyadka, where it was spoken best, what it found was a mixture of Koraga and Tulu. UNESCO's <em>Atlas of the World's
    Languages in Danger</em> (2010) marks Koraga critically endangered on its map of the Indian
    subcontinent (Map 21); Glottolog rates Korra Koraga threatened and Mudu Koraga shifting.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 9 — LIMITS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Limits of the Converter</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">What Is and Is Not Implemented</div>', unsafe_allow_html=True)

st.table({
    "Feature": ["1 to 20, the tens, the hundreds, 1,000", "4,000 to 10,000, 1,00,000",
                "Onti, Tappu and Mudu forms", "Numbers between the tens (21, 35 …)",
                "Numbers between the hundreds (101 …), other thousands", "Zero", "Above 1,00,000",
                "Numbers built by pattern", "Koraga digits", "Reading Koraga"],
    "Status": ["Shown, from Sharma (1990) and the Kerala word list, with the other sources "
               "where they record them",
               "Shown, from the Kerala handbook's Table 7",
               "Shown wherever Bhat (1971) records them",
               "Refused: no source records them",
               "Refused: no source records them",
               "Refused: no source records a word for zero",
               "Refused",
               "Never: every form shown is printed in a source",
               "None exist; numbers are written in Arabic numerals",
               "Any spelling from the three sources, with or without accents and length marks, "
               "or the handbook's Malayalam"],
})

# ══════════════════════════════════════════════════════════════
# SECTION 10 — SOURCES
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Sources</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">References</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p><strong>Bhat, D. N. S.</strong> 1971. <em>The Koraga Language</em>. Linguistic Survey of
    India Series 7. Poona: Deccan College Postgraduate and Research Institute. Introduction,
    pp. 1–3; comparative study, pp. 42–43; texts, pp. 58 and 67; comparative vocabulary,
    pp. 88–115; forms read from the page images.</p>
    <p><strong>Sharma, S. R.</strong> 1990. Korra Koraga. In Eugene S. L. Chan, <em>Numeral
    Systems of the World's Languages</em>. Max Planck Institute for Evolutionary
    Anthropology.</p>
    <p><strong>KIRTADS</strong> (prepared by S. K. Shyam). 2019. <em>Pasaru (Butterfly):
    Preparation of Handbook for Koraga Language of Koraga Community in Kerala State</em>.
    Kozhikode: Kerala Institute for Research, Training and Development Studies of Scheduled
    Castes and Scheduled Tribes. Table 7, pp. 107–108; word list, pp. 166–169; p. 53.</p>
    <p><strong>Brigel, J.</strong> 1872. <em>A Grammar of the Tulu Language</em>. Mangalore:
    C. Stolz, Basel Mission Book &amp; Tract Depository. <strong>D'Souza, Royson
    Norman.</strong> 2019. Tulu. In Chan, <em>Numeral Systems of the World's Languages</em>.</p>
    <p><strong>Burrow, T. &amp; M. B. Emeneau.</strong> 1984. <em>A Dravidian Etymological
    Dictionary</em>, 2nd edition. Oxford: Clarendon Press. Entry 474.</p>
    <p><strong>Ministry of Tribal Affairs, Government of India.</strong> 2013. <em>Statistical
    Profile of Scheduled Tribes in India</em>. Tables 1.24 and 1.25.
    <strong>Office of the Registrar General, India.</strong> 2018. <em>Census of India 2011,
    Paper 1 of 2018: Language</em>, paragraph 9.</p>
    <p><strong>Moseley, Christopher</strong> (ed.). 2010. <em>Atlas of the World's Languages in
    Danger</em>, 3rd edition. Paris: UNESCO. Map 21, Indian Subcontinent.
    <strong>Hammarström, Harald, et al.</strong> <em>Glottolog</em>, entry Koraga (kora1289),
    with endangerment from Campbell et al. (2022); consulted November 2026.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p><strong>A note on claims not used.</strong> Chan's database and Wikipedia say that the
    Koraga of Kerala speak Mudu Koraga. Bhat recorded Mudu at Coondapur in Karnataka, the Kerala
    handbook does not call its variety Mudu, and its numbers (<em>oñji</em>, <em>reddu</em>,
    <em>eelu</em>) are close to Bhat's Onti and to Tulu rather than to his Mudu
    (<span class="ko-f">unji</span>, <span class="ko-f">eyḍɨ</span>, <span
    class="ko-f">yo:ḷu</span>), so this page names the Kerala forms by place only. Speaker
    numbers of 45–50 (Wikipedia, citing a newspaper opinion piece), about 14,000 (Chan's
    database) and 16,665 from the 1981 census (a newspaper report) could not be traced to a
    count of speakers and are not used. A website lists Koraga numbers as <em>ondu</em>,
    <em>eradu</em> … <em>ombattu</em>, citing the Central Institute of Indian Languages without
    naming a document; these are the Kannada words, and no Koraga source above has them. In one Onti
    text Bhat translates <span class="ko-f">padra:ḍɨ dina</span> as 'fifteen days' (p. 67),
    although <span class="ko-f">padra:ḍɨ</span> is twelve in Tulu and in his vocabulary; the
    text is not used for numbers. Three rows of the handbook's word list are set aside, as
    explained above. The fullest grammar, Ramakrishna T. Shetty's <em>Koraga
    Grammar</em> (1978 thesis; Dravidian University, 2008), could not be obtained and was not
    consulted.</p>
</div>
""", unsafe_allow_html=True)

footer_nav("Koraga", "linguistics")
