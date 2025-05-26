---
layout: page
title: Beispiel 1 – Verkehrsampel
permalink: /notizen/Sequence_Learning/03-hmm/hmm_example1
---

## Idee

* **Verborgene Zustände**:  
  1 = Rot, 2 = Rot-Gelb, 3 = Grün, 4 = Gelb  
* **Emissionen**: tatsächliche Lampenfarbe (R, Y , G).  
  Leichtes Rauschen erlaubt: 95 % richtige Farbe, 5 % Verwechslung.

### Python-Demo

```python
from hmmlearn import hmm
import numpy as np

# Kodierung der Beobachtungen: 0=R, 1=Y, 2=G
obs = np.array([[0,0,1,2,2,1,0]]).T    # Beispielsequenz

model = hmm.MultinomialHMM(n_components=4, n_iter=20, tol=1e-3,
                           init_params="ste")   # nur Baum-Welch lernen
model.startprob_ = np.array([1,0,0,0])          # beginnt sicher bei Rot
model.transmat_  = np.array([
    [.0,1.0,0.0,0.0],   # Rot -> Rot-Gelb
    [.0,0.0,1.0,0.0],   # Rot-Gelb -> Grün
    [.0,0.0,0.0,1.0],   # Grün -> Gelb
    [1.0,0.0,0.0,0.0],  # Gelb -> Rot
])
model.emissionprob_ = 0.05*np.ones((4,3))
model.emissionprob_[0,0] = .95  # Rot-Lampe leuchtet meist bei Zustand 1 …
model.emissionprob_[1,1] = .95
model.emissionprob_[2,2] = .95
model.emissionprob_[3,1] = .95  # Gelb zeigt Gelb-Licht

logprob, states = model.decode(obs, algorithm="viterbi")
print("Zustandsfolge:", states)
```

*`states`* liefert z. B. `[0 0 1 2 2 3 0]` → damit erkennt Viterbi den Ampel‑Zyklus  
(Rot → Rot‑Gelb → Grün → Gelb → Rot) trotz kleiner Beobachtungs‑Fehler.  
So kann man aus einer verrauschten Farbserie das exakte Ampelschema rekonstruieren,
z. B. fürs autonome Fahren oder für eine Simulation.
