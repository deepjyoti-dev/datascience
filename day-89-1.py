# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 16:48:27 2021

@author: deepj
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv('xclara.csv')

features = dataset.iloc[:, [0, 1]].values


plt.scatter(features[:,0], features[:,1])
plt.show()


from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)

pred_cluster = kmeans.fit_predict(features)

print(pred_cluster)



plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Cluster 2')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'Cluster 3')


print(kmeans.cluster_centers_)  # There are three points for 3 centroid

print(kmeans.cluster_centers_[:, 0]) # x 
print(kmeans.cluster_centers_[:, 1]) # y 

# Central Location of the Cluster == Centroid
# Centroid = Avg of x coordinate and Avg of y coordinate for lets assume Cluster 1
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Cluster 2')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'Cluster 3')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')



plt.title('Clusters of datapoints')
plt.xlabel('X Cordindates')
plt.ylabel('Y Cordinates')
plt.legend()
plt.show()

for i in range(1, 11):
    print(i)
   
    
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('xclara.csv')

features = dataset.iloc[:, [0, 1]].values
   

from sklearn.cluster import KMeans

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans.fit(features)  
 
    wcss.append(kmeans.inertia_)  
    
       
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()


from sklearn.metrics import silhouette_score

for n_clusters in range(2, 11):
    clusterer = KMeans (n_clusters=n_clusters)
    preds = clusterer.fit_predict(features)
    centers = clusterer.cluster_centers_

    score = silhouette_score (features, preds, metric='euclidean')
    print("For n_clusters =", n_clusters,
          "The average silhouette_score is :", score)
 