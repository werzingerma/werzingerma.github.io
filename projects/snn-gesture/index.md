---
layout: page
title: snn-gesture
permalink: /projects/snn-gesture/
---

# snn-gesture

hand gesture recognition with event cameras and spiking neural networks.

project from the neuroai course, builds on my work with DVS cameras.
related to my master's thesis (STRAIVER).

## why event cameras?

regular camera: 30 fps, full frames, lots of redundant data
event camera (DVS): only changes, μs resolution, sparse output

```
RGB Camera                    Event Camera (DVS)
┌─────────────────┐           ┌─────────────────┐
│ Frame 1  30fps  │           │ ·    ·          │
│ ┌─────────────┐ │           │   ·      ·      │
│ │  [hand]     │ │           │ ·   [movement]  │
│ │             │ │    vs     │      ·    ·     │
│ └─────────────┘ │           │   ·        ·    │
│ Full image      │           │ Only changes    │
│ every 33ms      │           │ μs resolution   │
└─────────────────┘           └─────────────────┘
```

for fast movements (gestures) this is ideal – no motion blur, much lower latency.

## data preprocessing

the annoying part: converting event streams into something an SNN can process.

```python
import tonic
from tonic import transforms

transform = transforms.Compose([
    transforms.Denoise(filter_time=10000),
    transforms.ToFrame(
        sensor_size=(128, 128, 2),  # 2 = ON/OFF channels
        time_window=25000  # 25ms per frame
    )
])

dataset = tonic.datasets.DVSGesture(
    save_to='./data',
    transform=transform
)
```

**heads up:** `time_window` is critical.
- too short → too few events per frame
- too long → motion blur effect

i usually use 20-50ms, depends on movement speed.

## network architecture

spiking CNN with snnTorch:

```
input (128x128)
    ↓
SpikingConv2d (32 filters) + LIF
    ↓
SpikingConv2d (64 filters) + LIF
    ↓
flatten + SpikingLinear (256)
    ↓
output (4 gestures)
```

```python
import snntorch as snn
from snntorch import surrogate

class SpikingCNN(nn.Module):
    def __init__(self):
        super().__init__()
        spike_grad = surrogate.fast_sigmoid()
        beta = 0.9

        self.conv1 = nn.Conv2d(2, 32, 3, padding=1)
        self.lif1 = snn.Leaky(beta=beta, spike_grad=spike_grad)

        self.conv2 = nn.Conv2d(32, 64, 3, padding=1)
        self.lif2 = snn.Leaky(beta=beta, spike_grad=spike_grad)

        self.fc = nn.Linear(64 * 32 * 32, 256)
        self.lif3 = snn.Leaky(beta=beta, spike_grad=spike_grad)

        self.out = nn.Linear(256, 4)
        self.lif_out = snn.Leaky(beta=beta, spike_grad=spike_grad)
```

## results

| gesture | accuracy | notes |
|---------|----------|-------|
| swipe left | 94% | |
| swipe right | 91% | |
| wave | 87% | confused with swipe |
| circle | 72% | hard to detect |

**overall accuracy:** ~86%

### what hurts accuracy

- circle vs wave is sometimes ambiguous
- different people = different speeds
- lighting affects event rate

## what i learned

1. **SNN training is different:** no normal backprop, surrogate gradients are tricky

2. **events ≠ frames:** representation matters a lot, tried 3 different approaches

3. **hyperparameters:** LIF neuron params (tau, threshold) matter more than in regular NNs

## problems i had

- **too few spikes:** network learns "just never fire" → lower threshold
- **exploding activity:** everything fires all the time → higher threshold or regularization
- **vanishing spikes in deep networks:** no spikes reach the output → residual connections help

## next steps (if i had time)

- [ ] more training data for circle and wave
- [ ] online learning instead of batch only
- [ ] test on actual neuromorphic hardware (Loihi, Akida)

## connection to STRAIVER

this project was prep work for my master's thesis (STRAIVER), where i use DVS cameras for stroke assessment. similar pipeline, different movements (NIHSS instead of gestures).

---

[→ repo](https://github.com/werzingerma/neuroai-snn-gesture-recognition) · [→ snn notes](/notes/snn/)
