import streamlit as st
import pandas as pd

st.title('🎈 MENTAL_HEALTH')

st.write('Hello world!')
df = pd.read_csv("https://raw.githubusercontent.com/Mohsenmohebbi1993/penguins/refs/heads/main/penguins_size.csv")
df
