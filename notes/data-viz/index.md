---
layout: page
title: data-viz
permalink: /notes/data-viz/
---

# data visualization

matplotlib, seaborn, plotly snippets.

---

## matplotlib basics

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, y, label="Data")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Title")
ax.legend()
plt.tight_layout()
plt.savefig("plot.png", dpi=150)
```

always use `fig, ax = plt.subplots()` – more control than `plt.plot()` directly.

## seaborn (statistical plots)

```python
import seaborn as sns

# distribution
sns.histplot(df["column"], kde=True)

# correlation
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")

# categorical
sns.boxplot(x="category", y="value", data=df)
```

## plotly (interactive)

```python
import plotly.express as px

fig = px.line(df, x="date", y="value", title="Trend")
fig.show()

# save as html
fig.write_html("plot.html")
```

## when to use what

| library | when |
|---------|------|
| matplotlib | papers, full control |
| seaborn | quick exploration, stats |
| plotly | interactive, dashboards |

## for papers

```python
plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

plt.savefig("figure.pdf", bbox_inches='tight')  # PDF for latex
```

---

## links

- [matplotlib gallery](https://matplotlib.org/stable/gallery/index.html)
- [seaborn gallery](https://seaborn.pydata.org/examples/index.html)
