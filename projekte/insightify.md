---
layout: page
title: insightify
permalink: /projekte/insightify/
---

# insightify

CLI um schnell in Datasets reinzuschauen. Ohne Jupyter, ohne IDE.

## warum

Bei der Arbeit ständig CSVs gecheckt – Jupyter dafür aufmachen war mir zu umständlich.

## beispiel

```bash
$ insightify info verkaufsdaten.csv

 Datei: verkaufsdaten.csv
 Rows:  15,847
 Cols:  12

 Column       Type      Unique    Missing
 ──────────────────────────────────────────
 datum        date      365       0%
 umsatz       float     8,421     0.1%
 kunde_id     string    2,847     0%
 region       category  4         2.1%

$ insightify profile verkaufsdaten.csv --output report.html
```

## was geht

- `info` – Schneller Überblick
- `profile` – Missing Values, Outliers, Verteilungen
- `viz` – Histogramme, Korrelationen
- CSV, Excel, JSON, Parquet

## was noch nicht geht

- [ ] Dateien >500MB nicht getestet
- [ ] PDF-Export ist buggy
- [ ] Keine interaktive Shell (wäre cool)

## tech

Python, Pandas, Matplotlib, Streamlit

---

[→ GitHub](https://github.com/werzingerma/insightify)
