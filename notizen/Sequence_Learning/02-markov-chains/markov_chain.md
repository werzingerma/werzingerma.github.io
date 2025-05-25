---
layout: page
title: Markov Chains
permalink: /notizen/Sequence_Learning/02-markov-chains/markov_chain
---

## Was ist eine Markov‑Chain?

Eine **Markov‑Kette** ist ein stochastischer Prozess, bei dem sich das System Schritt für Schritt von einem **Zustand** in den nächsten bewegt.
Die **Markov‑Annahme** besagt, dass die Wahrscheinlichkeit für den nächsten Zustand **nur** vom *aktuellen* Zustand abhängt – nicht von der gesamten Vorgeschichte.

```
P(X_{t+1}=x | X_t, X_{t-1}, …, X_0) = P(X_{t+1}=x | X_t)
```

---

## Darstellungsmöglichkeiten

### 1. Zustandsgraph

![Markov Chain](/assets/images/markov_chain.png)

* **Knoten** = Zustände (hier: Wetter‑Typen)
* **Kanten** = mögliche Übergänge mit einer **Übergangswahrscheinlichkeit**

### 2. Transitionsmatrix \$\mathbf P\$

| von → nach | Sunny | Cloudy | Rainy |
| ---------- | :---: | :----: | :---: |
| **Sunny**  |  0.8  |   0.1  |  0.1  |
| **Cloudy** |  0.1  |   0.4  |  0.5  |
| **Rainy**  |  0.2  |   0.3  |  0.5  |

Die Einträge jeder Zeile summieren sich zu 1 (100 %).

Die Dynamik lässt sich algebraisch beschreiben  
![markov_formel1](/assets/images/markov_chain_formel1.png)

#### Was macht man nun damit?

![markov_formel2](/assets/images/markov_chain_formel2.png)

```python
import numpy as np

P = np.array([[0.8,0.1,0.1],
              [0.1,0.4,0.5],
              [0.2,0.3,0.5]])

pi = np.array([1,0,0])   # Start: 100 % Sunny
for t in range(4):        # vier Tage vorhersagen
    pi = pi @ P     # @ ist in NumPy der Operator für Matrix-Multiplikation
    print(f"Tag {t+1}: {pi.round(3)}")
```

*Ausgabe*

```
Tag 1: [0.8   0.1   0.1  ]
Tag 2: [0.67  0.15  0.18 ]
Tag 3: [0.587 0.181 0.232]
Tag 4: [0.548 0.199 0.253]
```

> Nach einigen Schritten stabilisieren sich die Werte.
> Löst man \$\pi = \pi P\$, erhält man die **stationäre Verteilung**
> \$\pi^{(\*)} \approx (0.44, 0.24, 0.32)\$.
>
> **Interpretation**: Langfristig ist es zu ≈ 44 % *sonnig*, 24 % *bewölkt* und 32 % *regnerisch*.

---

## Einsatzgebiete

* **Wetter‑ und Klima‑Modelle** – Wahrscheinliche Wetterszenarien simulieren
* **Text‑, Musik‑ und Bilderzeugung** – Sequenzen generieren (siehe Beispiele)
* **Finanz‑ und Risikoanalyse** – Kursbewegungen, Kredit‑Defaults
* **Queueing‑ und Netzwerkmodelle** – Paket‑Routing, Warteschlangen‑Längen

---

### Weiterführende Beispiele

* [Beispiel 1 – Wetter‑Simulation](markov_chain_example1.md)
* [Beispiel 2 – Tweet‑Generator](markov_chain_example2.md)