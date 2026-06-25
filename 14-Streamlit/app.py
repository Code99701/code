import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## title of the application
st.title("My First Streamlit App")

## display a simple text
st.write("Hello, welcome to my first Streamlit app!")

## create a simple dataframe
df = pd.DataFrame({ 
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
})

## display the dataframe
st.write("Here is a simple dataframe:")
st.write(df)

## create a simple line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)
st.line_chart(chart_data)


