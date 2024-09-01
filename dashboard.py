import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title("Interactive Data Visualization Dashboard")
st.write("Welcome to my first interactive dashboard using Streamlit!")
# Load an example dataset
df = sns.load_dataset("iris")
st.subheader("Scatter Plot")
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
st.plotly_chart(fig)
species = st.selectbox("Choose a species", df["species"].unique())
filtered_df = df[df["species"] == species]
st.write(f"Selected species: {species}")
fig = px.scatter(filtered_df, x="sepal_width", y="sepal_length", color="species")
st.plotly_chart(fig)
st.subheader("Histogram of Sepal Length")
fig = plt.figure(figsize=(10, 4))
sns.histplot(df["sepal_length"], bins=20, kde=True)
st.pyplot(fig)
col1, col2 = st.columns(2)
col1.write("Column 1 content here")
col2.write("Column 2 content here")
if st.button("Show Summary Statistics"):
    st.write(df.describe())
