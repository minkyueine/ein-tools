"""3D 출연진(학생·선생님·성인 수강생)으로 이벤트 글 배너와 본문 그림을 만든다. 거북이는 쓰지 않는다.
사용법: python3 tools/3d/compose_cast.py event
캐릭터 컷: tools/3d/cast/<인물>-<포즈>.png  (README 참고)
"""
import sys, os
from playwright.sync_api import sync_playwright

root = sys.argv[1]
HERE = os.path.dirname(os.path.abspath(__file__))
CAST = 'file://' + HERE + '/cast/'
PR = 'file://' + HERE + '/props/c_'
F = "'Noto Sans CJK KR',sans-serif"
INK = '#2A211D'


def ch(name, h, x, bottom=28, flip=False, extra=''):
    """전신 캐릭터. 발이 잘리지 않게 바닥에서 띄우고 그림자를 깐다."""
    t = 'transform:scaleX(-1);' if flip else ''
    return (f'<div style="position:absolute;left:{x}px;bottom:{bottom}px;height:{h}px">'
            f'<div style="position:absolute;left:8%;right:8%;bottom:-10px;height:{h*.07:.0f}px;border-radius:50%;background:rgba(0,0,0,.16);filter:blur(7px)"></div>'
            f'<img class="cc" src="{CAST}{name}.png" style="position:relative;height:{h}px;{t}{extra}"></div>')


def prop(name, h, x, y, extra=''):
    return f'<img src="{PR}{name}.png" style="position:absolute;left:{x}px;top:{y}px;height:{h}px;filter:drop-shadow(0 10px 14px rgba(0,0,0,.14));{extra}">'


def big(text, size, color='#fff', stroke=INK, sw=6):
    return f'<div style="font:900 {size}px/1.02 {F};color:{color};letter-spacing:-.03em;-webkit-text-stroke:{sw}px {stroke};paint-order:stroke fill;white-space:nowrap">{text}</div>'


def pill(text, bg='#FFD966', color=INK, size=36):
    return f'<div style="display:inline-block;background:{bg};border:4px solid {INK};border-radius:40px;padding:8px 28px;font:800 {size}px/1.2 {F};color:{color}">{text}</div>'


def line(text, size, color=INK):
    return f'<div style="font:800 {size}px/1.22 {F};color:{color};letter-spacing:-.02em">{text}</div>'


def dots(colors):
    pts = [(80, 120, 18), (990, 90, 14), (60, 600, 12), (1010, 560, 16), (520, 40, 10), (930, 960, 12)]
    return ''.join(f'<div style="position:absolute;left:{x}px;top:{y}px;width:{s}px;height:{s}px;border-radius:50%;background:{colors[i % len(colors)]};opacity:.9"></div>' for i, (x, y, s) in enumerate(pts))


def floor(color, top=820):
    return f'<div style="position:absolute;left:-10%;right:-10%;top:{top}px;bottom:-200px;background:{color};border-radius:50% 50% 0 0/80px 80px 0 0"></div>'


# ── 배너 1080×1080: 글마다 색·구도가 다르다 ─────────────────────────
B = {}
# 130 월 이벤트: 코랄 · 셋이 함께
B['130'] = f"""<div style="position:absolute;inset:0;background:#EC6856;overflow:hidden">{dots(['#fff', '#FFD966'])}{floor('#F6907F', 800)}
<div style="position:absolute;left:0;right:0;top:66px;text-align:center">{pill('이번 달 이벤트')}
<div style="margin-top:22px">{line('아인잉글리쉬', 58, '#fff')}</div><div style="margin-top:2px">{big('혜택 7가지', 156, '#FFD966')}</div>
<div style="margin-top:18px;display:flex;gap:12px;justify-content:center">{''.join(pill(t, '#fff', INK, 28) for t in ['신규', '재수강', '친구 추천', '누구나'])}</div></div>
{ch('student-cheer', 500, 40)}{ch('teacher-wave', 540, 400)}{ch('adult-thumbs', 530, 750)}
</div>"""
# 206 무이자 할부: 파랑 그라데이션 · 카드 든 성인 수강생
B['206'] = f"""<div style="position:absolute;inset:0;background:linear-gradient(160deg,#7DB0F7,#4F86E6);overflow:hidden">{dots(['#fff', '#FFD966'])}
<div style="position:absolute;left:84px;top:110px">{pill('카드 결제 부담 DOWN')}
<div style="margin-top:34px">{line('5만원 이상이면', 64, '#fff')}</div>
<div style="margin-top:6px">{big('무이자', 190)}</div><div style="margin-top:4px">{big('할부', 190, '#FFD966')}</div>
<div style="margin-top:26px">{line('최대 6개월까지', 50, '#fff')}</div></div>
{prop('prop-card', 230, 560, 150, 'transform:rotate(-12deg)')}
{ch('adult-card', 700, 640, 40)}
</div>"""
# 207 지인 추천: 초록 · 추천하는 수강생 + 친구
B['207'] = f"""<div style="position:absolute;inset:0;background:radial-gradient(circle at 50% 30%,#7CD6A0,#3FAE72);overflow:hidden">{dots(['#fff', '#FFD966'])}
<div style="position:absolute;left:0;right:0;top:70px;text-align:center">{pill('지인 추천 이벤트', '#fff')}
<div style="margin-top:24px">{line('추천하면 둘 다', 62, '#fff')}</div>
<div style="margin-top:6px;display:flex;justify-content:center;align-items:center;gap:18px">{big('5%', 190)}<span style="font:900 100px/1 {F};color:#FFD966;-webkit-text-stroke:5px {INK};paint-order:stroke fill">+</span>{big('5%', 190)}</div></div>
{prop('prop-coin', 120, 480, 640, 'transform:rotate(-14deg)')}
{ch('adult-recommend', 520, 70)}{ch('student-gift', 480, 640)}
</div>"""
# 205 체험 후기: 노랑 · 휴대폰으로 후기 쓰는 학생 + 말풍선·동전
B['205'] = f"""<div style="position:absolute;inset:0;background:#FFD45E;overflow:hidden">{dots(['#fff', '#EC6856'])}
<div style="position:absolute;left:0;top:0;width:520px;height:1080px;background:#FFC23D;border-radius:0 300px 300px 0"></div>
{prop('prop-bubble', 170, 300, 150, 'transform:rotate(-6deg)')}{prop('prop-coins', 150, 330, 820)}
{ch('student-phone', 640, 90, 50)}
<div style="position:absolute;left:560px;top:250px">{pill('신규 회원 선물', '#fff', size=34)}
<div style="margin-top:28px">{line('무료체험<br>후기 쓰면', 58)}</div>
<div style="margin-top:14px;display:flex;align-items:flex-end;gap:6px">{big('3,000', 150, '#EC6856')}{big('원', 90, '#EC6856', sw=5)}</div>
<div style="margin-top:18px">{line('바로 적립!', 54)}</div></div>
</div>"""
# 211 첫 결제 5%: 연한 복숭아 · 선물 든 학생 + 박수 치는 선생님
B['211'] = f"""<div style="position:absolute;inset:0;background:#FFE7DE;overflow:hidden">{dots(['#EC6856', '#FFD966'])}{floor('#FFD3C4', 790)}
<div style="position:absolute;left:0;right:0;top:70px;text-align:center">{pill('신규회원 전용')}
<div style="margin-top:22px">{line('첫 결제하면', 66)}</div>
<div style="margin-top:4px;display:flex;justify-content:center;align-items:flex-end;gap:8px">{big('5%', 210, '#EC6856')}{big('적립', 110, '#EC6856', sw=5)}</div>
<div style="margin-top:14px">{line('1·3·6개월 수강권 · 주 2회 이상', 38, '#7a5a50')}</div></div>
{prop('prop-gift', 140, 470, 600, 'transform:rotate(8deg)')}
{ch('student-gift', 500, 90)}{ch('teacher-clap', 540, 660)}
</div>"""
# 887 3회 맛보기: 청록 · 고민하는 학생 + 괜찮다는 선생님
B['887'] = f"""<div style="position:absolute;inset:0;background:#2F9C95;overflow:hidden">{dots(['#fff', '#FFD966'])}{floor('#3FB3AB', 800)}
<div style="position:absolute;left:0;right:0;top:66px;text-align:center">{pill('신규회원 한정')}
<div style="margin-top:22px">{line('25분 수업 3회', 72, '#fff')}</div>
<div style="margin-top:4px;display:flex;justify-content:center;align-items:flex-end;gap:6px">{big('10,000', 190, '#FFD966')}{big('원', 100, '#FFD966', sw=5)}</div>
<div style="margin-top:14px">{line('1회당 약 3,300원 · 정규수업과 같은 방식', 36, '#E6FFFB')}</div></div>
{ch('student-think', 500, 130)}{ch('teacher-thumbs', 540, 620)}
</div>"""


# ── 본문 장면 900×540: 두 사람 + 말풍선 ─────────────────────────────
def bub(text, bg='#fff', fs=38):
    return f'<div style="background:{bg};border:4px solid {INK};border-radius:28px;padding:{fs*.42:.0f}px {fs*.8:.0f}px;font:700 {fs}px/1.25 {F};color:{INK};white-space:nowrap">{text}</div>'


def duo(lt, lc, lh, rt, rc, rh, bg):
    return f"""<div style="position:absolute;inset:4px;background:{bg};border:4px solid {INK};border-radius:44px;overflow:hidden">
<div style="position:absolute;left:0;right:0;top:400px;bottom:-100px;background:rgba(255,255,255,.55);border-radius:50% 50% 0 0/50px 50px 0 0"></div>
{ch(lc, lh, 110, 30)}{ch(rc, rh, 580, 30)}
<div class="bb" style="position:absolute;left:30px;top:28px;z-index:2">{bub(lt)}</div><div class="bb" style="position:absolute;right:30px;top:28px;z-index:2">{bub(rt, '#FFD966')}</div></div>"""


H = 300  # 말풍선(위쪽 약 165px)과 겹치지 않는 높이
S = {
    '130': duo('친구랑 같이<br>시작할래요!', 'adult-recommend', H, '두 분 다 5%씩<br>적립해 드려요!', 'teacher-clap', H, '#E6F6EE'),
    '206': duo('한 번에 결제하기<br>부담돼요', 'adult-phone', H, '카드 무이자 할부로<br>나눠 내세요!', 'teacher-explain', H, '#E3EDFF'),
    '207': duo('친구한테 아인<br>추천했어요!', 'adult-recommend', H, '덕분에 저도<br>5% 받았어요!', 'student-gift', H, '#E6F6EE'),
    '205': duo('체험 후기<br>남겼어요!', 'student-phone', H, '3,000원<br>적립해 드릴게요!', 'teacher-thumbs', H, '#FFF6D6'),
    '211': duo('첫 결제인데<br>혜택 있어요?', 'adult-card', H, '결제 금액의 5%를<br>바로 드려요!', 'teacher-explain', H, '#FFF1EC'),
    '199': duo('선생님 덕분에<br>말이 늘었어요!', 'adult-thumbs', H, '그 이야기를<br>후기로 남겨 주세요!', 'teacher-clap', H, '#EEEAFF'),
    '203': duo('다음 달도<br>계속 들을래요!', 'adult-phone', H, '네이버에서 3만원 내면<br>4만원 적립!', 'teacher-explain', H, '#FFF4E2'),
    '887': duo('15분 체험으론<br>아직 잘 모르겠어요', 'student-think', H, '3번 더 해 보고<br>정해도 돼요!', 'teacher-thumbs', H, '#E4F5F3'),
}


# ── 좁은 띠 그림(투명 배경): 캐릭터 한 명 + 큰 말풍선 ───────────────
def strip(w, who, text):
    return f"""<div style="position:absolute;inset:0;display:flex;align-items:center;gap:26px;padding:0 10px">
<img src="{CAST}{who}.png" style="height:218px;flex:none">
<div style="background:#fff;border:5px solid {INK};border-radius:30px;padding:20px 30px;font:800 42px/1.25 {F};color:{INK};letter-spacing:-.02em">{text}</div></div>"""


X = {
    ('130', 'scene-store.png', 600): strip(600, 'adult-phone', '3만원 내고<br>4만원 받기!'),
    ('211', 'scene-use.png', 720): strip(720, 'student-gift', '모은 적립금은<br>다음 수강 때 쓰면 돼요!'),
    ('887', 'scene-report.png', 720): strip(720, 'teacher-report', '수업이 끝나면<br>일일평가서가 와요!'),
}
BANNER_FILE = {'130': 'banner.png', '206': 'banner.jpg', '207': 'banner.jpg', '205': 'banner.jpg', '211': 'banner.png', '887': 'banner.png'}
SCENE_FILE = {'130': 'scene-friend.png'}

jobs = []
for pid, html in B.items(): jobs.append((f'{root}/{pid}/{BANNER_FILE[pid]}', 1080, 1080, html, False))
for pid, html in S.items(): jobs.append((f'{root}/{pid}/{SCENE_FILE.get(pid, "scene-hello.png")}', 900, 540, html, True))
for (pid, name, w), html in X.items(): jobs.append((f'{root}/{pid}/{name}', w, 230, html, True))

with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome')
    for path, w, h, html, transparent in jobs:
        tmp = '/tmp/cast_job.html'
        open(tmp, 'w').write(f'<html><body style="margin:0;width:{w}px;height:{h}px;position:relative;overflow:hidden;background:transparent">{html}</body></html>')
        pg = b.new_page(viewport={'width': w, 'height': h}); pg.goto('file://' + tmp); pg.wait_for_timeout(300)
        ov = pg.evaluate('''() => { const b=[...document.querySelectorAll('.bb')].map(e=>e.getBoundingClientRect()); const c=[...document.querySelectorAll('.cc')].map(e=>e.getBoundingClientRect());
          let n=0; for (const x of b) for (const y of c) if (x.left<y.right && y.left<x.right && x.top<y.bottom && y.top<x.bottom) n++; return n; }''')
        if ov: print('OVERLAP', path, ov)
        if path.endswith('.jpg'): pg.screenshot(path=path, type='jpeg', quality=92)
        else: pg.screenshot(path=path, omit_background=transparent)
        pg.close(); print(path)
    b.close()


# ── 목록 썸네일 1080×1080: 캐릭터 없이, 큰 혜택 글자 + 3D 소품 하나 ─────────
def thumb(bg, inner, deco=('#fff', '#FFD966')):
    return f'<div style="position:absolute;inset:0;background:{bg};overflow:hidden">{dots(list(deco))}{inner}</div>'


T = {
    '206': thumb('linear-gradient(160deg,#7DB0F7,#4F86E6)', f"""
<div style="position:absolute;left:90px;top:120px">{pill('카드 결제 부담 DOWN', size=40)}
<div style="margin-top:40px">{line('5만원 이상이면', 72, '#fff')}</div>
<div style="margin-top:8px">{big('무이자', 230)}</div><div style="margin-top:6px">{big('할부', 230, '#FFD966')}</div>
<div style="margin-top:30px">{line('최대 6개월까지', 60, '#fff')}</div></div>
{prop('prop-card', 330, 680, 640, 'transform:rotate(-14deg)')}"""),
    '887': thumb('#2F9C95', f"""
<div style="position:absolute;left:0;right:0;top:120px;text-align:center">{pill('신규회원 한정', size=40)}
<div style="margin-top:34px">{line('25분 수업 3회', 92, '#fff')}</div>
<div style="margin-top:14px;display:flex;justify-content:center;align-items:flex-end;gap:8px">{big('10,000', 230, '#FFD966')}{big('원', 120, '#FFD966', sw=6)}</div>
<div style="margin-top:26px">{line('1회당 약 3,300원', 56, '#E6FFFB')}</div></div>
{prop('prop-star', 210, 790, 770, 'transform:rotate(12deg)')}{prop('prop-coin', 150, 120, 820, 'transform:rotate(-14deg)')}"""),
    '207': thumb('radial-gradient(circle at 50% 35%,#7CD6A0,#3FAE72)', f"""
<div style="position:absolute;left:0;right:0;top:110px;text-align:center">{pill('지인 추천 이벤트', '#fff', size=40)}
<div style="margin-top:34px">{line('추천하면 둘 다', 80, '#fff')}</div>
<div style="margin-top:10px;display:flex;justify-content:center;align-items:center;gap:20px">{big('5%', 230)}<span style="font:900 120px/1 {F};color:#FFD966;-webkit-text-stroke:6px {INK};paint-order:stroke fill">+</span>{big('5%', 230)}</div></div>
{prop('prop-coins', 300, 390, 700)}"""),
    '205': thumb('#FFD45E', f"""
<div style="position:absolute;left:0;right:0;top:110px;text-align:center">{pill('신규 회원 선물', '#fff', size=40)}
<div style="margin-top:34px">{line('무료체험 후기 쓰면', 80)}</div>
<div style="margin-top:14px;display:flex;justify-content:center;align-items:flex-end;gap:8px">{big('3,000', 220, '#EC6856')}{big('원', 120, '#EC6856', sw=6)}</div>
<div style="margin-top:20px">{line('바로 적립!', 72)}</div></div>
{prop('prop-bubble', 230, 110, 760, 'transform:rotate(-8deg)')}{prop('prop-coins', 220, 760, 800)}""", ('#fff', '#EC6856')),
    '199': thumb('linear-gradient(170deg,#9C8CF5,#6F5DE0)', f"""
<div style="position:absolute;left:0;right:0;top:110px;text-align:center">{pill('수강후기 이벤트', size=40)}
<div style="margin-top:34px">{line('베스트 후기는', 84, '#fff')}</div>
<div style="margin-top:14px;display:flex;justify-content:center;align-items:flex-end;gap:8px">{big('최대 2만원', 190, '#FFD966')}</div>
<div style="margin-top:24px">{line('적립해 드려요', 64, '#fff')}</div></div>
{prop('prop-star', 230, 120, 780, 'transform:rotate(-10deg)')}<img src="file://{HERE}/cut/popper.png" style="position:absolute;left:740px;top:760px;height:250px;transform:rotate(-8deg);filter:drop-shadow(0 10px 14px rgba(0,0,0,.14))">"""),
    '203': thumb('#FFF4E2', f"""
<div style="position:absolute;left:0;right:0;top:110px;text-align:center">{pill('재수강 회원 전용', '#2DB46B', '#fff', 40)}
<div style="margin-top:34px">{line('네이버 스토어에서', 80)}</div>
<div style="margin-top:14px;display:flex;justify-content:center;align-items:center;gap:22px">{big('3만', 200, '#FFD45E')}<span style="font:900 130px/1 {F};color:#2DB46B">→</span>{big('4만', 200, '#EC6856')}</div>
<div style="margin-top:20px">{line('매달 1만원 더 적립!', 64)}</div></div>
{prop('prop-bag', 260, 140, 760, 'transform:rotate(-6deg)')}{prop('prop-coins', 210, 760, 820)}""", ('#2DB46B', '#FFD966', '#EC6856')),
    '211': thumb('#FFE7DE', f"""
<div style="position:absolute;left:0;right:0;top:110px;text-align:center">{pill('신규회원 전용', size=40)}
<div style="margin-top:34px">{line('첫 결제하면', 86)}</div>
<div style="margin-top:10px;display:flex;justify-content:center;align-items:flex-end;gap:10px">{big('5%', 260, '#EC6856')}{big('적립', 140, '#EC6856', sw=6)}</div>
<div style="margin-top:20px">{line('1·3·6개월 수강권 · 주 2회 이상', 46, '#7a5a50')}</div></div>
{prop('prop-gift', 260, 410, 770, 'transform:rotate(6deg)')}""", ('#EC6856', '#FFD966')),
}

with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome')
    for pid, html in T.items():
        tmp = '/tmp/cast_thumb.html'
        open(tmp, 'w').write(f'<html><body style="margin:0;width:1080px;height:1080px;position:relative;overflow:hidden">{html}</body></html>')
        pg = b.new_page(viewport={'width': 1080, 'height': 1080}); pg.goto('file://' + tmp); pg.wait_for_timeout(300)
        pg.screenshot(path=f'{root}/{pid}/thumb.png'); pg.close(); print(f'{root}/{pid}/thumb.png')
    b.close()
