---
layout: page
title: Spiking Neural Networks
permalink: /notizen/spiking-neural-networks/
---

# Spiking Neural Networks

Notizen zu SNNs, Event-Kameras, neuromorphic Computing.

Mein Hauptthema im Master – siehe auch [SNN Gesture Recognition](/projekte/neuroai-snn-gesture-recognition/) und meine Thesis.

Stand: Januar 2025

---

## Warum SNNs?

Normale NNs: Alles auf einmal berechnen, floats überall.
SNNs: Zeitlich verteilte Spikes, binär, energieeffizient.

Für Event-Kameras perfekt weil die Daten schon zeitlich/sparse sind.

## LIF Neuron (Leaky Integrate-and-Fire)

Das simpelste Modell. Membranpotential akkumuliert Input, leakt über Zeit, feuert Spike wenn Threshold erreicht.

```python
import snntorch as snn

# beta = wie schnell leakt das Potential (0.9 = langsam, 0.5 = schnell)
lif = snn.Leaky(beta=0.9, threshold=1.0)

mem = lif.init_leaky()  # Membranpotential auf 0
for t in range(timesteps):
    spk, mem = lif(input[t], mem)
    # spk ist 0 oder 1
```

**Meine Erfahrung mit beta:**
- `0.9` – guter Startpunkt
- Zu hoch (0.99) → Neuron "merkt sich" zu viel, reagiert träge
- Zu niedrig (0.5) → Neuron vergisst zu schnell, braucht konstanten Input

## Event-Kamera Daten

DVS gibt Events als `(x, y, t, polarity)`. Muss in was umgewandelt werden das ins Netzwerk passt.

```python
from tonic import datasets, transforms

# Events zu Frames akkumulieren
transform = transforms.Compose([
    transforms.Denoise(filter_time=10000),  # Rauschen raus
    transforms.ToFrame(
        sensor_size=(128, 128, 2),  # 2 = ON/OFF channels
        time_window=25000  # 25ms pro Frame
    )
])

dataset = datasets.DVSGesture(save_to='./data', transform=transform)
```

**Achtung:** `time_window` ist kritisch.
- Zu kurz → zu wenig Events pro Frame
- Zu lang → Motion Blur Effekt

Ich nehm meistens 20-50ms, hängt von der Bewegungsgeschwindigkeit ab.

## Training

Spikes sind binär → kein Gradient. Lösung: Surrogate Gradients (tun so als wäre die Spike-Funktion differenzierbar).

snnTorch macht das automatisch, aber gut zu wissen:

```python
# Loss auf Spike-Counts
output_spikes = torch.stack(spk_rec)  # (timesteps, batch, classes)
loss = nn.CrossEntropyLoss()(output_spikes.sum(0), labels)

# Alternativ: Loss auf Membrane Potential am Ende
# loss = nn.CrossEntropyLoss()(mem_rec[-1], labels)
```

Spike-Count-Loss funktioniert bei mir meistens besser.

## Hardware

- **Intel Loihi** – der "echte" neuromorphe Chip, schwer ranzukommen
- **BrainChip Akida** – kommerziell verfügbar
- **GPU mit snnTorch** – für Forschung/Prototyping reicht das

Hab noch nicht auf echter Hardware deployed, nur simuliert.

## Probleme die ich hatte

1. **Zu wenig Spikes:** Netzwerk lernt "einfach nie feuern" → Threshold runter oder Input skalieren
2. **Zu viele Spikes:** Alles feuert immer → Threshold hoch oder Regularisierung
3. **Vanishing Spikes:** In tiefen Netzen kommen hinten keine Spikes an → Residual Connections helfen

---

## Links

- [snnTorch Tutorials](https://snntorch.readthedocs.io/en/latest/tutorials/index.html) – sehr gut
- [Tonic](https://tonic.readthedocs.io/) – Event-Daten preprocessing
- [Surrogate Gradient Paper](https://arxiv.org/abs/1901.09948)

---

Verwandt: [Gesture Recognition Projekt](/projekte/neuroai-snn-gesture-recognition/)
