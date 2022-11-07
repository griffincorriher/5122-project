import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

st.set_page_config(layout="wide")

df = pd.read_csv('data/Sample - Superstore.csv')
df

with st.container():
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Metrics of Interest")
        st.image("https://static.streamlit.io/examples/cat.jpg")

    with col2:
        st.header("Area of Interest")
        st.image("https://static.streamlit.io/examples/dog.jpg")

    with col3:
        st.header("Select Area(s)")
        st.image("https://static.streamlit.io/examples/owl.jpg")

with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Segments of Interest")
        st.image("https://static.streamlit.io/examples/cat.jpg")

    with col2:
        st.header("Category of Interest")
        st.image("https://static.streamlit.io/examples/dog.jpg")

    with col3:
        st.header("Select Product(s)")
        st.image("https://static.streamlit.io/examples/owl.jpg")

with st.container():
    col1, col2= st.columns([2,1])
    with col1:
        st.header("Chart Placeholder")
        st.line_chart(data=df, x='Sales', y='Profit')

    with col2:
        st.header("ML Recommendation Placeholder")
        st.image("https://static.streamlit.io/examples/dog.jpg")