---
layout: page
title: sequence-learning
permalink: /notes/sequence-learning/
---

# sequence learning

lecture notes from the master's (TH Nürnberg, WS 24/25).

course page: [seqlrn.github.io](https://seqlrn.github.io/)

---

## topics covered

### 1. sequence comparison
- hamming distance – for equal length sequences
- levenshtein distance – edit distance (insert, delete, replace)
- needleman-wunsch – global alignment with dynamic programming
- dynamic time warping – for temporally distorted sequences

### 2. markov chains & n-grams
- markov assumption: P(next | history) = P(next | current)
- n-grams: word sequences of length N
- smoothing for zero probabilities (laplace, kneser-ney)

### 3. hidden markov models
- states not directly observable, only emissions
- forward-backward: compute probabilities
- viterbi: find best state sequence
- baum-welch: learn parameters (EM)

### 4. neural networks for sequences
- RNN, LSTM, GRU (mostly replaced by transformers now)
- CNNs for sequences (wavenet-style)

### 5. attention & transformers
- self-attention: each position attends to all others
- BERT (bidirectional), GPT (autoregressive)
- Wav2Vec for audio

### 6. sequence-to-sequence
- encoder-decoder architecture
- CTC loss for alignment-free training

### 7. LLMs
- pre-training on large text corpora
- fine-tuning, instruction tuning, RLHF

---

## what stuck

- **viterbi** is basically dynamic programming for HMMs – finds most likely path
- **attention** was the breakthrough – finally no fixed sequence length
- **CTC** is clever for ASR – alignment is learned, not given

---

## resources

- [speech and language processing (jurafsky)](http://web.stanford.edu/~jurafsky/slp3/) – the standard reference
- [the illustrated transformer](https://jalammar.github.io/illustrated-transformer/)
- [understanding LSTMs (colah)](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- [attention is all you need (paper)](https://arxiv.org/abs/1706.03762)

---

detailed notes on individual topics are in my uni files, this is just the overview.
