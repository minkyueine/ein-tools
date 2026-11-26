"""신규회원 5% 적립금 이벤트(블로그 211번 글) 그림: 배너 + 본문 장면 2장.
사용법: cd tools/characters && python3 event211_images.py ../../event/211"""
import sys, os
from scene import *
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
F = "'Pretendard','Noto Sans CJK KR',sans-serif"

def confetti():
    dots = [(90,140,'#FFD966',16),(1000,120,'#A8E6CF',14),(160,560,'#FFFFFF',10),(950,520,'#FFD966',12),
            (70,860,'#A8E6CF',13),(1020,900,'#FFFFFF',11),(260,90,'#FFFFFF',9),(820,80,'#FFE7E1',15)]
    return ''.join(f'<div style="position:absolute;left:{x}px;top:{y}px;width:{s}px;height:{s}px;border-radius:50%;background:{c};border:3px solid {INK}"></div>' for x,y,c,s in dots)

banner = f'''<div style="position:absolute;inset:0;background:#EC6856;overflow:hidden">{confetti()}
<div style="position:absolute;left:0;right:0;top:70px;text-align:center;font-family:{F}">
  <div style="display:inline-block;background:#FFD966;border:4px solid {INK};border-radius:40px;padding:10px 30px;font:800 38px/1.2 {F};color:#2A211D">신규회원 전용</div>
  <div style="margin-top:34px;font:800 76px/1.18 {F};color:#fff;letter-spacing:-.01em">첫 결제하면</div>
  <div style="margin-top:6px;font:900 210px/1 {F};color:#fff;letter-spacing:-.03em;-webkit-text-stroke:6px {INK};paint-order:stroke fill">5%<span style="font-size:96px;-webkit-text-stroke:4px {INK}"> 적립</span></div>
  <div style="margin-top:26px;font:700 40px/1.3 {F};color:#FFF6D6">1·3·6개월 수강권 · 주 2회 이상</div>
</div>
<div style="position:absolute;left:0;right:0;bottom:-6px;display:flex;justify-content:center;align-items:flex-end;gap:70px">
  {ch('student-cheer',400)}<div style="margin-bottom:20px">{ch('turtle-cheer',390)}</div>
</div></div>'''

J = {}
J['banner.png'] = (1080, 1080, banner)
J['scene-hello.png'] = (900, 540, panel(row(
    col(bub('첫 결제인데<br>혜택 있어요?','w',44),ch('student-smile',270),gap=14),
    col(bub('결제 금액의 5%를<br>바로 드려요!','y',44),ch('turtle-point',270),gap=14,style='padding-bottom:24px'),
    gap=30, align='flex-end', style='position:absolute;bottom:-12px;left:0;right:0'), '#FFF6D6'))
J['scene-use.png'] = (720, 230, row(ch('turtle-paper',224), bub('모은 적립금은<br>다음 수강 때 쓰면 돼요!','w',40,'l'), gap=14))
render({f'{out}/{k}': v for k, v in J.items()})
