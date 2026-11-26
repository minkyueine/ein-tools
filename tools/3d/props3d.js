// 아인잉글리쉬 캐릭터 3D(클레이 느낌) — 학생과 거북이. render.html?c=turtle-cheer 형태로 불러 PNG로 찍는다.
import * as THREE from 'three';
import { RoundedBoxGeometry } from 'three/addons/geometries/RoundedBoxGeometry.js';

const C = {
  skin: 0xFFD9BE, hair: 0x4E3A33, blue: 0x7FAEF5, ink: 0x2E2420, pink: 0xFF9C94, white: 0xFFFFFF,
  green: 0x9CCB4E, greenDark: 0x82B33C, shell: 0x8E5A2B, shellLine: 0x6E4420, navy: 0x2F4270, belly: 0xE0B575,
  coral: 0xEC6856, yellow: 0xFFD45E, cream: 0xFFF8EC, mouth: 0xD9524A, leaf: 0x7CC04A,
};
const mat = (c, o = {}) => new THREE.MeshStandardMaterial({ color: c, roughness: o.r ?? 0.55, metalness: 0, ...o.extra });
const M = {}; for (const k in C) M[k] = mat(C[k]);
M.eyeShine = new THREE.MeshBasicMaterial({ color: 0xffffff });
M.pupil = mat(C.ink, { r: 0.25 });

function mesh(geo, m, pos = [0, 0, 0], rot = [0, 0, 0], scl = [1, 1, 1]) {
  const o = new THREE.Mesh(geo, m); o.position.set(...pos); o.rotation.set(...rot); o.scale.set(...scl);
  o.castShadow = true; o.receiveShadow = true; return o;
}
const sph = (r, seg = 48) => new THREE.SphereGeometry(r, seg, seg);
const cap = (r, l) => new THREE.CapsuleGeometry(r, l, 12, 24);

// 두 점 사이 캡슐(팔·다리)
function limb(a, b, r, m) {
  const A = new THREE.Vector3(...a), B = new THREE.Vector3(...b);
  const len = A.distanceTo(B); const o = mesh(cap(r, len), m);
  o.position.copy(A.clone().add(B).multiplyScalar(0.5));
  o.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), B.clone().sub(A).normalize());
  return o;
}
// 얼굴 위 곡선(입·눈썹·감은 눈): 머리 표면을 따라가는 튜브
function arcOnFace(center, radius, from, to, width, m, headC, headR, sx = 1) {
  const pts = [];
  for (let i = 0; i <= 24; i++) {
    const t = from + (to - from) * i / 24;
    const x = center[0] + Math.cos(t) * radius * sx, y = center[1] + Math.sin(t) * radius;
    const dx = x - headC[0], dy = y - headC[1];
    const z = headC[2] + Math.sqrt(Math.max(0, headR * headR - dx * dx - dy * dy)) + 0.015;
    pts.push(new THREE.Vector3(x, y, z));
  }
  return mesh(new THREE.TubeGeometry(new THREE.CatmullRomCurve3(pts), 40, width, 10, false), m);
}
function onFace(x, y, headC, headR, lift = 0) {
  const dx = x - headC[0], dy = y - headC[1];
  return [x, y, headC[2] + Math.sqrt(Math.max(0, headR * headR - dx * dx - dy * dy)) + lift];
}
function eyeDot(g, x, y, hc, hr, r = 0.085) {
  const p = onFace(x, y, hc, hr, -0.02);
  g.add(mesh(sph(r), M.pupil, p, [0, 0, 0], [1, 1.25, 0.6]));
  g.add(mesh(sph(r * 0.32), M.eyeShine, [p[0] + r * 0.35, p[1] + r * 0.45, p[2] + r * 0.5]));
}
function blush(g, x, y, hc, hr) {
  const p = onFace(x, y, hc, hr, -0.03);
  const b = mesh(sph(0.12), new THREE.MeshStandardMaterial({ color: C.pink, roughness: 0.9, transparent: true, opacity: 0.75 }), p, [0, 0, 0], [1.3, 0.8, 0.35]);
  b.lookAt(new THREE.Vector3(hc[0], hc[1], hc[2]).multiplyScalar(-1).add(new THREE.Vector3(...p).multiplyScalar(2)));
  g.add(b);
}

function face(g, mood, hc, hr, s = 1) {
  const ex = 0.34 * s, ey = hc[1] + 0.02 * s;
  if (mood === 'happy') {
    for (const sx of [-1, 1]) g.add(arcOnFace([hc[0] + sx * ex, ey - 0.06 * s], 0.1 * s, 0.15, Math.PI - 0.15, 0.028 * s, M.pupil, hc, hr));
    const mp = onFace(hc[0], hc[1] - 0.3 * s, hc, hr, -0.05);
    g.add(mesh(sph(0.13 * s), M.mouth, mp, [0, 0, 0], [1.1, 0.8, 0.5]));
  } else {
    for (const sx of [-1, 1]) eyeDot(g, hc[0] + sx * ex, ey, hc, hr, 0.085 * s);
    if (mood === 'worry') {
      for (const sx of [-1, 1]) g.add(arcOnFace([hc[0] + sx * ex, ey + 0.2 * s], 0.11 * s, sx > 0 ? 0.3 : Math.PI - 1.1, sx > 0 ? 1.1 : Math.PI - 0.3, 0.022 * s, M.pupil, hc, hr));
      g.add(arcOnFace([hc[0], hc[1] - 0.38 * s], 0.09 * s, 0.4, Math.PI - 0.4, 0.024 * s, M.pupil, hc, hr));
    } else if (mood === 'open') {
      const mp = onFace(hc[0], hc[1] - 0.3 * s, hc, hr, -0.05);
      g.add(mesh(sph(0.1 * s), M.mouth, mp, [0, 0, 0], [0.9, 1.1, 0.5]));
    } else {
      g.add(arcOnFace([hc[0], hc[1] - 0.2 * s], 0.11 * s, Math.PI + 0.45, 2 * Math.PI - 0.45, 0.026 * s, M.pupil, hc, hr));
    }
  }
  for (const sx of [-1, 1]) blush(g, hc[0] + sx * 0.55 * s, hc[1] - 0.17 * s, hc, hr);
}

export function student(pose = 'smile') {
  const g = new THREE.Group();
  const mood = { smile: 'smile', worry: 'worry', cheer: 'happy', book: 'happy', open: 'open' }[pose] || 'smile';
  // 몸
  g.add(mesh(cap(0.62, 0.55), M.blue, [0, 0.75, 0], [0, 0, 0], [1.08, 1, 0.85]));
  g.add(mesh(new THREE.CylinderGeometry(0.2, 0.22, 0.3, 24), M.skin, [0, 1.45, 0]));
  // 다리
  for (const sx of [-1, 1]) g.add(mesh(cap(0.2, 0.25), M.ink, [sx * 0.26, 0.12, 0.02]));
  // 머리
  const hc = [0, 2.25, 0], hr = 0.82;
  g.add(mesh(sph(hr), M.skin, hc));
  // 바가지 머리
  const hair = new THREE.SphereGeometry(hr * 1.07, 48, 32, 0, Math.PI * 2, 0, Math.PI * 0.47);
  g.add(mesh(hair, M.hair, [0, hc[1] + 0.02, -0.02], [-0.28, 0, 0]));
  const bang = new THREE.SphereGeometry(hr * 1.07, 48, 24, -Math.PI * 0.42, Math.PI * 0.84, Math.PI * 0.2, Math.PI * 0.22);
  g.add(mesh(bang, M.hair, [0, hc[1] + 0.02, 0.0], [0, Math.PI * 1.0 + Math.PI, 0]));
  const back = new THREE.SphereGeometry(hr * 1.05, 48, 32, Math.PI * 0.15, Math.PI * 0.7, 0, Math.PI * 0.62);
  g.add(mesh(back, M.hair, [0, hc[1] + 0.02, -0.04], [0, Math.PI, 0]));
  // 새싹
  const stem = new THREE.CatmullRomCurve3([new THREE.Vector3(0, 3.0, 0.05), new THREE.Vector3(0.02, 3.18, 0.04), new THREE.Vector3(0.12, 3.3, 0.02)]);
  g.add(mesh(new THREE.TubeGeometry(stem, 16, 0.035, 8), M.leaf));
  g.add(mesh(sph(0.11), M.leaf, [0.22, 3.33, 0.02], [0, 0, -0.5], [1.6, 0.6, 0.5]));
  face(g, mood, hc, hr, 0.95);
  // 귀
  for (const sx of [-1, 1]) g.add(mesh(sph(0.15), M.skin, [sx * 0.8, hc[1] - 0.05, 0], [0, 0, 0], [0.6, 1, 0.8]));
  // 팔
  const sh = [0.6, 1.15, 0];
  if (pose === 'cheer') {
    for (const sx of [-1, 1]) { g.add(limb([sx * sh[0], sh[1], 0], [sx * 1.05, 2.0, 0.15], 0.16, M.blue)); g.add(mesh(sph(0.2), M.skin, [sx * 1.1, 2.15, 0.18])); }
  } else if (pose === 'book') {
    for (const sx of [-1, 1]) { g.add(limb([sx * sh[0], sh[1], 0], [sx * 0.45, 0.75, 0.55], 0.16, M.blue)); g.add(mesh(sph(0.17), M.skin, [sx * 0.42, 0.8, 0.72])); }
    const book = new THREE.Group();
    book.add(mesh(new RoundedBoxGeometry(0.62, 0.8, 0.06, 3, 0.03), M.white, [-0.33, 0, 0], [0, 0.25, 0]));
    book.add(mesh(new RoundedBoxGeometry(0.62, 0.8, 0.06, 3, 0.03), M.white, [0.33, 0, 0], [0, -0.25, 0]));
    book.add(mesh(new RoundedBoxGeometry(1.3, 0.84, 0.05, 3, 0.02), M.coral, [0, 0, -0.1]));
    book.position.set(0, 0.85, 0.78); book.rotation.x = -0.35; g.add(book);
  } else {
    for (const sx of [-1, 1]) { g.add(limb([sx * sh[0], sh[1], 0], [sx * 0.82, 0.45, 0.1], 0.16, M.blue)); g.add(mesh(sph(0.19), M.skin, [sx * 0.85, 0.36, 0.12])); }
  }
  return g;
}

export function turtle(pose = 'point') {
  const g = new THREE.Group();
  const mood = { cheer: 'open', point: 'calm', paper: 'calm', coffee: 'tired' }[pose] || 'calm';
  // 등껍질 (뒤쪽, 살짝 보이게)
  g.add(mesh(sph(0.95), M.shell, [0.1, 0.95, -0.42], [0, 0, 0], [1.05, 1.0, 0.55]));
  for (let i = 0; i < 3; i++) g.add(mesh(new THREE.TorusGeometry(0.22, 0.03, 8, 24), M.shellLine, [0.82, 0.55 + i * 0.4, -0.35], [0, Math.PI / 2.4, 0], [0.6, 1, 1]));
  // 다리
  for (const sx of [-1, 1]) g.add(mesh(cap(0.22, 0.2), M.green, [sx * 0.33, 0.15, 0.05]));
  // 배·셔츠 몸통
  g.add(mesh(cap(0.72, 0.45), M.white, [0, 0.9, 0], [0, 0, 0], [1.1, 1, 0.9]));
  g.add(mesh(sph(0.66), M.belly, [0, 0.45, 0.06], [0, 0, 0], [1.15, 0.55, 0.95]));
  // 목 + 칼라 + 넥타이
  g.add(mesh(new THREE.CylinderGeometry(0.28, 0.32, 0.3, 24), M.green, [0, 1.6, 0]));
  for (const sx of [-1, 1]) g.add(mesh(new RoundedBoxGeometry(0.34, 0.2, 0.08, 3, 0.03), M.white, [sx * 0.2, 1.5, 0.52], [-0.3, 0, sx * -0.55]));
  g.add(mesh(new THREE.ConeGeometry(0.12, 0.5, 4), M.navy, [0, 1.1, 0.68], [Math.PI - 0.15, Math.PI / 4, 0], [1, 1, 0.5]));
  g.add(mesh(sph(0.09), M.navy, [0, 1.43, 0.62], [0, 0, 0], [1.2, 1, 0.6]));
  // 머리
  const hc = [0, 2.35, 0.05], hr = 0.95;
  g.add(mesh(sph(hr), M.green, hc, [0, 0, 0], [1.12, 0.96, 1]));
  // 큰 눈 (흰자 + 눈동자 + 반쯤 감긴 눈꺼풀)
  for (const sx of [-1, 1]) {
    const ep = [sx * 0.36, hc[1] + 0.12, 0.78];
    g.add(mesh(sph(0.27), M.white, ep, [0, 0, 0], [1, 1, 0.7]));
    g.add(mesh(sph(0.14), M.pupil, [ep[0] + sx * -0.02, ep[1] - 0.05, ep[2] + 0.14], [0, 0, 0], [1, 1, 0.6]));
    g.add(mesh(sph(0.045), M.eyeShine, [ep[0] + 0.05, ep[1] - 0.0, ep[2] + 0.23]));
    const lid = new THREE.SphereGeometry(0.285, 32, 16, 0, Math.PI * 2, 0, Math.PI * 0.5);
    g.add(mesh(lid, M.greenDark, ep, [0.35, 0, sx * 0.12], [1, 1, 0.72]));
    // 눈썹
    g.add(limb([ep[0] - 0.14, ep[1] + 0.36 - sx * 0.03, 0.75], [ep[0] + 0.14, ep[1] + 0.36 + sx * 0.03, 0.75], 0.028, M.pupil));
  }
  // 볼
  for (const sx of [-1, 1]) g.add(mesh(sph(0.14), new THREE.MeshStandardMaterial({ color: C.pink, roughness: 0.9, transparent: true, opacity: 0.7 }), [sx * 0.72, hc[1] - 0.28, 0.62], [0, sx * 0.6, 0], [1.3, 0.8, 0.3]));
  // 입
  const mz = 0.9, my = hc[1] - 0.42;
  if (mood === 'open') g.add(mesh(sph(0.13), M.mouth, [0, my, mz], [0, 0, 0], [1.2, 0.9, 0.5]));
  else {
    const pts = []; for (let i = 0; i <= 16; i++) { const t = Math.PI + 0.5 + (Math.PI - 1) * i / 16; pts.push(new THREE.Vector3(Math.cos(t) * 0.13, my + 0.08 + Math.sin(t) * 0.1 * (mood === 'tired' ? -1 : 1) + (mood === 'tired' ? -0.12 : 0), mz)); }
    g.add(mesh(new THREE.TubeGeometry(new THREE.CatmullRomCurve3(pts), 24, 0.03, 8), M.pupil));
  }
  for (const sx of [-1, 1]) g.add(mesh(sph(0.025), M.pupil, [sx * 0.06, hc[1] - 0.2, 0.95]));
  // 팔
  const sh = [0.72, 1.25, 0.05];
  const hand = (p) => g.add(mesh(sph(0.2), M.green, p));
  if (pose === 'cheer') {
    for (const sx of [-1, 1]) { g.add(limb([sx * sh[0], sh[1], 0], [sx * 1.15, 2.05, 0.2], 0.17, M.green)); hand([sx * 1.2, 2.2, 0.22]); }
  } else if (pose === 'point') {
    g.add(limb([-sh[0], sh[1], 0], [-0.95, 0.55, 0.15], 0.17, M.green)); hand([-0.98, 0.45, 0.17]);
    g.add(limb([sh[0], sh[1], 0], [1.45, 1.6, 0.35], 0.17, M.green)); hand([1.55, 1.68, 0.38]);
  } else if (pose === 'paper') {
    for (const sx of [-1, 1]) { g.add(limb([sx * sh[0], sh[1], 0], [sx * 0.5, 0.85, 0.7], 0.17, M.green)); hand([sx * 0.52, 0.85, 0.82]); }
    const pg = new THREE.Group();
    pg.add(mesh(new RoundedBoxGeometry(1.0, 0.75, 0.05, 3, 0.03), M.white));
    pg.add(mesh(new RoundedBoxGeometry(0.42, 0.08, 0.02, 2, 0.01), M.coral, [-0.2, 0.22, 0.035]));
    for (let i = 0; i < 3; i++) pg.add(mesh(new RoundedBoxGeometry(0.72 - i * 0.12, 0.06, 0.02, 2, 0.01), i === 2 ? M.yellow : new THREE.MeshStandardMaterial({ color: 0xE2DCD6 }), [-0.06 - i * 0.06, 0.06 - i * 0.14, 0.035]));
    pg.position.set(0, 0.95, 0.95); pg.rotation.x = -0.2; g.add(pg);
  } else if (pose === 'coffee') {
    g.add(limb([-sh[0], sh[1], 0], [-0.95, 0.55, 0.15], 0.17, M.green)); hand([-0.98, 0.45, 0.17]);
    g.add(limb([sh[0], sh[1], 0], [1.0, 0.95, 0.6], 0.17, M.green)); hand([1.02, 0.95, 0.72]);
    g.add(mesh(new THREE.CylinderGeometry(0.2, 0.16, 0.42, 24), M.white, [1.1, 1.2, 0.8]));
  }
  return g;
}

export function renderInto(canvas, build, opts = {}) {
  const r = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true, preserveDrawingBuffer: true });
  r.setPixelRatio(1); r.setClearColor(0x000000, 0); r.shadowMap.enabled = true; r.shadowMap.type = THREE.PCFSoftShadowMap;
  r.outputColorSpace = THREE.SRGBColorSpace; r.toneMapping = THREE.NeutralToneMapping; r.toneMappingExposure = 1.0;
  const scene = new THREE.Scene();
  scene.add(new THREE.HemisphereLight(0xffffff, 0xF6E2DA, 1.7));
  const key = new THREE.DirectionalLight(0xffffff, 2.0); key.position.set(3, 6, 6); key.castShadow = true;
  key.shadow.mapSize.set(2048, 2048); key.shadow.radius = 6; key.shadow.bias = -0.0008;
  Object.assign(key.shadow.camera, { left: -4, right: 4, top: 5, bottom: -2 }); scene.add(key);
  const rim = new THREE.DirectionalLight(0xFFE7D6, 0.9); rim.position.set(-4, 3, -3); scene.add(rim);
  const obj = build(); obj.rotation.y = opts.turn ?? -0.25; scene.add(obj);
  const cam = new THREE.PerspectiveCamera(26, canvas.width / canvas.height, 0.1, 100);
  cam.position.set(0, 2.2, 11); cam.lookAt(0, 1.6, 0);
  r.render(scene, cam);
}

// ---- 소품 ----
export function prop(name) {
  const g = new THREE.Group();
  if (name === 'card') {
    const c = new THREE.Group();
    c.add(mesh(new RoundedBoxGeometry(2.6, 1.65, 0.12, 4, 0.14), M.coral));
    c.add(mesh(new RoundedBoxGeometry(2.6, 0.3, 0.02, 2, 0.01), M.ink, [0, 0.35, 0.065]));
    c.add(mesh(new RoundedBoxGeometry(0.5, 0.38, 0.03, 3, 0.05), M.yellow, [-0.8, -0.15, 0.07]));
    for (let i = 0; i < 4; i++) c.add(mesh(new RoundedBoxGeometry(0.34, 0.1, 0.02, 2, 0.02), M.cream, [-0.85 + i * 0.45, -0.55, 0.07]));
    c.rotation.set(-0.25, 0.45, 0.22); c.position.y = 1.6; g.add(c);
    const c2 = c.clone(); c2.traverse(o => { if (o.material === M.coral) o.material = mat(0x7FAEF5); });
    c2.position.set(-0.5, 1.25, -0.6); c2.rotation.set(-0.2, 0.5, 0.45); g.add(c2);
  } else if (name === 'coins' || name === 'coin') {
    const coinMat = mat(0xFFC93C, { r: 0.35 }); const edge = mat(0xE8A920, { r: 0.4 });
    const coin = (x, y, z, rx = Math.PI / 2, rz = 0) => {
      const o = new THREE.Group();
      o.add(mesh(new THREE.CylinderGeometry(0.62, 0.62, 0.16, 48), edge));
      o.add(mesh(new THREE.CylinderGeometry(0.5, 0.5, 0.18, 48), coinMat));
      o.position.set(x, y, z); o.rotation.set(rx, 0, rz); g.add(o);
    };
    if (name === 'coin') coin(0, 1.6, 0, Math.PI / 2 - 0.2, 0.3);
    else { for (let i = 0; i < 5; i++) coin(-0.5, 0.2 + i * 0.17, 0, 0, 0); for (let i = 0; i < 3; i++) coin(0.75, 0.2 + i * 0.17, 0.3, 0, 0); coin(0.2, 1.9, 0.4, Math.PI / 2 - 0.3, 0.4); }
  } else if (name === 'gift') {
    g.add(mesh(new RoundedBoxGeometry(1.8, 1.4, 1.8, 4, 0.12), M.coral, [0, 0.7, 0]));
    g.add(mesh(new RoundedBoxGeometry(2.0, 0.4, 2.0, 4, 0.12), mat(0xF07D6C), [0, 1.55, 0]));
    g.add(mesh(new RoundedBoxGeometry(0.34, 1.82, 2.04, 2, 0.06), M.yellow, [0, 0.92, 0]));
    g.add(mesh(new RoundedBoxGeometry(2.04, 1.82, 0.34, 2, 0.06), M.yellow, [0, 0.92, 0]));
    for (const sx of [-1, 1]) g.add(mesh(new THREE.TorusGeometry(0.34, 0.12, 16, 32), M.yellow, [sx * 0.34, 1.95, 0], [0, 0, sx * 0.5], [1, 0.8, 0.8]));
    g.rotation.y = 0.6;
  } else if (name === 'star') {
    const shape = new THREE.Shape(); for (let i = 0; i < 10; i++) { const r = i % 2 ? 0.48 : 1.05, t = Math.PI / 2 + i * Math.PI / 5; i ? shape.lineTo(Math.cos(t) * r, Math.sin(t) * r) : shape.moveTo(Math.cos(t) * r, Math.sin(t) * r); }
    const geo = new THREE.ExtrudeGeometry(shape, { depth: 0.3, bevelEnabled: true, bevelThickness: 0.14, bevelSize: 0.12, bevelSegments: 8 }); geo.center();
    g.add(mesh(geo, mat(0xFFC93C, { r: 0.35 }), [0, 1.5, 0], [0.15, -0.35, 0.12]));
  } else if (name === 'bubble') {
    g.add(mesh(new RoundedBoxGeometry(2.4, 1.5, 0.5, 6, 0.4), M.white, [0, 1.7, 0]));
    g.add(mesh(new THREE.ConeGeometry(0.28, 0.6, 24), M.white, [-0.6, 0.85, 0], [0, 0, -0.5]));
    for (let i = 0; i < 3; i++) g.add(mesh(sph(0.17), M.coral, [-0.6 + i * 0.6, 1.7, 0.27], [0, 0, 0], [1, 1, 0.5]));
    g.rotation.set(0.05, 0.35, 0.05);
  } else if (name === 'bag') {
    const nav = mat(0x2DB46B);
    g.add(mesh(new RoundedBoxGeometry(1.9, 2.1, 1.0, 4, 0.12), nav, [0, 1.05, 0]));
    g.add(mesh(new THREE.TorusGeometry(0.45, 0.08, 12, 32, Math.PI), M.ink, [0, 2.1, 0]));
    g.add(mesh(new THREE.CylinderGeometry(0.48, 0.48, 0.06, 40), M.white, [0, 1.05, 0.5], [Math.PI / 2, 0, 0]));
    g.add(mesh(sph(0.2), M.coral, [-0.12, 1.12, 0.55], [0, 0, 0], [1, 1, 0.4])); g.add(mesh(sph(0.2), M.coral, [0.12, 1.12, 0.55], [0, 0, 0], [1, 1, 0.4]));
    g.add(mesh(new THREE.ConeGeometry(0.29, 0.32, 24), M.coral, [0, 0.88, 0.55], [Math.PI, 0, 0], [1, 1, 0.4]));
    g.rotation.y = 0.45;
  }
  return g;
}
