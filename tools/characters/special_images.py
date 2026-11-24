"""아인잉글리쉬 특별과정 페이지용 그림 — about 페이지와 같은 손그림 만화 느낌."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import art_lib as A
from art_lib import *

def plane(x, y, s=1.0):
    g = f'<g transform="translate({x},{y}) scale({s})" {W}>'
    g += f'<path d="M-150,10 Q-150,-26 -96,-30 L96,-30 Q160,-26 176,6 Q160,36 96,36 L-110,36 Q-150,34 -150,10 Z" fill="#ffffff" stroke="{K}" stroke-width="7" stroke-linejoin="round"/>'
    g += f'<path d="M-20,20 L-84,96 L-36,96 L46,20 Z" fill="{CORAL}" stroke="{K}" stroke-width="7" stroke-linejoin="round"/>'
    g += f'<path d="M-124,-28 L-166,-86 L-124,-86 L-78,-30 Z" fill="{CORAL}" stroke="{K}" stroke-width="7" stroke-linejoin="round"/>'
    for i in range(4):
        g += f'<circle cx="{-50 + i * 44}" cy="-2" r="11" fill="{BLUE}" stroke="{K}" stroke-width="5"/>'
    g += f'<path d="M118,-12 Q146,-10 156,6" fill="none" stroke="{K}" stroke-width="6" stroke-linecap="round"/>'
    return g + '</g>'

def suitcase(x, y, s=1.0, fill=YEL):
    g = f'<g transform="translate({x},{y}) scale({s})" {W}>'
    g += f'<path d="M-34,-70 L-34,-104 L34,-104 L34,-70" fill="none" stroke="{K}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>'
    g += f'<rect x="-76" y="-70" width="152" height="150" rx="22" fill="{fill}" stroke="{K}" stroke-width="7"/>'
    g += f'<path d="M-36,-70 L-36,80 M36,-70 L36,80" stroke="{K}" stroke-width="6"/>'
    g += f'<circle cx="-46" cy="94" r="12" fill="{K}"/><circle cx="46" cy="94" r="12" fill="{K}"/>'
    return g + '</g>'

def passport(x, y, s=1.0):
    g = f'<g transform="translate({x},{y}) scale({s}) rotate(-8)" {W}>'
    g += f'<rect x="-52" y="-70" width="104" height="140" rx="12" fill="#3F5FA8" stroke="{K}" stroke-width="7"/>'
    g += f'<circle cx="0" cy="-12" r="24" fill="none" stroke="#FFD95A" stroke-width="6"/><path d="M-24,-12 L24,-12 M0,-36 Q-14,-12 0,12 M0,-36 Q14,-12 0,12" fill="none" stroke="#FFD95A" stroke-width="4"/>'
    g += f'<path d="M-28,34 L28,34" stroke="#FFD95A" stroke-width="6" stroke-linecap="round"/>'
    return g + '</g>'

def sheet(x, y, w, h, title, lines, mark=None):
    g = box(x, y, w, h, '#ffffff', 22) + text(x + 30, y + 46, title, 30, 'start')
    g += f'<path d="M{x + 22},{y + 76} L{x + w - 22},{y + 76}" stroke="{K}" stroke-width="5" stroke-linecap="round" {W}/>'
    for i, wd in enumerate(lines):
        yy = y + 112 + i * 40
        g += f'<path d="M{x + 30},{yy} L{x + 30 + (w - 60) * wd:.0f},{yy}" stroke="#C9CCD3" stroke-width="10" stroke-linecap="round"/>'
    if mark:
        g += f'<circle cx="{x + w - 20}" cy="{y + 14}" r="56" fill="{CORAL}" stroke="{K}" stroke-width="7" {W}/>' + text(x + w - 20, y + 14, mark, 44, color='#ffffff')
    return g

def laptop(x, y, w=300, h=190):
    g = box(x, y, w, h, '#ffffff', 18)
    g += f'<rect x="{x + 22}" y="{y + 26}" width="56" height="56" rx="14" fill="{BLUE}" stroke="{K}" stroke-width="5"/><rect x="{x + 92}" y="{y + 26}" width="56" height="56" rx="14" fill="{MINT}" stroke="{K}" stroke-width="5"/><rect x="{x + 162}" y="{y + 26}" width="56" height="56" rx="14" fill="{YEL}" stroke="{K}" stroke-width="5"/>'
    g += f'<path d="M{x + 26},{y + 118} L{x + w - 30},{y + 118} M{x + 26},{y + 152} L{x + w - 110},{y + 152}" stroke="#C9CCD3" stroke-width="10" stroke-linecap="round" {W}/>'
    g += f'<path d="M{x - 36},{y + h + 10} L{x + w + 36},{y + h + 10} L{x + w + 14},{y + h + 40} L{x - 14},{y + h + 40} Z" fill="#E7E9EE" stroke="{K}" stroke-width="7" stroke-linejoin="round" {W}/>'
    return g

# ── 장면 ─────────────────────────────────────────────
def hero():
    b = f'<g {W}>{student(250, 330, 0.9, "happy")}</g>'
    b += bubble(40, 28, 300, 104, '#ffffff', (200, 196), ['오픽 IH 따야 해'], 40)
    b += bubble(430, 60, 330, 104, YEL, (384, 132), ['다음 달에 면접!'], 40)
    b += bubble(470, 220, 310, 104, MINT, (420, 292), ['3월에 출국해요'], 40)
    b += bubble(470, 380, 330, 104, '#D9E6FF', (420, 448), ['영어로 회의를…'], 40)
    b += f'<path d="M850,270 L940,270 M916,246 L942,270 L916,294" fill="none" stroke="{CORAL}" stroke-width="11" stroke-linecap="round" stroke-linejoin="round" {W}/>'
    b += framed(1010, 150, 380, 400, PINK_BG, teacher(190, 220, 1.0, 'point'))
    b += burst(1150, 82, 104, YEL, '목표대로!', 46) + mascot(900, 420, 0.64, 'cheer') + spark(960, 120, 18) + spark(1410, 110, 14, MINT)
    return 1440, 560, TINT, b

def exam():
    b = sheet(50, 80, 320, 330, 'Speaking Test', [0.9, 0.7, 0.85, 0.5, 0.75], 'IH')
    b += f'<g {W}>{student(540, 310, 0.95, "cheer")}</g>'
    b += bubble(400, 26, 300, 96, '#ffffff', (500, 170), ['실전처럼 연습!'], 38) + spark(380, 250, 18) + note(690, 240)
    return 720, 480, '#FFECE2', b

def interview():
    b = framed(40, 150, 280, 300, PINK_BG, teacher(140, 170, 0.82, 'none')) + framed(400, 150, 280, 300, BLUE_BG, student(140, 170, 0.82, 'happy'))
    b += bubble(30, 22, 380, 100, YEL, (160, 152), ['Tell me about yourself.'], 34)
    b += bubble(430, 34, 270, 90, '#ffffff', (560, 152), ["Sure! I'm…"], 36)
    return 720, 480, '#F1EAFF', b

def business():
    b = laptop(70, 150) + f'<g {W}>{student(540, 320, 0.95, "happy")}</g>'
    b += bubble(60, 26, 470, 96, '#ffffff', (480, 190), ['Could you send it by Friday?'], 34)
    b += tag(96, 410, '회의·이메일·발표', 30) + spark(660, 150, 18) + spark(420, 250, 14, MINT)
    return 720, 480, '#FFF5CF', b

def travel():
    b = plane(1090, 150, 1.1) + f'<path d="M700,210 Q800,150 880,170" fill="none" stroke="{K}" stroke-width="6" stroke-dasharray="4 20" stroke-linecap="round"/>'
    b += f'<g {W}>{student(250, 330, 0.9, "cheer")}</g>' + suitcase(470, 430, 0.95) + passport(600, 440, 0.8)
    b += bubble(400, 40, 430, 104, '#ffffff', (470, 196), ['Could I change rooms?'], 40)
    x = 690
    for lab, fill in (('여행', YEL), ('워킹홀리데이', MINT), ('유학', BLUE), ('이민', '#ffffff')):
        w = len(lab) * 36 + 50
        b += box(x, 410, w, 78, fill, 39) + text(x + w / 2, 449, lab, 36); x += w + 14
    b += mascot(1320, 270, 0.62, 'cheer') + spark(900, 330, 18) + spark(1400, 60, 14, MINT)
    return 1440, 560, '#E9F8EF', b

def close():
    b = framed(110, 60, 300, 320, BLUE_BG, student(150, 190, 0.85, 'cheer')) + framed(790, 60, 300, 320, PINK_BG, teacher(150, 180, 0.85, 'none'))
    b += burst(600, 130, 112, YEL, '목표 달성!', 46) + mascot(600, 300, 0.64, 'cheer') + note(470, 300) + spark(730, 290, 18, MINT)
    return 1200, 420, '#f7f7f7', b

def level():
    return 340, 340, '#ffffff', framed(20, 20, 300, 300, PINK_BG, teacher(140, 170, 0.85, 'point'))

def scenes():
    s = {}
    for name, fn in (('sp_hero.png', hero), ('sp_exam.png', exam), ('sp_interview.png', interview), ('sp_business.png', business), ('sp_travel.png', travel), ('sp_close.png', close), ('sp_level.png', level)):
        A._defs.clear(); w, h, bg, body = fn(); s[name] = (w, h, bg, body, ''.join(A._defs))
    return s

A.scenes = scenes
A.main(sys.argv[1])
