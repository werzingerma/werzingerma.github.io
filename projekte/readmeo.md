---
layout: page
title: Readmeo
permalink: /projekte/readmeo/
---

<div class="project-detail">
  <p class="pill">Desktop · Svelte · Tauri</p>
  <h2>Readmeo</h2>

  <p><strong>A desktop app for building GitHub profile READMEs with drag-and-drop.</strong></p>

  <p>
    <a href="https://github.com/werzingerma/readmeo" class="primary-btn" target="_blank">View on GitHub</a>
  </p>

  <h3>Overview</h3>
  <p>
    Readmeo is a small desktop app that helps you create a README for your GitHub profile. You drag around pre-made blocks (like "About Me", "Tech Stack", "GitHub Stats"), customize them, and export the markdown. Everything runs locally on your machine.
  </p>

  <h3>Features</h3>
  <ul>
    <li>Drag-and-drop editor for arranging content blocks</li>
    <li>Live preview of the markdown output</li>
    <li>Pre-built blocks for common sections (Header, About, Tech Stack, Stats, etc.)</li>
    <li>Custom markdown blocks if you need something specific</li>
    <li>Copy to clipboard or save as file</li>
    <li>Dark mode</li>
  </ul>

  <h3>Built with</h3>
  <table>
    <tr><td><strong>Frontend</strong></td><td>Svelte 5, TypeScript</td></tr>
    <tr><td><strong>Desktop</strong></td><td>Tauri 2</td></tr>
    <tr><td><strong>Build</strong></td><td>Vite</td></tr>
  </table>

  <h3>Why Tauri?</h3>
  <p>
    I wanted to try out Tauri as an alternative to Electron. The resulting app is much smaller and feels snappier. Plus I got to learn Svelte along the way.
  </p>
</div>
