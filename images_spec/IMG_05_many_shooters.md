# 05번 「사수 여러 명 — 앙상블은 튜닝을 넘을까」 이미지 제작 명세서

| 항목 | 내용 |
|---|---|
| 페이지 | 05_many_shooters.html |
| 주 앵커 | C 장부 + D: 표적지 여러 장, 나무 화분, 투표함 |
| 분야 | 1 인공지능 (주) + 2 통계학 (보조) |
| 시즌 | 기본 |
| 대결 결과 | R, 차이 4.4%p → 결과 후 표정 doc_judge, asst_spark, fly_cry or fly_coffee, robo_happy |
| 받은 그림 (2026-11-07) | 표지·썸네일·공유 미리보기 반영 완료, `assets/img/` |
| 처음 계획한 그림 | P1 1장 (cover_05) · P2 1장 (thumb_05) · P3 1장 (og_05) |
| 재사용 | 표정 15키, 모두 캐릭터 팩 1.3에 있음 |
| 그림이 없을 때 | 캐릭터 팩 그림 + CSS 대체 표지로 이미 완성 상태 |

## 1. 그림체와 고정 외형
캐릭터 팩 18-3·18-4 그대로. 이 페이지 장소: *a wide practice room in the night lab with three round paper targets side by side, a row of small potted trees, a simple ballot box with blank paper slips, and an instructor stand with a blank scoring sheet*

## 2. 필요한 그림 전체
| # | 키 | 판 | 상태 | 우선 | 들어가는 곳 |
|---|---|---|---|---|---|
| 0 | cover_05 | L 1920×1080 | 새로 (COVER_05_many_shooters.md) | P1 | 맨 위 글 표지 |
| 1 | thumb_05 | I 600×400 | cover_05 3:2 자르기 | P2 | 목차 카드 |
| 2 | og_05 | K 1200×630 | cover_05 자르기 | P3 | 공유 미리보기 |
| 3 | doc_think | A | 재사용 | — | 본문·대결 |
| 4 | doc_front | A | 재사용 | — | 본문·대결 |
| 5 | doc_magic | A | 재사용 | — | 본문·대결 |
| 6 | doc_judge | A | 재사용 | — | 본문·대결 |
| 7 | asst_smile | B | 재사용 | — | 본문·대결 |
| 8 | asst_report | B | 재사용 | — | 본문·대결 |
| 9 | asst_spark | B | 재사용 | — | 본문·대결 |
| 10 | fly_point | C | 재사용 | — | 본문·대결 |
| 11 | fly_clip | C | 재사용 | — | 본문·대결 |
| 12 | fly_magnify | C | 재사용 | — | 본문·대결 |
| 13 | fly_coffee | C | 재사용 | — | 본문·대결 |
| 14 | robo_coin | D | 재사용 | — | 본문·대결 |
| 15 | robo_smile | D | 재사용 | — | 본문·대결 |
| 16 | robo_chart | D | 재사용 | — | 본문·대결 |
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
 "page": "05_many_shooters",
 "anchor": "C 장부 + D: 표적지 여러 장, 나무 화분, 투표함",
 "domain": [
  "ai",
  "stats"
 ],
 "season": "default",
 "duel": {
  "result": "R",
  "gap": "4.4%p"
 },
 "images": [
  {
   "key": "cover_05",
   "plate": "L",
   "size": [
    1920,
    1080
   ],
   "status": "done",
   "priority": "P1",
   "slot": "cover",
   "fallback": "css-pixel-four",
   "alt": "밤의 연구실 연습장에서 표적지 여러 장과 작은 나무 화분 줄, 투표함 앞에 선 네 캐릭터의 표지"
  },
  {
   "key": "thumb_05",
   "plate": "I",
   "size": [
    600,
    400
   ],
   "status": "done",
   "priority": "P2",
   "slot": "index-card",
   "fallback": "color-card",
   "alt": "사수 여러 명 — 앙상블은 튜닝을 넘을까"
  },
  {
   "key": "og_05",
   "plate": "K",
   "size": [
    1200,
    630
   ],
   "status": "done",
   "priority": "P3",
   "slot": "og",
   "fallback": null,
   "alt": "사수 여러 명 — 앙상블은 튜닝을 넘을까"
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
   "key": "doc_magic",
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
   "key": "fly_coffee",
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
   "key": "robo_chart",
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
