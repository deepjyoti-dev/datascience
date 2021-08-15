# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 08:47:57 2021

@author: deepj
"""

import pandas as pd

df =  pd.read_csv('balanced_reviews.csv')



df.isnull().any(axis = 0)

#handle the missing data
df.dropna(inplace =  True)

#leaving the reviews with rating 3 and collect reviews with
#rating 1, 2, 4 and 5 onyl

df = df [df['overall'] != 3]

import numpy as np

#creating a label
#based on the values in overall column
df['Positivity'] = np.where(df['overall'] > 3 , 1 , 0)

#NLP
#reviewText - feature - df['reviewText']
#Positivity - label - df['Positivity']

#version #01

from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(df['reviewText'], df['Positivity'], random_state = 42 )



from sklearn.feature_extraction.text import CountVectorizer

vect = CountVectorizer().fit(features_train)

len(vect.get_feature_names())


vect.get_feature_names()[10000:10010]


features_train_vectorized = vect.transform(features_train)


#features_train_vectorized.toarray()


#create the classifier (first model)

#SVC,KNN, Naive Bayes, Logistic Regression, DT, RF


from sklearn.linear_model import LogisticRegression


model = LogisticRegression(max_iter=8000)

model.fit(features_train_vectorized, labels_train)

predictions = model.predict(vect.transform(features_test))


from sklearn.metrics import confusion_matrix

confusion_matrix(labels_test, predictions)

from sklearn.metrics import roc_auc_score
roc_auc_score(labels_test, predictions)


#version 02
#tf-idf 
#term frequency inverse document frequency

from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(df['reviewText'], df['Positivity'], random_state = 42 )



from sklearn.feature_extraction.text import TfidfVectorizer

vect = TfidfVectorizer(min_df = 5).fit(features_train)

len(vect.get_feature_names())


vect.get_feature_names()[10000:10010]


features_train_vectorized = vect.transform(features_train)


#features_train_vectorized.toarray()


#create the classifier (first model)

#SVC,KNN, Naive Bayes, Logistic Regression, DT, RF


from sklearn.linear_model import LogisticRegression


model = LogisticRegression(max_iter=8000)

model.fit(features_train_vectorized, labels_train)

predictions = model.predict(vect.transform(features_test))


from sklearn.metrics import confusion_matrix

confusion_matrix(labels_test, predictions)

from sklearn.metrics import roc_auc_score
roc_auc_score(labels_test, predictions)


#save - pickle format



