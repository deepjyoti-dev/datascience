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



#version 02
#tf-idf 
#term frequency inverse document frequency

from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(df['reviewText'], df['Positivity'], random_state = 42, test_size = 0.5 )



from sklearn.feature_extraction.text import TfidfVectorizer

#vect = TfidfVectorizer(min_df = 50).fit(features_train)
#vect = TfidfVectorizer(min_df=5, ngram_range=(1, 2), stop_words='english', max_features= 2000,strip_accents='unicode', norm='l2')
vect = TfidfVectorizer(min_df=5, max_features= 3000)

features_train_vectorized = vect.fit_transform(features_train)
features_train_vectorized
features_train_vectorized = features_train_vectorized.todense()
# Deep Learning modules

import numpy as np

from keras.models import Sequential

from keras.layers.core import Dense, Dropout, Activation

from keras.optimizers import Adadelta,Adam,RMSprop

from keras.utils import np_utils

#Deep Layer Model building in Keras

#del model

model = Sequential()

model.add(Dense(1000,input_shape= (3000,)))

model.add(Activation('relu'))

model.add(Dropout(0.5))

model.add(Dense(500))

model.add(Activation('relu'))

model.add(Dropout(0.5))

model.add(Dense(50))

model.add(Activation('relu'))

model.add(Dropout(0.5))

model.add(Dense(1))

model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam')
model.fit(features_train_vectorized, labels_train, batch_size=32, epochs=10)


#Model Prediction

labels_train_predclass = model.predict_classes(features_train_vectorized,batch_size=64)

labels_test_predclass = model.predict_classes(vect.transform(features_test).todense(),batch_size=64)

from sklearn.metrics import accuracy_score

print (("nnDeep Neural Network - Train accuracy:"),(round(accuracy_score( labels_train, labels_train_predclass),3)))

print (("nDeep Neural Network - Test accuracy:"),(round(accuracy_score( labels_test,labels_test_predclass),3)))


model.save('model.h5')
#how to load the keras model
from keras.models import load_model
recreated_model = load_model('model.h5')

model.summary()