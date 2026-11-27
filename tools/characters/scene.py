"""새 캐릭터(깔끔한 선)로 장면 그림을 만드는 도구. 말풍선과 캐릭터를 HTML로 놓고 PNG로 찍는다."""
import chars
from playwright.sync_api import sync_playwright
INK=chars.INK
VB={'t':'-30 -6 250 262','p':'-10 -4 250 262'}
def ch(name,h):
    if name.startswith('turtle'): body=chars.TURTLE[name]; vb=VB['t']
    else: body=chars.SET[name]; vb=VB['p']
    return svg_mid(body,vb,h)
_n=[0]
def svg_mid(body,vb,h=None):
    """중간 버전: 선은 한 번만, 손으로 그린 듯 살짝 삐뚤게."""
    _n[0]+=1; i=_n[0]; size=f' height="{h}" width="{h*250/262:.0f}" style="flex:none;display:block"' if h else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}"{size}><defs><filter id="w{i}" x="-8%" y="-8%" width="116%" height="116%"><feTurbulence type="fractalNoise" baseFrequency=".018" numOctaves="2" seed="{4+i%9}"/><feDisplacementMap in="SourceGraphic" scale="5.5"/></filter></defs><g filter="url(#w{i})">{body}</g></svg>'
COL={'w':'#FFFFFF','y':'#FFD966','m':'#A8E6CF','b':'#DCE9FF','p':'#FFE7E1'}
def bub(text,c='w',fs=40,tail=None):
    r={'l':'28px 28px 28px 6px','r':'28px 28px 6px 28px',None:'28px'}[tail]
    return f'<div style="flex:none;background:{COL[c]};border:4px solid {INK};border-radius:{r};padding:{fs*.42:.0f}px {fs*.8:.0f}px;font:700 {fs}px/1.25 \'Noto Sans CJK KR\',sans-serif;color:#2A211D;white-space:nowrap;letter-spacing:-.01em">{text}</div>'
def row(*items,gap=18,align='center',justify='center',style=''):
    return f'<div style="display:flex;align-items:{align};justify-content:{justify};gap:{gap}px;{style}">{"".join(items)}</div>'
def col(*items,gap=18,style=''):
    return f'<div style="display:flex;flex-direction:column;align-items:center;gap:{gap}px;{style}">{"".join(items)}</div>'
def panel(inner,bg='#FFFFFF'):
    return f'<div style="position:absolute;inset:4px;box-sizing:border-box;background:{bg};border:4px solid {INK};border-radius:44px;overflow:hidden;display:flex;align-items:center;justify-content:center">{inner}</div>'
def render(jobs,scale=3):
    """scale배로 그린 뒤 원래 크기로 줄인다 — 작은 캐릭터의 선이 깨지지 않게."""
    from PIL import Image
    with sync_playwright() as pw:
        b=pw.chromium.launch(executable_path='/usr/bin/google-chrome')
        for path,(w,h,html) in jobs.items():
            pg=b.new_page(viewport={'width':w,'height':h},device_scale_factor=scale)
            pg.set_content(f'<body style="margin:0;width:{w}px;height:{h}px;position:relative;overflow:hidden;background:transparent;display:flex;align-items:center;justify-content:center">{html}</body>')
            pg.screenshot(path=path,omit_background=True); pg.close()
            if scale!=1: Image.open(path).resize((w,h),Image.LANCZOS).save(path)
        b.close()
