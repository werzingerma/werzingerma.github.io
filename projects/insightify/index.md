---
layout: page
title: insightify
permalink: /projects/insightify/
---

# insightify

cli to quickly inspect datasets. no jupyter, no IDE.

## why

kept checking CSVs at work – opening jupyter every time was too much hassle.

## usage

```bash
$ insightify info sales_data.csv

 file: sales_data.csv
 rows:  15,847
 cols:  12

 column       type      unique    missing
 ──────────────────────────────────────────
 date         date      365       0%
 revenue      float     8,421     0.1%
 customer_id  string    2,847     0%
 region       category  4         2.1%

$ insightify profile sales_data.csv --output report.html
```

## what works

- `info` – quick overview
- `profile` – missing values, outliers, distributions
- `viz` – histograms, correlations
- csv, excel, json, parquet

## what doesn't work (yet)

- [ ] files >500MB not tested
- [ ] pdf export is buggy
- [ ] no interactive shell (would be nice)

## install

```bash
pip install insightify
```

---

[→ repo](https://github.com/werzingerma/insightify)
