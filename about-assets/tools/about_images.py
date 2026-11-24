#!/usr/bin/env python3
"""아인잉글리쉬 about 페이지('왜 아인 화상영어일까?')용 그림 생성기.

사용법: python3 about-assets/tools/about_images.py about-assets/
부드러운 파스텔 캐릭터(테두리 없는 색면)로 그린다. 색은 로고 코랄에 맞춘다.
필요한 것: playwright, Chrome(/usr/bin/google-chrome), Noto Sans CJK KR 글꼴.
"""
import sys, os

CORAL = '#EC6856'; INK = '#222222'; GRAY = '#777777'; YEL = '#FFE066'; TINT = '#FDF1EE'
BLUE_BG = '#E8F0FF'; PINK_BG = '#FFE9E4'; YEL_BG = '#FFF6D6'; MINT_BG = '#EAFBF4'

def ch(role='s', mood='smile'):
    """role: s(학생) | t(선생님), mood: smile | think"""
    t = role == 't'
    hair = '#6B4226' if t else '#2F2A3A'; shirt = CORAL if t else '#5B8DEF'; skin = '#FFD9C2'
    g = ''
    if t: g += f'<path d="M40,92 Q40,28 100,28 Q160,28 160,92 L164,172 Q150,184 132,176 L132,120 L68,120 L68,176 Q50,184 36,172 Z" fill="{hair}"/>'
    else: g += f'<circle cx="100" cy="84" r="57" fill="{hair}"/>'
    g += f'<path d="M26,222 Q26,160 100,160 Q174,160 174,222 Z" fill="{shirt}"/>'
    g += f'<rect x="87" y="132" width="26" height="36" rx="12" fill="{skin}"/>'
    g += '<path d="M80,162 Q100,182 120,162 L113,160 Q100,170 87,160 Z" fill="#fff" opacity=".9"/>'
    g += f'<circle cx="100" cy="94" r="49" fill="{skin}"/>'
    if t: g += f'<path d="M52,90 Q56,40 104,38 Q148,42 149,92 Q126,60 52,90 Z" fill="{hair}"/>'
    else: g += f'<path d="M50,88 Q58,40 100,38 Q144,40 150,90 Q130,64 102,68 Q86,60 70,76 Q60,82 50,88 Z" fill="{hair}"/>'
    g += '<ellipse cx="82" cy="100" rx="4.2" ry="5.6" fill="#33272A"/><ellipse cx="118" cy="100" rx="4.2" ry="5.6" fill="#33272A"/>'
    g += '<circle cx="69" cy="113" r="8" fill="#FF9E9E" opacity=".5"/><circle cx="131" cy="113" r="8" fill="#FF9E9E" opacity=".5"/>'
    if mood == 'think':
        g += '<path d="M73,88 L89,84" stroke="#33272A" stroke-width="3" stroke-linecap="round"/><path d="M111,84 L127,88" stroke="#33272A" stroke-width="3" stroke-linecap="round"/>'
        g += '<ellipse cx="100" cy="119" rx="5" ry="6" fill="#B5533F"/>'
        g += '<path d="M160,50 Q170,66 170,74 A10,10 0 0 1 150,74 Q150,66 160,50 Z" fill="#8CC8FF"/>'
    else:
        g += '<path d="M89,115 Q100,126 111,115" fill="none" stroke="#33272A" stroke-width="3.4" stroke-linecap="round"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 222">{g}</svg>'

CSS = f'''
*{{box-sizing:border-box}} body{{margin:0}}
.cv{{position:relative;overflow:hidden;font-family:"Noto Sans CJK KR","Noto Sans KR",sans-serif;color:{INK}}}
.a{{position:absolute}}
.tile{{position:absolute;border-radius:36px;overflow:hidden;display:flex;align-items:flex-end;justify-content:center}}
.tile svg{{width:88%;display:block}}
.fig svg{{display:block;width:100%}}
.bub{{position:absolute;background:#fff;border-radius:26px;padding:18px 28px;font-weight:700;font-size:30px;line-height:1.4;box-shadow:0 10px 24px rgba(0,0,0,.08);white-space:nowrap}}
.bub.y{{background:{YEL}}}
.card{{position:absolute;background:#fff;border-radius:28px;box-shadow:0 14px 32px rgba(0,0,0,.10)}}
.pill{{position:absolute;background:{INK};color:#fff;border-radius:40px;padding:8px 22px;font-weight:700;font-size:22px;white-space:nowrap}}
.lab{{position:absolute;font-weight:700;font-size:26px;text-align:center}}
.num{{position:absolute;left:40px;top:40px;width:88px;height:88px;border-radius:50%;background:{CORAL};color:#fff;font-weight:900;font-size:46px;line-height:88px;text-align:center}}
.x{{text-decoration:line-through;text-decoration-color:{CORAL};text-decoration-thickness:4px;color:{GRAY}}}
.cap{{position:absolute;left:0;right:0;text-align:center;font-weight:700;font-size:32px}}
'''

def tile(x, y, s, bg, role, mood='smile'):
    return f'<div class="tile" style="left:{x}px;top:{y}px;width:{s}px;height:{s}px;background:{bg}">{ch(role, mood)}</div>'
def fig(x, w, role='s', mood='smile'):
    return f'<div class="a fig" style="left:{x}px;bottom:0;width:{w}px">{ch(role, mood)}</div>'
def bub(x, y, html, cls='', extra=''):
    return f'<div class="bub {cls}" style="left:{x}px;top:{y}px;{extra}">{html}</div>'

def hero():
    return 1440, 860, '#ffffff', (
        f'<div class="a" style="left:0;top:0;right:0;height:92px;background:{TINT}"></div>'
        + ''.join(f'<div class="a" style="left:{48+i*40}px;top:34px;width:24px;height:24px;border-radius:50%;background:{c}"></div>' for i, c in enumerate(('#FF8A7A', '#FFD666', '#7ADFB5')))
        + '<div class="a" style="left:190px;top:22px;font-weight:700;font-size:30px">1:1 화상수업</div>'
        + tile(80, 150, 400, BLUE_BG, 's', 'think') + tile(960, 150, 400, PINK_BG, 't')
        + '<div class="lab" style="left:80px;top:566px;width:400px">학생</div><div class="lab" style="left:960px;top:566px;width:400px">선생님</div>'
        + f'<div class="a" style="left:480px;width:480px;top:170px;text-align:center;font-weight:700;font-size:30px;color:{GRAY}">그 자리에서 바로 교정</div>'
        + '<div class="a x" style="left:480px;width:480px;top:226px;text-align:center;font-weight:900;font-size:84px;line-height:1.2">try</div>'
        + f'<div class="a" style="left:480px;width:480px;top:336px;text-align:center;font-weight:900;font-size:48px;color:{CORAL}">↓</div>'
        + f'<div class="a" style="left:480px;width:480px;top:410px;text-align:center"><span style="display:inline-block;background:{YEL};border-radius:24px;padding:0 36px;font-weight:900;font-size:108px;line-height:1.3">tries</span></div>'
        + f'<div class="card" style="left:80px;top:650px;width:610px;height:160px;background:#F7F7F7;box-shadow:none;padding:26px 32px"><div style="font-weight:700;font-size:24px;color:{GRAY}">학생이 말한 문장</div><div class="x" style="margin-top:14px;font-weight:500;font-size:33px">He always try to care of others.</div></div>'
        + f'<div class="card" style="left:750px;top:650px;width:610px;height:160px;background:{YEL};box-shadow:none;padding:26px 32px"><div style="font-weight:700;font-size:24px">선생님이 고쳐 준 문장</div><div style="margin-top:14px;font-weight:900;font-size:29px;white-space:nowrap">He always tries to take care of others.</div></div>')

def pain(mood, bubbles, bg):
    body = fig(10, 320, 's', mood); y = 64
    for html, cls in bubbles:
        lines = html.count('<br>') + 1
        body += bub(336, y, html, cls); y += 36 + lines * 42 + 22
    return 720, 480, bg, body

def flow(n, body): return 720, 720, TINT, f'<div class="num">{n}</div>' + body
F1 = (tile(80, 170, 270, BLUE_BG, 's') + tile(370, 170, 270, PINK_BG, 't')
      + '<div class="lab" style="left:80px;top:452px;width:270px">학생</div><div class="lab" style="left:370px;top:452px;width:270px">선생님</div>'
      + bub(130, 530, '25분, 선생님과 1:1 대화', '', 'font-size:34px'))
F2 = (bub(80, 180, '<span class="x">I go to there yesterday.</span>', '', 'font-size:38px;font-weight:500;width:560px')
      + f'<div class="cap" style="top:316px;font-size:52px;font-weight:900;color:{CORAL}">↓</div>'
      + bub(80, 410, 'I went there yesterday.', 'y', 'font-size:42px;font-weight:900;width:560px;padding:26px 28px')
      + '<div class="cap" style="top:588px">틀린 문장은 그 자리에서</div>')
F3 = (f'<div class="card" style="left:190px;top:150px;width:340px;height:530px;border-radius:44px;padding:30px 28px">'
      f'<div style="text-align:center;font-weight:900;font-size:30px">일일평가서</div><div style="height:3px;background:#eee;margin:16px 0 22px"></div>'
      f'<div style="background:#F7F7F7;border-radius:12px;padding:16px 18px;font-size:22px;color:{GRAY}">Q1. Student: …</div>'
      '<div style="background:#ECFDF5;border-radius:14px;padding:14px 18px;margin-top:16px"><div style="font-weight:700;font-size:17px;color:#10B981">BETTER EXPRESSION</div><div style="height:14px;width:220px;border-radius:7px;background:#065F46;margin-top:12px"></div><div style="height:12px;width:150px;border-radius:6px;background:#6FCFB0;margin-top:10px"></div></div>'
      '<div style="background:#FFFBEB;border-radius:14px;padding:14px 18px;margin-top:16px"><div style="font-weight:700;font-size:17px;color:#D97706">ALTERNATIVE</div><div style="height:14px;width:200px;border-radius:7px;background:#92400E;margin-top:12px"></div></div>'
      f'<div style="background:{CORAL};border-radius:30px;margin-top:26px;height:60px;line-height:60px;text-align:center;color:#fff;font-weight:700;font-size:22px">오늘의 복습 완료하기</div></div>'
      f'<div class="a" style="left:486px;top:116px;width:88px;height:88px;border-radius:50%;background:#FF5A4D;color:#fff;font-weight:900;font-size:46px;line-height:88px;text-align:center;box-shadow:0 8px 16px rgba(0,0,0,.15)">1</div>')
F4 = (tile(40, 200, 300, BLUE_BG, 's')
      + f'<div class="card" style="left:350px;top:190px;width:330px;height:290px;padding:26px 30px"><div style="font-weight:700;font-size:24px;color:{GRAY}">실전 퀴즈</div><div style="margin-top:14px;font-weight:700;font-size:36px;line-height:1.45">I ____ there<br>yesterday.</div><div style="margin-top:14px"><span style="background:{YEL};border-radius:8px;padding:2px 12px;font-weight:900;font-size:36px">went</span></div></div>'
      + '<div class="a" style="left:600px;top:150px;width:100px;height:100px;border-radius:50%;background:#10B981;box-shadow:0 8px 16px rgba(0,0,0,.15)"><svg viewBox="0 0 100 100"><path d="M26,52 L44,70 L76,34" fill="none" stroke="#fff" stroke-width="11" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
      + '<div class="cap" style="top:626px">고친 문장을 내 것으로</div>')

T1 = (f'<div class="card" style="left:70px;top:44px;width:250px;height:400px;border-radius:36px;padding:28px 24px">'
      '<div style="text-align:center;font-weight:900;font-size:26px">무료체험 신청</div><div style="height:3px;background:#eee;margin:14px 0 20px"></div>'
      f'<div style="background:{YEL};border-radius:14px;height:60px;line-height:60px;text-align:center;font-weight:700;font-size:22px">강사 추천받기</div>'
      f'<div style="background:#F7F7F7;border-radius:14px;height:60px;line-height:60px;text-align:center;font-weight:700;font-size:22px;color:{GRAY};margin-top:16px">직접 강사 선택</div>'
      f'<div style="background:{CORAL};border-radius:32px;height:64px;line-height:64px;text-align:center;font-weight:900;font-size:24px;color:#fff;margin-top:52px">신청하기</div></div>'
      + fig(400, 290) + bub(400, 36, '오늘 바로 될까?'))
T2 = (tile(50, 96, 250, '#D6E4FF', 's') + tile(330, 96, 250, '#FFD9D0', 't')
      + f'<div class="a" style="left:528px;top:30px;width:164px;height:164px;border-radius:50%;background:{YEL};font-weight:900;font-size:54px;line-height:164px;text-align:center;box-shadow:0 10px 20px rgba(0,0,0,.12)">15분</div>'
      + bub(120, 372, 'Hello! Nice to meet you.'))
T3 = (f'<div class="card" style="left:150px;top:64px;width:420px;height:380px;padding:30px 36px"><div style="font-weight:900;font-size:28px;line-height:70px">레벨테스트 결과</div>'
      f'<div class="a" style="right:30px;top:20px;width:96px;height:96px;border-radius:50%;background:{CORAL};color:#fff;font-weight:900;font-size:32px;line-height:96px;text-align:center">Lv.4</div>'
      + ''.join(f'<div style="display:flex;align-items:center;margin-top:{14 if i==0 else 20}px"><div style="width:94px;font-weight:700;font-size:22px;color:{GRAY}">{n}</div><div style="flex:1;height:18px;border-radius:9px;background:#F1F1F1"><div style="width:{w}%;height:18px;border-radius:9px;background:{CORAL}"></div></div></div>' for i, (n, w) in enumerate((('어휘', 62), ('리스닝', 74), ('유창성', 50), ('문법', 56), ('발음', 70))))
      + '</div><div class="pill" style="left:232px;top:16px">30분~1시간 안에 도착</div>')
T4 = (fig(10, 300) + bub(300, 56, '수업 시간과 교재,<br>같이 정해 드릴게요', 'y') + bub(380, 236, '네, 좋아요!')
      + '<div class="pill" style="left:300px;top:366px">학습 매니저 상담</div>')
def trial(bg, body): return 720, 480, bg, body

def scenes():
    return {
        'hero_scene.png': hero(),
        'pain_1.png': pain('think', [('Um… I…<br>yesterday… movie?', '')], BLUE_BG),
        'pain_2.png': pain('smile', [('It was good.', ''), ('It was good.', ''), ('It was… good.', '')], YEL_BG),
        'pain_3.png': pain('think', [('I go to there<br>yesterday.', ''), ('Okay! Next~', 'y')], PINK_BG),
        'pain_4.png': pain('think', [('어제 뭐<br>배웠더라…?', '')], MINT_BG),
        'flow_1.png': flow(1, F1), 'flow_2.png': flow(2, F2), 'flow_3.png': flow(3, F3), 'flow_4.png': flow(4, F4),
        'trial_1.png': trial(BLUE_BG, T1), 'trial_2.png': trial(YEL_BG, T2), 'trial_3.png': trial(PINK_BG, T3), 'trial_4.png': trial(MINT_BG, T4),
    }

def main(outdir):
    from playwright.sync_api import sync_playwright
    os.makedirs(outdir, exist_ok=True)
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path='/usr/bin/google-chrome')
        for name, (w, h, bg, body) in scenes().items():
            pg = b.new_page(viewport={'width': w, 'height': h})
            pg.set_content(f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="cv" style="width:{w}px;height:{h}px;background:{bg}">{body}</div></body></html>')
            pg.screenshot(path=os.path.join(outdir, name)); pg.close(); print(name, (w, h))
        b.close()

if __name__ == '__main__':
    main(sys.argv[1])
