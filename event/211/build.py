"""211번 글(신규회원 5% 적립금) 본문 HTML 생성. python3 build.py → body.html(사이트용), preview.html(미리보기)"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
CDN = 'https://minkyueine.github.io/ein-tools/event/211/'
INK = '#2A211D'; CORAL = '#EC6856'; DEEP = '#C4452F'
PRICES = [('주 2회', 94000, 262300, 485000), ('주 3회', 129000, 359900, 665600),
          ('주 4회', 149000, 415700, 768800), ('주 5회', 169000, 471500, 872000)]
w = lambda n: f'{n:,}'
PAD = 'clamp(20px, 5vw, 32px)'

def build(img):
    rows = ''
    for i, (label, *ps) in enumerate(PRICES):
        bg = '#FFFFFF' if i % 2 == 0 else '#FFF9F7'
        cells = ''.join(f'<td style="padding: 12px 6px; text-align: center; border-top: 1px solid #F1E4DF"><div style="font-size: 17px; font-weight: 800; color: {DEEP}">{w(round(p*0.05))}원</div><div style="margin-top: 2px; font-size: 12px; color: #9A8F8A">{w(p)}원</div></td>' for p in ps)
        rows += f'<tr style="background: {bg}"><th scope="row" style="padding: 12px 6px; font-size: 15px; font-weight: 800; color: {INK}; border-top: 1px solid #F1E4DF; white-space: nowrap">{label}</th>{cells}</tr>'

    def card(emoji, bg, title, body):
        return f'''<div style="display: flex; gap: 14px; align-items: flex-start; padding: 18px; background: {bg}; border: 2px solid {INK}; border-radius: 18px">
<div style="flex: none; width: 44px; height: 44px; border-radius: 50%; background: #FFF; border: 2px solid {INK}; display: flex; align-items: center; justify-content: center; font-size: 22px">{emoji}</div>
<div><div style="font-size: 15px; font-weight: 700; color: #7A6F6A">{title}</div><div style="margin-top: 2px; font-size: 18px; font-weight: 800; line-height: 1.45; color: {INK}">{body}</div></div></div>'''

    def h2(no, text):
        return f'<h2 style="margin: 0; display: flex; align-items: center; gap: 10px; font-size: 24px; line-height: 1.35; font-weight: 800; color: {INK}"><span style="flex: none; display: inline-flex; align-items: center; justify-content: center; width: 32px; height: 32px; border-radius: 50%; background: {CORAL}; color: #FFF; font-size: 17px">{no}</span>{text}</h2>'

    def li(text):
        return f'<li style="position: relative; padding-left: 18px; margin-top: 10px"><span style="position: absolute; left: 2px; top: 11px; width: 6px; height: 6px; border-radius: 50%; background: {CORAL}"></span>{text}</li>'

    return f'''<div style="max-width: 640px; margin: 0 auto; font-family: Pretendard, 'Noto Sans KR', sans-serif; color: #333; font-size: 16px; line-height: 1.6; word-break: keep-all">

<section style="padding: 8px {PAD} 0">
<p style="margin: 0; font-size: 18px; line-height: 1.7; text-align: center">아인잉글리쉬에서 <b style="color: {INK}">처음 결제</b>하시는 분께<br>결제 금액의 <b style="color: {DEEP}">5%를 적립금</b>으로 바로 드려요.</p>
<div style="margin-top: 24px"><img src="{img}scene-hello.png" alt="첫 결제인데 혜택 있어요? 결제 금액의 5%를 바로 드려요!" style="display: block; width: 100%; height: auto"></div>
</section>

<section style="padding: 48px {PAD} 0">
{h2(1, '누가, 언제 받나요?')}
<div style="display: grid; gap: 12px; margin-top: 20px">
{card('🙋', '#FDE3DC', '대상', '신규 회원의 첫 결제 1회')}
{card('🎟️', '#FFF6D6', '수강권', '1개월 · 3개월 · 6개월 수강권<br><span style="font-size: 16px; font-weight: 700; color: #555">주 2회 이상 수업일 때 (주 1회 제외)</span>')}
{card('⚡', '#E6F6EE', '적립 시점', '수강신청 후 수업 배정과 함께<br>바로 적립돼요')}
</div>
</section>

<section style="padding: 48px {PAD} 0">
{h2(2, '얼마나 받을 수 있나요?')}
<p style="margin: 12px 0 0; font-size: 15px; color: #666">25분 수업, 정가 기준 예시예요. 위는 적립금, 아래는 수강료예요.</p>
<div style="margin-top: 16px; border: 2px solid {INK}; border-radius: 18px; overflow: hidden">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed">
<thead><tr style="background: {CORAL}; color: #FFF"><th style="width: 22%; padding: 12px 4px; font-size: 14px; font-weight: 700"></th><th style="padding: 12px 4px; font-size: 16px; font-weight: 800">1개월</th><th style="padding: 12px 4px; font-size: 16px; font-weight: 800">3개월</th><th style="padding: 12px 4px; font-size: 16px; font-weight: 800">6개월</th></tr></thead>
<tbody>{rows}</tbody>
</table></div>
<p style="margin: 12px 0 0; font-size: 14px; color: #888">실제 적립금은 할인이 적용된 <b>최종 결제 금액의 5%</b>예요. 50분 수업은 수강료에 따라 달라져요.</p>
<div style="margin-top: 16px; text-align: center"><a href="https://einenglish.com/study/tuition" style="display: inline-flex; align-items: center; min-height: 44px; padding: 0 20px; border-radius: 22px; background: #FFF; border: 2px solid {INK}; color: {INK}; font-size: 16px; font-weight: 700; text-decoration: none">💰 전체 수강료 보기 →</a></div>
</section>

<section style="padding: 48px {PAD} 0">
{h2(3, '적립금은 이렇게 써요')}
<div style="margin-top: 20px"><img src="{img}scene-use.png" alt="모은 적립금은 다음 수강 때 쓰면 돼요!" style="display: block; width: 100%; max-width: 420px; height: auto"></div>
<div style="margin-top: 16px; padding: 20px; background: #E3EDFF; border-radius: 18px; font-size: 17px; line-height: 1.6; color: {INK}">
다음 <b>재수강 결제</b> 때 사용할 수 있고,<br><b style="color: #2F5FC4">결제 금액의 최대 30%</b>까지 적립금으로 낼 수 있어요.</div>
</section>

<section style="padding: 48px {PAD} 0">
<div style="padding: 22px; background: #F7F7F7; border-radius: 18px">
<div style="font-size: 18px; font-weight: 800; color: {INK}">📌 꼭 확인하세요</div>
<ul style="margin: 6px 0 0; padding: 0; list-style: none; font-size: 16px; color: #444">
{li('<b>첫 결제 1회</b>에만 적립돼요.')}
{li('주 1회 수강권과 12개월 수강권은 대상이 아니에요.')}
{li('따로 정해진 종료일 없이 진행 중인 이벤트예요.')}
{li('다른 이벤트 혜택은 이번 달 이벤트 안내에서 함께 볼 수 있어요.')}
</ul>
<div style="margin-top: 16px"><a href="https://einenglish.com/cscenter/detail/130" style="color: {DEEP}; font-size: 16px; font-weight: 800; text-decoration: underline; text-underline-offset: 4px">이번 달 전체 이벤트 보기 →</a></div>
</div>
</section>

<section style="margin-top: 48px; padding: 36px {PAD} 40px; background: #FFF6D6; text-align: center">
<div style="font-size: 22px; font-weight: 800; line-height: 1.45; color: {INK}">첫 결제 혜택, 놓치지 마세요 🎁</div>
<p style="margin: 8px 0 0; font-size: 16px; color: #666">결제하면 수업 배정과 함께 5%가 바로 들어와요.</p>
<div style="display: grid; gap: 10px; max-width: 360px; margin: 22px auto 0">
<a href="https://einenglish.com/study" style="display: flex; align-items: center; justify-content: center; min-height: 54px; border-radius: 27px; background: {CORAL}; border: 2px solid {INK}; color: #FFF; font-size: 18px; font-weight: 800; text-decoration: none">수강신청하고 5% 받기</a>
<a href="https://einenglish.com/apply/step1" style="display: flex; align-items: center; justify-content: center; min-height: 50px; border-radius: 25px; background: #FFF; border: 2px solid {INK}; color: {INK}; font-size: 16px; font-weight: 700; text-decoration: none">먼저 무료체험 해 볼게요</a>
</div>
</section>

</div>'''

open(os.path.join(HERE, 'body.html'), 'w').write(build(CDN))
body = build('')
open(os.path.join(HERE, 'preview.html'), 'w').write(f'''<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>211 미리보기</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css"></head>
<body style="margin:0;background:#fff"><div style="max-width:640px;margin:0 auto;padding:24px 0">
<div style="text-align:center;font-family:Pretendard,sans-serif"><div style="color:#666;font-size:15px">이벤트</div><h1 style="margin:10px 0 20px;font-size:30px;line-height:1.35">[진행중] 신규회원 첫 결제<br>5% 적립금 드려요!</h1></div>
<div style="max-width:480px;margin:0 auto 32px;padding:0 20px"><img src="banner.png" style="width:100%;border-radius:16px;display:block"></div>
{body}</div></body></html>''')
print('ok')
