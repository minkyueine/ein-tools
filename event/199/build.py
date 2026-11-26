"""199번 글(정규수업 수강후기 적립) 본문. python3 build.py → post.html, preview.html"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.dirname(HERE))
from kit import *
CDN = 'https://minkyueine.github.io/ein-tools/event/199/'
WRITE = 'https://einenglish.com/mypage/lecture/review'


def build(b):
    pts = table(['후기 종류', '적립금'], [
        ['🏆 베스트 후기 선정', f'<b style="font-size: 18px; color: {DEEP}">20,000원</b>'],
        ['600자 이상', f'<b style="color: {DEEP}">4,000원</b>'],
        ['300자 이상', f'<b style="color: {DEEP}">1,000원</b>'],
        ['100자 ~ 300자', f'<b style="color: {DEEP}">500원</b>'],
        ['📸 수업 사진 첨부', f'<b style="color: {DEEP}">+1,000원</b>']], '55%')
    return wrap(
        section(intro(f'수업을 들으며 달라진 점을 후기로 남겨 주세요.<br>글자 수에 따라 적립금을 드리고,<br><b style="color: {DEEP}">베스트 후기는 20,000원</b>을 드려요.')
                + img(b + 'scene-hello.png', '선생님 덕분에 말이 늘었어요! / 그 이야기를 후기로 남겨 주세요!', top=24), top=8)
        + section(h2(1, '이만큼 적립해 드려요') + pts
                  + p('수업 사진은 본인이 즐겁게 수업하는 모습이 담긴 사진이어야 해요. 글 캡처 화면은 해당되지 않아요.', top=10, size=14, color='#888'))
        + section(h2(2, '이렇게 참여해요') + grid(
            step(1, '홈페이지 로그인', ''),
            step(2, '마이페이지 → 후기관리에서 작성', '마지막 수업일을 포함해 7일 안에 써 주세요.'),
            step(3, '확인 후 포인트 적립', '다음 수강신청 때 바로 쓸 수 있어요.'), gap=10)
            + link_btn(WRITE, '✍️ 후기 작성하러 가기 →'))
        + section(h2(3, '이런 후기가 큰 도움이 돼요') + grid(
            card('👩‍🏫', '#FDE3DC', '', '담당 선생님 이름과 추천하는 이유'),
            card('💬', '#FFF6D6', '', '수업 전과 후, 달라진 점'),
            card('📝', '#E6F6EE', '', '일일평가서·교재 등 도움이 된 점'))
            + p('영어 말하기가 두려워 시작을 망설이는 분들께 여러분의 후기가 큰 용기가 돼요.', top=14, size=15, color='#555'))
        + section(notes('📌 꼭 확인하세요', [
            '후기 적립은 <b>한 달에 1번</b>이에요.',
            '후기를 연달아 올리면 1개만 정상 적립되고, 나머지는 500원씩 적립돼요.',
            '같은 내용을 반복해서 쓰면 1개만 적립되고, 나머지는 적립되지 않아요.',
            '후기는 홈페이지에서, <b>마지막 수업일을 포함해 7일 안</b>에 써 주세요.',
            '적립 금액은 달마다 바뀔 수 있어요. 지인 추천 이벤트는 이번 달 이벤트 안내를 확인해 주세요.',
            '비방이나 욕설이 담긴 후기는 삭제되고, 탈퇴 처리될 수 있어요.'],
            extra=f'<div style="margin-top: 16px"><a href="https://einenglish.com/cscenter/detail/130" style="color: {DEEP}; font-size: 16px; font-weight: 800; text-decoration: underline; text-underline-offset: 4px">이번 달 전체 이벤트 보기 →</a></div>'))
        + cta('여러분의 이야기를 들려주세요 ✍️', '베스트 후기로 뽑히면 20,000원을 드려요.', (WRITE, '후기 작성하러 가기'), ('https://einenglish.com/review', '다른 수강생 후기 보기')))


write(HERE, CDN, ['[진행중] 수강후기 쓰고', '최대 2만원 적립받기!'], '수강후기 이벤트 · 후기 쓰고 포인트 받기 · 베스트 후기 선정 시 20,000원', build)
print('ok')
