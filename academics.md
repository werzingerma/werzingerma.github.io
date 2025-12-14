---
layout: page
title: Academics
permalink: /academics/
papers:
# Example Entry
#  - title: Adaptive Analytics for Smart Mobility
#    description: Dynamische Nachfrageprognosen für urbane Mobilität mithilfe von Graph-Signalen.
#    link: https://example.com/paper/adaptive-analytics
---

<ul class="academics-list">
  {% for paper in page.papers %}
  <li class="academics-item">
    <a href="{{ paper.link }}" target="_blank" rel="noreferrer">{{ paper.title }}</a>
    <div class="meta">{{ paper.description }}</div>
  </li>
  {% endfor %}
</ul>
