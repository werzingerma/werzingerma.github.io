---
layout: page
title: Forward- und Backward-Algorithmus in HMMs
permalink: /notizen/Sequence_Learning/03-hmm/forward_backward
---

## Ziel

Berechne die **Gesamtwahrscheinlichkeit** einer Beobachtungssequenz $O = (o_1, \dots, o_T)$:
$P(O | \text{Modell})$

Zwei Wege:

* **Forward-Algorithmus**: summiert über alle Pfade bis zum aktuellen Zeitpunkt
* **Backward-Algorithmus**: summiert über alle Fortsetzungen ab einem Zeitpunkt

---

## Forward-Algorithmus ($\alpha$)

### Definition

$\alpha_t(j) = P(o_1, \dots, o_t, q_t = s_j)$

### Rekursion

1. Initialisierung:
   $\alpha_1(j) = \pi_j \cdot b_j(o_1)$
2. Rekursion:
   $\alpha_t(j) = \left( \sum_{i=1}^N \alpha_{t-1}(i) \cdot a_{ij} \right) \cdot b_j(o_t)$
3. Abschluss:
   $P(O) = \sum_j \alpha_T(j)$

---

## Beispiel: HMM Wettermodell

Beobachtungen: Spaziergang, Shoppen, Putzen (entspricht \[0, 1, 2])

```python
import numpy as np

states = ['Sonnig', 'Regnerisch']
obs = [0, 1, 2]
start = [0.6, 0.4]
trans = [[0.7, 0.3], [0.4, 0.6]]
emit = [[0.6, 0.3, 0.1], [0.1, 0.4, 0.5]]

T = len(obs)
N = len(states)
alpha = np.zeros((T, N))

# Initialisierung
t = 0
for j in range(N):
    alpha[t][j] = start[j] * emit[j][obs[t]]

# Rekursion
for t in range(1, T):
    for j in range(N):
        alpha[t][j] = sum(alpha[t-1][i] * trans[i][j] for i in range(N)) * emit[j][obs[t]]

# Endsumme
prob = sum(alpha[T-1])
print("P(O):", prob)
```

### Rechnung Beispiel (T=3)

$$
\alpha_0 = [0.6 \cdot 0.6, 0.4 \cdot 0.1] = [0.36, 0.04] \\
\alpha_1(S) = (0.36 \cdot 0.7 + 0.04 \cdot 0.4) \cdot 0.3 = 0.0756 \\
\alpha_1(R) = (0.36 \cdot 0.3 + 0.04 \cdot 0.6) \cdot 0.4 = 0.0432 \\
\alpha_2(S) = (0.0756 \cdot 0.7 + 0.0432 \cdot 0.4) \cdot 0.1 = 0.005292 \\
\alpha_2(R) = (0.0756 \cdot 0.3 + 0.0432 \cdot 0.6) \cdot 0.5 = 0.01296 \\
\Rightarrow P(O) = 0.005292 + 0.01296 = 0.018252
$$

---

## Backward-Algorithmus ($\beta$)

### Definition

$\beta_t(i) = P(o_{t+1}, \dots, o_T \| q_t = s_i)$

### Rekursion

1. Initialisierung:
   $\beta_T(i) = 1$
2. Rekursion rückwärts:
   $\beta_t(i) = \sum_j a_{ij} \cdot b_j(o_{t+1}) \cdot \beta_{t+1}(j)$

### Beispiel in Python

```python
beta = np.zeros((T, N))
beta[T-1] = [1, 1]  # Initialisierung

for t in reversed(range(T-1)):
    for i in range(N):
        beta[t][i] = sum(trans[i][j] * emit[j][obs[t+1]] * beta[t+1][j] for j in range(N))

prob_b = sum(start[i] * emit[i][obs[0]] * beta[0][i] for i in range(N))
print("P(O) via backward:", prob_b)
```

### Validierung

$P(O) \text{ via forward } = P(O) \text{ via backward} = 0.018252$

---

## Anwendung

* **Likelihood-Berechnung** von Sequenzen
* **Baum-Welch** verwendet beide (siehe nächste Datei)
* **Zustandswahrscheinlichkeiten**: $\gamma_t(i) = \frac{\alpha_t(i) \cdot \beta_t(i)}{P(O)}$
