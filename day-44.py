import pandas as p

df=p.read_csv("caesarian.csv");

df.shape

df.columns.tolist()

df.dtypes

df.isnull().any(axis=0)

features=df.iloc[:,0:5].values
labels=df.iloc[:,-1].values


from sklearn.model_selection import train_test_split as tts


f_train, f_test, l_train, l_test = tts(features, labels, test_size = 0.2)

from sklearn.neighbors import KNeighborsClassifier


classifier = KNeighborsClassifier(n_neighbors = 5, p = 1)

classifier.fit(f_train, l_train)

pred = classifier.predict(f_test)


from sklearn.metrics import confusion_matrix


confusion_matrix(l_test, pred)

x = [22, 1, 0, 1, 0]

import numpy as np

x = np.array(x)

x =  x.reshape(1,5)

classifier.predict(x)


