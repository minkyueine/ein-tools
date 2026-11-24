"""아인잉글리쉬 프리토킹 페이지용 그림. 사용법: python3 freetalk_images.py freetalk-assets/"""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import art_lib as A
from art_lib import *
RED = '#E5484D'
def went(t): return t.replace('went', f'<tspan fill="{RED}">went</tspan>')
def cta(): return 680, 680, 'none', framed(20, 20, 640, 640, PINK_BG, teacher(300, 350, 1.75, 'point'))
def fix():
    b = framed(50, 310, 500, 560, BLUE_BG, student(250, 290, 1.3, 'worry')) + framed(650, 310, 500, 560, PINK_BG, teacher(240, 310, 1.3, 'point'))
    b += bubble(40, 50, 580, 170, '#ffffff', (260, 310), ['I go to Jeju…'], 70)
    b += bubble(660, 50, 500, 170, MINT_BG, (900, 310), [went('go → went!')], 70)
    return 1200, 920, 'none', b
def good():
    b = framed(40, 310, 500, 570, BLUE_BG, student(250, 310, 1.3, 'cheer')) + framed(660, 310, 500, 570, PINK_BG, teacher(240, 320, 1.3, 'none'))
    b += bubble(30, 50, 640, 180, YEL_BG, (250, 310), [went('I went to Jeju!')], 70) + burst(950, 140, 150, YEL, 'Perfect!', 76)
    b += note(590, 560) + spark(600, 690, 26, MINT)
    return 1200, 920, 'none', b
def news():
    b = bubble(80, 40, 700, 150, YEL_BG, (640, 260), ['매주 새 뉴스!'], 76) + mascot(620, 430, 2.0, 'cheer')
    b += f'<g transform="rotate(-4 1290 390)">' + box(940, 150, 700, 480, '#ffffff', 16)
    b += f'<rect x="980" y="190" width="620" height="84" fill="#2F5FB3" {W}/>' + text(1290, 232, 'GLOBAL NEWS', 60, color='#ffffff')
    b += f'<rect x="980" y="310" width="250" height="200" rx="10" fill="#C9DBFA" stroke="{K}" stroke-width="6"/>'
    for i, wd in enumerate((330, 330, 260, 330)): b += f'<path d="M1270,{330 + i * 54} L{1270 + wd},{330 + i * 54}" stroke="{K}" stroke-width="9" stroke-linecap="round"/>'
    b += f'<path d="M980,566 L1600,566" stroke="#C9CCD3" stroke-width="9" stroke-linecap="round"/></g>'
    b += bubble(1640, 40, 720, 150, '#ffffff', (2060, 250), ['I think… because…'], 68) + f'<g {W}>{student(2060, 500, 1.5, "happy")}</g>'
    b += spark(830, 660, 26) + spark(1700, 620, 22, MINT)
    return 2400, 760, 'none', b
def scenes():
    s = {}
    for name, fn in (('ft_cta.png', cta), ('ft_fix.png', fix), ('ft_good.png', good), ('ft_news.png', news)):
        A._defs.clear(); w, h, bg, body = fn(); s[name] = (w, h, bg, body, ''.join(A._defs))
    return s
A.scenes = scenes
A.main(sys.argv[1])
