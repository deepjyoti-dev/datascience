

import pandas as p


data = p.read_csv("mushrooms.csv")


f = data.iloc[:,[5,-2,-1]].values 
l = data.iloc[:,0].values
             
from sklearn.preprocessing import LabelEncoder

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

le = LabelEncoder()
l = le.fit_transform(l)

cT = ColumnTransformer([('encoder', OneHotEncoder(), [0,1,2])], remainder = 'passthrough')


f = cT.fit_transform(f).toarray()

from sklearn.model_selection import train_test_split as tts
f_train,f_test,l_train,l_test = tts(f,l,test_size=0.25,random_state=0)

from sklearn.neighbors import KNeighborsClassifier as knc
classifier = knc(n_neighbors=3, p=3)
classifier.fit(f_train,l_train)
pred = classifier.predict(f_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(l_test,pred)

print ("Model Score : "+str(round(classifier.score(f_test,l_test),3)*100)+"%")


