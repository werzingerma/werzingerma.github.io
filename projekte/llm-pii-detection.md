---
layout: page
title: PII Detection for LLMs
permalink: /projekte/llm-pii-detection/
---

<div class="project-detail">
  <p class="pill">Master's Project · Privacy · AI</p>
  <h2>PII Detection for LLMs</h2>

  <p><strong>Detecting and masking personal data before sending it to LLMs.</strong></p>

  <p>
    <a href="https://github.com/werzingerma/llm-pii-detection" class="primary-btn" target="_blank">View on GitHub</a>
  </p>

  <h3>Overview</h3>
  <p>
    This project explores how to detect and mask personally identifiable information (PII) in text before it gets processed by Large Language Models. I compared different detection approaches and built a small pipeline that includes logging and access controls.
  </p>

  <h3>What I implemented</h3>
  <ul>
    <li>PII redaction using both regex patterns and Named Entity Recognition (NER)</li>
    <li>Comparison of regex vs. NER accuracy (including false positives/negatives)</li>
    <li>Audit logging with role-based access control</li>
    <li>Selective demasking for authorized users</li>
    <li>GDPR considerations</li>
  </ul>

  <h3>Built with</h3>
  <table>
    <tr><td><strong>Language</strong></td><td>Python</td></tr>
    <tr><td><strong>NER</strong></td><td>SpaCy</td></tr>
    <tr><td><strong>Local LLM</strong></td><td>Llama 3.2 (GGUF)</td></tr>
    <tr><td><strong>Analysis</strong></td><td>Jupyter Notebooks</td></tr>
  </table>

  <h3>Detection approaches</h3>
  <p>I tested two main methods:</p>
  <ul>
    <li><strong>Regex</strong> – Fast pattern matching for emails, phone numbers, IDs. Works well for structured data but misses context.</li>
    <li><strong>NER with SpaCy</strong> – Better at catching names, locations, organizations in natural text. Slower but more accurate for unstructured data.</li>
  </ul>

  <h3>Context</h3>
  <p>
    This was a university project looking at privacy concerns when using LLMs with sensitive data. The main question was: how can you use LLMs without accidentally leaking personal information?
  </p>
</div>
