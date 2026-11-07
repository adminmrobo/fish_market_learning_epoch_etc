# 01번 「판 짜기 — 무엇으로 배우고, 무엇으로 판정할까」 이미지 제작 명세서

| 항목 | 내용 |
|---|---|
| 페이지 | 01_setting_the_board.html |
| 모드 / 주 앵커 | 교과서 / B 연구실: 측정실·봉인 봉투 (보조: 시리즈 비유 '영점 잡기'는 글로만, 그림은 표적지만) |
| 분야 | 1 인공지능 (주) + 2 통계학 (보조) |
| 시즌 | 기본 |
| 대결 | k를 무엇으로 고를까? → 결과 X (주판봇 실격, 데이터 누수). 봉인 점수 초파리 77.4% · 주판봇 76.5%, 차이 0.9%p |
| 새로 그릴 그림 | P1 1장 (cover_01) · P2 1장 (thumb_01) · P3 2장 (bg_01, og_01) |
| 재사용 | 표정 15키 모두 캐릭터 팩 1.3에 있음 (공용 — IMG_00_index.md 참조) |
| 그림이 없을 때 | 페이지는 캐릭터 팩 그림 + CSS 대체 표지로 이미 완성 상태 |

## 1. 그림체와 고정 외형
- 스타일: 캐릭터 팩 18-3 (16비트 RPG 픽셀아트, 굵은 외곽선, 2~3단계 명암)
- 고정 외형: 캐릭터 팩 18-4 표 그대로, 키 순서 박사 ≥ 조수 > 주판봇 > 초파리
- 이 페이지 장소: 밤의 연구실 옆 측정실 — 측정대, 저울, 줄자, 봉인 봉투 상자, 벽의 표적지
- 장소 영어 묘사: *a measuring room beside the night lab, a long wooden measuring bench, a balance scale, a long tape measure, a box of sealed envelopes, a single round paper target on the wall*

## 2. 필요한 그림 전체

| # | 키 | 판 | 크기 | 상태 | 우선 | 들어가는 곳 | 대신 쓰는 그림 |
|---|---|---|---|---|---|---|---|
| 0 | cover_01 | L | 1920×1080 | 새로 (COVER_01_setting_the_board.md) | P1 | 맨 위 글 표지 | 대체 표지 (CSS 벌집 + 캐릭터 넷 + 표적 SVG) |
| 1 | bg_01 | F | 1920×720 | 새로 | P3 (표지 있음) | 히어로 배경 | 표지 자르기 / CSS 벌집 |
| 2 | doc_think | A | 192×192 | 재사용 | — | 히어로 첫마디, 대체 표지 | — |
| 3 | doc_front | A | 192×192 | 재사용 | — | 등장인물, 큰 그림 말풍선, 아웃트로 | — |
| 4 | doc_magic | A | 192×192 | 재사용 | — | ⑤ 말풍선 | — |
| 5 | doc_judge | A | 192×192 | 재사용 | — | 대결 판정 (결과 X) | doc_front |
| 6 | asst_smile | B | 180×220 | 재사용 | — | 히어로, 꾸러미 섹션 | — |
| 7 | asst_report | B | 180×220 | 재사용 | — | 등장인물, ④ 말풍선 | — |
| 8 | asst_shock | B | 180×220 | 재사용 | — | 대결 결과 발표 (실격) | asst_report |
| 9 | asst_spark | B | 180×220 | 재사용 | — | 아웃트로 | asst_smile |
| 10 | fly_point | C | 220×220 | 재사용 (오른쪽 보게 뒤집어 씀) | — | 히어로, ③ 말풍선, 대결 전 | — |
| 11 | fly_clip | C | 220×220 | 재사용 | — | 등장인물 | — |
| 12 | fly_magnify | C | 220×220 | 재사용 | — | ① 말풍선 | fly_point |
| 13 | fly_arms | C | 220×220 | 재사용 | — | 대결 후 (실격승), 아웃트로 | fly_clip |
| 14 | robo_coin | D | 180×200 | 재사용 | — | 히어로, 대결 전 | — |
| 15 | robo_smile | D | 180×200 | 재사용 | — | 등장인물 | — |
| 16 | robo_calc | D | 180×200 | 재사용 | — | ② 말풍선 | robo_smile |
| 17 | robo_blush | D | 180×200 | 재사용 | — | 대결 후 (실격), 아웃트로 | robo_smile |
| 18 | thumb_01 | I | 600×400 | 새로 (cover_01을 3:2로 자르기) | P2 | 시리즈 목차 카드 | 색 카드 |
| 19 | og_01 | K | 1200×630 | 새로 (cover_01 자르기) | P3 | 공유 미리보기 | 없음 |
| — | 나르미, 이웃 찾기, 봉인관, 묶음 돌기 | — | — | 코드 (캔버스) | — | 각 칸 '행동으로 보기' | — |

## 3. 새로 그릴 그림 상세

### 3-0. `cover_01` — 봉인되는 카드 무더기
COVER_01_setting_the_board.md에 지시문 전체가 있다.

### 3-1. `bg_01` — 측정실 넓은 배경 (선택)
| 항목 | 내용 |
|---|---|
| 판 · 크기 | F · 1920×720 |
| 배경 | 그림 전체 |
| 구도 | 인물 없음. 왼쪽 45%는 어둡고 단순한 벽, 오른쪽에 측정대·저울·봉인 봉투 상자·벽 표적지 |
| 소품 | 저울, 줄자, 눈금 실린더, 일곱 색 빈 카드 무더기, 봉인 봉투 상자 (글자 없음) |
| 빛·분위기 | 남보라 어둠, 봉투 상자에 호박색 빛 |
| 피할 것 | 글자, 무기, 현미경·초파리 해부 소품(생물 앵커 아님) |
| 대체 글 (alt) | 일곱 색 카드 무더기와 봉인 봉투 상자가 놓인 밤의 연구실 측정대 |
| 대신 쓰는 그림 | cover_01 자르기 |

**프롬프트 (복사해서 사용)**
```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, wide 8:3 background, left side simple and calm for title text, details on the right, a measuring room beside the night lab with a long wooden measuring bench, a brass balance scale, a long tape measure, graduated cylinders, seven neat piles of blank cards in seven soft colors, a box of sealed envelopes glowing faintly amber, a single round paper target with concentric rings on the wall, no characters, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 3-2. `thumb_01`, `og_01`
cover_01을 받은 뒤 잘라 만든다. thumb_01은 3:2(600×400, 봉투와 네 캐릭터 얼굴이 들어가게), og_01은 1200×630(가운데 기준).

## 4. 일관성 지침
- 참고 이미지: 캐릭터 팩 기본 그림 4장 + 설정샷 k01(단체), k12(키 비교)
- 같은 세션에서 연달아 생성, 시드 고정 가능하면 고정
- 투명 배경이 필요 없는 판(L·F·I·K)만 있으므로 #00ff00 처리는 해당 없음

## 5. 넘겨받은 뒤 처리
1. 크기·비율·글자 확인
2. WebP 압축: cover 1600×900 220 KB 이하, bg 1280 너비
3. `data-img` 키 자리에 넣고 재조립, 그림 합계(표지 포함 600 KB 이하) 확인 — 현재 페이지 316 KB(캐릭터 그림 약 95 KB 포함)라 표지 220 KB를 넣으면 약 540 KB
4. 표지는 SKILL 18-15 절차

## 6. 체크리스트 (SKILL 18-13)
- [x] HTML의 모든 `data-img` 키가 이 표에 있고, 이 표의 페이지 안 키가 HTML에 쓰임 (thumb_01·og_01은 목차·공유용으로 HTML 밖)
- [x] 대결 결과 후 표정이 5-8 실격 줄과 일치 (doc_judge, asst_shock, fly_arms, robo_blush)
- [x] 결과 전 그림(fly_point, robo_coin)에 승패 암시 없음
- [x] 프롬프트에 고정 외형·금지 구절, 무기 금지 추가
- [x] 장소가 B 연구실 앵커와 일치, 현미경·해부 소품 없음
- [x] 새 그림 P1 1장 (6장 이하)

## 7. 매니페스트
```json
{
  "page": "01_setting_the_board",
  "anchor": "B:measuring-room",
  "domain": ["ai", "stats"],
  "season": "default",
  "duel": {"result": "X", "gap": 0.009},
  "images": [
    {"key":"cover_01","plate":"L","size":[1920,1080],"status":"new","priority":"P1","slot":"cover","fallback":"css-pixel-four","alt":"밤의 연구실 측정대 위에 일곱 색 물고기 카드 무더기가 놓이고, 조수가 한 무더기를 봉투에 봉인하는 동안 초파리 연구원은 돋보기로 카드를 살피고 주판봇은 봉투를 엿보려 하며 박사가 벽의 표적지를 가리키는 표지"},
    {"key":"bg_01","plate":"F","size":[1920,720],"status":"new","priority":"P3","slot":"hero-bg","fallback":"cover_01","alt":"일곱 색 카드 무더기와 봉인 봉투 상자가 놓인 밤의 연구실 측정대"},
    {"key":"thumb_01","plate":"I","size":[600,400],"status":"new","priority":"P2","slot":"index-card","fallback":"color-card","alt":"Fish Market 연구실 1장 판 짜기"},
    {"key":"og_01","plate":"K","size":[1200,630],"status":"new","priority":"P3","slot":"og","fallback":null,"alt":"Fish Market 연구실 1장 판 짜기"},
    {"key":"doc_think","plate":"A","status":"reuse","slot":"hero-dialog","alt":""},
    {"key":"doc_front","plate":"A","status":"reuse","slot":"cast,map,outro","alt":""},
    {"key":"doc_magic","plate":"A","status":"reuse","slot":"lv5","alt":""},
    {"key":"doc_judge","plate":"A","status":"reuse","slot":"duel-after","alt":""},
    {"key":"asst_smile","plate":"B","status":"reuse","slot":"hero-dialog,export","alt":""},
    {"key":"asst_report","plate":"B","status":"reuse","slot":"cast,lv4","alt":""},
    {"key":"asst_shock","plate":"B","status":"reuse","slot":"duel-after","alt":""},
    {"key":"asst_spark","plate":"B","status":"reuse","slot":"outro","alt":""},
    {"key":"fly_point","plate":"C","status":"reuse","slot":"hero-dialog,lv3,duel-before","alt":""},
    {"key":"fly_clip","plate":"C","status":"reuse","slot":"cast","alt":""},
    {"key":"fly_magnify","plate":"C","status":"reuse","slot":"lv1","alt":""},
    {"key":"fly_arms","plate":"C","status":"reuse","slot":"duel-after,outro","alt":""},
    {"key":"robo_coin","plate":"D","status":"reuse","slot":"hero-dialog,duel-before","alt":""},
    {"key":"robo_smile","plate":"D","status":"reuse","slot":"cast","alt":""},
    {"key":"robo_calc","plate":"D","status":"reuse","slot":"lv2","alt":""},
    {"key":"robo_blush","plate":"D","status":"reuse","slot":"duel-after,outro","alt":""}
  ]
}
```
