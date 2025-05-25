---
layout: page
title: Kostenmodellierung (Modeling Cost)
permalink: /notizen/Sequence_Learning/01-comparing-sequences/cost_modelling
---

## Was bedeutet Kostenmodellierung?

Beim Vergleichen von Sequenzen (z. B. mit Edit-Distanz, Needleman-Wunsch, etc.) legt man fest, **wie „teuer“ bestimmte Operationen** sind:

- **Match (m)**: zwei gleiche Zeichen → meist kostenfrei oder sogar belohnt
- **Substitution (s)**: ein Zeichen wird durch ein anderes ersetzt → moderate Kosten
- **Insertion (i)**: ein Zeichen wird eingefügt → z. B. +1
- **Deletion (d)**: ein Zeichen wird entfernt → z. B. +1

Diese **Kostenwerte bestimmen, welches Alignment „optimal“ ist**, d. h. den geringsten Gesamtkostenwert hat.

## Beispiel: Gleichmäßige Kosten

```python
cost = {'m': 0, 's': 1, 'i': 1, 'd': 1}
```

→ Jede Änderung ist gleich gewichtet.

## Beispiel: Anpassung an ein Szenario

```python
cost = {'m': 0, 's': 2, 'i': 1, 'd': 1}
```

→ Substitution ist „schlimmer“ als Einfügen oder Löschen.

## Python-Beispiel für Edit Distance mit Kosten

```python
import numpy as np

def edit(x, y, cost={'m': 0, 's': 1, 'i': 1, 'd': 1}):
    D = np.zeros((len(x) + 1, len(y) + 1), dtype=int)
    D[0, 1:] = range(1, len(y) + 1)
    D[1:, 0] = range(1, len(x) + 1)

    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            delta = cost['m'] if x[i-1] == y[j-1] else cost['s']
            D[i, j] = min(
                D[i-1, j] + cost['d'],
                D[i, j-1] + cost['i'],
                D[i-1, j-1] + delta
            )

    return D[len(x), len(y)]
```

## Warum ist das wichtig?

- Durch Kostenmodellierung kannst du das Verhalten des Algorithmus **anpassen an die Anwendung**:
  - In Bioinformatik z. B. ist eine Insertion oft „günstiger“ als eine Substitution.
  - In Textverarbeitung kann eine falsche Taste (s ↔ a) durch eine **tastaturbasierte Gewichtung** berücksichtigt werden.
- Für **Autovervollständigung, Rechtschreibkorrektur, DNA-Alignments** etc. ist die **richtige Gewichtung entscheidend**.

## Erweiterungsmöglichkeiten

- **Kontextabhängige Kosten** (z. B. je nach vorherigem Zeichen)
- **Tastaturdistanz als Substitutionskosten**
- **Matrix-basiertes Kostenmodell** (wie bei Needleman-Wunsch)

## Fazit

Ein gutes Kostenmodell verbessert die Qualität des Alignments deutlich – es hilft dem Algorithmus, **relevante Fehler zu tolerieren** und **wichtige Übereinstimmungen zu erkennen**.
