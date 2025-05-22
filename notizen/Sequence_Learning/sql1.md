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

---

### Beispiel für Levenshtein (kitten → sitting)

Wir berechnen die minimale Anzahl von Einfüge-, Lösch- oder Ersetz-Operationen, um "kitten" in "sitting" zu verwandeln.

**Wörter:**
- Quelle: `kitten`
- Ziel: `sitting`

Initiale Matrix (inkl. leere Zeichen "" vorangestellt):

|   |   | s | i | t | t | i | n | g |
|---|---|---|---|---|---|---|---|---|
|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| k | 1 |   |   |   |   |   |   |   |
| i | 2 |   |   |   |   |   |   |   |
| t | 3 |   |   |   |   |   |   |   |
| t | 4 |   |   |   |   |   |   |   |
| e | 5 |   |   |   |   |   |   |   |
| n | 6 |   |   |   |   |   |   |   |

**Füllregel:**
- Wenn Buchstaben gleich → cost = 0
- Sonst → cost = 1
- Zelle = min(Einfügen, Löschen, Ersetzen) + cost

Wir füllen die Matrix zeilenweise, z. B.:
- Für Zelle (1,1): `k` vs. `s` → cost = 1 → min(1, 1, 0) + 1 = 1
- Für Zelle (2,2): `i` vs. `i` → cost = 0 → min(2, 2, 1) + 0 = 1
- usw.

Am Ende steht in der rechten unteren Ecke die Lösung: **3**

→ **Levenshtein-Abstand("kitten", "sitting") = 3**

---

### Beispiel für DTW (Dynamic Time Warping)

Wir vergleichen zwei Zeitreihen, z. B.:

```
A = [1, 2, 3]
B = [2, 2, 3, 4]
```

**Initialisierung:**
- Matrixgröße = len(A)+1 x len(B)+1
- Startpunkt (0,0) = 0, alle anderen Zellen ∞
- Abstand: quadratischer Abstand: `(a_i - b_j)^2`

**Schritt-für-Schritt-Füllung:**
```
DTW[0][0] = 0

Für alle i, j:
DTW[i][j] = (A[i-1] - B[j-1])^2 + min(
    DTW[i-1][j],     # Einfügen
    DTW[i][j-1],     # Löschen
    DTW[i-1][j-1]    # Match
)
```

**Beispielhafte Matrix für A=[1,2,3], B=[2,2,3,4] (gekürzt):**

|   |   | 2 | 2 | 3 | 4 |
|---|---|---|---|---|---|
|   | 0 | ∞ | ∞ | ∞ | ∞ |
| 1 | ∞ | 1 | 1 | 5 | 14 |
| 2 | ∞ | 1 | 1 | 2 | 6 |
| 3 | ∞ | 2 | 2 | 1 | 2 |

→ Der optimale Pfad (Warping Path) verläuft dort, wo die kumulierten Kosten am niedrigsten sind.  
→ **DTW-Abstand = 2** (unterste rechte Ecke)

---

### Anwendung:
- Basis für Edit-Distanzen, DTW, Alignment-Algorithmen
- Sehr effizient bei rekursiven Problemen

🔗 [Video: Dynamische Programmierung einfach erklärt (Teil 1)](https://www.youtube.com/watch?v=oNoILrFOx2k)  
🔗 [Video: Dynamische Programmierung einfach erklärt (Teil 2)](https://www.youtube.com/watch?v=aPQY__2H3tE)


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