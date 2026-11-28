#!/usr/bin/env python3
"""아인잉글리쉬 블로그 썸네일 생성기 (2026-11-28 개편판).

사용법:  python3 thumbs.py spec.json 출력폴더
spec.json의 각 글 "thumbnail"로 1200x1200 썸네일을 만든다(HTML/SVG를 Playwright로 렌더링).

thumbnail 필드
  layout  : "scene"(주제 장면 그림, 기본) | "versus"(표현 비교 타일) | "call"(화상수업 화면)
  palette : PALETTES 이름. 글마다, 그리고 전날 글과 다르게 고른다.
  kicker  : 제목 위 작은 줄 (예: "화상영어 롤플레이")
  title   : 큰 제목 두 줄 ["식당 예약 영어", "3단계로 끝내기"]
  hook    : 그림 위 스티커에 들어갈 짧은 영어 (선택)
  scene   : scene 레이아웃의 장면 이름 (SCENES 참고)
  words   : versus 레이아웃의 비교 타일 [{"w":"see","ko":"보이다","icon":"eye"}, ...]
  people  : call 레이아웃의 학생 표정·말풍선 {"student":"wow","bubble":"Could you say that again?"}
category(knowhow/tip)는 왼쪽 위 배지로만 구분하고, 배경색은 palette로 매번 바꾼다.
"""
import json, os, sys, html as H

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = 'file://' + os.path.join(HERE, 'fonts')

INK = '#16161D'
PALETTES = {
    'tomato':    dict(bg='#FF5B4F', dot='#FF7A70', acc='#FFE04A', deep='#B8231A', dark=False),
    'cobalt':    dict(bg='#2D5BFF', dot='#4A72FF', acc='#FFE04A', deep='#1A2F99', dark=True),
    'lilac':     dict(bg='#B7A3FF', dot='#C6B6FF', acc='#FFE04A', deep='#5B3FD6', dark=False),
    'sky':       dict(bg='#5EC3FF', dot='#7ACFFF', acc='#FF6F9C', deep='#1D6FB8', dark=False),
    'tangerine': dict(bg='#FF9A3D', dot='#FFAE60', acc='#1F2B7A', deep='#C25E0A', dark=False),
    'forest':    dict(bg='#1E8C5E', dot='#2B9C6C', acc='#FFD27A', deep='#0E5B3A', dark=True),
    'pink':      dict(bg='#FF8DB8', dot='#FFA3C6', acc='#2A2A80', deep='#D1457D', dark=False),
    'lemon':     dict(bg='#FFE15A', dot='#FFE97F', acc='#FF5B4F', deep='#D9A800', dark=False),
    'night':     dict(bg='#1D2040', dot='#2A2E57', acc='#FFE04A', deep='#0E1026', dark=True),
    'mint':      dict(bg='#4FDDB0', dot='#6EE5BF', acc='#2D2DA8', deep='#159A70', dark=False),
}
CAT = {'knowhow': ('화상영어 노하우', '#FFD60A', INK), 'tip': ('영어공부 꿀팁', '#3FDDA8', INK)}
SKIN = ['#FFDCC2', '#F6C9A4', '#E8B08A', '#C98E66']

def esc(s): return H.escape(s, quote=True)

# ---------------------------------------------------------------- 사람
def person(x, y, s, skin=SKIN[0], hair='#3B2416', style='short', shirt='#2F6FDE',
           face='smile', headset=False, glasses=False, hand=None, flip=False):
    """머리+어깨 캐릭터. (x,y)=왼쪽 위, s=폭(px). viewBox 200x230."""
    hs = {
        'short': '<path d="M44 92 C40 40 80 22 104 24 C140 26 164 52 158 96 C150 70 128 58 100 60 C76 60 56 70 44 92Z" fill="{h}"/>'
                 '<path d="M96 26 C104 8 124 10 122 22" fill="none" stroke="{h}" stroke-width="7" stroke-linecap="round"/>',
        'bob':   '<path d="M38 140 C26 70 56 28 100 28 C146 28 176 70 162 140 L146 140 C150 100 140 74 100 72 C62 72 52 100 54 140Z" fill="{h}"/>'
                 '<path d="M52 92 C60 56 90 48 118 52 C142 56 152 76 150 92 C130 74 92 72 52 92Z" fill="{h}"/>',
        'long':  '<path d="M34 196 C20 90 50 28 100 28 C150 28 182 90 166 196 L140 196 C148 120 140 76 100 74 C60 76 52 120 60 196Z" fill="{h}"/>'
                 '<path d="M52 94 C58 54 90 46 116 50 C144 54 152 76 150 94 C128 70 84 70 52 94Z" fill="{h}"/>',
        'bun':   '<circle cx="100" cy="20" r="22" fill="{h}"/>'
                 '<path d="M44 96 C42 44 76 30 100 30 C126 30 160 44 156 96 C146 70 124 62 100 62 C76 62 56 70 44 96Z" fill="{h}"/>',
        'curly': ''.join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{{h}}"/>' for cx, cy, r in
                         [(60,70,26),(84,46,28),(116,44,28),(142,66,26),(156,96,18),(46,98,18),(100,56,22)]),
        'spiky': '<path d="M42 96 L50 52 L66 66 L76 30 L94 54 L110 24 L122 54 L142 34 L146 66 L160 58 L158 98 C144 72 122 62 100 62 C76 62 56 72 42 96Z" fill="{h}"/>',
    }[style].replace('{h}', hair)
    eyes = {
        'smile': '<path d="M70 112 Q78 102 86 112" fill="none" stroke="#2B1B12" stroke-width="6" stroke-linecap="round"/>'
                 '<path d="M114 112 Q122 102 130 112" fill="none" stroke="#2B1B12" stroke-width="6" stroke-linecap="round"/>',
        'wow':   '<ellipse cx="78" cy="110" rx="9" ry="12" fill="#2B1B12"/><ellipse cx="122" cy="110" rx="9" ry="12" fill="#2B1B12"/>'
                 '<circle cx="81" cy="105" r="3.5" fill="#fff"/><circle cx="125" cy="105" r="3.5" fill="#fff"/>',
        'think': '<ellipse cx="78" cy="112" rx="7" ry="9" fill="#2B1B12"/><ellipse cx="122" cy="112" rx="7" ry="9" fill="#2B1B12"/>'
                 '<path d="M64 96 Q74 86 88 90 M112 90 Q126 86 136 96" fill="none" stroke="#2B1B12" stroke-width="5" stroke-linecap="round"/>',
        'talk':  '<ellipse cx="78" cy="110" rx="7" ry="10" fill="#2B1B12"/><ellipse cx="122" cy="110" rx="7" ry="10" fill="#2B1B12"/>'
                 '<circle cx="80" cy="106" r="3" fill="#fff"/><circle cx="124" cy="106" r="3" fill="#fff"/>',
        'wink':  '<path d="M70 112 Q78 102 86 112" fill="none" stroke="#2B1B12" stroke-width="6" stroke-linecap="round"/>'
                 '<ellipse cx="122" cy="110" rx="7" ry="10" fill="#2B1B12"/>',
    }[face]
    mouth = {
        'smile': '<path d="M84 136 Q100 156 116 136 Z" fill="#8A2E25"/><path d="M90 144 Q100 152 110 144" fill="#FF8A8A"/>',
        'wow':   '<ellipse cx="100" cy="144" rx="10" ry="13" fill="#8A2E25"/>',
        'think': '<path d="M88 144 Q100 138 112 146" fill="none" stroke="#8A2E25" stroke-width="5" stroke-linecap="round"/>',
        'talk':  '<path d="M84 134 Q100 160 116 134 Z" fill="#8A2E25"/><path d="M92 146 Q100 152 108 146 Z" fill="#FF8A8A"/>',
        'wink':  '<path d="M84 136 Q100 156 116 136 Z" fill="#8A2E25"/>',
    }[face]
    extra = ''
    if glasses:
        extra += ('<g fill="none" stroke="#1B1B1B" stroke-width="4"><circle cx="78" cy="110" r="17"/>'
                  '<circle cx="122" cy="110" r="17"/><path d="M95 110 H105"/></g>')
    if headset:
        extra += ('<path d="M40 112 C36 40 164 40 160 112" fill="none" stroke="#1B1B1B" stroke-width="9"/>'
                  '<rect x="30" y="98" width="20" height="38" rx="9" fill="#1B1B1B"/>'
                  '<rect x="150" y="98" width="20" height="38" rx="9" fill="#1B1B1B"/>'
                  '<path d="M40 134 Q46 162 76 160" fill="none" stroke="#1B1B1B" stroke-width="5"/>'
                  '<circle cx="78" cy="160" r="6" fill="#1B1B1B"/>')
    arm = ''
    if hand == 'wave':
        arm = (f'<path d="M156 230 C170 200 176 170 178 150" stroke="{shirt}" stroke-width="30" stroke-linecap="round" fill="none"/>'
               f'<circle cx="180" cy="138" r="18" fill="{skin}"/>')
    elif hand == 'phone':
        arm = (f'<path d="M150 230 C168 206 170 176 156 146" stroke="{shirt}" stroke-width="30" stroke-linecap="round" fill="none"/>'
               '<rect x="140" y="88" width="34" height="62" rx="8" fill="#1B1B1B" transform="rotate(-12 157 119)"/>'
               f'<circle cx="152" cy="140" r="16" fill="{skin}"/>')
    elif hand == 'chin':
        arm = (f'<path d="M60 230 C70 200 84 182 96 172" stroke="{shirt}" stroke-width="28" stroke-linecap="round" fill="none"/>'
               f'<circle cx="100" cy="166" r="16" fill="{skin}"/>')
    tr = f' transform="translate(200 0) scale(-1 1)"' if flip else ''
    return (f'<svg x="{x}" y="{y}" width="{s}" height="{s*1.15:.0f}" viewBox="0 0 200 230" overflow="visible"><g{tr}>'
            f'<path d="M22 230 C22 186 58 168 100 168 C142 168 178 186 178 230Z" fill="{shirt}"/>'
            f'<path d="M80 168 Q100 190 120 168Z" fill="#fff"/>'
            f'<rect x="86" y="150" width="28" height="24" fill="{skin}"/>'
            + (hs if style in ('long', 'bob') else '') +
            f'<ellipse cx="100" cy="112" rx="58" ry="60" fill="{skin}"/>'
            f'<ellipse cx="62" cy="134" rx="10" ry="6" fill="#FF9AA2" opacity=".8"/><ellipse cx="138" cy="134" rx="10" ry="6" fill="#FF9AA2" opacity=".8"/>'
            + (hs if style not in ('long', 'bob') else
               '<path d="M44 100 C44 52 76 36 104 38 C134 40 158 58 156 100 C140 76 116 68 100 68 C80 68 60 78 44 100Z" fill="%s"/>' % hair)
            + eyes + mouth + extra + arm + '</g></svg>')

# ---------------------------------------------------------------- 소품
def phone_call(x, y, s, name, sub, acc):
    return (f'<svg x="{x}" y="{y}" width="{s}" height="{s*1.9:.0f}" viewBox="0 0 200 380">'
            '<rect x="6" y="6" width="188" height="368" rx="34" fill="#16161D"/>'
            '<rect x="18" y="22" width="164" height="336" rx="24" fill="#F7F4EE"/>'
            '<rect x="76" y="30" width="48" height="10" rx="5" fill="#16161D"/>'
            f'<circle cx="100" cy="112" r="40" fill="{acc}"/>'
            '<path d="M88 92 v18 M82 92 v12 q0 8 6 8 q6 0 6 -8 v-12 M88 112 v24" stroke="#16161D" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M112 92 q-10 10 -4 24 h4 v20" stroke="#16161D" stroke-width="5" fill="none" stroke-linecap="round"/>'
            f'<text x="100" y="186" text-anchor="middle" font-family="Pretendard" font-weight="800" font-size="20" fill="#16161D">{esc(name)}</text>'
            f'<text x="100" y="212" text-anchor="middle" font-family="Pretendard" font-weight="600" font-size="15" fill="#7A7A85">{esc(sub)}</text>'
            '<circle cx="60" cy="300" r="26" fill="#FF4B3A"/><path d="M47 300 q13 -10 26 0" stroke="#fff" stroke-width="6" fill="none" stroke-linecap="round"/>'
            '<circle cx="140" cy="300" r="26" fill="#2BC46B"/><path d="M128 296 q12 12 24 0" stroke="#fff" stroke-width="6" fill="none" stroke-linecap="round"/>'
            '</svg>')

def table_scene(x, y, s):
    return (f'<svg x="{x}" y="{y}" width="{s}" height="{s*0.62:.0f}" viewBox="0 0 400 250">'
            '<ellipse cx="200" cy="120" rx="196" ry="70" fill="#fff"/>'
            '<path d="M4 120 v30 c0 40 392 40 392 0 v-30" fill="#E9E2D6"/>'
            '<ellipse cx="200" cy="114" rx="70" ry="26" fill="#F3EEE6" stroke="#D8D0C2" stroke-width="4"/>'
            '<ellipse cx="200" cy="112" rx="40" ry="14" fill="#FF9A3D"/><circle cx="188" cy="108" r="6" fill="#2BC46B"/><circle cx="210" cy="110" r="5" fill="#FF4B3A"/>'
            '<rect x="100" y="80" width="8" height="64" rx="4" fill="#9AA0AA"/><path d="M96 80 v-20 M104 80 v-20 M112 80 v-20" stroke="#9AA0AA" stroke-width="4"/>'
            '<rect x="292" y="80" width="10" height="64" rx="5" fill="#9AA0AA"/><path d="M302 60 q14 10 0 34z" fill="#9AA0AA"/>'
            '<g transform="translate(280 30) rotate(6)"><path d="M0 50 L20 0 H96 L116 50Z" fill="#16161D"/>'
            '<text x="58" y="34" text-anchor="middle" font-family="Pretendard" font-weight="900" font-size="17" fill="#FFE04A">RESERVED</text></g>'
            '<path d="M60 150 v90 M340 150 v90" stroke="#C9BFAE" stroke-width="12" stroke-linecap="round"/>'
            '</svg>')

def clock(x, y, s, h=7, m=0, col='#fff'):
    import math
    ha = math.radians((h % 12 + m / 60) * 30 - 90); ma = math.radians(m * 6 - 90)
    return (f'<svg x="{x}" y="{y}" width="{s}" height="{s}" viewBox="0 0 100 100">'
            f'<circle cx="50" cy="50" r="46" fill="{col}" stroke="#16161D" stroke-width="6"/>'
            + ''.join(f'<circle cx="{50+36*math.cos(math.radians(a)):.1f}" cy="{50+36*math.sin(math.radians(a)):.1f}" r="3" fill="#16161D"/>' for a in range(0, 360, 30)) +
            f'<path d="M50 50 L{50+22*math.cos(ha):.1f} {50+22*math.sin(ha):.1f}" stroke="#16161D" stroke-width="7" stroke-linecap="round"/>'
            f'<path d="M50 50 L{50+32*math.cos(ma):.1f} {50+32*math.sin(ma):.1f}" stroke="#FF4B3A" stroke-width="5" stroke-linecap="round"/>'
            '<circle cx="50" cy="50" r="5" fill="#16161D"/></svg>')

def icon(name, x, y, s, col, bg='#fff'):
    body = {
        'eye':   f'<path d="M8 50 Q50 8 92 50 Q50 92 8 50Z" fill="{bg}" stroke="#16161D" stroke-width="6"/><circle cx="50" cy="50" r="18" fill="{col}"/><circle cx="50" cy="50" r="8" fill="#16161D"/><circle cx="56" cy="44" r="4" fill="#fff"/>',
        'look':  f'<circle cx="42" cy="42" r="28" fill="{bg}" stroke="#16161D" stroke-width="7"/><circle cx="42" cy="42" r="14" fill="{col}"/><path d="M62 62 L88 88" stroke="#16161D" stroke-width="12" stroke-linecap="round"/>',
        'watch': f'<rect x="6" y="18" width="88" height="62" rx="10" fill="{bg}" stroke="#16161D" stroke-width="6"/><path d="M42 36 L64 49 L42 62Z" fill="{col}"/><path d="M34 92 H66" stroke="#16161D" stroke-width="6" stroke-linecap="round"/>',
        'speak': f'<path d="M10 20 H90 V66 H44 L24 86 V66 H10Z" fill="{bg}" stroke="#16161D" stroke-width="6" stroke-linejoin="round"/><circle cx="32" cy="43" r="6" fill="{col}"/><circle cx="50" cy="43" r="6" fill="{col}"/><circle cx="68" cy="43" r="6" fill="{col}"/>',
        'ear':   f'<path d="M30 40 C30 10 80 10 78 44 C76 64 58 64 58 82 C58 94 40 96 36 84" fill="{bg}" stroke="#16161D" stroke-width="7" stroke-linecap="round"/><path d="M46 42 C46 30 64 30 62 44" fill="none" stroke="{col}" stroke-width="7" stroke-linecap="round"/>',
        'pen':   f'<path d="M20 80 L70 30 L84 44 L34 94 L14 98Z" fill="{col}" stroke="#16161D" stroke-width="6" stroke-linejoin="round"/>',
        'bulb':  f'<path d="M50 8 C24 8 14 32 22 50 C28 62 36 66 36 78 H64 C64 66 72 62 78 50 C86 32 76 8 50 8Z" fill="{col}" stroke="#16161D" stroke-width="6"/><path d="M38 88 H62" stroke="#16161D" stroke-width="7" stroke-linecap="round"/>',
    }[name]
    return f'<svg x="{x}" y="{y}" width="{s}" height="{s}" viewBox="0 0 100 100">{body}</svg>'

def headphones(x, y, s, col):
    return (f'<svg x="{x}" y="{y}" width="{s}" height="{s}" viewBox="0 0 200 200">'
            '<path d="M30 120 C20 30 180 30 170 120" fill="none" stroke="#16161D" stroke-width="18" stroke-linecap="round"/>'
            f'<rect x="14" y="104" width="50" height="80" rx="22" fill="{col}" stroke="#16161D" stroke-width="8"/>'
            f'<rect x="136" y="104" width="50" height="80" rx="22" fill="{col}" stroke="#16161D" stroke-width="8"/></svg>')

def wave(x, y, w, h, col, n=22, seed=3):
    import random
    r = random.Random(seed); bw = w / n
    bars = ''.join(f'<rect x="{i*bw+bw*0.2:.1f}" y="{h/2-hh/2:.1f}" width="{bw*0.6:.1f}" height="{hh:.1f}" rx="{bw*0.3:.1f}" fill="{col}"/>'
                   for i, hh in enumerate(h * (0.25 + 0.75 * abs(__import__("math").sin(i * 0.55 + r.random()))) for i in range(n)))
    return f'<svg x="{x}" y="{y}" width="{w}" height="{h}">{bars}</svg>'

def notebook(x, y, w, h, lines, acc):
    rows = ''
    for i, (t, hl) in enumerate(lines):
        yy = 92 + i * 64
        if hl: rows += f'<rect x="58" y="{yy-38}" width="{hl}" height="44" rx="6" fill="{acc}" opacity=".85"/>'
        rows += f'<text x="62" y="{yy}" font-family="Pretendard" font-weight="800" font-size="34" fill="#16161D">{esc(t)}</text>'
    rl = ''.join(f'<path d="M40 {104+i*64} H{w-30}" stroke="#D9E4F2" stroke-width="3"/>' for i in range(len(lines)))
    rings = ''.join(f'<circle cx="{60+i*((w-120)/5):.0f}" cy="16" r="11" fill="#16161D"/>' for i in range(6))
    return (f'<svg x="{x}" y="{y}" width="{w}" height="{h}" overflow="visible">'
            f'<rect x="12" y="14" width="{w-12}" height="{h-14}" rx="22" fill="#16161D"/>'
            f'<rect x="0" y="0" width="{w-12}" height="{h-14}" rx="22" fill="#fff" stroke="#16161D" stroke-width="6"/>'
            f'<path d="M40 30 V{h-30}" stroke="#FF9AA2" stroke-width="3"/>{rl}{rings}{rows}</svg>')

def map_card(x, y, s, acc):
    return (f'<svg x="{x}" y="{y}" width="{s}" height="{s*0.8:.0f}" viewBox="0 0 300 240">'
            '<path d="M10 30 L100 10 L200 30 L290 10 V210 L200 230 L100 210 L10 230Z" fill="#FFF7E6" stroke="#16161D" stroke-width="6" stroke-linejoin="round"/>'
            '<path d="M100 10 V210 M200 30 V230" stroke="#E8DCC4" stroke-width="4"/>'
            '<path d="M40 190 C80 150 120 170 150 130 S220 80 250 60" fill="none" stroke="#2D5BFF" stroke-width="9" stroke-dasharray="2 18" stroke-linecap="round"/>'
            f'<path d="M250 20 C226 20 214 38 214 54 C214 78 250 108 250 108 C250 108 286 78 286 54 C286 38 274 20 250 20Z" fill="{acc}" stroke="#16161D" stroke-width="6"/>'
            '<circle cx="250" cy="54" r="11" fill="#fff" stroke="#16161D" stroke-width="5"/>'
            '<circle cx="40" cy="190" r="12" fill="#16161D"/></svg>')

def calendar(x, y, s, acc, top='SAT', num='29'):
    return (f'<svg x="{x}" y="{y}" width="{s}" height="{s}" viewBox="0 0 200 200">'
            '<rect x="14" y="26" width="180" height="168" rx="22" fill="#16161D"/>'
            '<rect x="6" y="18" width="180" height="168" rx="22" fill="#fff" stroke="#16161D" stroke-width="6"/>'
            f'<path d="M6 70 V40 a22 22 0 0 1 22 -22 H164 a22 22 0 0 1 22 22 V70Z" fill="{acc}" stroke="#16161D" stroke-width="6"/>'
            f'<text x="96" y="58" text-anchor="middle" font-family="Pretendard" font-weight="900" font-size="30" fill="#16161D">{top}</text>'
            f'<text x="96" y="160" text-anchor="middle" font-family="Pretendard" font-weight="900" font-size="82" fill="#16161D">{num}</text>'
            '<path d="M50 8 v26 M142 8 v26" stroke="#16161D" stroke-width="10" stroke-linecap="round"/></svg>')

def bubble(x, y, w, h, text, fill='#fff', tail='left', size=46, font='Pretendard', weight=900, col=INK, rot=0):
    tx = 0.22 * w if tail == 'left' else 0.78 * w
    tp = (f'<path d="M{tx-26} {h-8} L{tx-(40 if tail=="left" else -40)} {h+44} L{tx+26} {h-8}Z" fill="{fill}" stroke="#16161D" stroke-width="6" stroke-linejoin="round"/>'
          f'<path d="M{tx-20} {h-12} L{tx+20} {h-12}" stroke="{fill}" stroke-width="10"/>') if tail else ''
    return (f'<div class="fit" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate({rot}deg)">'
            f'<svg width="{w}" height="{h+50}" style="position:absolute;left:0;top:0;overflow:visible">'
            f'<rect x="8" y="10" width="{w-8}" height="{h-6}" rx="{min(h/2,40)}" fill="#16161D"/>'
            f'<rect x="0" y="0" width="{w-8}" height="{h-8}" rx="{min(h/2,40)}" fill="{fill}" stroke="#16161D" stroke-width="6"/>{tp}</svg>'
            f'<div class="t" style="position:absolute;left:24px;right:32px;top:0;height:{h-8}px;display:flex;align-items:center;justify-content:center;'
            f'font-family:{font};font-weight:{weight};font-size:{size}px;color:{col};white-space:nowrap">{esc(text)}</div></div>')

def sparkles(pts, col):
    return ''.join(f'<svg x="{x}" y="{y}" width="{s}" height="{s}" viewBox="0 0 40 40"><path d="M20 0 L25 15 L40 20 L25 25 L20 40 L15 25 L0 20 L15 15Z" fill="{col}"/></svg>' for x, y, s in pts)

# ---------------------------------------------------------------- 장면 (위쪽 1200x700 영역)
def scene_svg(name, p, t):
    acc, deep = p['acc'], p['deep']
    if name == 'restaurant':
        return (person(230, 110, 320, skin=SKIN[1], hair='#2A1A10', style='bob', shirt='#2D5BFF', face='talk', hand='phone')
                + table_scene(60, 380, 640) + clock(600, 120, 150) + phone_call(820, 60, 230, 'Bella Table', 'calling…', acc)
                + sparkles([(120, 110, 50), (1060, 560, 40)], '#fff'))
    if name == 'directions':
        return (map_card(560, 110, 520, acc) + person(140, 150, 340, skin=SKIN[0], style='spiky', hair='#2A1A10', shirt=acc, face='wow', hand='wave')
                + sparkles([(480, 120, 50)], '#fff'))
    if name == 'shadowing':
        return (headphones(140, 110, 300, acc) + wave(480, 210, 600, 220, '#fff', 20, 5)
                + person(700, 330, 260, skin=SKIN[2], style='curly', hair='#3B2416', shirt=INK, face='talk')
                + icon('speak', 560, 120, 120, acc))
    if name == 'dictation':
        return (notebook(120, 110, 620, 400, [('I\'m ____ pick', 0), ('up a coffee.', 250), ('→ going to', 220)], acc)
                + headphones(800, 100, 260, acc) + person(830, 340, 250, skin=SKIN[0], style='long', hair='#5A2E12', shirt='#2D5BFF', face='think'))
    if name == 'review':
        return (notebook(110, 100, 600, 420, [('Today\'s note', 280), ('✓ I usually…', 0), ('✓ on my way', 0)], acc)
                + clock(780, 90, 200, 10, 10) + icon('pen', 760, 330, 160, acc)
                + person(900, 330, 230, skin=SKIN[1], style='bun', hair='#2A1A10', shirt='#fff', face='smile'))
    if name == 'opinion':
        return (bubble(560, 110, 460, 120, 'I think…', '#fff', 'left', 64, rot=-4)
                + bubble(640, 290, 470, 120, 'because…', acc, 'left', 64, rot=3)
                + person(130, 130, 380, skin=SKIN[3], style='short', hair='#16110C', shirt=acc, face='talk', glasses=True)
                + icon('bulb', 470, 60, 120, '#FFE04A'))
    if name == 'weekend':
        return (calendar(560, 90, 250, acc, 'SAT', '29') + calendar(820, 160, 230, '#fff', 'SUN', '30')
                + person(150, 140, 360, skin=SKIN[0], style='bob', hair='#3B2416', shirt=acc, face='smile', hand='wave')
                + sparkles([(560, 400, 60), (1060, 90, 44)], '#fff'))
    if name == 'wordblank':
        return (bubble(560, 110, 520, 160, '?!  It\'s a thing…', '#fff', 'left', 60, rot=-3)
                + person(150, 140, 360, skin=SKIN[2], style='short', hair='#2A1A10', shirt=acc, face='think', hand='chin')
                + icon('bulb', 900, 330, 170, '#FFE04A'))
    raise SystemExit('알 수 없는 scene: ' + name)

# ---------------------------------------------------------------- 레이아웃
def page(inner, p):
    dot = p['dot']
    return f'''<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="{FONTS}/black-han-sans/font.css"><link rel="stylesheet" href="{FONTS}/jua/font.css">
<style>
@font-face{{font-family:Pretendard;font-weight:900;src:url({FONTS}/Pretendard-Black.woff2)}}
@font-face{{font-family:Pretendard;font-weight:800;src:url({FONTS}/Pretendard-ExtraBold.woff2)}}
@font-face{{font-family:Pretendard;font-weight:700;src:url({FONTS}/Pretendard-Bold.woff2)}}
@font-face{{font-family:Pretendard;font-weight:600;src:url({FONTS}/Pretendard-SemiBold.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1200px;height:1200px;overflow:hidden;background:{p['bg']};
 background-image:radial-gradient({dot} 5px,transparent 6px);background-size:44px 44px;font-family:Pretendard}}
.abs{{position:absolute}}
.title{{font-family:'Black Han Sans';line-height:1.08;color:{INK};white-space:nowrap}}
</style></head><body>{inner}
<script>
document.fonts.ready.then(()=>{{
 document.querySelectorAll('[data-fit]').forEach(el=>{{let s=parseFloat(getComputedStyle(el).fontSize);
  const max=+el.dataset.fit; while(el.scrollWidth>max && s>20){{s-=2;el.style.fontSize=s+'px'}} }});
 document.querySelectorAll('.fit .t').forEach(el=>{{let s=parseFloat(getComputedStyle(el).fontSize);
  while(el.scrollWidth>el.clientWidth && s>18){{s-=2;el.style.fontSize=s+'px'}} }});
 document.body.dataset.ready=1;}});
</script></body></html>'''

def chrome(cat, p):
    label, bg, fg = CAT[cat]
    brand_col = '#fff' if p['dark'] else INK
    return (f'<div class="abs" style="left:64px;top:56px;padding:12px 26px;border-radius:40px;background:{bg};border:5px solid {INK};'
            f'font-weight:900;font-size:34px;color:{fg};box-shadow:6px 6px 0 {INK}">{label}</div>'
            '')

def title_panel(t, p, top=740):
    hook = t.get('hook')
    kick = t.get('kicker', '')
    l1, l2 = t['title']
    out = (f'<div class="abs" style="left:48px;right:48px;top:{top}px;bottom:48px;background:#fff;border:6px solid {INK};border-radius:40px;box-shadow:12px 12px 0 {INK}"></div>'
           f'<div class="abs" style="left:96px;top:{top+44}px;font-weight:900;font-size:40px;color:{p["deep"] if not p["dark"] else p["bg"]}">{esc(kick)}</div>'
           f'<div class="abs" style="right:96px;top:{top+50}px;font-weight:800;font-size:30px;color:#8A8A96">아인잉글리쉬</div>'
           f'<div class="abs title" data-fit="1000" style="left:94px;top:{top+100}px;font-size:118px">{esc(l1)}</div>'
           f'<div class="abs title" data-fit="1000" style="left:94px;top:{top+228}px;font-size:118px">'
           f'<span style="background:linear-gradient(transparent 58%, {p["acc"] if p["acc"] not in ("#1F2B7A","#2A2A80","#2D2DA8") else "#FFE04A"} 58%)">{esc(l2)}</span></div>')
    if hook:
        out += bubble(620, top - 110, 520, 104, hook, p['acc'] if p['acc'] not in ('#1F2B7A', '#2A2A80', '#2D2DA8') else '#FFE04A',
                      tail='right', size=40, weight=800, rot=-3)
    return out

def layout_scene(t, p, cat):
    return page(f'<svg class="abs" style="left:0;top:0" width="1200" height="760" overflow="visible">{scene_svg(t["scene"], p, t)}</svg>'
                + chrome(cat, p) + title_panel(t, p), p)

def layout_versus(t, p, cat):
    words = t['words']; n = len(words); gap = 28; w = (1200 - 2 * 64 - gap * (n - 1)) / n
    tiles = ''
    tile_cols = ['#FFFFFF', p['acc'] if p['acc'] not in ('#1F2B7A', '#2A2A80', '#2D2DA8') else '#FFE04A', '#FFFFFF', '#FFE04A']
    for i, wd in enumerate(words):
        x = 64 + i * (w + gap); rot = (-3, 2, -2, 3)[i % 4]; fill = tile_cols[i % len(tile_cols)]
        tiles += (f'<div class="abs" style="left:{x:.0f}px;top:200px;width:{w:.0f}px;height:440px;transform:rotate({rot}deg);'
                  f'background:{fill};border:6px solid {INK};border-radius:36px;box-shadow:12px 12px 0 {INK};text-align:center">'
                  f'<svg width="150" height="150" style="display:block;margin:36px auto 0">{icon(wd.get("icon","eye"),0,0,150,p["bg"] if fill!="#FFFFFF" else (p["acc"] if p["acc"] not in ("#1F2B7A","#2A2A80","#2D2DA8") else "#FF5B4F"))}</svg>'
                  f'<div data-fit="{w-40:.0f}" style="display:inline-block;font-family:Pretendard;font-weight:900;font-size:{100 if n<=3 else 80}px;line-height:1;margin-top:20px;color:{INK};white-space:nowrap">{esc(wd["w"])}</div>'
                  f'<div style="font-weight:800;font-size:40px;margin-top:22px;color:#4A4A55">{esc(wd["ko"])}</div></div>')
    peek = person(980, 560, 190, skin=SKIN[1], style='short', hair='#2A1A10', shirt=INK, face=t.get('face', 'wow'))
    return page(chrome(cat, p) + tiles + title_panel(t, p, 760)
                + f'<svg class="abs" style="left:0;top:0;pointer-events:none" width="1200" height="1200" overflow="visible">{peek}</svg>', p)

def layout_call(t, p, cat):
    pp = t.get('people', {})
    win = (f'<div class="abs" style="left:64px;top:150px;width:1072px;height:520px;background:#16161D;border-radius:36px;box-shadow:12px 12px 0 rgba(0,0,0,.25)"></div>'
           f'<div class="abs" style="left:92px;top:178px;width:500px;height:420px;background:#CFE0FF;border-radius:24px;overflow:hidden">'
           f'<svg width="500" height="420">{person(80, 60, 340, skin=SKIN[0], style="spiky", hair="#2A1A10", shirt="#2D5BFF", face=pp.get("student","think"), headset=True)}</svg></div>'
           f'<div class="abs" style="left:608px;top:178px;width:500px;height:420px;background:#FFD9D2;border-radius:24px;overflow:hidden">'
           f'<svg width="500" height="420">{person(80, 60, 340, skin=SKIN[1], style="long", hair="#5A2E12", shirt="#FF5B4F", face="smile", headset=True)}</svg></div>'
           '<div class="abs" style="left:92px;top:612px;display:flex;gap:18px">'
           + ''.join(f'<div style="width:44px;height:44px;border-radius:22px;background:{c}"></div>' for c in ('#3A3A46', '#3A3A46', '#FF4B3A')) + '</div>'
           '<div class="abs" style="left:110px;top:200px;padding:6px 16px;border-radius:12px;background:rgba(0,0,0,.55);color:#fff;font-weight:800;font-size:26px">Me</div>'
           '<div class="abs" style="left:626px;top:200px;padding:6px 16px;border-radius:12px;background:rgba(0,0,0,.55);color:#fff;font-weight:800;font-size:26px">Teacher</div>')
    b = pp.get('bubble')
    bub = bubble(300, 90, 620, 110, b, '#fff', 'left', 44, weight=800, rot=-2) if b else ''
    t2 = dict(t); t2.pop('hook', None)
    return page(chrome(cat, p) + win + bub + title_panel(t2, p), p)

LAYOUT = {'scene': layout_scene, 'versus': layout_versus, 'call': layout_call}

def render(posts, outdir):
    from playwright.sync_api import sync_playwright
    os.makedirs(outdir, exist_ok=True)
    with sync_playwright() as pw:
        br = pw.chromium.launch(); pg = br.new_page(viewport={'width': 1200, 'height': 1200}, device_scale_factor=1)
        for post in posts:
            t = post['thumbnail']; p = PALETTES[t['palette']]
            htm = LAYOUT[t.get('layout', 'scene')](t, p, post['category'])
            hp = os.path.join(outdir, f"{post['prefix']}_thumbnail.html")
            open(hp, 'w').write(htm)
            pg.goto('file://' + os.path.abspath(hp)); pg.wait_for_selector('body[data-ready]', timeout=15000)
            pg.wait_for_timeout(200)
            fn = os.path.join(outdir, f"{post['prefix']}_thumbnail_1200.png"); pg.screenshot(path=fn); os.remove(hp)
            print(fn, (1200, 1200))
        br.close()

if __name__ == '__main__':
    spec = json.load(open(sys.argv[1])); render([p for p in spec['posts'] if 'title' in p['thumbnail']], sys.argv[2])
