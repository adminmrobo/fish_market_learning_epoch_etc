# 02번 4컷 만화 「확신에 찬 오답」 — Genspark 지시문

| 항목 | 내용 |
|---|---|
| 키 | `comic_02_mushroom` |
| 파일 | `assets/img/comic_02_mushroom.webp` (정사각 1600×1600, WebP) |
| 들어가는 곳 | 02_loss_and_gradient.html ③칸 「크로스 엔트로피」, 벌점표 위 |
| 그림이 없을 때 | 페이지 안 CSS·SVG 4컷(캐릭터 팩 표정 + NPC 봇 도형)으로 대신 보임 |
| 그림이 있을 때 | 파일을 넣기만 하면 자동으로 이 그림으로 바뀜 (코드 수정 불필요) |
| 우선 | P2 |

## 1. 등장인물
- **NPC 휴머노이드 봇** (이 만화에만 나오는 새 인물): 매끈한 흰색·연회색 휴머노이드, 얼굴은 어두운 바이저에 하늘색 둥근 눈 두 개, 머리 위 짧은 안테나, 가슴에 "NPC" 글자. 게임 속 안내원처럼 늘 지나치게 밝게 웃는 표정. 실존 제품·캐릭터를 닮지 않게.
- 주판봇·박사·조수 하루·초파리 연구원: 캐릭터 팩 18-3·18-4 고정 외형 그대로.

## 2. 컷 구성 (2×2, 왼쪽 위 → 오른쪽 위 → 왼쪽 아래 → 오른쪽 아래)
| 컷 | 장면 | 말풍선 (한국어 그대로) | 작은 자막 |
|---|---|---|---|
| 1 | 맑은 낮 초원. 화면 왼쪽에서 손(얼굴 없음)이 갈색 버섯을 내밀고, NPC 봇이 엄지를 들고 활짝 웃는다 | 손: "이 버섯 먹어도 돼?" / 봇: "네! 먹어도 안전해요!" | 봇이 독버섯에 준 확률 0.01 |
| 2 | 같은 초원, 보랏빛·주황 노을. 금 간 작은 비석(R.I.P) 옆에 NPC 봇이 여전히 웃으며 비석에 손을 얹는다. 사람은 나오지 않는다 | 봇: "맞아요, 그건 독버섯이에요. 잘못 알려 드려 죄송합니다!" | 정답: 독버섯 |
| 3 | 밤의 연구실. 모니터에 2컷 장면이 떠 있고, 주판봇이 주판을 높이 들고 화난 얼굴(이마에 김)로 화면 속 봇을 가리킨다 | 주판봇: "너는 용서가 안 돼! 이렇게 확신을 가지고 틀리면 더 혼나야 돼!" | 손실 −log 0.01 = 4.61 |
| 4 | 같은 연구실. 박사·조수 하루·초파리 연구원이 나란히 서서 한목소리로 외친다. 뒤 화이트보드에 −log p 곡선이 0 쪽에서 위로 치솟는 그림 | 셋이 함께: "저렇게 틀리면 바로 폐기 처분 해야지!" | 확률 → 0이면 손실 → ∞ |

## 3. Genspark에 붙여 넣을 프롬프트
```
A 4-panel square comic (2x2 grid, 1600x1600), clean Korean webtoon style, bold outlines, flat colors, white speech bubbles with Korean text exactly as given.
Panel 1: sunny green meadow, blue sky. A hand from the left edge holds out a brown mushroom. A cheerful white-and-light-gray humanoid robot NPC (smooth helmet head, dark visor with two round sky-blue eyes, short antenna, "NPC" printed on chest) gives a thumbs-up with an over-bright smile. Bubble from hand: "이 버섯 먹어도 돼?" Bubble from robot: "네! 먹어도 안전해요!" Small caption box: "봇이 독버섯에 준 확률 0.01".
Panel 2: same meadow at purple-orange sunset. A small cracked gravestone engraved "R.I.P". The same NPC robot still smiling, one hand resting on the gravestone. No person visible. Bubble: "맞아요, 그건 독버섯이에요. 잘못 알려 드려 죄송합니다!" Caption: "정답: 독버섯".
Panel 3: purple-lit night laboratory. A monitor shows the sunset scene. [ABACUS ROBOT fixed look from character pack] holds an abacus high, angry face with steam puffs, pointing at the monitor. Bubble: "너는 용서가 안 돼! 이렇게 확신을 가지고 틀리면 더 혼나야 돼!" Caption: "손실 −log 0.01 = 4.61".
Panel 4: same lab. [DOCTOR], [ASSISTANT HARU], [FRUIT FLY RESEARCHER] fixed looks from character pack stand side by side shouting together, arms pointing forward. Whiteboard behind shows a curve shooting upward as x approaches 0. Bubble: "저렇게 틀리면 바로 폐기 처분 해야지!" Caption: "확률 → 0이면 손실 → ∞".
No weapons, no blood, no real brand logos, no letters "AI" on clothing, no resemblance to existing characters.
```

## 4. 체크리스트
- [ ] 말풍선 한국어가 위 표와 글자 하나까지 같음 (틀리면 페이지 자막과 어긋남)
- [ ] 2컷에 사람(시신) 없음, 비석만
- [ ] NPC 봇이 연구실 네 캐릭터와 헷갈리지 않음
- [ ] 무기·피 없음
- [ ] 받은 PNG → `assets/img/src/comic_02_mushroom.png`, WebP 1600px → `assets/img/comic_02_mushroom.webp`
