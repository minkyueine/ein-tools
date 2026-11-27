import sys,base64
sys.path.insert(0,'/home/claude/ein-tools/tools/characters')
import chars
from chars import P,C,face,INK,SKIN,BLUE,PINK,W,ST,CORAL
from scene import svg_mid,COL
F="'Noto Sans CJK KR',sans-serif"
HAIR_S='#5A4640'; HAIR_M='#3B2C26'; NAVY='#6F86C9'; MINT='#8ED1BE'
VB='-30 -14 270 272'

def qmarks():
    return (f'<text x="168" y="44" font-family="{F}" font-weight="900" font-size="46" fill="{CORAL}" stroke="{INK}" stroke-width="2.4" transform="rotate(14 168 44)">?</text>'
            f'<text x="196" y="78" font-family="{F}" font-weight="900" font-size="30" fill="{CORAL}" stroke="{INK}" stroke-width="2" transform="rotate(22 196 78)">?</text>')
def puzzled(cx=100,cy=104):
    o=f'<ellipse cx="{cx-30}" cy="{cy+13}" rx="9" ry="6" fill="{PINK}" opacity=".6"/><ellipse cx="{cx+30}" cy="{cy+13}" rx="9" ry="6" fill="{PINK}" opacity=".6"/>'
    o+=f'<ellipse cx="{cx-17}" cy="{cy}" rx="4.6" ry="5.8" fill="{INK}"/><ellipse cx="{cx+17}" cy="{cy+1}" rx="3.6" ry="3.6" fill="{INK}"/>'
    o+=f'<path d="M{cx-27},{cy-16} Q{cx-17},{cy-24} {cx-8},{cy-17}" fill="none" {ST} stroke-width="2.8"/><path d="M{cx+9},{cy-11} L{cx+26},{cy-9}" fill="none" {ST} stroke-width="2.8"/>'
    o+=f'<path d="M{cx-9},{cy+19} q4,-4 8,0 q4,4 8,0" fill="none" {ST} stroke-width="3"/>'
    return o
def student_base(r=0,extra='',body='M42,240 Q42,164 100,164 Q158,164 158,240 Z'):
    o=P(body,BLUE)+extra
    o+=f'<path d="M87,140 L87,166 Q100,178 113,166 L113,140" fill="{SKIN}" {ST}/>'
    o+=f'<g transform="rotate({r} 100 150)">'+C(100,100,54,SKIN)
    o+=P('M46,98 Q42,42 100,40 Q158,42 154,98 Q150,72 122,66 Q112,80 78,78 Q56,80 46,98 Z',HAIR_S)
    o+=f'<path d="M100,40 Q98,24 110,22" fill="none" {ST}/>'
    return o
def student_scratch():
    # 고개 갸웃 + 머리 긁적
    o=student_base(-8)+puzzled()+'</g>'
    o+=P('M138,196 Q182,184 170,92 L154,92 Q160,168 124,180 Z',BLUE)+C(160,82,14,SKIN)
    o+=f'<path d="M150,72 l-6,-6 M162,66 l0,-9 M174,72 l6,-6" fill="none" {ST} stroke-width="2.6"/>'
    return o+qmarks()
def student_phone():
    # 휴대폰 보며 갸웃
    o=student_base(7)+puzzled()+'</g>'
    o+=f'<rect x="78" y="176" width="44" height="64" rx="8" fill="#3E3A44" {ST} transform="rotate(-10 100 208)"/><rect x="84" y="184" width="32" height="44" rx="4" fill="#CFE3FF" transform="rotate(-10 100 208)"/>'
    o+=C(76,214,11,SKIN)+C(124,206,11,SKIN)
    return o+qmarks()

def manager_bob():
    # 단발 + 남색 카디건 + 사원증 + 태블릿
    o=P('M44,150 Q36,40 100,40 Q164,40 156,150 Q152,168 138,168 L62,168 Q48,168 44,150 Z',HAIR_M)
    o+=P('M42,240 Q42,166 100,166 Q158,166 158,240 Z',NAVY)
    o+=P('M84,168 L100,200 L116,168 Z',W)
    o+=f'<path d="M87,142 L87,168 Q100,180 113,168 L113,142" fill="{SKIN}" {ST}/>'
    o+=C(100,104,50,SKIN)
    o+=f'<path d="M50,108 Q48,50 100,50 Q152,50 150,108 Q144,82 120,72 Q96,90 50,108 Z" fill="{HAIR_M}" stroke="{HAIR_M}" stroke-width="3.4"/>'
    o+=f'<path d="M150,108 Q144,82 120,72 Q96,90 50,108" fill="none" {ST}/>'
    o+=face('happy',100,108)
    o+=f'<path d="M86,170 L76,212 M114,170 L82,212" fill="none" {ST} stroke-width="2.6"/>'
    o+=f'<rect x="64" y="208" width="30" height="24" rx="4" fill="{W}" {ST} stroke-width="2.8"/><rect x="70" y="222" width="18" height="5" rx="2.5" fill="{CORAL}"/>'
    o+=f'<rect x="114" y="180" width="50" height="62" rx="7" fill="#FFFFFF" {ST} transform="rotate(8 139 211)"/><rect x="122" y="192" width="30" height="6" rx="3" fill="{CORAL}" transform="rotate(8 139 211)"/><rect x="122" y="206" width="34" height="5" rx="2.5" fill="#E2DCD6" transform="rotate(8 139 211)"/><rect x="122" y="218" width="26" height="5" rx="2.5" fill="#E2DCD6" transform="rotate(8 139 211)"/>'
    o+=C(118,226,11,SKIN)
    o+=P('M160,198 Q186,192 190,156 L204,160 Q204,206 170,222 Z',NAVY)+C(198,146,13,SKIN)
    o+=f'<path d="M218,130 q7,6 5,15 M228,122 q10,9 8,22" fill="none" {ST} stroke-width="2.6"/>'
    return o
def manager_glasses():
    # 묶은 머리 + 안경 + 민트 니트 + 사원증 + 엄지 척
    o=f'<ellipse cx="150" cy="140" rx="16" ry="26" fill="{HAIR_M}" {ST} transform="rotate(-20 150 140)"/>'
    o+=P('M42,240 Q42,166 100,166 Q158,166 158,240 Z',MINT)
    o+=f'<path d="M87,142 L87,168 Q100,180 113,168 L113,142" fill="{SKIN}" {ST}/>'
    o+=C(100,104,50,SKIN)
    o+=P('M48,106 Q46,46 100,46 Q154,46 152,106 Q146,78 104,74 L100,62 L96,74 Q54,78 48,106 Z',HAIR_M)
    o+=f'<ellipse cx="70" cy="121" rx="9" ry="6" fill="{PINK}" opacity=".6"/><ellipse cx="130" cy="121" rx="9" ry="6" fill="{PINK}" opacity=".6"/>'
    o+=f'<circle cx="82" cy="106" r="14" fill="none" {ST} stroke-width="3"/><circle cx="118" cy="106" r="14" fill="none" {ST} stroke-width="3"/><path d="M96,105 L104,105" {ST} stroke-width="3"/>'
    o+=f'<path d="M75,108 Q82,100 89,108 M111,108 Q118,100 125,108" fill="none" {ST} stroke-width="3"/>'
    o+=f'<path d="M90,126 Q100,138 110,126 Z" fill="#E0604F" {ST} stroke-width="2.6"/>'
    o+=f'<path d="M84,170 L94,212 M116,170 L106,212" fill="none" {ST} stroke-width="2.6"/>'
    o+=f'<rect x="84" y="208" width="32" height="26" rx="4" fill="{W}" {ST} stroke-width="2.8"/><rect x="91" y="223" width="18" height="5" rx="2.5" fill="{CORAL}"/>'
    o+=P('M156,200 Q184,196 186,160 L200,162 Q202,208 166,222 Z',MINT)
    o+=C(194,146,14,SKIN)+f'<path d="M214,128 q7,6 5,15 M224,120 q10,9 8,22" fill="none" {ST} stroke-width="2.6"/>'
    return o

def ch(body,h): return svg_mid(body,VB,h)
def tbub(text,c,fs,tail):
    pos='right:64px' if tail=='r' else 'left:64px'
    t=f'<div style="position:absolute;{pos};bottom:-20px;width:32px;height:32px;background:{COL[c]};border-right:4px solid {INK};border-bottom:4px solid {INK};transform:rotate(45deg)"></div>'
    return f'<div style="position:relative;background:{COL[c]};border:4px solid {INK};border-radius:30px;padding:20px 34px;font:700 {fs}px/1.3 {F};color:#2A211D;white-space:nowrap">{text}{t}</div>'
def chip(t,bg,fg): return f'<div style="background:{bg};border:4px solid {INK};border-radius:999px;padding:9px 30px;font:700 36px/1 {F};color:{fg}">{t}</div>'
def blob(inner,bg): return f'<div style="position:relative;width:460px;height:470px;display:flex;align-items:flex-end;justify-content:center"><div style="position:absolute;left:30px;right:30px;bottom:0;height:350px;background:{bg};border-radius:200px 200px 40px 40px"></div><div style="position:relative;margin-bottom:-2px">{inner}</div></div>'
def scene(stu,mgr):
    side=lambda b,body,bg,lab,lbg,lfg,tail,txt: f'<div style="display:flex;flex-direction:column;align-items:center;gap:28px">{tbub(txt,b,52,tail)}{blob(ch(body,470),bg)}{chip(lab,lbg,lfg)}</div>'
    return (f'<div style="position:absolute;inset:4px;background:#fff;border:4px solid {INK};border-radius:44px;display:flex;align-items:center;justify-content:center;gap:80px">'
            + side('w',stu,'#DCE9FF','학생','#9DBFF5','#2A211D','r','수업은 어떻게<br>듣는 거지…?')
            + side('y',mgr,'#E2F4EE' if mgr==M2 else '#E5EBFA','아인 매니저','#4A3A34','#fff','l','하나씩<br>알려 드릴게요!') + '</div>')
M1=manager_bob(); M2=manager_glasses()
def render(jobs,scale):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        b=pw.chromium.launch(executable_path='/usr/bin/google-chrome')
        for path,(w,h,html) in jobs.items():
            pg=b.new_page(viewport={'width':w,'height':h},device_scale_factor=scale)
            pg.set_content(f'<body style="margin:0;width:{w}px;height:{h}px;position:relative;overflow:hidden;background:transparent">{html}</body>')
            pg.wait_for_timeout(400); pg.screenshot(path=path,omit_background=True); pg.close()
        b.close()
W_,H_=1200,900
render({'/home/claude/out/v3_1.png':(W_,H_,scene(student_scratch(),M1)),
        '/home/claude/out/v3_2.png':(W_,H_,scene(student_phone(),M2))},2)
def b64(f): return base64.b64encode(open(f,'rb').read()).decode()
rows=''
for k,name in (('1','학생 머리 긁적 · 단발 매니저(태블릿)'),('2','학생 휴대폰 보며 갸웃 · 안경 매니저(인사)')):
    d=b64(f'/home/claude/out/v3_{k}.png')
    rows+=(f'<div style="display:flex;gap:40px;align-items:flex-start;margin-bottom:44px"><div style="width:170px;font:800 30px/1.2 {F}">{k}안<div style="font:600 17px/1.4 {F};color:#777;margin-top:6px">{name}</div></div>'
      f'<div><div style="font:600 16px {F};color:#999;margin-bottom:8px">PC (600px)</div><img src="data:image/png;base64,{d}" style="width:600px;display:block"></div>'
      f'<div><div style="font:600 16px {F};color:#999;margin-bottom:8px">모바일 (375px 화면)</div><div style="width:375px;border:10px solid #222;border-radius:44px;background:#fff;padding:36px 12px 26px"><img src="data:image/png;base64,{d}" style="width:100%;display:block"></div></div></div>')
render({'/home/claude/out/scene-1_매니저_시안.png':(1340,1090,f'<div style="padding:46px;background:#F3F1EE;height:100%;box-sizing:border-box">{rows}</div>')},1)

# ---- v4: 1안 수정 ----
def confused(cx=100,cy=104):
    o=f'<ellipse cx="{cx-30}" cy="{cy+13}" rx="9" ry="6" fill="{PINK}" opacity=".6"/><ellipse cx="{cx+30}" cy="{cy+13}" rx="9" ry="6" fill="{PINK}" opacity=".6"/>'
    for x in (cx-17,cx+17):
        o+=f'<ellipse cx="{x}" cy="{cy}" rx="5" ry="6.2" fill="{INK}"/><circle cx="{x+1.5}" cy="{cy-2.4}" r="1.7" fill="#fff"/>'
    o+=f'<path d="M{cx-27},{cy-13} Q{cx-18},{cy-20} {cx-9},{cy-17} M{cx+9},{cy-17} Q{cx+18},{cy-20} {cx+27},{cy-13}" fill="none" {ST} stroke-width="2.8"/>'
    o+=f'<ellipse cx="{cx+2}" cy="{cy+19}" rx="4.5" ry="5.5" fill="#E0604F" {ST} stroke-width="2.4"/>'
    return o
def student_scratch2():
    # 팔(소매)을 몸통 뒤에서 어깨로 이어지게 먼저 그리고, 손만 머리 위에 얹는다
    o=P('M118,196 Q168,194 176,150 Q180,112 170,88 L152,90 Q160,124 154,150 Q146,174 112,180 Z',BLUE)
    o+=P('M76,180 C58,176 40,184 33,204 Q26,222 22,240 L52,240 Q54,210 72,188 Z',BLUE)
    o+=student_base(-8)+confused()+'</g>'
    o+=C(160,84,14,SKIN)
    return o+qmarks()
def manager_bob_mint():
    b=manager_bob()
    arm=P('M160,198 Q186,192 190,156 L204,160 Q204,206 170,222 Z',NAVY)
    arm2=P('M128,196 Q182,198 190,156 L204,160 Q206,214 150,226 Z',NAVY)
    b=arm2+b.replace(arm,'')
    return b.replace(f'fill="{NAVY}"',f'fill="{MINT}"')
def scene4(stu,mgr):
    side=lambda b,body,bg,lab,lbg,lfg,tail,txt: f'<div style="display:flex;flex-direction:column;align-items:center;gap:28px">{tbub(txt,b,52,tail)}{blob(ch(body,470),bg)}{chip(lab,lbg,lfg)}</div>'
    return (f'<div style="position:absolute;inset:4px;background:#fff;border:4px solid {INK};border-radius:44px;display:flex;align-items:center;justify-content:center;gap:80px">'
            + side('w',stu,'#DCE9FF','학생','#9DBFF5','#2A211D','r','수업은 어떻게<br>듣는 거지…?')
            + side('y',mgr,'#E2F4EE','아인 매니저','#4A3A34','#fff','l','하나씩<br>알려 드릴게요!') + '</div>')
render({'/home/claude/out/scene-1_v4.png':(W_,H_,scene4(student_scratch2(),manager_bob_mint()))},2)

# ---- 매니저 포즈 (거북이 자리 교체용) ----
def manager_core():
    o=P('M44,150 Q36,40 100,40 Q164,40 156,150 Q152,168 138,168 L62,168 Q48,168 44,150 Z',HAIR_M)
    o+=P('M42,240 Q42,166 100,166 Q158,166 158,240 Z',MINT)
    o+=P('M84,168 L100,200 L116,168 Z',W)
    o+=f'<path d="M87,142 L87,168 Q100,180 113,168 L113,142" fill="{SKIN}" {ST}/>'
    o+=C(100,104,50,SKIN)
    o+=f'<path d="M50,108 Q48,50 100,50 Q152,50 150,108 Q144,82 120,72 Q96,90 50,108 Z" fill="{HAIR_M}" stroke="{HAIR_M}" stroke-width="3.4"/>'
    o+=f'<path d="M150,108 Q144,82 120,72 Q96,90 50,108" fill="none" {ST}/>'
    return o
def lanyard(): return f'<path d="M86,170 L76,212 M114,170 L82,212" fill="none" {ST} stroke-width="2.6"/><rect x="64" y="208" width="30" height="24" rx="4" fill="{W}" {ST} stroke-width="2.8"/><rect x="70" y="222" width="18" height="5" rx="2.5" fill="{CORAL}"/>'
def manager_point():
    # 오른쪽(말풍선 쪽)을 손으로 가리킴 — 팔은 몸 뒤에서 시작
    o=P('M126,190 Q170,196 196,170 L204,182 Q178,214 140,222 Z',MINT)
    o+=manager_core()+face('happy',100,108)+lanyard()
    o+=C(204,172,13,SKIN)
    return o
def manager_paper():
    o=manager_core()+face('smile',100,108)+lanyard()
    o+=f'<rect x="54" y="176" width="92" height="62" rx="8" fill="{W}" {ST}/><rect x="66" y="188" width="40" height="7" rx="3.5" fill="{CORAL}"/><rect x="66" y="202" width="66" height="5" rx="2.5" fill="#E2DCD6"/><rect x="66" y="214" width="52" height="5" rx="2.5" fill="#FFD966"/>'
    o+=C(54,212,11,SKIN)+C(146,212,11,SKIN)
    return o
import scene as SC
def mch(body,h): return svg_mid(body,'34 32 196 214',h)
J={}
J['scene-1.png']=None
J['scene-3.png']=(744,152,SC.row(mch(manager_point(),150),SC.bub('이어폰까지 챙기면 준비 끝!','w',38,'l')))
J['scene-8.png']=(795,166,SC.row(mch(manager_point(),164),SC.bub('전화 없이, 클릭 몇 번이면 끝!','y',38,'l')))
J['scene-9.png']=(682,159,SC.row(mch(manager_paper(),157),SC.bub('날짜 말고, 횟수로 세요!','w',38,'l')))
del J['scene-1.png']
import os
os.makedirs('/home/claude/out/mgr',exist_ok=True)
jobs={}
for k,(w,h,html) in J.items():
    jobs[f'/home/claude/out/mgr/{k}']=(w,h,f'<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center">{html}</div>')
render(jobs,1)
