"""아인잉글리쉬 소개(about/intro) 페이지용 그림. 사용법: python3 intro_images.py intro-assets/"""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import art_lib as A
from art_lib import *
def now():
    b = framed(84, 252, 400, 360, BLUE_BG, student(200, 200, 1.0, 'worry')) + framed(888, 252, 400, 360, MINT_BG, student(200, 210, 1.0, 'cheer'))
    b += bubble(60, 40, 516, 150, '#ffffff', (250, 252), ['영어… 언젠가', '해야 하는데'], 46)
    b += bubble(828, 52, 540, 126, YEL, (1090, 252), ['오늘 한 문장부터!'], 50)
    b += burst(686, 400, 112, YEL, '지금!', 64) + mascot(1376, 500, 0.6, 'cheer') + note(1400, 330) + spark(590, 230, 18, MINT) + spark(800, 560, 16, CORAL)
    return 1440, 640, '#ffffff', b
def cta():
    b = f'<g {W}>{student(396, 330, 0.86, "cheer")}</g>' + f'<g {W}>{teacher(1044, 330, 0.84, "none")}</g>' + mascot(720, 360, 1.05, 'cheer')
    b += bubble(490, 30, 460, 116, '#ffffff', (720, 232), ['같이 시작해요!'], 50)
    b += note(150, 300) + note(1210, 280) + spark(210, 150, 20) + spark(1230, 120, 20, MINT) + spark(590, 250, 14) + spark(860, 250, 14, MINT)
    return 1440, 520, '#EC6856', b
def scenes():
    s = {}
    for name, fn in (('intro_now.png', now), ('intro_cta.png', cta)):
        A._defs.clear(); w, h, bg, body = fn(); s[name] = (w, h, bg, body, ''.join(A._defs))
    return s
A.scenes = scenes
A.main(sys.argv[1])
