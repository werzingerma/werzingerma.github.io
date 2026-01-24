---
layout: page
title: snn
permalink: /notes/snn/
---

# spiking neural networks

notes on SNNs, event cameras, neuromorphic computing.

my main focus in the master's – see also [snn-gesture project](/projects/snn-gesture/) and my thesis (STRAIVER).

last updated: january 2025

---

## why SNNs?

regular NNs: compute everything at once, floats everywhere.
SNNs: temporally distributed spikes, binary, energy efficient.

perfect for event cameras because the data is already temporal/sparse.

## LIF neuron (leaky integrate-and-fire)

the simplest model. membrane potential accumulates input, leaks over time, fires spike when threshold is reached.

```python
import snntorch as snn

# beta = how fast the potential leaks (0.9 = slow, 0.5 = fast)
lif = snn.Leaky(beta=0.9, threshold=1.0)

mem = lif.init_leaky()  # membrane potential to 0
for t in range(timesteps):
    spk, mem = lif(input[t], mem)
    # spk is 0 or 1
```

**my experience with beta:**
- `0.9` – good starting point
- too high (0.99) → neuron "remembers" too much, sluggish response
- too low (0.5) → neuron forgets too fast, needs constant input

## event camera data

DVS outputs events as `(x, y, t, polarity)`. needs to be converted to something the network can use.

```python
from tonic import datasets, transforms

# accumulate events to frames
transform = transforms.Compose([
    transforms.Denoise(filter_time=10000),  # remove noise
    transforms.ToFrame(
        sensor_size=(128, 128, 2),  # 2 = ON/OFF channels
        time_window=25000  # 25ms per frame
    )
])

dataset = datasets.DVSGesture(save_to='./data', transform=transform)
```

**heads up:** `time_window` is critical.
- too short → too few events per frame
- too long → motion blur effect

i usually use 20-50ms, depends on movement speed.

## training

spikes are binary → no gradient.
solution: surrogate gradients (pretend spike function is differentiable).

snnTorch handles this automatically, but good to know:

```python
# loss on spike counts
output_spikes = torch.stack(spk_rec)  # (timesteps, batch, classes)
loss = nn.CrossEntropyLoss()(output_spikes.sum(0), labels)

# alternative: loss on membrane potential at the end
# loss = nn.CrossEntropyLoss()(mem_rec[-1], labels)
```

spike count loss works better for me usually.

## hardware

- **Intel Loihi** – the "real" neuromorphic chip, hard to get access
- **BrainChip Akida** – commercially available
- **GPU with snnTorch** – fine for research/prototyping

haven't deployed on real hardware yet, only simulation.

## problems i've had

1. **too few spikes:** network learns "just never fire" → lower threshold or scale input
2. **too many spikes:** everything fires always → raise threshold or add regularization
3. **vanishing spikes:** in deep networks no spikes reach the end → residual connections help

---

## links

- [snnTorch tutorials](https://snntorch.readthedocs.io/en/latest/tutorials/index.html) – very good
- [Tonic](https://tonic.readthedocs.io/) – event data preprocessing
- [surrogate gradient paper](https://arxiv.org/abs/1901.09948)

---

related: [snn-gesture project](/projects/snn-gesture/)
