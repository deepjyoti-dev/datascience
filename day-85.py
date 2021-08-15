# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 06:47:34 2021

@author: deepj
"""


import pandas as pd
dataset = pd.read_csv("Churn_Modelling.csv")

dataset.shape

dataset['Geography'].unique()

dataset.shape

dataset.head()

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

features = dataset.iloc[:, 3:13].values
labels = dataset.iloc[:, 13].values

type(features)

features.shape

features[0:10,:]

dataset.dtypes

features

labels

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

columnTransformer = ColumnTransformer([('encoder', OneHotEncoder(), [1,2])], remainder='passthrough')

features = np.array(columnTransformer.fit_transform(features), dtype = np.float32)

features[0:10,:]

features = features[:, 1:] #drop the first dummy column for Geography

features[0]

features = features[:, [0,1,3,4,5,6,7,8,9,10,11]] #drop the column for Gender

features.shape

features[0,:]

features.shape

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)

features[0]

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

features_train[0]

# Importing the Keras libraries and packages
import keras
from keras.models import Sequential
from keras.layers import Dense



classifier = Sequential()

features.shape

#adding the first hidden layer
classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu', input_dim = 11))

# Adding the second hidden layer
classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu'))

# Adding the output layer
classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation='sigmoid'))

# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

classifier.fit(features_train, labels_train, batch_size = 10, epochs = 10)

labels_pred = classifier.predict_classes(features_test)
#labels_pred = (labels_pred > 0.5)

labels_pred

len(labels_pred)

list(zip(labels_test, labels_pred))

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

cm