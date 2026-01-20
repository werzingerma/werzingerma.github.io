---
layout: page
title: Readmeo
permalink: /projekte/readmeo/
---

<div class="project-detail">
  <p class="pill">Desktop · Svelte · Tauri</p>
  <h2>Readmeo</h2>

  <p><strong>A local desktop application for creating GitHub profile READMEs through a visual drag-and-drop interface.</strong></p>

  <p>
    <a href="https://github.com/werzingerma/readmeo" class="primary-btn" target="_blank">View on GitHub</a>
  </p>

  <h3>Overview</h3>
  <p>
    Readmeo simplifies the process of building README files for GitHub profiles. Users can arrange pre-built content blocks, customize them, preview the output in real-time, and export the final markdown—all without needing server accounts or cloud services. The application emphasizes local-first functionality, keeping all processing on the user's machine for maximum privacy.
  </p>

  <h3>Key Features</h3>
  <ul>
    <li><strong>Drag-and-Drop Editor</strong> – Intuitive block-based interface for arranging content</li>
    <li><strong>Live Preview</strong> – Real-time markdown rendering as you build</li>
    <li><strong>Pre-built Blocks</strong> – Ready-to-use sections for Header, About, Tech Stack, GitHub Stats, Social Links, and Projects</li>
    <li><strong>Custom Blocks</strong> – Support for custom markdown content</li>
    <li><strong>Export Options</strong> – Copy to clipboard or save as file</li>
    <li><strong>Dark Theme</strong> – Built-in dark mode support</li>
    <li><strong>Privacy-First</strong> – All processing happens locally, no cloud services required</li>
  </ul>

  <h3>Technology Stack</h3>
  <table>
    <tr><td><strong>Frontend</strong></td><td>Svelte 5, TypeScript</td></tr>
    <tr><td><strong>Desktop Framework</strong></td><td>Tauri 2</td></tr>
    <tr><td><strong>Build Tool</strong></td><td>Vite</td></tr>
    <tr><td><strong>Styling</strong></td><td>CSS</td></tr>
  </table>

  <h3>Why Tauri?</h3>
  <p>
    Tauri provides a lightweight alternative to Electron, resulting in smaller bundle sizes and better performance. Combined with Svelte's reactive approach, Readmeo delivers a snappy, native-feeling experience while maintaining cross-platform compatibility.
  </p>

  <h3>License</h3>
  <p>MIT License</p>
</div>
