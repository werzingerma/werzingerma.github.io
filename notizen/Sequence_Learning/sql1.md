---
layout: page
title: SQL1 - comparing sequences
permalink: /notizen/Sequence_Learning/sql1/
---

# comparing sequences

## 1. Hamming-Abstand

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

## 2. Edit-/Levenshtein-Abstand

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

## 3. Edit-Transcript / Alignment

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

## 4. Dynamische Programmierung (DP)

**Grundprinzip**, bei dem große Probleme in **überlappende Teilprobleme** zerlegt und deren Lösungen **gespeichert (Memoization)** werden.

### Beispiel für Levenshtein:
Für die Wörter `kitten` und `sitting` wird eine Matrix erstellt, die jede mögliche Kombination von Teilstrings speichert. So wird Schritt für Schritt die minimale Anzahl von Änderungen bestimmt, statt alles mehrfach zu berechnen.

### Beispiel für DTW:
Für zwei Zeitreihen z. B. `[1, 2, 3]` und `[1, 1.5, 2.5, 3]` wird eine Matrix aufgebaut, die die Abweichung jedes Punktepaares misst. Durch „Verzerren“ der Zeitachsen wird der optimal passende Pfad gefunden.

### Anwendung:
- Basis für Edit-Distanzen, DTW, Alignment-Algorithmen
- Sehr effizient bei rekursiven Problemen

🔗 [Video: Dynamische Programmierung einfach erklärt (Teil 1)](https://www.youtube.com/watch?v=oNoILrFOx2k)  
🔗 [Video: Dynamische Programmierung einfach erklärt (Teil 2)](https://www.youtube.com/watch?v=aPQY__2H3tE)

---

## 5. Needleman-Wunsch-Algorithmus

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

🔗 [YouTube: Needleman-Wunsch Algorithmus erklärt (Deutsch)](https://www.youtube.com/watch?v=Lsa-VfSQgt4)

---

## 6. Damerau-Levenshtein-Abstand

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

🔗 [Wikipedia: Damerau-Levenshtein Distance (engl.)](https://en.wikipedia.org/wiki/Damerau–Levenshtein_distance)

---

## 7. Dynamic Time Warping (DTW)

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
🔗 [YouTube: DTW Explained – Part 1](https://www.youtube.com/watch?v=_K1OsqCicBY)  
🔗 [YouTube: DTW Explained – Part 2](https://www.youtube.com/watch?v=ERKDHZyZDwA)

---
