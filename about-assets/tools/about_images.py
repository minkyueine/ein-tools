#!/usr/bin/env python3
"""아인잉글리쉬 about 페이지('왜 아인 화상영어일까?')용 그림 생성기.
사용법: python3 about-assets/tools/about_images.py about-assets/
블로그 그림과 같은 캐릭터(blog_images.py)를 쓰고, 색은 로고 코랄에 맞춘다.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'blog-assets', 'tools'))
from blog_images import *
from PIL import ImageDraw
CORAL='#EC6856'; TINT='#FDF1EE'; SOFT='#F7F7F7'; LINE='#E3E3E3'; GREEN='#10B981'; GBG='#ECFDF5'; ABG='#FFFBEB'; AMB='#D97706'
STU=dict(shirt=BLUE); TEA=dict(shirt=CORAL,hair='#5A2E12',long=True,mood='smile')
def strike(d,x,y,t,f,fill=GRAY,anchor='lm'):
    T(d,(x,y),t,f,fill,anchor); w=tw(t,f); x0=x if anchor[0]=='l' else x-w/2
    d.line([(x0*S,(y+2)*S),((x0+w)*S,(y+2)*S)],fill=RED,width=4*S)
def pill(d,x,y,t,size=24,fill=INK,fg=WHITE,right=False):
    f=F('Bold',size); w=tw(t,f)+size*1.6; h=size*2.1
    x0=x-w if right else x; R(d,(x0,y,x0+w,y+h),h/2,fill=fill); T(d,(x0+w/2,y+h/2),t,f,fg,'mm'); return w
def bubble(d,box,lines,fill=WHITE,size=34,weight='Bold',fg=INK,tail=None):
    card(d,box,r=26,fill=fill,off=7); x0,y0,x1,y1=box; n=len(lines); lh=size*1.45; y=(y0+y1)/2-lh*(n-1)/2
    for l in lines:
        T(d,(x0+30,y),l,F(weight,fit(l,weight,size,x1-x0-60)),fg,'lm'); y+=lh

def hero(name):
    W_,H_=1440,860; im=canvas(W_,H_,WHITE); d=ImageDraw.Draw(im)
    R(d,(0,0,W_,96),0,fill=INK)
    for i,c in enumerate((RED,YEL,MINT)): E(d,(48+i*44,34,76+i*44,62),fill=c)
    T(d,(200,48),'1:1 화상수업',F('Bold',30),WHITE,'lm')
    tile(im,(80,150,480,550),'#CFE0FF',mood='think',**STU); tile(im,(960,150,1360,550),'#FFD3CC',**TEA); d=ImageDraw.Draw(im)
    T(d,(280,588),'학생',F('Bold',28),INK,'mm'); T(d,(1160,588),'선생님',F('Bold',28),INK,'mm')
    T(d,(720,190),'그 자리에서 바로 교정',F('Bold',30),GRAY,'mm')
    strike(d,720,290,'try',F('Black',84),GRAY,'mm'); T(d,(720,372),'↓',F('Black',44),CORAL,'mm')
    f=F('Black',112); w=tw('tries',f); R(d,(720-w/2-22,410,720+w/2+22,545),18,fill=YEL); T(d,(720,474),'tries',f,INK,'mm')
    card(d,(80,640,690,800),r=26,fill=SOFT,off=7); T(d,(112,682),'학생이 말한 문장',F('Bold',24),GRAY,'lm'); strike(d,112,744,'He always try to care of others.',F('Medium',33),GRAY)
    card(d,(750,640,1360,800),r=26,fill=YEL,off=7); T(d,(782,682),'선생님이 고쳐 준 문장',F('Bold',24),INK,'lm')
    t='He always tries to take care of others.'; T(d,(782,744),t,F('Black',fit(t,'Black',33,548)),INK,'lm')
    out(im,name)

def pain(name,mood,bubbles,bg):
    W_,H_=720,480; im=canvas(W_,H_,bg); d=ImageDraw.Draw(im)
    bust(im,170,250,92,H_,mood=mood,**STU); d=ImageDraw.Draw(im); y=70
    for lines,fill in bubbles:
        h=44+len(lines)*50; bubble(d,(330,y,676,y+h),lines,fill=fill,size=32); y+=h+26
    out(im,name)

def flow(name,n,draw):
    W_=H_=720; im=canvas(W_,H_,TINT); d=ImageDraw.Draw(im)
    E(d,(40,40,128,128),fill=CORAL); T(d,(84,84),str(n),F('Black',48),WHITE,'mm')
    draw(im,d); out(im,name)
def f1(im,d):
    tile(im,(70,190,340,460),'#CFE0FF',mood='smile',**STU); tile(im,(380,190,650,460),'#FFD3CC',**TEA); d=ImageDraw.Draw(im)
    T(d,(205,494),'학생',F('Bold',26),INK,'mm'); T(d,(515,494),'선생님',F('Bold',26),INK,'mm')
    bubble(d,(120,540,600,650),['25분, 선생님과 1:1 대화'],fill=WHITE,size=34)
def f2(im,d):
    bubble(d,(70,180,650,300),['I go to there yesterday.'],fill=WHITE,size=38,weight='Medium',fg=GRAY)
    d.line([(100*S,242*S),(560*S,242*S)],fill=RED,width=4*S)
    T(d,(360,352),'↓',F('Black',52),CORAL,'mm')
    bubble(d,(70,410,650,540),['I went there yesterday.'],fill=YEL,size=42,weight='Black')
    T(d,(360,610),'틀린 문장은 그 자리에서',F('Bold',32),INK,'mm')
def f3(im,d):
    R(d,(190+10,150+10,530+10,680+10),44,fill=INK); R(d,(190,150,530,680),44,fill=WHITE,outline=INK,width=6)
    T(d,(360,204),'일일평가서',F('Black',30),INK,'mm'); d.line([(220*S,240*S),(500*S,240*S)],fill=LINE,width=3*S)
    R(d,(220,264,500,330),12,fill=SOFT); T(d,(238,297),'Q1. Student: …',F('Medium',22),GRAY,'lm')
    R(d,(220,346,500,446),14,fill=GBG); T(d,(238,372),'BETTER EXPRESSION',F('Bold',17),GREEN,'lm'); R(d,(238,396,470,410),7,fill='#065F46'); R(d,(238,420,400,432),6,fill='#6FCFB0')
    R(d,(220,462,500,552),14,fill=ABG); T(d,(238,488),'ALTERNATIVE',F('Bold',17),AMB,'lm'); R(d,(238,512,450,526),7,fill='#92400E')
    R(d,(220,580,500,640),30,fill=CORAL); T(d,(360,610),'오늘의 복습 완료하기',F('Bold',22),WHITE,'mm')
    E(d,(486,116,574,204),fill=RED); T(d,(530,160),'1',F('Black',46),WHITE,'mm')
def f4(im,d):
    bust(im,190,330,100,600,mood='smile',**STU); d=ImageDraw.Draw(im)
    card(d,(330,190,670,480),r=26,fill=WHITE,off=7); T(d,(360,236),'실전 퀴즈',F('Bold',24),GRAY,'lm')
    T(d,(360,296),'I ____ there',F('Bold',36),INK,'lm'); T(d,(360,348),'yesterday.',F('Bold',36),INK,'lm')
    f=F('Black',36); w=tw('went',f); R(d,(360-8,400,360+w+8,448),8,fill=YEL); T(d,(360,424),'went',f,INK,'lm')
    E(d,(590,170,690,270),fill=GREEN); d.line([(614*S,222*S),(634*S,242*S),(668*S,200*S)],fill=WHITE,width=10*S,joint='curve')
    R(d,(0,600,720,720),0,fill=TINT); T(d,(360,650),'고친 문장을 내 것으로',F('Bold',32),INK,'mm')

def main(outdir):
    os.makedirs(outdir,exist_ok=True); p=lambda n: os.path.join(outdir,n)
    hero(p('hero_scene.png'))
    pain(p('pain_1.png'),'think',[(['Um… I…','yesterday… movie?'],WHITE)],'#E8F0FF')
    pain(p('pain_2.png'),'smile',[(['It was good.'],WHITE),(['It was good.'],WHITE),(['It was… good.'],WHITE)],'#FFF6D6')
    pain(p('pain_3.png'),'think',[(['I go to there','yesterday.'],WHITE),(['Okay! Next~'],YEL)],'#FFE9E4')
    pain(p('pain_4.png'),'think',[(['어제 뭐','배웠더라…?'],WHITE)],'#EAFBF4')
    for i,fn in enumerate((f1,f2,f3,f4),1): flow(p(f'flow_{i}.png'),i,fn)
if __name__=='__main__': main(sys.argv[1])
