---
layout: page
title: Needleman-Wunsch Beispiel
permalink: /notizen/Sequence_Learning/01-comparing-sequences/needleman_wunsch_example
---

![Needleman-Wunsch Beispiel](/assets/images/needleman-wunsch-algorithm-example.png)

## Sequenzen

- Horizontale Sequenz (x-Achse): `HEAGAWGHEE`
- Vertikale Sequenz (y-Achse): `PAWHEAE`

## Was zeigt die Matrix?

- Jede Zelle enthält den **Score des besten Alignments** bis zu diesem Punkt.
- **Pfeile** zeigen den gewählten Pfad:
  - ↖️ Diagonal: Match oder Mismatch
  - ⬅️ Von links: Gap in vertikaler Sequenz (Insertion)
  - ⬆️ Von oben: Gap in horizontaler Sequenz (Deletion)

## Ziel

Durch **Backtrace vom letzten Feld (rechts unten)** wird das **optimale Alignment** rekonstruiert.

## Optimales Alignment aus dem Bild

```
HEAGAWGHE-E
-P-A--W-HEAE
```

## Bedeutung des Alignments

| Zeichen x (Seq1) | Zeichen y (Seq2) | Operation   |
|------------------|------------------|-------------|
| H                | -                | Deletion    |
| E                | P                | Mismatch    |
| A                | A                | Match       |
| G                | -                | Deletion    |
| A                | -                | Deletion    |
| W                | W                | Match       |
| G                | -                | Deletion    |
| H                | H                | Match       |
| E                | E                | Match       |
| -                | A                | Insertion   |
| E                | E                | Match       |

## Fazit

- Der grüne Pfad in der Matrix zeigt das **optimale globale Alignment**.
- Die Matrix enthält sowohl die **Punktzahlen** als auch die **Pfeile für die Rückverfolgung**.
- Durch Nachvollziehen dieses Pfads erhält man das **beste mögliche Alignment beider Sequenzen**.