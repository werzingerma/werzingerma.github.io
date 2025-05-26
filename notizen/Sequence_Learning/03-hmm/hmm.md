---
layout: page
title: Hidden Markov Models (HMM)
permalink: /notizen/Sequence_Learning/03-hmm/hmm
---

## Was ist ein HMM?

Ein Hidden Markov Model beschreibt einen Prozess, bei dem  
* **Zustände** zwar die Dynamik bestimmen, aber **verborgen** sind.  
* Wir sehen nur **Emissionen** (Messwerte, Symbole).  
* Die Zustandsfolge selbst ist eine Markov-Kette 1. Ordnung.

## Unterschied zu Markov-Ketten

**Markov-Kette:**  
![marcov-chain-hmm](/assets/images/markov_chain_example_HMM.png)

*Zustand = Wetter (Rain / Sun / Cloud). Wir sehen direkt, wo wir sind.*

**Hidden Markov Model:**  
![hmm](/assets/images/hidden_markov_model_hmm.png)

*Zustand = Jahreszeit (Winter / Spring / Summer / Fall) → **hidden***  
*Emission = Wetter (Rain / Sun / Cloud) → **sichtbar***

## Wie sieht ein HMM aus?

| Symbol | Bedeutung |
|--------|-----------|
| **π**  | Startverteilung: Wahrscheinlichkeit, in welchem Zustand wir beginnen |
| **A**  | Übergangsmatrix: aᵢⱼ = P(qₜ = sⱼ | qₜ₋₁ = sᵢ) |
| **B**  | Emissionsmatrix/-verteilung: bⱼ(o) = P(Oₜ = o | qₜ = sⱼ) |

## Wie funktioniert das?

1. **Generieren**: Zustand q₁ ∼ π → Emission O₁ ∼ B(q₁) → Übergang zu q₂ ∼ A(q₁,·) …  
2. **Aufgaben in der Praxis**  
   * *Bewerten* P(O | λ) → Forward/Backward  
   * *Dekodieren* q* → Viterbi  
   * *Parameter lernen* λ → Baum-Welch (EM)

## Wozu benutzt man HMMs?

* **Spracherkennung** (Phoneme / Wörter)  
* **Bioinformatik** (Gene vs. Nicht-Gene)  
* **Gesten-, Aktivitäts-, Musik-Analyse**  
* Allgemein: sequentielle, verrauschte Daten beliebiger Länge

---

➡ Siehe die beiden praktischen Beispiele in  
* [Verkehrsampel](hmm_example1.md)  
* [Wetter + Jahreszeiten](hmm_example2.md)
