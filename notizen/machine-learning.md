---
layout: page
title: Machine Learning
permalink: /notizen/machine-learning/
---

<p class="pill">Notes · ML · Deep Learning</p>

Notes on neural networks, training techniques, and architectures.

### The basics

A neural network is a function that maps inputs to outputs through layers of learned transformations. Each layer does: `output = activation(weights @ input + bias)`. Training adjusts the weights to minimize a loss function using gradient descent.

### Simple neural network in PyTorch

```python
import torch
import torch.nn as nn

class SimpleNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, output_size)
        )

    def forward(self, x):
        return self.layers(x)

# Training loop
model = SimpleNet(784, 128, 10)
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
loss_fn = nn.CrossEntropyLoss()

for epoch in range(epochs):
    for batch_x, batch_y in dataloader:
        optimizer.zero_grad()
        pred = model(batch_x)
        loss = loss_fn(pred, batch_y)
        loss.backward()
        optimizer.step()
```

### Activation functions

| Function | Use case |
|----------|----------|
| ReLU | Default for hidden layers |
| Sigmoid | Binary classification output (0-1) |
| Softmax | Multi-class output (sum to 1) |
| Tanh | Sometimes better for RNNs |
| GELU | Transformers, smoother than ReLU |

### Common architectures

| Architecture | Use case |
|-------------|----------|
| MLP | Fully connected layers, tabular data |
| CNN | Convolutional layers, images, spatial data |
| RNN/LSTM | Sequential data (mostly replaced by transformers) |
| Transformer | Attention-based, state of the art for everything |

### Transformers - the key insight

The attention mechanism lets the model look at all positions in the input and decide which ones matter for each output:

```python
# Scaled dot-product attention
def attention(Q, K, V):
    d_k = Q.size(-1)
    scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(d_k)
    weights = F.softmax(scores, dim=-1)
    return torch.matmul(weights, V)
```

### Training tips

- Start with a small model and overfit on a tiny dataset first
- Learning rate is the most important hyperparameter - try 3e-4
- Batch normalization or layer normalization usually helps
- Data augmentation is often more effective than a bigger model
- If loss is NaN, learning rate is probably too high

### Resources

- [3Blue1Brown - Neural Networks](https://www.youtube.com/watch?v=aircAruvnKk) - Best visual explanation
- [Karpathy's Training Recipe](https://karpathy.github.io/2019/04/25/recipe/)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [Karpathy - Let's build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY)
