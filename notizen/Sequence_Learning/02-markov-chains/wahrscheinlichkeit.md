---
layout: page
title: Wahrscheinlichkeitsabschätzung in Sprachmodellen
permalink: /notizen/Sequence_Learning/02-markov-chains/wahrscheinlichkeit
---

## Ziel

Wir wollen Wahrscheinlichkeiten für Wortfolgen abschätzen. Typischerweise:
$P(w_n | w_{n-1}) = \frac{\text{Häufigkeit}(w_{n-1}, w_n)}{\text{Häufigkeit}(w_{n-1})}$

Dies ist die **Maximum Likelihood Estimation (MLE)** für Bigramme.

## Beispiel

Text: "ich mag tee ich mag kaffee"

### Python-Code

```python
from collections import Counter

text = "ich mag tee ich mag kaffee"
tokens = text.split()
bigrams = [(tokens[i], tokens[i+1]) for i in range(len(tokens)-1)]
counts_bigram = Counter(bigrams)
counts_unigram = Counter(tokens[:-1])

# P(kaffee | mag)
numerator = counts_bigram[('mag', 'kaffee')]
denominator = counts_unigram['mag']
prob = numerator / denominator if denominator > 0 else 0

print(f"P(kaffee | mag) = {prob:.2f}")
```

## Was bringt das?

* Modelliert Vorhersagewahrscheinlichkeit
* Nützlich für Textgenerierung, Autovervollständigung
* Grundlage für komplexere Sprachmodelle (z.B. HMMs, RNNs)
