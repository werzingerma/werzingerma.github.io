---
layout: page
title: Begriffserklärungen (zu HMMs)
permalink: /notizen/Sequence_Learning/03-hmm/hmm_terms
---

---

## Beobachtungsmodell

Das Beobachtungs‑ oder Emissionsmodell beschreibt, **welche Beobachtung (Symbol, Feature‑Vektor)** in welchem verborgenen Zustand mit welcher Wahrscheinlichkeit auftreten kann.  
Ohne ein passendes Beobachtungsmodell könnte das HMM die realen Messwerte nicht erklären.

**Mini‑Beispiel & Ergebnis**

```python
# Ausschnitt aus dem Ampel‑Beispiel
model.emissionprob_ = 0.05*np.ones((4,3))  # Grundrauschen 5 %
model.emissionprob_[0,0] = 0.95            # Zustand 'Rot' sendet fast immer R‑Licht
```

> Die Werte sagen: **95 %** der Zeit, wenn der Zustand *Rot* aktiv ist, sehen wir eine rote Lampe;  
> **5 %** sind Fehlmessungen. Genau diese weichen Beobachtungs‑Wahrscheinlichkeiten machen das HMM robuster.

---

## HMM‑Struktur
 
Mit **π, A, B** legt man Start‑, Übergangs‑ und Emissions­wahrscheinlich­keiten fest – das komplette, lern‑ und auswertbare Modell.

**Beispielcode**

```python
n = 3                         # 3 Zustände
model = hmm.MultinomialHMM(n_components=n, init_params="")
model.startprob_ = [0.7,0.2,0.1]  # π
model.transmat_  = [[.8,.2,0],
                    [.1,.8,.1],
                    [.1,.1,.8]]   # A
model.emissionprob_ = [[.6,.4],
                       [.3,.7],
                       [.9,.1]]   # B
```

> Damit ist das HMM vollständig definiert und kann sofort für Viterbi, Forward oder Training verwendet werden.

---

## Isolated Word Recognition

Aufgabe: **Einzelne** gesprochene Wörter einem Wörterbuch zuordnen (z. B. „yes“, „no“, „stop“).  
Dazu bekommt jedes Wort ein eigenes HMM; das Wort mit der höchsten Beobachtungs­wahrscheinlichkeit **P(O | λ)** gewinnt.

**Ablauf in Pseudocode**

```python
best_word, best_logp = None, -np.inf
for word, hmm_model in dictionary.items():
    logp = hmm_model.score(features)     # Forward‑Log‑Wahrscheinlichkeit
    if logp > best_logp:
        best_word, best_logp = word, logp
print("Erkanntes Wort:", best_word)
```

> Forward liefert eine Zahl für jedes Wort‑HMM; das Maximum entscheidet – fertig ist die Klassifikation.

---

## Forward‑ & Backward‑Algorithmen

*Forward* berechnet **P(O | λ)** vom Start nach vorn, *Backward* das Gleiche rückwärts.  
Beide zusammen sind Basis für **Baum‑Welch** und erlauben schnelle Wahrscheinlichkeitsschätzung *ohne* alle Pfad‑Kombinationen durchzugehen.

**Beispielcode & Ergebnis**

```python
logp = model.score(obs)        # interner Forward‑Algorithmus
print("Log‑Likelihood:", logp)
```

> Für die Wetter‑Sequenz ergibt sich z. B. `Log‑Likelihood: -12.47`, was bedeutet:  
> Die Beobachtung ist mit Wahrscheinlichkeit ≈ e^(−12.47) ≈ 3.8 × 10⁻⁶ unter diesem Modell entstanden.

---

## Viterbi‑Algorithmus

Gibt die **wahrscheinlichste Zustandsfolge q\*** zu einer Beobachtungsreihe zurück – ideal für Dekodierungs‑ oder Segmentierungsaufgaben.

**Beispielcode & Ergebnis**

```python
logp, states = model.decode(obs, algorithm="viterbi")
print(states)
```

> Ausgabe (Ampel): `[0 0 1 2 2 3 0]` – genau ein kompletter Ampelzyklus.  
> Damit hat Viterbi auf einen Blick die versteckte Logik rekonstruiert.

---

## Baum‑Welch‑Algorithmus (EM‑Training)

Unüberwachtes Lernen der Parameter **π, A, B**.  
Iteriert zwischen  
1. **E‑Schritt**: Erwartete Zustands‑ und Übergangshäufigkeiten via Forward/Backward,  
2. **M‑Schritt**: Aktualisieren der Parameter.

**Beispielcode**

```python
model = hmm.MultinomialHMM(n_components=4, n_iter=30)  # 'ste' = alle Parameter lernen
model.fit(obs)           # Baum‑Welch läuft automatisch
print(model.transmat_)   # gelerntes A
```

> Nach einigen Iterationen nähert sich `transmat_` einer Matrix, die die echten Saison‑Wechsel (Winter→Frühling→Sommer→Herbst) widerspiegelt – **ohne** dass die Jahreszeiten je als Label gegeben waren.
