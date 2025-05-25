---
layout: page
title: Levenshtein-Distanz (Edit Distance)
permalink: /notizen/Sequence_Learning/01-comparing-sequences/levenshtein_distance
---

## Was ist die Levenshtein-Distanz?

Die Levenshtein-Distanz beschreibt die minimale Anzahl an Editieroperationen, um eine Zeichenkette in eine andere zu überführen. Dabei sind erlaubt:

- **Insertion** (Einfügen eines Zeichens)
- **Deletion** (Löschen eines Zeichens)
- **Substitution** (Ersetzen eines Zeichens)

Die Levenshtein-Distanz ist also ein Maß für die Ähnlichkeit zweier Zeichenketten beliebiger Länge.

## Beispiel

```python
x = "kitten"
y = "sitting"
```

Um "kitten" in "sitting" zu überführen:

1. Substituiere 'k' → 's' → "sitten"
2. Substituiere 'e' → 'i' → "sittin"
3. Füge 'g' ein → "sitting"

**Levenshtein-Distanz = 3**

## Eigenschaften

- Funktioniert auch bei unterschiedlich langen Strings
- Berücksichtigt die drei Grundoperationen: Insert, Delete, Substitute
- Laufzeit der Standard-Implementierung:

![Zeitkomplexität der Levenshtein-Distanz](/assets/images/zeitkomplexität_levenshtein.png)

Bedeutung der Formel:
- n= Länge des ersten Strings (z. B. x)
- m= Länge des zweiten Strings (z. B. y)
- Das Produkt n⋅m ergibt die Anzahl der Zellen in der dynamischen Programmierungs-Matrix.
- Jeder Zellenwert wird in konstanter Zeit berechnet → daher insgesamt linear in der Anzahl der Matrixzellen.

## Python-Implementierung (Bottom-Up)
Bottom-Up bedeutet, dass man ein Problem löst, indem man zuerst alle kleinen Teilprobleme berechnet und deren Lösungen Schritt für Schritt zu einer Gesamtlösung zusammensetzt.

```python
import numpy as np

def edit(x, y):
    D = np.zeros((len(x) + 1, len(y) + 1), dtype=int)
    D[0, 1:] = range(1, len(y) + 1)
    D[1:, 0] = range(1, len(x) + 1)

    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            delta = 1 if x[i - 1] != y[j - 1] else 0
            D[i, j] = min(
                D[i - 1, j] + 1,
                D[i, j - 1] + 1,
                D[i - 1, j - 1] + delta
            )

    return D[len(x), len(y)]
```

## Erklärung des Codes

- `D` ist eine Matrix (Tabelle), in der für jedes Teilproblem die minimale Anzahl an Änderungen gespeichert wird.
- `D[i][j]` gibt die Levenshtein-Distanz zwischen den ersten `i` Zeichen von `x` und den ersten `j` Zeichen von `y` an.
- Die erste Zeile und Spalte der Matrix werden mit 0, 1, 2, ... gefüllt, da es so viele Schritte braucht, um aus einem leeren String einen String dieser Länge zu machen (nur Einfügungen oder Löschungen).
- Die Schleifen füllen dann die Matrix:
  - Wenn das aktuelle Zeichen in `x` und `y` gleich ist, ist `delta = 0` (kein Fehler).
  - Ansonsten `delta = 1` (ein Fehler – Substitution).
- In jeder Zelle wird das Minimum aus drei möglichen Operationen gewählt:
  1. **Löschen** eines Zeichens aus `x` (hochkommen in der Matrix)
  2. **Einfügen** eines Zeichens in `x` (von links kommen)
  3. **Substitution** (von diagonal kommen)

Am Ende steht in der unteren rechten Ecke `D[len(x)][len(y)]` die finale Levenshtein-Distanz.

## Beispielaufruf

```python
edit("kitten", "sitting")  # Ergebnis: 3
```

## Anwendung

- Rechtschreibkorrektur (z. B. Autovervollständigung)
- Bioinformatik (Sequenzvergleich von DNA/RNA)
- Versionsvergleich in Textverarbeitung
- Ähnlichkeitssuche in Datenbanken

## Wichtig

- Die Levenshtein-Distanz berücksichtigt Einfügungen, Löschungen und Ersetzungen.
- Im Gegensatz zur Hamming-Distanz funktioniert sie auch bei unterschiedlich langen Strings.
- Die Matrix-basierte Lösung erlaubt effiziente Berechnung und Backtracking zur Bestimmung des optimalen Edit-Transkripts.
