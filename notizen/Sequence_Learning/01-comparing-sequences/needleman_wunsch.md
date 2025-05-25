---
layout: page
title: Needleman-Wunsch Algorithmus
permalink: /notizen/Sequence_Learning/01-comparing-sequences/needleman_wunsch
---

[Needleman-Wunsch - Ausführliches Beispiel](needleman_wunsch_example.md)

## Was ist der Needleman-Wunsch-Algorithmus?

Der Needleman-Wunsch-Algorithmus ist ein dynamisches Programmierverfahren zur **globalen Sequenz-Alignment** zweier Zeichenketten.  
Er wurde ursprünglich in der **Bioinformatik** entwickelt, um DNA-/Proteinsequenzen zu vergleichen.

## Ziel

Ein Alignment finden, das den **maximalen Score** erzielt, unter Berücksichtigung von:

- **Match-Belohnung** (z. B. +1 oder +10)
- **Mismatch-Strafe** (z. B. −1 oder −3)
- **Gap-Penalty** für Einfügungen/Löschungen (z. B. −1)

## Beispiel: Ähnlichkeitsmatrix (sim)

|     | A  | G  | C  | T  |
|-----|----|----|----|----|
| A   | 10 | −1 | −3 | −4 |
| G   | −1 |  7 | −5 | −3 |
| C   | −3 | −5 |  9 |  0 |
| T   | −4 | −3 |  0 |  8 |

### Warum sind die Werte unterschiedlich?

- **Matches (z. B. A-A, C-C, G-G, T-T)** geben positive Werte, aber **nicht alle gleich**:
  - Das liegt daran, dass **nicht jede Übereinstimmung biologisch gleichwertig ist**.
  - Beispielsweise ist A-A sehr häufig → hoher Score **(+10)**.
  - C-C kann weniger stabil sein oder seltener vorkommen → geringerer Score **(+9)**.

- **Mismatches** (z. B. A-G, A-C, etc.) geben negative Punkte – abhängig von:
  - **Wie unterschiedlich** die Basen oder Zeichen biologisch/semantisch sind.
  - Wie **„verzeihlich“** eine Verwechslung ist. Ein A↔T könnte weniger „bestraft“ werden als A↔C.

→ Die Ähnlichkeitsmatrix kann also **biologisch motiviert angepasst** werden – je nach Anwendung.

### Schlussfolgerungen aus der Matrix

- Hohe Scores (z. B. A-A = 10) bevorzugen Matches → das Alignment wird versuchen, möglichst viele Zeichen direkt zu matchen.
- Mismatches mit stark negativen Werten (z. B. G-C = −5) werden eher vermieden – es kann stattdessen ein Gap eingefügt werden.
- Das optimale Alignment hängt vom **Verhältnis zwischen Match-Belohnung, Mismatch-Strafe und Gap-Penalty** ab.

### Beispiel 1: Ideales Alignment möglich

```
x = ACGT
y = ACGT
```

→ Alle Zeichen passen perfekt (A-A, C-C, G-G, T-T) → maximales Matching ohne Gaps.  
**Ergebnis:** Gesamtscore = 10 + 9 + 7 + 8 = **34**

### Beispiel 2: Kein perfektes Alignment

```
x = AGGT
y = ATCT
```

- A-A → +10  
- G-T → −3 (Mismatch)  
- G-C → −5 (Mismatch)  
- T-T → +8  

→ Direktes Matching bringt Score: 10 − 3 − 5 + 8 = **10**  
→ Möglicherweise besser, ein Gap zu setzen, z. B.:

```
x: A G - G T
y: A - T C T
```

→ Einfügen von Gaps kann je nach Gap-Penalty (z. B. −5) vorteilhafter sein als manche Mismatches.

**Fazit:** Die Matrix beeinflusst maßgeblich, **welches Alignment als „optimal“ gilt**.

## Python-Implementierung

```python
import numpy as np

def nw(x, y, d, sim):
    D = np.zeros((len(x) + 1, len(y) + 1), dtype=int)

    # Initialisierung der Ränder
    D[0, 1:] = range(1, len(y) + 1)
    D[0, 1:] *= d
    D[1:, 0] = range(1, len(x) + 1)
    D[1:, 0] *= d

    # Füllen der Matrix
    for i in range(1, len(x)):
        for j in range(1, len(y)):
            cs = D[i-1, j-1] + sim(x[i], y[j])  # Match oder Mismatch
            cd = D[i-1, j] + d                  # Deletion (Gap in y)
            ci = D[i, j-1] + d                  # Insertion (Gap in x)
            D[i,j] = max(cs, cd, ci)            # Maximaler Score

    print(D)
    return D[len(x)-1][len(y)-1]
```

## Erklärung des Codes

- **D ist die Score-Matrix** mit Dimension (len(x)+1) × (len(y)+1).
- Die erste Zeile und Spalte werden mit den Gap-Strafen initialisiert.
- Jede Zelle `D[i][j]` wird auf Basis der drei Möglichkeiten berechnet:
  - **cs**: Diagonal – Match/Mismatch (abhängig vom Ähnlichkeitswert)
  - **cd**: Oben – Deletion
  - **ci**: Links – Insertion
- Die beste Option (höchster Score) wird gewählt → globales Maximum.

## Anwendung

- Bioinformatik: Vergleich von DNA-, RNA- oder Proteinsequenzen
- Plagiatserkennung: Vergleich kompletter Texte
- Computerlinguistik: Alignment von Sätzen oder Wörtern

## Wichtig

- Needleman-Wunsch ist ein **globaler Alignment-Algorithmus**: 
  → vergleicht die **gesamten Sequenzen von Anfang bis Ende**
- Er unterscheidet sich vom Levenshtein-Ansatz dadurch, dass man hier mit **belohnungsbasierten Scores** arbeitet (nicht nur mit Distanzen).
