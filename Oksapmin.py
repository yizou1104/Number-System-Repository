"""
Oksapmin body-tally data and logic, shared by the converter and
linguistics pages.
"""
import re

# ============================================================
# OKSAPMIN BODY TALLY
#
# Oksapmin (Tekin Valley, Sandaun Province, Papua New Guinea) counts
# along 27 points of the upper body: thumb to little finger, up the
# arm, across the face to the nose (14), and down the other side.
# Each number is the name of a body part; tən 'side' marks the
# second half.
#
# Two dialects are documented, and they disagree on the order of the
# second hand: Upper Oksapmin runs thumb-first again (23 = thumb),
# Lower Oksapmin mirrors the first hand (23 = little finger).
#
# Sources, transcribed as printed:
#   Upper  Lawrence, M. (2018), in Chan, Numeral Systems of the
#          World's Languages; Saxe (1981), as printed in Saxe &
#          Esmonde (2004), fig. 1.
#   Lower  Loughnane (2009) A Grammar of Oksapmin, Table 1-5 (1-16);
#          Loughnane (2008), in Chan (17-27).
# Script g (U+0261) in the Chan entries is written here as plain g.
# ============================================================

# ── Counting forms ───────────────────────────────────────────
# Each entry: (forms, gloss). The first form is the citation form;
# the rest are variants printed by the same source.
UPPER = {
    1:  (["tiβəna", "tiβən"], "thumb"),
    2:  (["tipneɾip", "tipneɾipᶲ"], "index finger"),
    3:  (["bumɾup", "bumɾupᶲ"], "middle finger"),
    4:  (["xətɾip", "xətɾipᶲ"], "ring finger"),
    5:  (["xətxəta", "xətxət"], "little finger"),
    6:  (["doβa", "dop", "dopᶲ"], "inner wrist"),
    7:  (["beza", "bes"], "forearm"),
    8:  (["kiɾ"], "elbow"),
    9:  (["towat"], "upper arm"),
    10: (["kata", "kat"], "shoulder"),
    11: (["gweɾa", "gweɾ"], "side of neck"),
    12: (["nata", "nat"], "ear"),
    13: (["kina", "kin"], "eye"),
    14: (["ɾuma", "ɾum"], "nose"),
    15: (["tən kina", "tən kin"], "side eye"),
    16: (["tən nata", "tən nat"], "side ear"),
    17: (["tən gweɾ"], "side side of neck"),
    18: (["tən kata", "tən kat"], "side shoulder"),
    19: (["tən towat"], "side upper arm"),
    20: (["tən kiɾ"], "side elbow"),
    21: (["tən beza", "tən bez"], "side forearm"),
    22: (["tən doβa", "tən dop", "tən dopᶲ"], "side inner wrist"),
    23: (["tən tiβəna", "tən tiβən"], "side thumb"),
    24: (["tən tipneɾip", "tən tipneɾipᶲ"], "side index finger"),
    25: (["tən bumɾup", "tən bumɾupᶲ"], "side middle finger"),
    26: (["tən xətɾip", "tən xətɾipᶲ"], "side ring finger"),
    27: (["tən xətxəta", "tən xətxət"], "side little finger"),
}

# Lawrence: from 23 to the end "the word tən is often left out".
TEN_DROPPED_FROM = 23

# Saxe's (1981) transcription of the same Upper Oksapmin count. ^ is his
# symbol for the central vowel. The caption prints 17 and 23 without the
# hyphen (tangwer, tantip^na); it is restored here for consistency.
SAXE = {
    1: "tip^na", 2: "tipnarip", 3: "bum rip", 4: "h^tdip", 5: "h^th^ta",
    6: "dopa", 7: "besa", 8: "kir", 9: "tow^t", 10: "kata", 11: "gwer",
    12: "nata", 13: "kina", 14: "aruma", 15: "tan-kina", 16: "tan-nata",
    17: "tan-gwer", 18: "tan-kata", 19: "tan-tow^t", 20: "tan-kir",
    21: "tan-besa", 22: "tan-dopa", 23: "tan-tip^na", 24: "tan-tipnarip",
    25: "tan-bum rip", 26: "tan-h^tdip", 27: "tan-h^th^ta",
}

LOWER = {
    1:  (["tipun", "tupun"], "thumb"),
    2:  (["ləwatipun"], "index finger"),
    3:  (["bumlip"], "middle finger"),
    4:  (["xətlip"], "ring finger"),
    5:  (["xətxət"], "little finger"),
    6:  (["xadəp"], "wrist"),
    7:  (["bes"], "forearm"),
    8:  (["amun"], "elbow"),
    # Table 1-5 has tuwət; the grammar's example (1-7) has təwət.
    9:  (["tuwət", "təwət"], "upper arm"),
    10: (["kat"], "shoulder"),
    11: (["gwel"], "side of neck"),
    12: (["nat"], "ear"),
    13: (["kin"], "eye"),
    14: (["lum"], "nose"),
    15: (["kin tən", "tən kin"], "(other) side eye"),
    16: (["nat tən", "tən nat"], "(other) side ear"),
    # 17-27: Loughnane's 2008 database entry; the grammar stops at 16.
    17: (["gwel tən"], "(other) side of neck"),
    18: (["kat tən"], "(other) shoulder"),
    19: (["tuwət tən"], "(other) side upper arm"),
    20: (["amun tən"], "(other) side elbow"),
    21: (["bes tən"], "(other) side forearm"),
    22: (["xadəp tən"], "(other) side wrist"),
    23: (["xətxət tən"], "(other) side little finger"),
    24: (["xətlip tən"], "(other) side ring finger"),
    25: (["bumlip tən"], "(other) side middle finger"),
    26: (["ləwatipun tən"], "(other) side index finger"),
    27: (["tipun tən"], "(other) side thumb"),
}

DIALECTS = {"upper": UPPER, "lower": LOWER}

# ── Forms for counting things ────────────────────────────────
# Upper: Lawrence (2018) gives a full quantity series; from 6 it is the
# counting form plus the quantity marker -xeⁱ.
UPPER_QUANTITY = {
    1: "tita ~ tit", 2: "yota ~ yot", 3: "yitiɾ", 4: "yotayota ~ yotyot",
    5: "xətxət timbəs ~ xanin", 6: "doβxeⁱ", 7: "besxeⁱ", 8: "kiɾxeⁱ",
    9: "towatxeⁱ", 10: "katxeⁱ", 11: "gweɾxeⁱ", 12: "natxeⁱ", 13: "kinxeⁱ",
    14: "ɾumxeⁱ", 15: "tən kinxeⁱ", 16: "tən natxeⁱ", 17: "tən gweɾxeⁱ",
    18: "tən katxeⁱ", 19: "tən towatxeⁱ", 20: "tən kiɾxeⁱ", 21: "tən besxeⁱ",
    22: "tən dopxeⁱ", 23: "tən tiβənxeⁱ", 24: "tən tipneɾipxeⁱ",
    25: "tən bumɾupxeⁱ", 26: "tən xətɾipxeⁱ", 27: "tən xətxətxeⁱ",
}

# Lower: Loughnane (2009). Body parts act as numerals by taking the
# possessive =xe (§1.2.5, §6.3.2). Forms marked "attested" occur in her
# examples; "by rule" applies that stated rule to a single-word body
# part. Where =xe falls in a phrase with tən is not documented, so
# 15-27 are left out rather than guessed.
LOWER_QUANTITY = {
    1: ("pitle ~ pitil", "attested", "ex. 4-47; the older tit 'one' survives only in compounds"),
    3: ("ot=a tit=a", "attested", "ex. 4-48, 'two and one'"),
    4: ("xətxət tibəs", "attested", "ex. 1-8, 'no little finger'"),
    5: ("xanengon ~ xətxət=xe", "attested", "ex. 1-9 'fist'; ex. 7-42 'little finger's'"),
    6: ("xadəp=xe", "attested", "ex. 6-48, 'wrist's'"),
    8: ("amun=xe", "attested", "ex. 1-6, 'elbow's'"),
    10: ("kat=xe", "attested", "ex. 7-43, 'shoulder's'"),
}
for _n in (7, 9, 11, 12, 13, 14):
    LOWER_QUANTITY[_n] = (f"{LOWER[_n][0][0]}=xe", "by rule", "body part + =xe 'POSS'")

# ── Beyond 27 ────────────────────────────────────────────────
# Saxe & Esmonde (2004): past 27 one "continues up to the wrist, forearm,
# and on up and around the body"; the 21st and 29th points are both
# tan-besa. Only those two steps are described, so only they are given.
SECOND_CIRCUIT = {28: 22, 29: 21}

MAX_COUNT = 27


def number_to_oksapmin(n, dialect="upper"):
    """Citation form for a count of n."""
    if not isinstance(n, int) or n < 1:
        raise ValueError(
            "The count begins at the thumb with one. There is no body point "
            "for zero or for negative numbers."
        )
    table = DIALECTS[dialect]
    if n <= MAX_COUNT:
        return table[n][0][0]
    if dialect == "upper" and n in SECOND_CIRCUIT:
        return table[SECOND_CIRCUIT[n]][0][0]
    raise ValueError(
        f"{n} is beyond the documented count. One circuit of the body is 27"
        + (" (tit pu, 'once around the body'); Saxe & Esmonde describe the count "
           "turning back up the arm only as far as 29." if dialect == "upper"
           else "; no source describes how Lower Oksapmin continues past it.")
    )


def saxe_spelling(n):
    """Saxe's (1981) transcription of the Upper Oksapmin form."""
    return SAXE[SECOND_CIRCUIT.get(n, n)]


def literal(n, dialect="upper"):
    """The source's own literal gloss, e.g. Lawrence's 'side side of neck'."""
    if n > MAX_COUNT:
        return DIALECTS[dialect][SECOND_CIRCUIT[n]][1]
    return DIALECTS[dialect][n][1]


def gloss(n, dialect="upper"):
    """Plain description of the body point: 'ear', 'other ear'."""
    where, part = path(dialect)[SECOND_CIRCUIT.get(n, n) - 1]
    return f"other {part}" if where == "second" else part


def variants(n, dialect="upper"):
    if n > MAX_COUNT:
        return []
    return DIALECTS[dialect][n][0][1:]


def side(n):
    if n > MAX_COUNT:
        return "second side, on a second pass"
    if n == 14:
        return "centre — the turning point"
    return "first side" if n < 14 else "second side"


# ── Reverse direction ───────────────────────────────────────
def fold(text):
    """
    Reduce a spelling to Lawrence's practical orthography, in which ə is
    written a, x is h, β is p and ɾ is r. Saxe's ^ is the same vowel. This
    lets Saxe's tip^na, Lawrence's tiβəna and a typed 'tipana' meet.
    """
    s = text.lower().strip()
    for old, new in (("ɡ", "g"), ("ə", "a"), ("^", "a"), ("x", "h"), ("β", "p"),
                     ("ɾ", "r"), ("ᶲ", ""), ("ⁱ", "i")):
        s = s.replace(old, new)
    s = re.sub(r"[-=()~,.]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def _build_index():
    index = {}

    def add(form, n, dialect, role, note=""):
        entry = (n, dialect, role, note)
        bucket = index.setdefault(fold(form), [])
        if entry not in bucket:
            bucket.append(entry)

    for dialect, table in DIALECTS.items():
        for n, (forms, _) in table.items():
            for form in forms:
                add(form, n, dialect, "counting")
    for n, (forms, _) in UPPER.items():
        if n >= TEN_DROPPED_FROM:
            for form in forms:
                add(form.removeprefix("tən "), n, "upper", "counting",
                    "with tən left out, as Lawrence notes is common from 23")
    for n, form in SAXE.items():
        add(form, n, "upper", "counting", "Saxe's spelling")
    for n, form in UPPER_QUANTITY.items():
        for part in form.split(" ~ "):
            add(part, n, "upper", "counting things")
    for n, (form, status, _) in LOWER_QUANTITY.items():
        for part in form.split(" ~ "):
            add(part, n, "lower", "counting things",
                "by rule" if status == "by rule" else "")
    add("tit pu", 27, "upper", "unit", "'once around the body'")
    return index


INDEX = _build_index()


def oksapmin_lookup(text):
    """Every documented reading of a form: [(n, dialect, role, note), ...]."""
    if not text or not text.strip():
        raise ValueError("Enter an Oksapmin form.")
    hits = INDEX.get(fold(text))
    if not hits:
        raise ValueError(
            "Not recognised. Try a documented form such as 'nata' (12), "
            "'tən kina' (15) or 'tipun tən' (27, Lower Oksapmin)."
        )
    return sorted(hits, key=lambda h: (h[0], h[1] != "upper"))


def oksapmin_to_number(text):
    """First documented reading of a form as a number."""
    return oksapmin_lookup(text)[0][0]


# ── Body diagram ────────────────────────────────────────────
# Points on a front-facing figure, first side on the viewer's left. The
# sources do not say which hand starts, so the drawing does not either.
_FIRST = {
    "thumb": (40, 300), "index finger": (50, 331), "middle finger": (63, 338),
    "ring finger": (76, 334), "little finger": (87, 322), "wrist": (70, 290),
    "forearm": (79, 252), "elbow": (88, 214), "upper arm": (100, 172),
    "shoulder": (113, 130), "side of neck": (157, 110), "ear": (133, 64),
    "eye": (157, 58),
}
POINTS = {("first", k): v for k, v in _FIRST.items()}
POINTS.update({("second", k): (340 - x, y) for k, (x, y) in _FIRST.items()})
POINTS[("centre", "nose")] = (170, 74)

_ARM = ["thumb", "index finger", "middle finger", "ring finger", "little finger",
        "wrist", "forearm", "elbow", "upper arm", "shoulder", "side of neck",
        "ear", "eye"]


def path(dialect):
    """Body point for each count 1-27."""
    seq = [("first", p) for p in _ARM] + [("centre", "nose")]
    back = [("second", p) for p in reversed(_ARM[5:])]          # eye ... wrist
    fingers = _ARM[:5] if dialect == "upper" else list(reversed(_ARM[:5]))
    return seq + back + [("second", p) for p in fingers]


def body_svg(dialect, active=None):
    seq = path(dialect)
    active_key = None
    if active:
        active_key = seq[(SECOND_CIRCUIT.get(active, active)) - 1]
    lines = [
        '<svg viewBox="0 0 340 360" class="ok-body" xmlns="http://www.w3.org/2000/svg">',
        '<circle cx="170" cy="66" r="34" class="ok-skin"/>',
        '<rect x="158" y="96" width="24" height="24" class="ok-skin-flat"/>',
        '<path d="M113 130 Q170 112 227 130 L214 300 Q170 312 126 300 Z" class="ok-skin"/>',
        '<polyline points="113,130 100,172 88,214 79,252 70,290" class="ok-limb"/>',
        '<polyline points="227,130 240,172 252,214 261,252 270,290" class="ok-limb"/>',
        '<ellipse cx="65" cy="312" rx="16" ry="18" class="ok-skin"/>',
        '<ellipse cx="275" cy="312" rx="16" ry="18" class="ok-skin"/>',
    ]
    for i, key in enumerate(seq, start=1):
        x, y = POINTS[key]
        on = key == active_key
        lines.append(f'<circle cx="{x}" cy="{y}" r="{7 if on else 3.4}" '
                     f'class="{"ok-pt-on" if on else "ok-pt"}"/>')
        dx = -12 if key[0] == "first" else (12 if key[0] == "second" else 0)
        dy = 4
        if key[1] == "eye":
            dx, dy = 0, -10
        elif key[1] == "nose":
            dy = 20
        elif key[1] in ("index finger", "middle finger", "ring finger"):
            dx, dy = 0, 17
        elif key[1] == "little finger":
            dx = -dx                     # label toward the body, clear of the palm
        anchor = "middle" if dx == 0 else ("end" if dx < 0 else "start")
        lines.append(f'<text x="{x + dx}" y="{y + dy}" text-anchor="{anchor}" '
                     f'class="{"ok-num-on" if on else "ok-num"}">{i}</text>')
    lines.append("</svg>")
    return "".join(lines)


# Styles for body_svg, for any page that draws the figure.
OK_SVG_CSS = """<style>
.ok-body{width:100%;max-width:400px;display:block;margin:0 auto}
.ok-skin{fill:var(--parchment-3);stroke:var(--rule-strong);stroke-width:1.2}
.ok-skin-flat{fill:var(--parchment-3)}
.ok-limb{fill:none;stroke:var(--parchment-3);stroke-width:17;stroke-linecap:round;stroke-linejoin:round}
.ok-pt{fill:var(--ink-faint)}
.ok-pt-on{fill:var(--accent);stroke:var(--card-bg);stroke-width:2}
.ok-num{font-family:'DM Mono',monospace;font-size:9px;fill:var(--ink-muted)}
.ok-num-on{font-family:'DM Mono',monospace;font-size:12px;font-weight:700;fill:var(--accent)}
</style>"""
