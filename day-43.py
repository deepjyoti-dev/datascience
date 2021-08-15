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
#p = 1, manhanttan
#p = 2, euclidian


classifier.fit(f_train, l_train)

classifier.predict(f_test)
