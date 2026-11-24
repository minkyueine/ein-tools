import sys,os
from scene import *
out=sys.argv[1]; os.makedirs(out,exist_ok=True)
J={}
J['scene-1.png']=(1200,806,panel(col(
    row(bub('수업은 어떻게 듣는 거지…?','w',44),),
    row(ch('student-worry',215),ch('turtle-coffee',190),gap=150,style='margin-left:300px'),
    bub('하나씩 알려 드릴게요!','y',44),
    ch('teacher-smile',235),gap=14,style='margin-top:30px')))
J['scene-2.png']=(1200,758,panel(col(bub('Can you introduce yourself?','y',44),ch('teacher-soft',200),bub('Hi! Nice to meet you!','m',44),ch('student-smile',200),gap=14,style='margin-top:26px'),'#EAF1FF'))
J['scene-3.png']=(744,152,row(ch('turtle-point',150),bub('이어폰까지 챙기면 준비 끝!','w',38,'l')))
J['scene-4.png']=(884,184,row(ch('student-cheer',182),bub('5분 전에 미리 들어와 있을게요!','m',38,'l')))
J['scene-5.png']=(507,163,row(ch('student-worry',161),bub('앗, 늦었다…!','w',40,'l')))
J['scene-6.png']=(953,310,col(row(bub('Could you speak slowly, please?','w',38,'r'),ch('teacher-smile',150),gap=22),row(bub('Sure! No problem!','y',38,'r'),style='margin-left:330px;margin-top:8px'),gap=0))
J['scene-7.png']=(1200,409,panel(row(col(bub('He always try…','w',36),ch('student-worry',200),gap=12),col(bub('tries! 평가서에 적어 둘게요','y',36),ch('teacher-soft',200),gap=12),gap=70,align='flex-start',style='margin-top:36px')))
J['scene-8.png']=(795,166,row(ch('turtle-point',164),bub('전화 없이, 클릭 몇 번이면 끝!','y',38,'l')))
J['scene-9.png']=(682,159,row(ch('turtle-paper',157),bub('날짜 말고, 횟수로 세요!','w',38,'l')))
render({f'{out}/{k}':v for k,v in J.items()})
