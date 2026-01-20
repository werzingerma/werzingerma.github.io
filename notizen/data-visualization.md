---
layout: page
title: Data Visualization
permalink: /notizen/data-visualization/
---

<p class="pill">Notes · Matplotlib · Plotly</p>

Notes on different plotting libraries and when to use them.

### Matplotlib basics

```python
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 6))

x = np.linspace(0, 10, 100)
ax.plot(x, np.sin(x), label='sin(x)', linewidth=2)
ax.plot(x, np.cos(x), label='cos(x)', linewidth=2)

ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_title('Trigonometric Functions', fontsize=14)
ax.legend()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('plot.png', dpi=150)
```

### Common plot types

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Bar chart
axes[0, 0].bar(['A', 'B', 'C'], [23, 45, 56], color='steelblue')

# Scatter
axes[0, 1].scatter(x, y, s=sizes, alpha=0.5, c=colors, cmap='viridis')

# Histogram
axes[1, 0].hist(data, bins=30, edgecolor='black')

# Line with error bars
axes[1, 1].errorbar(x, y, yerr=errors, fmt='o-')
```

---

## Seaborn

Higher-level API, better defaults, built for pandas.

```python
import seaborn as sns

sns.set_theme(style="whitegrid", palette="muted")

# Distribution
sns.histplot(data=df, x='values', kde=True)

# Categorical
sns.boxplot(data=df, x='category', y='values')
sns.violinplot(data=df, x='category', y='values')

# Relationships
sns.scatterplot(data=df, x='x', y='y', hue='category', size='value')

# Correlation matrix
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', center=0)

# Pair plot
sns.pairplot(df, hue='category')
```

---

## Plotly

Interactive plots, great for dashboards.

```python
import plotly.express as px
import plotly.graph_objects as go

# Quick plots
fig = px.scatter(df, x='x', y='y', color='category', size='value')
fig.show()

fig = px.line(df, x='date', y='value', color='category')

# More control
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y1, mode='lines', name='Series 1'))
fig.add_trace(go.Scatter(x=x, y=y2, mode='lines+markers', name='Series 2'))
fig.update_layout(
    title='Custom Chart',
    template='plotly_white'
)

# Save
fig.write_html('chart.html')
fig.write_image('chart.png')
```

---

### When to use what

| Library | Use case |
|---------|----------|
| Matplotlib | Full control, publication-quality, static |
| Seaborn | Statistical plots, quick exploration |
| Plotly | Interactive, dashboards, web |
| Altair | Declarative grammar of graphics |

### Color tips

- Use colorblind-friendly palettes: `viridis`, `cividis`, `plasma`
- Sequential data: single hue varying in lightness
- Diverging data: two hues meeting at neutral midpoint
- Categorical: distinct hues, similar saturation

### Resources

- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)
- [Plotly Python](https://plotly.com/python/)
- [From Data to Viz](https://www.data-to-viz.com/) - Which chart to use
- [ColorBrewer](https://colorbrewer2.org/)
