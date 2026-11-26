"""월 이벤트(공지 130번) 본문 HTML. python3 build.py → post.html(사이트용), preview.html(미리보기)
매달 바꿀 곳: MONTH, CARD_LINK(그 달 카드사 무이자 글)"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
MONTH = 11
CARD_LINK = 'https://einenglish.com/cscenter/blog/detail/206'
CDN = 'https://minkyueine.github.io/ein-tools/event/130/'
INK = '#2A211D'; CORAL = '#EC6856'; DEEP = '#C4452F'
PAD = 'clamp(20px, 5vw, 32px)'
GROUPS = {'new': ('🌱', '신규 회원', '#FDE3DC'), 're': ('🔁', '재수강 회원', '#FFF6D6'),
          'ref': ('🤝', '친구 추천', '#E6F6EE'), 'everyone': ('🙌', '누구나', '#E3EDFF')}

def btn(href, text, primary=False):
    if primary:
        return f'<a href="{href}" style="display: flex; align-items: center; justify-content: center; min-height: 50px; margin-top: 16px; border-radius: 25px; background: {CORAL}; border: 2px solid {INK}; color: #FFF; font-size: 16px; font-weight: 800; text-decoration: none">{text}</a>'
    return f'<a href="{href}" style="display: flex; align-items: center; justify-content: center; min-height: 48px; margin-top: 16px; border-radius: 24px; background: #FFF; border: 2px solid {INK}; color: {INK}; font-size: 16px; font-weight: 700; text-decoration: none">{text}</a>'

def note(items):
    lis = ''.join(f'<li style="position: relative; padding-left: 16px; margin-top: 6px"><span style="position: absolute; left: 2px; top: 10px; width: 5px; height: 5px; border-radius: 50%; background: #9A8F8A"></span>{t}</li>' for t in items)
    return f'<ul style="margin: 14px 0 0; padding: 12px 16px 14px; list-style: none; background: #F7F7F7; border-radius: 12px; font-size: 14px; line-height: 1.55; color: #555">{lis}</ul>'

def benefit(no, title, big, body, extra=''):
    return f'''<div style="margin-top: 16px; padding: 22px 20px; background: #FFF; border: 2px solid {INK}; border-radius: 20px">
<div style="display: flex; align-items: center; gap: 10px"><span style="flex: none; display: inline-flex; align-items: center; justify-content: center; width: 30px; height: 30px; border-radius: 50%; background: {CORAL}; color: #FFF; font-size: 16px; font-weight: 800">{no}</span><span style="font-size: 19px; font-weight: 800; line-height: 1.35; color: {INK}">{title}</span></div>
<div style="margin-top: 12px; font-size: 26px; font-weight: 900; line-height: 1.3; color: {DEEP}">{big}</div>
<p style="margin: 8px 0 0; font-size: 16px; line-height: 1.65; color: #444">{body}</p>{extra}</div>'''

def group(key, inner):
    e, name, bg = GROUPS[key]
    return f'''<section id="{key}" style="scroll-margin-top: 140px; margin-top: 40px; padding: 28px {PAD} 30px; background: {bg}">
<h2 style="margin: 0; font-size: 24px; line-height: 1.35; font-weight: 800; color: {INK}">{e} {name} 혜택</h2>
{inner}</section>'''

def img(src, alt, maxw='100%', top=18):
    return f'<div style="margin-top: {top}px"><img src="{src}" alt="{alt}" style="display: block; width: 100%; max-width: {maxw}; height: auto"></div>'

def build(base):
    pills = ''.join(f'<a href="#{k}" style="display: inline-flex; align-items: center; gap: 6px; min-height: 44px; padding: 0 16px; border-radius: 22px; background: {bg}; border: 2px solid {INK}; color: {INK}; font-size: 16px; font-weight: 700; text-decoration: none">{e} {n}</a>' for k, (e, n, bg) in GROUPS.items())
    summary_rows = [('1', '무료체험 후기 작성', '3,000원 적립', 'new'), ('2', '첫 결제', '결제 금액 5% 적립', 'new'),
                    ('3', '네이버 스토어 이벤트', '3만원 → 4만원 적립', 're'), ('4', '친구 추천', '두 사람 각 5% 적립', 'ref'),
                    ('5', '장기·집중 수강', '회당 최대 46.2% 할인', 'everyone'), ('6', '수강후기 작성', '베스트 후기 적립금', 'everyone'),
                    ('7', '카드 결제', '무이자 할부', 'everyone')]
    summary = ''.join(f'<a href="#{g}" style="display: flex; align-items: center; gap: 12px; padding: 13px 4px; border-top: 1px solid #EFE6E2; color: {INK}; text-decoration: none"><span style="flex: none; width: 26px; height: 26px; border-radius: 50%; background: {GROUPS[g][2]}; border: 1.5px solid {INK}; display: inline-flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 800">{n}</span><span style="flex: 1; font-size: 16px; font-weight: 700">{t}</span><span style="flex: none; font-size: 15px; font-weight: 800; color: {DEEP}">{v}</span></a>' for n, t, v, g in summary_rows)

    new = benefit(1, '무료체험 후기 작성', '3,000원 적립',
        '첫 무료체험 후 후기를 남겨 주시면, 수강신청에 바로 쓰실 수 있는 적립금 3,000원을 드려요.',
        note(['무료체험일을 포함해 <b>7일 이내</b>에 작성하셔야 적립돼요.', '기간이 지나면 적립되지 않고, 1회만 드려요.']))
    new += benefit(2, '첫 결제 5% 적립', '결제 금액의 5%',
        '1·3·6개월 수강권을 <b>처음 결제</b>하시면, 수업 배정과 함께 결제 금액의 5%를 바로 적립해 드려요.',
        note(['주 2회 이상 수강권에 적용돼요. (주 1회 제외)', '다음 재수강 때 결제 금액의 30%까지 사용할 수 있어요.']) + btn('https://einenglish.com/cscenter/blog/detail/211', '얼마나 받는지 금액표 보기 →'))

    re = img(base + 'scene-store.png', '3만원 내고 4만원 받기!', '360px')
    re += benefit(3, '네이버 스토어 이벤트', '3만원 결제 → 4만원 적립',
        '네이버 스마트스토어에서 3만원을 결제하시면, 아인잉글리쉬 적립금 <b>4만원</b>을 드려요. 1만원을 더 받고 다음 수강에 쓰세요.',
        note(['재수강 회원만 참여할 수 있어요.']) + btn('https://smartstore.naver.com/einenglish/products/8912013180', '네이버 스토어에서 보기 →'))

    ref = img(base + 'scene-friend.png', '친구랑 같이 시작할래요! 두 분 다 5%씩 적립해 드려요!')
    ref += benefit(4, '친구 추천', '두 사람 모두 5%씩',
        '수강생(지금 또는 예전 수강생)이 지인을 추천해 그 지인이 첫 정규수업을 등록하면, <b>추천한 분</b>은 신규 결제 금액의 5%, <b>추천받은 분</b>은 최종 결제 금액의 5%를 적립해 드려요. 가족·친구와 함께 신규 신청하셔도 같아요.',
        note(['주 2회 이상, 1·3·6개월 수강권에 적용돼요.', '결제(입금 완료) 후 <b>카카오톡으로 성함과 휴대폰 번호</b>를 남겨 주세요.', '<b>첫 수업 시작 전까지</b> 알려 주셔야 적립할 수 있어요.']))

    al = benefit(5, '길게, 자주 할수록', '회당 최대 46.2% 할인',
        '주 1회 1개월은 회당 13,500원, 주 5회 6개월은 회당 7,267원이에요. 결제 단계에서 할인이 자동으로 적용돼요.',
        note(['같은 주 횟수라면 6개월이 1개월보다 회당 최대 14% 저렴해요.']) + btn('https://einenglish.com/study/tuition', '수강료 전체 보기 →'))
    al += benefit(6, '수강후기 작성', '베스트 후기 적립금',
        '수업 후기를 남겨 주시면 베스트 후기로 뽑힌 분께 적립금을 드려요. 네이버 스토어 후기도 함께 참여돼요.',
        btn('https://einenglish.com/cscenter/blog/detail/199', '수강후기 적립 알아보기 →'))
    al += benefit(7, '카드 무이자 할부', '언제나 무이자 할부',
        '카드사별 무이자 할부로 부담 없이 결제하세요. 결제 전에 카드사 조건을 꼭 확인해 주세요.',
        btn(CARD_LINK, f'{MONTH}월 카드사별 무이자 혜택 보기 →'))

    return f'''<div style="max-width: 640px; margin: 0 auto; font-family: Pretendard, 'Noto Sans KR', sans-serif; color: #333; font-size: 16px; line-height: 1.6; word-break: keep-all">

<div style="max-width: 480px; margin: 0 auto; padding: 0 {PAD}"><img src="{base}banner.png" alt="이번 달 이벤트 · 아인잉글리쉬 혜택 7가지 · 신규, 재수강, 친구 추천, 누구나" style="display: block; width: 100%; height: auto; border-radius: 16px"></div>

<section style="padding: 32px {PAD} 0; text-align: center">
<p style="margin: 0; font-size: 18px; line-height: 1.7; color: {INK}">영어, 결심한 지금이 가장 좋은 때예요.<br>나에게 맞는 혜택부터 확인해 보세요.</p>
<div style="display: inline-block; margin-top: 16px; padding: 8px 16px; border-radius: 10px; background: #FDE3DC; font-size: 15px; font-weight: 800; color: {DEEP}">📅 {MONTH}월 이벤트 혜택은 {MONTH}월에 결제하신 분께만 적용돼요</div>
</section>

<section style="padding: 32px {PAD} 0">
<div style="font-size: 18px; font-weight: 800; color: {INK}">나는 누구인가요?</div>
<div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px">{pills}</div>
<div style="margin-top: 24px; padding: 6px 16px 4px; border: 2px solid {INK}; border-radius: 18px">
<div style="padding: 10px 4px; font-size: 15px; font-weight: 800; color: #7A6F6A">혜택 한눈에 보기</div>
{summary}</div>
</section>

{group('new', new)}
{group('re', re)}
{group('ref', ref)}
{group('everyone', al)}

<section style="padding: 40px {PAD} 44px; text-align: center">
<div style="font-size: 22px; font-weight: 800; line-height: 1.45; color: {INK}">25분, 오늘부터 시작해 보세요 🙌</div>
<p style="margin: 8px 0 0; font-size: 16px; color: #666">무료체험으로 먼저 수업을 경험해 볼 수 있어요.</p>
<div style="max-width: 360px; margin: 6px auto 0">
{btn('https://einenglish.com/apply/step1', '무료체험 신청하기', True)}
{btn('https://einenglish.com/study', '바로 수강신청하기')}
</div></section>

</div>'''

open(os.path.join(HERE, 'post.html'), 'w').write(build(CDN))
open(os.path.join(HERE, 'preview.html'), 'w').write(f'<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body style="margin:0"><div style="max-width:640px;margin:0 auto;padding:24px 0"><h1 style="text-align:center;font-family:sans-serif;font-size:26px;margin:0 0 24px">[이벤트] 2026년 {MONTH}월 이벤트</h1>{build("")}</div></body></html>')
print('ok')
