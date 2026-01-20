---
layout: page
title: Sequence Learning
permalink: /notizen/Sequence_Learning/
---

<div class="note-page">
  <p class="pill">University · Master · TH Nürnberg</p>

  <p>Notes from the Sequence Learning course at TH Nürnberg. Covers everything from basic sequence comparison to modern transformer architectures.</p>

  <h3>Course Content</h3>

  <h4>1. Comparing Sequences</h4>
  <p>How to measure similarity between sequences using different distance metrics and alignment algorithms.</p>
  <ul>
    <li><a href="01-comparing-sequences/hamming_distance">Hamming Distance</a></li>
    <li><a href="01-comparing-sequences/levenshtein_distance">Levenshtein Distance</a></li>
    <li><a href="01-comparing-sequences/needleman_wunsch">Needleman-Wunsch Algorithm</a></li>
    <li><a href="01-comparing-sequences/dynamic_time_warping">Dynamic Time Warping</a></li>
    <li><a href="01-comparing-sequences/cost_modelling">Cost Modeling</a></li>
  </ul>

  <h4>2. Markov Chains & N-Grams</h4>
  <p>Statistical models for sequences where the next state depends only on the current state.</p>
  <ul>
    <li><a href="02-markov-chains/markov-annahme">Markov Assumption</a></li>
    <li><a href="02-markov-chains/token_type">Token vs Type</a></li>
    <li><a href="02-markov-chains/wahrscheinlichkeit">Probability Estimation</a></li>
    <li><a href="02-markov-chains/zipf_smoothing">Zipf Distribution & Smoothing</a></li>
  </ul>

  <h4>3. Hidden Markov Models</h4>
  <p>Models where the underlying states are not directly observable, only their emissions.</p>
  <ul>
    <li><a href="03-hmm/beobachtungsmodell">Observation Model</a></li>
    <li><a href="03-hmm/forward_backward">Forward-Backward Algorithm</a></li>
    <li><a href="03-hmm/viterbi">Viterbi Decoding</a></li>
    <li><a href="03-hmm/baum_welch">Baum-Welch Training</a></li>
    <li><a href="03-hmm/isolated_word_recognition">Isolated Word Recognition</a></li>
  </ul>

  <h4>4. Neural Networks Basics</h4>
  <p>Fundamentals: feedforward networks, autoencoders, Word2Vec, FastText.</p>

  <h4>5. Convolutional Networks for Sequences</h4>
  <p>CNNs for sequence data, embeddings, HMM-DNN hybrids.</p>

  <h4>6. Recurrent Neural Networks</h4>
  <p>RNN, LSTM, GRU architectures for sequential processing.</p>

  <h4>7. Attention Mechanisms</h4>
  <p>How attention allows models to focus on relevant parts of the input.</p>

  <h4>8. Sequence-to-Sequence & CTC</h4>
  <p>Encoder-decoder architectures and Connectionist Temporal Classification.</p>

  <h4>9. RNN-Transducers</h4>
  <p>Streaming sequence-to-sequence models for ASR systems.</p>

  <h4>10. Transformers</h4>
  <p>Self-attention, BERT, GPT, Wav2Vec2.</p>

  <h4>11. Large Language Models</h4>
  <p>Pre-training, instruction fine-tuning, RLHF.</p>

  <h4>12. Reinforcement Learning</h4>
  <p>RL applications in sequence tasks.</p>

  <h3>Resources</h3>
  <ul>
    <li><a href="https://seqlrn.github.io/" target="_blank">Course Page</a></li>
    <li><a href="https://github.com/seqlrn/assignments" target="_blank">Assignments Repository</a></li>
    <li><a href="http://web.stanford.edu/~jurafsky/slp3/" target="_blank">Speech and Language Processing (Jurafsky)</a></li>
    <li><a href="http://www.deeplearningbook.org/" target="_blank">Deep Learning Book</a></li>
    <li><a href="http://colah.github.io/posts/2015-08-Understanding-LSTMs/" target="_blank">Understanding LSTMs</a></li>
    <li><a href="https://jalammar.github.io/illustrated-transformer/" target="_blank">The Illustrated Transformer</a></li>
  </ul>
</div>
