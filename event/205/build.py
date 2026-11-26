"""205번 글(무료체험 후기 3,000원) 본문. python3 build.py → post.html, preview.html"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.dirname(HERE))
from kit import *
CDN = 'https://minkyueine.github.io/ein-tools/event/205/'
KAKAO = 'https://pf.kakao.com/_TpqVu'


def build(b):
    return wrap(
        section(intro(f'무료체험은 어떠셨나요?<br>느낀 점을 <b style="color: {INK}">짧은 후기</b>로 남겨 주시면<br><b style="color: {DEEP}">적립금 3,000원</b>을 드려요.')
                + img(b + 'scene-hello.png', '체험 후기 남겼어요! / 3,000원 적립해 드릴게요!', top=24), top=8)
        + section(h2(1, '이렇게 받아요') + grid(
            step(1, '무료체험 수업 듣기', '15분 · 레벨테스트와 함께 진행돼요'),
            step(2, '7일 안에 체험 후기 남기기', '길지 않아도 괜찮아요. 느낀 그대로 적어 주세요.'),
            step(3, '3,000원 적립', '수강신청할 때 바로 쓸 수 있어요.'), gap=10))
        + section(h2(2, '후기에 이런 걸 적어 주세요') + grid(
            card('👩‍🏫', '#FDE3DC', '', '선생님과 수업 분위기는 어땠는지'),
            card('✏️', '#FFF6D6', '', '틀린 문장을 어떻게 고쳐 줬는지'),
            card('📊', '#E6F6EE', '', '레벨테스트 결과를 보고 느낀 점')))
        + section(h2('', '🙋 이런 분께 추천해요') + grid(
            check('무료체험 후 수강을 고민하고 있는 분'),
            check('첫 수강료를 조금이라도 아끼고 싶은 분'),
            check('체험해 보고 느낀 점을 솔직하게 나누고 싶은 분'), gap=10))
        + section(notes('📌 꼭 확인하세요', [
            '<b>첫 무료체험일로부터 7일 안</b>에 작성한 후기만 적립돼요.',
            '무료체험은 <b>1인 1회</b>만 제공돼요. 공정한 체험 기회를 위해 반복 신청이나 추가 체험은 어려워요.',
            '적립금은 수강신청 결제 때 바로 사용할 수 있어요.'],
            extra=p(f'💬 궁금한 점은 카카오톡 채널 <b>아인화상영어</b>로 물어봐 주세요.<br>상담 시간: 평일 11:00~18:00 (점심 12:30~14:00, 공휴일 제외)', top=14, size=15, color='#555')))
        + cta('체험하고, 후기 쓰고, 3,000원 받기 🎁', '첫 수강을 더 가볍게 시작하세요.', ('https://einenglish.com/apply/step1', '무료체험 신청하기'), (KAKAO, '카카오톡으로 문의하기')))


write(HERE, CDN, ['[진행중] 무료체험 후기 쓰고', '3,000원 적립받기!'], '신규 회원 응원 선물 · 무료체험 후기 쓰면 3,000원 · 수강신청할 때 바로 사용', build)
print('ok')
