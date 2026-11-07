import numpy as np, pandas as pd, json, warnings
warnings.filterwarnings("ignore")
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier
from sklearn.metrics import mean_squared_error, accuracy_score, confusion_matrix

R = {}
df = pd.read_csv("fish.csv"); df = df[df.Weight > 0].reset_index(drop=True)
FEAT = ["Length", "Diagonal", "Height", "Width"]
tr, te = train_test_split(df, test_size=0.25, stratify=df.Species, random_state=42)
sc = StandardScaler().fit(tr[FEAT]); A, B = sc.transform(tr[FEAT]), sc.transform(te[FEAT])
ya, yb = tr.Species.values, te.Species.values
cv = StratifiedKFold(5, shuffle=True, random_state=42)

# 회귀 Phase#3: 무게는 길이의 세제곱에 비례
for name, p in [("선형 (원래 4변수)", make_pipeline(StandardScaler(), LinearRegression())),
                ("선형 + 2차항", make_pipeline(PolynomialFeatures(2), StandardScaler(), LinearRegression())),
                ("선형, log(무게)~log(변수)", "log")]:
    if p == "log":
        m = LinearRegression().fit(np.log(tr[FEAT]), np.log(tr.Weight))
        pr = np.exp(m.predict(np.log(te[FEAT])))
    else:
        pr = p.fit(tr[FEAT], tr.Weight).predict(te[FEAT])
    mse = mean_squared_error(te.Weight, pr)
    R.setdefault("reg_phase3", {})[name] = dict(mse=round(mse, 1), rmse=round(mse ** .5, 1))

# 혼동: 로지스틱이 틀린 물고기
lr = LogisticRegression(max_iter=5000).fit(A, ya); pr = lr.predict(B)
R["lr_wrong"] = [f"{t}→{p}" for t, p in zip(yb, pr) if t != p]
knn = KNeighborsClassifier(5).fit(A, ya); pk = knn.predict(B)
R["knn_wrong"] = [f"{t}→{p}" for t, p in zip(yb, pk) if t != p]
svl = SVC(kernel="linear", C=100).fit(A, ya)
R["svc_lin_wrong"] = [f"{t}→{p}" for t, p in zip(yb, svl.predict(B)) if t != p]

# 하드보팅 의견 갈린 물고기: 세 모델 예측이 다른 경우
svc = SVC(probability=True, random_state=42).fit(A, ya)
ps = svc.predict(B)
dis = []
for i in range(len(yb)):
    votes = [pr[i], pk[i], ps[i]]
    if len(set(votes)) > 1:
        dis.append(dict(true=yb[i], lr=pr[i], knn=pk[i], svc=ps[i],
                        feat={f: float(te[FEAT].iloc[i][f]) for f in FEAT},
                        lr_p={c: round(float(x), 2) for c, x in zip(lr.classes_, lr.predict_proba(B[i:i+1])[0]) if x > .05},
                        knn_p={c: round(float(x), 2) for c, x in zip(knn.classes_, knn.predict_proba(B[i:i+1])[0]) if x > .05},
                        svc_p={c: round(float(x), 2) for c, x in zip(svc.classes_, svc.predict_proba(B[i:i+1])[0]) if x > .05}))
R["disagree"] = dis

# 부스팅: 나무 깊이
bo = {}
for d in [1, 2, 3]:
    for n in [1, 30, 100]:
        m = AdaBoostClassifier(DecisionTreeClassifier(max_depth=d, random_state=42), n_estimators=n, random_state=42).fit(A, ya)
        bo[f"depth{d}_n{n}"] = round(accuracy_score(yb, m.predict(B)) * 100, 1)
for d in [1, 3]:
    t = DecisionTreeClassifier(max_depth=d, random_state=42).fit(A, ya)
    bo[f"single_depth{d}"] = round(accuracy_score(yb, t.predict(B)) * 100, 1)
    bo[f"single_depth{d}_leaves"] = int(t.get_n_leaves())
gb = GradientBoostingClassifier(random_state=42).fit(A, ya)
bo["gradient_boosting"] = round(accuracy_score(yb, gb.predict(B)) * 100, 1)
R["boost"] = bo

# 에포크: 훈련 손실 vs 시험 손실 (과적합 관찰) — 큰 학습률로 오래
classes = sorted(df.Species.unique()); ci = {c: i for i, c in enumerate(classes)}
Ya = np.eye(7)[[ci[c] for c in ya]]; Yb = np.eye(7)[[ci[c] for c in yb]]
def sm(z): z = z - z.max(1, keepdims=True); e = np.exp(z); return e / e.sum(1, keepdims=True)
def run(lrate, bs, ep, Xa=A, Xb=B):
    rng = np.random.default_rng(42); W = np.zeros((Xa.shape[1], 7)); b = np.zeros(7); tl, vl, acc = [], [], []
    for e in range(ep):
        perm = rng.permutation(len(Xa))
        for s in range(0, len(Xa), bs):
            j = perm[s:s+bs]; g = (sm(Xa[j] @ W + b) - Ya[j]) / len(j)
            W -= lrate * Xa[j].T @ g; b -= lrate * g.sum(0)
        tl.append(-np.mean(np.log(np.clip((sm(Xa @ W + b) * Ya).sum(1), 1e-12, 1))))
        Pb = sm(Xb @ W + b)
        vl.append(-np.mean(np.log(np.clip((Pb * Yb).sum(1), 1e-12, 1))))
        acc.append((Pb.argmax(1) == Yb.argmax(1)).mean() * 100)
    return tl, vl, acc
tl, vl, acc = run(0.1, 16, 2000)
pts = [1, 10, 100, 300, 500, 1000, 1500, 2000]
R["epoch_long"] = {e: dict(train=round(tl[e-1], 3), test=round(vl[e-1], 3), acc=round(acc[e-1], 1)) for e in pts}
R["epoch_long_min_test"] = dict(epoch=int(np.argmin(vl)) + 1, loss=round(min(vl), 3))

# 다항 특성(과적합 잘 나는 조건)에서 에포크
pf = make_pipeline(PolynomialFeatures(3, include_bias=False), StandardScaler()).fit(tr[FEAT])
A3, B3 = pf.transform(tr[FEAT]), pf.transform(te[FEAT])
tl3, vl3, acc3 = run(0.5, 16, 3000, A3, B3)
R["epoch_poly3"] = {e: dict(train=round(tl3[e-1], 3), test=round(vl3[e-1], 3), acc=round(acc3[e-1], 1)) for e in [1, 10, 100, 300, 1000, 2000, 3000]}
R["epoch_poly3_min_test"] = dict(epoch=int(np.argmin(vl3)) + 1, loss=round(min(vl3), 3), acc=round(acc3[int(np.argmin(vl3))], 1))
R["n_poly_feat"] = A3.shape[1]

# seed 반복: 튜닝한 모델 포함
rep = {k: [] for k in ["SVC linear C=100", "로지스틱 C=100", "KNN + 비율변수 (k=5)", "AdaBoost 깊이3 x30"]}
for s in range(20):
    a, b = train_test_split(df, test_size=0.25, stratify=df.Species, random_state=s)
    ss = StandardScaler().fit(a[FEAT]); X1, X2 = ss.transform(a[FEAT]), ss.transform(b[FEAT])
    rep["SVC linear C=100"].append(accuracy_score(b.Species, SVC(kernel="linear", C=100).fit(X1, a.Species).predict(X2)) * 100)
    rep["로지스틱 C=100"].append(accuracy_score(b.Species, LogisticRegression(C=100, max_iter=20000).fit(X1, a.Species).predict(X2)) * 100)
    rep["AdaBoost 깊이3 x30"].append(accuracy_score(b.Species, AdaBoostClassifier(DecisionTreeClassifier(max_depth=3), n_estimators=30, random_state=s).fit(X1, a.Species).predict(X2)) * 100)
    c = FEAT + ["HL"]; a2 = a.assign(HL=a.Height / a.Length); b2 = b.assign(HL=b.Height / b.Length)
    s2 = StandardScaler().fit(a2[c])
    rep["KNN + 비율변수 (k=5)"].append(accuracy_score(b.Species, KNeighborsClassifier(5).fit(s2.transform(a2[c]), a.Species).predict(s2.transform(b2[c]))) * 100)
R["seeds2"] = {k: dict(mean=round(np.mean(v), 1), std=round(np.std(v), 1), min=round(min(v), 1), max=round(max(v), 1)) for k, v in rep.items()}
# 로지스틱 C=100 고정 시드42
R["lr_C100_seed42"] = round(accuracy_score(yb, LogisticRegression(C=100, max_iter=20000).fit(A, ya).predict(B)) * 100, 1)
R["lr_C100_cv"] = round(cross_val_score(LogisticRegression(C=100, max_iter=20000), A, ya, cv=cv).mean() * 100, 1)
json.dump(R, open("results2.json", "w"), ensure_ascii=False, indent=1, default=str)
print(json.dumps(R, ensure_ascii=False, indent=1, default=str))
