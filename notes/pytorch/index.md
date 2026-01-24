---
layout: page
title: pytorch
permalink: /notes/pytorch/
---

# pytorch

snippets and notes i regularly need for training models.

last updated: january 2025

---

## training loop (my standard template)

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
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)  # helps with transformers
        optimizer.step()

    # validation
    model.eval()
    with torch.no_grad():
        val_loss = ...
```

## activation functions

| function | when |
|----------|------|
| ReLU | default, except transformers |
| GELU | transformers (smoother) |
| Sigmoid | binary output (0-1) |
| Softmax | multi-class output |

don't think i've used tanh in years.

## hyperparameters i try first

- **learning rate:** `3e-4` (Adam/AdamW)
- **batch size:** as big as fits in GPU
- **optimizer:** AdamW with weight_decay=0.01

if loss is NaN → lr too high.

## attention (note to self)

```python
# always forget the dimensions
def attention(Q, K, V):
    # Q, K, V: (batch, seq_len, d_model)
    d_k = Q.size(-1)
    scores = Q @ K.transpose(-2, -1) / math.sqrt(d_k)
    weights = F.softmax(scores, dim=-1)
    return weights @ V
```

## debugging tips

1. **overfit on tiny dataset first** – if that doesn't work, something's wrong with the code
2. **print shapes** – `print(x.shape)` is your friend
3. **gradient check:** are gradients 0? then nothing's flowing.

```python
for name, param in model.named_parameters():
    if param.grad is not None:
        print(f"{name}: {param.grad.abs().mean():.6f}")
```

---

## TODO

- [ ] mixed precision training notes
- [ ] LoRA/QLoRA for fine-tuning

---

## links

- [karpathy's training recipe](https://karpathy.github.io/2019/04/25/recipe/) – required reading
- [let's build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY) – best transformer tutorial
- [pytorch docs](https://pytorch.org/docs/)
