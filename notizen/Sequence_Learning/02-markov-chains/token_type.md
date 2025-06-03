---
layout: page
title: Token vs. Type
permalink: /notizen/Sequence_Learning/02-markov-chains/token_type
---

## Definition

* **Token**: Jedes einzelne Auftreten eines Wortes im Text.
* **Type**: Einzigartige Wörter (Wortformen) im Text.

> Beispiel: Im Satz "der Hund bellt, der Hund rennt" gibt es 6 Tokens, aber nur 4 Types: der, Hund, bellt, rennt.

## Warum ist der Unterschied wichtig?

* **Token-Zahl** spiegelt die Textlänge wider.
* **Type-Zahl** misst den Wortschatzumfang.

Das **Type-Token-Verhältnis (TTR)** wird oft zur Analyse von Stil und Komplexität verwendet:
$TTR = \frac{\text{Anzahl der Types}}{\text{Anzahl der Tokens}}$

## Code-Beispiel

```python
text = "der Hund bellt der Hund rennt"
tokens = text.split()
types = set(tokens)

print("Tokens:", len(tokens))
print("Types:", len(types))
print("TTR:", len(types)/len(tokens))
```

## Anwendung

* Autorenstil analysieren
* Sprachniveau bestimmen
* Duplicate Detection
* Textklassifikation
