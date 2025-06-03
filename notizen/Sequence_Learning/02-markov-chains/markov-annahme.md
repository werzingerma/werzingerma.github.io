---
layout: page
title: Markov-Annahme vs. Markov-Kette
permalink: /notizen/Sequence_Learning/02-markov-chains/markov-annahme
---

## Markov-Annahme

Die **Markov-Annahme** ist eine Vereinfachung, die besagt:

> Die Wahrscheinlichkeit für das Auftreten eines Ereignisses hängt nur vom aktuellen Zustand ab, nicht von vorherigen Zuständen.

Formal:
$P(x_n | x_{n-1}, x_{n-2}, \dots, x_0) \approx P(x_n | x_{n-1})$

Diese Annahme macht komplexe Modelle berechenbar, da sie die Zahl der berücksichtigten Zustände drastisch reduziert.

## Unterschied zur Markov-Kette

* Die **Markov-Annahme** ist ein theoretisches Konzept.
* Eine **Markov-Kette** ist das mathematische Modell, das auf dieser Annahme basiert.

Die Kette besteht aus Zuständen und Übergangswahrscheinlichkeiten.

## Beispiel

Angenommen, du hast folgende Wörter in einem Satz:

> "ich gehe zur schule"

Mit der Markov-Annahme würden wir sagen:
$P(\text{"schule"} | \text{"gehe"}, \text{"ich"}) \approx P(\text{"schule"} | \text{"gehe"})$

Das heißt: Nur das vorherige Wort zählt für die Berechnung.

## Code-Beispiel

```python
from collections import Counter

text = "ich gehe zur schule ich gehe nach hause"
tokens = text.split()
bigrams = [(tokens[i], tokens[i+1]) for i in range(len(tokens)-1)]
counts = Counter(bigrams)

# Wahrscheinlichkeit von schule nach gehe:
bigram = ("gehe", "schule")
base = sum(c for (w1, w2), c in counts.items() if w1 == "gehe")
prob = counts[bigram] / base if base > 0 else 0
print(f"P(schule | gehe) = {prob:.2f}")
```

## Was bringt das?

* Reduktion der Komplexität
* Effizientere Berechnung in Sprachmodellen
* Grundlage für viele NLP-Anwendungen
