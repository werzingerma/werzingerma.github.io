---
layout: page
title: Baum-Welch-Algorithmus (EM-Training für HMM)
permalink: /notizen/Sequence_Learning/03-hmm/baum_welch
---

## Ziel

Lerne die **Parameter eines HMMs** ($\pi, A, B$) nur auf Basis beobachteter Sequenzen $O$, ohne dass die Zustandsfolgen bekannt sind.

Dieses Problem wird mit dem **Baum-Welch-Algorithmus** gelöst, einer Form des **Expectation-Maximization (EM)**-Verfahrens.

---

## Ablauf

### E-Schritt (Erwartung)

Berechne mit aktuellem Modell:

* $\alpha_t(i)$: Forward-Wahrscheinlichkeiten
* $\beta_t(i)$: Backward-Wahrscheinlichkeiten
* $\gamma_t(i) = P(q_t = s_i | O)$
* $\xi_t(i,j) = P(q_t = s_i, q_{t+1} = s_j | O)$

### M-Schritt (Maximierung)

Aktualisiere Parameter:

* $\pi_i = \gamma_0(i)$
* $a_{ij} = \frac{\sum_{t=0}^{T-2} \xi_t(i,j)}{\sum_{t=0}^{T-2} \gamma_t(i)}$
* $b_j(k) = \frac{\sum_{t, o_t = k} \gamma_t(j)}{\sum_{t=0}^{T-1} \gamma_t(j)}$

---

## Beispiel (1 Iteration, hart gecodet)

Modell wie zuvor: 2 Zustände (Sonnig, Regnerisch), 3 Beobachtungen (Spaziergang, Shoppen, Putzen)

```python
import numpy as np

# Daten und Modellinitialisierung
states = ['Sonnig', 'Regnerisch']
obs = [0, 1, 2]
start = [0.5, 0.5]
trans = np.array([[0.5, 0.5], [0.5, 0.5]])
emit = np.array([[0.4, 0.4, 0.2], [0.3, 0.3, 0.4]])

T = len(obs)
N = len(states)

# Forward
alpha = np.zeros((T, N))
for i in range(N):
    alpha[0][i] = start[i] * emit[i][obs[0]]
for t in range(1, T):
    for j in range(N):
        alpha[t][j] = sum(alpha[t-1][i] * trans[i][j] for i in range(N)) * emit[j][obs[t]]

# Backward
beta = np.ones((T, N))
for t in reversed(range(T-1)):
    for i in range(N):
        beta[t][i] = sum(trans[i][j] * emit[j][obs[t+1]] * beta[t+1][j] for j in range(N))

# Gamma & Xi
P_O = sum(alpha[-1])
gamma = (alpha * beta) / P_O

xi = np.zeros((T-1, N, N))
for t in range(T-1):
    denom = sum(alpha[t][i] * trans[i][j] * emit[j][obs[t+1]] * beta[t+1][j]
                for i in range(N) for j in range(N))
    for i in range(N):
        for j in range(N):
            xi[t][i][j] = (alpha[t][i] * trans[i][j] * emit[j][obs[t+1]] * beta[t+1][j]) / denom

# Neue Parameter berechnen
new_start = gamma[0]
new_trans = xi.sum(axis=0) / gamma[:-1].sum(axis=0)[:, None]
new_emit = np.zeros_like(emit)
for j in range(N):
    for k in range(3):
        mask = [o == k for o in obs]
        new_emit[j][k] = sum(gamma[t][j] for t in range(T) if mask[t]) / sum(gamma[:, j])

print("Neue Startverteilung:", new_start)
print("Neue Übergangsmatrix:\n", new_trans)
print("Neue Emissionsmatrix:\n", new_emit)
```

---

## Was bringt das?

* Lerne HMMs **vollautomatisch** aus Daten (z. B. Sprache, Bioinformatik, Bewegungsdaten)
* Ermöglicht Anwendungen wie Speech Tagging, Gestenerkennung, Worterkennung ohne manuelles Labeln

## Hinweis

Der Baum-Welch-Algorithmus wird **iterativ** wiederholt, bis sich die Parameter kaum ändern (Konvergenz).
