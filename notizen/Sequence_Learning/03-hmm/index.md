---
layout: page
title: Hidden Markov Modelle (HMM)
permalink: /notizen/Sequence_Learning/03-hmm/index
---

## Was ist ein Hidden Markov Modell (HMM)?

Ein **Hidden Markov Modell** ist eine Erweiterung des klassischen Markov-Modells. Während bei Markov-Ketten die Zustände direkt beobachtbar sind, sind sie bei einem HMM **"versteckt"** (hidden). Stattdessen beobachten wir **Ausgaben/Emissionen**, die von diesen versteckten Zuständen abhängen.

## Unterschied zu normalen Markov-Ketten

| Merkmal               | Markov-Kette        | Hidden Markov Modell (HMM)   |
| --------------------- | ------------------- | ---------------------------- |
| Zustände beobachtbar? | Ja                  | Nein                         |
| Ausgaben/Emissionen?  | Nein                | Ja                           |
| Ziel                  | Zustand vorhersagen | Versteckte Zustände schätzen |

## Struktur eines HMM

Ein HMM besteht aus:

1. **Zustandsmenge** $S = \{s_1, s_2, \dots, s_N\}$
2. **Beobachtungsalphabet** $O = \{o_1, o_2, \dots, o_M\}$
3. **Startwahrscheinlichkeiten** $\pi_i = P(q_1 = s_i)$
4. **Übergangswahrscheinlichkeiten** $a_{ij} = P(q_{t+1} = s_j \| q_t = s_i)$
5. **Emissionswahrscheinlichkeiten** $b_j(o_k) = P(o_k \| q_t = s_j)$

## Beispiel mit Python-Code

Angenommen, wir haben ein Wettermodell mit zwei Zuständen: "Sonnig" und "Regnerisch" und drei mögliche Beobachtungen: "Spaziergang", "Shoppen", "Putzen".

```python
import numpy as np

states = ['Sonnig', 'Regnerisch']
observations = ['Spaziergang', 'Shoppen', 'Putzen']

start_prob = np.array([0.6, 0.4])
transition_prob = np.array([
    [0.7, 0.3],
    [0.4, 0.6]
])
emission_prob = np.array([
    [0.6, 0.3, 0.1],  # Sonnig
    [0.1, 0.4, 0.5]   # Regnerisch
])

obs_sequence = [0, 1, 2]  # Spaziergang, Shoppen, Putzen
```

## Was kann man mit dem Modell machen?

* **Forward-Algorithmus**: Wahrscheinlichkeit der Beobachtung berechnen
* **Viterbi-Algorithmus**: Wahrscheinlichste Zustandsfolge berechnen
* **Baum-Welch-Algorithmus**: Lernen der HMM-Parameter aus Daten

## Ausblick

Die folgenden Markdown-Dateien behandeln jeweils:

* Forward- & Backward-Algorithmus [forward/backward](forward_backward.md)
* Viterbi-Algorithmus [viterbi](viterbi.md)
* Baum-Welch (EM-Training) [baum-welch](baum_welch.md)
* Beobachtungsmodell [beobachtungsmodell](beobachtungsmodell.md)
* Isolated Word Recognition [isolated word recognition](isolated_word_recognition.md)