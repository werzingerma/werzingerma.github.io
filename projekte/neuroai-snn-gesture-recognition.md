---
layout: page
title: snn gesture recognition
permalink: /projekte/neuroai-snn-gesture-recognition/
---

# snn gesture recognition

Spiking Neural Network für Handgesten-Erkennung mit Event-Kamera Daten.

Teil vom NeuroAI-Kurs.

## was sind SNNs

Spiking Neural Networks versuchen biologische Neuronen nachzuahmen. Statt kontinuierlicher Werte kommunizieren sie über diskrete Spikes. Passt gut zu Event-Kamera Daten, die auch temporal/sparse sind.

## dataset

IBM DVS Gesture Dataset:
- 1.341 Samples, 11 Gesten
- Aufgenommen mit Dynamic Vision Sensor (DVS)
- Event-basiert: nur Änderungen werden aufgezeichnet, keine Frames

## ansatz

- Convolutional SNN mit LIF (Leaky Integrate-and-Fire) Neuronen
- Preprocessing mit Tonic Library
- Training in Jupyter Notebooks

## ergebnis

~89% Accuracy auf Test Set

## was schwierig war

- SNN-Training funktioniert anders als normale NNs
- Event-Daten Preprocessing ist unintuitiv am Anfang
- Hyperparameter-Tuning dauert ewig

## tech

snnTorch, Tonic, PyTorch, NumPy, Matplotlib

---

[→ GitHub](https://github.com/werzingerma/neuroai-snn-gesture-recognition)
