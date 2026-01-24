---
layout: page
title: pii detection
permalink: /projekte/llm-pii-detection/
---

# pii detection

Personenbezogene Daten erkennen und maskieren bevor sie an ein LLM gehen.

Entstanden im Kurs "Datenschutz in KI-Systemen" an der TH Nürnberg.

## problem

LLMs sehen oft Daten die sie nicht sehen sollten – Namen, E-Mails, Adressen landen im Prompt und damit beim API-Anbieter.

## pipeline

```
┌──────────┐     ┌───────────────┐     ┌──────────────┐     ┌─────────┐
│  Input   │ ──▶ │  Regex +      │ ──▶ │   Masked     │ ──▶ │  LLM    │
│  (Text)  │     │  SpaCy NER    │     │   Output     │     │         │
└──────────┘     └───────────────┘     └──────────────┘     └─────────┘
```

## code-beispiel

```python
import re
import spacy

nlp = spacy.load("de_core_news_lg")

# Regex für strukturierte Daten
PATTERNS = {
    'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
    'iban': r'DE\d{2}\s?\d{4}\s?\d{4}\s?\d{4}\s?\d{4}\s?\d{2}',
    'phone': r'\b0\d{2,4}[\s/-]?\d{3,}[\s/-]?\d{2,}\b',
}

def detect_pii(text):
    found = []

    # Regex-basierte Detection
    for pii_type, pattern in PATTERNS.items():
        for match in re.finditer(pattern, text):
            found.append({
                'type': pii_type,
                'text': match.group(),
                'start': match.start(),
                'end': match.end(),
                'method': 'regex'
            })

    # NER für Namen, Orte, Firmen
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ in ['PER', 'LOC', 'ORG']:
            found.append({
                'type': ent.label_,
                'text': ent.text,
                'start': ent.start_char,
                'end': ent.end_char,
                'method': 'ner'
            })

    return found

def mask_pii(text, pii_items):
    # Von hinten nach vorne ersetzen (Indizes bleiben stabil)
    for item in sorted(pii_items, key=lambda x: x['start'], reverse=True):
        text = text[:item['start']] + f"[{item['type']}]" + text[item['end']:]
    return text
```

## ergebnisse

| Entity-Typ | Precision | Recall | Anmerkung |
|------------|-----------|--------|-----------|
| E-Mail | 98% | 99% | Regex funktioniert super |
| IBAN | 94% | 91% | Manchmal Verwechslung mit Rechnungsnr. |
| Telefon | 89% | 85% | Deutsche Formate sind chaotisch |
| Namen (PER) | 76% | 68% | SpaCy struggelt mit deutschen Namen |

## was schwierig war

- **Deutsche Namen:** SpaCy erkennt "Müller" oder "Özdemir" nicht zuverlässig. Eigene Namensliste hilft, aber die ist nie vollständig.

- **Kontext:** "Angela Merkel" sollte nicht maskiert werden (öffentliche Person), "Angela Schmidt" schon. Das ist noch nicht gelöst.

- **False Positives:** "Müller GmbH" ist kein Personenname. "Am Bahnhof 5" ist keine Adresse die maskiert werden muss.

## was ich anders machen würde

- Früher mit echten (anonymisierten) Testdaten arbeiten
- Mehr Zeit in die Evaluation stecken
- Vielleicht ein kleineres LLM für NER statt SpaCy

## tech

Python, SpaCy, Llama 3.2 (lokal via Ollama), Jupyter

---

[→ GitHub](https://github.com/werzingerma/llm-pii-detection)
