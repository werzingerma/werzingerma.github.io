---
layout: page
title: Insightify
permalink: /projekte/insightify/
---

<div class="project-detail">
  <p class="pill">Data Science · Python</p>
  <h2>Insightify</h2>

  <p><strong>A CLI tool for quick dataset analysis with an optional Streamlit dashboard.</strong></p>

  <p>
    <a href="https://github.com/werzingerma/insightify" class="primary-btn" target="_blank">View on GitHub</a>
  </p>

  <h3>Overview</h3>
  <p>
    I built Insightify because I got tired of writing the same exploratory data analysis code over and over. It's a command-line tool that lets you quickly inspect datasets, check for missing values, spot outliers, and generate basic visualizations. There's also a web dashboard if you prefer clicking around instead of typing commands.
  </p>

  <h3>What it does</h3>
  <ul>
    <li>Reads CSV, Excel, JSON, and Parquet files</li>
    <li>Shows quick stats and data quality info (missing values, outliers)</li>
    <li>Generates histograms, correlation plots, and scatter diagrams</li>
    <li>Basic filtering, grouping, and aggregation</li>
    <li>Can detect anomalies using simple ML</li>
    <li>Exports reports as HTML or PDF</li>
    <li>Optional Streamlit web interface</li>
  </ul>

  <h3>Built with</h3>
  <table>
    <tr><td><strong>Language</strong></td><td>Python</td></tr>
    <tr><td><strong>Web UI</strong></td><td>Streamlit</td></tr>
    <tr><td><strong>Data</strong></td><td>Pandas, NumPy</td></tr>
    <tr><td><strong>Plots</strong></td><td>Matplotlib, Plotly</td></tr>
  </table>

  <h3>Why I made this</h3>
  <p>
    Mostly for my own use when working with new datasets. Instead of opening a Jupyter notebook and writing the same df.describe(), df.isnull().sum() etc. every time, I wanted something that just does all of that in one command.
  </p>
</div>
