import streamlit as st
import pandas as pd
from functools import reduce
from bs4 import BeautifulSoup as soup
import requests
data = pd.read_excel("fo_mktlots.xlsx")


def Investing():
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

     from bs4 import BeautifulSoup as soup
     import requests

     url = 'https://www.investing.com/news/'
     html = requests.get(url)
     bsobj = soup(html.content, 'lxml')
     headlines_with_keyword_ = []
     all_headlines_ = []

     for link in bsobj.findAll(class_="title"):
         print("{}".format(link.text.upper()))
         sentence = link.text.upper()
         all_headlines_.append(sentence)

         try:
             ans_ = recognize(all_headlines_, c)

         except:
             pass

     ans_ = set(tuple(element) for element in ans_)
     ans_

     final_data = pd.DataFrame(ans_)
     return final_data