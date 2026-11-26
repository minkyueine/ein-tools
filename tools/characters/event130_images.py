"""월 이벤트(공지 130번) 그림: 배너 + 장면 2장. 달이 바뀌어도 그대로 쓰도록 월 표기는 넣지 않는다.
사용법: cd tools/characters && python3 event130_images.py ../../event/130"""
import sys, os
from scene import *
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
F = "'Pretendard','Noto Sans CJK KR',sans-serif"

def dots():
    d = [(90,150,'#FFD966',16),(990,130,'#A8E6CF',14),(150,560,'#FFFFFF',10),(960,560,'#FFD966',12),
         (60,880,'#A8E6CF',13),(1030,900,'#FFFFFF',11),(270,90,'#FFFFFF',9),(810,80,'#FFE7E1',15)]
    return ''.join(f'<div style="position:absolute;left:{x}px;top:{y}px;width:{s}px;height:{s}px;border-radius:50%;background:{c};border:3px solid {INK}"></div>' for x,y,c,s in d)

def chip(t, bg):
    return f'<div style="background:{bg};border:4px solid {INK};border-radius:40px;padding:8px 24px;font:800 34px/1.2 {F};color:#2A211D">{t}</div>'

banner = f'''<div style="position:absolute;inset:0;background:#EC6856;overflow:hidden">{dots()}
<div style="position:absolute;left:0;right:0;top:70px;text-align:center">
  <div style="display:inline-block;background:#FFD966;border:4px solid {INK};border-radius:40px;padding:10px 30px;font:800 38px/1.2 {F};color:#2A211D">이번 달 이벤트</div>
  <div style="margin-top:30px;font:800 74px/1.18 {F};color:#fff">아인잉글리쉬</div>
  <div style="margin-top:4px;font:900 150px/1.05 {F};color:#fff;-webkit-text-stroke:5px {INK};paint-order:stroke fill">혜택 7가지</div>
  <div style="display:flex;justify-content:center;gap:14px;margin-top:30px">{chip('신규','#FFFFFF')}{chip('재수강','#FFF6D6')}{chip('친구 추천','#A8E6CF')}{chip('누구나','#DCE9FF')}</div>
</div>
<div style="position:absolute;left:0;right:0;bottom:-6px;display:flex;justify-content:center;align-items:flex-end;gap:0px">
  {ch('student-cheer',380)}<div style="margin-bottom:18px">{ch('turtle-cheer',370)}</div>{ch('teacher-wave',380)}
</div></div>'''

J = {}
J['banner.png'] = (1080, 1080, banner)
J['scene-friend.png'] = (900, 540, panel(row(
    col(bub('친구랑 같이<br>시작할래요!','w',44),ch('student-cheer',270),gap=14),
    col(bub('두 분 다<br>5%씩 적립해 드려요!','y',44),ch('teacher-wave',270),gap=14),
    gap=30, align='flex-end', style='position:absolute;bottom:-12px;left:0;right:0'), '#E6F6EE'))
J['scene-store.png'] = (600, 230, row(ch('turtle-point',224), bub('3만원 내고<br>4만원 받기!','y',44,'l'), gap=4))
render({f'{out}/{k}': v for k, v in J.items()})
