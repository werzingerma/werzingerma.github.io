---
layout: page
title: Wichtige Begriffe & Konzepte
permalink: /notizen/Sequence_Learning/02-markov-chains/markov_chain_terms
---

## Markov‑Annahme

Der Folgezustand eines Prozesses hängt **ausschließlich** vom aktuellen Zustand ab, nicht von weiter zurückliegender Vergangenheit. Das erlaubt eine kompakte Beschreibung als Übergangs­matrix bzw. gerichteten Graphen.

### Beispiel / Code

```python
# Wir referenzieren das Wetter‑Beispiel aus markov_chain_example1.md
next_tag = next_state('sunny')
print(next_tag)  # → z. B. 'cloudy' oder 'sunny'
```

`next_state` berücksichtigt nur den aktuellen Zustand (`'sunny'`) – die gesamte Sequenz davor spielt keine Rolle. So manifestiert sich die Markov‑Annahme praktisch im Code.

### Markov Annahme vs Markov-Kette

- Die Markov-Annahme ist die Aussage, dass der nächste Zustand nur vom aktuellen Zustand abhängt.
- Eine Markov-Kette ist ein konkretes stochastisches Modell / Prozess, der genau diese Annahme erfüllt.

---

## Token vs. Type

* **Token** → jedes einzelne Auftreten eines Wortes in einem Text.
* **Type**  → die eindeutige Wortform (»Wörterbuch­eintrag«).
  Ein Text mit 100 Tokens kann z. B. 60 Types enthalten, wenn manche Wörter mehrfach vorkommen.

### Beispiel / Code

```python
text = "Make America great again, make America smart again."
tokens = text.lower().split()
print(len(tokens))           # 8 Tokens
print(len(set(tokens)))      # 6 Types
```

Obwohl 8 Wörter (Tokens) vorkommen, sind es nur 6 verschiedene Wortformen (Types) – »make« und »america« erscheinen jeweils doppelt. Diese Unterscheidung ist wichtig, wenn man Häufigkeiten und Wahrscheinlichkeiten schätzt.

---

## Wahrscheinlichkeits­abschätzung

Die einfachste Schätzung der Auftritts­wahrscheinlichkeit eines Ereignisses ist die **relative Häufigkeit**:
$\hat P(x) = \frac{C(x)}{N}$

*$C(x)$: Anzahl der Beobachtungen*  
*$N$: Gesamtzahl aller Beobachtungen*

### Beispiel / Code

```python
from collections import Counter
words = "a a a b b c".split()
C = Counter(words)
N = len(words)
P_a = C['a'] / N
print(P_a)   # 0.5
```

Von 6 Tokens sind 3 mal `'a'` aufgetreten → $\hat P(a)=3/6=0{,}5$. Dieses Prinzip verwenden wir auch beim Zählen von N‑Grams (z. B. Bi‑gram‑Wahrscheinlichkeiten).

---

## Zipf‑Verteilung

In vielen natürlichsprachlichen Korpora folgt die Rang‑Häufigkeits‑Kurve etwa dem Gesetz:
*Häufigkeit ≈ 1 / Rang*
→ wenige Wörter sind extrem häufig, sehr viele Wörter extrem selten.

![Zipf‑Verteilung](/assets/images/zipf_verteilung.png)

### Beispiel / Code

```python
import matplotlib.pyplot as plt
from collections import Counter
import re

with open('alice.txt') as f:
    words = re.findall(r"\w+", f.read().lower())
counts = Counter(words)

ranks  = range(1, len(counts)+1)
frequ  = [c for _, c in counts.most_common()]

plt.loglog(ranks, frequ)
plt.title("Zipf‑Plot – Alice im Wunderland")
plt.xlabel("Rang")
plt.ylabel("Häufigkeit")
plt.show()
```

In der doppelt logarithmischen Darstellung bildet die Kurve nahezu eine Gerade – das Charakteristikum der Zipf‑Verteilung. Dies erklärt, warum bei N‑Gram‑Modellen viele mögliche Wort­folgen nie beobachtet werden; **Smoothing** (z. B. Laplace) wird nötig, um Null‑Wahrscheinlichkeiten zu vermeiden.

### Smoothing
**Smoothing** (Glättung) gibt auch nie beobachteten N-Grammen eine kleine, von den beobachteten Häufigkeiten abgezweigte Wahrscheinlichkeit, indem man z. B. bei der Laplace-Methode zu jedem Zähler 1 addiert.
Hat man nur die Bigramme „die Katze“ (3×) und „die Maus“ (1×) gesehen, aber nie „die Kuh“, erhält man mit Laplace $P(\text{‚Kuh‘}|\text{‚die‘}) = (0+1)/(3+1+0+3) = 1/7$ statt 0.
