---
layout: page
title: Dynamic Time Warping (DTW)
permalink: /notizen/Sequence_Learning/01-comparing-sequences/dynamic_time_warping
---

## Was ist Dynamic Time Warping?

**Dynamic Time Warping (DTW)** ist ein Algorithmus zum Vergleichen zweier zeitabhängiger Sequenzen, die sich in der Länge oder Geschwindigkeit unterscheiden können.

Beispiel:
- Zwei Personen sagen „Hallo“, aber in unterschiedlichem Tempo
- DTW erkennt, dass die Signale ähnlich sind, **auch wenn sie zeitlich verzogen sind**

## Eigenschaften

- Funktioniert auf **nicht-diskreten Daten** (z. B. Zahlenreihen, Audio-Features wie MFCCs)
- Kein explizites Modellieren von Einfügungen/Löschungen
- Jeder Punkt wird mit mindestens einem Punkt der anderen Sequenz verglichen
- Es wird eine **Distanzmatrix** berechnet, um die optimale Pfad-Ähnlichkeit zu bestimmen

## DTW-Visualisierung

![DTW Beispiel](/assets/images/dynamic_time_warping.png)

## Python-Implementierung

```python
import numpy as np

def dtw(x: list, y: list, d) -> float:
    D = np.full((len(x) + 1, len(y) + 1), np.inf)
    D[0, 0] = 0

    for i in range(1, len(x)):
        for j in range(1, len(y)):
            cost = d(x[i], y[j])
            D[i, j] = cost + min(
                D[i-1, j],    # oben
                D[i, j-1],    # links
                D[i-1, j-1]   # diagonal
            )

    return D[len(x)-1, len(y)-1]
```

## Erklärung des Codes

- `x` und `y` sind zwei Zeitreihen (z. B. Listen von Zahlen oder Vektoren)
- `d(a, b)` ist eine Distanzfunktion, z. B. die **euklidische Distanz**
- Die Matrix `D` speichert die minimalen kumulativen Distanzen
- Der Rückgabewert ist die **optimale Pfaddistanz** zwischen den Sequenzen

## Anwendung

- **Spracherkennung**: Zwei gesprochene Wörter gleichen Typs vergleichen
- **Bewegungsanalyse**: Vergleich von Körperbewegungen über die Zeit
- **Finanzanalyse**: Ähnlichkeitsvergleich zwischen Aktienkursverläufen
- **Medizin**: Vergleich von Herzfrequenz- oder EEG-Signalen

## Beispielhafte Distanzfunktion

```python
def euclidean(a, b):
    return np.linalg.norm(np.array(a) - np.array(b))
```

## Wichtig

- DTW findet ein nicht-lineares Alignment zwischen zwei Sequenzen
- Besonders nützlich bei **verzögerten oder verzerrten** Abläufen
- Berechnung hat Komplexität \( O(n \cdot m) \) für Sequenzen der Länge \( n \) und \( m \)

