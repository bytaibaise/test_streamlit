import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("Me title.")
# Add a sidebar
st.sidebar.header('User Input Features')

@st.cache
def load_data():
    data = pd.read_csv('churn_clean.csv')
    return data

df = load_data()

# Show the data as a table
if st.checkbox('Show dataframe'):
    st.write(df)

# Show the data as a plot
if st.sidebar.checkbox('Show Plot'):
    st.subheader('Data Plot')
    st.line_chart(df)