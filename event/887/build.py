"""887번 글(3회 맛보기 수강권) 본문 HTML 생성. python3 build.py → body.html(사이트용, 배너 포함), preview.html(미리보기)"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
CDN = 'https://minkyueine.github.io/ein-tools/event/887/'
INK = '#2A211D'; CORAL = '#EC6856'; DEEP = '#C4452F'
PAD = 'clamp(20px, 5vw, 32px)'


def build(img):
    def card(emoji, bg, title, body):
        return f'''<div style="display: flex; gap: 14px; align-items: flex-start; padding: 18px; background: {bg}; border: 2px solid {INK}; border-radius: 18px">
<div style="flex: none; width: 44px; height: 44px; border-radius: 50%; background: #FFF; border: 2px solid {INK}; display: flex; align-items: center; justify-content: center; font-size: 22px">{emoji}</div>
<div><div style="font-size: 18px; font-weight: 800; line-height: 1.45; color: {INK}">{title}</div><div style="margin-top: 4px; font-size: 16px; line-height: 1.55; color: #555">{body}</div></div></div>'''

    def h2(no, text):
        badge = f'<span style="flex: none; display: inline-flex; align-items: center; justify-content: center; width: 32px; height: 32px; border-radius: 50%; background: {CORAL}; color: #FFF; font-size: 17px">{no}</span>'
        return f'<h2 style="margin: 0; display: flex; align-items: center; gap: 10px; font-size: 24px; line-height: 1.35; font-weight: 800; color: {INK}">{badge}{text}</h2>'

    def li(text):
        return f'<li style="position: relative; padding-left: 18px; margin-top: 10px"><span style="position: absolute; left: 2px; top: 11px; width: 6px; height: 6px; border-radius: 50%; background: {CORAL}"></span>{text}</li>'

    def step(tag, tag_bg, title, sub, bg, strong=False):
        bw = '3px' if strong else '2px'
        return f'''<div style="flex: 1; min-width: 0; padding: 16px 8px; background: {bg}; border: {bw} solid {INK}; border-radius: 18px; text-align: center">
<div style="display: inline-block; padding: 2px 10px; border-radius: 12px; background: {tag_bg}; border: 2px solid {INK}; font-size: 13px; font-weight: 800; color: {INK}">{tag}</div>
<div style="margin-top: 8px; font-size: 17px; font-weight: 800; line-height: 1.35; color: {INK}">{title}</div>
<div style="margin-top: 4px; font-size: 14px; line-height: 1.45; color: #666">{sub}</div></div>'''

    arrow = f'<div style="flex: none; align-self: center; font-size: 20px; font-weight: 800; color: {CORAL}">›</div>'

    def report_row(label, label_bg, text, strike=False):
        deco = 'text-decoration: line-through; text-decoration-color: #E0604F; color: #888' if strike else f'color: {INK}'
        return f'''<div style="margin-top: 10px; padding: 12px 14px; background: {label_bg}; border: 2px solid {INK}; border-radius: 14px">
<div style="font-size: 12px; font-weight: 800; letter-spacing: .04em; color: #7A6F6A">{label}</div>
<div style="margin-top: 2px; font-size: 17px; font-weight: 700; line-height: 1.45; {deco}">{text}</div></div>'''

    def chip(t):
        return f'<span style="display: inline-block; margin: 4px 3px 0; padding: 4px 12px; border-radius: 14px; background: #FFF; border: 2px solid {INK}; font-size: 14px; font-weight: 700; color: {INK}">{t}</span>'

    def check(t):
        return f'<div style="display: flex; gap: 10px; align-items: center; padding: 14px 16px; background: #FFF; border: 2px solid {INK}; border-radius: 14px; font-size: 17px; font-weight: 700; color: {INK}"><span style="flex: none; display: inline-flex; align-items: center; justify-content: center; width: 26px; height: 26px; border-radius: 50%; background: #A8E6CF; border: 2px solid {INK}; font-size: 14px">✓</span>{t}</div>'

    def qa(q, a):
        return f'''<div style="padding: 18px 0; border-top: 1px solid #EEE4E0">
<div style="font-size: 17px; font-weight: 800; line-height: 1.5; color: {INK}"><span style="color: {CORAL}">Q.</span> {q}</div>
<div style="margin-top: 6px; font-size: 16px; line-height: 1.6; color: #555">{a}</div></div>'''

    return f'''<div style="max-width: 640px; margin: 0 auto; font-family: Pretendard, 'Noto Sans KR', sans-serif; color: #333; font-size: 16px; line-height: 1.6; word-break: keep-all">

<section style="padding: 8px {PAD} 0">
<p style="margin: 0; font-size: 18px; line-height: 1.7; text-align: center">15분 무료체험만으로는<br><b style="color: {INK}">강사와 잘 맞는지, 수업이 나에게 맞는지</b><br>판단하기 어려우셨죠?<br><br>정규수업과 같은 <b style="color: {DEEP}">25분 수업 3회를 1만 원</b>에<br>받아 보고 결정하세요.</p>
<div style="margin-top: 24px"><img src="{img}scene-hello.png" alt="15분 체험으론 아직 잘 모르겠어요 / 3번 더 해 보고 정해도 돼요!" style="display: block; width: 100%; height: auto"></div>
</section>

<section style="padding: 48px {PAD} 0">
{h2(1, '무료체험 다음, 이렇게 이어져요')}
<div style="display: flex; gap: 6px; margin-top: 20px">
{step('무료', '#FFF', '무료체험', '15분 · 1회<br>레벨테스트', '#F7F7F7')}
{arrow}
{step('10,000원', '#FFD966', '3회 맛보기', '25분 · 3회<br>강사 1명 선택', '#FDE3DC', True)}
{arrow}
{step('결정', '#FFF', '정규수강', '마음에 들면<br>이어서 수강', '#E6F6EE')}
</div>
<p style="margin: 14px 0 0; font-size: 15px; color: #666; text-align: center">1회당 약 3,300원으로 정규수업을 그대로 경험해요.</p>
</section>

<section style="padding: 48px {PAD} 0">
{h2(2, '3번이면 이런 걸 확인할 수 있어요')}
<div style="display: grid; gap: 12px; margin-top: 20px">
{card('👩‍🏫', '#FDE3DC', '강사와 잘 맞는지', '원하는 강사 1명과 3번 연달아 수업해요.<br>한 번으론 몰랐던 호흡이 보여요.')}
{card('✏️', '#FFF6D6', '틀린 문장을 바로 고쳐 주는지', '말하다 틀린 문장은 수업 중에 바로 교정해 줘요.<br>고친 문장을 다시 말해 보며 익혀요.')}
{card('📝', '#E6F6EE', '수업 후 복습이 되는지', '매 수업 뒤 일일평가서로<br>오늘 배운 문장을 다시 볼 수 있어요.')}
</div>
</section>

<section style="padding: 48px {PAD} 0">
{h2(3, '수업이 끝나면 이런 평가서가 와요')}
<div style="margin-top: 20px"><img src="{img}scene-report.png" alt="수업이 끝나면 일일평가서가 와요!" style="display: block; width: 100%; max-width: 420px; height: auto"></div>
<div style="margin-top: 16px; padding: 20px 18px; background: #FFF9F7; border: 2px solid {INK}; border-radius: 18px">
<div style="display: flex; justify-content: space-between; align-items: center"><div style="font-size: 18px; font-weight: 800; color: {INK}">📋 일일평가서</div><div style="font-size: 13px; font-weight: 700; color: #9A8F8A">문장 교정 예시</div></div>
{report_row('내가 말한 문장', '#F3F3F3', 'I go to the park yesterday.', True)}
{report_row('BETTER', '#D9F3E6', 'I <b style="color: {DEEP}">went</b> to the park yesterday.')}
{report_row('ALTERNATIVE', '#FFF3C4', 'I <b style="color: {DEEP}">visited</b> the park yesterday.')}
<div style="margin-top: 14px; text-align: center">{chip('단어 암기')}{chip('발음 교정')}{chip('문장 교정')}{chip('실전 퀴즈')}</div>
</div>
<p style="margin: 12px 0 0; font-size: 15px; color: #666">평가서는 3회 맛보기 수업에도 매번 똑같이 제공돼요.</p>
</section>

<section style="padding: 48px {PAD} 0">
{h2(4, '이런 분께 추천해요')}
<div style="display: grid; gap: 10px; margin-top: 20px">
{check('무료체험 15분이 짧게 느껴졌던 분')}
{check('강사를 조금 더 겪어 보고 싶은 분')}
{check('정규등록 전에 부담 없이 확인하고 싶은 분')}
{check('화상영어가 처음이라 망설여지는 분')}
</div>
</section>

<section style="padding: 48px {PAD} 0">
<div style="padding: 22px; background: #F7F7F7; border-radius: 18px">
<div style="font-size: 18px; font-weight: 800; color: {INK}">📌 꼭 확인하세요</div>
<ul style="margin: 6px 0 0; padding: 0; list-style: none; font-size: 16px; color: #444">
{li('<b>신규회원 전용</b>이며, <b>1인 1회</b>만 구매할 수 있어요.')}
{li('이벤트 수강권이라 <b>수업 연기·스케줄 변경이 안 되고</b>, <b>학생 휴강권도 없어요.</b>')}
{li('처음 정한 스케줄대로 3회가 진행되니, <b>꼭 수업 가능한 시간</b>으로 신청해 주세요.')}
</ul>
</div>
</section>

<section style="padding: 48px {PAD} 0">
<h2 style="margin: 0 0 6px; font-size: 24px; line-height: 1.35; font-weight: 800; color: {INK}">💬 자주 묻는 질문</h2>
{qa('무료체험을 했는데 구매할 수 있나요?', '네, 무료체험 이후에 구매하실 수 있어요.')}
{qa('강사를 직접 고를 수 있나요?', '네, 원하시는 강사 1명을 직접 골라 3회 모두 그 강사와 수업해요.')}
{qa('정규수업과 다른 점이 있나요?', '수업 방식은 25분 정규수업과 같아요. 다만 이벤트 수강권이라 수업 연기, 학생 휴강권, 스케줄 변경은 적용되지 않아요.')}
{qa('수업을 미루거나 시간을 바꿀 수 있나요?', '아니요, 수업 연기와 스케줄 변경이 안 되고 학생 휴강권도 제공되지 않아요.')}
{qa('마음에 들면 이어서 수강할 수 있나요?', '네, 3회 수업 후 원하시는 스케줄로 정규수강을 신청하시면 돼요.')}
</section>

<section style="margin-top: 40px; padding: 36px {PAD} 40px; background: #FFF6D6; text-align: center">
<div style="font-size: 22px; font-weight: 800; line-height: 1.45; color: {INK}">무료체험만으로 부족했다면<br>3번 더 경험해 보세요 🎁</div>
<div style="margin-top: 14px; font-size: 15px; font-weight: 700; color: #7A6F6A">25분 × 3회 · 신규회원 1인 1회</div>
<div style="margin-top: 2px; font-size: 34px; font-weight: 900; color: {DEEP}">10,000원</div>
<div style="display: grid; gap: 10px; max-width: 360px; margin: 20px auto 0">
<a href="https://einenglish.com/study" style="display: flex; align-items: center; justify-content: center; min-height: 54px; border-radius: 27px; background: {CORAL}; border: 2px solid {INK}; color: #FFF; font-size: 18px; font-weight: 800; text-decoration: none">3회 수강신청하러 가기</a>
<a href="https://einenglish.com/apply/step1" style="display: flex; align-items: center; justify-content: center; min-height: 50px; border-radius: 25px; background: #FFF; border: 2px solid {INK}; color: {INK}; font-size: 16px; font-weight: 700; text-decoration: none">무료체험부터 해 볼게요</a>
</div>
</section>

</div>'''


BANNER = '<div style="max-width: 480px; margin: 0 auto 36px; padding: 0 clamp(20px, 5vw, 32px);"><img style="display: block; width: 100%; height: auto; border-radius: 16px;" src="{}banner.png" alt="신규회원 한정 · 25분 수업 3회 10,000원 · 1회당 약 3,300원"></div>\n'

open(os.path.join(HERE, 'body.html'), 'w').write(BANNER.format(CDN) + build(CDN))
open(os.path.join(HERE, 'preview.html'), 'w').write(f'''<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>887 미리보기</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css"></head>
<body style="margin:0;background:#fff"><div style="max-width:640px;margin:0 auto;padding:24px 0">
<div style="text-align:center;font-family:Pretendard,sans-serif"><div style="color:#666;font-size:15px">이벤트</div><h1 style="margin:10px 0 20px;font-size:30px;line-height:1.35">무료체험만으로는<br>결정하기 어려우셨나요?</h1></div>
{BANNER.format('')}{build('')}</div></body></html>''')
print('ok')
