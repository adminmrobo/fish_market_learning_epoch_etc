# 02번 「손실 함수와 경사하강법 — 상자를 열어 영점 잡기」 이미지 제작 명세서

| 항목 | 내용 |
|---|---|
| 페이지 | 02_loss_and_gradient.html |
| 주 앵커 | D 생활: 연습장 벽의 표적지와 큰 조준 다이얼 (총 없음) |
| 분야 | 1 인공지능 (주) + 2 통계학 (보조) |
| 시즌 | 기본 |
| 대결 결과 | F, 차이 45.0%p → 결과 후 표정 doc_judge, asst_spark, fly_arms, robo_sigh |
| 받은 그림 (2026-11-07) | 표지·썸네일·공유 미리보기 반영 완료, `assets/img/` |
| 처음 계획한 그림 | P1 1장 (cover_02) · P2 1장 (thumb_02) · P3 1장 (og_02) |
| 추가 (2026-11-08) | P2 1장 (comic_02_mushroom, 4컷 만화) |
| 재사용 | 표정 15키, 모두 캐릭터 팩 1.3에 있음 |
| 그림이 없을 때 | 캐릭터 팩 그림 + CSS 대체 표지로 이미 완성 상태 |

## 1. 그림체와 고정 외형
캐릭터 팩 18-3·18-4 그대로. 이 페이지 장소: *a quiet practice room inside the same night lab world, one round paper target with concentric rings on the wall and a large brass dial knob with click marks mounted on a stand in front of it, purple lab light spilling in from the left*

## 2. 필요한 그림 전체
| # | 키 | 판 | 상태 | 우선 | 들어가는 곳 |
|---|---|---|---|---|---|
| 0 | cover_02 | L 1920×1080 | 새로 (COVER_02_loss_and_gradient.md) | P1 | 맨 위 글 표지 |
| 1 | thumb_02 | I 600×400 | cover_02 3:2 자르기 | P2 | 목차 카드 |
| 2 | og_02 | K 1200×630 | cover_02 자르기 | P3 | 공유 미리보기 |
| 3 | doc_think | A | 재사용 | — | 본문·대결 |
| 4 | doc_front | A | 재사용 | — | 본문·대결 |
| 5 | doc_board | A | 재사용 | — | 본문·대결 |
| 6 | doc_judge | A | 재사용 | — | 본문·대결 |
| 7 | asst_smile | B | 재사용 | — | 본문·대결 |
| 8 | asst_report | B | 재사용 | — | 본문·대결 |
| 9 | asst_spark | B | 재사용 | — | 본문·대결 |
| 10 | fly_point | C | 재사용 | — | 본문·대결 |
| 11 | fly_clip | C | 재사용 | — | 본문·대결 |
| 12 | fly_type | C | 재사용 | — | 본문·대결 |
| 13 | fly_arms | C | 재사용 | — | 본문·대결 |
| 14 | robo_coin | D | 재사용 | — | 본문·대결 |
| 15 | robo_smile | D | 재사용 | — | 본문·대결 |
| 16 | robo_calc | D | 재사용 | — | 본문·대결 |
| 17 | robo_sigh | D | 재사용 | — | 본문·대결 |
| 18 | comic_02_mushroom | 정사각 1600×1600 | 반영 완료 (2026-11-08, 4컷 칠판 곡선을 −log p 모양으로 고침) | P2 | ③칸 4컷 만화 「확신에 찬 오답」 (없으면 CSS 컷) |
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
 "page": "02_loss_and_gradient",
 "anchor": "D 생활: 연습장 벽의 표적지와 큰 조준 다이얼 (총 없음)",
 "domain": [
  "ai",
  "stats"
 ],
 "season": "default",
 "duel": {
  "result": "F",
  "gap": "45.0%p"
 },
 "images": [
  {
   "key": "cover_02",
   "plate": "L",
   "size": [
    1920,
    1080
   ],
   "status": "done",
   "priority": "P1",
   "slot": "cover",
   "fallback": "css-pixel-four",
   "alt": "밤의 연구실 연습장 벽의 표적지 앞에서 조수가 큰 조준 다이얼을 돌리고, 초파리 연구원은 탄착점 무리를 가리키며 주판봇은 빈 성적표를 든 표지"
  },
  {
   "key": "thumb_02",
   "plate": "I",
   "size": [
    600,
    400
   ],
   "status": "done",
   "priority": "P2",
   "slot": "index-card",
   "fallback": "color-card",
   "alt": "손실 함수와 경사하강법 — 상자를 열어 영점 잡기"
  },
  {
   "key": "og_02",
   "plate": "K",
   "size": [
    1200,
    630
   ],
   "status": "done",
   "priority": "P3",
   "slot": "og",
   "fallback": null,
   "alt": "손실 함수와 경사하강법 — 상자를 열어 영점 잡기"
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
   "key": "fly_type",
   "status": "reuse",
   "alt": ""
  },
  {
   "key": "fly_arms",
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
   "key": "robo_calc",
   "status": "reuse",
   "alt": ""
  },
  {
   "key": "robo_sigh",
   "status": "reuse",
   "alt": ""
  }
 ]
}
```
