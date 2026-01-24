---
layout: page
title: quarto
permalink: /notes/quarto/
---

# quarto

scientific publishing from jupyter notebooks / markdown.

used in: [quarto-workflow project](/projects/quarto-workflow/)

---

## basics

```bash
brew install quarto
quarto render document.qmd
```

```markdown
---
title: "My Paper"
author: "Max"
format: pdf
bibliography: refs.bib
---

## Introduction

According to @smith2020 this is important.

```{python}
import pandas as pd
df = pd.read_csv("data.csv")
df.describe()
```
```

## output formats

```yaml
# PDF (needs LaTeX)
format:
  pdf:
    documentclass: article

# HTML with TOC
format:
  html:
    toc: true
    code-fold: true

# multiple at once
format:
  html: default
  pdf: default
```

## citations

```bibtex
# refs.bib
@article{smith2020,
  author = {Smith, John},
  title = {A Paper},
  year = {2020}
}
```

```markdown
According to @smith2020 this is true.
Multiple sources [@smith2020; @jones2021].
```

## journal templates

```bash
quarto use template quarto-journals/elsevier
```

available for Springer, Nature, PLOS, etc.

## what i learned

- latex errors are cryptic – render to HTML first for testing
- `code-fold: true` is great for papers – code there but hidden
- github actions for auto-rendering works well

---

## links

- [quarto docs](https://quarto.org/docs/guide/)
- [journal templates](https://quarto.org/docs/journals/)
