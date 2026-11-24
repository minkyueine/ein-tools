#!/usr/bin/env python3
"""아인잉글리쉬 캐릭터(학생·선생님·마스코트) SVG/PNG 생성기 — 깔끔한 선 버전.
사용법: python3 tools/chars.py ch/
선은 한 번만, 부드러운 갈색으로. 색은 선 안에 맞춘다."""
import sys, os
INK='#4A3A34'; SKIN='#FFE8D6'; CORAL='#F0806F'; BLUE='#9DBFF5'; YEL='#FFD966'; HAIR_S='#5A4640'; HAIR_T='#9A6A4A'; PINK='#FFA8A0'; W='#FFFFFF'
ST=f'stroke="{INK}" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"'

def face(mood,cx=100,cy=100):
    o=f'<ellipse cx="{cx-30}" cy="{cy+13}" rx="9" ry="6" fill="{PINK}" opacity=".6"/><ellipse cx="{cx+30}" cy="{cy+13}" rx="9" ry="6" fill="{PINK}" opacity=".6"/>'
    eye=lambda x:f'<ellipse cx="{x}" cy="{cy}" rx="4.6" ry="5.8" fill="{INK}"/><circle cx="{x+1.6}" cy="{cy-2}" r="1.6" fill="#fff"/>'
    arc=lambda x:f'<path d="M{x-7},{cy+2} Q{x},{cy-7} {x+7},{cy+2}" fill="none" {ST}/>'
    if mood=='smile': o+=eye(cx-17)+eye(cx+17)+f'<path d="M{cx-8},{cy+14} Q{cx},{cy+22} {cx+8},{cy+14}" fill="none" {ST}/>'
    elif mood=='happy': o+=arc(cx-17)+arc(cx+17)+f'<path d="M{cx-9},{cy+13} Q{cx},{cy+27} {cx+9},{cy+13} Z" fill="#E0604F" {ST} stroke-width="2.6"/>'
    elif mood=='worry':
        o+=eye(cx-17)+eye(cx+17)
        o+=f'<path d="M{cx-26},{cy-11} L{cx-12},{cy-15}" fill="none" {ST} stroke-width="2.8"/><path d="M{cx+26},{cy-11} L{cx+12},{cy-15}" fill="none" {ST} stroke-width="2.8"/>'
        o+=f'<path d="M{cx-7},{cy+18} Q{cx},{cy+12} {cx+7},{cy+18}" fill="none" {ST}/>'
        o+=f'<path d="M{cx+50},{cy-30} q-7,11 0,16 q7,-5 0,-16Z" fill="#B5D4FA" {ST} stroke-width="2.4"/>'
    elif mood=='open': o+=eye(cx-17)+eye(cx+17)+f'<ellipse cx="{cx}" cy="{cy+18}" rx="6" ry="7" fill="#E0604F" {ST} stroke-width="2.6"/>'
    return o

def P(d,fill): return f'<path d="{d}" fill="{fill}" {ST}/>'
def C(cx,cy,r,fill): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" {ST}/>'

def student(mood='smile',arms=None):
    o=''
    if arms=='up':
        for sx in(-1,1):
            o+=P(f'M{100+sx*40},186 Q{100+sx*72},170 {100+sx*70},122 L{100+sx*86},124 Q{100+sx*92},186 {100+sx*58},214 Z',BLUE)+C(100+sx*79,110,12,SKIN)
    o+=P('M42,240 Q42,164 100,164 Q158,164 158,240 Z',BLUE)
    o+=f'<path d="M87,140 L87,166 Q100,178 113,166 L113,140" fill="{SKIN}" {ST}/>'
    o+=C(100,100,54,SKIN)
    o+=P('M46,98 Q42,42 100,40 Q158,42 154,98 Q150,72 122,66 Q112,80 78,78 Q56,80 46,98 Z',HAIR_S)
    o+=f'<path d="M100,40 Q98,24 110,22" fill="none" {ST}/>'
    o+=face(mood,100,104)
    if arms=='book':
        o+=P('M56,204 Q78,196 100,206 Q122,196 144,204 L144,246 Q122,238 100,248 Q78,238 56,246 Z',W)+f'<path d="M100,206 L100,248" fill="none" {ST}/>'
        o+=C(54,226,10,SKIN)+C(146,226,10,SKIN)
    return o

def teacher(mood='smile',arms=None):
    o=C(100,30,15,HAIR_T)
    o+=P('M44,104 Q40,42 100,42 Q160,42 156,104 Q160,156 148,176 L52,176 Q40,156 44,104 Z',HAIR_T)
    o+=P('M42,240 Q42,166 100,166 Q158,166 158,240 Z',CORAL)
    o+=f'<path d="M87,142 L87,168 Q100,180 113,168 L113,142" fill="{SKIN}" {ST}/>'
    o+=C(100,104,50,SKIN)
    o+=P('M52,100 Q54,54 100,54 Q146,54 148,100 Q136,74 104,72 Q92,86 52,100 Z',HAIR_T)
    o+=f'<path d="M48,92 Q50,36 100,36 Q150,36 152,92" fill="none" {ST}/>'
    o+=f'<rect x="38" y="90" width="18" height="32" rx="9" fill="{YEL}" {ST}/><rect x="144" y="90" width="18" height="32" rx="9" fill="{YEL}" {ST}/>'
    o+=f'<path d="M46,122 Q48,140 74,138" fill="none" {ST} stroke-width="2.8"/><circle cx="77" cy="138" r="4" fill="{INK}"/>'
    o+=face(mood,100,106)
    if arms=='wave':
        o+=P('M148,206 Q170,196 174,164 L188,168 Q188,214 160,230 Z',CORAL)+C(182,152,13,SKIN)
        o+=f'<path d="M204,134 q7,6 5,15 M214,126 q10,9 8,22" fill="none" {ST} stroke-width="2.6"/>'
    return o

def mascot(mood='smile',arms=None):
    o=f'<ellipse cx="84" cy="238" rx="13" ry="6.5" fill="{INK}"/><ellipse cx="116" cy="238" rx="13" ry="6.5" fill="{INK}"/>'
    if arms=='up': o+=P('M66,170 Q40,160 36,134 L48,130 Q54,150 72,156 Z',W)+P('M134,170 Q160,160 164,134 L152,130 Q146,150 128,156 Z',W)
    elif arms=='point': o+=P('M134,178 Q162,174 182,156 L190,166 Q170,190 138,192 Z',W)
    o+=f'<ellipse cx="100" cy="190" rx="40" ry="48" fill="{W}" {ST}/>'
    o+=f'<path d="M48,92 Q50,34 100,34 Q150,34 152,92" fill="none" stroke="{INK}" stroke-width="15" stroke-linecap="round"/><path d="M48,92 Q50,34 100,34 Q150,34 152,92" fill="none" stroke="{CORAL}" stroke-width="8.5" stroke-linecap="round"/>'
    o+=C(100,102,50,W)
    o+=f'<rect x="36" y="82" width="22" height="42" rx="11" fill="{CORAL}" {ST}/><rect x="142" y="82" width="22" height="42" rx="11" fill="{CORAL}" {ST}/>'
    o+=face(mood,100,104)
    if arms=='paper':
        o+=f'<rect x="64" y="166" width="72" height="58" rx="7" fill="{W}" {ST}/><rect x="74" y="177" width="32" height="7" rx="3.5" fill="{CORAL}"/><rect x="74" y="191" width="52" height="5" rx="2.5" fill="#E2DCD6"/><rect x="74" y="202" width="42" height="5" rx="2.5" fill="#E2DCD6"/><rect x="74" y="213" width="48" height="5" rx="2.5" fill="{YEL}"/>'
        o+=C(62,198,9,W)+C(138,198,9,W)
    return o

def svg(body,vb='-10 -4 250 262'): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}">{body}</svg>'
SET={'student-smile':student('smile'),'student-worry':student('worry'),'student-cheer':student('happy','up'),'student-open':student('open'),'student-book':student('happy','book'),
     'teacher-smile':teacher('happy'),'teacher-wave':teacher('happy','wave'),'teacher-soft':teacher('smile'),
     'mascot-smile':mascot('happy'),'mascot-point':mascot('happy','point'),'mascot-paper':mascot('smile','paper')}
if __name__=='__main__':
    out=sys.argv[1]; os.makedirs(out,exist_ok=True)
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        b=pw.chromium.launch(executable_path='/usr/bin/google-chrome'); pg=b.new_page(viewport={'width':500,'height':524})
        for k,v in SET.items():
            s=svg(v); open(f'{out}/{k}.svg','w').write(s)
            pg.set_content(f'<body style="margin:0;background:transparent">{s.replace("<svg ","<svg width=500 height=524 ")}</body>'); pg.screenshot(path=f'{out}/{k}.png',omit_background=True)
        b.close()

# ---- 거북이 (인스타 프로필의 직장인 거북이 원본을 보고 같은 그림체로) ----
GREEN='#A3CC52'; SHELL='#8E5A2B'; NAVY='#2F4270'; BELLY='#D9AE6C'
def turtle(mood='tired',arms='coffee'):
    # 원본 비율: 머리와 몸통이 거의 같은 폭, 셔츠 입은 몸통이 머리를 받친다
    o=f'<path d="M104,136 Q144,126 160,150 Q176,180 168,214 Q160,240 130,238 L104,232 Z" fill="{SHELL}" {ST}/>'
    o+=f'<path d="M156,160 L168,164 M160,188 L172,192 M156,214 L166,220" fill="none" stroke="{INK}" stroke-width="2.4" stroke-linecap="round"/>'
    o+=f'<rect x="70" y="220" width="24" height="32" rx="10" fill="{GREEN}" {ST}/><rect x="108" y="220" width="24" height="32" rx="10" fill="{GREEN}" {ST}/>'
    o+=P('M54,222 Q100,248 148,222 L146,206 L56,206 Z',BELLY)
    if arms=='up': o+=P('M62,172 Q34,160 30,128 L46,124 Q50,150 72,156 Z',GREEN)+P('M140,172 Q168,160 172,128 L156,124 Q152,150 130,156 Z',GREEN)
    elif arms=='point': o+=P('M138,170 Q168,166 192,146 L200,158 Q176,186 142,188 Z',GREEN)
    o+=P('M54,214 Q46,134 100,130 Q156,134 148,214 Q100,226 54,214 Z',W)
    o+=P('M84,122 L84,150 L100,166 L116,150 L116,122 Z',GREEN)
    o+=f'<path d="M76,146 L100,168 L124,146" fill="none" {ST} stroke-width="2.8"/>'
    o+=f'<path d="M100,168 L92,179 L100,210 L108,179 Z" fill="{NAVY}" {ST} stroke-width="2.6"/>'
    if arms=='coffee':
        o+=P('M134,160 Q152,164 152,200 Q150,220 138,218 Q128,214 130,190 Z',GREEN)
        o+=P('M64,166 Q44,174 30,184 L36,200 Q54,192 72,186 Z',GREEN)
        o+=f'<path d="M0,180 L32,180 Q32,208 16,208 Q0,208 0,180 Z" fill="{W}" {ST}/><ellipse cx="16" cy="180" rx="16" ry="4.5" fill="#6B4630" {ST} stroke-width="2.4"/><circle cx="35" cy="191" r="6.5" fill="{GREEN}" {ST} stroke-width="2.6"/>'
        o+=f'<path d="M9,168 q-4,-5 0,-10 q4,-5 0,-10 M20,168 q-4,-5 0,-10 q4,-5 0,-10" fill="none" stroke="#B9B2AB" stroke-width="2.6" stroke-linecap="round"/>'
    if arms=='point': o+=P('M62,166 Q46,182 52,204 L66,200 Q64,186 74,176 Z',GREEN)
    o+='<g transform="translate(4,-2) scale(.96)">'
    o+=f'<path d="M36,98 Q34,38 100,38 Q166,38 164,98 Q162,148 100,148 Q38,148 36,98 Z" fill="{GREEN}" {ST} stroke-width="3.6"/>'
    cy=94
    o+=f'<ellipse cx="52" cy="{cy+24}" rx="10" ry="6.5" fill="{PINK}" opacity=".7"/><ellipse cx="148" cy="{cy+24}" rx="10" ry="6.5" fill="{PINK}" opacity=".7"/>'
    for x,rot in((74,-7),(126,7)):
        o+=f'<ellipse cx="{x}" cy="{cy+13}" rx="13" ry="7" fill="#8B6A96" opacity=".22"/>'
        o+=f'<circle cx="{x}" cy="{cy}" r="17" fill="{W}" {ST} stroke-width="3"/><circle cx="{x}" cy="{cy+4}" r="8.5" fill="{INK}"/><circle cx="{x+3}" cy="{cy+1}" r="2.8" fill="#fff"/>'
        o+=f'<path d="M{x-15.9},{cy-6} A17,17 0 0 1 {x+15.9},{cy-6} Z" fill="#8DB843" {ST} stroke-width="3" transform="rotate({rot} {x} {cy})"/>'
    o+=f'<path d="M60,68 Q69,66 76,60" fill="none" {ST} stroke-width="2.8"/><path d="M124,60 Q131,66 140,68" fill="none" {ST} stroke-width="2.8"/>'
    if mood=='tired': o+=f'<path d="M92,130 Q100,123 108,130" fill="none" {ST} stroke-width="3.6"/>'
    elif mood=='calm': o+=f'<path d="M91,125 Q100,134 109,125" fill="none" {ST} stroke-width="3.6"/>'
    else: o+=f'<path d="M90,123 Q100,138 110,123 Z" fill="#E0604F" {ST} stroke-width="3"/>'
    o+=f'<circle cx="96" cy="114" r="1.8" fill="{INK}"/><circle cx="104" cy="114" r="1.8" fill="{INK}"/></g>'
    if arms=='paper':
        o+=f'<rect x="60" y="166" width="80" height="60" rx="7" fill="{W}" {ST}/><rect x="70" y="177" width="36" height="7" rx="3.5" fill="{CORAL}"/><rect x="70" y="191" width="60" height="5" rx="2.5" fill="#E2DCD6"/><rect x="70" y="202" width="46" height="5" rx="2.5" fill="#E2DCD6"/><rect x="70" y="213" width="52" height="5" rx="2.5" fill="{YEL}"/>'
        o+=C(58,198,9.5,GREEN)+C(142,198,9.5,GREEN)
    return o
TURTLE={'turtle-coffee':turtle('tired','coffee'),'turtle-point':turtle('calm','point'),'turtle-paper':turtle('calm','paper'),'turtle-cheer':turtle('open','up')}
