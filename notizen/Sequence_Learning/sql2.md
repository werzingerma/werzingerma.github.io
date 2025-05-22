---
layout: page
title: Sequence Learning - Markov Chains and n-grams
permalink: /notizen/Sequence_Learning/sql2/
---

# Markov Chains and n-grams

## Markov-Ketten

**Was ist das?**  
Ein Modell für Reihenfolgen (z. B. Wörter), bei dem das nächste Element **nur vom aktuellen Zustand** abhängt, nicht von der ganzen Vorgeschichte.

**Wozu?**  
Zum Vorhersagen von nächsten Wörtern, Tönen, Bewegungen, Zuständen – überall, wo Dinge in Reihenfolge passieren.

**Beispiel (1. Ordnung):**  
Wenn in vielen Texten nach „great“ das Wort „again“ folgt, dann lernt das Modell:
```
p(again | great) = C(great again) / C(great)
```
→ Je häufiger „great again“ vorkommt, desto wahrscheinlicher wird „again“ vorhergesagt.

## N-Gramme

**Was ist das?**  
Eine Methode, Text in Wortfolgen der Länge N zu zerlegen:
- **Unigramm:** 1 Wort → „America“
- **Bigramm:** 2 Wörter → „Make America“
- **Trigramm:** 3 Wörter → „Make America great“

**Wozu?**  
Zum Erstellen von **Sprachmodellen**, die Texte verstehen, vervollständigen oder generieren können.

**Wie lernen N-Gramme?**  
Beim **Training** zählt man einfach, wie oft bestimmte Wortfolgen vorkommen.

Beispieltext:
```
"Make America great again. Make America strong again."
```

→ Häufigkeiten:
- bigram("Make America") = 2  
- bigram("America great") = 1  
- bigram("great again") = 1  
- bigram("strong again") = 1  

→ Daraus:
- p(again | great) = 1 / 1 = 1  
- p(again | strong) = 1 / 1 = 1  
- p(great | America) = 1 / 2 = 0.5  
- p(strong | America) = 1 / 2 = 0.5

→ Das Modell speichert diese Wahrscheinlichkeiten.

## Beispiel: Textgenerierung mit N-Grammen

Starte mit: **„Make America“**

→ Modell schaut auf den letzten Teil („America“) und sucht:
- Was kam nach „America“? → „great“ (50 %) oder „strong“ (50 %)

→ Nächstes Wort zufällig, je nach Wahrscheinlichkeit.

→ Dann folgt nach „great“ → „again“ (100 %)

→ **Satz:** „Make America great again“

## Smoothing

**Problem:**  
Was tun, wenn ein Wortpaar oder Dreier nie im Training vorkam?  
→ z. B. „Make America rich“ kam nie vor → Wahrscheinlichkeit = 0

**Lösung: Glättung**  
→ Verhindert, dass unbekannte Kombinationen eine 0 bekommen.

### Beispiel: Laplace-Smoothing (add-one)

Angenommen, im Training kam vor:
- bigram("America great") = 1  
- bigram("America rich") = 0  

**Ohne Smoothing:**
- p(great | America) = 1 / 1 = 1  
- p(rich | America) = 0 / 1 = 0 ← schlecht

**Mit Smoothing (Vokabulargröße = 4):**
- p(great | America) = (1 + 1) / (1 + 4) = 2 / 5 = 0.4  
- p(rich | America) = (0 + 1) / (1 + 4) = 1 / 5 = 0.2  

→ Bessere Verteilung, keine Null-Wahrscheinlichkeiten!

## Wie wird ein Markov- oder N-Gramm-Modell trainiert?

1. **Großen Textkorpus sammeln**  
   z. B. alle Trump-Tweets, Zeitungstexte, Bücher…

2. **Tokenisieren:**  
   Text wird in Wörter zerlegt.

3. **N-Gramme zählen:**  
   Für jede Wortfolge (z. B. bigram, trigram) wird gezählt, wie oft sie vorkommt.

4. **Wahrscheinlichkeiten berechnen:**  
   z. B.  
   ```
   p(w3 | w1 w2) = count(w1 w2 w3) / count(w1 w2)
   ```

5. **Optional: Glättung anwenden**, um unbekannte Wortfolgen sinnvoll zu behandeln.

→ So „lernt“ das Modell aus Erfahrung, was wahrscheinlich ist – wie ein Statistik-basiertes Bauchgefühl.