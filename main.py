from enum import unique
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    st.write("File uploaded...")
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview:")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_columns = st.selectbox("Select columns to filter", columns)
    unique_values = df[selected_columns].unique()
    selected_value = st.selectbox("Select a value", unique_values)

    filtered_df = df[df[selected_columns] == selected_value]
    st.write("filtered_df")

    st.subheader("Plot Data")
    x_columns = st.selectbox("Select X-axis column", columns)
    y_columns = st.selectbox("Select Y-axis column", columns)

    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_columns) [y_columns])
else:
    st.write("Waiting on file upload....")
        
 












    
    

