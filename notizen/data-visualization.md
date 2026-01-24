---
layout: page
title: Data Visualization
permalink: /notizen/data-visualization/
---

# Data Visualization

Matplotlib, Seaborn, Plotly – wann was.

Stand: Januar 2025

---

## Matplotlib (der Standard)

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, label='Daten')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.legend()
plt.savefig('plot.png', dpi=150)
```

Meine üblichen Plot-Typen:

```python
ax.bar(categories, values)           # Balken
ax.scatter(x, y, alpha=0.5)          # Punkte
ax.hist(data, bins=30)               # Histogramm
ax.errorbar(x, y, yerr=err, fmt='o') # Mit Fehlerbalken
```

## Seaborn (für schnelle Exploration)

```python
import seaborn as sns

sns.histplot(df, x='values', kde=True)
sns.boxplot(df, x='category', y='values')
sns.heatmap(df.corr(), annot=True)
```

Bessere Defaults als Matplotlib. Gut für pandas DataFrames.

## Plotly (interaktiv)

```python
import plotly.express as px

fig = px.scatter(df, x='x', y='y', color='category')
fig.show()
fig.write_html('chart.html')
```

Für Dashboards und Web.

## Wann was

| Library | Wann |
|---------|------|
| Matplotlib | Paper, volle Kontrolle |
| Seaborn | Schnelle Exploration, statistische Plots |
| Plotly | Interaktiv, Web, Dashboards |

## Farb-Tipps

- `viridis`, `cividis` sind colorblind-friendly
- Kategorien: verschiedene Farbtöne
- Sequentiell: ein Farbton, variiert Helligkeit
- Divergierend: zwei Farben, treffen sich in der Mitte

---

## Links

- [From Data to Viz](https://www.data-to-viz.com/) – welcher Chart für welche Daten
- [ColorBrewer](https://colorbrewer2.org/) – Farbpaletten
