---
layout: page
title: Streamlit
permalink: /notizen/streamlit/
---

# Streamlit

Python-Script wird Web-App. Kein HTML/CSS nötig.

Stand: Januar 2025

---

## Hello World

```python
import streamlit as st

st.title("Meine App")
name = st.text_input("Name?")
if name:
    st.write(f"Hi {name}!")
```

```bash
streamlit run app.py
```

## Widgets die ich oft brauche

```python
# Input
text = st.text_input("Label")
number = st.slider("Wert", 0, 100, 50)
option = st.selectbox("Auswahl", ["A", "B", "C"])
file = st.file_uploader("CSV hochladen", type="csv")

# Button
if st.button("Los"):
    st.write("Clicked!")

# DataFrame anzeigen
st.dataframe(df)

# Plot
st.line_chart(data)
```

## Layout

```python
# Zwei Spalten
col1, col2 = st.columns(2)
with col1:
    st.write("Links")
with col2:
    st.write("Rechts")

# Sidebar
with st.sidebar:
    option = st.selectbox("Menu", ["A", "B"])
```

## Session State

Streamlit läuft bei jeder Interaktion neu. State speichern:

```python
if 'count' not in st.session_state:
    st.session_state.count = 0

if st.button("Plus"):
    st.session_state.count += 1

st.write(st.session_state.count)
```

## Caching

```python
@st.cache_data
def load_data(path):
    return pd.read_csv(path)  # läuft nur einmal
```

## Wann Streamlit, wann was anderes

- Streamlit: Schnelle Demos, ML-Prototypen, interne Tools
- Gradio: Wenn's nur um ein ML-Model geht
- Flask/FastAPI: Wenn mehr Kontrolle nötig

---

## Links

- [Streamlit Docs](https://docs.streamlit.io/)
- [Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)
