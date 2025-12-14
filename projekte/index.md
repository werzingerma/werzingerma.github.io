---
layout: page
title: Projekte
permalink: /projekte/
projects:
  - title: Personenbezogene Daten in LLMs
    tagline: "Beispielprojekt: sichere Verarbeitung sensibler Daten in generativen Modellen."
    status: Konzept
    focus: Privacy · AI
    link: /projekte/personenbezogene-daten-llms/
    logo: /assets/images/example-project-logo.jpg
---

<div class="cards-grid">
  {% for project in page.projects %}
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
