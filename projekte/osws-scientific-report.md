---
layout: page
title: quarto workflow
permalink: /projekte/osws-scientific-report/
---

# quarto workflow

Automatisierte Pipeline: Jupyter Notebook → Quarto → PDF/HTML Paper

## warum

Notebook schreiben, manuell exportieren, Formatierung anpassen, nochmal exportieren... Nervig. Also hab ich das automatisiert.

## pipeline

1. Notebook schreiben (Code + Text zusammen)
2. Referenzen via BibTeX / Zotero
3. Push zu GitHub
4. GitHub Actions rendert alles automatisch
5. Output landet auf GitHub Pages

## was geht

- Output: HTML, PDF, LaTeX, Word
- Journal-Templates (Springer, Elsevier, Nature, Lancet)
- Citations mit verschiedenen Styles
- Automatisches Deployment

## limitationen

- Komplexes LaTeX geht manchmal nicht
- Bibliographie-Support ist basic
- Tables können nervig sein

## tech

Quarto, Python, Jupyter, GitHub Actions, TinyTeX

---

[→ GitHub](https://github.com/werzingerma/osws-scientific-report)
