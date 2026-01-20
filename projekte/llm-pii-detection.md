---
layout: page
title: PII Detection for LLMs
permalink: /projekte/llm-pii-detection/
---

<div class="project-detail">
  <p class="pill">Master's Project · Privacy · AI</p>
  <h2>PII Detection for LLMs</h2>

  <p><strong>Detection and masking of personally identifiable information (PII) in Large Language Model workflows.</strong></p>

  <p>
    <a href="https://github.com/werzingerma/llm-pii-detection" class="primary-btn" target="_blank">View on GitHub</a>
  </p>

  <h3>Overview</h3>
  <p>
    This project addresses the critical challenge of protecting sensitive personal data when using Large Language Models. It provides a complete pipeline for safeguarding PII in LLM workflows, combining detection mechanisms with governance controls including logging, access restrictions, and audit capabilities.
  </p>

  <h3>Key Features</h3>
  <ul>
    <li><strong>PII Redaction Module</strong> – Masks sensitive information using regex or NER approaches</li>
    <li><strong>Comparative Analysis</strong> – Benchmarks regex vs. neural network-based recognition</li>
    <li><strong>False Positive/Negative Analysis</strong> – Evaluates detection accuracy with edge cases</li>
    <li><strong>Audit Logging System</strong> – Role-based access control (RBAC) and data access tracking</li>
    <li><strong>Selective Demasking</strong> – Authorized personnel can retrieve masked information with audit trails</li>
    <li><strong>GDPR Compliance</strong> – Addresses European data protection regulations</li>
  </ul>

  <h3>Technology Stack</h3>
  <table>
    <tr><td><strong>Language</strong></td><td>Python</td></tr>
    <tr><td><strong>NER Framework</strong></td><td>SpaCy</td></tr>
    <tr><td><strong>Local LLMs</strong></td><td>GGUF format (Llama 3.2)</td></tr>
    <tr><td><strong>Analysis</strong></td><td>Jupyter Notebooks</td></tr>
    <tr><td><strong>Pattern Matching</strong></td><td>Regex</td></tr>
  </table>

  <h3>Detection Approaches</h3>
  <p>The project implements and compares two main approaches for PII detection:</p>
  <ul>
    <li><strong>Regex-based Detection</strong> – Fast pattern matching for structured PII like emails, phone numbers, and IDs</li>
    <li><strong>NER-based Detection</strong> – Neural network approach using SpaCy for context-aware entity recognition of names, locations, and organizations</li>
  </ul>

  <h3>Use Cases</h3>
  <ul>
    <li>Preprocessing data before sending to LLM APIs</li>
    <li>Building privacy-preserving AI applications</li>
    <li>GDPR-compliant data processing pipelines</li>
    <li>Enterprise LLM deployments with audit requirements</li>
  </ul>
</div>
