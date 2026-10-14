"""Genera un carosello Instagram ETNASOLUTIONclean (slide 1080x1350 JPG).
Uso: python3 scripts/genera_carosello.py spec.json cartella_output
spec.json:
{
  "prefix": "2026-10-16_ambulatori",
  "bg": "#0f4c4a", "acc": "#9be7c4",
  "icon": "🩺",
  "kicker": "Ambulatori medici",
  "title": "Il punto più contaminato<br>non è il pavimento.",   (max 3 righe brevi)
  "subtitle": "Dove si annidano davvero i germi in sala d'attesa",
  "slides": [ {"h": "Titolo scheda", "p": "Testo 1-3 frasi (max ~220 caratteri)", "icon": "🚪"}, ... ]   (3-5 schede)
}
Produce: <prefix>_01.jpg (copertina), <prefix>_02..N (schede), ultima = contatti.
"""
import asyncio, json, sys, os
from playwright.async_api import async_playwright
from PIL import Image

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1350px;font-family:'Inter';background:%(bg)s;color:#fff;position:relative;overflow:hidden}
.top{position:absolute;top:64px;left:80px;right:80px;display:flex;justify-content:space-between;align-items:center}
.brand{font-family:'Inter Display';font-weight:800;font-size:32px;letter-spacing:1px}
.brand span{color:%(acc)s}
.count{font-size:24px;font-weight:600;opacity:.75}
.c1{position:absolute;right:-240px;top:160px;width:720px;height:720px;border-radius:50%%;background:%(acc)s;opacity:.14}
.c2{position:absolute;left:-180px;bottom:-220px;width:540px;height:540px;border-radius:50%%;border:60px solid rgba(255,255,255,.06)}
.foot{position:absolute;bottom:64px;left:80px;right:80px;display:flex;justify-content:space-between;align-items:center;border-top:2px solid rgba(255,255,255,.22);padding-top:28px;font-size:26px}
.foot b{color:%(acc)s}
.dots{display:flex;gap:10px}.dots i{width:12px;height:12px;border-radius:50%%;background:rgba(255,255,255,.3)}.dots i.on{background:%(acc)s;width:34px;border-radius:6px}
"""

def dots(n, k):
    return '<div class="dots">' + "".join(f'<i class="{"on" if i==k else ""}"></i>' for i in range(n)) + '</div>'

def page(body, s, n, k, foot_left):
    return f"""<html><head><style>{CSS % s}</style></head><body><div class="c1"></div><div class="c2"></div>
<div class="top"><div class="brand">ETNA<span>SOLUTION</span>clean</div><div class="count">{k+1} / {n}</div></div>
{body}<div class="foot"><div>{foot_left}</div>{dots(n,k)}</div></body></html>"""

def cover(s, n):
    body = f"""<style>
.icon{{position:absolute;top:220px;left:80px;font-size:130px}}
.kicker{{position:absolute;top:410px;left:80px;font-size:30px;font-weight:700;color:{s['acc']};letter-spacing:4px;text-transform:uppercase}}
h1{{position:absolute;top:470px;left:80px;right:80px;font-family:'Inter Display';font-weight:800;font-size:88px;line-height:1.04}}
.sub{{position:absolute;top:auto;bottom:230px;left:80px;right:120px;font-size:36px;font-weight:500;line-height:1.3;opacity:.9}}
</style><div class="icon">{s['icon']}</div><div class="kicker">{s['kicker']}</div><h1>{s['title']}</h1><div class="sub">{s['subtitle']}</div>"""
    return page(body, s, n, 0, "Scorri <b>→</b>")

def card(s, n, k, sl):
    body = f"""<style>
.num{{position:absolute;top:200px;left:80px;font-family:'Inter Display';font-weight:800;font-size:200px;color:{s['acc']};opacity:.9;line-height:1}}
.ic{{position:absolute;top:230px;right:90px;font-size:120px}}
h2{{position:absolute;top:470px;left:80px;right:80px;font-family:'Inter Display';font-weight:800;font-size:72px;line-height:1.08}}
.p{{position:absolute;top:700px;left:80px;right:80px;font-size:40px;line-height:1.4;font-weight:400;opacity:.95}}
</style><div class="num">{k:02d}</div><div class="ic">{sl.get('icon','')}</div><h2>{sl['h']}</h2><div class="p">{sl['p']}</div>"""
    return page(body, s, n, k, "Scorri <b>→</b>")

def contacts(s, n):
    body = f"""<style>
.k{{position:absolute;top:220px;left:80px;font-size:30px;font-weight:700;color:{s['acc']};letter-spacing:4px;text-transform:uppercase}}
h2{{position:absolute;top:280px;left:80px;right:80px;font-family:'Inter Display';font-weight:800;font-size:86px;line-height:1.04}}
.row{{position:absolute;left:80px;right:80px;font-size:44px;font-weight:600;display:flex;gap:26px;align-items:center}}
.row span{{display:inline-flex;width:84px;height:84px;border-radius:50%;background:{s['acc']};justify-content:center;align-items:center;font-size:42px}}
</style><div class="k">Preventivo gratuito</div><h2>Richiedi un<br>sopralluogo<br>senza impegno.</h2>
<div class="row" style="top:700px"><span>📞</span>346 2468238<br>377 1212161</div>
<div class="row" style="top:900px"><span>🌐</span>etnasolutionclean.it</div>"""
    return page(body, s, n, n-1, "Catania e comuni etnei")

async def main(spec, out):
    os.makedirs(out, exist_ok=True)
    n = len(spec["slides"]) + 2
    pages = [cover(spec, n)] + [card(spec, n, i+1, sl) for i, sl in enumerate(spec["slides"])] + [contacts(spec, n)]
    files = []
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width":1080,"height":1350})
        for i, html in enumerate(pages):
            await pg.set_content(html); await pg.wait_for_timeout(250)
            png = os.path.join(out, f"tmp.png"); await pg.screenshot(path=png)
            f = os.path.join(out, f"{spec['prefix']}_{i+1:02d}.jpg")
            Image.open(png).convert("RGB").save(f, quality=84, optimize=True); os.remove(png); files.append(f)
        await b.close()
    print("\n".join(files))

asyncio.run(main(json.load(open(sys.argv[1], encoding="utf-8")), sys.argv[2]))
