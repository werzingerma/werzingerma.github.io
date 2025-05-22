---
layout: page
title: SQL1 - comparing sequences
permalink: /notizen/Sequence_Learning/sql1/
---

# comparing sequences

## 📏 1. Hamming-Abstand

Der **Hamming-Abstand** zählt, **wie viele Stellen sich zwei gleich lange Bitfolgen unterscheiden**.

### Beispiel:
```
A: 1 0 1 1 0 0 1  
B: 1 0 0 1 1 0 1

Unterschiede an Position 3 und 5  
→ Hamming-Abstand = 2
```

### Anwendung:
- Vergleich von Audiosignalen oder Binärmerkmalen
- Fehlererkennung bei Datenübertragung

🔗 [Wikipedia: Hamming-Abstand](https://de.wikipedia.org/wiki/Hamming-Abstand)

---

## ✏️ 2. Edit-/Levenshtein-Abstand

Zählt die **minimale Anzahl an Operationen** (Einfügen, Löschen, Ersetzen), um eine Zeichenfolge in eine andere umzuwandeln.

### Beispiel:
```
"kitten" → "sitting"
1. kitten → sitten   (k → s)
2. sitten → sittin   (e → i)
3. sittin → sitting  (g anhängen)

→ Levenshtein-Abstand = 3
```

### Anwendung:
- Spracherkennung (z. B. erkannte Wörter vs. Zieltext)
- Rechtschreibkorrektur
- Ähnlichkeitsmessung

🔗 [Wikipedia: Levenshtein-Distanz](https://de.wikipedia.org/wiki/Levenshtein-Distanz)

---

## 🧾 3. Edit-Transcript / Alignment

Das **Edit-Transcript** beschreibt die **Reihenfolge der Schritte** (Insert, Delete, Substitute), um eine Sequenz in eine andere zu überführen.

### Beispiel:
```
A: kitten  
B: sitting

Transcript:
S(k → s), S(e → i), I(g)

Alignment (vereinfacht):
k i t t e n
| | | | | |
s i t t i n g
```

### Anwendung:
- Visualisierung von Fehlern bei automatischer Spracherkennung
- Auswertung von Vorhersagegenauigkeit

🔗 [Lecture Slide Beispiel (engl.) mit Edit Transcripts](https://web.stanford.edu/class/cs124/lec/med.pdf)

---

## 🔁 4. Dynamische Programmierung (DP)

**Grundprinzip**, bei dem große Probleme in **überlappende Teilprobleme** zerlegt und deren Lösungen **gespeichert (Memoization)** werden.

### Beispiel-Idee:
Beim Levenshtein- oder DTW-Algorithmus wird eine Matrix aufgebaut, die **Schritt für Schritt die optimale Lösung** berechnet, statt alles mehrfach zu prüfen.

### Anwendung:
- Basis für Edit-Distanzen, DTW, Alignment-Algorithmen
- Sehr effizient bei rekursiven Problemen

🔗 [Wikipedia: Dynamische Programmierung](https://de.wikipedia.org/wiki/Dynamische_Programmierung)

---

## 🧬 5. Needleman-Wunsch-Algorithmus

Ein auf dynamischer Programmierung basierender Algorithmus zur **globalen Sequenz-Ausrichtung**.

### Beispiel:
```
A: G A T T A C A  
B: G C A T G C U

Alignment:
G A T T A - C A
|   | |     | |
G C A T - G C U
```

### Anwendung:
- Sprachvergleiche über gesamte Zeiträume
- Ursprünglich für Bioinformatik, heute auch in Audioanalyse genutzt

🔗 [Needleman-Wunsch einfach erklärt (YouTube)](https://www.youtube.com/watch?v=3hcaVyX00_4)

---

## 🔄 6. Damerau-Levenshtein-Abstand

Erweiterung der Levenshtein-Distanz: erlaubt zusätzlich **Vertauschung benachbarter Zeichen (Transposition)**.

### Beispiel:
```
"ca" → "ac"
→ Levenshtein: 2 (Löschen + Einfügen)
→ Damerau-Levenshtein: 1 (Vertauschung)
```

### Anwendung:
- Besseres Modell für reale Tippfehler
- Nützlich bei Tastatureingaben und ASR

🔗 [Wikipedia: Damerau-Levenshtein-Distanz](https://de.wikipedia.org/wiki/Damerau-Levenshtein-Distanz)

---

## ⏱️ 7. Dynamic Time Warping (DTW)

Ein DP-basierter Algorithmus, der **ähnliche Zeitreihen unterschiedlicher Länge** vergleicht (z. B. Audiosignale).

### Beispiel:
```
Signal A: [1, 2, 3, 4, 5]
Signal B: [1, 1.5, 2.5, 4, 5]

→ DTW „verzerrt“ die Zeitachse, um optimale Übereinstimmung zu finden.
```

### Anwendung:
- Spracherkennung
- Audio-Matching
- Musikvergleich

🔗 [Wikipedia: Dynamic Time Warping](https://de.wikipedia.org/wiki/Dynamic_Time_Warping)
🔗 [DTW Erklärungsvideo (YouTube)](https://www.youtube.com/watch?v=3dZ_0s8f3N8)

---
