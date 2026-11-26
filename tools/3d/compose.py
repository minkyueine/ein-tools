"""3D 캐릭터로 이벤트 배너(글마다 다른 구성)와 본문 장면 그림을 만든다.
사용법: python3 compose.py /home/claude/ein-tools/event"""
import sys, os
from playwright.sync_api import sync_playwright
root = sys.argv[1]
import os
HERE=os.path.dirname(os.path.abspath(__file__))
C='file://'+HERE+'/cut/'
PR='file://'+HERE+'/props/c_'
F = "'Noto Sans CJK KR',sans-serif"
INK = '#2A211D'


def im(name, h, x=None, y=None, extra='', bottom=None):
    src = (PR + name) if name.startswith('prop-') else (C + name)
    if bottom is not None: pos = f'position:absolute;left:{x}px;bottom:{bottom}px;'
    elif x is not None: pos = f'position:absolute;left:{x}px;top:{y}px;'
    else: pos = ''
    return f'<img src="{src}.png" style="{pos}height:{h}px;filter:drop-shadow(0 10px 14px rgba(0,0,0,.14));{extra}">'


def big(text, size, color='#fff', stroke=INK, sw=6):
    return f'<div style="font:900 {size}px/1.02 {F};color:{color};letter-spacing:-.03em;-webkit-text-stroke:{sw}px {stroke};paint-order:stroke fill;white-space:nowrap">{text}</div>'


def pill(text, bg='#FFD966', color=INK, size=36):
    return f'<div style="display:inline-block;background:{bg};border:4px solid {INK};border-radius:40px;padding:8px 28px;font:800 {size}px/1.2 {F};color:{color}">{text}</div>'


def dots(colors):
    pts = [(80, 120, 18), (990, 90, 14), (60, 600, 12), (1010, 560, 16), (520, 40, 10), (930, 960, 12)]
    return ''.join(f'<div style="position:absolute;left:{x}px;top:{y}px;width:{s}px;height:{s}px;border-radius:50%;background:{colors[i % len(colors)]};opacity:.9"></div>' for i, (x, y, s) in enumerate(pts))


def shadow(x, y, w):
    return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{w*.16:.0f}px;border-radius:50%;background:rgba(0,0,0,.12);filter:blur(6px)"></div>'


B = {}
# 206 무이자: 파란 배경, 왼쪽 글 + 오른쪽 위 카드 + 아래 학생·거북이
B['206'] = f"""<div style="position:absolute;inset:0;background:linear-gradient(160deg,#7DB0F7,#4F86E6);overflow:hidden">{dots(['#fff', '#FFD966'])}
<div style="position:absolute;left:84px;top:96px">{pill('카드 결제 부담 DOWN')}
<div style="margin-top:34px;font:800 64px/1.2 {F};color:#fff">5만원 이상이면</div>
<div style="margin-top:6px">{big('무이자', 190)}</div><div style="margin-top:4px">{big('할부', 190, '#FFD966')}</div></div>
{im('prop-card', 330, 640, 110, 'transform:rotate(-6deg)')}
{im('student-cheer', 330, 230, None, bottom=0)}{im('turtle-wave', 520, 600, None, bottom=0)}
</div>"""
# 207 지인 추천: 초록 배경, 가운데 큰 5%+5%, 아래 학생·거북이 나란히 + 동전
B['207'] = f"""<div style="position:absolute;inset:0;background:radial-gradient(circle at 50% 30%,#7CD6A0,#3FAE72);overflow:hidden">{dots(['#fff', '#FFD966'])}
<div style="position:absolute;left:0;right:0;top:80px;text-align:center">{pill('지인 추천 이벤트', '#fff')}
<div style="margin-top:28px;font:800 62px/1.2 {F};color:#fff">추천하면 둘 다</div>
<div style="margin-top:10px;display:flex;justify-content:center;align-items:center;gap:18px">{big('5%', 200)}<span style="font:900 100px/1 {F};color:#FFD966;-webkit-text-stroke:5px {INK};paint-order:stroke fill">+</span>{big('5%', 200)}</div></div>
{im('prop-coin', 150, 60, 600, 'transform:rotate(-14deg)')}{im('prop-coin', 120, 905, 560, 'transform:rotate(16deg)')}
{im('student-cheer', 360, 150, None, bottom=0)}{im('turtle-cheer', 470, 560, None, bottom=-10)}
</div>"""
# 205 체험 후기: 노란 배경, 왼쪽 큰 거북이(쓰는 중) + 말풍선, 오른쪽 글
B['205'] = f"""<div style="position:absolute;inset:0;background:#FFD45E;overflow:hidden">{dots(['#fff', '#EC6856'])}
<div style="position:absolute;left:0;top:0;width:540px;height:1080px;background:#FFC23D;border-radius:0 300px 300px 0"></div>
{im('bubble', 200, 300, 170, 'transform:rotate(-6deg)')}
{im('turtle-write', 520, 30, None, bottom=60)}
<div style="position:absolute;left:580px;top:250px">{pill('신규 회원 선물', '#fff', size=34)}
<div style="margin-top:28px;font:800 56px/1.25 {F};color:{INK}">무료체험<br>후기 쓰면</div>
<div style="margin-top:14px;display:flex;align-items:flex-end;gap:6px">{big('3,000', 150, '#EC6856')}{big('원', 90, '#EC6856', sw=5)}</div>
<div style="margin-top:18px;font:800 52px/1.2 {F};color:{INK}">바로 적립!</div></div>
</div>"""
# 203 네이버 재수강: 크림 배경, 위 글 + 쇼핑백·동전 + 오른쪽 거북이
B['203'] = f"""<div style="position:absolute;inset:0;background:#FFF4E2;overflow:hidden">{dots(['#2DB46B', '#FFD966', '#EC6856'])}
<div style="position:absolute;left:0;right:0;top:80px;text-align:center">{pill('재수강 회원 전용', '#2DB46B', '#fff')}
<div style="margin-top:26px;font:800 60px/1.2 {F};color:{INK}">네이버 스토어에서</div>
<div style="margin-top:10px;display:flex;justify-content:center;align-items:center;gap:20px">{big('3만', 170, '#FFD45E')}<span style="font:900 110px/1 {F};color:#2DB46B">→</span>{big('4만', 170, '#EC6856')}</div></div>
{im('prop-bag', 360, 130, 600, 'transform:rotate(-6deg)')}{im('prop-coins', 190, 360, 840)}
{im('turtle-paper', 480, 620, None, bottom=0)}
</div>"""
# 199 수강후기: 보라 배경, 위 글 + 별, 아래 선생님·거북이(책)
B['199'] = f"""<div style="position:absolute;inset:0;background:linear-gradient(170deg,#9C8CF5,#6F5DE0);overflow:hidden">{dots(['#fff', '#FFD966'])}
{im('prop-star', 210, 820, 70, 'transform:rotate(12deg)')}{im('prop-star', 110, 60, 560, 'transform:rotate(-14deg)')}
<div style="position:absolute;left:84px;top:110px">{pill('수강후기 이벤트')}
<div style="margin-top:30px;font:800 62px/1.2 {F};color:#fff">베스트 후기는</div>
<div style="margin-top:8px">{big('2만원', 200, '#FFD966')}</div></div>
{im('teacher-wave', 470, 220, None, bottom=0)}{im('turtle-book', 400, 520, None, bottom=0)}
</div>"""


def bub(text, bg='#fff', fs=40):
    return f'<div style="background:{bg};border:4px solid {INK};border-radius:28px;padding:{fs*.42:.0f}px {fs*.8:.0f}px;font:700 {fs}px/1.25 {F};color:{INK};white-space:nowrap">{text}</div>'


def duo(lt, lc, lh, rt, rc, rh, bg='#FFF6D6'):
    return f"""<div style="position:absolute;inset:4px;background:{bg};border:4px solid {INK};border-radius:44px;overflow:hidden">
<div style="position:absolute;left:36px;top:36px">{bub(lt)}</div><div style="position:absolute;right:36px;top:36px">{bub(rt, '#FFD966')}</div>
{im(lc, lh, 110, None, bottom=0)}{im(rc, rh, 500, None, bottom=0)}</div>"""


S = {
    '206': duo('한 번에 결제하기<br>부담돼요', 'student-worry', 300, '카드 무이자 할부로<br>나눠 내세요!', 'turtle-wave', 330, '#E3EDFF'),
    '207': duo('친구한테 아인<br>추천했어요!', 'student-cheer', 250, '두 분 다 5%씩<br>적립해 드려요!', 'turtle-cheer', 330, '#E6F6EE'),
    '205': duo('체험 후기<br>남겼어요!', 'student-cheer', 250, '3,000원<br>적립해 드릴게요!', 'turtle-paper', 330, '#FFF6D6'),
    '203': duo('다음 달도<br>계속 들을래요!', 'student-cheer', 250, '네이버에서 3만원 내면<br>4만원 적립!', 'turtle-clip', 320, '#FFF4E2'),
    '199': duo('선생님 덕분에<br>말이 늘었어요!', 'student-cheer', 250, '그 이야기를<br>후기로 남겨 주세요!', 'teacher-wave', 340, '#EEEAFF'),
}

with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome')
    for pid in B:
        for name, (w, h, html) in {'banner.png': (1080, 1080, B[pid]), 'scene-hello.png': (900, 540, S[pid])}.items():
            path = f'/tmp/compose_{pid}_{name}.html'
            open(path, 'w').write(f'<html><body style="margin:0;width:{w}px;height:{h}px;position:relative;overflow:hidden;background:transparent">{html}</body></html>')
            pg = b.new_page(viewport={'width': w, 'height': h}); pg.goto('file://' + path); pg.wait_for_timeout(300)
            pg.screenshot(path=f'{root}/{pid}/{name}', omit_background=True); pg.close()
    b.close()
print('ok')
