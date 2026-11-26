"""203번 글(네이버 스토어 재수강 3만→4만 적립) 본문. python3 build.py → post.html, preview.html"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.dirname(HERE))
from kit import *
CDN = 'https://minkyueine.github.io/ein-tools/event/203/'
STORE = 'https://smartstore.naver.com/einenglish/products/8912013180'
KAKAO = 'https://pf.kakao.com/_TpqVu'
EXAMPLE = 'https://einenglish.sgp1.cdn.digitaloceanspaces.com/prod/202601/1769779305147'


def build(b):
    return wrap(
        section(intro(f'다시 수강하시는 회원님께 드리는 혜택이에요.<br>네이버 스토어에서 <b style="color: {INK}">3만원 수강권</b>을 사시면<br><b style="color: {DEEP}">4만원을 적립금</b>으로 드려요.')
                + img(b + 'scene-hello.png', '다음 달도 계속 들을래요! / 네이버에서 3만원 내면 4만원 적립!', top=24), top=8)
        + section(h2(1, '혜택 한눈에 보기') + grid(
            card('🎁', '#FDE3DC', '혜택', '3만원 결제 → 4만원 적립' + sub('1만원을 더 받아 홈페이지 수강신청 때 현금처럼 써요.')),
            card('🔁', '#FFF6D6', '참여 횟수', '매달 1번씩 참여할 수 있어요' + sub('마지막 적립일로부터 30일이 지나면 다시 구매할 수 있어요.')),
            card('📅', '#E6F6EE', '기간', '종료 공지 전까지 계속 진행해요')))
        + section(h2(2, '누가 참여할 수 있나요?') + grid(
            check('지금 수강 중이거나, 예전에 수강한 <b>재수강 회원</b>'),
            check('홈페이지에서 정규수업을 <b>직접 신청</b>한 회원'), gap=10)
            + f'<div style="margin-top: 12px; padding: 14px 16px; background: #FDE3DC; border-radius: 14px; font-size: 16px; font-weight: 700; line-height: 1.55; color: {DEEP}">신규 회원은 참여할 수 없어요. 구매하시면 자동으로 결제가 취소돼요.<br><span style="font-weight: 600; color: #555">신규 회원은 첫 결제 5% 적립 등 다른 이벤트를 이용해 주세요.</span></div>')
        + section(h2(3, '이렇게 참여해요') + grid(
            step(1, "네이버 스토어에서 '3만원 수강권' 구매", ''),
            step(2, '구매 영수증을 카카오톡으로 보내기', '발송 처리를 요청해 주세요.'),
            step(3, '발송 처리 후 상품 리뷰 작성', ''),
            step(4, '리뷰 작성 후 적립 요청', '확인 후 홈페이지에 4만원이 적립돼요.'), gap=10)
            + f'<div style="margin-top: 20px; text-align: center"><img src="{EXAMPLE}" alt="네이버 스토어 구매 화면 예시" style="display: inline-block; width: 100%; max-width: 280px; height: auto; border: 2px solid {INK}; border-radius: 14px"></div>'
            + p('구매 화면 예시예요. 실제 화면과 조금 다를 수 있어요.', top=8, size=14, color='#9A8F8A', center=True)
            + link_btn(STORE, '🛒 네이버 스토어 바로가기 →'))
        + section(h2(4, '매달 1만원 더 받는 법') + f'''<div style="margin-top: 16px; padding: 20px; background: #E3EDFF; border-radius: 18px; font-size: 17px; line-height: 1.6; color: {INK}">
한 달에 한 장씩 구매하고 적립받으세요.<br><b style="color: #2F5FC4">마지막 구매일(적립일) + 30일</b> 이후에 다시 살 수 있어요.
<div style="margin-top: 8px; font-size: 15px; color: #555">예) 4월 13일에 적립받았다면 → 5월 14일부터 구매 가능</div></div>'''
            + p('30일이 지나기 전에 다시 구매하면 자동으로 취소돼요.', top=10, size=15, color=DEEP))
        + section(notes('📌 꼭 확인하세요', [
            '적립금은 언제든 현금처럼 쓸 수 있고, <b>전체 수업료의 최대 30%</b>까지 사용할 수 있어요.',
            '네이버 스토어 수강권은 <b>부분 환불이 안 돼요.</b> 중도 환불 시에는 추가로 적립된 금액을 빼고 환불돼요.',
            '환불 이력이 있는 수강생은 참여할 수 없어요.',
            '구매 후 <b>2일 안에</b> 영수증을 보내지 않거나 리뷰를 쓰지 않으면 자동으로 취소돼요.',
            '작성한 리뷰는 홈페이지 수강후기로 등록될 수 있어요. 원치 않으시면 참여가 어려워요. 베스트 후기로 뽑히면 추가 적립금을 드려요.',
            '이벤트 내용은 사전 공지 없이 바뀔 수 있어요.'],
            extra=p('참여는 자유예요. 원치 않으시면 홈페이지에서 바로 재수강 신청을 하시면 돼요.', top=14, size=15, color='#555')))
        + cta('다음 달 수강, 1만원 더 받고 시작하세요 🎁', '구매 후 영수증은 카카오톡으로 보내 주세요.', (STORE, '네이버 스토어에서 구매하기'), (KAKAO, '카카오톡으로 영수증 보내기')))


write(HERE, CDN, ['[진행중] 네이버 스토어 재수강', '매달 1만원 더 적립!'], '재수강 회원 전용 · 네이버 스토어에서 3만원 구매하면 4만원 적립', build)
print('ok')
