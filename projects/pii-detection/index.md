---
layout: page
title: pii-detection
permalink: /projects/pii-detection/
---

# pii-detection

detect and mask personal data before it hits an LLM.

university project from "Datenschutz in KI-Systemen" at TH Nürnberg.

## the problem

LLMs see data they shouldn't – names, emails, addresses end up in prompts and get sent to API providers.

## pipeline

```
┌──────────┐     ┌───────────────┐     ┌──────────────┐     ┌─────────┐
│  input   │ ──▶ │  regex +      │ ──▶ │   masked     │ ──▶ │   LLM   │
│  (text)  │     │  spacy NER    │     │   output     │     │         │
└──────────┘     └───────────────┘     └──────────────┘     └─────────┘
```

## code

```python
import re
import spacy

nlp = spacy.load("de_core_news_lg")

# regex for structured data
PATTERNS = {
    'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
    'iban': r'DE\d{2}\s?\d{4}\s?\d{4}\s?\d{4}\s?\d{4}\s?\d{2}',
    'phone': r'\b0\d{2,4}[\s/-]?\d{3,}[\s/-]?\d{2,}\b',
}

def detect_pii(text):
    found = []

    # regex-based detection
    for pii_type, pattern in PATTERNS.items():
        for match in re.finditer(pattern, text):
            found.append({
                'type': pii_type,
                'text': match.group(),
                'start': match.start(),
                'end': match.end(),
                'method': 'regex'
            })

    # NER for names, locations, organizations
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
    # replace from end to start (indices stay stable)
    for item in sorted(pii_items, key=lambda x: x['start'], reverse=True):
        text = text[:item['start']] + f"[{item['type']}]" + text[item['end']:]
    return text
```

## results

| entity type | precision | recall | notes |
|-------------|-----------|--------|-------|
| email | 98% | 99% | regex works great |
| IBAN | 94% | 91% | sometimes confused with invoice numbers |
| phone | 89% | 85% | german formats are chaotic |
| names (PER) | 76% | 68% | spacy struggles with german names |

## what was hard

- **german names:** spacy doesn't reliably detect "Müller" or "Özdemir". custom name list helps but is never complete.

- **context:** "Angela Merkel" shouldn't be masked (public figure), "Angela Schmidt" should. not solved yet.

- **false positives:** "Müller GmbH" is not a person's name. "Am Bahnhof 5" is not an address that needs masking.

## what i'd do differently

- start with real (anonymized) test data earlier
- spend more time on evaluation
- maybe try a small LLM for NER instead of spacy

---

[→ repo](https://github.com/werzingerma/llm-pii-detection)
