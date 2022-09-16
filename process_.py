import streamlit as st
import pandas as pd
from functools import reduce
from bs4 import BeautifulSoup as soup
import requests
data = pd.read_excel("fo_mktlots.xlsx")

def Moneycontrol():
     data.drop(data.iloc[:, 2:], inplace=True, axis=1)
     key = []
     for i in data['UNDERLYING']:
         key.append(i)

     def remove(key):
         s = []
         for i in key:
             # print(i.strip()+"gg")
             s.append(i.strip())
         return s

     a = remove(data['UNDERLYING'])
     b = remove(data['SYMBOL    '])

     c = a + b

     def recognize(s, key):
         answer = []
         for i in s:
             pairofheadandkey = []
             i = i.upper()
             arr = i.split()
             for j in arr:
                 for k in key:
                     if k == j:
                         new_str = " ".join(arr)
                         pairofheadandkey.append(new_str)
                         pairofheadandkey.append(k)
                         answer.append(pairofheadandkey)
                         break
         return answer

     url = 'https://www.moneycontrol.com/news/'
     html = requests.get(url)
     bsobj = soup(html.content, 'lxml')
     count = 0
     headlines_with_keyword = []
     all_headlines = []

     for link in bsobj.findAll('h3', class_='related_des'):
         sentence = link.text.upper()
         all_headlines.append(sentence)

         try:
             ans = recognize(all_headlines, c)

         except:
             pass

     for link in bsobj.findAll(class_='title'):
         sentence = link.text.upper()
         all_headlines.append(sentence)

         try:
             ans = recognize(all_headlines, c)

         except:
             pass

     for link in bsobj.findAll("h2", class_='related_des'):
         sentence = link.text.upper()
         all_headlines.append(sentence)

     try:
         ans = recognize(all_headlines, c)

     except:
         pass



     ans = set(tuple(element) for element in ans)
     final_data = pd.DataFrame(ans)

     return final_data