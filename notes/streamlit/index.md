---
layout: page
title: streamlit
permalink: /notes/streamlit/
---

# streamlit

quick & dirty python dashboards.

---

## when to use

- quickly visualize data
- prototype for stakeholders
- internal tools

not for: production apps with many users.

## basics

```python
# app.py
import streamlit as st
import pandas as pd

st.title("My Dashboard")

# widgets
name = st.text_input("Name")
age = st.slider("Age", 0, 100, 25)

# button
if st.button("Submit"):
    st.write(f"Hello {name}, you are {age} years old.")

# show dataframe
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
st.dataframe(df)

# plot
st.line_chart(df)
```

```bash
streamlit run app.py
```

## layout

```python
# columns
col1, col2 = st.columns(2)
with col1:
    st.write("Left")
with col2:
    st.write("Right")

# sidebar
with st.sidebar:
    st.selectbox("Option", ["A", "B", "C"])
```

## caching

important for performance:

```python
@st.cache_data
def load_data():
    return pd.read_csv("big_file.csv")

df = load_data()  # only slow the first time
```

---

## links

- [streamlit docs](https://docs.streamlit.io/)
- [cheat sheet](https://docs.streamlit.io/library/cheatsheet)
