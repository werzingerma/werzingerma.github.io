---
layout: page
title: Projects
permalink: /projekte/
---

<main class="terminal">
  <h1>Projekte</h1>

  <div class="terminal-window">
    <div class="terminal-header">
      <span class="terminal-prompt">$ ls ~/projects</span>
    </div>

    <div class="terminal-content">
      <!-- Uni -->
      <div class="directory">
        <span class="dir-header">drwxr-xr-x  uni/</span>
        <ul>
          <li>
            <span class="tree">├── </span>
            <a href="/projekte/neuroai-snn-gesture-recognition/">snn-gesture</a>
            <span class="comment"># gesture recognition mit SNNs</span>
            <span class="star">★</span>
          </li>
          <li>
            <span class="tree">├── </span>
            <a href="/projekte/llm-pii-detection/">pii-detection</a>
            <span class="comment"># PII maskieren vor LLM-Calls</span>
          </li>
          <li>
            <span class="tree">└── </span>
            <a href="/projekte/osws-scientific-report/">quarto-workflow</a>
            <span class="comment"># notebooks → papers</span>
          </li>
        </ul>
      </div>

      <!-- Side Projects -->
      <div class="directory">
        <span class="dir-header">drwxr-xr-x  side-projects/</span>
        <ul>
          <li>
            <span class="tree">├── </span>
            <a href="/projekte/insightify/">insightify</a>
            <span class="comment"># CLI für CSV-Exploration</span>
          </li>
          <li>
            <span class="tree">├── </span>
            <a href="/projekte/readmeo/">readmeo</a>
            <span class="comment"># GitHub README generator</span>
          </li>
          <li>
            <span class="tree">└── </span>
            <a href="/projekte/pocket-arcade/">pocket-arcade</a>
            <span class="comment"># retro games PWA</span>
          </li>
        </ul>
      </div>

    </div>
  </div>
</main>

<style>
/* Terminal Container */
.terminal {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem 1rem;
}

.terminal h1 {
  font-family: inherit;
  margin-bottom: 1.5rem;
}

/* Terminal Window */
.terminal-window {
  background: #0d1117;
  border: 1px solid #30363d;
  border-radius: 8px;
  overflow: hidden;
}

.terminal-header {
  background: #161b22;
  padding: 0.75rem 1rem;
  border-bottom: 1px solid #30363d;
}

.terminal-prompt {
  font-family: 'JetBrains Mono', 'Fira Code', 'SF Mono', Consolas, monospace;
  font-size: 0.9rem;
  color: #7ee787;
}

.terminal-prompt::after {
  content: '▋';
  animation: blink 1s step-end infinite;
  margin-left: 0.5rem;
}

@keyframes blink {
  50% { opacity: 0; }
}

.terminal-content {
  padding: 1rem 1.25rem;
  font-family: 'JetBrains Mono', 'Fira Code', 'SF Mono', Consolas, monospace;
  font-size: 0.85rem;
  line-height: 1.7;
}

/* Directories */
.directory {
  margin-bottom: 1.25rem;
}

.directory:last-child {
  margin-bottom: 0;
}

.dir-header {
  color: #8b949e;
  display: block;
  margin-bottom: 0.25rem;
}

.directory ul {
  list-style: none;
  margin: 0;
  padding: 0;
  padding-left: 1rem;
}

.directory li {
  display: flex;
  align-items: baseline;
  gap: 0;
  white-space: nowrap;
}

.directory li:hover {
  background: rgba(88, 166, 255, 0.1);
  margin-left: -0.5rem;
  padding-left: 0.5rem;
  margin-right: -0.5rem;
  padding-right: 0.5rem;
}

/* Tree Characters */
.tree {
  color: #484f58;
  user-select: none;
}

/* Links */
.terminal-content a {
  color: #58a6ff;
  text-decoration: none;
  min-width: 140px;
  display: inline-block;
}

.terminal-content a:hover {
  text-decoration: underline;
}

/* Comments */
.comment {
  color: #6e7681;
  margin-left: 0.5rem;
}

/* Special Markers */
.star {
  color: #f0c14b;
  margin-left: 0.5rem;
}

/* Mobile */
@media (max-width: 600px) {
  .terminal-content {
    font-size: 0.75rem;
    padding: 0.75rem 1rem;
  }

  .terminal-content a {
    min-width: 100px;
  }

  .comment {
    display: none;
  }
}
</style>
