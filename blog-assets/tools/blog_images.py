#!/usr/bin/env python3
"""아인잉글리쉬 블로그 이미지 생성기.

사용법:  python3 blog_images.py spec.json 출력폴더
글마다 썸네일 1장(1200x1200)과 본문 이미지(1200x900)를 만든다.
category: "knowhow"(화상영어노하우, 노랑) 또는 "tip"(영어공부꿀팁, 민트)
본문 이미지 type: cards | dialogue | table | note   (예시는 example_spec.json)
필요한 것: Pillow, Noto Sans CJK 글꼴(/usr/share/fonts/opentype/noto)
"""
import json, sys, os, re
from PIL import Image, ImageDraw, ImageFont
S=2
FD='/usr/share/fonts/opentype/noto/'
INK='#111111'; YEL='#FFD60A'; RED='#FF4B3A'; BLUE='#2F6FDE'; MINT='#3FDDA8'; NAVY='#1B2A6B'; WHITE='#FFFFFF'; GRAY='#5A5F6B'
def F(w,size): return ImageFont.truetype(FD+f'NotoSansCJK-{w}.ttc', int(size*S), index=1)
def tw(t,f): return f.getlength(t)/S
def fit(t,w,size,maxw):
    while tw(t,F(w,size))>maxw: size-=2
    return size
def T(d,xy,t,f,fill,anchor='la'): d.text((xy[0]*S,xy[1]*S),t,font=f,fill=fill,anchor=anchor)
def R(d,box,r,**k):
    if 'width' in k: k['width']*=S
    d.rounded_rectangle([c*S for c in box],r*S,**k)
def E(d,box,**k):
    if 'width' in k: k['width']*=S
    d.ellipse([c*S for c in box],**k)
def A(d,box,a0,a1,**k):
    if 'width' in k: k['width']*=S
    d.arc([c*S for c in box],a0,a1,**k)
def canvas(w,h,bg): 
    im=Image.new('RGBA',(w*S,h*S),bg); return im
def layer(w,h): 
    im=Image.new('RGBA',(int(w*S),int(h*S)),(0,0,0,0)); return im,ImageDraw.Draw(im)
def paste_rot(base,lay,cx,cy,ang):
    r=lay.rotate(ang,expand=True,resample=Image.BICUBIC)
    base.alpha_composite(r,(int(cx*S-r.width/2),int(cy*S-r.height/2)))
def out(im,name):  # 2배로 그린 뒤 줄여서 저장
    w,h=im.size; im.convert('RGB').resize((w//S,h//S),Image.LANCZOS).save(name); print(name,(w//S,h//S))
def card(d,box,r=28,fill=WHITE,off=10):
    x0,y0,x1,y1=box
    R(d,(x0+off,y0+off,x1+off,y1+off),r,fill=INK); R(d,box,r,fill=fill,outline=INK,width=5)
def person(d,cx,cy,r,skin='#FFE0C7',hair='#3B2416',shirt=BLUE,base=None,mood='think',long=False):
    base=base or cy+r*2.4
    # body (small, round)
    d.pieslice([c*S for c in (cx-r*1.45,cy+r*1.05,cx+r*1.45,base+r*1.5)],180,360,fill=shirt)
    # collar
    d.pieslice([c*S for c in (cx-r*0.5,cy+r*0.75,cx+r*0.5,cy+r*1.45)],0,180,fill=WHITE)
    if long:
        R(d,(cx-r*1.22,cy-r*0.5,cx+r*1.22,cy+r*1.45),r*0.55,fill=hair)
    # back hair
    E(d,(cx-r*1.16,cy-r*1.14,cx+r*1.16,cy+r*0.75),fill=hair)
    # face (slightly wide)
    E(d,(cx-r*1.04,cy-r*0.86,cx+r*1.04,cy+r*1.0),fill=skin)
    # bangs
    d.chord([c*S for c in (cx-r*1.1,cy-r*1.12,cx+r*1.1,cy+r*0.55)],188,352,fill=hair)
    E(d,(cx-r*0.75,cy-r*0.62,cx-r*0.05,cy-r*0.18),fill=hair); E(d,(cx-r*0.1,cy-r*0.66,cx+r*0.8,cy-r*0.2),fill=hair)
    # ahoge
    d.pieslice([c*S for c in (cx-r*0.1,cy-r*1.5,cx+r*0.5,cy-r*0.95)],150,330,fill=hair)
    # blush
    for sx in (-1,1):
        E(d,(cx+sx*r*0.66-r*0.2,cy+r*0.42,cx+sx*r*0.66+r*0.2,cy+r*0.64),fill='#FFA8AE')
    # eyes
    for ex in (-0.4,0.4):
        E(d,(cx+ex*r-r*0.12,cy+r*0.08,cx+ex*r+r*0.12,cy+r*0.4),fill='#2B1B12')
        E(d,(cx+ex*r+r*0.0,cy+r*0.12,cx+ex*r+r*0.09,cy+r*0.21),fill=WHITE)
    lw=max(2,int(r*0.07))
    if mood=='think':
        E(d,(cx-r*0.09,cy+r*0.56,cx+r*0.09,cy+r*0.76),fill='#8A3B2E')
        for ex in (-0.4,0.4):
            d.line([((cx+ex*r-r*0.17)*S,(cy-r*0.06-(0.11*r if ex>0 else 0))*S),((cx+ex*r+r*0.17)*S,(cy-r*0.06-(0.11*r if ex<0 else 0))*S)],fill='#2B1B12',width=int(r*0.06*S))
        # sweat drop
        dx,dy=cx+r*1.38,cy-r*0.55
        d.polygon([((dx)*S,(dy-r*0.34)*S),((dx-r*0.15)*S,(dy)*S),((dx+r*0.15)*S,(dy)*S)],fill='#6EC6FF')
        E(d,(dx-r*0.16,dy-r*0.12,dx+r*0.16,dy+r*0.2),fill='#6EC6FF')
    else:
        d.chord([c*S for c in (cx-r*0.24,cy+r*0.3,cx+r*0.24,cy+r*0.78)],0,180,fill='#8A3B2E')
        d.chord([c*S for c in (cx-r*0.15,cy+r*0.56,cx+r*0.15,cy+r*0.8)],0,180,fill='#FF8A8A')
    # headset
    A(d,(cx-r*1.2,cy-r*1.22,cx+r*1.2,cy+r*1.0),190,350,fill=INK,width=max(3,int(r*0.1)))
    for sx in (-1,1):
        R(d,(cx+sx*r*1.13-r*0.17,cy-r*0.12,cx+sx*r*1.13+r*0.17,cy+r*0.5),r*0.16,fill=INK)
        R(d,(cx+sx*r*1.13-r*0.07,cy+r*0.0,cx+sx*r*1.13+r*0.07,cy+r*0.38),r*0.07,fill=YEL)
    d.line([((cx-r*1.13)*S,(cy+r*0.45)*S),((cx-r*0.85)*S,(cy+r*0.82)*S),((cx-r*0.55)*S,(cy+r*0.84)*S)],fill=INK,width=int(r*0.06*S),joint='curve')
    E(d,(cx-r*0.62,cy+r*0.75,cx-r*0.44,cy+r*0.93),fill=INK)
def bust(im,cx,cy,r,base,**k):
    lay,ld=layer(im.size[0]//S,base); person(ld,cx,cy,r,base=base,**k); im.alpha_composite(lay,(0,0))
def tile(im,box,bg,**k):
    x0,y0,x1,y1=box; w=x1-x0; h=y1-y0
    lay,ld=layer(w,h); m,md=Image.new('L',lay.size,0),None; md=ImageDraw.Draw(m); md.rounded_rectangle([0,0,w*S-1,h*S-1],26*S,fill=255)
    ld.rectangle([0,0,w*S,h*S],fill=bg); person(ld,w/2,h*0.46,h*0.25,base=h,**k)
    lay.putalpha(m); d=ImageDraw.Draw(im)
    R(d,(x0+8,y0+8,x1+8,y1+8),26,fill=INK); im.alpha_composite(lay,(x0*S,y0*S)); d=ImageDraw.Draw(im); R(d,box,26,outline=INK,width=5)


THEME={'knowhow':dict(bg=YEL,circ=RED,shirt=BLUE,pill='화상영어 노하우',soft='#FFF6D6',hl=YEL),
       'tip':dict(bg=MINT,circ=NAVY,shirt=RED,pill='영어공부 꿀팁',soft='#EAFBF4',hl=YEL)}
W,H=1200,900

def thumb(name,th,t):
    Wt=Ht=1200; M=120
    im=canvas(Wt,Ht,th['bg']); d=ImageDraw.Draw(im)
    E(d,(700,-120,1320,500),fill=th['circ'])
    bust(im,985,250,92,500,shirt=th['shirt'],mood=t.get('mood','think')); d=ImageDraw.Draw(im)
    bub=t.get('bubble','???')
    R(d,(640,150,860,290),40,fill=WHITE); d.polygon([(p[0]*S,p[1]*S) for p in [(810,286),(878,330),(850,270)]],fill=WHITE)
    T(d,(750,220),bub,F('Black',fit(bub,'Black',80,170)),INK,'mm')
    pf=F('Bold',38); pw=tw(th['pill'],pf)+60
    R(d,(M,M,M+pw,M+76),38,fill=INK); T(d,(M+pw/2,M+38),th['pill'],pf,WHITE,'mm')
    T(d,(M,470),t['line1'],F('Black',fit(t['line1'],'Black',170,560)),INK,'ls')
    T(d,(M,665),t['line2'],F('Black',fit(t['line2'],'Black',170,Wt-2*M)),INK,'ls')
    lay,ld=layer(900,190); R(ld,(10,10,890,180),24,fill=INK)
    T(ld,(450,95),t['band'],F('Black',fit(t['band'],'Black',100,800)),th['bg'],'mm')
    paste_rot(im,lay,M+450,840,3); d=ImageDraw.Draw(im)
    T(d,(M,Ht-M+10),'아인잉글리쉬',F('Bold',40),INK,'ls')
    if t.get('sub'): T(d,(Wt-M,Ht-M+10),t['sub'],F('Bold',fit(t['sub'],'Bold',36,560)),INK,'rs')
    out(im,name)

def header(im,th,title,mood='smile'):
    d=ImageDraw.Draw(im)
    T(d,(70,118),title,F('Black',fit(title,'Black',56,900)),INK,'ls')
    bust(im,1050,102,46,172,shirt=th['shirt'],mood=mood)
    return ImageDraw.Draw(im)

def cards(name,th,b):
    im=canvas(W,H,th['bg']); d=header(im,th,b['title'])
    rows=b['rows']; n=len(rows); gap=26; rh=(H-172-40-gap*(n-1))/n; k=rh/208; y=172
    for i,r in enumerate(rows):
        card(d,(70,y,W-80,y+rh))
        E(d,(100,y+26*k,100+60*k,y+86*k),fill=RED); T(d,(100+30*k,y+56*k),str(i+1),F('Black',34*k),WHITE,'mm')
        T(d,(118+60*k,y+56*k),r['label'],F('Bold',32*k),GRAY,'lm')
        T(d,(100,y+124*k),r['main'],F('Black',fit(r['main'],'Black',int(46*k),W-290)),INK,'lm')
        ex=r.get('example',''); nt=r.get('note','')
        fn=F('Regular',23*k); T(d,(W-110,y+176*k),nt,fn,GRAY,'rm')
        T(d,(100,y+176*k),ex,F('Medium',fit(ex,'Medium',int(26*k),W-250-tw(nt,fn))),INK,'lm')
        y+=rh+gap
    out(im,name)

def dialogue(name,th,b):
    im=canvas(W,H,th['soft']); d=ImageDraw.Draw(im)
    T(d,(70,112),b['title'],F('Black',fit(b['title'],'Black',54,780)),INK,'ls')
    tf=F('Bold',24); tg='연출한 예시 대화'; R(d,(W-70-tw(tg,tf)-40,68,W-70,118),25,fill=INK); T(d,(W-70-20,93),tg,tf,WHITE,'rm')
    turns=b['turns']; hs=[60+50*len(t['lines'])+ (40 if t.get('ko') else 0) for t in turns]; hs=[max(h,180) for h in hs]
    gap=(H-160-50-sum(hs))/max(len(turns)-1,1); gap=min(gap,60); y=160
    for t,h in zip(turns,hs):
        y=int(y); h=int(h); student=t['who']=='student'
        if student:
            tile(im,(70,y,250,y+180),'#CFE0FF',shirt=BLUE,mood=t.get('mood','smile')); d=ImageDraw.Draw(im)
            box=(290,y,1120,y+h); T(d,(160,y+204),'학생',F('Bold',22),INK,'mm')
        else:
            tile(im,(950,y,1130,y+180),'#FFD3CC',shirt=RED,hair='#5A2E12',mood='smile',long=True); d=ImageDraw.Draw(im)
            wmax=max([tw(l,F('Bold',33)) for l in t['lines']]+[tw(t.get('ko',''),F('Regular',24))])+80
            box=(max(80,910-wmax),y,910,y+h); T(d,(1040,y+204),'선생님',F('Bold',22),INK,'mm')
        card(d,box,r=30,fill=WHITE if student else YEL,off=8)
        yy=box[1]+50
        for l in t['lines']: T(d,(box[0]+36,yy),l,F('Bold',fit(l,'Bold',33,box[2]-box[0]-72)),INK,'lm'); yy+=50
        if t.get('ko'): T(d,(box[0]+36,yy+4),t['ko'],F('Regular',fit(t['ko'],'Regular',24,box[2]-box[0]-72)),GRAY,'lm')
        y+=h+gap
    out(im,name)

def table(name,th,b):
    im=canvas(W,H,th['bg']); d=header(im,th,b['title'],mood=b.get('mood','think'))
    foot=b.get('footnote'); bottom=H-110 if foot else H-50
    card(d,(70,172,W-80,bottom))
    hd=b.get('headers',['','']); T(d,(120,218),hd[0],F('Bold',27),GRAY,'lm'); T(d,(620,218),hd[1],F('Bold',27),GRAY,'lm')
    rows=b['rows']; pitch=min(104,(bottom-250-12)/len(rows)); k=pitch/104; y=250
    for a,c in rows:
        d.line([(105*S,y*S),((W-115)*S,y*S)],fill='#DDDDDD',width=2*S)
        T(d,(120,y+pitch/2),a,F('Bold',fit(a,'Bold',int(42*k),380)),INK,'lm')
        T(d,(545,y+pitch/2),'→',F('Black',38*k),RED,'mm')
        f=F('Black',fit(c,'Black',int(42*k),440)); w=tw(c,f); R(d,(612,y+pitch/2-30*k,640+w,y+pitch/2+32*k),10,fill=th['hl'])
        T(d,(626,y+pitch/2),c,f,INK,'lm'); y+=pitch
    if foot: T(d,(70,H-52),foot,F('Medium',fit(foot,'Medium',25,W-140)),INK,'lm')
    out(im,name)

def note(name,th,b):
    """steps: [{label, lines:[...]}]  줄 안에서 [[글자]]는 형광펜, ____(밑줄 4개 이상)는 빨간 빈칸. big:false면 작은 글씨."""
    im=canvas(W,H,th['bg']); d=header(im,th,b['title'])
    card(d,(70,172,W-80,H-70),fill='#FFFDF4')
    steps=b['steps']; nl=sum(len(s['lines']) for s in steps); avail=H-70-172-30
    unit=min(60,(avail-len(steps)*70)/max(nl,1)); y=172+53
    for i,s in enumerate(steps):
        if i: d.line([(105*S,(y-45)*S),((W-115)*S,(y-45)*S)],fill='#D9D4C0',width=2*S)
        E(d,(105,y-22,149,y+22),fill=INK); T(d,(127,y),str(i+1),F('Black',26),WHITE,'mm'); T(d,(164,y),s['label'],F('Bold',27),INK,'lm')
        y+=67; big=s.get('big',True); f=F('Bold',42) if big else F('Medium',31)
        for line in s['lines']:
            x=110
            for part in re.split(r'(\[\[.*?\]\]|_{4,})',line):
                if not part: continue
                hl=part.startswith('[['); txt=part[2:-2] if hl else part
                w=f.getlength(txt)/S
                if hl: R(d,(x-4,y-30,x+w+4,y+28),8,fill=th['hl'])
                T(d,(x,y),txt,f,RED if txt.startswith('____') else INK,'lm'); x+=w
            y+=unit
        y+=28
    out(im,name)

DRAW={'cards':cards,'dialogue':dialogue,'table':table,'note':note}
def main(spec_path,outdir):
    spec=json.load(open(spec_path,encoding='utf-8')); os.makedirs(outdir,exist_ok=True)
    for p in spec['posts']:
        th=THEME[p['category']]
        thumb(os.path.join(outdir,p['prefix']+'_thumbnail_1200.png'),th,p['thumbnail'])
        for b in p['body']: DRAW[b['type']](os.path.join(outdir,b['file']),th,b)
if __name__=='__main__': main(sys.argv[1],sys.argv[2])
