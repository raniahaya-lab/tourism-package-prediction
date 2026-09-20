import streamlit as st
import pandas as pd
st.title("Tourism Package Prediction")
age = st.number_input("Age")
if st.button("Predict"):
    st.success("Prediction generated successfully")
