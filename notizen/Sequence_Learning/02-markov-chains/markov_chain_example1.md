---
layout: page
title: Beispiel 1 – Wetter‑Simulation
permalink: /notizen/Sequence_Learning/02-markov-chains/markov_chain_example1
---

Dieses Beispiel zeigt, wie man mit einer einfachen Markov‑Kette eine plausible Wetter­abfolge simuliert.

## Übergangswahrscheinlichkeiten

Wir verwenden drei Zustände – `sunny`, `cloudy`, `rainy` – und legen die Wahrscheinlichkeiten empirisch fest:

| von → nach | sunny | cloudy | rainy |
| ---------- | ----- | ------ | ----- |
| **sunny**  | 0.7   | 0.2    | 0.1   |
| **cloudy** | 0.3   | 0.4    | 0.3   |
| **rainy**  | 0.2   | 0.3    | 0.5   |

## Python‑Code

```python
import random
states = ["sunny", "cloudy", "rainy"]
P = {
    "sunny":  {"sunny":0.7, "cloudy":0.2, "rainy":0.1},
    "cloudy": {"sunny":0.3, "cloudy":0.4, "rainy":0.3},
    "rainy":  {"sunny":0.2, "cloudy":0.3, "rainy":0.5}
}

def next_state(s):
    """Ziehe den Folgezustand proportional zu den Übergangswahrscheinlichkeiten."""
    r, cum = random.random(), 0
    for nxt, p in P[s].items():
        cum += p
        if r < cum:
            return nxt

# Simulation: starte sonnig und laufe 10 Tage
seq = ["sunny"]
for _ in range(10):
    seq.append(next_state(seq[-1]))
print(seq)
```

### Was passiert hier?

1. **random.random()** liefert eine Zufalls­zahl $r\in[0,1)$.
2. Wir gehen die Nachfolger nacheinander durch und akkumulieren die Wahrscheinlichkeiten (`cum`).
   Sobald `cum` größer als `r` wird, ist der aktuelle Nachfolger gezogen.
3. Dieser Trick macht genau das, was in der Übergangsmatrix steht – häufige Kanten werden öfter getroffen.

> **Tipp:**  Je mehr Schritte du simulierst, desto stärker nähert sich die Verteilung der Zustände dem *stationären* Verhalten der Kette an.
