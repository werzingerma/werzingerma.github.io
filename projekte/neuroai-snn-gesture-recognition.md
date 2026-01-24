---
layout: page
title: snn gesture recognition
permalink: /projekte/neuroai-snn-gesture-recognition/
---

# snn gesture recognition

Handgesten erkennen mit Event-Kamera und Spiking Neural Network.

Projekt aus dem NeuroAI-Kurs, baut auf meiner Arbeit mit DVS-Kameras auf.

## warum event-kamera?

Normale Kamera: 30 fps, jedes Frame komplett, viel redundante Daten.

Event-Kamera (DVS): Nur Änderungen, μs-Auflösung, viel weniger Daten.

```
RGB-Kamera:         Event-Kamera:
┌─────────────┐     ╔═════════════╗
│ ░░░░░░░░░░░ │     ║     *       ║
│ ░░░░█░░░░░░ │     ║    * *      ║
│ ░░░░█░░░░░░ │     ║   *   *     ║
│ ░░░██░░░░░░ │     ║  *     *    ║
│ ░░░░░░░░░░░ │     ║             ║
└─────────────┘     ╚═════════════╝
 Ganzes Bild        Nur Bewegung
 (redundant)        (sparse)
```

Für schnelle Bewegungen (Gesten) ideal: keine Motion-Blur, geringe Latenz.

## daten-preprocessing

Der nervigste Teil: Event-Streams in was umwandeln das ein SNN versteht.

```python
import numpy as np
from tonic import transforms

def events_to_frames(events, dt_ms=50, resolution=(128, 128)):
    """
    Events zu Frame-Repräsentation.
    Akkumuliert Events über dt_ms Zeitfenster.

    TODO: Adaptives dt basierend auf Event-Rate wäre besser
    """
    frames = []
    t_start = events['t'].min()
    t_end = events['t'].max()

    for t in range(t_start, t_end, dt_ms * 1000):  # μs
        mask = (events['t'] >= t) & (events['t'] < t + dt_ms * 1000)
        frame = np.zeros(resolution)

        # Polarity berücksichtigen (ON/OFF events)
        for e in events[mask]:
            frame[e['y'], e['x']] += e['p']  # +1 oder -1

        frames.append(frame)

    return np.array(frames)

# Oder mit Tonic (einfacher)
transform = transforms.ToFrame(
    sensor_size=(128, 128, 2),
    time_window=50000  # 50ms in μs
)
```

## netzwerk

Spiking CNN mit snnTorch:

```
Input (128x128 x T timesteps)
    ↓
SpikingConv2d (32 Filter, 3x3) + LIF
    ↓
MaxPool (2x2)
    ↓
SpikingConv2d (64 Filter, 3x3) + LIF
    ↓
MaxPool (2x2)
    ↓
Flatten + SpikingLinear (256) + LIF
    ↓
Output (11 Gesten)
```

LIF = Leaky Integrate-and-Fire Neuron

```python
import snntorch as snn
import torch.nn as nn

class GestureSNN(nn.Module):
    def __init__(self, num_classes=11):
        super().__init__()
        self.conv1 = nn.Conv2d(2, 32, 3, padding=1)
        self.lif1 = snn.Leaky(beta=0.9)

        self.conv2 = nn.Conv2d(32, 64, 3, padding=1)
        self.lif2 = snn.Leaky(beta=0.9)

        self.fc = nn.Linear(64 * 32 * 32, 256)
        self.lif3 = snn.Leaky(beta=0.9)

        self.out = nn.Linear(256, num_classes)
        self.lif_out = snn.Leaky(beta=0.9)
```

## ergebnisse

| Geste | Accuracy | Anmerkung |
|-------|----------|-----------|
| Swipe Left | 94% | |
| Swipe Right | 91% | |
| Swipe Up | 90% | |
| Swipe Down | 88% | |
| Wave | 87% | Verwechslung mit Swipe |
| Clap | 85% | |
| Circle CW | 72% | Schwierig |
| Circle CCW | 70% | Schwierig |

**Gesamt: ~86% Accuracy**

## was die accuracy drückt

- Circle vs. Wave ist manchmal mehrdeutig
- Verschiedene Personen = verschiedene Geschwindigkeiten
- Beleuchtung beeinflusst Event-Rate

## was ich gelernt hab

1. **SNN-Training ist anders:** Kein normales Backprop, Surrogate Gradients sind tricky. `snnTorch` macht das einfacher.

2. **Events ≠ Frames:** Die Repräsentation macht viel aus. Hab 3 verschiedene ausprobiert (ToFrame, ToVoxelGrid, ToTimeSurface).

3. **Hyperparameter:** LIF-Neuron Parameter (beta/tau, threshold) sind wichtiger als bei normalen NNs.

## nächste schritte

- [ ] Mehr Training-Daten für Circle-Gesten
- [ ] Online-Learning statt nur Batch
- [ ] Auf echter Hardware testen (z.B. Intel Loihi)

## verbindung zu meiner thesis

Dieses Projekt war Vorarbeit für meine Master-Thesis, wo ich DVS-Kameras für Stroke-Assessment einsetze. Ähnliche Pipeline, aber andere Bewegungen (NIHSS-Tests statt Gesten).

## tech

snnTorch, Tonic, PyTorch, NumPy, Matplotlib

---

[→ GitHub](https://github.com/werzingerma/neuroai-snn-gesture-recognition)
