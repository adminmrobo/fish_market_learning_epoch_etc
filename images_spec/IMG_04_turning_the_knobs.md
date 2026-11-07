# 04번 「손잡이 다시 돌리기 — Phase #2·#3와 신뢰도」 이미지 제작 명세서

| 항목 | 내용 |
|---|---|
| 페이지 | 04_turning_the_knobs.html |
| 주 앵커 | B 연구실: 조정 패널과 반복 실험 노트 |
| 분야 | 1 인공지능 (주) + 2 통계학 (보조) |
| 시즌 | 기본 |
| 대결 결과 | R, 차이 11.1%p → 결과 후 표정 doc_judge, asst_spark, fly_cry or fly_coffee, robo_happy |
| 새로 그릴 그림 | P1 1장 (cover_04) · P2 1장 (thumb_04) · P3 1장 (og_04) |
| 재사용 | 표정 15키, 모두 캐릭터 팩 1.3에 있음 |
| 그림이 없을 때 | 캐릭터 팩 그림 + CSS 대체 표지로 이미 완성 상태 |

## 1. 그림체와 고정 외형
캐릭터 팩 18-3·18-4 그대로. 이 페이지 장소: *a control panel wall in the night lab with several dial knobs of different sizes, a stack of twenty lab notebooks with blank striped pages, a few small paper targets pinned in a row*

## 2. 필요한 그림 전체
| # | 키 | 판 | 상태 | 우선 | 들어가는 곳 |
|---|---|---|---|---|---|
| 0 | cover_04 | L 1920×1080 | 새로 (COVER_04_turning_the_knobs.md) | P1 | 맨 위 글 표지 |
| 1 | thumb_04 | I 600×400 | cover_04 3:2 자르기 | P2 | 목차 카드 |
| 2 | og_04 | K 1200×630 | cover_04 자르기 | P3 | 공유 미리보기 |
| 3 | doc_think | A | 재사용 | — | 본문·대결 |
| 4 | doc_front | A | 재사용 | — | 본문·대결 |
| 5 | doc_board | A | 재사용 | — | 본문·대결 |
| 6 | doc_judge | A | 재사용 | — | 본문·대결 |
| 7 | asst_smile | B | 재사용 | — | 본문·대결 |
| 8 | asst_report | B | 재사용 | — | 본문·대결 |
| 9 | asst_spark | B | 재사용 | — | 본문·대결 |
| 10 | fly_point | C | 재사용 | — | 본문·대결 |
| 11 | fly_clip | C | 재사용 | — | 본문·대결 |
| 12 | fly_magnify | C | 재사용 | — | 본문·대결 |
| 13 | fly_cry | C | 재사용 | — | 본문·대결 |
| 14 | robo_coin | D | 재사용 | — | 본문·대결 |
| 15 | robo_smile | D | 재사용 | — | 본문·대결 |
| 16 | robo_wow | D | 재사용 | — | 본문·대결 |
| 17 | robo_happy | D | 재사용 | — | 본문·대결 |
| — | 표적지·다이얼·탄착군·노트 그림 | — | 코드 (캔버스) | — | 각 칸 '행동으로 보기' |

## 3. 체크리스트 (SKILL 18-13)
- [x] HTML의 모든 `data-img` 키가 이 표에 있음 (thumb·og는 HTML 밖)
- [x] 결과 후 표정이 캐릭터 팩 5-8 표와 일치, 결과 전(fly_point, robo_coin)에 승패 암시 없음
- [x] 표지 프롬프트에 고정 외형·금지 구절·무기 금지
- [x] 생물 앵커가 아니므로 현미경·해부 소품 없음
- [x] 새 그림 P1 1장

## 4. 매니페스트
```json
{
 "page": "04_turning_the_knobs",
 "anchor": "B 연구실: 조정 패널과 반복 실험 노트",
 "domain": [
  "ai",
  "stats"
 ],
 "season": "default",
 "duel": {
  "result": "R",
  "gap": "11.1%p"
 },
 "images": [
  {
   "key": "cover_04",
   "plate": "L",
   "size": [
    1920,
    1080
   ],
   "status": "new",
   "priority": "P1",
   "slot": "cover",
   "fallback": "css-pixel-four",
   "alt": "밤의 연구실 조정 패널 앞에서 네 캐릭터가 크기가 다른 다이얼과 쌓인 실험 노트, 벽의 표적지 여러 장을 둘러싼 표지"
  },
  {
   "key": "thumb_04",
   "plate": "I",
   "size": [
    600,
    400
   ],
   "status": "new",
   "priority": "P2",
   "slot": "index-card",
   "fallback": "color-card",
   "alt": "손잡이 다시 돌리기 — Phase #2·#3와 신뢰도"
  },
  {
   "key": "og_04",
   "plate": "K",
   "size": [
    1200,
    630
   ],
   "status": "new",
   "priority": "P3",
   "slot": "og",
   "fallback": null,
   "alt": "손잡이 다시 돌리기 — Phase #2·#3와 신뢰도"
  },
  {
   "key": "doc_think",
   "status": "reuse",
   "alt": ""
  },
  {
   "key": "doc_front",
   "status": "reuse",
   "alt": ""
  },
  {
   "key": "doc_board",
   "status": "reuse",
   "alt": ""
  },
  {
   "key": "doc_judge",
   "status": "reuse",
   "alt": ""
  },
  {
   "key": "asst_smile",
   "status": "reuse",
   "alt": ""
  },
  {
   "key": "asst_report",
   "status": "reuse",
   "alt": ""
  },
  {
   "key": "asst_spark",
   "status": "reuse",
   "alt": ""
  },
  {
   "key": "fly_point",
   "status": "reuse",
   "alt": ""
  },
  {
   "key": "fly_clip",
   "status": "reuse",
   "alt": ""
  },
  {
   "key": "fly_magnify",
   "status": "reuse",
   "alt": ""
  },
  {
   "key": "fly_cry",
   "status": "reuse",
   "alt": ""
  },
  {
   "key": "robo_coin",
   "status": "reuse",
   "alt": ""
  },
  {
   "key": "robo_smile",
   "status": "reuse",
   "alt": ""
  },
  {
   "key": "robo_wow",
   "status": "reuse",
   "alt": ""
  },
  {
   "key": "robo_happy",
   "status": "reuse",
   "alt": ""
  }
 ]
}
```
