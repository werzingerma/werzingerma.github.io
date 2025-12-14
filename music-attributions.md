---
layout: page
title: Musik-Credits
permalink: /music-attributions/
---

<div class="section-heading">
  <h2>Hintergrundmusik</h2>
  <p></p>
</div>

<div id="attribution-list"></div>

<script>
  const attributionFiles = [
    {%- assign credit_files = site.static_files 
      | where_exp: "file", "file.path contains 'assets/background-music'"
      | where_exp: "file", "file.extname != '.mp3'" -%}
    {%- for credit in credit_files -%}
    { name: "{{ credit.name | escape }}", path: "{{ credit.path | relative_url | uri_escape }}" }{% unless forloop.last %},{% endunless %}
    {%- endfor -%}
  ];

  async function loadAttributions() {
    const container = document.getElementById('attribution-list');
    if (!container) return;
    if (!attributionFiles.length) {
      container.innerHTML = '<p>Keine Attribution-Dateien gefunden.</p>';
      return;
    }

    for (const file of attributionFiles) {
      try {
        const res = await fetch(file.path);
        const text = await res.text();
        const item = document.createElement('div');
        item.style.padding = '0.8rem 0';
        item.style.borderBottom = '1px solid var(--border)';
        item.innerHTML = `
          <strong>${file.name}</strong>
          <pre style="white-space:pre-wrap; color: var(--muted); line-height:1.5; margin: 0.25rem 0 0;">${text}</pre>
        `;
        container.appendChild(item);
      } catch (err) {
        console.error('Fehler beim Laden', file.name, err);
      }
    }
  }

  loadAttributions();
</script>
