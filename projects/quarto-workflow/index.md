---
layout: page
title: quarto-workflow
permalink: /projects/quarto-workflow/
---

# quarto-workflow

write jupyter notebook → push to github → get pdf/html paper automatically.

built this because manual exports suck and latex boilerplate is tedious.

university project from "Open Science & Wiss. Schreiben" at TH Nürnberg.

## how it works

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  jupyter        │     │  github         │     │  github pages   │
│  notebook       │ ──▶ │  actions        │ ──▶ │  (html/pdf)     │
│  (.ipynb)       │     │  + quarto       │     │                 │
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
  pdf:
    documentclass: scrartcl

execute:
  echo: false  # hide code in output
```

github action (simplified):
```yaml
name: Render

on:
  push:
    branches: [main]

jobs:
  render:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Quarto
        uses: quarto-dev/quarto-actions/setup@v2

      - name: Render
        run: quarto render

      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./_output
```

## limitations

- complex latex packages don't always work
- pandas tables sometimes look weird
- bibliography works but misses some biblatex features

## when to use this

- seminar papers, project documentation
- when code and text belong together
- **not for:** thesis, journal papers (use proper latex)

---

[→ repo](https://github.com/werzingerma/osws-scientific-report) · [→ quarto notes](/notes/quarto/)
