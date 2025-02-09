import streamlit as st
import pandas as pd
import nbformat
from nbconvert import PythonExporter

st.title("Prodigy InfoTech Task 5 - Data Analysis")

st.write("### 📊 Data from Notebooks")

# Load a CSV file (if your notebooks generate CSVs)
try:
    df = pd.read_csv("/Users/adityakumar/Downloads/US_Accidents_March23.csv")  # Replace with your actual data file
    st.dataframe(df)  # Display the data
except FileNotFoundError:
    st.write("No data file found. Please check the file path.")

st.write("### 📈 Visualization")
st.line_chart(df)  # Example visualization

st.write("### 💡 Insights")
st.write("This app visualizes data analysis from Jupyter Notebooks.")

st.write("### 🔍 Want More Features?")
st.write("Modify `app.py` to add your own custom graphs and insights!")
