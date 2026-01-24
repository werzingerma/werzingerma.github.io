---
layout: page
title: quarto workflow
permalink: /projekte/osws-scientific-report/
---

# quarto workflow

Jupyter Notebook schreiben → GitHub pushen → automatisch als PDF/HTML Paper.

Entstanden weil manuelles Exportieren nervt und ich LaTeX-Boilerplate hasse.

## wie es funktioniert

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Jupyter        │     │  GitHub         │     │  GitHub Pages   │
│  Notebook       │ ──▶ │  Actions        │ ──▶ │  (HTML/PDF)     │
│  (.ipynb)       │     │  + Quarto       │     │                 │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

## setup

`_quarto.yml`:

```yaml
project:
  type: manuscript

format:
  html:
    toc: true
    theme: cosmo
  pdf:
    documentclass: scrartcl
    papersize: a4

execute:
  echo: false    # Code nicht im Output zeigen
  warning: false

bibliography: references.bib
csl: apa.csl
```

GitHub Action (`.github/workflows/publish.yml`):

```yaml
name: Render and Deploy

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Quarto
        uses: quarto-dev/quarto-actions/setup@v2

      - name: Install TinyTeX
        run: quarto install tinytex

      - name: Render
        run: quarto render

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./_site
```

## citations

In `references.bib`:

```bibtex
@article{smith2023,
  author = {Smith, John and Doe, Jane},
  title = {A Study on Something},
  journal = {Journal of Examples},
  year = {2023},
  volume = {1},
  pages = {1-10}
}
```

Im Text: `@smith2023` oder `[@smith2023, p. 5]`

## wann es sinn macht

- Seminararbeiten, Projekt-Dokumentation
- Wenn Code und Text zusammengehören
- Reproduzierbare Analysen

## wann nicht

- Abschlussarbeiten (zu wenig LaTeX-Kontrolle)
- Papers für Journals (besser direkt deren Template)
- Alles wo man sehr spezifische Formatierung braucht

## limitationen

- Komplexe LaTeX-Sachen (Custom Packages, TikZ) gehen nicht immer
- BibLaTeX-Features fehlen
- Tabellen aus Pandas sehen manchmal komisch aus
- Debugging bei Render-Fehlern ist nervig

## tech

Quarto, Python, Jupyter, GitHub Actions, TinyTeX

---

[→ GitHub](https://github.com/werzingerma/osws-scientific-report)
