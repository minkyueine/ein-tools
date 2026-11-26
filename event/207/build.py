"""207번 글(지인 추천 5%+5%) 본문. python3 build.py → post.html, preview.html"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.dirname(HERE))
from kit import *
CDN = 'https://minkyueine.github.io/ein-tools/event/207/'
KAKAO = 'https://pf.kakao.com/_TpqVu'
PRICES = [('1개월', 94000), ('3개월', 262300), ('6개월', 485000)]  # 주 2회 25분 정가


def build(b):
    ex = table(['주 2회 수강권', '추천받은 분', '추천한 분'],
               [[f'{n}<br><span style="font-size: 13px; font-weight: 600; color: #9A8F8A">{v:,}원</span>', f'<b style="color: {DEEP}">{round(v*.05):,}원</b>', f'<b style="color: {DEEP}">{round(v*.05):,}원</b>'] for n, v in PRICES], '36%')
    return wrap(
        section(intro(f'아인잉글리쉬를 지인에게 소개해 주세요.<br>지인이 첫 정규수업을 등록하면<br><b style="color: {DEEP}">추천한 분도, 추천받은 분도 5%씩</b> 적립해 드려요.')
                + img(b + 'scene-hello.png', '친구한테 아인 추천했어요! / 두 분 다 5%씩 적립해 드려요!', top=24), top=8)
        + section(h2(1, '누가 얼마나 받나요?') + grid(
            card('🙋', '#FDE3DC', '추천한 분 (수강생)', '추천받은 분 결제 금액의 5%'),
            card('🤝', '#E6F6EE', '추천받은 분 (첫 정규 수강)', '본인 결제 금액의 5%'),
            card('♾️', '#FFF6D6', '추천 횟수', '제한 없어요' + sub('여러 명을 추천하면 그만큼 계속 적립돼요.'))))
        + section(h2(2, '이만큼 받아요') + p('주 2회 25분 수업, 정가 기준 예시예요. 실제로는 최종 결제 금액의 5%가 적립돼요.') + ex)
        + section(h2(3, '이렇게 참여해요') + grid(
            step(1, '추천받은 분이 수강 결제', '1·3·6개월, 주 2회 이상 수강권'),
            step(2, '카카오톡으로 알려 주세요', '추천한 분과 추천받은 분의 <b>성함·휴대폰 번호</b>'),
            step(3, '확인 후 두 분 모두 적립', '적립금은 다음 수강 때 바로 쓸 수 있어요.'), gap=10)
            + f'<div style="margin-top: 14px; padding: 14px 16px; background: #FDE3DC; border-radius: 14px; font-size: 16px; font-weight: 700; line-height: 1.55; color: {DEEP}">⏰ 적립은 추천받은 분의 <b>첫 수업이 시작되기 전까지</b>만 가능해요.</div>')
        + section(h2('', '🙋 이런 분께 좋아요') + grid(
            check('가족·친구와 함께 영어 공부를 시작하고 싶은 분'),
            check('주변에 영어 회화를 고민하는 지인이 있는 분'),
            check('혜택을 서로 나눠 받고 싶은 분'), gap=10))
        + section(notes('📌 꼭 확인하세요', [
            '추천받은 분의 <b>첫 정규 수강</b>에만 적용돼요.',
            '<b>주 2회 이상, 1·3·6개월 수강권</b> 결제 시 적용돼요. (주 1회 제외)',
            '결제 후 카카오톡으로 알려 주셔야 적립돼요. 첫 수업이 시작된 뒤에는 적립할 수 없어요.']))
        + cta('함께 하면 혜택도 두 배 🤝', '결제 후 카카오톡으로 성함과 번호만 남겨 주세요.', (KAKAO, '카카오톡으로 추천 알리기'), ('https://einenglish.com/study', '수강신청하러 가기')))


write(HERE, CDN, ['[진행중] 지인 추천하면', '두 사람 모두 5% 적립!'], '지인 추천 이벤트 · 추천하면 둘 다 5% 적립 · 추천한 분도 추천받은 분도', build)
print('ok')
