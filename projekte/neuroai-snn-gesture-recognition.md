---
layout: page
title: Gesture Recognition with SNNs
permalink: /projekte/neuroai-snn-gesture-recognition/
---

<div class="project-detail">
  <p class="pill">Master's Project · NeuroAI · Deep Learning</p>
  <h2>Gesture Recognition with Spiking Neural Networks</h2>

  <p><strong>Spiking Neural Network implementation for hand gesture recognition using event-based camera data.</strong></p>

  <p>
    <a href="https://github.com/werzingerma/neuroai-snn-gesture-recognition" class="primary-btn" target="_blank">View on GitHub</a>
  </p>

  <h3>Overview</h3>
  <p>
    This project implements a Spiking Neural Network (SNN) to recognize hand gestures from the IBM DVS Gesture Dataset. Unlike traditional frame-based cameras, event-based cameras capture movement data asynchronously, making SNNs particularly well-suited for processing this type of temporal information.
  </p>

  <h3>Key Results</h3>
  <ul>
    <li><strong>Test Accuracy</strong> – Approximately 89%</li>
    <li><strong>Dataset</strong> – 1,341 gesture samples</li>
    <li><strong>Classes</strong> – 11 different hand and arm gestures</li>
  </ul>

  <h3>Key Features</h3>
  <ul>
    <li><strong>Convolutional SNN Architecture</strong> – Uses Leaky Integrate-and-Fire (LIF) neurons</li>
    <li><strong>Event-based Processing</strong> – Efficiently handles temporal event data from DVS cameras</li>
    <li><strong>Dataset Analysis</strong> – Comprehensive exploration of the gesture dataset</li>
    <li><strong>Live Inference</strong> – Real-time gesture classification capabilities</li>
    <li><strong>Jupyter Notebooks</strong> – Interactive exploration and model training</li>
  </ul>

  <h3>Technology Stack</h3>
  <table>
    <tr><td><strong>SNN Framework</strong></td><td>snnTorch (built on PyTorch)</td></tr>
    <tr><td><strong>Event Data</strong></td><td>Tonic library</td></tr>
    <tr><td><strong>Deep Learning</strong></td><td>PyTorch</td></tr>
    <tr><td><strong>Analysis</strong></td><td>NumPy, Scikit-learn, Matplotlib</td></tr>
  </table>

  <h3>What are Spiking Neural Networks?</h3>
  <p>
    Spiking Neural Networks are a type of artificial neural network that more closely mimics biological neurons. Instead of continuous activation values, SNNs communicate through discrete spikes over time, making them particularly efficient for processing temporal and event-based data. This neuromorphic approach can lead to more energy-efficient implementations on specialized hardware.
  </p>

  <h3>IBM DVS Gesture Dataset</h3>
  <p>
    The dataset was captured using a Dynamic Vision Sensor (DVS), which records changes in light intensity asynchronously. This results in sparse, event-based data that naturally encodes motion information, making it ideal for gesture recognition tasks with SNNs.
  </p>
</div>
