import sys
from PIL import Image
names=sys.argv[1:]
W=Image.new('RGBA',(400*len(names),420),'#FDE3DC')
for i,n in enumerate(names): W.alpha_composite(Image.open(f'/home/claude/r3d/out/{n}.png').convert('RGBA').resize((400,420)),(i*400,0))
W.save('/tmp/t3d.png')
