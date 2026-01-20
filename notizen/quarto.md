---
layout: page
title: Quarto
permalink: /notizen/quarto/
---

<p class="pill">Notes · Publishing · Scientific Writing</p>

Quarto is a publishing system for creating documents, presentations, websites, and books from Markdown and Jupyter notebooks.

### Why Quarto?

- Write in Markdown or Jupyter notebooks
- Output to HTML, PDF, Word, presentations
- Built-in support for citations, cross-references, figures
- Multiple journal templates (Springer, Elsevier, Nature, etc.)
- Great for reproducible research

### Installation

```bash
# macOS
brew install quarto

# Or download from quarto.org
```

### Basic document

Create `document.qmd`:

```markdown
---
title: "My Document"
author: "Max"
format: html
---

## Introduction

This is a Quarto document with **markdown** and code.

```{python}
import pandas as pd
df = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
df
```

## Conclusion

That's it!
```

Render it:

```bash
quarto render document.qmd
```

---

## Output formats

### HTML

```yaml
---
format:
  html:
    toc: true
    toc-depth: 2
    theme: cosmo
    code-fold: true
---
```

### PDF (requires LaTeX)

```yaml
---
format:
  pdf:
    documentclass: article
    papersize: a4
    fontsize: 11pt
---
```

### Word

```yaml
---
format:
  docx:
    reference-doc: template.docx
---
```

### Multiple formats

```yaml
---
format:
  html: default
  pdf: default
  docx: default
---
```

---

## Citations

### BibTeX file

Create `references.bib`:

```bibtex
@article{smith2020,
  author = {Smith, John},
  title = {A Great Paper},
  journal = {Journal of Examples},
  year = {2020},
  volume = {1},
  pages = {1-10}
}
```

### Use in document

```yaml
---
bibliography: references.bib
csl: apa.csl
---
```

```markdown
According to @smith2020, this is important.

Multiple citations [@smith2020; @jones2021].

This is also important [see @smith2020, p. 5].
```

---

## Figures and tables

### Figures with captions

```markdown
![A descriptive caption](image.png){#fig-myimage width=80%}

See @fig-myimage for details.
```

### Tables

```markdown
| Column 1 | Column 2 |
|----------|----------|
| A        | B        |
| C        | D        |

: My table caption {#tbl-mytable}

See @tbl-mytable.
```

### Code output as figure

````markdown
```{python}
#| label: fig-plot
#| fig-cap: "A scatter plot"

import matplotlib.pyplot as plt
plt.scatter([1,2,3], [4,5,6])
plt.show()
```
````

---

## Journal templates

```bash
# List available templates
quarto use template quarto-journals/

# Use specific template
quarto use template quarto-journals/elsevier
```

Common templates:
- `quarto-journals/elsevier`
- `quarto-journals/plos`
- `quarto-journals/jss`
- `quarto-journals/acs`

---

## Projects and websites

### Create project

```bash
quarto create-project mysite --type website
```

### _quarto.yml

```yaml
project:
  type: website

website:
  title: "My Site"
  navbar:
    left:
      - href: index.qmd
        text: Home
      - href: about.qmd
        text: About

format:
  html:
    theme: cosmo
```

### Preview and publish

```bash
# Preview locally
quarto preview

# Render all
quarto render

# Publish to GitHub Pages
quarto publish gh-pages
```

### Resources

- [Quarto Docs](https://quarto.org/docs/guide/)
- [Quarto Gallery](https://quarto.org/docs/gallery/)
- [Journal Templates](https://quarto.org/docs/journals/)
