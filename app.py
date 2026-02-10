import streamlit as st
import pandas as pd

url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv'
df = pd.read_csv(url)
df_récup = ["NA"] + sorted(df['pickup_borough'].dropna().unique())

st.title("Bienvenue sur le site web", text_alignment = "center")
st.header("de Dominique", text_alignment = "center")
arrond = st.selectbox("Indiquez votre arrondissement de récupération",
             df_récup) 
st.write('___')
st.image("Images/"+str(arrond)+".png")