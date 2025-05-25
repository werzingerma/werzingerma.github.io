# Beispiel 2 – Tweet‑Generator (Bi‑gram‑Markov‑Kette)

Hier wird eine Markov‑Kette aus den Tweets von Donald Trump gebaut, um neue, stilechte Sätze zu erzeugen.

```python
import random, re
from collections import Counter, defaultdict

# Tweets einlesen & in Tokens zerlegen
text   = open('trump_tweets.txt').read().lower()
tokens = re.findall(r"\w+|[^\w\s]", text)   # Worte & Satzzeichen

# Bi‑grams und Häufigkeiten zählen
bigrams = Counter(zip(tokens, tokens[1:]))

# Übergangsliste aufbauen: für jedes Wort alle möglichen Nachfolger
next_tok = defaultdict(list)
for (w1, w2), cnt in bigrams.items():
    next_tok[w1].extend([w2] * cnt)  # Häufigkeit = Gewicht im Sampling

def generate(seed='make', length=15):
    out = [seed]
    for _ in range(length):
        out.append(random.choice(next_tok[out[-1]]))
    return ' '.join(out)

print(generate())
```

**Warum ist das eine Markov‑Kette?**

* Zustand = aktuelles Wort.  
* Übergänge = beobachtete Wortpaare (Bi‑grams).  
* Die Wahrscheinlichkeit, welches Wort als nächstes kommt,
  hängt *nur* vom aktuellen Wort ab – genau die Markov‑Annahme.

**Sampling‑Mechanismus**

* `next_tok[w]` enthält jeden Nachfolger so oft, wie er im Korpus vorkam.
* `random.choice` wählt proportional zur Häufigkeit → häufige Paare
  sind wahrscheinlicher.  
* Das Ergebnis sind erstaunlich authentische, wenn auch leicht
  chaotische Sätze.
