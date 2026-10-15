"""Builds the Nearmap-styled portfolio. Usage: python3 -I build_portfolio.py <outDir>
Writes index.html (standalone, fonts and headshot embedded) and artifact.html (fragment using Google Fonts)."""
import base64, html, sys
from pathlib import Path
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
from content import *
import art_svgs

e = html.escape
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE.parent
FONTS = Path("/home/claude/nearmap/fonts/node_modules/@fontsource")
HEADSHOT = HERE.parent / "headshot.jpg"
if not HEADSHOT.exists():
    HEADSHOT = HERE / "headshot.jpg"

def b64(p): return base64.b64encode(Path(p).read_bytes()).decode()

def font_css():
    out = ""
    for fam, d, ws in (("Figtree", "figtree", (400, 600, 700, 800)), ("Sora", "sora", (600, 700))):
        for w in ws:
            out += "@font-face{font-family:'%s';font-weight:%d;font-style:normal;font-display:swap;src:url(data:font/woff2;base64,%s) format('woff2');}" % (fam, w, b64(FONTS / d / "files" / f"{d}-latin-{w}-normal.woff2"))
    return out

CSS = r"""
:root{--ink:#08112e;--blue:#3448ff;--mist:#deeeef;--slate:#27455c;--lime:#cbf69f;--white:#fff;--pale:#f3f8f8;--periwinkle:#8fa0ff;--ink2:#27455c;
--display:'Sora','Figtree',Arial,sans-serif;--body:'Figtree',Arial,sans-serif;--mono:'Figtree',Arial,sans-serif;--beige:#deeeef;--cream:#f3f8f8;--orange:#3448ff}
*{box-sizing:border-box}
html{scroll-behavior:smooth;color-scheme:light}
body{margin:0;background:#fff;color:var(--ink);font-family:var(--body);font-size:17px;line-height:1.6;-webkit-font-smoothing:antialiased}
h1,h2,h3,h4{font-family:var(--display);color:var(--ink);margin:0;line-height:1.12}
p{margin:0}
a{color:var(--blue)}
.wrap{max-width:1180px;margin:0 auto;padding-left:max(20px,env(safe-area-inset-left,0px));padding-right:max(20px,env(safe-area-inset-right,0px))}
.ann{background:var(--ink);color:#fff;text-align:center;font-size:14px;font-weight:600;padding:10px 16px}
.ann b{color:var(--lime)}
.nav{position:sticky;top:env(safe-area-inset-top,0px);z-index:20;background:#fff;border-bottom:1px solid var(--mist)}
.nav .wrap{display:flex;align-items:center;gap:20px;min-width:0;padding-top:12px;padding-bottom:12px}
.brand{font-family:var(--display);font-weight:700;font-size:18px;white-space:nowrap;color:var(--ink);text-decoration:none}
.brand i{display:inline-block;width:12px;height:12px;border-radius:50%;background:var(--blue);margin-right:8px}
.links{display:flex;gap:4px;overflow-x:auto;min-width:0;flex:1;justify-content:safe flex-end;scrollbar-width:none}
.links::-webkit-scrollbar{display:none}
.links a{white-space:nowrap;text-decoration:none;color:var(--ink);font-weight:600;font-size:14px;padding:8px 10px;border-radius:6px}
.links a:hover{background:var(--mist)}
.btn{display:inline-block;background:var(--blue);color:#fff;font-weight:700;font-size:16px;text-decoration:none;padding:14px 24px;border-radius:6px;border:2px solid var(--blue)}
.btn.ghost{background:transparent;color:var(--ink);border-color:var(--ink)}
.btn.dark{background:var(--ink);border-color:var(--ink)}
.hero{background:var(--mist);position:relative;overflow:hidden;padding:72px 0 80px}
.hero:before{content:"";position:absolute;right:-120px;top:-140px;width:520px;height:520px;border-radius:50%;background:var(--blue);opacity:.12}
.hero:after{content:"";position:absolute;left:-90px;bottom:-120px;width:300px;height:300px;border-radius:50%;background:var(--lime);opacity:.55}
.hero .wrap{position:relative;z-index:1;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,340px);gap:48px;align-items:center}
.eyebrow{font-weight:700;font-size:14px;letter-spacing:.04em;color:var(--blue);margin-bottom:16px}
h1{font-size:clamp(40px,6vw,80px);font-weight:700;letter-spacing:-.01em}
.tag{font-family:var(--display);font-weight:600;font-size:clamp(20px,2.6vw,30px);color:var(--blue);margin-top:14px}
.target{font-size:19px;margin-top:20px;max-width:52ch}
.target b{font-weight:800}
.keys{display:flex;flex-wrap:wrap;gap:8px;font-size:14px;font-weight:700;color:var(--slate);margin-top:18px;max-width:64ch}
.keys span{background:#ffffffaa;border:1px solid #b9cfd2;border-radius:6px;padding:5px 10px}
.cta{display:flex;gap:12px;flex-wrap:wrap;margin-top:28px}
.photo{position:relative;justify-self:center;width:100%;max-width:320px}
.photo:before{content:"";position:absolute;inset:18px -18px -18px 18px;background:var(--lime);border-radius:16px}
.photo img{position:relative;display:block;width:100%;height:auto;border-radius:16px;border:4px solid var(--ink)}
.stats{background:var(--ink);color:#fff}
.stats .wrap{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:0}
.stat{padding:34px 22px;border-left:1px solid #ffffff22}
.stat:first-child{border-left:0}
.stat b{display:block;font-family:var(--display);font-size:clamp(30px,4vw,46px);color:var(--lime);line-height:1.1}
.stat span{font-size:15px;color:#d5dcff}
section{padding:84px 0}
section.alt{background:var(--pale)}
section.mist{background:var(--mist)}
.kick{font-weight:700;font-size:14px;color:var(--blue);margin-bottom:12px}
h2{font-size:clamp(30px,4.2vw,48px);font-weight:700;max-width:22ch}
.lede{font-size:19px;color:var(--slate);margin-top:16px;max-width:62ch}
.sumlist{list-style:none;margin:36px 0 0;padding:0;display:grid;gap:14px;max-width:880px}
.sumlist li{background:#fff;border:1px solid var(--mist);box-shadow:inset 6px 0 0 var(--blue);border-radius:10px;padding:18px 22px 18px 28px}
.fit{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,330px),1fr));gap:20px;margin-top:40px}
.fcard{border-radius:14px;padding:30px 26px 32px;min-width:0}
.fcard small{display:block;font-weight:700;font-size:13px;letter-spacing:.06em;text-transform:uppercase;margin-bottom:12px;opacity:.85}
.fcard h3{font-size:22px;margin-bottom:12px;color:inherit}
.fcard p{font-size:16px}
.f0{background:var(--blue);color:#fff}.f1{background:var(--ink);color:#fff}.f2{background:var(--lime);color:var(--ink)}.f3{background:var(--slate);color:#fff}.f4{background:var(--mist);color:var(--ink)}.f5{background:#fff;color:var(--ink);border:2px solid var(--ink)}
.res{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,340px),1fr));gap:20px;margin-top:40px}
.rcard{--a:var(--blue);background:#fff;border-radius:14px;padding:34px 26px 28px;box-shadow:inset 0 6px 0 var(--a);min-width:0}
.rcard:nth-child(3n+2){--a:var(--lime)}.rcard:nth-child(3n){--a:var(--slate)}
.rcard b{display:block;font-family:var(--display);font-size:clamp(38px,5vw,54px);line-height:1.05;color:var(--blue)}
.rcard strong{display:block;font-size:18px;margin:8px 0 6px}
.rcard span{color:var(--slate);font-size:15px}
.cases{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,460px),1fr));gap:26px;margin-top:40px}
.case{background:#fff;border:1px solid #d3e1e3;border-radius:14px;overflow:hidden;display:flex;flex-direction:column;min-width:0}
.case .stripe{height:10px;background:var(--c);flex:none}
.case .in{padding:26px 26px 30px;display:flex;flex-direction:column;gap:14px;flex:1}
.case h3{font-size:24px}
.emp{font-size:14px;font-weight:700;color:var(--slate)}
.case h4{font-family:var(--body);font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--blue);margin-bottom:4px;font-weight:800}
.case p{font-size:16px}
.callout{background:var(--mist);border-radius:10px;padding:14px 16px}
.callout p{font-weight:600}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:auto;padding-top:6px}
.chips span{background:var(--ink);color:#fff;font-size:12px;font-weight:700;padding:7px 11px;border-radius:6px}
.vals{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr));gap:20px;margin-top:40px}
.val{--a:var(--blue);background:#fff;border-radius:14px;padding:26px 26px 26px 34px;box-shadow:inset 8px 0 0 var(--a);min-width:0}
.val:nth-child(2){--a:var(--lime)}.val:nth-child(3){--a:var(--slate)}.val:nth-child(4){--a:var(--periwinkle)}.val:nth-child(5){--a:var(--ink)}
.val h3{font-size:24px;margin-bottom:10px;color:var(--blue)}
.val small{display:block;font-weight:700;color:var(--slate);font-size:12px;letter-spacing:.06em;text-transform:uppercase;margin-bottom:6px}
.jobs{margin-top:40px;display:grid;gap:22px}
.job{background:#fff;border:1px solid #d3e1e3;border-radius:14px;padding:28px;min-width:0}
.job .jh{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;align-items:baseline}
.job h3{font-size:22px}.job h3 span{color:var(--blue)}
.job .dt{font-weight:700;color:var(--slate);font-size:15px}
.job .meta{font-size:14px;color:var(--slate);margin:6px 0 14px}
.job ul{margin:0;padding-left:20px;display:grid;gap:9px;font-size:16px}
.job li::marker{color:var(--blue)}
.job .sub{margin-top:20px;padding-top:18px;border-top:1px dashed #b9cfd2}
.earlier{margin-top:22px}
.earlier h3{font-size:20px;margin-bottom:10px}
.earlier ul{margin:0;padding-left:20px;display:grid;gap:6px;font-size:15px;color:var(--slate)}
.arc{margin-top:40px;background:#fff;border-radius:14px;padding:26px;overflow:hidden}
.arow,.aaxis{display:grid;grid-template-columns:minmax(0,260px) minmax(0,1fr);gap:18px;align-items:center}
.arow{padding:7px 0;border-top:1px solid #eaf1f2}
.alab{font-size:14px;line-height:1.3;min-width:0}.alab b{display:block;font-size:15px}.alab span{color:var(--slate)}
.atrack{position:relative;height:22px;background:repeating-linear-gradient(90deg,#eef4f5 0,#eef4f5 1px,transparent 1px,transparent calc(100%/14));border-radius:4px}
.atrack i{position:absolute;top:3px;bottom:3px;border-radius:4px;background:var(--periwinkle)}
.atrack i.mid{background:var(--slate)}.atrack i.main{background:var(--blue)}.atrack i.cons{background:var(--lime);outline:1px solid var(--ink)}
.aaxis{padding-bottom:8px}.aaxis .yrs{position:relative;height:18px;font-size:12px;font-weight:700;color:var(--slate)}
.aaxis .yrs span{position:absolute;transform:translateX(-50%)}
.anote{font-size:13px;color:var(--slate);margin-top:14px}
.creds{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:20px;margin-top:40px}
.cred{--a:var(--blue);background:#fff;border-radius:14px;padding:32px 26px 26px;box-shadow:inset 0 6px 0 var(--a)}
.cred:nth-child(2){--a:var(--lime)}.cred:nth-child(3){--a:var(--slate)}.cred:nth-child(4){--a:var(--periwinkle)}
.cred b{font-family:var(--display);font-size:20px;display:block;margin-bottom:6px}
.cred span{color:var(--slate);font-size:15px}
.tgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,340px),1fr));gap:20px;margin-top:40px}
.quote{background:#fff;border-radius:14px;padding:26px;border:1px solid #d3e1e3;display:flex;flex-direction:column;gap:16px;min-width:0}
.quote p{font-size:17px}
.quote footer{font-size:14px;color:var(--slate);margin-top:auto}.quote footer b{display:block;color:var(--ink);font-size:16px}
.quote:before{content:"";display:block;width:36px;height:6px;border-radius:3px;background:var(--lime)}
.recs{display:grid;gap:24px;margin-top:48px}
.rec{--a:var(--blue);background:#fff;border-radius:14px;padding:32px 32px 32px 40px;box-shadow:inset 8px 0 0 var(--a);min-width:0}
.rec:nth-child(2){--a:var(--lime)}.rec:nth-child(3){--a:var(--slate)}.rec:nth-child(4){--a:var(--periwinkle)}
.rec h3{font-size:22px}
.rec .rt{font-size:15px;color:var(--slate);margin:4px 0 2px}
.rec .rd{font-size:13px;font-weight:700;color:var(--blue);margin-bottom:16px}
.rec p+p{margin-top:12px}
.subhead{font-size:clamp(26px,3.4vw,36px);margin-top:72px}
.contact{background:var(--ink);color:#fff;padding:84px 0 56px}
.contact h2{color:#fff;max-width:20ch}
.contact .lede{color:#d5dcff}
.contact .row{display:flex;gap:14px;flex-wrap:wrap;margin-top:28px}
.contact .btn.ghost{color:#fff;border-color:#fff}
.contact .loc{margin-top:22px;color:#b9c4ff;font-size:15px}
.contact .fine{margin-top:48px;padding-top:20px;border-top:1px solid #ffffff22;font-size:13px;color:#9ba8e6;max-width:80ch}
"""

TOOLS_CSS = r"""
.tools{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,360px),1fr));gap:28px;margin-top:32px}
.tcard{background:var(--white);min-width:0;display:flex;flex-direction:column;border-radius:14px;overflow:hidden;border:1px solid #d3e1e3}
.tcard.wide{grid-column:1/-1}
.tart{position:relative;aspect-ratio:2/1;overflow:hidden;background:var(--beige)}
.tart svg{position:absolute;inset:0;width:100%;height:100%;display:block}
.tcard.wide .tart{aspect-ratio:auto;height:150px}
.tlabel{position:absolute;top:16px;left:16px;font-size:12px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;padding:9px 13px;border-radius:6px}
.tbody{padding:22px 20px 26px;min-width:0}
.tbody h3{font-size:24px;line-height:1.15;margin:0 0 18px}
.tcard ul{display:flex;flex-wrap:wrap;gap:8px;margin:0;padding:0;list-style:none}
.tcard li{font-size:12px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;line-height:1.3;padding:9px 12px;border-radius:6px;background:#deeeef;color:#08112e}
.tcard li:nth-child(5n+2){background:#cbf69f}
.tcard li:nth-child(5n+3){background:#3448ff;color:#fff}
.tcard li:nth-child(5n+4){background:#27455c;color:#fff}
.tcard li:nth-child(5n+5){background:#c9d1ff}
.tnote{font-size:13px;color:var(--ink2);margin:18px 0 0}
"""

PLAN_CSS = r"""
.steps{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px;margin-top:40px;position:relative}
.steps:before{content:"";position:absolute;left:6%;right:6%;top:19px;border-top:2px dashed #08112e33}
.step{display:flex;flex-direction:column;align-items:center;min-width:0;position:relative}
.stag{background:#fff;font-weight:800;font-size:13px;letter-spacing:.08em;text-transform:uppercase;padding:11px 18px;margin-bottom:22px;position:relative;white-space:nowrap;border-radius:6px;border:1px solid #b9cfd2}
.stag.dark{background:var(--ink);color:#fff;border-color:var(--ink)}
.pcard{background:#fff;border-radius:18px;padding:24px 22px 28px;width:100%;flex:1;min-width:0;border:1px solid #d3e1e3}
.pcard svg{display:block;width:120px;height:auto;margin-bottom:20px}
.pcard h3{font-size:24px;line-height:1.12;margin:0 0 14px}
.pcard ul{margin:0;padding-left:18px;display:grid;gap:9px;font-size:15px;line-height:1.45}
.pcard li::marker{color:var(--blue)}
.pnote{margin:28px auto 0;color:var(--ink2);max-width:70ch;text-align:center;font-size:14px}
.pcta{text-align:center;margin-top:30px}
.plansec .wrap>.kick,.plansec .wrap>h2,.plansec .wrap>.lede{text-align:center;margin-left:auto;margin-right:auto}
@media(max-width:980px){.steps{grid-template-columns:repeat(2,minmax(0,1fr))}.steps:before{display:none}}
@media(max-width:600px){.steps{grid-template-columns:minmax(0,1fr)}.step{align-items:flex-start}}
"""

RESP_CSS = r"""
@media(max-width:820px){.hero .wrap{grid-template-columns:minmax(0,1fr)}.photo{max-width:300px;order:-1}.hero{padding:44px 0 56px}.stats .wrap{grid-template-columns:repeat(2,minmax(0,1fr))}.stat:nth-child(3){border-left:0}.stat{border-top:1px solid #ffffff22}.stat:nth-child(-n+2){border-top:0}section{padding:60px 0}.nav .brand{display:none}.arow,.aaxis{grid-template-columns:minmax(0,1fr)}.arow{gap:6px}.aaxis .lab{display:none}.rec{padding:24px 20px}}
@media(max-width:480px){body{font-size:16px}.wrap{padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}.job,.case .in{padding:22px 18px}}
"""

PLAN_ART = [
    '<svg viewBox="0 0 120 100" aria-hidden="true"><path d="M8 18 L92 8 L100 70 L18 88Z" fill="#cbf69f"/><rect x="24" y="22" width="56" height="30" rx="6" fill="#08112e"/><path d="M36 52 l-4 12 l14 -12z" fill="#08112e"/><rect x="50" y="44" width="52" height="28" rx="6" fill="#f4f8f8" stroke="#08112e" stroke-width="2"/><path d="M84 72 l6 12 l2 -12z" fill="#f4f8f8" stroke="#08112e" stroke-width="2"/><path d="M34 34h36M34 42h22M60 54h32M60 62h20" stroke="#f4f8f8" stroke-width="3" opacity=".9"/></svg>',
    '<svg viewBox="0 0 120 100" aria-hidden="true"><path d="M6 30 Q30 4 70 12 L108 26 L96 84 L14 90Z" fill="#3448ff"/><path d="M22 70 Q40 40 62 56 T98 34" stroke="#f4f8f8" stroke-width="3" fill="none" stroke-dasharray="5 5"/><circle cx="22" cy="70" r="6" fill="#f4f8f8"/><circle cx="62" cy="56" r="6" fill="#cbf69f"/><circle cx="98" cy="34" r="6" fill="#f4f8f8"/><rect x="50" y="14" width="34" height="22" fill="#08112e"/><path d="M56 22h22M56 29h14" stroke="#f4f8f8" stroke-width="3"/></svg>',
    '<svg viewBox="0 0 120 100" aria-hidden="true"><circle cx="54" cy="44" r="38" fill="#deeeef"/><path d="M8 92 L70 78 L112 92Z" fill="#27455c"/><rect x="30" y="50" width="14" height="30" fill="#08112e"/><rect x="50" y="36" width="14" height="44" fill="#3448ff"/><rect x="70" y="20" width="14" height="60" fill="#08112e"/><path d="M28 40 L56 26 L90 10" stroke="#3448ff" stroke-width="3" fill="none"/></svg>',
    '<svg viewBox="0 0 120 100" aria-hidden="true"><circle cx="62" cy="48" r="40" fill="#cbf69f"/><circle cx="20" cy="20" r="5" fill="#08112e"/><circle cx="32" cy="10" r="3" fill="#08112e"/><path d="M50 84 V22" stroke="#08112e" stroke-width="4"/><path d="M52 22 L92 34 L52 48Z" fill="#3448ff" stroke="#08112e" stroke-width="3" stroke-linejoin="round"/></svg>',
]

TAGS = ['#3448ff', '#cbf69f', '#27455c', '#deeeef', '#8fa0ff']

def tool_card(i, title, items, unit, wide=False, art_idx=None):
    if wide:
        bg, shapes, vb = art_svgs.hub()
    else:
        fn = art_svgs.ARTS[art_idx if art_idx is not None else i]
        bg, shapes = fn() if title != "Service & Case Management" else art_svgs.ats("Case queue", ("New", "Triage", "Working", "Resolved"))
        vb = "0 0 400 200"
    tag = TAGS[i % len(TAGS)]
    tcol = "#ffffff" if tag in ("#3448ff", "#27455c") else "#08112e"
    svg = '<svg viewBox="%s" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect width="1000" height="200" fill="%s"/>%s</svg>' % (vb, bg, shapes)
    lis = "".join("<li>%s</li>" % e(t) for t in items)
    return ('<article class="tcard%s"><div class="tart">%s<span class="tlabel" style="background:%s;color:%s">%d %s</span></div>'
            '<div class="tbody"><h3>%s</h3><ul>%s</ul></div></article>') % (" wide" if wide else "", svg, tag, tcol, len(items), unit, e(title), lis)

def sec(id_, cls, kick, h, lede, body):
    return (f'<section id="{id_}" class="{cls}"><div class="wrap"><div class="kick">{e(kick)}</div><h2>{e(h)}</h2>'
            + (f'<p class="lede">{e(lede)}</p>' if lede else "") + body + '</div></section>')

def job_html(j):
    s = f"<article class='job'><div class='jh'><h3>{e(j['title'])}, <span>{e(j['org'])}</span></h3><div class='dt'>{e(j['dates'])}</div></div><div class='meta'>{e(j['meta'])}</div><ul>" + "".join(f"<li>{e(b)}</li>" for b in j["bullets"]) + "</ul>"
    if "sub" in j:
        sb = j["sub"]
        s += f"<div class='sub'><div class='jh'><h3>{e(sb['title'])}, <span>{e(j['org'])}</span></h3><div class='dt'>{e(sb['dates'])}</div></div><ul>" + "".join(f"<li>{e(b)}</li>" for b in sb["bullets"]) + "</ul></div>"
    return s + "</article>"

def arc_html():
    lo, hi = 2013.0, 2027.0
    pos = lambda y: (y - lo) / (hi - lo) * 100
    rows = ""
    for org, title, sy, sm, ey, em, kind in ARC:
        s = sy + (sm - 1) / 12; en = ey + em / 12
        a = pos(s); w = max(pos(en) - a, 0.8)
        mon = lambda y, m: ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"][m-1] + f" {y}"
        rows += (f"<div class='arow'><div class='alab'><b>{e(org)}</b><span>{e(title)}, {mon(sy,sm)} - {mon(ey,em)}</span></div>"
                 f"<div class='atrack' role='img' aria-label='{e(org)} {mon(sy,sm)} to {mon(ey,em)}'><i class='{kind}' style='left:{a:.2f}%;width:{w:.2f}%'></i></div></div>")
    yrs = "".join(f"<span style='left:{pos(y):.2f}%'>{y}</span>" for y in range(2013, 2027, 2))
    axis = f"<div class='aaxis'><div class='lab'></div><div class='yrs'>{yrs}</div></div>"
    return f"<div class='arc'>{axis}{rows}<p class='anote'>Bars are drawn to scale from each role's start and end dates. Oldest first.</p></div>"

def build():
    p = []
    p.append(f'<div class="ann">Portfolio for <b>{e(COMPANY)}</b>  |  {e(ROLE)}</div>')
    p.append('<header class="nav"><div class="wrap"><a class="brand" href="#top"><i></i>Catherine Nolasco</a><nav class="links" aria-label="Sections">'
             + "".join(f'<a href="#{a}">{b}</a>' for a, b in [("summary","Summary"),("fit","Role fit"),("results","Results"),("cases","Case studies"),("values","Values"),("tools","Tools"),("experience","Experience"),("arc","Career arc"),("plan","30-60-90"),("creds","Credentials"),("kind","Kind words")])
             + f'</nav><a class="btn" href="mailto:{EMAIL}" style="padding:10px 18px;font-size:14px;white-space:nowrap">Say hello</a></div></header>')
    img = "data:image/jpeg;base64," + b64(HEADSHOT)
    p.append(f'<main id="top"><div class="hero"><div class="wrap"><div><div class="eyebrow">Catherine Nolasco, SHRM-CP</div><h1>Catherine Nolasco</h1><div class="tag">people ops. powered by AI.</div>'
             f'<p class="target">Applying for <b>{e(ROLE)}</b> at <b>{e(COMPANY)}</b>. I build People Operations that run smoothly, so people teams can spend their time on the empathy, nuance and conversations that AI cannot handle.</p>'
             '<p class="keys">'+"".join(f"<span>{e(k.strip())}</span>" for k in KEYLINE.split("|") if k.strip())+'</p>'
             f'<div class="cta"><a class="btn" href="#cases">See the work</a><a class="btn ghost" href="mailto:{EMAIL}">Email me</a></div></div>'
             f'<div class="photo"><img src="{img}" alt="Catherine Nolasco" width="560" height="704"></div></div></div>')
    p.append('<div class="stats"><div class="wrap">' + "".join(f"<div class='stat'><b>{e(a)}</b><span>{e(b)}</span></div>" for a, b in STATS) + '</div></div>')
    p.append(sec("summary", "", "Summary", "A People Operations builder, from zero to audit-ready", "", '<ul class="sumlist">' + "".join(f"<li>{e(s)}</li>" for s in SUMMARY) + '</ul>'))
    p.append(sec("fit", "mist", "Role fit", f"What the {COMPANY} role asks for, and what I have done", "Each card pairs an area of the role with work I have actually done.",
                 '<div class="fit">' + "".join(f'<article class="fcard f{i}"><small>{e(k)}</small><h3>{e(h)}</h3><p>{e(b)}</p></article>' for i, (k, h, b) in enumerate(FIT)) + '</div>'))
    p.append(sec("results", "", "Results", "Numbers I can stand behind", "", '<div class="res">' + "".join(f'<article class="rcard"><b>{e(a)}</b><strong>{e(b)}</strong><span>{e(c)}</span></article>' for a, b, c in RESULTS) + '</div>'))
    stripes = ["#3448ff", "#cbf69f", "#27455c", "#8fa0ff", "#08112e"]
    cs = ""
    for i, c in enumerate(CASES):
        cs += (f'<article class="case" style="--c:{stripes[i%5]}"><div class="stripe"></div><div class="in"><h3>{e(c["title"])}</h3><div class="emp">{e(c["org"])}  |  {e(c["dates"])}</div>'
               f'<div><h4>Challenge</h4><p>{e(c["challenge"])}</p></div><div><h4>What I did</h4><p>{e(c["did"])}</p></div>'
               f'<div class="callout"><h4>Result</h4><p>{e(c["result"])}</p></div><div><h4>What I would do differently</h4><p>{e(c["diff"])}</p></div>'
               f'<div class="chips">{"".join(f"<span>{e(t)}</span>" for t in c["tools"])}</div></div></article>')
    p.append(sec("cases", "alt", "Case studies", "Five projects, told straight", "Ridecell first, then Prezent AI. Each one ends with what I would change.", f'<div class="cases">{cs}</div>'))
    p.append(sec("values", "", "Values", f"{COMPANY}'s values, in my work", "Own it. Work it. Risk it. Tell it. Love it. Here is where each one shows up in what I have done.",
                 '<div class="vals">' + "".join(f'<article class="val"><small>Value {i+1}</small><h3>{e(k)}</h3><p>{e(v)}</p></article>' for i, (k, v) in enumerate(VALUES)) + '</div>'))
    cards = ""
    arts = [0, 1, 2, 1, 4, 3, 5]
    for i, (name, items) in enumerate(TOOLS):
        names = [x.strip() for x in items.split(", ")]
        cards += tool_card(i, name, names, "tools", art_idx=arts[i])
    cards += tool_card(len(TOOLS), "Core competencies", COMPETENCIES, "areas", wide=True)
    p.append(sec("tools", "mist", "Tools and systems", "The stack I know, and the skills behind it", "Tools I have used, grouped by job to be done.", f'<div class="tools">{cards}</div><p class="tnote">Card illustrations are simplified examples with sample shapes, not screenshots of real systems or data.</p>'))
    p.append(sec("experience", "", "Experience", "Where I have done the work", "", '<div class="jobs">' + "".join(job_html(j) for j in JOBS) + '</div><div class="earlier"><h3>Earlier experience</h3><ul>' + "".join(f"<li>{e(x)}</li>" for x in EARLIER) + '</ul></div>'))
    p.append(sec("arc", "alt", "Career arc", "13 years, drawn to scale", "", arc_html()))
    plan = "".join(f'<div class="step"><span class="stag{" dark" if i == len(PLAN) - 1 else ""}">{e(a)}</span><div class="pcard">{PLAN_ART[i]}<h3>{e(b)}</h3><ul>' + "".join(f"<li>{e(x)}</li>" for x in c) + "</ul></div></div>" for i, (a, b, c) in enumerate(PLAN))
    p.append(sec("plan", "plansec mist", "30-60-90", "How I would start", "A proposed plan for the first six months, built around the role description.",
                 f'<div class="steps">{plan}</div><p class="pnote">This is a starting point. I would adjust it after the first conversations with the people I would be supporting and the leaders I would be working with.</p><div class="pcta"><a class="btn dark" href="mailto:{EMAIL}">Let\'s talk</a></div>'))
    creds = ('<div class="creds">' + f'<article class="cred"><b>{e(CERT[0])}</b><span>{e(CERT[1])}</span></article>'
             + "".join(f'<article class="cred"><b>{e(a)}</b><span>{e(b)}</span></article>' for a, b in EDUCATION) + '</div>')
    p.append(sec("creds", "", "Credentials", "Certified and educated", "", creds))
    quotes = "".join(f'<figure class="quote" style="margin:0"><p>{e(q)}</p><footer><b>{e(n)}</b>{e(r)}  |  {e(src)}</footer></figure>' for n, r, src, q in TESTIMONIALS)
    recs = "".join(f'<article class="rec"><h3>{e(n)}</h3><div class="rt">{e(t)}</div><div class="rd">{e(d)}  |  {e(rel)}</div>' + "".join(f"<p>{e(x)}</p>" for x in paras) + '</article>' for n, t, d, rel, paras in RECS)
    p.append(sec("kind", "alt", "Kind words", "What colleagues have said", "", f'<div class="tgrid">{quotes}</div><h2 class="subhead">LinkedIn recommendations</h2><div class="recs">{recs}</div>'))
    p.append(f'<footer class="contact"><div class="wrap"><h2>Let\'s talk about {e(COMPANY)}</h2><p class="lede">I would love to hear what the People Operations team needs most.</p>'
             f'<div class="row"><a class="btn" href="mailto:{EMAIL}">{e(EMAIL)}</a><a class="btn ghost" href="https://{LINKEDIN}">{e(LINKEDIN)}</a></div><p class="loc">{e(LOCATION)}</p>'
             f'<p class="fine">This is an independent portfolio styled after the {e(COMPANY)} brand. It is not affiliated with or endorsed by {e(COMPANY)}. Card illustrations are simplified examples, not screenshots of real systems.</p></div></footer></main>')
    return "".join(p)

BODY = build()
STYLE = CSS + TOOLS_CSS + PLAN_CSS + RESP_CSS
TITLE = "Catherine Nolasco"
standalone = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{TITLE}</title><meta name="description" content="Portfolio of Catherine Nolasco, SHRM-CP: People Operations leader applying for {ROLE} at {COMPANY}."><style>{font_css()}{STYLE}</style></head><body>{BODY}</body></html>'
gf = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;600;700;800&family=Sora:wght@600;700&display=swap" rel="stylesheet">'
artifact = f'<title>{TITLE}</title><meta name="claude:viewport-fit-sides" content="cover">{gf}<style>{STYLE}</style><body>{BODY}</body>'
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "index.html").write_text(standalone, encoding="utf-8")
(OUT / "artifact.html").write_text(artifact, encoding="utf-8")
print("built", len(standalone) // 1024, "KB standalone;", len(artifact) // 1024, "KB artifact")
