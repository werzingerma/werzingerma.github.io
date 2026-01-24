---
layout: page
title: readmeo
permalink: /projekte/readmeo/
---

# readmeo

Desktop-App für GitHub Profile READMEs.

Drag & Drop, Preview, Export. Kein Account, läuft lokal.

## features

- Block-Editor mit vorgefertigten Sektionen (About, Tech Stack, Stats)
- Live Markdown Preview
- Eigene Markdown-Blöcke wenn nötig
- Dark Mode

## known issues

- Kein Undo/Redo (muss ich noch machen)
- Dark Mode Setting speichert nicht zwischen Sessions
- Manchmal buggy wenn man Blöcke schnell hin und her zieht

## warum Tauri

Wollte Tauri mal ausprobieren statt Electron. App ist viel kleiner (~15MB vs ~150MB) und fühlt sich schneller an. Hab dabei auch Svelte gelernt.

## tech

Svelte 5, TypeScript, Tauri 2, Vite

---

[→ GitHub](https://github.com/werzingerma/readmeo)
