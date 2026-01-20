---
layout: page
title: Notes
permalink: /notizen/
---

<div class="notes-overview">
  <p>A collection of notes on topics I find interesting.</p>

  <h3>Topics</h3>
  <div class="notes-grid">
    <a href="/notizen/machine-learning/" class="note-card">
      <h4>Machine Learning</h4>
      <p>Neural networks, PyTorch, transformers, training tips</p>
    </a>
    <a href="/notizen/spiking-neural-networks/" class="note-card">
      <h4>Spiking Neural Networks</h4>
      <p>LIF neurons, event cameras, neuromorphic computing</p>
    </a>
    <a href="/notizen/data-visualization/" class="note-card">
      <h4>Data Visualization</h4>
      <p>Matplotlib, Seaborn, Plotly, chart design</p>
    </a>
    <a href="/notizen/git/" class="note-card">
      <h4>Git</h4>
      <p>Workflows, GitHub Actions, GitHub Pages</p>
    </a>
    <a href="/notizen/docker/" class="note-card">
      <h4>Docker</h4>
      <p>Containers, Dockerfile, Docker Compose</p>
    </a>
    <a href="/notizen/pwa-service-workers/" class="note-card">
      <h4>PWAs & Service Workers</h4>
      <p>Offline apps, caching strategies, manifest</p>
    </a>
    <a href="/notizen/tauri/" class="note-card">
      <h4>Tauri</h4>
      <p>Desktop apps with web frontend and Rust backend</p>
    </a>
    <a href="/notizen/rust/" class="note-card">
      <h4>Rust</h4>
      <p>Ownership, borrowing, error handling</p>
    </a>
    <a href="/notizen/quarto/" class="note-card">
      <h4>Quarto</h4>
      <p>Scientific publishing, citations, PDF/HTML output</p>
    </a>
    <a href="/notizen/streamlit/" class="note-card">
      <h4>Streamlit</h4>
      <p>Python dashboards, widgets, data apps</p>
    </a>
    <a href="/notizen/svelte/" class="note-card">
      <h4>Svelte</h4>
      <p>Reactive frontend, components, stores</p>
    </a>
  </div>

  <h3>University Notes</h3>
  <div class="notes-grid">
    <a href="/notizen/Sequence_Learning/" class="note-card">
      <h4>Sequence Learning</h4>
      <p>Sequence comparison, Markov chains, HMMs, Transformers</p>
    </a>
  </div>
</div>

<style>
.notes-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1rem;
  margin: 1.5rem 0;
}

.note-card {
  display: block;
  padding: 1.25rem;
  background: var(--card-bg, #f8f9fa);
  border-radius: 8px;
  text-decoration: none;
  color: inherit;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  border: 1px solid var(--border-color, #e9ecef);
}

.note-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.note-card h4 {
  margin: 0 0 0.5rem 0;
  color: var(--link-color, #4a90d9);
  font-size: 1.1rem;
}

.note-card p {
  margin: 0;
  font-size: 0.9rem;
  color: var(--text-muted, #6c757d);
}
</style>
