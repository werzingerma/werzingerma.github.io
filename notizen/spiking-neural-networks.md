---
layout: page
title: Spiking Neural Networks
permalink: /notizen/spiking-neural-networks/
---

<p class="pill">Notes · NeuroAI · Neuromorphic</p>

SNNs are neural networks that communicate through discrete spikes over time, similar to biological neurons.

### Why SNNs?

Traditional neural networks process everything at once. SNNs process information over time through spikes. This makes them naturally suited for temporal data (like event cameras) and potentially very energy-efficient on specialized hardware.

### The Leaky Integrate-and-Fire (LIF) neuron

The simplest spiking neuron model. It accumulates input over time, "leaks" some of it, and fires a spike when it crosses a threshold.

```python
import snntorch as snn
import torch.nn as nn

class SpikingNet(nn.Module):
    def __init__(self):
        super().__init__()
        # beta = decay rate (how fast membrane potential leaks)
        self.fc1 = nn.Linear(784, 128)
        self.lif1 = snn.Leaky(beta=0.9)
        self.fc2 = nn.Linear(128, 10)
        self.lif2 = snn.Leaky(beta=0.9)

    def forward(self, x):
        mem1 = self.lif1.init_leaky()
        mem2 = self.lif2.init_leaky()
        spk_rec = []

        for step in range(x.size(0)):
            cur1 = self.fc1(x[step])
            spk1, mem1 = self.lif1(cur1, mem1)
            cur2 = self.fc2(spk1)
            spk2, mem2 = self.lif2(cur2, mem2)
            spk_rec.append(spk2)

        return torch.stack(spk_rec)
```

### LIF dynamics

The membrane potential follows:

`U[t+1] = beta * U[t] + I[t] - spike[t] * threshold`

- **beta** controls the leak (0.9 = slow leak, 0.5 = fast leak)
- **I[t]** is the input current at time t
- When U crosses the threshold, a spike is emitted and U resets

### Event cameras

DVS (Dynamic Vision Sensors) only record changes in light intensity, producing sparse event streams. Each event is a tuple: `(x, y, timestamp, polarity)`. Perfect input for SNNs.

```python
from tonic import datasets, transforms

transform = transforms.Compose([
    transforms.Denoise(filter_time=10000),
    transforms.ToFrame(sensor_size=(128, 128, 2), time_window=25000)
])

dataset = datasets.DVSGesture(
    save_to='./data',
    train=True,
    transform=transform
)
```

### Training SNNs

Spikes are binary (0 or 1), so gradients don't flow through them normally. Solution: surrogate gradients - pretend the spike function has a smooth gradient during backprop.

```python
# snnTorch handles this automatically
# Loss is usually computed on spike counts
loss = nn.CrossEntropyLoss()(spk_rec.sum(0), labels)
```

### Key parameters

| Parameter | Notes |
|-----------|-------|
| beta (decay) | 0.9 is a good start. Lower = faster response |
| threshold | Usually 1.0. Higher = fewer spikes |
| timesteps | More = better temporal resolution, slower training |

### Neuromorphic hardware

- **Intel Loihi** - Research chip, 128 cores
- **IBM TrueNorth** - 1 million neurons on a chip
- **BrainChip Akida** - Available commercially

### Resources

- [snnTorch Documentation](https://snntorch.readthedocs.io/)
- [Tonic](https://tonic.readthedocs.io/) - Event data preprocessing
- [Surrogate Gradient Learning in SNNs](https://arxiv.org/abs/1809.05793)
