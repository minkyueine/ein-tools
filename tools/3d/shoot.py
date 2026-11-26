import sys, subprocess, time, os
from playwright.sync_api import sync_playwright
out = sys.argv[1]; names = sys.argv[2:]; os.makedirs(out, exist_ok=True)
srv = subprocess.Popen(['python3', '-m', 'http.server', '8765'], cwd='/home/claude/r3d', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1)
try:
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/usr/bin/google-chrome', proxy={'server':'direct://'} if False else None, args=['--no-proxy-server', '--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'])
        for n in names:
            pg = b.new_page(viewport={'width': 800, 'height': 840})
            pg.on('console', lambda m: print('console', m.text)); pg.on('pageerror', lambda e: print('err', e)); pg.goto(f'http://127.0.0.1:8765/render.html?c={n}')
            pg.wait_for_function('window.done', timeout=60000); print(n, pg.evaluate('window.done'))
            pg.locator('#c').screenshot(path=f'{out}/{n}.png', omit_background=True); pg.close()
        b.close()
finally:
    srv.terminate()
