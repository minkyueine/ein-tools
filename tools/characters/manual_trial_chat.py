exec(open('s2_more.py').read().split('def page(inner,w)')[0])
from chars import P,C,ST,SKIN,YEL,HAIR_T,HAIR_S,face as FACE
HEADS={
 'teacher-smile':(P('M44,112 Q38,46 100,46 Q162,46 156,112 L158,142 Q154,152 140,150 L60,150 Q46,152 42,142 Z',HAIR_T)
   +C(100,104,50,SKIN)
   +P('M52,100 Q54,54 100,54 Q146,54 148,100 Q136,74 104,72 Q92,86 52,100 Z',HAIR_T)
   +f'<path d="M48,92 Q50,36 100,36 Q150,36 152,92" fill="none" {ST}/>'
   +f'<rect x="38" y="90" width="18" height="32" rx="9" fill="{YEL}" {ST}/><rect x="144" y="90" width="18" height="32" rx="9" fill="{YEL}" {ST}/>'
   +f'<path d="M46,122 Q48,140 74,138" fill="none" {ST} stroke-width="2.8"/><circle cx="77" cy="138" r="4" fill="{INK}"/>'
   +FACE('happy',100,106),'30 24 140 140'),
 'student-smile':(C(100,100,54,SKIN)
   +P('M46,98 Q42,42 100,40 Q158,42 154,98 Q150,72 122,66 Q112,80 78,78 Q56,80 46,98 Z',HAIR_S)
   +f'<path d="M100,40 Q98,24 110,22" fill="none" {ST}/>'+FACE('smile',100,104),'26 16 148 148')}
def face(name,bg,s):
    body,vb=HEADS[name]
    return f'<div style="flex:none;width:{s}px;height:{s}px;border-radius:50%;background:{bg};border:2px solid {INK};overflow:hidden;display:flex;align-items:center;justify-content:center">{svg_mid(body,vb,s*0.86)}</div>'
def face_old(name,bg,s):
    vb={'teacher-smile':'18 6 164 164','student-smile':'26 16 148 148'}[name]
    return f'<div style="flex:none;width:{s}px;height:{s}px;border-radius:50%;background:{bg};border:2px solid {INK};overflow:hidden;display:flex;align-items:center;justify-content:center"><div style="margin-top:{s*0.06:.0f}px">{svg_mid(chars.SET[name],vb,s*0.84)}</div></div>'
T=lambda s=46: face('teacher-smile','#FFE7E1',s); S=lambda s=46: face('student-smile','#FFFFFF',s)
def note2(t): return f'<div style="align-self:center;background:#EC6856;color:#fff;border:2px solid {INK};border-radius:999px;padding:4px 14px;font:800 13px {F}">{t}</div>'
def bl2(t,ko=None): 
    k=f'<div style="font:500 13px/1.4 {F};color:#6B5E58;margin-top:2px">{ko}</div>' if ko else ''
    return f'<div style="background:#FFD966;border:2px solid {INK};border-radius:18px 18px 18px 4px;padding:9px 15px;font:800 16px/1.4 {F};max-width:78%">{t}{k}</div>'
def br2(t): return f'<div style="background:#fff;border:2px solid {INK};border-radius:18px 18px 4px 18px;padding:9px 15px;font:800 16px/1.4 {F};max-width:78%">{t}</div>'
L2=lambda b: f'<div style="display:flex;gap:8px;align-items:flex-end">{T(46)}{b}</div>'
R2=lambda b: f'<div style="display:flex;gap:8px;align-items:flex-end;justify-content:flex-end">{b}{S(46)}</div>'
chat=(L2(bl2('Can you introduce yourself?'))+R2(br2("Hi! I'm Minji. I'm a… student."))+note2('발음 · 말하는 속도를 들어요')
 +L2(bl2('What did you do yesterday?'))+R2(br2('I go… I went to the park!'))+note2('문장을 만드는 힘을 봐요')
 +L2(bl2('Take your time. Good job! 😊')))
# 1안: 노란 배경 + 두꺼운 테두리 + 색 그림자
V1=(f'<div style="margin-top:16px;background:#FFF1C9;border:3px solid #222;border-radius:20px;box-shadow:6px 6px 0 #EC6856;padding:18px 16px;display:flex;flex-direction:column;gap:10px">'
    f'<div style="align-self:center;background:#222;color:#fff;border-radius:999px;padding:5px 16px;font:800 13px {F}">🎧 실제 체험 수업은 이렇게 진행돼요</div>'+chat+'</div>')
# 2안: 코랄 머리띠 + 연한 배경
V2=(f'<div style="margin-top:16px;border:3px solid #222;border-radius:20px;overflow:hidden;box-shadow:6px 6px 0 #EC6856">'
    f'<div style="background:#222;color:#fff;padding:12px 16px;font:800 17px {F}"><svg width="20" height="18" viewBox="0 0 24 22" style="vertical-align:-3px;margin-right:6px"><path d="M4,14 V11 a8,8 0 0 1 16,0 V14" fill="none" stroke="#FFD966" stroke-width="2.6" stroke-linecap="round"/><rect x="2" y="12" width="6" height="9" rx="3" fill="#FFD966"/><rect x="16" y="12" width="6" height="9" rx="3" fill="#FFD966"/></svg>실제 체험 수업은 이렇게 진행돼요<div style="font:600 13px {F};opacity:.9;margin-top:2px">영어가 서툴러도 선생님이 천천히 이끌어 드려요</div></div>'
    f'<div style="background:#FFF8EC;padding:16px;display:flex;flex-direction:column;gap:10px">'+chat+'</div></div>')
def page(inner,w): return f'<div style="width:{w}px;background:#fff;border:1px solid #ddd;padding:22px;box-sizing:border-box">{inner}</div>'
def col(l,inner): return f'<div><div style="font:700 18px {F};margin-bottom:8px">{l}</div>{inner}</div>'
rows=''
V3=V2.replace('background:#222;color:#fff;padding:12px','background:#4A3A34;color:#fff;padding:12px').replace('border:3px solid #222;border-radius:20px;overflow:hidden','border:3px solid #4A3A34;border-radius:20px;overflow:hidden')
for l,x in (('검은색 띠',V2),('진한 갈색 띠',V3)):
    rows+=f'<div style="display:flex;gap:36px;align-items:flex-start;margin-bottom:36px">{col(l+" — PC",page(head+x,640))}{col("모바일",page(head+x,375))}</div>'
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg=b.new_page(viewport={'width':1150,'height':900})
    pg.set_content(f'<body style="margin:0"><div style="padding:34px;background:#F3F1EE;display:inline-block">{rows}</div></body>'); pg.wait_for_timeout(500)
    pg.locator('body>div').screenshot(path='/home/claude/out/scene2_A2_strong.png'); b.close()
open('/home/claude/out/a2_v1.html','w').write(V1); open('/home/claude/out/a2_v2.html','w').write(V2)
