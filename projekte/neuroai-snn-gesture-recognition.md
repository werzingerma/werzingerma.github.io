---
layout: page
title: Gesture Recognition with SNNs
permalink: /projekte/neuroai-snn-gesture-recognition/
---

<div class="project-detail">
  <p class="pill">Master's Project · NeuroAI · Deep Learning</p>
  <h2>Gesture Recognition with Spiking Neural Networks</h2>

  <p><strong>Using SNNs to classify hand gestures from event camera data.</strong></p>

  <p>
    <a href="https://github.com/werzingerma/neuroai-snn-gesture-recognition" class="primary-btn" target="_blank">View on GitHub</a>
  </p>

  <h3>Overview</h3>
  <p>
    This project trains a Spiking Neural Network (SNN) to recognize hand gestures from the IBM DVS Gesture Dataset. The data comes from an event-based camera, which works differently from normal cameras - instead of frames, it records individual pixel changes asynchronously. SNNs are a good match for this kind of temporal data.
  </p>

  <h3>Results</h3>
  <ul>
    <li><strong>Accuracy</strong> – ~89% on test set</li>
    <li><strong>Dataset</strong> – 1,341 samples, 11 gesture classes</li>
  </ul>

  <h3>Implementation</h3>
  <ul>
    <li>Convolutional SNN with Leaky Integrate-and-Fire (LIF) neurons</li>
    <li>Event data preprocessing with the Tonic library</li>
    <li>Dataset exploration and analysis</li>
    <li>Training and evaluation in Jupyter notebooks</li>
  </ul>

  <h3>Built with</h3>
  <table>
    <tr><td><strong>SNN Framework</strong></td><td>snnTorch</td></tr>
    <tr><td><strong>Event Data</strong></td><td>Tonic</td></tr>
    <tr><td><strong>Deep Learning</strong></td><td>PyTorch</td></tr>
    <tr><td><strong>Analysis</strong></td><td>NumPy, Scikit-learn, Matplotlib</td></tr>
  </table>

  <h3>What are SNNs?</h3>
  <p>
    Spiking Neural Networks try to mimic how biological neurons work. Instead of continuous values, they communicate through discrete spikes over time. This makes them naturally suited for temporal data like event camera output. They can also be very energy-efficient on neuromorphic hardware.
  </p>

  <h3>About the dataset</h3>
  <p>
    The IBM DVS Gesture Dataset was recorded with a Dynamic Vision Sensor - a camera that only records changes in light intensity. This produces sparse, event-based data that encodes motion naturally. The dataset contains 11 different hand and arm gestures.
  </p>
</div>
