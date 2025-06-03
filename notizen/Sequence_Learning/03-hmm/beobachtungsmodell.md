---
layout: page
title: Beobachtungsmodell im Hidden Markov Modell
permalink: /notizen/Sequence_Learning/03-hmm/beobachtungsmodell
---

# Ziel

Ein **Beobachtungsmodell** definiert, wie beobachtbare Symbole $o_t$ aus versteckten Zuständen $q_t$ erzeugt werden. Es modelliert die Wahrscheinlichkeit:
$b_j(o_t) = P(o_t \mid q_t = s_j)$

Diese Werte bilden die **Emissionsmatrix** $B$.

---

## Beispiel: Wettermodell

Zustände:

* $s_1 =$ Sonnig
* $s_2 =$ Regnerisch

Beobachtungen:

* $o_1 =$ Spaziergang
* $o_2 =$ Shoppen
* $o_3 =$ Putzen

### Emissionsmatrix $B$:

| Zustand \ Beobachtung | Spaziergang | Shoppen | Putzen |
| --------------------- | ----------- | ------- | ------ |
| Sonnig                | 0.6         | 0.3     | 0.1    |
| Regnerisch            | 0.1         | 0.4     | 0.5    |

$b_1(\text{Spaziergang}) = 0.6$, $b_2(\text{Putzen}) = 0.5$, etc.

---

## Python-Darstellung

```python
emissions = {
    'Sonnig':    {'Spaziergang': 0.6, 'Shoppen': 0.3, 'Putzen': 0.1},
    'Regnerisch':{'Spaziergang': 0.1, 'Shoppen': 0.4, 'Putzen': 0.5},
}

# Zugriff:
p = emissions['Sonnig']['Shoppen']  # 0.3
```

---

## Anwendung

* Wahrscheinlichkeiten für Beobachtungen im **Forward-/Backward-/Viterbi**-Algorithmus
* Essenziell beim Lernen via **Baum-Welch**
* Kann kontinuierlich (z. B. mit Gaussverteilungen) oder diskret (z. B. als Wahrscheinlichkeiten) sein

---

## Was bringt das?

* Verbindet beobachtbare Daten mit nicht direkt sichtbaren Zuständen
* Zentrale Komponente des HMM zum Modellieren realer Systeme (Sprache, Bioinformatik, Bewegung)
* Über Emissionen wird das HMM praktisch anwendbar
