#!/usr/bin/env python3
"""아인잉글리쉬 소개(about/intro) 페이지용 캐릭터 그림 — about_images.py의 캐릭터를 그대로 쓴다.
사용법: python3 intro_images.py <about_images.py 경로> <출력폴더> <글꼴폴더>"""
import sys, os, importlib.util
spec = importlib.util.spec_from_file_location('ab', sys.argv[1]); ab = importlib.util.module_from_spec(spec); spec.loader.exec_module(ab)
W = ab.W
def now():
    b = ab.bubble(60, 40, 520, 150, '#ffffff', (250, 252), ['영어… 언젠가', '해야 하는데'], 44)
    b += ab.framed(90, 250, 400, 360, ab.BLUE_BG, ab.student(200, 190, 1.0, 'worry'))
    b += ab.burst(700, 350, 118, ab.YEL, '지금!', 80) + ab.spark(590, 220, 18, ab.MINT) + ab.spark(800, 500, 16, ab.CORAL)
    b += ab.bubble(830, 40, 540, 130, ab.YEL, (1090, 252), ['오늘 한 문장부터!'], 48)
    b += ab.framed(890, 250, 400, 360, ab.MINT_BG, ab.student(200, 190, 1.0, 'cheer'))
    b += ab.mascot(1366, 500, 0.56, 'cheer') + ab.note(1350, 330)
    return 1440, 640, '#ffffff', b
def cta():
    b = f'<g {W}>{ab.student(400, 310, 1.0, "cheer")}</g><g {W}>{ab.teacher(1040, 310, 1.0, "none")}</g>'
    b += ab.mascot(720, 350, 1.1, 'cheer')
    b += ab.bubble(490, 24, 460, 120, '#ffffff', (720, 232), ['같이 시작해요!'], 52)
    b += ab.spark(210, 150, 22) + ab.spark(1230, 130, 20, ab.MINT) + ab.note(140, 330) + ab.note(1200, 300) + ab.spark(590, 250, 14, '#ffffff') + ab.spark(860, 240, 14)
    return 1440, 520, '#ec6856', b
def main(outdir, fontdir):
    from playwright.sync_api import sync_playwright
    fk = 'file://' + os.path.abspath(os.path.join(fontdir, 'gaegu-korean-700-normal.woff2')); fl = 'file://' + os.path.abspath(os.path.join(fontdir, 'gaegu-latin-700-normal.woff2'))
    tmp = os.path.join(outdir, '_scene.html')
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        for name, fn in (('intro_now.png', now), ('intro_cta.png', cta)):
            ab._defs.clear(); w, h, bg, body = fn(); defs = ''.join(ab._defs)
            open(tmp, 'w').write(f'''<!DOCTYPE html><html><head><meta charset="utf-8"><style>@font-face{{font-family:G;src:url({fk});unicode-range:U+1100-11FF,U+3130-318F,U+AC00-D7AF}}@font-face{{font-family:G;src:url({fl})}}body{{margin:0}}text{{font-family:G,"Noto Sans CJK KR",sans-serif;font-weight:700}}</style></head><body><svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><defs><filter id="w" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="0.012" numOctaves="2" seed="4"/><feDisplacementMap in="SourceGraphic" scale="9"/></filter>{defs}</defs><rect width="{w}" height="{h}" fill="{bg}"/>{body}</svg></body></html>''')
            pg = br.new_page(viewport={'width': w, 'height': h}); pg.goto('file://' + os.path.abspath(tmp)); pg.wait_for_timeout(400)
            pg.screenshot(path=os.path.join(outdir, name)); pg.close(); print(name, (w, h))
        br.close()
    os.remove(tmp)
if __name__ == '__main__': main(sys.argv[2], sys.argv[3])
