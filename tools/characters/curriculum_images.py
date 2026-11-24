import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import art_lib as A
from art_lib import *
DARK='#1f2430'
def stairs():
    base=540; b=''
    steps=[('Lv.1',MINT,90),('Lv.2~3',YEL,180),('Lv.4~6',BLUE,270),('Lv.7~10',CORAL,360)]
    x=470
    for lab,fill,h in steps:
        b+=box(x,base-h,220,h+60,fill,26)+text(x+110,base-h+50,lab,44, color='#ffffff' if fill==CORAL else K)
        x+=228
    b+=f'<g {W}>{student(210,330,0.82,"worry")}</g>'+bubble(40,30,400,110,'#ffffff',(230,190),['나는 어디쯤일까?'],42)
    b+=mascot(1268,82,0.56,'cheer')+spark(1120,110,18)+spark(1400,150,14,MINT)+note(1150,60)
    b+=f'<path d="M500,400 Q640,300 720,310 M740,300 L720,312 L734,330" fill="none" stroke="{K}" stroke-width="0"/>'
    return 1440,540,TINT,b
def level():
    b=framed(20,20,300,300,PINK_BG,teacher(140,170,0.85,'point'))
    return 340,340,DARK,b
def match():
    b=framed(110,60,300,320,BLUE_BG,student(150,190,0.85,'cheer'))+framed(790,60,300,320,PINK_BG,teacher(150,180,0.85,'none'))
    b+=burst(600,130,112,YEL,'딱 맞는 교재!',44)+mascot(600,318,0.52,'cheer')+note(470,300)+spark(730,290,18,MINT)
    return 1200,420,'#f7f7f7',b
def scenes():
    s={}
    for name,fn in (('map_stairs.png',stairs),('map_level.png',level),('map_match.png',match)):
        A._defs.clear(); w,h,bg,body=fn(); s[name]=(w,h,bg,body,''.join(A._defs))
    return s
A.scenes=scenes
A.main(sys.argv[1])
