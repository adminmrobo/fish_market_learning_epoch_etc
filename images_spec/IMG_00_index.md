# 시리즈 공용 이미지 명세서 — Fish Market 연구실 (머신러닝 핵심 개념 2)

| 항목 | 내용 |
|---|---|
| 시리즈 | Fish Market 연구실, 5장 (1 판 짜기 · 2 손실 함수와 경사하강법 · 3 학습률·배치·에포크 · 4 손잡이 다시 돌리기 · 5 사수 여러 명) |
| 분야 | 인공지능(주) + 통계학(보조) |
| 시즌 | 기본 |
| 시리즈 비유 | 영점 잡기. **그림에는 총을 넣지 않는다** — 표적지, 조준 다이얼, 공 던지기 과녁으로만 |
| 공용 표정 | 1장에서 쓴 15키 모두 캐릭터 팩 1.3에 있음 (새로 그릴 것 없음) |

## 1. 공용 표정 현황
| 키 | 판 | 상태 | 쓰는 페이지 |
|---|---|---|---|
| doc_front, doc_think, doc_magic, doc_judge | A | 있음 | 01 |
| asst_smile, asst_report, asst_shock, asst_spark | B | 있음 | 01 |
| fly_point, fly_clip, fly_magnify, fly_arms | C | 있음 (fly는 왼쪽을 보는 그림 → 대결에서 뒤집어 씀) | 01 |
| robo_coin, robo_smile, robo_calc, robo_blush | D | 있음 | 01 |

## 2. 목차·표지 그림
| 키 | 판 | 내용 | 우선 |
|---|---|---|---|
| cover_index | L | 밤의 연구실 전경. 긴 측정대 위에 일곱 색 물고기 카드 무더기, 벽에 표적지 다섯 장이 한 줄로(각 장의 상징 소품이 작게 아래에: 봉인 봉투 · 조준 다이얼 · 공 바구니 · 다이얼 여러 개 · 과녁 여러 개). 박사가 가운데에서 표적지 줄을 가리키고, 초파리와 주판봇이 양쪽에서 올려다보고, 조수가 빈 점수판을 든다 | P1 (목차 페이지를 만들 때) |
| bg_index | F | 연구실 복도에 문이 다섯 개, 문마다 다른 색 빛이 샌다 | P2 |
| thumb_01 ~ thumb_05 | I | 각 장 표지를 3:2로 자르기 | P2 |
| og_index | K | cover_index 축소 | P3 |

**cover_index 프롬프트 (목차를 만들 때 COVER_00_index.md로 따로 낸다)**
```
Website top cover illustration, wide 16:9. Match the art style, proportions and colors of the attached reference images exactly. Cozy night laboratory mood, purple light, soft magenta and green fluorescent accents. Scene: a wide night laboratory with a long measuring bench holding seven neat piles of blank cards in seven soft colors; on the back wall a row of five round paper targets with concentric rings, under each a small prop: a sealed envelope, a dial knob, a basket of soft balls, several dial knobs, several small targets. All four characters together (height order doctor ≥ girl researcher > robot > fruit fly): chibi scientist with thin teal rectangular glasses, spiky black hair with one white streak and a small ponytail, white lab coat over black vest and tie, center back pointing at the row of targets; girl researcher with long pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, at the side holding a blank scoreboard; anthropomorphic fruit fly researcher with black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right looking up; boxy beige retro CRT-monitor robot with dark green screen face, mint pixel eyes, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left looking up. Keep faces and hands in the central safe area, bottom-left corner dark and simple. Mood: curious, friendly rivalry. No text, no letters, no numbers, no logos, no weapons, no guns, no cigarettes, no alcohol, no blood, no real brands.
```

## 3. 페이지별 대표 그림
| 페이지 | 앵커 | 상징 소품 | cover | thumb | 상태 |
|---|---|---|---|---|---|
| 01 판 짜기 | B 측정실 | 봉인 봉투 | cover_01 | thumb_01 | 지시문 완료 |
| 02 손실 함수와 경사하강법 | D 사격장 대신 '조준 다이얼과 표적지' | 다이얼 | cover_02 | thumb_02 | 예정 |
| 03 학습률·배치·에포크 | D 공 던지기 과녁 | 공 바구니 | cover_03 | thumb_03 | 예정 |
| 04 손잡이 다시 돌리기 | B 연구실 | 다이얼 여러 개 | cover_04 | thumb_04 | 예정 |
| 05 사수 여러 명 | C 장부 / D | 과녁 여러 개 | cover_05 | thumb_05 | 예정 |

## 4. 매니페스트
```json
{"series":"fishmarket-ml-core2","shared":["doc_front","doc_think","doc_magic","doc_judge","asst_smile","asst_report","asst_shock","asst_spark","fly_point","fly_clip","fly_magnify","fly_arms","robo_coin","robo_smile","robo_calc","robo_blush"],
 "pages":[{"page":"01_setting_the_board","cover":"cover_01","status":"spec"},{"page":"02","cover":"cover_02","status":"planned"},{"page":"03","cover":"cover_03","status":"planned"},{"page":"04","cover":"cover_04","status":"planned"},{"page":"05","cover":"cover_05","status":"planned"}],
 "index":{"cover":"cover_index","status":"planned"}}
```
