---
layout: page
title: Machine Learning
permalink: /notizen/machine-learning/
---

# Machine Learning

PyTorch-Snippets und Notizen die ich regelmäßig brauche.

Stand: Januar 2025

---

## Training Loop (meine Standard-Vorlage)

```python
model = MyModel()
optimizer = torch.optim.AdamW(model.parameters(), lr=3e-4)  # AdamW > Adam
loss_fn = nn.CrossEntropyLoss()

for epoch in range(epochs):
    model.train()
    for batch in train_loader:
        optimizer.zero_grad()
        loss = loss_fn(model(batch.x), batch.y)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)  # hilft bei Transformers
        optimizer.step()

    # Validation
    model.eval()
    with torch.no_grad():
        val_loss = ...
```

## Aktivierungsfunktionen

| Funktion | Wann |
|----------|------|
| ReLU | Default, außer bei Transformers |
| GELU | Transformers (smoother) |
| Sigmoid | Binary Output (0-1) |
| Softmax | Multi-Class Output |

Tanh brauch ich eigentlich nie mehr.

## Hyperparameter die ich immer zuerst probiere

- **Learning Rate:** `3e-4` (Adam/AdamW)
- **Batch Size:** So groß wie in GPU passt
- **Optimizer:** AdamW mit weight_decay=0.01

Wenn Loss NaN → LR zu hoch.

## Attention (für mich selbst)

```python
# Immer wieder vergessen wie die Dimensionen gehen
def attention(Q, K, V):
    # Q, K, V: (batch, seq_len, d_model)
    d_k = Q.size(-1)
    scores = Q @ K.transpose(-2, -1) / math.sqrt(d_k)
    weights = F.softmax(scores, dim=-1)
    return weights @ V
```

## Debugging-Tipps

1. **Erstmal auf Mini-Dataset overfitten** – wenn das nicht klappt, stimmt was am Code nicht
2. **Shapes printen** – `print(x.shape)` ist dein Freund
3. **Gradient-Check:** Sind die Gradienten 0? Dann fließt nix.

```python
for name, param in model.named_parameters():
    if param.grad is not None:
        print(f"{name}: {param.grad.abs().mean():.6f}")
```

---

## TODO

- [ ] Mixed Precision Training Notizen
- [ ] LoRA/QLoRA für Fine-Tuning

---

## Links

- [Karpathy's Training Recipe](https://karpathy.github.io/2019/04/25/recipe/) – Pflichtlektüre
- [Let's build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY) – bestes Transformer-Tutorial
- [PyTorch Docs](https://pytorch.org/docs/)
