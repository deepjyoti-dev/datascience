# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 09:52:27 2021

@author: deepj
"""

from bs4 import BeautifulSoup as Bs
import pandas as pd
import requests as r

link = "https://www.embibe.com/exams/nirf-rankings/"
pg = r.get(link).text
sp = Bs(pg,"lxml")



all_tab = sp.find_all('div',class_="table")
csv_list =["NIRF Rankings Of Overall Educational Institutes.csv","NIRF Rankings Of Engineering Colleges.csv","NIRF Rankings Of Medical Institutes.csv","NIRF Rankings Of Universities.csv"]
for i in range(len(all_tab)):
    A=[]
    B=[]
    C=[]
    D=[]
    for body in all_tab[i].find_all("tbody"):
        for row in body.find_all("tr"):
            col = row.find_all('td')
            A.append(col[0].text.strip())
            B.append(col[1].text.strip())
            C.append(col[2].text.strip())
            D.append(col[3].text.strip())
           

    df = pd.DataFrame()
    df["Rank & Name of the Institute"]= A
    df["City"]=B
    df["State"]=C
    df["NIRF Score"]=D
    df.to_csv(csv_list[i], index=False)



