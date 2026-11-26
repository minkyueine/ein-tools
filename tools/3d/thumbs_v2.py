"""블로그 목록 썸네일(1080×1080) v2: 큰 글자 두 줄 + 큰 3D 오브젝트 하나. 캐릭터·작은 글씨 없음.
사용법: python3 tools/3d/thumbs_v2.py 출력폴더
이벤트 글은 event/<id>/thumb.png 로, 이용 가이드는 출력폴더/guide_<id>.png 로 저장한다."""
import sys, os
from playwright.sync_api import sync_playwright
HERE = os.path.dirname(os.path.abspath(__file__))
F = "'Noto Sans CJK KR',sans-serif"

def obj(path):
    return f'file://{HERE}/{path}.png'

def card(bg, glow, pill, head, big, sub, img, ink='#fff', big_color=None, pill_bg='rgba(0,0,0,.22)', pill_fg='#fff', img_h=560):
    big_color = big_color or ink
    return f"""<div style="position:absolute;inset:0;background:{bg};overflow:hidden;font-family:{F}">
<div style="position:absolute;right:-160px;bottom:-200px;width:820px;height:820px;border-radius:50%;background:{glow}"></div>
<div style="position:absolute;left:84px;top:110px;right:84px">
 <div style="font:800 88px/1.15 {F};color:{ink};letter-spacing:-.03em">{head}</div>
 <div class="fit" style="margin-top:14px;font:900 210px/1.02 {F};color:{big_color};letter-spacing:-.05em;white-space:nowrap">{big}</div>
</div>
<img src="{img}" style="position:absolute;right:56px;bottom:56px;max-height:{img_h}px;max-width:560px;filter:drop-shadow(0 26px 34px rgba(0,0,0,.22))">
</div>"""

EV = {
 '206': card('#3D7BF2', 'rgba(255,255,255,.16)', '카드 결제 부담 DOWN', '5만원 이상 결제 시', '무이자 할부', '최대 6개월까지<br>나눠 내세요', obj('props/c_prop-card'), big_color='#FFE066'),
 '887': card('#178F84', 'rgba(255,255,255,.14)', '신규회원 한정', '25분 수업 3회', '10,000원', '1회당 약 3,300원<br>정규수업과 같은 방식', obj('props/c_prop-star'), big_color='#FFE066', img_h=480),
 '207': card('#249E5C', 'rgba(255,255,255,.15)', '지인 추천 이벤트', '추천하면 둘 다', '5% + 5%', '추천한 분도<br>추천받은 분도', obj('props/c_prop-coins'), big_color='#FFE066', img_h=500),
 '205': card('#FFC531', 'rgba(255,255,255,.35)', '체험 후기 이벤트', '무료체험 후기 쓰면', '3,000원', '바로 적립해 드려요', obj('props/c_prop-bubble'), ink='#2A211D', big_color='#E5482F', pill_bg='#2A211D', img_h=440),
 '199': card('#6A55E0', 'rgba(255,255,255,.14)', '수강후기 이벤트', '베스트 후기는', '최대 2만원', '선정되면<br>적립금으로 드려요', obj('props/c_prop-star'), big_color='#FFE066', img_h=480),
 '203': card('#1FAE5E', 'rgba(255,255,255,.15)', '재수강 회원 전용', '네이버 스토어 3만원 결제', '4만원 적립', '매달 1만원 더', obj('props/c_prop-bag'), big_color='#FFE066', img_h=520),
 '211': card('#EC5A45', 'rgba(255,255,255,.16)', '신규회원 전용', '첫 결제하면', '5% 적립', '1·3·6개월 수강권<br>주 2회 이상', obj('props/c_prop-gift'), big_color='#FFE066', img_h=520),
}
GD = {
 '874': card('#E2557A', 'rgba(255,255,255,.16)', '영상 가이드', '줌 연락처', '수락·추가', 'PC · 휴대폰<br>영상으로 따라 하기', obj('icons/video'), img_h=440),
 '794': card('#4C8DF6', 'rgba(255,255,255,.16)', '첫 수업 준비', '선생님과 Zoom 연결', '연락처 수락', '요청이 없으면<br>직접 추가하기', obj('icons/contact'), img_h=540),
 '448': card('#FFC531', 'rgba(255,255,255,.35)', '첫 수업 준비', 'Zoom 설치·가입·로그인', '3단계', '처음이어도<br>순서대로 따라 하기', obj('icons/steps'), ink='#2A211D', big_color='#2A211D', pill_bg='#2A211D', img_h=500),
 '606': card('#119BBE', 'rgba(255,255,255,.15)', '무료체험', '무료체험 수업', '입장 방법', '5분 전 알림부터<br>5단계로 정리', obj('icons/enter'), big_color='#FFE066', img_h=420),
 '250': card('#22304F', 'rgba(255,255,255,.08)', 'Zoom 활용', 'Zoom 수업', '녹화하기', 'PC · 태블릿 · 휴대폰<br>기기별 방법', obj('icons/record'), big_color='#FF7A66', img_h=400),
 '91':  card('#FF8A3D', 'rgba(255,255,255,.18)', '수강신청', '선생님·시간', '직접 고르기', '두 가지 방법으로<br>수강신청하기', obj('icons/calendar'), img_h=460),
}

FIT = "for(const e of document.querySelectorAll('.fit')){let s=parseFloat(getComputedStyle(e).fontSize);while(e.scrollWidth>e.parentElement.clientWidth&&s>80){s-=4;e.style.fontSize=s+'px'}}"

def render(jobs):
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/usr/bin/google-chrome')
        for path, html in jobs:
            open('/tmp/v2.html', 'w').write(f'<html><body style="margin:0;width:1080px;height:1080px;position:relative;overflow:hidden">{html}</body></html>')
            pg = b.new_page(viewport={'width': 1080, 'height': 1080}); pg.goto('file:///tmp/v2.html'); pg.wait_for_timeout(300)
            pg.evaluate(FIT); pg.screenshot(path=path); pg.close(); print(path)
        b.close()

if __name__ == '__main__':
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    render([(f'{out}/event_{k}.png', v) for k, v in EV.items()] + [(f'{out}/guide_{k}.png', v) for k, v in GD.items()])
