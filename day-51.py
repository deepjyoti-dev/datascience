
import numpy as n
import pandas as p


dataset = p.read_csv("affairs.csv")

features = dataset.iloc[:,:-1].values
labels = dataset.iloc[:,-1].values
  
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
    
col_to_ohe = [6,7]  
ct = ColumnTransformer([("encoder", OneHotEncoder(), [6,7])], remainder = 'passthrough')
features = ct.fit_transform(features)
    
total_col, indexes = 0, []
for col in col_to_ohe:
        unique_val_count = len(dataset.iloc[:,col].value_counts())
        total_col += unique_val_count
        indexes.append(total_col - unique_val_count)
    
features = n.delete(features, indexes, axis=1)
    
from sklearn.model_selection import train_test_split as TTS
    
features_train,features_test,labels_train,labels_test = TTS(features, labels, test_size = 0.25,
                                        random_state = 0)
   
from sklearn.linear_model import LogisticRegression as L
classifier = L(max_iter=5000)
classifier.fit(features_train, labels_train)
    
pred = classifier.predict(features_test)   
  
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, pred)
    
   
mod_score = classifier.score(features_test, labels_test)
    
    
val = n.array([3, 25, 3, 1, 4, 16, 4, 2]).reshape(1,-1)
val = ct.transform(val)
val = n.delete(val, indexes, axis=1)
    
val_pred = classifier.predict_proba(val)  
    

    
pred,cm, mod_score,val_pred



print ("model accuracy using confusion matrix : "+str(cm))
print ("model accuracy using .score() function : "+str(round(mod_score*100,2)))
print ("percentage of total women actually had an affair : "+str(round(dataset["affair"].mean()*100,2))+"%")
print ("probability of an affair for a random woman is : "+str(val_pred))

