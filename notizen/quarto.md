---
layout: page
title: Quarto
permalink: /notizen/quarto/
---

# Quarto

Jupyter Notebooks als Paper publishen. Markdown + Code = PDF/HTML/Word.

Benutzt für: [Quarto Workflow](/projekte/osws-scientific-report/)

Stand: Januar 2025

---

## Basics

```bash
brew install quarto
quarto render document.qmd
```

```markdown
---
title: "Mein Paper"
author: "Max"
format: pdf
bibliography: refs.bib
---

## Einleitung

Laut @smith2020 ist das wichtig.

```{python}
import pandas as pd
df = pd.read_csv("data.csv")
df.describe()
```
```

## Output-Formate

```yaml
# PDF (braucht LaTeX)
format:
  pdf:
    documentclass: article

# HTML mit Inhaltsverzeichnis
format:
  html:
    toc: true
    code-fold: true

# Mehrere gleichzeitig
format:
  html: default
  pdf: default
```

## Zitieren

```bibtex
# refs.bib
@article{smith2020,
  author = {Smith, John},
  title = {A Paper},
  year = {2020}
}
```

```markdown
Nach @smith2020 ist das so.
Mehrere Quellen [@smith2020; @jones2021].
```

## Journal Templates

```bash
quarto use template quarto-journals/elsevier
```

Gibt's für Springer, Nature, PLOS, etc.

## Was ich gelernt hab

- LaTeX-Fehler sind kryptisch. Erstmal HTML rendern zum Testen
- `code-fold: true` ist super für Papers – Code da, aber versteckt
- GitHub Actions für automatisches Rendering funktioniert gut

---

## Links

- [Quarto Docs](https://quarto.org/docs/guide/)
- [Journal Templates](https://quarto.org/docs/journals/)
