import sys; import os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import art_lib as A
from art_lib import *
NAVY='#6F86C9'
import re
def doodle(body):
    def rep(m):
        el=m.group(0)
        f=re.search(r'fill="([^"]+)"',el); st=re.search(r'stroke="([^"]+)"',el)
        if not f or not st or f.group(1)=='none' or st.group(1)!=K: return el
        fill=re.sub(r' stroke="[^"]+"','',el); fill=re.sub(r' stroke-width="[^"]+"','',fill)
        line=el.replace(f.group(0),'fill="none"'); line=re.sub(r'stroke-width="([\d.]+)"',lambda w:f'stroke-width="{float(w.group(1))*0.62:.1f}"',line)
        return f'<g transform="translate(6,5)">{fill}</g>{line}<g transform="translate(-2,2) rotate(0.5)" opacity="0.75">{line}</g>'
    return re.sub(r'<(path|ellipse|circle|rect|polygon)\b[^>]*/>',rep,body)

def kid(cx,cy,s=1.0,mood='happy'):
    g=f'<g transform="translate({cx},{cy}) scale({s})">'
    if mood=='cheer': g+=A._arm(-80,150,-140,112,-142,26,YEL)+A._arm(80,150,140,112,142,26,YEL)
    for sx in (-1,1):
        g+=f'<ellipse cx="{sx*112}" cy="-40" rx="34" ry="44" fill="#4A4038" stroke="{K}" stroke-width="7" transform="rotate({sx*24} {sx*112} -40)"/>'
        g+=f'<circle cx="{sx*90}" cy="-66" r="13" fill="{CORAL}" stroke="{K}" stroke-width="6"/>'
    g+=f'<path d="M-74,84 Q-104,190 -94,270 L94,270 Q104,190 74,84 Z" fill="{YEL}" stroke="{K}" stroke-width="7" stroke-linejoin="round"/>'
    g+=f'<path d="M-28,98 Q0,128 28,98" fill="none" stroke="{K}" stroke-width="6" stroke-linecap="round"/>'
    g+=f'<ellipse cx="0" cy="0" rx="98" ry="90" fill="{SK}" stroke="{K}" stroke-width="7"/>'
    g+=f'<path d="M-96,-6 Q-104,-98 0,-102 Q104,-98 96,-6 Q60,-58 0,-40 Q-60,-58 -96,-6 Z" fill="#4A4038" stroke="{K}" stroke-width="7" stroke-linejoin="round"/>'
    return g+A._face(mood)+'</g>'
def adult(cx,cy,s=1.0,mood='happy'):
    g=f'<g transform="translate({cx},{cy}) scale({s})">'
    if mood=='cheer': g+=A._arm(-88,150,-150,110,-150,20,NAVY)+A._arm(88,150,150,110,150,20,NAVY)
    g+=f'<path d="M-86,80 Q-124,190 -112,270 L112,270 Q124,190 86,80 Z" fill="{NAVY}" stroke="{K}" stroke-width="7" stroke-linejoin="round"/>'
    g+=f'<path d="M-40,84 L0,132 L40,84 L22,150 L0,132 L-22,150 Z" fill="#ffffff" stroke="{K}" stroke-width="6" stroke-linejoin="round"/>'
    g+=f'<path d="M0,134 L-12,190 L0,214 L12,190 Z" fill="{CORAL}" stroke="{K}" stroke-width="6" stroke-linejoin="round"/>'
    g+=f'<ellipse cx="0" cy="0" rx="98" ry="90" fill="{SK}" stroke="{K}" stroke-width="7"/>'
    g+=f'<path d="M-96,-10 Q-106,-100 0,-104 Q106,-100 96,-10 Q86,-56 30,-58 Q-50,-56 -96,-10 Z" fill="#3A332E" stroke="{K}" stroke-width="7" stroke-linejoin="round"/>'
    g+=A._face(mood)
    g+=f'<circle cx="-31" cy="8" r="24" fill="none" stroke="{K}" stroke-width="5"/><circle cx="31" cy="8" r="24" fill="none" stroke="{K}" stroke-width="5"/><path d="M-7,6 Q0,1 7,6" fill="none" stroke="{K}" stroke-width="5" stroke-linecap="round"/>'
    return g+'</g>'
def hero():
    b=framed(60,230,380,400,YEL_BG,kid(190,210,1.0,'cheer'))+framed(530,230,380,400,PINK_BG,teacher(180,220,1.0,'point'))+framed(1000,230,380,400,BLUE_BG,adult(190,215,1.0,'cheer'))
    b+=bubble(50,40,400,140,'#ffffff',(210,236),['I like apples!'],48)
    b+=burst(720,112,104,YEL,'Great!',58)
    b+=bubble(960,40,440,140,'#ffffff',(1200,236),["I've worked here","for five years."],42)
    b+=text(250,676,'주니어 5~16세',44)+text(720,676,'선생님',44)+text(1190,676,'성인',44)
    b+=spark(480,300,20)+spark(960,560,16,MINT)+note(476,540)
    return 1440,730,TINT,b
def fix(who,bg,wrong,right,x1,x2):
    h1=56+46*len(wrong); h2=56+46*len(right); y2=36+h1+80; yb=y2+h2; H=max(587,yb+175)
    b=bubble(280,36,400,h1,'#ffffff',(236,36+h1/2+34),wrong,40)
    b+=strike(x1,x2,36+h1/2-(0 if len(wrong)==1 else 24))
    b+=arrow(480,36+h1+12)
    b+=bubble(280,y2,400,h2,YEL,(590,yb+34),right,40)
    b+=f'<g {W}>{who(150,H-190,0.82,"cheer")}</g>'+mascot(600,yb+100,0.42,'cheer')+spark(690,yb+70,16,MINT)+note(500,yb+120)
    return 720,H,bg,b
def scenes():
    s={}
    for name,fn in (('basic_hero.png',hero),
        ('basic_junior.png',lambda:fix(kid,YEL_BG,['I like apple.'],['I like apples!'],350,610)),
        ('basic_adult.png',lambda:fix(adult,BLUE_BG,["I'm working here",'since 2020.'],["I've worked here",'since 2020.'],330,630))):
        A._defs.clear(); w,h,bg,body=fn(); s[name]=(w,h,bg,body,''.join(A._defs))
    return s
A.scenes=scenes
A.main(sys.argv[1])
