---
layout: page
title: Beispiel 2 – Wetter + Jahreszeiten
permalink: /notizen/Sequence_Learning/03-hmm/hmm_example2
---

## Idee

* **Verborgene Zustände**: Winter (W), Frühling (Sp), Sommer (S), Herbst (F)  
* **Emissionen**: Rain (Ra), Sun (Su), Cloud (Cl)

### Python-Demo

```python
from hmmlearn import hmm
import numpy as np

# 0=Rain, 1=Sun, 2=Cloud
obs = np.array([[0,0,1,1,2,0,1,1]]).T

model = hmm.MultinomialHMM(n_components=4, n_iter=50, tol=1e-3,
                           init_params="ste")         # nur B & π lernen
model.startprob_ = np.full(4, 0.25)                  # alle Jahreszeiten gleich wahrscheinlich
model.transmat_  = np.eye(4)*0.9 + 0.033             # meistens bleiben, selten Wechsel
model.emissionprob_ = np.array([                     # grobe Startschätzung
    [0.5,0.3,0.2],  # Winter
    [0.3,0.4,0.3],  # Spring
    [0.2,0.5,0.3],  # Summer
    [0.4,0.2,0.4],  # Fall
])

logprob, seasons = model.decode(obs, algorithm="viterbi")
print("wahrscheinlichste Saisonfolge:", seasons)
```

Angenommen, die Ausgabe lautet `[0 0 0 1 2 2 3 3]`.  
Das bedeutet sinngemäß:

* **Winter** bei den ersten drei Regentagen,  
* **Frühling**, sobald zweimal Sonne erscheint,  
* **Sommer** mit Sonne+Cloud,  
* **Herbst** am Ende (wieder bewölkt).

> Der Viterbi-Algorithmus wählt also die *wahrscheinlichste* Jahreszeitfolge,
> die zu den Wetterbeobachtungen passt – ein typisches HMM-Anwendungsszenario.
