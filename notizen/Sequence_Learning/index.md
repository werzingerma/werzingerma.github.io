---
layout: page
title: Sequence Learning
permalink: /notizen/Sequence_Learning/
---

# Sequence Learning

Aus dem Master an der TH Nürnberg. Von klassischen Algorithmen bis Transformers.

Stand: Sommer 2024

---

## Themen

### Sequenzen vergleichen
- Hamming Distance, Levenshtein Distance
- Needleman-Wunsch (globales Alignment)
- Dynamic Time Warping

### Statistische Modelle
- Markov Chains, N-Grams
- Hidden Markov Models (Forward-Backward, Viterbi, Baum-Welch)

### Neural Networks für Sequenzen
- RNNs, LSTMs, GRUs
- CNNs für Sequenzdaten
- Attention Mechanismen

### Sequence-to-Sequence
- Encoder-Decoder Architekturen
- CTC (Connectionist Temporal Classification)
- RNN-Transducers

### Transformers & LLMs
- Self-Attention
- BERT, GPT
- Pre-training, Fine-tuning, RLHF

---

## Was hängengeblieben ist

- **Viterbi** ist quasi Dynamic Programming für HMMs – findet den wahrscheinlichsten Pfad
- **Attention** war der Durchbruch – endlich keine feste Sequenzlänge mehr
- **CTC** ist clever für ASR – Alignment wird gelernt, nicht vorgegeben

## Gute Ressourcen

- [Kurs-Seite](https://seqlrn.github.io/)
- [Speech and Language Processing](http://web.stanford.edu/~jurafsky/slp3/) – Jurafsky & Martin
- [Understanding LSTMs](http://colah.github.io/posts/2015-08-Understanding-LSTMs/) – Colah
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) – Jay Alammar
