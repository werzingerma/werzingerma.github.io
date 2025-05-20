---
layout: page
title: SQL1 - comparing sequences
permalink: /notizen/Sequence_Learning/sql1/
---

# comparing sequences

## 1  Hamming-Abstand
**Idee**  
Zwei gleich lange Zeichenketten werden Zeichen-für-Zeichen verglichen; jedes ungleiche Zeichen kostet 1.

```text
x = 101110
y = 100100
Unterschiede an Position 3 und 5
→ Hamming-Abstand = 2
```

> **Merken:** Funktioniert nur bei *gleich langen* Sequenzen – keine Lücken erlaubt.

---

## 2  Edit-/Levenshtein-Abstand
**Idee**  
Kleinste Anzahl von **Einfügen (I), Löschen (D), Ersetzen (R)**, um String A in String B zu verwandeln (jeder Schritt kostet 1).

```text
kitten   →  sitting
kitten → sitten   (R)
sitten → sittin   (R)
sittin → sitting  (I)
Distanz = 3
```

> **Merken:** Erlaubt unterschiedliche Längen – realistisch für Tippfehler & DNA-Mutationen.

---

## 3  Edit-Transcript / Alignment
**Idee**  
Beide Sequenzen untereinander legen, „–“ für Lücken. Ein Band aus **M**atch, **R**eplace, **I**nsert, **D**elete beschreibt den optimalen Weg.

```text
k i t t e n -
s i t t i n g
M R M M R M I
```

> **Merken:** Zeigt **welche** Operationen nötig sind, nicht nur wie viele.

---

## 4  Dynamische Programmierung (DP)
**Idee**  
Matrix D[i,j] füllen – jede Zelle ist  
* links + 1 (Insert)  
* oben + 1 (Delete)  
* diagonal + δ (0 = Match, 1 = Mismatch)

Beispiel: „ab“ → „ac“

|   | ε | a | c |
|---|---|---|---|
| **ε** | 0 | 1 | 2 |
| **a** | 1 | 0 | 1 |
| **b** | 2 | 1 | 2 |

Rechts-unten = 2 → Distanz 2.

> **Merken:** Zeit & Speicher O(m · n); Rückwärts-Pfeile liefern das Alignment.

---

## 5  Anpassbare Kosten
**Idee**  
Operationen können beliebige Preise haben (z. B. Tastatur-Distanz als Substitutionskosten).

```python
cost_subst = {
    ('g','h'): 0.5,   # Nachbartasten
    ('g','p'): 2.2    # weiter Abstand
}
gap_penalty = 2      # Einfügen / Löschen
```

> **Merken:** Richtige Kosten machen Ergebnisse praxisnäher (Bio-Scores, Autokorrektur).

---

## 6  Needleman-Wunsch-Algorithmus
**Idee**  
Biologisches Alignment – **Match-Belohnung**, **Mismatch- und Gap-Strafen**; DP **maximiert** den Gesamt-Score.

```text
Scores:  Match +2,  Mismatch −1,  Gap −2

A G C
A - C
Score = +2 −2 +2 = +2   → bestes Alignment
```

> **Merken:** Gleiches Raster wie Levenshtein, aber auf *Maximum* statt Minimum optimiert.

---

## 7  Damerau-Levenshtein
**Idee**  
Zählt zusätzlich **Vertauschungen benachbarter Zeichen** als eine Operation.

```text
"hte"  → "the"   (Vertauschung)  → Distanz = 1
```

> **Merken:** Fängt typische Vertipper ab („teh“ → „the“).

---

## 8  Dynamic Time Warping (DTW)
**Idee**  
Ein „elastisches Band“ passt zwei **Zeit-Kurven** aneinander; erlaubt lokale Streckung/Kompression.

```text
Kurven: [100,105,110,115]   vs.   [100,110,115]
DTW biegt die zweite, bis Punkte übereinanderliegen  
→ geringe Gesamtkosten
```

> **Merken:** Gleiche DP-Matrix-Idee, aber für kontinuierliche Daten (Audio, Gesten).

---

## 9  Typische Anwendungen

| Verfahren | Klassischer Einsatz |
|-----------|--------------------|
| Hamming | QR-/Barcode-Prüfung |
| Levenshtein | Rechtschreibkorrektur, Auto-Complete |
| Needleman-Wunsch | Protein-/DNA-Alignment |
| Tastatur-Kosten | „Smart Keyboard“-Fehlerkorrektur |
| Damerau | Schnelle Tippfehler-Erkennung |
| DTW | Sprach- und Gestenerkennung, DTMF-Decoder |

---

## 10  Lern-Roadmap

1. **Papier zuerst:** Male die DP-Matrix für „kitten/sitting“.  
2. **Code-Schritte:**  
   * `hamming(x,y)` in < 5 Zeilen  
   * `levenshtein_dp(x,y)` mit `numpy`  
   * Needleman-Wunsch mit variablen Gap-Strafen  
3. **Parameter spielen:** Gap-Strafe erhöhen/verringern und das Alignment beobachten.  
4. **Übertragen:** Gleiche Matrix-Logik auf Audio-Kurven → DTW.

> **Faustregel:** Kannst du die Matrix zeichnen, kannst du den Algorithmus programmieren. 🎯

