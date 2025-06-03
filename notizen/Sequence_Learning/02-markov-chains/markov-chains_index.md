---
layout: page
title: Markov-Ketten und N-Grammen
permalink: /notizen/Sequence_Learning/02-markov-chains/markov-chains_index
---

## Allgemeine Einführung

### Was sind Markov-Ketten?

Eine **Markov-Kette** ist ein mathematisches Modell, das eine Folge von Ereignissen beschreibt, bei denen die Wahrscheinlichkeit des nächsten Ereignisses nur vom aktuellen Zustand abhängt und nicht von der gesamten bisherigen Geschichte.

Diese Eigenschaft nennt man **Markov-Eigenschaft**.

> Beispiel: Wenn du dich auf einem Spielbrett bewegst und dein nächster Zug nur von deiner aktuellen Position abhängt, nicht davon, wie du dorthin gekommen bist, dann ist das ein Markov-Prozess.

### Was sind N-Gramme?

Ein **N-Gramm** ist eine Folge von *n* aufeinanderfolgenden Elementen (z.B. Wörter oder Buchstaben) aus einer gegebenen Sequenz.

* Ein **Unigramm** ist ein einzelnes Element
* Ein **Bigramm** sind zwei aufeinanderfolgende Elemente
* Ein **Trigramm** sind drei usw.

Diese Technik wird in der Sprachverarbeitung verwendet, um Wahrscheinlichkeiten für Wortfolgen zu berechnen.

## Beispiel mit Python-Code: Textmodellierung mit Bigrammen

Wir erstellen ein einfaches Sprachmodell basierend auf Bigrammen (2-Gramme).

```python
import random
from collections import defaultdict

text = "ich mag kaffee ich mag tee ich trinke kaffee"

# Schritt 1: Tokenisierung
words = text.split()

# Schritt 2: Bigramme erstellen
bigrams = [(words[i], words[i+1]) for i in range(len(words)-1)]

# Schritt 3: Wahrscheinlichkeiten berechnen
model = defaultdict(list)
for w1, w2 in bigrams:
    model[w1].append(w2)

# Schritt 4: Text generieren
word = "ich"
output = [word]
for _ in range(5):
    next_words = model[word]
    if not next_words:
        break
    word = random.choice(next_words)
    output.append(word)

print("Generierter Text:", " ".join(output))
```

### Erklärung

1. Wir teilen den Text in Wörter (Tokens).
2. Wir erstellen Bigramme (Wortpaare).
3. Wir bauen ein Modell, das speichert, welches Wort auf welches folgen kann.
4. Wir generieren neuen Text, indem wir zufällig ein Folgewort aus dem Modell auswählen.

### Was kann man mit dem Ergebnis machen?

* Text vervollständigen oder generieren
* Stil eines Autors imitieren
* Wahrscheinlichkeiten von Wortfolgen schätzen
* Nächstes Wort vorhersagen

## Weitere Themen

Die folgenden Themen werden in separaten Teil behandelt:

1. **Markov-Annahme**: Was sie bedeutet und der Unterschied zur Markov-Kette [Markov-Annahme](markov-annahme.md)
2. **Token vs. Type**: Unterschied und Relevanz für Sprachverarbeitung [Token vs. Type]()
3. **Wahrscheinlichkeitsabschätzung**: z.B. Maximum Likelihood Estimation [Wahrscheinlichkeitsabschätzung]()
4. **Zipf-Verteilung & Smoothing**: Wortfrequenzverteilungen und Techniken zur Vermeidung von Nullwahrscheinlichkeiten [Zipf & Smoothing]()

---

Diese Anleitung ist ideal für den Einstieg in stochastische Modelle für Text und Sprache. Jede weitere Datei vertieft ein zentrales Konzept.
