---
layout: page
title: N-Grams
permalink: /notizen/Sequence_Learning/02-markov-chains/ngrams
---

Ein **n‑Gram** ist eine Kette von `n` aufeinanderfolgenden Tokens aus einem Text. In Sprachmodellen schätzen wir, wie wahrscheinlich das nächste Wort ist, wenn wir die letzten `n − 1` Wörter kennen.

## Formel

Für ein Bi‑gramm (`n = 2`) gilt

```
P(w_i | w_{i-1}) = C(w_{i-1}, w_i) / C(w_{i-1})
```

`C(⋅)` steht für beobachtete Häufigkeiten im Korpus.

> **Markov‑Bezug**: Ein n‑Gram‑Modell ist eine Markov‑Kette der Ordnung `n − 1`.

---

## Beispiel­code: Uni‑, Bi‑ und Tri‑grams

```python
from collections import Counter

def ngrams(seq, n):
    """Erzeuge Zähler für alle n‑Grams in der Sequenz."""
    return Counter(tuple(seq[i:i+n]) for i in range(len(seq)-n+1))

text = "make america great again".lower().split()
print("Unigrams ", ngrams(text, 1))
print("Bigrams  ", ngrams(text, 2))
print("Trigrams ", ngrams(text, 3))
```

Jedes `Counter`‑Objekt enthält das N‑Gram als Schlüssel und die Häufigkeit als Wert. Durch Ändern des Parameters `n` lässt sich dieselbe Funktion für *beliebige* n‑Grams nutzen.

---

## Anwendung

* **Sprachmodelle** (Autovervollständigung, ASR)
* **Textklassifikation** (Autorschaft, Sentiment)
* **Maschinelle Übersetzung**, **Spell‑Checker**

Durch Vergrößerung von `n` steigt der Kontext, aber auch die Zahl der Parameter und damit die Daten­knappheit → *Smoothing* notwendig (siehe *Wichtige Begriffe*).
