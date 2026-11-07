import numpy as np, pandas as pd, json, warnings
warnings.filterwarnings("ignore")
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression, LogisticRegression, SGDClassifier
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (VotingClassifier, BaggingClassifier, AdaBoostClassifier,
                              StackingClassifier)
from sklearn.metrics import mean_squared_error, accuracy_score, log_loss

R = {}
df = pd.read_csv("fish.csv")
R["raw_n"] = len(df)
df = df[df.Weight > 0].reset_index(drop=True)
R["n"] = len(df)
R["counts"] = df.Species.value_counts().to_dict()
FEAT = ["Length", "Diagonal", "Height", "Width"]
classes = sorted(df.Species.unique())

tr, te = train_test_split(df, test_size=0.25, stratify=df.Species, random_state=42)
R["n_train"], R["n_test"] = len(tr), len(te)
cv = StratifiedKFold(5, shuffle=True, random_state=42)

# ---------- 회귀: 무게 ----------
Xr_tr, Xr_te = tr[FEAT], te[FEAT]
yr_tr, yr_te = tr.Weight, te.Weight
reg = {}
for name, m in [("선형 회귀", LinearRegression()),
                ("KNN 회귀 (k=5)", KNeighborsRegressor(5))]:
    p = make_pipeline(StandardScaler(), m).fit(Xr_tr, yr_tr)
    mse = mean_squared_error(yr_te, p.predict(Xr_te))
    reg[name] = dict(mse=round(mse, 1), rmse=round(mse ** .5, 1))
R["regression"] = reg
# 예시 한 마리 (시험셋 농어 하나)
ex = te[te.Species == "Perch"].iloc[0]
lin = make_pipeline(StandardScaler(), LinearRegression()).fit(Xr_tr, yr_tr)
knr = make_pipeline(StandardScaler(), KNeighborsRegressor(5)).fit(Xr_tr, yr_tr)
R["reg_example"] = dict(feat={f: float(ex[f]) for f in FEAT}, weight=float(ex.Weight),
                        lin=round(float(lin.predict(ex[FEAT].to_frame().T)[0]), 1),
                        knn=round(float(knr.predict(ex[FEAT].to_frame().T)[0]), 1))

# ---------- 분류: 7개 어종 ----------
X_tr, X_te = tr[FEAT].values, te[FEAT].values
y_tr, y_te = tr.Species.values, te.Species.values
sc = StandardScaler().fit(X_tr)
Xs_tr, Xs_te = sc.transform(X_tr), sc.transform(X_te)

def ev(m):
    m.fit(Xs_tr, y_tr)
    pr = m.predict(Xs_te)
    out = dict(acc=round(accuracy_score(y_te, pr) * 100, 1), wrong=int((pr != y_te).sum()))
    if hasattr(m, "predict_proba"):
        try:
            out["loss"] = round(log_loss(y_te, m.predict_proba(Xs_te), labels=m.classes_), 3)
        except Exception:
            pass
    return out

base = {"로지스틱 회귀": LogisticRegression(max_iter=5000),
        "KNN (k=5)": KNeighborsClassifier(5),
        "SVC (rbf, 기본)": SVC(probability=True, random_state=42)}
R["clf"] = {k: ev(v) for k, v in base.items()}

# ---------- Phase #2: 하이퍼파라미터 (교차검증) ----------
kgrid = {}
for k in [1, 3, 5, 7, 9, 15]:
    s = cross_val_score(KNeighborsClassifier(k), Xs_tr, y_tr, cv=cv)
    kgrid[k] = dict(cv=round(s.mean() * 100, 1), test=ev(KNeighborsClassifier(k))["acc"],
                    train=round(accuracy_score(y_tr, KNeighborsClassifier(k).fit(Xs_tr, y_tr).predict(Xs_tr)) * 100, 1))
R["k_grid"] = kgrid
svgrid = {}
for ker in ["linear", "rbf", "poly"]:
    for C in [0.1, 1, 10, 100]:
        s = cross_val_score(SVC(kernel=ker, C=C), Xs_tr, y_tr, cv=cv)
        svgrid[f"{ker}, C={C}"] = round(s.mean() * 100, 1)
R["svc_grid"] = svgrid
best_sv = max(svgrid, key=svgrid.get)
ker, C = best_sv.split(", C=")
R["svc_best"] = dict(setting=best_sv, cv=svgrid[best_sv],
                     test=ev(SVC(kernel=ker, C=float(C)))["acc"])

# ---------- Phase #3: 변수 바꾸기 ----------
fs = {"Length + Weight (2개)": ["Length", "Weight"],
      "Length·Diagonal·Height·Width (4개)": FEAT,
      "4개 + Weight (5개)": FEAT + ["Weight"],
      "4개 + Height/Length 비율 (5개)": FEAT + ["HL"]}
d2 = df.copy(); d2["HL"] = d2.Height / d2.Length
tr2, te2 = d2.loc[tr.index], d2.loc[te.index]
ph3 = {}
for name, cols in fs.items():
    s = StandardScaler().fit(tr2[cols])
    a, b = s.transform(tr2[cols]), s.transform(te2[cols])
    best_k, best_cv = None, -1
    for k in [1, 3, 5, 7, 9, 15]:
        c = cross_val_score(KNeighborsClassifier(k), a, y_tr, cv=cv).mean()
        if c > best_cv + 1e-9: best_k, best_cv = k, c
    t = accuracy_score(y_te, KNeighborsClassifier(best_k).fit(a, y_tr).predict(b))
    lr_cv = cross_val_score(LogisticRegression(max_iter=5000), a, y_tr, cv=cv).mean()
    ph3[name] = dict(best_k=best_k, knn_cv=round(best_cv * 100, 1), knn_test=round(t * 100, 1),
                     lr_cv=round(lr_cv * 100, 1))
R["phase3"] = ph3

# ---------- 손실: 크로스 엔트로피 실제 예시 ----------
lr = LogisticRegression(max_iter=5000).fit(Xs_tr, y_tr)
P = lr.predict_proba(Xs_te)
idx_true = np.array([list(lr.classes_).index(c) for c in y_te])
pt = P[np.arange(len(y_te)), idx_true]
order = np.argsort(pt)
picks = {"가장 자신 있게 맞힘": order[-1], "가장 애매함(중간)": order[len(order) // 2], "가장 낮은 정답확률": order[0]}
ce = {}
for lab, i in picks.items():
    top = np.argsort(P[i])[::-1][:3]
    ce[lab] = dict(true=y_te[i], pred=lr.classes_[P[i].argmax()],
                   top3={lr.classes_[j]: round(float(P[i, j]), 3) for j in top},
                   p_true=round(float(pt[i]), 3), loss=round(float(-np.log(pt[i])), 3))
R["ce_examples"] = ce

# ---------- SGD 직접 구현 (소프트맥스) ----------
cls_idx = {c: i for i, c in enumerate(classes)}
Ytr = np.eye(7)[[cls_idx[c] for c in y_tr]]
yte_i = np.array([cls_idx[c] for c in y_te])

def softmax(z):
    z = z - z.max(1, keepdims=True); e = np.exp(z); return e / e.sum(1, keepdims=True)

def train_sgd(lr_, bs, epochs, seed=42):
    rng = np.random.default_rng(seed)
    W = np.zeros((4, 7)); b = np.zeros(7); n = len(Xs_tr); hist = []; ups = 0
    for ep in range(epochs):
        perm = rng.permutation(n)
        for s in range(0, n, bs):
            j = perm[s:s + bs]
            Pp = softmax(Xs_tr[j] @ W + b)
            g = (Pp - Ytr[j]) / len(j)
            W -= lr_ * Xs_tr[j].T @ g; b -= lr_ * g.sum(0); ups += 1
        Pa = softmax(Xs_tr @ W + b)
        hist.append(float(-np.mean(np.log(np.clip((Pa * Ytr).sum(1), 1e-12, 1)))))
    acc = float((softmax(Xs_te @ W + b).argmax(1) == yte_i).mean())
    return hist, round(acc * 100, 1), ups

EP = 100
lrs = {}
for l in [0.001, 0.01, 0.1, 1, 10, 50]:
    h, a, u = train_sgd(l, 16, EP)
    lrs[l] = dict(ep1=round(h[0], 3), ep10=round(h[9], 3), ep100=round(h[-1], 3),
                  maxloss=round(max(h), 2), acc=a, curve=[round(x, 3) for x in h])
R["lr"] = lrs
bsr = {}
for bs in [1, 16, len(Xs_tr)]:
    h, a, u = train_sgd(0.1, bs, EP)
    bsr[bs] = dict(ups=u, ups_ep=u // EP, ep1=round(h[0], 3), ep100=round(h[-1], 3), acc=a,
                   curve=[round(x, 3) for x in h])
R["batch"] = bsr
h, a, u = train_sgd(0.1, 16, 300)
R["epoch"] = dict(points={e: round(h[e - 1], 3) for e in [1, 2, 5, 10, 30, 100, 200, 300]},
                  acc_at={e: train_sgd(0.1, 16, e)[1] for e in [1, 5, 10, 30, 100, 300]})
R["sgd_sklearn"] = ev(SGDClassifier(loss="log_loss", random_state=42))

# ---------- 앙상블 ----------
voters = [("lr", LogisticRegression(max_iter=5000)), ("knn", KNeighborsClassifier(5)),
          ("svc", SVC(probability=True, random_state=42))]
ens = {}
ens["하드 보팅"] = ev(VotingClassifier(voters, voting="hard"))
ens["소프트 보팅"] = ev(VotingClassifier(voters, voting="soft"))
ens["배깅 (KNN 30개)"] = ev(BaggingClassifier(KNeighborsClassifier(5), n_estimators=30, max_samples=0.5, bootstrap=True, random_state=42))
ens["페이스팅 (KNN 30개)"] = ev(BaggingClassifier(KNeighborsClassifier(5), n_estimators=30, max_samples=0.5, bootstrap=False, random_state=42))
ens["결정나무 1개"] = ev(DecisionTreeClassifier(random_state=42))
ens["배깅 (결정나무 100개)"] = ev(BaggingClassifier(DecisionTreeClassifier(), n_estimators=100, random_state=42))
for n in [1, 5, 30, 100]:
    ens[f"부스팅 (그루터기 {n}개)"] = ev(AdaBoostClassifier(DecisionTreeClassifier(max_depth=1), n_estimators=n, random_state=42))
ens["스태킹 (LR+KNN+SVC → LR)"] = ev(StackingClassifier(voters, final_estimator=LogisticRegression(max_iter=5000), cv=5))
R["ensemble"] = ens
# 하드 vs 소프트 갈린 물고기
hv = VotingClassifier(voters, voting="hard").fit(Xs_tr, y_tr)
sv = VotingClassifier(voters, voting="soft").fit(Xs_tr, y_tr)
ph, ps = hv.predict(Xs_te), sv.predict(Xs_te)
diff = []
for i in np.where(ph != ps)[0]:
    row = dict(true=y_te[i], hard=ph[i], soft=ps[i], feat=dict(zip(FEAT, map(float, X_te[i]))), models={})
    for nm, m in sv.named_estimators_.items():
        pr = m.predict_proba(Xs_te[i:i + 1])[0]
        top = np.argsort(pr)[::-1][:2]
        row["models"][nm] = {m.classes_[j]: round(float(pr[j]), 2) for j in top}
    diff.append(row)
R["hard_soft_diff"] = diff

# ---------- seed 반복: 신뢰도 ----------
rep = {k: [] for k in ["로지스틱 회귀", "KNN (k=5)", "SVC", "하드 보팅", "부스팅 (그루터기 30개)"]}
for s in range(20):
    a, b = train_test_split(df, test_size=0.25, stratify=df.Species, random_state=s)
    ss = StandardScaler().fit(a[FEAT]); A, B = ss.transform(a[FEAT]), ss.transform(b[FEAT])
    ms = {"로지스틱 회귀": LogisticRegression(max_iter=5000), "KNN (k=5)": KNeighborsClassifier(5),
          "SVC": SVC(), "하드 보팅": VotingClassifier([("lr", LogisticRegression(max_iter=5000)), ("knn", KNeighborsClassifier(5)), ("svc", SVC())], voting="hard"),
          "부스팅 (그루터기 30개)": AdaBoostClassifier(DecisionTreeClassifier(max_depth=1), n_estimators=30, random_state=s)}
    for k, m in ms.items():
        rep[k].append(accuracy_score(b.Species, m.fit(A, a.Species).predict(B)) * 100)
R["seeds"] = {k: dict(mean=round(np.mean(v), 1), std=round(np.std(v), 1), min=round(min(v), 1), max=round(max(v), 1)) for k, v in rep.items()}

json.dump(R, open("results.json", "w"), ensure_ascii=False, indent=1, default=str)
light = {k: v for k, v in R.items()}
for k in ["lr", "batch"]:
    light[k] = {a: {x: y for x, y in b.items() if x != "curve"} for a, b in R[k].items()}
print(json.dumps(light, ensure_ascii=False, indent=1, default=str))
