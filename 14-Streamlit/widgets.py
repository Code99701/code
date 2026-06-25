import streamlit as st
import pandas as pd

st.title("Streamlit text imput")

name = st.text_input("Enter your name:")

age = st.slider("Select your age:", 0, 100, 25)

options = ["python", "javascript", "java", "c++", "ruby"]
choice = st.selectbox("Select your favorite programming language:", options)
st.write(f"Your favorite programming language is: {choice}")

st.write(f"You are {age} years old.")


if name:
    st.write(f"Hello, {name}!")


data ={ 
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

df = pd.DataFrame(data)
df.to_csv("sample_data.csv", index=False)
st.write("Here is a simple dataframe:")
st.write(df)

uploaded_file = st.file_uploader("Choose a csv file",type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)