"""이벤트 글 206·207·205·203·199 그림: 글마다 배너 1장 + 장면 1장.
사용법: cd tools/characters && python3 events_more_images.py ../../event"""
import sys, os
from scene import *
root = sys.argv[1]
F = "'Pretendard','Noto Sans CJK KR',sans-serif"


def confetti():
    dots = [(90,140,'#FFD966',16),(1000,120,'#A8E6CF',14),(150,520,'#FFFFFF',10),(960,500,'#FFD966',12),
            (60,860,'#A8E6CF',13),(1030,880,'#FFFFFF',11),(260,80,'#FFFFFF',9),(820,70,'#FFE7E1',15)]
    return ''.join(f'<div style="position:absolute;left:{x}px;top:{y}px;width:{s}px;height:{s}px;border-radius:50%;background:{c};border:3px solid {INK}"></div>' for x,y,c,s in dots)


def banner(tag, line1, big, big_size, sub, left, right):
    l1 = f'<div style="margin-top:30px;font:800 68px/1.18 {F};color:#fff;letter-spacing:-.01em">{line1}</div>' if line1 else '<div style="height:24px"></div>'
    return f'''<div style="position:absolute;inset:0;background:#EC6856;overflow:hidden">{confetti()}
<div style="position:absolute;left:0;right:0;top:86px;text-align:center;font-family:{F}">
  <div style="display:inline-block;background:#FFD966;border:4px solid {INK};border-radius:40px;padding:10px 30px;font:800 38px/1.2 {F};color:#2A211D">{tag}</div>
  {l1}
  <div style="margin-top:6px;font:900 {big_size}px/1.05 {F};color:#fff;letter-spacing:-.03em;-webkit-text-stroke:6px {INK};paint-order:stroke fill;white-space:nowrap">{big}</div>
  <div style="margin-top:24px;font:700 40px/1.3 {F};color:#FFF6D6">{sub}</div>
</div>
<div style="position:absolute;left:0;right:0;bottom:-6px;display:flex;justify-content:center;align-items:flex-end;gap:70px">
  {ch(left,400)}<div style="margin-bottom:20px">{ch(right,390)}</div>
</div></div>'''


def duo(left_text, left_ch, right_text, right_ch, bg='#FFF6D6', lc='w', rc='y'):
    return (900, 540, panel(row(
        col(bub(left_text, lc, 42), ch(left_ch, 270), gap=14),
        col(bub(right_text, rc, 42), ch(right_ch, 270), gap=14, style='padding-bottom:24px'),
        gap=30, align='flex-end', style='position:absolute;bottom:-12px;left:0;right:0'), bg))


def solo(name, text, w=720):
    return (w, 230, row(ch(name, 224), bub(text, 'w', 40, 'l'), gap=14))


small = '<span style="font-size:110px;-webkit-text-stroke:4px #4A3A34">'
J = {
  '206': {
    'banner.png': (1080, 1080, banner('카드 결제 부담 DOWN', '언제나', '무이자 할부', 150, '5만원 이상 · 신청 없이 자동 적용', 'student-cheer', 'turtle-cheer')),
    'scene-hello.png': duo('한 번에 결제하기<br>부담돼요', 'student-worry', '카드 무이자 할부로<br>나눠 내세요!', 'turtle-point'),
  },
  '207': {
    'banner.png': (1080, 1080, banner('지인 추천 이벤트', '추천하면 둘 다', f'5%{small} 적립</span>', 190, '추천한 분도 · 추천받은 분도', 'student-cheer', 'turtle-cheer')),
    'scene-hello.png': duo('친구한테 아인<br>추천했어요!', 'student-smile', '두 분 다 5%씩<br>적립해 드려요!', 'turtle-point'),
  },
  '205': {
    'banner.png': (1080, 1080, banner('신규 회원 응원 선물', '무료체험 후기 쓰면', f'3,000{small}원</span>', 190, '수강신청할 때 바로 사용', 'student-cheer', 'turtle-cheer')),
    'scene-hello.png': duo('체험 후기<br>남겼어요!', 'student-book', '3,000원<br>적립해 드릴게요!', 'turtle-paper'),
  },
  '203': {
    'banner.png': (1080, 1080, banner('재수강 회원 전용', '네이버 스토어에서', f'3만→4만{small}원</span>', 150, '3만원 구매하면 4만원 적립', 'student-cheer', 'turtle-cheer')),
    'scene-hello.png': duo('다음 달도<br>계속 들을래요!', 'student-smile', '네이버에서 3만원 내면<br>4만원 적립!', 'turtle-point'),
  },
  '199': {
    'banner.png': (1080, 1080, banner('수강후기 이벤트', '후기 쓰고 포인트 받기', f'최대 2만{small}원</span>', 170, '베스트 후기 선정 시 20,000원', 'student-cheer', 'turtle-cheer')),
    'scene-hello.png': duo('선생님 덕분에<br>말이 늘었어요!', 'student-book', '그 이야기를<br>후기로 남겨 주세요!', 'turtle-paper'),
  },
}
jobs = {}
for pid, files in J.items():
    os.makedirs(f'{root}/{pid}', exist_ok=True)
    for name, job in files.items():
        jobs[f'{root}/{pid}/{name}'] = job
render(jobs)
print('ok', len(jobs))
