---
layout: page
title: readmeo
permalink: /projects/readmeo/
---

# readmeo

desktop app to build github profile READMEs.

drag & drop, live preview, runs locally.

## why

online generators were too limited or full of ads. wanted something that works offline.

## features

- block editor (header, about, stats, tech stack, etc.)
- live markdown preview
- export as `.md`
- dark theme

## known issues

- [ ] no undo/redo (annoys me too)
- [ ] settings don't persist between sessions
- [ ] preview sometimes lags

## tech

svelte 5 + tauri 2.

tauri because electron is too bloated for something this simple.

## download

[→ releases](https://github.com/werzingerma/readmeo/releases)

or build yourself:
```bash
npm install
npm run tauri build
```

---

[→ repo](https://github.com/werzingerma/readmeo) · [→ svelte notes](/notes/svelte/) · [→ tauri notes](/notes/tauri/)
