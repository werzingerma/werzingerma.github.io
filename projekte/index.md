---
layout: page
title: Projects
permalink: /projekte/
university_projects:
  - title: PII Detection for LLMs
    tagline: "Detection and masking of personally identifiable information in LLM workflows."
    status: Completed
    focus: Privacy · AI
    link: /projekte/llm-pii-detection/
    logo: /assets/images/pii-detection_logo.png

  - title: Scientific Report Workflow with Quarto
    tagline: "Automated workflow for publishing scientific reports from Jupyter notebooks."
    status: Completed
    focus: Academic · Automation
    link: /projekte/osws-scientific-report/
    logo: /assets/images/scientific-report-workflow-with-quarto_logo.png

  - title: Gesture Recognition with SNNs
    tagline: "Spiking Neural Network for hand gesture recognition using event-based cameras."
    status: Completed
    focus: NeuroAI · Deep Learning
    link: /projekte/neuroai-snn-gesture-recognition/
    logo: /assets/images/gesture-recognition_logo.png

private_projects:
  - title: Insightify
    tagline: "CLI tool for dataset analysis with interactive web dashboard for data exploration and visualization."
    status: Completed
    focus: Data Science · Python
    link: /projekte/insightify/
    logo: /assets/images/insightify_logo.png

  - title: Readmeo
    tagline: "Local desktop app for creating GitHub profile READMEs with drag-and-drop interface."
    status: Completed
    focus: Desktop · Svelte · Tauri
    link: /projekte/readmeo/
    logo: /assets/images/readmeo_logo.png

  - title: Pocket Arcade
    tagline: "Collection of classic retro games as a mobile-optimized PWA with offline support."
    status: Completed
    focus: Web · PWA · Games
    link: /projekte/pocket-arcade/
    logo: /assets/images/pocket_arcade_logo.png
---

<h2 class="section-heading">University Projects</h2>
<p class="section-description">Projects completed during my Master's program in Computer Science.</p>

<div class="cards-grid">
  {% for project in page.university_projects %}
  <a class="card project-card" href="{{ project.link | relative_url }}">
    <header>
      <img class="project-logo" src="{{ project.logo | relative_url }}" alt="{{ project.title }} Logo">
      <div>
        <h3>{{ project.title }}</h3>
        <div class="meta">{{ project.tagline }}</div>
      </div>
    </header>
    <div class="meta">
      <span class="tag">{{ project.status }}</span>
      <span class="tag">{{ project.focus }}</span>
    </div>
  </a>
  {% endfor %}
</div>

<h2 class="section-heading" style="margin-top: 3rem;">Private Projects</h2>
<p class="section-description">Personal side projects built in my free time.</p>

<div class="cards-grid">
  {% for project in page.private_projects %}
  <a class="card project-card" href="{{ project.link | relative_url }}">
    <header>
      <img class="project-logo" src="{{ project.logo | relative_url }}" alt="{{ project.title }} Logo">
      <div>
        <h3>{{ project.title }}</h3>
        <div class="meta">{{ project.tagline }}</div>
      </div>
    </header>
    <div class="meta">
      <span class="tag">{{ project.status }}</span>
      <span class="tag">{{ project.focus }}</span>
    </div>
  </a>
  {% endfor %}
</div>
