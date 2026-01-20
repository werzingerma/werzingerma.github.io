---
layout: page
title: Scientific Report Workflow with Quarto
permalink: /projekte/osws-scientific-report/
---

<div class="project-detail">
  <p class="pill">Master's Project · Academic · Automation</p>
  <h2>Scientific Report Workflow with Quarto</h2>

  <p><strong>Automating the conversion of Jupyter notebooks into formatted scientific papers.</strong></p>

  <p>
    <a href="https://github.com/werzingerma/osws-scientific-report" class="primary-btn" target="_blank">View on GitHub</a>
  </p>

  <h3>Overview</h3>
  <p>
    Writing scientific papers usually means dealing with formatting headaches - different journals want different styles, citations need to be formatted correctly, and converting between formats is tedious. This project sets up an automated workflow where you write your content in Jupyter notebooks, and GitHub Actions handles the rest.
  </p>

  <h3>What it does</h3>
  <ul>
    <li>Converts notebooks to HTML, PDF, LaTeX, and Word</li>
    <li>Pre-configured templates for different journals (Springer, Elsevier, Nature, Lancet)</li>
    <li>Citation management with BibTeX and different citation styles</li>
    <li>Zotero integration for references</li>
    <li>Automatic deployment to GitHub Pages</li>
    <li>Generates downloadable files in all formats</li>
  </ul>

  <h3>Built with</h3>
  <table>
    <tr><td><strong>Publishing</strong></td><td>Quarto</td></tr>
    <tr><td><strong>Analysis</strong></td><td>Python, Jupyter</td></tr>
    <tr><td><strong>CI/CD</strong></td><td>GitHub Actions</td></tr>
    <tr><td><strong>PDF</strong></td><td>TinyTeX</td></tr>
  </table>

  <h3>How it works</h3>
  <ol>
    <li>Write your content in Jupyter notebooks</li>
    <li>Add references via BibTeX or Zotero</li>
    <li>Push to GitHub</li>
    <li>GitHub Actions renders everything automatically</li>
    <li>Results get published to GitHub Pages</li>
  </ol>

  <h3>Context</h3>
  <p>
    This came out of frustration with the typical academic writing workflow. I wanted to write in notebooks (so code and text are together) and have the formatting happen automatically. Quarto turned out to be a good fit for this.
  </p>
</div>
