"""3회 맛보기 수강권 이벤트(블로그 887번 글) 그림: 배너 + 본문 장면 2장.
사용법: cd tools/characters && python3 event887_images.py ../../event/887"""
import sys, os
from scene import *
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
F = "'Pretendard','Noto Sans CJK KR',sans-serif"

def confetti():
    dots = [(90,140,'#FFD966',16),(1000,120,'#A8E6CF',14),(150,520,'#FFFFFF',10),(960,500,'#FFD966',12),
            (60,860,'#A8E6CF',13),(1030,880,'#FFFFFF',11),(260,80,'#FFFFFF',9),(820,70,'#FFE7E1',15)]
    return ''.join(f'<div style="position:absolute;left:{x}px;top:{y}px;width:{s}px;height:{s}px;border-radius:50%;background:{c};border:3px solid {INK}"></div>' for x,y,c,s in dots)

banner = f'''<div style="position:absolute;inset:0;background:#EC6856;overflow:hidden">{confetti()}
<div style="position:absolute;left:0;right:0;top:92px;text-align:center;font-family:{F}">
  <div style="display:inline-block;background:#FFD966;border:4px solid {INK};border-radius:40px;padding:10px 30px;font:800 38px/1.2 {F};color:#2A211D">신규회원 한정</div>
  <div style="margin-top:30px;font:800 72px/1.18 {F};color:#fff;letter-spacing:-.01em">25분 수업 3회</div>
  <div style="margin-top:4px;font:900 176px/1 {F};color:#fff;letter-spacing:-.03em;-webkit-text-stroke:6px {INK};paint-order:stroke fill">10,000<span style="font-size:96px;-webkit-text-stroke:4px {INK}">원</span></div>
  <div style="margin-top:24px;font:700 40px/1.3 {F};color:#FFF6D6">1회당 약 3,300원 · 정규수업과 같은 방식</div>
</div>
<div style="position:absolute;left:0;right:0;bottom:-6px;display:flex;justify-content:center;align-items:flex-end;gap:70px">
  {ch('student-cheer',440)}<div style="margin-bottom:20px">{ch('turtle-cheer',430)}</div>
</div></div>'''

J = {}
J['banner.png'] = (1080, 1080, banner)
J['scene-hello.png'] = (900, 540, panel(row(
    col(bub('15분 체험으론<br>아직 잘 모르겠어요','w',42),ch('student-worry',270),gap=14),
    col(bub('3번 더 해 보고<br>정해도 돼요!','y',42),ch('turtle-point',270),gap=14,style='padding-bottom:24px'),
    gap=30, align='flex-end', style='position:absolute;bottom:-12px;left:0;right:0'), '#FFF6D6'))
J['scene-report.png'] = (720, 230, row(ch('turtle-paper',224), bub('수업이 끝나면<br>일일평가서가 와요!','w',40,'l'), gap=14))
render({f'{out}/{k}': v for k, v in J.items()})
