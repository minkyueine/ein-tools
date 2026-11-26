"""이벤트 글 공통 부품(211·887과 같은 형식). 각 글의 build.py에서 import 해서 쓴다."""
INK = '#2A211D'; CORAL = '#EC6856'; DEEP = '#C4452F'
PAD = 'clamp(20px, 5vw, 32px)'
FONT = "Pretendard, 'Noto Sans KR', sans-serif"


def wrap(inner):
    return f'''<div style="max-width: 640px; margin: 0 auto; font-family: {FONT}; color: #333; font-size: 16px; line-height: 1.6; word-break: keep-all">
{inner}
</div>'''


def banner(src, alt):
    return f'<div style="max-width: 480px; margin: 0 auto 36px; padding: 0 {PAD}"><img src="{src}" alt="{alt}" style="display: block; width: 100%; height: auto; border-radius: 16px"></div>\n'


def section(inner, top=48):
    return f'<section style="padding: {top}px {PAD} 0">\n{inner}\n</section>\n'


def intro(html):
    return f'<p style="margin: 0; font-size: 18px; line-height: 1.7; text-align: center">{html}</p>'


def img(src, alt, maxw='100%', top=20):
    return f'<div style="margin-top: {top}px"><img src="{src}" alt="{alt}" style="display: block; width: 100%; max-width: {maxw}; height: auto"></div>'


def h2(no, text):
    badge = f'<span style="flex: none; display: inline-flex; align-items: center; justify-content: center; width: 32px; height: 32px; border-radius: 50%; background: {CORAL}; color: #FFF; font-size: 17px">{no}</span>' if no else ''
    return f'<h2 style="margin: 0; display: flex; align-items: center; gap: 10px; font-size: 24px; line-height: 1.35; font-weight: 800; color: {INK}">{badge}{text}</h2>'


def card(emoji, bg, label, body):
    lab = f'<div style="font-size: 15px; font-weight: 700; color: #7A6F6A">{label}</div>' if label else ''
    return f'''<div style="display: flex; gap: 14px; align-items: flex-start; padding: 18px; background: {bg}; border: 2px solid {INK}; border-radius: 18px">
<div style="flex: none; width: 44px; height: 44px; border-radius: 50%; background: #FFF; border: 2px solid {INK}; display: flex; align-items: center; justify-content: center; font-size: 22px">{emoji}</div>
<div>{lab}<div style="margin-top: 2px; font-size: 18px; font-weight: 800; line-height: 1.45; color: {INK}">{body}</div></div></div>'''


def grid(*items, gap=12, top=20):
    return f'<div style="display: grid; gap: {gap}px; margin-top: {top}px">\n' + '\n'.join(items) + '\n</div>'


def sub(text):
    return f'<span style="display: block; margin-top: 2px; font-size: 16px; font-weight: 600; line-height: 1.55; color: #555">{text}</span>'


def p(text, top=12, size=15, color='#666', center=False):
    al = '; text-align: center' if center else ''
    return f'<p style="margin: {top}px 0 0; font-size: {size}px; line-height: 1.6; color: {color}{al}">{text}</p>'


def li(text):
    return f'<li style="position: relative; padding-left: 18px; margin-top: 10px"><span style="position: absolute; left: 2px; top: 11px; width: 6px; height: 6px; border-radius: 50%; background: {CORAL}"></span>{text}</li>'


def notes(title, items, bg='#F7F7F7', extra=''):
    lis = '\n'.join(li(t) for t in items)
    return f'''<div style="padding: 22px; background: {bg}; border-radius: 18px">
<div style="font-size: 18px; font-weight: 800; color: {INK}">{title}</div>
<ul style="margin: 6px 0 0; padding: 0; list-style: none; font-size: 16px; color: #444">
{lis}
</ul>{extra}</div>'''


def step(no, title, body, bg='#FFF'):
    return f'''<div style="display: flex; gap: 14px; align-items: flex-start; padding: 16px 18px; background: {bg}; border: 2px solid {INK}; border-radius: 18px">
<div style="flex: none; display: inline-flex; align-items: center; justify-content: center; min-width: 54px; height: 30px; padding: 0 8px; border-radius: 15px; background: {CORAL}; border: 2px solid {INK}; color: #FFF; font-size: 14px; font-weight: 800">STEP {no}</div>
<div><div style="font-size: 18px; font-weight: 800; line-height: 1.45; color: {INK}">{title}</div>{f'<div style="margin-top: 2px; font-size: 15px; line-height: 1.55; color: #666">{body}</div>' if body else ''}</div></div>'''


def check(t):
    return f'<div style="display: flex; gap: 10px; align-items: center; padding: 14px 16px; background: #FFF; border: 2px solid {INK}; border-radius: 14px; font-size: 17px; font-weight: 700; line-height: 1.45; color: {INK}"><span style="flex: none; display: inline-flex; align-items: center; justify-content: center; width: 26px; height: 26px; border-radius: 50%; background: #A8E6CF; border: 2px solid {INK}; font-size: 14px">✓</span><span>{t}</span></div>'


def qa(q, a):
    return f'''<div style="padding: 18px 0; border-top: 1px solid #EEE4E0">
<div style="font-size: 17px; font-weight: 800; line-height: 1.5; color: {INK}"><span style="color: {CORAL}">Q.</span> {q}</div>
<div style="margin-top: 6px; font-size: 16px; line-height: 1.6; color: #555">{a}</div></div>'''


def faq(*pairs):
    return f'<h2 style="margin: 0 0 6px; font-size: 24px; line-height: 1.35; font-weight: 800; color: {INK}">💬 자주 묻는 질문</h2>\n' + '\n'.join(qa(q, a) for q, a in pairs)


def link_btn(href, text, top=16):
    return f'<div style="margin-top: {top}px; text-align: center"><a href="{href}" style="display: inline-flex; align-items: center; min-height: 44px; padding: 0 20px; border-radius: 22px; background: #FFF; border: 2px solid {INK}; color: {INK}; font-size: 16px; font-weight: 700; text-decoration: none">{text}</a></div>'


def cta(title, desc, primary, secondary=None, bg='#FFF6D6'):
    """primary/secondary = (href, text)"""
    b = f'<a href="{primary[0]}" style="display: flex; align-items: center; justify-content: center; min-height: 54px; border-radius: 27px; background: {CORAL}; border: 2px solid {INK}; color: #FFF; font-size: 18px; font-weight: 800; text-decoration: none">{primary[1]}</a>'
    if secondary:
        b += f'\n<a href="{secondary[0]}" style="display: flex; align-items: center; justify-content: center; min-height: 50px; border-radius: 25px; background: #FFF; border: 2px solid {INK}; color: {INK}; font-size: 16px; font-weight: 700; text-decoration: none">{secondary[1]}</a>'
    d = f'<p style="margin: 8px 0 0; font-size: 16px; color: #666">{desc}</p>' if desc else ''
    return f'''<section style="margin-top: 48px; padding: 36px {PAD} 40px; background: {bg}; text-align: center">
<div style="font-size: 22px; font-weight: 800; line-height: 1.45; color: {INK}">{title}</div>
{d}
<div style="display: grid; gap: 10px; max-width: 360px; margin: 22px auto 0">
{b}
</div>
</section>
'''


def table(head, rows, first_w='30%'):
    """head: 열 제목 목록, rows: [[칸,...]]"""
    th = ''.join(f'<th style="padding: 12px 6px; font-size: 15px; font-weight: 800; text-align: center{"; width: " + first_w if i == 0 else ""}">{h}</th>' for i, h in enumerate(head))
    body = ''
    for r, cells in enumerate(rows):
        bg = '#FFFFFF' if r % 2 == 0 else '#FFF9F7'
        tds = ''.join((f'<th scope="row" style="padding: 12px 8px; font-size: 15px; font-weight: 800; color: {INK}; text-align: center; border-top: 1px solid #F1E4DF">{c}</th>' if i == 0 else
                       f'<td style="padding: 12px 8px; font-size: 15px; line-height: 1.5; color: #444; text-align: center; border-top: 1px solid #F1E4DF">{c}</td>') for i, c in enumerate(cells))
        body += f'<tr style="background: {bg}">{tds}</tr>'
    return f'''<div style="margin-top: 16px; border: 2px solid {INK}; border-radius: 18px; overflow: hidden">
<table style="width: 100%; border-collapse: collapse">
<thead><tr style="background: {CORAL}; color: #FFF">{th}</tr></thead>
<tbody>{body}</tbody>
</table></div>'''


def write(here, cdn, title_lines, banner_alt, build):
    """post.html(사이트용: 배너+본문)과 preview.html(로컬 미리보기)을 쓴다."""
    import os
    post = banner(cdn + 'banner.jpg', banner_alt) + build(cdn)
    open(os.path.join(here, 'post.html'), 'w').write(post)
    open(os.path.join(here, 'preview.html'), 'w').write(f'''<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>미리보기</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css"></head>
<body style="margin:0;background:#fff"><div style="max-width:640px;margin:0 auto;padding:24px 0">
<div style="text-align:center;font-family:Pretendard,sans-serif"><div style="color:#666;font-size:15px">이벤트</div><h1 style="margin:10px 0 20px;font-size:30px;line-height:1.35">{'<br>'.join(title_lines)}</h1></div>
{banner('banner.jpg', banner_alt)}{build('')}</div></body></html>''')
    return post
