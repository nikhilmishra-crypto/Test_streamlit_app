import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("My first Streamlit App")

st.header("Calculator App")

a= st.number_input("Enter a number ",min_value=1,max_value=500, value=100, key="number1")
b= st.number_input("Enter a number ",min_value=1,max_value=500, key="number2")

c=a+b

btn = st.button("calculate")



if btn:
    st.header(f"Addition of {a} and {b} : {c}")


st.subheader("fill the form")

var = st.text_input("Enter your name", key="name")

age= st.number_input("Enter your age", min_value=1, max_value=130, key="age")

export_btn = st.button("export data")



df= pd.read_csv("data/orders.csv")

st.dataframe(df)

st.subheader("city wise total qnty sold")

city_total= df.groupby("city").sum()["quantity"].sort_index(ascending=False)

st.dataframe(city_total)

st.subheader("city wise total qnty sold bar chart")

st.bar_chart(city_total)