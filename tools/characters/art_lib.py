#!/usr/bin/env python3
"""아인잉글리쉬 about 페이지('왜 아인 화상영어일까?')용 그림 생성기 — 깔끔한 선에 살짝 손그림 느낌(중간 버전).

사용법: python3 art_lib.py about-assets/
선은 한 번만 긋고 살짝 흔든다. 글자는 Noto Sans 굵게.
등장인물: 학생, 선생님(헤드셋), 거북이(안내). 캐릭터 그림은 chars.py.
필요한 것: playwright, Chrome(/usr/bin/google-chrome), Noto Sans CJK KR 글꼴.
"""
import sys, os, math

K = '#4A3A34'; SK = '#FFE8D6'; CORAL = '#F0806F'; YEL = '#FFD966'; MINT = '#A6E6C8'; BLUE = '#9DBFF5'
TINT = '#FDF1EE'; BLUE_BG = '#E4EEFF'; PINK_BG = '#FFE6DF'; YEL_BG = '#FFF6D6'; MINT_BG = '#E6F8EF'
W = 'filter="url(#w)"'
_defs = []

import chars as C
_PM={'worry':'worry','happy':'smile','cheer':'happy'}
def _face(mood):
    """어린이·직장인 캐릭터가 같이 쓰는 얼굴 (머리 중심이 0,0인 예전 좌표)."""
    return f'<g transform="scale(1.8)">{C.face(_PM.get(mood,"smile"),0,4)}</g>'

def _arm(x1, y1, cx_, cy_, x2, y2, color):
    d = f'M{x1},{y1} Q{cx_},{cy_} {x2},{y2}'
    return (f'<path d="{d}" fill="none" stroke="{K}" stroke-width="30" stroke-linecap="round"/><path d="{d}" fill="none" stroke="{color}" stroke-width="17" stroke-linecap="round"/>'
            f'<circle cx="{x2}" cy="{y2-12}" r="19" fill="{SK}" stroke="{K}" stroke-width="6"/>')

def student(cx, cy, s=1.0, mood='worry'):
    body = C.student('happy','up') if mood=='cheer' else C.student(_PM.get(mood,'smile'))
    return f'<g transform="translate({cx},{cy}) scale({s*1.8:.3f}) translate(-100,-100)">{body}</g>'

def teacher(cx, cy, s=1.0, pose='point'):
    body = C.teacher('happy','wave') if pose=='point' else C.teacher('happy')
    return f'<g transform="translate({cx},{cy}) scale({s*1.9:.3f}) translate(-100,-104)">{body}</g>'

def mascot(cx, cy, s=1.0, mood='happy'):
    """안내 캐릭터: 인스타 프로필의 직장인 거북이."""
    body = C.turtle('open','up') if mood=='cheer' else C.turtle('calm','down')
    return f'<g transform="translate({cx},{cy}) scale({s*1.05:.3f}) translate(-100,-88)" {W}>{body}</g>'

def text(x, y, lines, size, anchor='middle', color=K):
    if isinstance(lines, str): lines = [lines]
    size = size * 0.8; lh = size * 1.3; y0 = y - lh * (len(lines) - 1) / 2 + size * 0.34
    return ''.join(f'<text x="{x}" y="{y0 + i * lh:.0f}" font-size="{size}" text-anchor="{anchor}" fill="{color}">{l}</text>' for i, l in enumerate(lines))

def bubble(x, y, w, h, fill, tail, lines, size=44):
    cx = x + w / 2; cy = y + h / 2; tx, ty = tail
    bx = min(max(tx, x + 70), x + w - 70); top = mid = left = right = ''
    if tx < x: left = f'L{x},{cy + 20} L{tx},{ty} L{x - 2},{cy - 16}'
    elif tx > x + w: right = f'L{x + w},{cy - 16} L{tx},{ty} L{x + w + 2},{cy + 20}'
    elif ty > cy: mid = f'L{bx + 26},{y + h + 2} L{tx},{ty} L{bx - 22},{y + h}'
    else: top = f'L{bx - 22},{y} L{tx},{ty} L{bx + 26},{y - 2}'
    d = (f'M{x + 30},{y} {top} L{x + w - 30},{y} Q{x + w + 12},{y + 4} {x + w},{cy - 20} {right} L{x + w},{cy + 24} Q{x + w + 10},{y + h - 4} {x + w - 30},{y + h} '
         f'{mid} L{x + 30},{y + h} Q{x - 12},{y + h - 4} {x},{cy + 24} {left} L{x},{cy - 20} Q{x - 12},{y + 4} {x + 30},{y} Z')
    return f'<path d="{d}" fill="{fill}" stroke="{K}" stroke-width="7" stroke-linejoin="round" {W}/>' + text(cx, cy, lines, size)

def burst(cx, cy, r, fill, label, size=64):
    pts = []
    for i in range(18):
        a = i * math.pi / 9; rr = r * (1.0 if i % 2 == 0 else 0.78)
        pts.append(f'{cx + rr * 1.25 * math.cos(a):.0f},{cy + rr * 0.8 * math.sin(a):.0f}')
    return f'<polygon points="{" ".join(pts)}" fill="{fill}" stroke="{K}" stroke-width="7" stroke-linejoin="round" {W}/>' + text(cx, cy, label, size)

def box(x, y, w, h, fill, rx=40, sw=7): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{K}" stroke-width="{sw}" {W}/>'

def framed(x, y, w, h, fill, inner):
    i = len(_defs); _defs.append(f'<clipPath id="c{i}"><rect x="{x + 3}" y="{y + 3}" width="{w - 6}" height="{h - 6}" rx="38"/></clipPath>')
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="40" fill="{fill}"/><g clip-path="url(#c{i})"><g transform="translate({x},{y})" {W}>{inner}</g></g>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="40" fill="none" stroke="{K}" stroke-width="7" {W}/>')

def spark(x, y, r=18, fill=YEL):
    return f'<path d="M{x},{y - r} Q{x + r * .2},{y - r * .2} {x + r},{y} Q{x + r * .2},{y + r * .2} {x},{y + r} Q{x - r * .2},{y + r * .2} {x - r},{y} Q{x - r * .2},{y - r * .2} {x},{y - r} Z" fill="{fill}" stroke="{K}" stroke-width="5" stroke-linejoin="round"/>'
def note(x, y): return f'<g transform="translate({x},{y})"><path d="M0,0 L0,-44 L26,-52 L26,-10" fill="none" stroke="{K}" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/><ellipse cx="-9" cy="2" rx="11" ry="8" fill="{K}"/><ellipse cx="17" cy="-8" rx="11" ry="8" fill="{K}"/></g>'
def badge(n): return f'<circle cx="84" cy="84" r="46" fill="{CORAL}" stroke="{K}" stroke-width="7" {W}/>' + text(84, 84, str(n), 60, color='#ffffff')
def strike(x1, x2, y): return f'<path d="M{x1},{y} Q{(x1 + x2) / 2},{y - 10} {x2},{y + 4}" fill="none" stroke="#E5484D" stroke-width="7" stroke-linecap="round" {W}/>'
def arrow(x, y): return f'<path d="M{x},{y} L{x},{y + 46} M{x - 18},{y + 28} L{x},{y + 48} L{x + 18},{y + 28}" fill="none" stroke="{CORAL}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>'
def tag(x, y, label, size=36):
    w = len(label) * size * 0.78 + 44
    return f'<rect x="{x}" y="{y}" width="{w:.0f}" height="{size + 26}" rx="{(size + 26) / 2}" fill="{K}" {W}/>' + text(x + w / 2, y + (size + 26) / 2, label, size, color='#ffffff')

def phone(x, y, w, h, title, rows):
    g = box(x, y, w, h, '#ffffff', 34) + text(x + w / 2, y + 46, title, 36)
    g += f'<path d="M{x + 24},{y + 78} L{x + w - 24},{y + 78}" stroke="{K}" stroke-width="5" stroke-linecap="round" {W}/>'
    yy = y + 100
    for kind, label, hh in rows:
        fill = {'y': YEL, 'g': '#D9F5E5', 'a': '#FFF0C2', 'c': CORAL, 'w': '#F4F4F4'}[kind]
        g += box(x + 24, yy, w - 48, hh, fill, 16, 5) + text(x + w / 2, yy + hh / 2, label, 28, color='#ffffff' if kind == 'c' else K)
        yy += hh + 16
    return g

# ── 장면 ─────────────────────────────────────────────
def hero():
    b = tag(70, 34, '틀린 문장을 말하면')
    b += framed(70, 330, 440, 470, BLUE_BG, student(220, 240, 1.15)) + framed(930, 330, 440, 470, PINK_BG, teacher(200, 250, 1.15))
    b += bubble(60, 120, 560, 170, '#ffffff', (250, 342), ['He always try', 'to care of others…'], 46)
    b += bubble(800, 110, 590, 170, YEL, (1100, 336), ['He always tries', 'to take care of others!'], 46)
    b += burst(720, 440, 120, MINT, 'tries!', 84) + text(720, 628, ['그 자리에서', '바로 고쳐요'], 46)
    b += text(290, 846, '학생', 44) + text(1150, 846, '선생님', 44)
    o = 900
    b += f'<path d="M70,{o} L1370,{o}" stroke="{K}" stroke-width="5" stroke-dasharray="4 22" stroke-linecap="round"/>'
    b += tag(70, o + 40, '따라 말하면')
    b += framed(70, o + 330, 440, 470, BLUE_BG, student(220, 250, 1.15, 'cheer')) + framed(930, o + 330, 440, 470, PINK_BG, teacher(200, 250, 1.15, 'none'))
    b += bubble(60, o + 120, 620, 170, MINT, (250, o + 342), ['He always tries', 'to take care of others!'], 46)
    b += burst(1150, o + 200, 130, YEL, 'Perfect!', 68)
    b += mascot(720, o + 520, 1.25, 'cheer') + note(600, o + 400) + note(852, o + 380) + spark(580, o + 560, 20) + spark(866, o + 600, 16, MINT)
    b += text(720, o + 760, '입에 붙었어요!', 50)
    b += text(290, o + 846, '학생', 44) + text(1150, o + 846, '선생님', 44)
    return 1440, 1790, '#ffffff', b

def pain(mood, bubbles, bg):
    b = f'<g {W}>{student(180, 290, 1.05, mood)}</g>'; y = 50
    for lines, fill, tail in bubbles:
        h = 50 + len(lines) * 46
        b += bubble(340, y, 340, h, fill, tail if tail else (292, y + h / 2 + 30), lines, 36); y += h + 34
    return 720, 480, bg, b

def flow(n, body): return 720, 720, TINT, badge(n) + body
def f1():
    return (framed(70, 180, 270, 290, BLUE_BG, student(135, 150, 0.8, 'happy')) + framed(380, 180, 270, 290, PINK_BG, teacher(125, 160, 0.8, 'none'))
            + text(205, 506, '학생', 38) + text(515, 506, '선생님', 38) + bubble(110, 560, 500, 110, '#ffffff', (360, 548), ['25분, 선생님과 1:1 대화'], 40))
def f2():
    return (bubble(70, 170, 580, 120, '#ffffff', (150, 330), ['I go to there yesterday.'], 44) + strike(120, 600, 232) + arrow(360, 322)
            + bubble(70, 400, 580, 130, YEL, (560, 560), ['I went there yesterday.'], 48) + mascot(600, 620, 0.62) + text(300, 630, '틀린 문장은 그 자리에서', 40))
def f3():
    return (framed(60, 300, 330, 360, BLUE_BG, student(165, 190, 0.95, 'cheer')) + bubble(150, 130, 520, 120, MINT, (260, 300), ['I went there yesterday!'], 44)
            + burst(545, 400, 104, YEL, 'Good job!', 40) + note(430, 560) + spark(620, 560, 20) + spark(470, 300, 14, CORAL) + text(540, 640, ['따라 말하면', '내 문장!'], 40))
def f4():
    return (phone(70, 160, 290, 480, '일일평가서', [('w', 'Q1. Student: …', 60), ('g', 'BETTER', 84), ('a', 'ALTERNATIVE', 70), ('c', '복습 완료하기', 64)])
            + box(400, 190, 270, 250, '#ffffff', 30) + text(535, 236, '실전 퀴즈', 34) + text(535, 312, ['I ____ there', 'yesterday.'], 38)
            + box(470, 372, 130, 50, YEL, 14, 5) + text(535, 397, 'went', 38) + mascot(535, 560, 0.7, 'cheer') + spark(650, 180, 22))
def trial(bg, body): return 720, 480, bg, body
def t1():
    return (phone(60, 40, 260, 400, '무료체험 신청', [('y', '강사 추천받기', 62), ('w', '직접 강사 선택', 62), ('c', '신청하기', 66)])
            + f'<g {W}>{student(530, 330, 0.95, "happy")}</g>' + bubble(370, 30, 320, 100, '#ffffff', (480, 200), ['오늘 바로 될까?'], 38))
def t2():
    return (framed(50, 96, 250, 260, '#D6E4FF', student(125, 140, 0.75, 'happy')) + framed(330, 96, 250, 260, '#FFD9D0', teacher(120, 150, 0.75, 'none'))
            + burst(610, 100, 78, YEL, '15분', 48) + bubble(110, 380, 500, 86, '#ffffff', (190, 340), ['Hello! Nice to meet you.'], 38))
def t3():
    g = box(140, 70, 410, 380, '#ffffff', 30) + text(300, 126, '레벨테스트 결과', 38)
    g += f'<circle cx="490" cy="126" r="48" fill="{CORAL}" stroke="{K}" stroke-width="6" {W}/>' + text(490, 126, 'Lv.4', 38, color='#ffffff')
    for i, (n, w_) in enumerate((('어휘', 62), ('리스닝', 74), ('유창성', 50), ('문법', 56), ('발음', 70))):
        y = 200 + i * 48
        g += text(176, y + 10, n, 30, 'start') + f'<rect x="280" y="{y - 4}" width="240" height="24" rx="12" fill="#F1F1F1" stroke="{K}" stroke-width="4"/><rect x="280" y="{y - 4}" width="{240 * w_ / 100:.0f}" height="24" rx="12" fill="{CORAL}" stroke="{K}" stroke-width="4"/>'
    return g + tag(180, 8, '30분~1시간 안에 도착', 30) + mascot(640, 330, 0.6, 'cheer')
def t4():
    return (f'<g {W}>{student(170, 300, 1.0, "happy")}</g>' + mascot(610, 380, 0.62) + bubble(300, 40, 390, 150, YEL, (590, 290), ['수업 시간과 교재,', '같이 정해 드릴게요'], 36)
            + bubble(310, 236, 220, 84, '#ffffff', (268, 300), ['네, 좋아요!'], 36) + tag(300, 400, '학습 매니저 상담', 28))

def scenes():
    s = {}
    def add(name, fn):
        _defs.clear(); w, h, bg, body = fn(); s[name] = (w, h, bg, body, ''.join(_defs))
    add('hero_scene.png', hero)
    add('pain_1.png', lambda: pain('worry', [(['Um… I…', 'yesterday… movie?'], '#ffffff', None)], BLUE_BG))
    add('pain_2.png', lambda: pain('happy', [(['It was good.'], '#ffffff', None), (['It was good.'], '#ffffff', None), (['It was… good.'], '#ffffff', None)], YEL_BG))
    add('pain_3.png', lambda: pain('worry', [(['I go to there', 'yesterday.'], '#ffffff', None), (['Okay! Next~'], YEL, (716, 380))], PINK_BG))
    add('pain_4.png', lambda: pain('worry', [(['어제 뭐', '배웠더라…?'], '#ffffff', None)], MINT_BG))
    for i, fn in enumerate((f1, f2, f3, f4), 1): add(f'flow_{i}.png', (lambda fn=fn, i=i: flow(i, fn())))
    for i, (fn, bg) in enumerate(((t1, BLUE_BG), (t2, YEL_BG), (t3, PINK_BG), (t4, MINT_BG)), 1): add(f'trial_{i}.png', (lambda fn=fn, bg=bg: trial(bg, fn())))
    return s

def main(outdir, fontdir=None):
    from playwright.sync_api import sync_playwright
    os.makedirs(outdir, exist_ok=True)
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path='/usr/bin/google-chrome')
        for name, (w, h, bg, body, defs) in scenes().items():
            pg = b.new_page(viewport={'width': w, 'height': h})
            pg.set_content(f'''<!DOCTYPE html><html><head><meta charset="utf-8"><style>body{{margin:0}}text{{font-family:"Noto Sans CJK KR",sans-serif;font-weight:700;letter-spacing:-.01em}}</style></head><body><svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><defs><filter id="w" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="0.012" numOctaves="2" seed="4"/><feDisplacementMap in="SourceGraphic" scale="6"/></filter>{defs}</defs><rect width="{w}" height="{h}" fill="{bg}"/>{body}</svg></body></html>''')
            pg.wait_for_timeout(150); pg.screenshot(path=os.path.join(outdir, name), omit_background=(bg == 'none')); pg.close(); print(name, (w, h))
        b.close()

if __name__ == '__main__':
    main(sys.argv[1])
