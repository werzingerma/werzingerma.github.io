---
layout: page
title: pii detection
permalink: /projekte/llm-pii-detection/
---

# pii detection

Uni-Projekt: Personenbezogene Daten erkennen bevor sie an ein LLM gehen.

## problem

LLMs bekommen oft Texte mit Namen, Emails, Telefonnummern. Die sollten da nicht rein. Also: erkennen und maskieren.

## ansatz

Zwei Methoden verglichen:

- **Regex** – Schnell, gut für Emails/Telefonnummern/IBANs. Aber: versteht keinen Kontext.
- **NER (SpaCy)** – Erkennt Namen, Orte, Firmen im Fließtext. Langsamer, aber besser bei unstrukturierten Daten.

Am Ende: Kombination aus beiden.

## was ich gemacht hab

- Detection Pipeline mit Regex + NER
- Vergleich der Ansätze (False Positives/Negatives)
- Audit Logging (wer hat was wann angefragt)
- Demaskierung für berechtigte User
- GDPR-Überlegungen

## was ich gelernt hab

- SpaCy ist nicht perfekt für deutsche Namen
- Regex für strukturierte Daten, NER für Fließtext
- False Positives bei Namen nervig ("Herr Müller" vs. "Müller GmbH")

## tech

Python, SpaCy, Llama 3.2 (lokal), Jupyter

---

[→ GitHub](https://github.com/werzingerma/llm-pii-detection)
