#!/usr/bin/env python3
"""깔끔한 선으로 그린 그림(PNG)을 '낙서 느낌'으로 바꾼다.
- 굵은 검은 테두리선: 가늘게 만들고 삐뚤빼뚤하게 흔든 뒤 한 번 더 겹쳐 그림
- 색: 선에서 오른쪽 아래로 살짝 밀어 선 밖으로 삐져나오게 함
- 글자와 작은 점(눈 등), 검은 꼬리표는 그대로 둠
사용법: python3 doodlify.py 입력.png 출력.png [입력2.png 출력2.png ...]
필요한 것: numpy, scipy, opencv-python, pillow
"""
import sys, numpy as np, cv2
from PIL import Image
from scipy import ndimage as ndi
K = np.array([27, 27, 27], np.float32)

def doodlify(src, dst, seed=7, big=90, bg_dark=False):
    im = np.asarray(Image.open(src).convert('RGBA')).astype(np.float32)
    h, w = im.shape[:2]; rgb = im[..., :3]; al = im[..., 3] / 255.0
    lum = rgb @ np.array([.299, .587, .114], np.float32)
    chroma = rgb.max(-1) - rgb.min(-1)
    a = np.clip((58 - lum) / 22, 0, 1) * (chroma < 28) * al           # 검은 선일수록 1
    m = (a > 0.5).astype(np.uint8)
    n, lab, stats, _ = cv2.connectedComponentsWithStats(m, connectivity=8)
    cands = [i for i in range(1, n) if max(stats[i][2], stats[i][3]) >= big]
    if not cands: Image.open(src).save(dst); return 0
    cm = np.isin(lab, cands); dall = ndi.distance_transform_edt(cm)
    t = float(np.clip(4 * np.median(dall[cm]), 2.5, 26))                # 선 굵기
    line = np.zeros((h, w), bool); frozen = np.zeros((h, w), bool)
    for i in cands:
        x, y, bw, bh, area = stats[i]
        comp = lab[y:y + bh, x:x + bw] == i
        if dall[y:y + bh, x:x + bw][comp].max() > 1.5 * t:              # 굵게 칠한 검은 면(꼬리표 등): 그대로
            frozen[max(0, y - 8):y + bh + 8, max(0, x - 8):x + bw + 8] = True; continue
        line[y:y + bh, x:x + bw] |= comp
    if not line.any(): Image.open(src).save(dst); return 0
    d = ndi.distance_transform_edt(line)
    # 1) 색 층: 선 자리를 가장 가까운 색으로 메우고 오른쪽 아래로 밀기
    hole = ndi.binary_dilation(line, iterations=2)
    dark = ndi.binary_dilation(a > 0.08, iterations=1)                 # 글자·눈 등도 색 층에서는 지움
    keepa = np.where(hole, 0, a)
    hole = hole | dark
    idx = ndi.distance_transform_edt(hole, return_distances=False, return_indices=True)
    base = im[idx[0], idx[1]]
    dx, dy = min(0.85 * t, 7.0), min(0.7 * t, 6.0)
    M = np.float32([[1, 0, dx], [0, 1, dy]])
    base = cv2.warpAffine(base, M, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    # 글자·눈처럼 그대로 둘 검은 부분과 검은 면은 원래 자리에 다시 올림
    keep = np.clip(keepa, 0, 1)[..., None]
    base[..., :3] = base[..., :3] * (1 - keep) + rgb * keep; base[..., 3] = np.maximum(base[..., 3], keep[..., 0] * 255)
    base[frozen] = im[frozen]
    # 2) 선 층: 가늘게, 흔들어서, 두 번
    la = np.clip(d - 0.19 * t + 0.5, 0, 1).astype(np.float32)
    rng = np.random.default_rng(seed); yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    def wobble(alpha, amp, ox, oy, sig):
        fx = ndi.gaussian_filter(rng.standard_normal((h, w)).astype(np.float32), sig); fy = ndi.gaussian_filter(rng.standard_normal((h, w)).astype(np.float32), sig)
        fx *= amp / (np.abs(fx).max() + 1e-6); fy *= amp / (np.abs(fy).max() + 1e-6)
        return cv2.remap(alpha, xx + fx - ox, yy + fy - oy, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    l1 = wobble(la, 0.5 * t, 0, 0, 3.2 * t); l2 = wobble(la, 0.6 * t, -0.3 * t, 0.3 * t, 2.6 * t) * 0.75
    out = base.copy()
    for l in (l1, l2):
        l3 = l[..., None]
        out[..., :3] = out[..., :3] * (1 - l3) + K * l3; out[..., 3] = np.maximum(out[..., 3], l * 255)
    out[frozen] = im[frozen]
    Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)).save(dst, optimize=True); return t

if __name__ == '__main__':
    args = sys.argv[1:]
    for s, o in zip(args[0::2], args[1::2]): print(s, '->', o, 'line', round(doodlify(s, o), 1))
