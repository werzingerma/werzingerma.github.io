---
layout: page
title: Scientific Report Workflow with Quarto
permalink: /projekte/osws-scientific-report/
---

<div class="project-detail">
  <p class="pill">Master's Project · Academic · Automation</p>
  <h2>Scientific Report Workflow with Quarto</h2>

  <p><strong>An automated workflow system for publishing scientific reports that converts Jupyter notebooks into multiple output formats.</strong></p>

  <p>
    <a href="https://github.com/werzingerma/osws-scientific-report" class="primary-btn" target="_blank">View on GitHub</a>
  </p>

  <h3>Overview</h3>
  <p>
    This workflow streamlines academic publication by eliminating manual document formatting. Users create Jupyter notebooks with research content, push to GitHub, and GitHub Actions automatically renders outputs in journal-specific formats and publishes them to a website—removing tedious conversion and deployment steps from scientific writing processes.
  </p>

  <h3>Key Features</h3>
  <ul>
    <li><strong>Multi-format Output</strong> – Automatic conversion to HTML, PDF, LaTeX, and Word</li>
    <li><strong>Journal Profiles</strong> – Pre-configured templates for Springer, Elsevier, Nature, and Lancet</li>
    <li><strong>Citation Management</strong> – BibTeX support with multiple CSL citation styles</li>
    <li><strong>Zotero Integration</strong> – Seamless reference handling from Zotero libraries</li>
    <li><strong>Custom Theme</strong> – Responsive design for web output</li>
    <li><strong>Downloadable Outputs</strong> – Automatic generation of PDF, Word, and LaTeX archives</li>
    <li><strong>Automated Deployment</strong> – Continuous publishing via GitHub Pages</li>
  </ul>

  <h3>Technology Stack</h3>
  <table>
    <tr><td><strong>Publishing</strong></td><td>Quarto</td></tr>
    <tr><td><strong>Analysis</strong></td><td>Python, Jupyter</td></tr>
    <tr><td><strong>CI/CD</strong></td><td>GitHub Actions</td></tr>
    <tr><td><strong>PDF/LaTeX</strong></td><td>TinyTeX</td></tr>
  </table>

  <h3>Workflow</h3>
  <ol>
    <li>Write research content in Jupyter notebooks</li>
    <li>Add references using BibTeX or Zotero</li>
    <li>Push changes to GitHub repository</li>
    <li>GitHub Actions automatically renders all output formats</li>
    <li>Results are published to GitHub Pages</li>
  </ol>

  <h3>Use Cases</h3>
  <ul>
    <li>Academic paper preparation with reproducible research</li>
    <li>Multi-journal submission workflows</li>
    <li>Research documentation and sharing</li>
    <li>Collaborative scientific writing projects</li>
  </ul>
</div>
