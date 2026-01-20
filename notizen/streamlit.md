---
layout: page
title: Streamlit
permalink: /notizen/streamlit/
---

<p class="pill">Notes · Python · Dashboards</p>

Streamlit turns Python scripts into web apps. No frontend knowledge needed.

### Why Streamlit?

- Write only Python, no HTML/CSS/JS
- Hot reload during development
- Built-in widgets for user input
- Easy to deploy
- Great for data apps and ML demos

### Installation

```bash
pip install streamlit
```

### Hello World

Create `app.py`:

```python
import streamlit as st

st.title("Hello Streamlit")
st.write("This is my first app!")

name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}!")
```

Run it:

```bash
streamlit run app.py
```

---

## Input widgets

```python
import streamlit as st

# Text
name = st.text_input("Name")
bio = st.text_area("Bio")

# Numbers
age = st.number_input("Age", min_value=0, max_value=120)
rating = st.slider("Rating", 1, 10, 5)

# Selection
option = st.selectbox("Choose one", ["A", "B", "C"])
options = st.multiselect("Choose many", ["X", "Y", "Z"])

# Boolean
agree = st.checkbox("I agree")
on = st.toggle("Enable feature")

# Date/Time
date = st.date_input("Date")
time = st.time_input("Time")

# File upload
file = st.file_uploader("Upload a file", type=["csv", "txt"])

# Button
if st.button("Submit"):
    st.write("Submitted!")
```

---

## Displaying data

```python
import streamlit as st
import pandas as pd
import numpy as np

# DataFrames
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35]
})

st.dataframe(df)  # Interactive table
st.table(df)      # Static table

# Metrics
st.metric("Temperature", "70°F", delta="2°F")

# JSON
st.json({"key": "value", "list": [1, 2, 3]})

# Code
st.code("print('hello')", language="python")
```

### Charts

```python
import streamlit as st
import pandas as pd
import numpy as np

# Built-in charts
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)
st.area_chart(chart_data)
st.bar_chart(chart_data)

# Matplotlib
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])
st.pyplot(fig)

# Plotly
import plotly.express as px

fig = px.scatter(df, x='x', y='y', color='category')
st.plotly_chart(fig)
```

---

## Layout

```python
import streamlit as st

# Columns
col1, col2 = st.columns(2)
with col1:
    st.write("Left column")
with col2:
    st.write("Right column")

# Tabs
tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
with tab1:
    st.write("Content of tab 1")
with tab2:
    st.write("Content of tab 2")

# Sidebar
with st.sidebar:
    st.title("Sidebar")
    option = st.selectbox("Select", ["A", "B"])

# Expander
with st.expander("Click to expand"):
    st.write("Hidden content")

# Container
with st.container():
    st.write("Grouped content")
```

---

## State management

Streamlit reruns the script on every interaction. Use `st.session_state` to persist data.

```python
import streamlit as st

# Initialize state
if 'count' not in st.session_state:
    st.session_state.count = 0

# Update state
if st.button("Increment"):
    st.session_state.count += 1

st.write(f"Count: {st.session_state.count}")

# Form (batches inputs)
with st.form("my_form"):
    name = st.text_input("Name")
    age = st.number_input("Age")
    submitted = st.form_submit_button("Submit")

    if submitted:
        st.write(f"Hello {name}, age {age}")
```

---

## Caching

Avoid recomputing expensive functions:

```python
import streamlit as st

@st.cache_data
def load_data(url):
    return pd.read_csv(url)

@st.cache_resource
def load_model():
    return SomeHeavyModel()

df = load_data("data.csv")  # Only runs once
model = load_model()
```

### Deployment

```bash
# Streamlit Community Cloud (free)
# 1. Push to GitHub
# 2. Go to share.streamlit.io
# 3. Connect repo

# Or use Docker
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

### Resources

- [Streamlit Docs](https://docs.streamlit.io/)
- [Streamlit Gallery](https://streamlit.io/gallery)
- [Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)
