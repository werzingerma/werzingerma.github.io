---
layout: page
title: Zipf-Verteilung und Smoothing
permalink: /notizen/Sequence_Learning/02-markov-chains/zipf-smoothing
---

## Zipf'sches Gesetz

Das **Zipf-Gesetz** beschreibt die Häufigkeitsverteilung von Wörtern:
$\text{Häufigkeit} \propto \frac{1}{\text{Rang}}$

Beispiel: Das zweithäufigste Wort kommt etwa halb so oft vor wie das häufigste.

### Code zum Plotten

```python
import matplotlib.pyplot as plt
from collections import Counter

text = "der hund bellt der hund rennt der hund schläft"
tokens = text.split()
counts = Counter(tokens)
frequencies = sorted(counts.values(), reverse=True)

plt.plot(range(1, len(frequencies)+1), frequencies)
plt.xscale("log")
plt.yscale("log")
plt.title("Zipf-Verteilung")
plt.xlabel("Rang")
plt.ylabel("Häufigkeit")
plt.show()
```

## Problem: Null-Wahrscheinlichkeiten

Bei MLE kann es vorkommen, dass manche Bigramme nie auftreten → Wahrscheinlichkeit = 0.

### Beispiel

* "mag wasser" kommt nie vor → P(wasser \| mag) = 0 → Modell bricht zusammen

## Lösung: Smoothing

### Add-One-Smoothing (Laplace)

$P(w_n | w_{n-1}) = \frac{\text{H}(w_{n-1}, w_n) + 1}{\text{H}(w_{n-1}) + V}$
mit $V$ = Anzahl verschiedener Wörter (Vokabulargröße)

### Python-Beispiel

```python
V = len(set(tokens))
numerator = counts_bigram.get(('mag', 'wasser'), 0) + 1
denominator = counts_unigram['mag'] + V
prob = numerator / denominator
print(f"P(wasser | mag) mit Smoothing = {prob:.4f}")
```

## Anwendungen

* Robustere Sprachmodelle
* Generierung auch für seltene/unsichtbare Wortfolgen
