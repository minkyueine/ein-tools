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
    b += box(90, 600, 780, 500, '#FFF6D6', 40, 8)
    b += play(480, 830, 150)
    b += f'<rect x="150" y="1030" width="660" height="18" rx="9" fill="#F2D9A8" stroke="{K}" stroke-width="5"/><rect x="150" y="1030" width="260" height="18" rx="9" fill="{CORAL}" stroke="{K}" stroke-width="5"/><circle cx="410" cy="1039" r="20" fill="#fff" stroke="{K}" stroke-width="6"/>'
    b += pill(1030, 640, 'PC', YEL, K, 50, 'middle') + pill(1030, 770, '휴대폰', '#fff', K, 50, 'middle')
    b += spark(980, 260, 30, YEL) + spark(1110, 400, 20, '#fff') + spark(1060, 900, 18, YEL)
    return '#EC6856', b

# 2) 794 연락처 요청 — 연파랑, 휴대폰 화면 카드 + 학생
def t794():
    b = T(600, 150, ['연락처 요청 수락', '& 선생님 추가'], 96, K)
    b += box(140, 360, 920, 640, '#fff', 56, 8)
    b += T(600, 440, '연락처 요청', 54, K, weight=800)
    b += f'<path d="M180,500 L1020,500" stroke="{K}" stroke-width="5" stroke-linecap="round" {W}/>'
    b += box(180, 540, 840, 210, '#FDF1EE', 28, 6)
    b += f'<circle cx="290" cy="645" r="62" fill="{CORAL}" stroke="{K}" stroke-width="6" {W}/>' + T(290, 645, 'T', 62, '#fff')
    b += T(390, 612, 'Teacher', 52, K, 'start', 800) + T(390, 678, '연락처 요청을 보냈어요', 36, '#7a6a64', 'start', 600)
    b += box(350, 800, 230, 100, CORAL, 50, 6) + T(465, 850, '수락', 50, '#fff')
    b += box(620, 800, 230, 100, '#F4F4F4', 50, 6) + T(735, 850, '거절', 50, '#9a8f8a', weight=700)
    b += burst(1010, 350, 84, YEL, '연결!', 50) + spark(150, 420, 22, YEL) + spark(1110, 1080, 18, CORAL)
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
    b += f'<path d="M970,560 L970,330" stroke="{K}" stroke-width="10" stroke-linecap="round"/><path d="M970,335 L1100,375 L970,420 Z" fill="{MINT}" stroke="{K}" stroke-width="7" stroke-linejoin="round" {W}/>' + burst(1040, 470, 60, YEL, '완료', 36)
    b += spark(180, 560, 26, '#fff') + spark(380, 420, 18, CORAL) + note(640, 560)
    return '#FFD966', b

# 4) 606 무료체험 입장 — 흰 바탕 + 민트 패널, 알림 말풍선
def t606():
    b = f'<rect x="40" y="40" width="1120" height="1120" rx="60" fill="{MINT_BG}" stroke="{K}" stroke-width="8" {W}/>'
    b += pill(600, 110, '첫 수업 준비', MINT, K, 40, 'middle')
    b += T(600, 330, ['무료체험', '입장하는 방법'], 120, K)
    b += box(150, 560, 900, 470, '#fff', 44, 8)
    b += f'<circle cx="300" cy="700" r="90" fill="{YEL}" stroke="{K}" stroke-width="8" {W}/><path d="M300,640 L300,700 L345,725" fill="none" stroke="{K}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>'
    b += T(430, 668, '수업 5분 전', 60, K, 'start', 900) + T(430, 738, '입장 안내가 왔어요', 40, '#7a6a64', 'start', 700)
    b += box(240, 850, 720, 120, CORAL, 60, 8) + T(600, 910, '입장하기 ▶', 60, '#fff')
    b += spark(110, 520, 22, YEL) + spark(1090, 960, 18, CORAL)
    return '#ffffff', b

# 5) 250 수업 녹화 — 진한 남색, REC 화면
def t250():
    b = T(600, 170, ['Zoom 수업', '녹화하는 법'], 120, '#fff')
    b += box(150, 400, 900, 560, '#FFE6DF', 40, 8)
    b += f'<circle cx="600" cy="690" r="130" fill="#fff" stroke="{K}" stroke-width="8" {W}/><circle cx="600" cy="690" r="70" fill="#FF4B3A" stroke="{K}" stroke-width="6" {W}/>'
    b += T(600, 890, '00:12:34', 52, K, weight=800)
    b += f'<rect x="190" y="440" width="230" height="84" rx="42" fill="{DK}" stroke="{K}" stroke-width="6" {W}/><circle cx="240" cy="482" r="20" fill="#FF4B3A"/>' + T(330, 482, 'REC', 44, '#fff')
    for i, lab in enumerate(['PC', '태블릿', '휴대폰']):
        b += pill(600 + (i - 1) * 300, 1010, lab, [YEL, '#fff', MINT][i], K, 46, 'middle')
    b += spark(110, 330, 22, YEL) + spark(1090, 380, 16, '#fff')
    return '#26324A', b

# 6) 91 수강신청 방법 — 연분홍, 두 갈래 카드
def t91():
    b = T(600, 150, ['수강신청 방법', '두 가지 길'], 112, K)
    b += box(90, 380, 470, 600, '#fff', 44, 8) + box(640, 380, 470, 600, '#fff', 44, 8)
    b += box(150, 430, 350, 330, '#FFF6D6', 36, 6)
    for i,(y,f) in enumerate(((470,CORAL),(570,MINT),(670,'#9DBFF5'))):
        b += f'<circle cx="205" cy="{y+40}" r="34" fill="{f}" stroke="{K}" stroke-width="5"/><rect x="260" y="{y+20}" width="200" height="16" rx="8" fill="#E2D6C8"/><rect x="260" y="{y+48}" width="140" height="14" rx="7" fill="#EFE6DA"/>'
    b += spark(470, 470, 22, YEL)
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
