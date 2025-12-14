---
layout: page
title: Personenbezogene Daten in LLMs
permalink: /projekte/personenbezogene-daten-llms/
---

<div class="project-detail">
  <p class="pill">Privacy · AI</p>
  <h2>Personenbezogene Daten in LLMs</h2>

  <h3>PII-Redaktion (Demo)</h3>

  <div class="card" style="padding:1rem;">
    <label for="pii-input"><strong>Text eingeben:</strong></label>
    <textarea id="pii-input" rows="5" style="width:100%; margin-top:0.4rem; padding:0.75rem; border:1px solid var(--border); border-radius:12px; background:#f8f8f6;"></textarea>
    <button id="pii-run" class="primary-btn" style="margin-top:0.75rem;">Maskieren</button>
    <div id="pii-output" style="margin-top:1rem; white-space:pre-wrap; background:#f6f7f8; border:1px solid var(--border); border-radius:12px; padding:0.9rem;"></div>
    <div id="pii-counts" style="margin-top:0.6rem; color:var(--muted);"></div>
  </div>
</div>

<script>
  (function() {
    const EMAIL = /[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+/g;
    const ID = /(ID[-:]?\s?\d{3,}|TK-\d{3,}|\d{4}-LLM)/g;
    const NAME = /\b[A-Z][a-z]+\s[A-Z][a-z]+\b/g;

    const input = document.getElementById('pii-input');
    const runBtn = document.getElementById('pii-run');
    const output = document.getElementById('pii-output');
    const countsEl = document.getElementById('pii-counts');

    function mask(text) {
      const counts = { email: 0, id: 0, name: 0 };
      const maskedEmail = text.replace(EMAIL, () => { counts.email++; return '[EMAIL]'; });
      const maskedId = maskedEmail.replace(ID, () => { counts.id++; return '[ID]'; });
      const maskedName = maskedId.replace(NAME, () => { counts.name++; return '[NAME]'; });
      return { masked: maskedName, counts };
    }

    runBtn?.addEventListener('click', () => {
      const text = input.value || '';
      const result = mask(text);
      output.textContent = result.masked || 'Keine Eingabe erkannt.';
      countsEl.textContent = `Treffer – email: ${result.counts.email || 0}, id: ${result.counts.id || 0}, name: ${result.counts.name || 0}`;
    });
  })();
</script>
