# Fish Market 연구실 — 머신러닝 핵심 개념 2

> 모델은 이미 최적화하는데, 왜 또 최적화할까?

생선 가게 물고기 158마리(7어종)로 머신러닝 최적화의 네 층위를 따라가는 해설 시리즈입니다. 박사·조수 하루·초파리 연구원·주판봇이 진행하고, 모든 그래프와 표는 실제 데이터로 페이지 안에서 직접 계산합니다.

글 · 안상선 ((주)M-Robo 대표)

## 목차

| 장 | 파일 | 주제 | 층위 | 대결 |
|---|---|---|---|---|
| 목차 | [index.html](index.html) | 시리즈 지도 | — | — |
| 1 | [01_setting_the_board.html](01_setting_the_board.html) | 판 짜기 — 무엇으로 배우고, 무엇으로 판정할까 | 0층위 | X · 주판봇 실격 (데이터 누수) |
| 2 | [02_loss_and_gradient.html](02_loss_and_gradient.html) | 손실 함수와 경사하강법 — 상자를 열어 영점 잡기 | 0층위 + ① | F · 초파리 승 |
| 3 | [03_rate_batch_epoch.html](03_rate_batch_epoch.html) | 학습률·배치·에포크 — 몇 클릭, 몇 발, 몇 바퀴 | ② | F · 초파리 승 |
| 4 | [04_turning_the_knobs.html](04_turning_the_knobs.html) | 손잡이 다시 돌리기 — Phase #2·#3와 신뢰도 | ② + 0층위 + 신뢰도 | R · 주판봇 승 |
| 5 | [05_many_shooters.html](05_many_shooters.html) | 사수 여러 명 — 앙상블은 튜닝을 넘을까 | ③ | R · 주판봇 승 |

## 최적화의 네 층위

| 층위 | 무엇을 정하나 | 무엇으로 판정하나 |
|---|---|---|
| 0층위 · 판 짜기 | 문제 정의, 입력 변수, 손실 함수, 데이터 분할 | 최적화 대상이 아님 |
| ① 파라미터 | 가중치(계수) | 훈련 손실 최소화 |
| ② 하이퍼파라미터 | 학습률·배치·에포크, k·C·kernel | 검증(교차검증) 성적 |
| ③ 모형 구조·결합 | 어떤 모델(들)을 쓸지 | 검증 성적, 오차의 성격 |
| 별도 축 | random_state, 교차검증 | 재현성, 성적의 신뢰도 |

## 폴더

| 경로 | 내용 |
|---|---|
| `*.html` | 해설 페이지 6개 (각각 파일 하나로 열림, 외부 요청은 글꼴뿐) |
| `experiments/` | 데이터 `fish.csv`, 실험 스크립트(scikit-learn) 2개, Genspark용 슬라이드 원고 |
| `images_spec/` | 표지 지시문 `COVER_*.md`(Genspark에 붙여 넣기)와 이미지 제작 명세서 `IMG_*.md` |
| `data/` | 시리즈 개념·문헌 등록부 추가분 (`KG_00_registry.json`에 합칠 것) |

## 숫자의 출처

- 페이지 안 계산: KNN, 선형·로지스틱 회귀(scikit-learn과 같은 목적식), 소프트맥스 SGD(실험 스크립트와 같은 섞기 순서), 결정나무·배깅·AdaBoost, 분할 20번(scikit-learn `random_state` 0~19와 같은 분할).
- 실험 스크립트 값으로 옮긴 것: SVC, 스태킹, Gradient Boosting, 2,000에포크 결과. 페이지에 `scikit-learn 값`으로 표시했습니다.
- 결정나무 계열은 같은 성적의 분할 후보 중 무엇을 고르는지가 scikit-learn과 달라 슬라이드 원고와 값이 조금 다릅니다. 학습률 50은 혼돈 구간이라 계산 환경에 따라 끝값이 달라집니다.

## 데이터와 참고문헌

- Aung Pyae, Kaggle "Fish market" (CC BY 4.0). 정리본 fish.csv: 박해선(2020), 『혼자 공부하는 머신러닝+딥러닝』, 한빛미디어.
- Pedregosa 외 (2011), Scikit-learn: Machine Learning in Python, JMLR 12.
- Kohavi (1995), A Study of Cross-Validation and Bootstrap for Accuracy Estimation and Model Selection, IJCAI, 1137–1144.
- Robbins & Monro (1951), Breiman (1996), Freund & Schapire (1997), Zhu 외 (2009), Wolpert (1992).

## 라이선스

캐릭터(박사·조수 하루·초파리 연구원·주판봇)의 이름·설정·그림은 저작권자 안상선에게 있으며 허락 없이 쓸 수 없습니다. 페이지 본문과 코드의 라이선스는 저자가 정합니다.

이 페이지들은 교육용이며 투자 자문이 아닙니다.
