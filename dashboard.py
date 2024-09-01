import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Title of the dashboard
st.title("Interactive Data Visualization Dashboard")
st.write("Welcome to my first interactive dashboard using Streamlit!")

# Load an example dataset
df = sns.load_dataset("iris")

# Scatter plot using Plotly
st.subheader("Scatter Plot")
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
st.plotly_chart(fig)

# Filtered scatter plot based on user selection
species = st.selectbox("Choose a species", df["species"].unique())
filtered_df = df[df["species"] == species]
st.write(f"Selected species: {species}")
fig = px.scatter(filtered_df, x="sepal_width", y="sepal_length", color="species")
st.plotly_chart(fig)

# Histogram of Sepal Length using Matplotlib and Seaborn
st.subheader("Histogram of Sepal Length")

# Create a figure for the plot
fig, ax = plt.subplots(figsize=(10, 4))
sns.histplot(df["sepal_length"], bins=20, kde=True, ax=ax)

# Display the plot in Streamlit
st.pyplot(fig)

# Two columns for additional content
col1, col2 = st.columns(2)
col1.write("Column 1 content here")
col2.write("Column 2 content here")

# Button to show summary statistics
if st.button("Show Summary Statistics"):
    st.write(df.describe())
