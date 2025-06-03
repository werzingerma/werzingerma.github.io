---
layout: page
title: Isolated Word Recognition mit HMM
permalink: /notizen/Sequence_Learning/03-hmm/isolated_word_recognition
---

## Ziel

Erkenne **einzelne gesprochene Wörter** aus einer Audiodatei mithilfe von **Hidden Markov Modellen** (HMMs).

Diese Technik wird z. B. im Sprachassistenten-Training verwendet, um Wörter wie "Ja", "Nein" oder Ziffern zuverlässig zu erkennen.

---

## Grundidee

* Jedes Wort bekommt ein eigenes HMM-Modell
* Die beobachtete Merkmalfolge (z. B. MFCC-Vektoren) wird mit jedem Modell bewertet
* Das Modell mit der **höchsten Wahrscheinlichkeit** gewinnt

$\text{argmax}_w\; P(O \mid \text{HMM}_w)$

---

## Beispielablauf

1. Extrahiere Merkmale (z. B. MFCCs) aus Audiosignal
2. Berechne mit dem **Forward-Algorithmus** die Wahrscheinlichkeit $P(O \mid \lambda)$ für jedes Wortmodell $\lambda$
3. Entscheide dich für das Modell mit dem höchsten Wert

---

## Python-Beispiel (vereinfacht)

Angenommen, wir haben zwei Modelle ("eins" und "zwei")

```python
from hmmlearn import hmm
import numpy as np

# Beispielhafte Merkmalsvektoren für ein Testwort
O = np.array([[1.2], [0.9], [1.1], [1.0]])  # z. B. MFCC-Folge

# Zwei trainierte Modelle für verschiedene Wörter
model_eins = hmm.GaussianHMM(n_components=3)
model_zwei = hmm.GaussianHMM(n_components=3)

# (Hier würde man .fit(...) mit Trainingsdaten aufrufen)

# Bewertung
score_eins = model_eins.score(O)
score_zwei = model_zwei.score(O)

if score_eins > score_zwei:
    print("Erkanntes Wort: eins")
else:
    print("Erkanntes Wort: zwei")
```

---

## Was bringt das?

* Robuste Erkennung von Einzelwörtern auch bei variierender Aussprache
* Grundlage für Sprachsteuerung und assistive Systeme
* Auch kombinierbar mit Viterbi für genaue Pfadrekonstruktion

---

## Weiterführend

* Bei kontinuierlicher Sprache ist ein **Lexikon + Sprachemodell** notwendig (nicht isoliert)
* Alternative Trainingsmethode: **Baum-Welch** (wenn keine Labels vorhanden sind)
