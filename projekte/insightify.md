---
layout: page
title: insightify
permalink: /projekte/insightify/
---

# insightify

CLI um schnell in CSVs/JSONs reinzuschauen.

## warum

Jupyter für jede kleine Datei aufmachen nervt. `df.describe()`, `df.isnull().sum()`, immer das gleiche. Also hab ich das in ein CLI gepackt.

## was geht

- `insightify info data.csv` → Spalten, Typen, Speicher
- `insightify profile data.csv` → Missing values, Outliers, Stats
- `insightify viz data.csv` → Histogramme, Korrelationen
- Optional: Streamlit Dashboard wenn mans lieber klickt

## was noch nicht so gut geht

- Große Dateien (>500MB) werden langsam
- PDF Export manchmal kaputt
- Keine interaktiven Plots im CLI (nur im Dashboard)

## tech

Python, Pandas, Matplotlib, Streamlit

---

[→ GitHub](https://github.com/werzingerma/insightify)
