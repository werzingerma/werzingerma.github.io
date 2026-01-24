---
layout: page
title: Notes
permalink: /notes/
---

<main class="terminal">
  <h1>Notes</h1>

  <div class="terminal-window">
    <div class="terminal-header">
      <span class="terminal-prompt">$ ls ~/notes</span>
    </div>

    <div class="terminal-content">
      <!-- Languages -->
      <div class="directory">
        <span class="dir-header">drwxr-xr-x  languages/</span>
        <ul>
          <li>
            <span class="tree">└── </span>
            <a href="/notes/rust/">rust</a>
            <span class="comment"># <span class="wip">[wip]</span> ownership, borrowing</span>
          </li>
        </ul>
      </div>

      <!-- Frameworks -->
      <div class="directory">
        <span class="dir-header">drwxr-xr-x  frameworks/</span>
        <ul>
          <li>
            <span class="tree">├── </span>
            <a href="/notes/pytorch/">pytorch</a>
            <span class="comment"># training, models</span>
          </li>
          <li>
            <span class="tree">├── </span>
            <a href="/notes/svelte/">svelte</a>
            <span class="comment"># reactive frontend</span>
          </li>
          <li>
            <span class="tree">└── </span>
            <a href="/notes/tauri/">tauri</a>
            <span class="comment"># rust + webview desktop</span>
          </li>
        </ul>
      </div>

      <!-- Tools -->
      <div class="directory">
        <span class="dir-header">drwxr-xr-x  tools/</span>
        <ul>
          <li>
            <span class="tree">├── </span>
            <a href="/notes/git/">git</a>
            <span class="comment"># version control</span>
          </li>
          <li>
            <span class="tree">├── </span>
            <a href="/notes/docker/">docker</a>
            <span class="comment"># containers</span>
          </li>
          <li>
            <span class="tree">├── </span>
            <a href="/notes/quarto/">quarto</a>
            <span class="comment"># notebooks → papers</span>
          </li>
          <li>
            <span class="tree">└── </span>
            <a href="/notes/streamlit/">streamlit</a>
            <span class="comment"># python dashboards</span>
          </li>
        </ul>
      </div>

      <!-- Topics -->
      <div class="directory">
        <span class="dir-header">drwxr-xr-x  topics/</span>
        <ul>
          <li>
            <span class="tree">├── </span>
            <a href="/notes/snn/">snn</a>
            <span class="comment"># neuromorphic computing</span>
            <span class="star">★</span>
          </li>
          <li>
            <span class="tree">├── </span>
            <a href="/notes/data-viz/">data-viz</a>
            <span class="comment"># matplotlib, plotly</span>
          </li>
          <li>
            <span class="tree">└── </span>
            <a href="/notes/pwa/">pwa</a>
            <span class="comment"># offline web apps</span>
          </li>
        </ul>
      </div>

      <!-- University -->
      <div class="directory">
        <span class="dir-header">drwxr-xr-x  university/</span>
        <ul>
          <li>
            <span class="tree">└── </span>
            <a href="/notes/sequence-learning/">sequence-learning</a>
            <span class="comment"># master ws24/25</span>
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

/* Terminal Window - Nord Theme */
.terminal-window {
  background: #2e3440;
  border: 1px solid #4c566a;
  border-radius: 8px;
  overflow: hidden;
}

.terminal-header {
  background: #3b4252;
  padding: 0.75rem 1rem;
  border-bottom: 1px solid #4c566a;
}

.terminal-prompt {
  font-family: 'JetBrains Mono', 'Fira Code', 'SF Mono', Consolas, monospace;
  font-size: 0.9rem;
  color: #a3be8c;
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
  color: #d8dee9;
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
  background: rgba(136, 192, 208, 0.1);
  margin-left: -0.5rem;
  padding-left: 0.5rem;
  margin-right: -0.5rem;
  padding-right: 0.5rem;
}

/* Tree Characters */
.tree {
  color: #4c566a;
  user-select: none;
}

/* Links */
.terminal-content a {
  color: #88c0d0;
  text-decoration: none;
  min-width: 140px;
  display: inline-block;
}

.terminal-content a:hover {
  color: #8fbcbb;
  text-decoration: underline;
}

/* Comments */
.comment {
  color: #616e88;
  margin-left: 0.5rem;
}

/* Special Markers */
.star {
  color: #ebcb8b;
  margin-left: 0.5rem;
}

.wip {
  color: #bf616a;
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
