# 아인잉글리쉬 3D 출연진 (2026-11-26~)

블로그·이벤트·페이지 그림에 쓰는 고정 출연진 3명입니다. **거북이는 쓰지 않습니다.**
모두 같은 찰흙(클레이) 3D 질감, 머리부터 신발까지 나오는 전신(머리 크기 약 1/3)으로 맞췄습니다.
`_lineup.png`가 세 명이 나란히 선 기준 그림입니다.

| 인물 | 생김새 | 파일 |
|---|---|---|
| 학생 | 갈색 바가지 머리 + 머리 위 새싹 한 가닥, 하늘색 스웨터, 베이지 바지, 흰 운동화 | `student-*.png` |
| 선생님 | 필리핀 선생님, 갈색 올림머리, 노란 헤드셋(검은 마이크), 코랄 상의, 크림색 바지 | `teacher-*.png` |
| 성인 수강생 | 30대 한국 남성, 짧은 검은 머리, 둥근 안경, 민트 니트 + 흰 셔츠 깃, 남색 바지 | `adult-*.png` |

## 포즈 (배경을 지운 PNG)

- 학생: `cheer`(두 팔 번쩍) · `wave` · `phone`(휴대폰 입력) · `gift`(선물 상자) · `think`(턱에 손가락) · `present`(옆을 가리키며 소개)
- 선생님: `wave` · `thumbs`(엄지 척) · `report`(평가서 클립보드) · `explain`(옆을 가리키며 설명) · `clap`(박수) · `book`(영어책)
- 성인 수강생: `card`(카드) · `phone` · `wave` · `thumbs` · `coffee`(머그잔) · `recommend`(옆을 가리키며 추천)

상황에 맞는 포즈를 먼저 여기서 고르고, 없을 때만 새로 만듭니다.

## 새 포즈 만드는 법

Figma `generate_image`(gpt-image-2.5-flare, 1536×1024)로 한 인물의 포즈 6개를 3열×2행 시트로 만들고,
칸별로 잘라 `rembg`(isnet-general-use)로 배경을 지웁니다. 프롬프트 기본형:

> Pose sheet of ONE character shown six times in a neat 3 columns x 2 rows grid with generous empty space between poses,
> every pose full body from head to white sneakers, no overlapping, cute 3D clay-style character like premium 3D icons,
> soft matte clay texture, gentle studio lighting, pure white background, no floor shadow, no text.
> The character: (위 표의 생김새를 영어로 그대로) Poses: 1) … 6) …

생김새 문장은 바꾸지 않고 그대로 써야 같은 인물로 나옵니다.

## 쓰는 곳

- 이벤트 글 그림: `tools/3d/compose_cast.py` (`python3 tools/3d/compose_cast.py event`)
- 소품(카드·동전·선물·말풍선 등): `tools/3d/props/`
- 예전 3D 컷(`tools/3d/cut/`, 거북이 포함)은 더 이상 쓰지 않습니다.
