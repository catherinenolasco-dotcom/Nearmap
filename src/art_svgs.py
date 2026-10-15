"""Original illustrative panels for the tool cards. Generic sample shapes, no real product UI, no real data.
Colors are recolored to the Nearmap-inspired palette at the end of this file."""
import re

F = "font-family:Figtree,sans-serif"
INK = "#2b2729"  # source ink, mapped below


def t(x, y, s, size=9, w=600, c=INK, anchor="start"):
    return f'<text x="{x}" y="{y}" style="{F};font-size:{size}px;font-weight:{w};fill:{c}" text-anchor="{anchor}">{s}</text>'


def panel(x, y, w, h, rot=0, extra=""):
    return (f'<g transform="rotate({rot} {x+w/2} {y+h/2})"><rect x="{x+3}" y="{y+4}" width="{w}" height="{h}" fill="{INK}" opacity=".12"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#fff"/>{extra}</g>')


def bar(x, y, w, c, h=6):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}"/>'


def dot(x, y, r, c):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>'


def hris():
    e = t(128, 42, "Org chart", 10, 700)
    e += f'<rect x="215" y="52" width="60" height="22" fill="#5d7446"/>' + dot(227, 63, 5, "#fff") + bar(236, 60, 30, "#fff", 3) + bar(236, 66, 22, "#ffffffaa", 3)
    e += f'<path d="M245 74 V86 M170 86 H320 M170 86 V96 M245 86 V96 M320 86 V96" stroke="{INK}" stroke-width="1.2" fill="none"/>'
    for x, c in ((140, "#6da4a4"), (215, "#ff8fb2"), (290, "#b8a3ae")):
        e += f'<rect x="{x}" y="96" width="60" height="22" fill="{c}"/>' + dot(x+12, 107, 5, "#fff") + bar(x+21, 104, 30, "#fff", 3) + bar(x+21, 110, 22, "#ffffffaa", 3)
    for x in (140, 215, 290):
        e += f'<path d="M{x+30} 118 V128" stroke="{INK}" stroke-width="1.2"/><rect x="{x+8}" y="128" width="44" height="16" fill="#efe5da"/>' + bar(x+14, 134, 30, INK + "55", 3)
    return ("#d9dcd9", '<path d="M0 0 L190 0 Q150 100 210 200 L0 200Z" fill="#b8a3ae"/><path d="M300 120 L400 100 L400 200 L280 200Z" fill="#5d7446"/>' + panel(118, 22, 262, 140, -2, e))


def ats(title="Hiring pipeline", names=("Applied", "Screen", "Interview", "Offer")):
    e = t(124, 40, title, 10, 700)
    cols = [(names[0], "#6da4a4", 3), (names[1], "#ff8247", 2), (names[2], "#ac8c37", 2), (names[3], "#5d7446", 1)]
    x = 124
    for n, c, k in cols:
        e += f'<rect x="{x}" y="50" width="58" height="4" fill="{c}"/>' + t(x, 66, n, 8, 600)
        for i in range(k):
            y = 72 + i * 28
            e += f'<rect x="{x}" y="{y}" width="58" height="24" fill="#faf3ec"/>' + dot(x+9, y+12, 4.5, c) + bar(x+18, y+8, 34, INK + "66", 3) + bar(x+18, y+14, 22, INK + "33", 3)
        x += 66
    return ("#e9dcc0", '<path d="M0 60 Q90 10 150 70 L170 200 L0 200Z" fill="#ac8c37"/><path d="M300 0 L400 0 L400 90 Q340 70 300 0Z" fill="#ff8fb2"/>' + panel(112, 22, 272, 150, 2, e))


def perf():
    e = t(128, 42, "Review cycle", 10, 700)
    rows = [("Self reviews", 0.9, "#6da4a4"), ("Manager reviews", 0.65, "#ff8247"), ("Calibration", 0.35, "#5d7446"), ("Goals set", 0.8, "#b8a3ae")]
    for i, (n, v, c) in enumerate(rows):
        y = 58 + i * 26
        e += t(128, y + 8, n, 8.5, 600) + f'<rect x="215" y="{y}" width="150" height="9" fill="#efe5da"/>' + f'<rect x="215" y="{y}" width="{150*v}" height="9" fill="{c}"/>'
    return ("#d3e2e2", '<path d="M120 0 L400 0 L400 200 L0 200Z" fill="#b8a3ae"/><path d="M20 40 L100 30 L120 150 L30 165Z" fill="#5d7446"/>' + panel(118, 24, 262, 140, 0, e))


def comp():
    e = t(128, 42, "Audit readiness", 10, 700)
    items = ["SOPs reviewed and owned", "Access reviews complete", "Evidence collected", "Policies acknowledged"]
    for i, n in enumerate(items):
        y = 56 + i * 26
        e += f'<rect x="128" y="{y}" width="16" height="16" fill="#5d7446"/><path d="M132 {y+8} l4 4 l6 -8" stroke="#fff" stroke-width="2" fill="none"/>' + t(152, y + 12, n, 9.5, 600)
    e += f'<path d="M335 62 l24 8 v20 q0 18 -24 28 q-24 -10 -24 -28 v-20z" fill="#ff8fb2"/><path d="M325 92 l8 8 l14 -16" stroke="{INK}" stroke-width="3" fill="none"/>'
    return ("#f3d6c4", '<path d="M0 0 L200 0 Q160 100 230 200 L0 200Z" fill="#ff8247"/><path d="M290 110 L400 90 L400 200 L280 200Z" fill="#718484"/>' + panel(116, 22, 268, 140, -2, e))


def ai():
    e = t(124, 42, "Employee action flow", 10, 700)
    nodes = [("Request", "#6da4a4"), ("Approve", "#ff8247"), ("Update HRIS", "#ac8c37"), ("Audit trail", "#5d7446")]
    for i, (n, c) in enumerate(nodes):
        x = 124 + i * 66
        tc = "#fff" if c in ("#5d7446", "#ac8c37") else INK
        e += f'<rect x="{x}" y="72" width="56" height="34" fill="{c}"/>' + t(x + 28, 93, n, 8.5, 700, tc, "middle")
        if i < 3:
            e += f'<path d="M{x+56} 89 h10" stroke="{INK}" stroke-width="1.5"/><path d="M{x+62} 85 l4 4 l-4 4" stroke="{INK}" stroke-width="1.5" fill="none"/>'
    e += f'<rect x="124" y="124" width="250" height="26" fill="#faf3ec"/>' + t(136, 141, "Documented, approved, recorded", 9, 600)
    return ("#e5e0d2", '<path d="M0 150 Q100 20 220 90 T400 60 L400 200 L0 200Z" fill="#718484"/><path d="M40 20 L100 10 L112 70 L50 80Z" fill="#ac8c37"/>' + panel(112, 22, 272, 150, 1.5, e))


def rep():
    e = t(128, 42, "People metrics", 10, 700)
    hs = [38, 54, 46, 70, 62, 84]
    cs = ["#6da4a4", "#ff8247", "#6da4a4", "#ff8247", "#6da4a4", "#ff8247"]
    for i, h in enumerate(hs):
        e += f'<rect x="{132+i*24}" y="{150-h}" width="16" height="{h}" fill="{cs[i]}"/>'
    e += f'<path d="M132 120 L160 104 L190 112 L220 86 L250 92 L280 70" stroke="{INK}" stroke-width="2" fill="none"/>'
    e += f'<rect x="300" y="56" width="70" height="36" fill="#faf3ec"/>' + bar(308, 66, 40, INK + "66", 4) + bar(308, 76, 28, INK + "33", 4)
    e += f'<rect x="300" y="100" width="70" height="36" fill="#faf3ec"/>' + bar(308, 110, 34, INK + "66", 4) + bar(308, 120, 46, INK + "33", 4)
    return ("#ecd7de", '<path d="M200 0 L400 0 L400 140 Q300 120 200 200Z" fill="#ff8fb2"/><path d="M0 90 L100 60 L120 200 L0 200Z" fill="#5d7446"/>' + panel(116, 22, 268, 146, -1.5, e))


def hub():
    c = "".join(dot(x, y, r, col) for x, y, r, col in [(500, 75, 38, "#ff8247"), (380, 60, 26, "#ff8fb2"), (620, 62, 28, "#5d7446"), (300, 100, 20, "#ac8c37"), (700, 98, 22, "#b8a3ae"), (560, 122, 16, "#718484"), (440, 118, 14, "#faf3ec")])
    lines = f'<path d="M500 75 L380 60 M500 75 L620 62 M380 60 L300 100 M620 62 L700 98 M500 75 L560 122 M500 75 L440 118" stroke="{INK}" stroke-width="1.5"/>'
    return ("#6da4a4", '<path d="M0 100 Q250 40 520 100 T1000 70 L1000 150 L0 150Z" fill="#dfe6d6"/><path d="M780 20 L940 10 L960 140 L790 150Z" fill="#ff8247" opacity=".9"/><path d="M40 60 L200 40 L220 150 L50 150Z" fill="#b8a3ae"/>' + lines + c, "0 0 1000 150")


# ---- Recolor to the Nearmap palette: ink #08112e, blue #3448ff, mist #deeeef, slate #27455c, lime #cbf69f ----
MAP = {
    "#2b2729": "#08112e",
    "#5d7446": "#3448ff", "#6da4a4": "#8fa0ff", "#ff8247": "#cbf69f", "#ac8c37": "#27455c",
    "#ff8fb2": "#deeeef", "#b8a3ae": "#3448ff", "#718484": "#27455c", "#faf3ec": "#f4f8f8",
    "#efe5da": "#e3ecee", "#dfe6d6": "#eaf0ff",
    "#d9dcd9": "#deeeef", "#e9dcc0": "#e8ecff", "#d3e2e2": "#eaf7da", "#f3d6c4": "#deeeef",
    "#e5e0d2": "#e8ecff", "#ecd7de": "#eaf7da",
}
_RX = re.compile("|".join(re.escape(k) for k in MAP), re.I)


def recolor(s):
    return _RX.sub(lambda m: MAP[m.group(0).lower()], s)


def _wrap(fn):
    def inner(*a, **k):
        r = fn(*a, **k)
        return tuple(recolor(x) if isinstance(x, str) and i < 2 else x for i, x in enumerate(r))
    return inner


hris, ats, perf, comp, ai, rep, hub = map(_wrap, (hris, ats, perf, comp, ai, rep, hub))
ARTS = [hris, ats, perf, comp, ai, rep]
