---
layout: page
title: Sequence Learning - Comparing Sequences
permalink: /notizen/Sequence_Learning/01-comparing-sequences/hamming_distance
---

<script type="text/javascript" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script>

# Hamming-Distanz

## Was ist die Hamming-Distanz?

Die Hamming-Distanz zwischen zwei gleich langen Zeichenketten ist die Anzahl der Positionen, an denen sich die Zeichen unterscheiden.

**Formel:**
\[
\text{Hamming}(x, y) = \sum_{i=1}^{n} [x_i \neq y_i]
\]

## Voraussetzung

- Beide Strings müssen gleich lang sein.
- Es werden nur Substitutionen berücksichtigt – keine Einfügungen oder Löschungen.

## Beispiel 1

```python
x = "karolin"
y = "kathrin"
```

Vergleich:
```
k a r o l i n  
k a t h r i n  
    ↑ ↑ ↑    
```

Unterschiede an den Positionen 3, 4 und 5 →  
**Hamming-Distanz = 3**

## Beispiel 2

```python
x = "1011101"
y = "1001001"
```

Vergleich:
```
1 0 1 1 1 0 1  
1 0 0 1 0 0 1  
    ↑   ↑    
```

Unterschiede an den Positionen 2 und 4 →  
**Hamming-Distanz = 2**

## Python-Implementierung

```python
def hamming_distance(x: str, y: str) -> int:
    assert len(x) == len(y), "Strings must be of equal length"
    return sum(1 for a, b in zip(x, y) if a != b)
```

## Anwendung

- Bioinformatik: Vergleich von DNA-/RNA-Sequenzen gleicher Länge
- Telekommunikation: Fehlererkennung bei digitaler Datenübertragung
- Maschinelles Lernen: Vergleich binärer Vektoren oder Ähnlichkeitsmessung
- Klassifikation: z. B. bei Fingerabdruckmustern oder Bitstrings

## Wichtig

- Effizient berechenbar: Laufzeit in O(n)
- Nur sinnvoll bei gleich langen Sequenzen
- Für komplexere Fälle (z. B. mit Einfügungen oder Löschungen) ist die Edit-Distanz besser geeignet
