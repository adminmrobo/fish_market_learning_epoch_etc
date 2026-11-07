# 표지 지시문 — 02 손실 함수와 경사하강법 — 상자를 열어 영점 잡기

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_02 · L (16:9, 가로 1920 이상) |
| 장소 (앵커) | D 생활: 연습장 벽의 표적지와 큰 조준 다이얼 (총 없음) |
| 네 캐릭터 포즈 | 박사 at the back center, one finger raised as if explaining a rule / 조수 at the right side, turning the large dial knob with both hands / 초파리 on the left facing right, pointing at the dot cluster on the target / 주판봇 on the right facing left, holding up the abacus and a blank report card with only striped lines |
| 대체 글 (alt) | 밤의 연구실 연습장 벽의 표적지 앞에서 조수가 큰 조준 다이얼을 돌리고, 초파리 연구원은 탄착점 무리를 가리키며 주판봇은 빈 성적표를 든 표지 |
| 앞 표지와 다른 점 | 1장의 봉인 봉투 대신 조준 다이얼과 표적지 하나 |
| 주의 | 총·무기 금지(영점 사격 비유는 표적지·다이얼·공으로만). 결과 암시 금지 |

**참고 이미지 (함께 올리기):** 네 캐릭터 기본 그림 4장 (GitHub `adminmrobo/fruitfly-lab-expressions`, 설정샷 k01·k12). 1장 표지(cover_01)를 받았으면 그것도 함께 올려 화풍을 맞춘다.

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 그림 안에 글자·숫자·로고를 넣지 말 것, 총이나 무기를 그리지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 어둡고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
(if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
Cozy night laboratory mood, purple light, soft magenta and green fluorescent accents.
Scene: a quiet practice room inside the same night lab world, one round paper target with concentric rings on the wall and a large brass dial knob with click marks mounted on a stand in front of it, purple lab light spilling in from the left.
All four characters together, height order doctor ≥ girl researcher > robot > fruit fly:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center, one finger raised as if explaining a rule;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, at the right side, turning the large dial knob with both hands;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, pointing at the dot cluster on the target;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, holding up the abacus and a blank report card with only striped lines.
Visual metaphor of the topic: a cluster of small green dots on the target shifting toward the center along a faint dotted arrow, as the dial is turned a few clicks.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner dark and simple; the light falls on the target and the dial.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no guns, no cigarettes, no alcohol, no blood, no real brands.
```

**고칠 때 (같은 대화에서):** `Same four characters, same art style and composition. Change only: {고칠 점}. Still no text, no weapons.`

## 받은 뒤 처리 (SKILL 18-15)
1. 16:9·가로 1600 이상·글자 없음·네 캐릭터 외형 확인
2. WebP 1600×900(220 KB 이하)을 `<header class="cover" data-img="cover_02">`에 넣고 대체 표지를 지움 — `<!-- lab-cover -->` 표시 사이만 바꾼다
3. 390·768·1280 폭에서 얼굴 잘림 확인, `thumb_02`·`og_02` 자르기
