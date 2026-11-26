"""이용 가이드 6개 글 썸네일(1200x1200). 학생·선생님 캐릭터만 쓰고, 글마다 색과 구도를 다르게.
사용법: python3 guide_thumbs.py 출력폴더"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import art_lib as A
from art_lib import *

DK = '#2A211D'
def T(x, y, lines, size, color=K, anchor='middle', weight=900):
    if isinstance(lines, str): lines = [lines]
    lh = size * 1.22; y0 = y - lh * (len(lines) - 1) / 2 + size * 0.36
    return ''.join(f'<text x="{x}" y="{y0 + i * lh:.0f}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{color}" style="letter-spacing:-.02em">{l}</text>' for i, l in enumerate(lines))
def pill(x, y, label, fill=K, color='#fff', size=40, anchor='left'):
    w = len(label) * size * 0.92 + 56; h = size + 34
    if anchor == 'middle': x = x - w / 2
    return f'<rect x="{x:.0f}" y="{y}" width="{w:.0f}" height="{h}" rx="{h/2}" fill="{fill}" stroke="{K}" stroke-width="6" {W}/>' + T(x + w / 2, y + h / 2, label, size, color, weight=700)
def brand(x, y, color=K, anchor='middle'): return T(x, y, '아인잉글리쉬', 34, color, anchor, 700)
def play(cx, cy, r):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff" stroke="{K}" stroke-width="8" {W}/>'
            f'<path d="M{cx - r*.28},{cy - r*.4} L{cx + r*.45},{cy} L{cx - r*.28},{cy + r*.4} Z" fill="{CORAL}" stroke="{K}" stroke-width="7" stroke-linejoin="round" {W}/>')

# 1) 874 영상 가이드 — 코랄 배경, 큰 영상 화면
def t874():
    b = pill(80, 70, '영상 가이드', '#fff', K, 42)
    b += T(80, 345, ['줌 연락처', '수락·추가'], 132, '#fff', 'start')
    b += framed(90, 600, 780, 500, '#FFF6D6', teacher(390, 300, 1.3, 'point'))
    b += play(850, 1020, 120)
    b += pill(1030, 640, 'PC', YEL, K, 50, 'middle') + pill(1030, 770, '휴대폰', '#fff', K, 50, 'middle')
    b += spark(980, 260, 30, YEL) + spark(1110, 400, 20, '#fff') + spark(1060, 900, 18, YEL)
    return '#EC6856', b

# 2) 794 연락처 요청 — 연파랑, 휴대폰 화면 카드 + 학생
def t794():
    b = T(600, 150, ['연락처 요청 수락', '& 선생님 추가'], 96, K)
    b += box(420, 360, 640, 640, '#fff', 56, 8)
    b += T(740, 430, '연락처 요청', 46, K, weight=800)
    b += f'<path d="M460,480 L1020,480" stroke="{K}" stroke-width="5" stroke-linecap="round" {W}/>'
    b += box(460, 520, 560, 200, '#FDF1EE', 28, 6)
    b += f'<circle cx="550" cy="620" r="54" fill="{CORAL}" stroke="{K}" stroke-width="6" {W}/>' + T(550, 620, 'T', 54, '#fff')
    b += T(630, 590, 'Teacher', 44, K, 'start', 800) + T(630, 648, '연락처 요청을 보냈어요', 30, '#7a6a64', 'start', 600)
    b += box(520, 770, 220, 96, CORAL, 48, 6) + T(630, 818, '수락', 46, '#fff')
    b += box(770, 770, 220, 96, '#F4F4F4', 48, 6) + T(880, 818, '거절', 46, '#9a8f8a', weight=700)
    b += f'<path d="M560,930 L920,930" stroke="#E2DCD6" stroke-width="14" stroke-linecap="round"/>'
    b += f'<g {W}>{student(250, 760, 1.12, "cheer")}</g>'
    b += burst(980, 340, 84, YEL, '연결!', 50) + spark(150, 420, 22, YEL) + spark(1110, 1080, 18, CORAL)
    b += ''
    return '#E4EEFF', b

# 3) 448 설치·가입·로그인 — 노랑, 계단 3단계
def t448():
    b = T(600, 150, ['Zoom 설치·가입', '로그인 3단계'], 110, K)
    steps = [(90, 860, '설치', '#fff'), (450, 700, '가입', MINT), (810, 560, '로그인', CORAL)]
    for i, (x, y, lab, fill) in enumerate(steps, 1):
        b += box(x, y, 320, 1200 - y + 40, fill, 34, 8)
        b += f'<circle cx="{x + 70}" cy="{y + 74}" r="44" fill="{K}" {W}/>' + T(x + 70, y + 74, str(i), 54, '#fff')
        b += T(x + 160, y + 170, lab, 70, '#fff' if fill == CORAL else K, weight=900)
    b += f'<g {W}>{student(970, 350, 0.8, "cheer")}</g>'
    b += spark(180, 560, 26, '#fff') + spark(380, 420, 18, CORAL) + note(640, 560)
    return '#FFD966', b

# 4) 606 무료체험 입장 — 흰 바탕 + 민트 패널, 알림 말풍선
def t606():
    b = f'<rect x="40" y="40" width="1120" height="1120" rx="60" fill="{MINT_BG}" stroke="{K}" stroke-width="8" {W}/>'
    b += pill(600, 110, '첫 수업 준비', MINT, K, 40, 'middle')
    b += T(600, 330, ['무료체험', '입장하는 방법'], 120, K)
    b += framed(120, 560, 460, 460, '#fff', teacher(230, 260, 0.95, 'point'))
    b += bubble(640, 560, 460, 130, YEL, (596, 640), ['수업 5분 전!'], 56)
    b += box(660, 740, 420, 120, CORAL, 60, 8) + T(870, 800, '입장하기 ▶', 54, '#fff')
    b += f'<g {W}>{student(870, 990, 0.58, "happy")}</g>'
    b += spark(110, 520, 22, YEL) + spark(1090, 960, 18, CORAL)
    return '#ffffff', b

# 5) 250 수업 녹화 — 진한 남색, REC 화면
def t250():
    b = T(600, 170, ['Zoom 수업', '녹화하는 법'], 120, '#fff')
    b += framed(150, 400, 900, 560, '#FFE6DF', teacher(450, 330, 1.0, 'none'))
    b += f'<rect x="190" y="440" width="230" height="84" rx="42" fill="{DK}" stroke="{K}" stroke-width="6" {W}/><circle cx="240" cy="482" r="20" fill="#FF4B3A"/>' + T(330, 482, 'REC', 44, '#fff')
    for i, lab in enumerate(['PC', '태블릿', '휴대폰']):
        b += pill(600 + (i - 1) * 300, 1010, lab, [YEL, '#fff', MINT][i], K, 46, 'middle')
    b += spark(110, 330, 22, YEL) + spark(1090, 380, 16, '#fff')
    return '#26324A', b

# 6) 91 수강신청 방법 — 연분홍, 두 갈래 카드
def t91():
    b = T(600, 150, ['수강신청 방법', '두 가지 길'], 112, K)
    b += box(90, 380, 470, 600, '#fff', 44, 8) + box(640, 380, 470, 600, '#fff', 44, 8)
    b += framed(150, 430, 350, 330, '#FFF6D6', teacher(175, 190, 0.78, 'none'))
    b += T(325, 860, ['선생님부터', '고르기'], 56, K)
    gx, gy = 700, 440
    for r in range(5):
        for c in range(5):
            on = (r, c) in ((1, 0), (1, 2), (3, 4), (2, 1))
            b += f'<rect x="{gx + c*72}" y="{gy + r*62}" width="60" height="50" rx="10" fill="{CORAL if on else "#F4EFEC"}" stroke="{K}" stroke-width="4"/>'
    b += T(875, 860, ['시간부터', '고르기'], 56, K)
    b += pill(600, 1040, '나에게 맞는 쪽으로', K, '#fff', 42, 'middle')
    b += spark(600, 320, 24, YEL) + spark(80, 300, 18, CORAL) + spark(1120, 330, 18, MINT)
    return '#FFE6DF', b

def scenes():
    s = {}
    for name, fn in (('t874.png', t874), ('t794.png', t794), ('t448.png', t448), ('t606.png', t606), ('t250.png', t250), ('t91.png', t91)):
        A._defs.clear(); bg, body = fn(); s[name] = (1200, 1200, bg, body, ''.join(A._defs))
    return s
A.scenes = scenes
A.main(sys.argv[1])
