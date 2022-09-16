import streamlit as st
import pandas as pd
from functools import reduce
from bs4 import BeautifulSoup as soup
import requests
import process_
import develop
data = pd.read_excel("fo_mktlots.xlsx")
df = process_.Moneycontrol()
af = develop.Investing()

st.sidebar.title("News Scraping")
user_menu = st.sidebar.radio(
    'Select an option',
     ('Moneycontrol website','Investing.com website')
)

if user_menu == 'Moneycontrol website':
    st.header("Moneycontrol Website")
    Moneycontrol_website = df
    st.dataframe(Moneycontrol_website)

if user_menu == 'Investing.com website':
    st.header("Investing Website")
    Investing_website = af
    st.dataframe(Investing_website)