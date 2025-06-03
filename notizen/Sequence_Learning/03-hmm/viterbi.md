---
layout: page
title: Viterbi-Algorithmus - Wahrscheinlichste Zustandsfolge in HMMs
permalink: /notizen/Sequence_Learning/03-hmm/viterbi
---

## Ziel

Gegeben eine Beobachtungssequenz $O = (o_1, o_2, \dots, o_T)$ wollen wir die **wahrscheinlichste Sequenz von versteckten Zuständen** $Q = (q_1, q_2, \dots, q_T)$ berechnen.

## Idee

Der **Viterbi-Algorithmus** ist ein dynamisches Programmierverfahren. Er speichert zu jedem Zeitpunkt:

* Die maximale Wahrscheinlichkeit bis zu diesem Punkt
* Den vorherigen Zustand, der dazu führte

## Beispielmodell (aus HMM-Grundlagen-Datei)

```python
states = ['Sonnig', 'Regnerisch']
observations = ['Spaziergang', 'Shoppen', 'Putzen']
obs_sequence = [0, 1, 2]  # Spaziergang, Shoppen, Putzen

start_prob = [0.6, 0.4]
trans = [
    [0.7, 0.3],
    [0.4, 0.6]
]
emit = [
    [0.6, 0.3, 0.1],
    [0.1, 0.4, 0.5]
]
```

## Mathematische Rekursion

Sei $\delta_t(j)$ die Wahrscheinlichkeit der besten Sequenz bis zum Zeitpunkt $t$ und Zustand $s_j$:
$\delta_t(j) = \max_i [\delta_{t-1}(i) \cdot a_{ij}] \cdot b_j(o_t)$

## Schrittweise Berechnung (Beispiel)

### Initialisierung (t = 0):

$$
\delta_0(Sonnig) = 0.6 \cdot 0.6 = 0.36 \\
\delta_0(Regnerisch) = 0.4 \cdot 0.1 = 0.04
$$

### Rekursion (t = 1, Beobachtung: "Shoppen")

Für "Sonnig":

$$
\max(0.36 \cdot 0.7, 0.04 \cdot 0.4) \cdot 0.3 = 0.252 \cdot 0.3 = 0.0756
$$

Für "Regnerisch":

$$
\max(0.36 \cdot 0.3, 0.04 \cdot 0.6) \cdot 0.4 = 0.108 \cdot 0.4 = 0.0432
$$

### Rekursion (t = 2, Beobachtung: "Putzen")

Für "Sonnig":

$$
\max(0.0756 \cdot 0.7, 0.0432 \cdot 0.4) \cdot 0.1 = 0.05292 \cdot 0.1 = 0.005292
$$

Für "Regnerisch":

$$
\max(0.0756 \cdot 0.3, 0.0432 \cdot 0.6) \cdot 0.5 = 0.02592 \cdot 0.5 = 0.01296
$$

### Rückverfolgung

Die maximale Wahrscheinlichkeit am Ende ist:
$\max(0.005292, 0.01296) = 0.01296 \Rightarrow letzter Zustand: Regnerisch$

Verfolgt man die Pfade zurück, ergibt sich:
$\text{Zustandsfolge: } \text{Sonnig} \rightarrow \text{Sonnig} \rightarrow \text{Regnerisch}$

## Python-Code

```python
import numpy as np

n_states = len(states)
n_obs = len(obs_sequence)

delta = np.zeros((n_obs, n_states))
psi = np.zeros((n_obs, n_states), dtype=int)

# Initialisierung
delta[0] = [start_prob[i] * emit[i][obs_sequence[0]] for i in range(n_states)]

# Rekursion
for t in range(1, n_obs):
    for j in range(n_states):
        seq_probs = [delta[t-1][i] * trans[i][j] for i in range(n_states)]
        psi[t][j] = np.argmax(seq_probs)
        delta[t][j] = max(seq_probs) * emit[j][obs_sequence[t]]

# Rückverfolgung
path = [np.argmax(delta[-1])]
for t in range(n_obs-1, 0, -1):
    path.insert(0, psi[t][path[0]])

state_seq = [states[i] for i in path]
print("Wahrscheinlichste Zustandsfolge:", state_seq)
```

## Was bringt das?

* Zustandssequenzen rekonstruieren, z. B. POS-Tagging, Bioinformatik
* Analyse nicht direkt beobachtbarer Prozesse auf Basis beobachteter Daten
