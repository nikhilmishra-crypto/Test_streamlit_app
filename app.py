import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("My first Streamlit App")

st.header("Calculator App")

a= st.number_input("Enter a number ",min_value=1,max_value=500, value=100, key="number1")
b= st.number_input("Enter a number ",min_value=1,max_value=500, key="number2")

c=a+b

btn = st.button("calculate")

