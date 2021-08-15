# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 17:18:47 2021

@author: deepj
"""

# using db scan


import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
data=pd.read_csv("deliveryfleet.csv")

data.isnull().any(axis=0)

data.info()

features=data.iloc[:,[1,2]].values

plt.scatter(features[:,0], features[:,1])
plt.show()

stscaler = StandardScaler().fit(data)

data = stscaler.transform(data)
from sklearn.cluster import DBSCAN

db = DBSCAN(eps=0.3, min_samples=10).fit(data)
labels = db.labels_ 


len(features[labels== 0])

len(features[labels== 1])

len(features[labels== 2])

len(features[labels== -1])

plt.scatter(features[labels== 0,0], features[labels == 0,1],c='red', marker='+' )
plt.scatter(features[labels == 1,0], features[labels == 1,1],c='green', marker='o' )
plt.scatter(features[labels == 2,0], features[labels == 2,1],c='blue', marker='s' )
plt.scatter(features[labels == -1,0],features[labels == -1,1],c='yellow', marker='*' )

plt.title('Clusters of Drivers')
plt.xlabel('Distance_Feature')
plt.ylabel('Speed_Feature')
plt.legend()
