
import pandas as pd


df = pd.read_csv("addhealth.csv")

df.isnull().any(axis = 0)

for i in df:
    df[i] = df[i].fillna(df[i].mode()[0])


features = df[['BIO_SEX','age','WHITE','BLACK','HISPANIC','NAMERICAN','ASIAN',
           'ALCEVR1','ALCPROBS1','marever1','cocever1','inhever1','cigavail',
           
           'DEP1','ESTEEM1']].values
labels = df["TREG1"].values
    

from sklearn.model_selection import train_test_split as TTS

features_train,features_test,labels_train,labels_test = TTS(features, labels, test_size = 0.25,
                                    random_state = 0)

from sklearn.linear_model import LogisticRegression
classification_treg1 = LogisticRegression(random_state=0,max_iter=5000)
classification_treg1.fit(features_train, labels_train)

pred = classification_treg1.predict(features_test)   


from sklearn.metrics import confusion_matrix
classification_treg1_cm = confusion_matrix(labels_test, pred)

classification_treg1_score = classification_treg1.score(features_test, labels_test)
    


print ("model accuracy using confusion matrix (LogisticRegression): "+str(classification_treg1_cm))
print ("model accuracy using .score() function (LogisticRegression): "+str(round(classification_treg1_score*100,2)))


features_expel = df[["BIO_SEX","VIOL1"]].values
labels_expel = df["EXPEL1"].values


from sklearn.model_selection import train_test_split as TTS

f_train,f_test,l_train,l_test = TTS(features_expel, labels_expel, test_size = 0.25,
                                    random_state = 0)


from sklearn.linear_model import LogisticRegression
classifier_expel = LogisticRegression(random_state=0)
classifier_expel.fit(f_train, l_train)

Pred1 = classifier_expel.predict(f_test)  


from sklearn.metrics import confusion_matrix
CM1 = confusion_matrix(l_test, Pred1)


Score1 = classifier_expel.score(f_test, l_test)
    


print ("model accuracy using confusion matrix (LogisticRegression): "+str(CM1))
print ("model accuracy using .score() function (LogisticRegression): "+str(round(Score1*100,2)))


from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split as TTS
from sklearn.metrics import confusion_matrix, accuracy_score


classifier_knn = KNeighborsClassifier(n_neighbors = 8)


######## Solution for Part 1 ########


fe = df[['BIO_SEX','age','WHITE','BLACK','HISPANIC','NAMERICAN','ASIAN',
           'ALCEVR1','ALCPROBS1','marever1','cocever1','inhever1','cigavail',
           'DEP1','ESTEEM1']].values
la = df["TREG1"].values


ft_train,ft_test,l_train,l_test = TTS(fe,la,test_size=.2,random_state=0)


classifier_knn.fit(ft_train,l_train)
pred_knn = classifier_knn.predict(ft_test)


CM = confusion_matrix(pred_knn,l_test)


Score = accuracy_score(l_test,pred_knn)
print ("model accuracy using confusion matrix (KNN): "+str(CM))
print ("model accuracy using .score() function (KNN): "+str(round(Score*100,2))+"%")



######## Solution for Part 2 ########


fe1 = df[["BIO_SEX","VIOL1"]].values
la1 = df["EXPEL1"].values


ftr,fte,ltr,lte = TTS(fe1,la1,test_size=.2,random_state=0)


classifier_knn.fit(ftr,ltr)
Pred1 = classifier_knn.predict(fte)


CM1 = confusion_matrix(Pred1,lte)


Score1 = accuracy_score(lte,Pred1)

print ("model accuracy using confusion matrix (KNN): "+str(CM1))
print ("model accuracy using .score() function (KNN): "+str(round(Score1*100,2))+"%")

