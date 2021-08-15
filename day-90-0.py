# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 17:21:08 2021

@author: deepj
"""


import numpy as np

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Generate sample data
centers = [[1, 1], [-1, -1], [1, -1]]  # 3 ---> 0 1 2 

# make_blobs generates random points from any point from a list
# by default it gives 2 features, 
features, labels = make_blobs(n_samples=750, centers=centers, cluster_std=0.4,
                            random_state=0)

print(features)

print(labels)

#Scatter all these data points on the matplotlib
plt.scatter(features[:,0], features[:,1])
plt.show()



features = StandardScaler().fit_transform(features)

#Scatter all these data points on the matplotlib
plt.scatter(features[:,0], features[:,1])
plt.show()


# Compute DBSCAN
db = DBSCAN(eps=0.3, min_samples=10).fit(features)
#core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
#core_samples_mask[db.core_sample_indices_] = True

labels_pred = db.labels_ # belongs to which cluster id

print(labels_pred)



# Plot result
import matplotlib.pyplot as plt


plt.scatter(features[labels_pred == 0,0], features[labels_pred == 0,1],c='r', marker='+' )
plt.scatter(features[labels_pred == 1,0], features[labels_pred == 1,1],c='g', marker='o' )
plt.scatter(features[labels_pred == 2,0], features[labels_pred == 2,1],c='b', marker='s' )
plt.scatter(features[labels_pred == -1,0],features[labels_pred == -1,1],c='y', marker='*' )


#measure the performance of the dbscan

"""
# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

print('Estimated number of clusters: %d' % n_clusters_)
print('Estimated number of noise points: %d' % n_noise_)
print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
print("Adjusted Rand Index: %0.3f"
      % metrics.adjusted_rand_score(labels_true, labels))
print("Adjusted Mutual Information: %0.3f"
      % metrics.adjusted_mutual_info_score(labels_true, labels))
print("Silhouette Coefficient: %0.3f"
      % metrics.silhouette_score(X, labels))

"""

# Remmbering how to read data from datasets

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset boston dataset 
from sklearn.datasets import load_iris
iris = load_iris()

dataset = iris.data

##Noise 