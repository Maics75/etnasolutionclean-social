"""Genera le grafiche Instagram (1080x1350, JPG) di ETNASOLUTIONclean.
Uso: python3 scripts/genera_grafiche.py spec.json cartella_output
spec.json = lista di oggetti: {file, bg, acc, tag, icon, kicker, title, items:[4 voci]}
title puo' contenere <br>. Titolo max ~2 righe da 18 caratteri.
"""
import asyncio, json, sys, os
from playwright.async_api import async_playwright
from PIL import Image

BASE = open(os.path.join(os.path.dirname(__file__), "template.html"), encoding="utf-8").read()

async def main(spec, out):
    os.makedirs(out, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width":1080,"height":1350})
        for d in spec:
            d2 = dict(d); d2.setdefault("listtop", 760)
            d2["items"] = "".join(f"<li><b>✓</b>{i}</li>" for i in d["items"])
            await pg.set_content(BASE % d2)
            await pg.wait_for_timeout(300)
            png = os.path.join(out, d["file"].rsplit(".",1)[0] + ".png")
            await pg.screenshot(path=png)
            Image.open(png).convert("RGB").save(os.path.join(out, d["file"]), quality=82, optimize=True)
            os.remove(png)
        await b.close()

asyncio.run(main(json.load(open(sys.argv[1], encoding="utf-8")), sys.argv[2]))
