
import numpy as n
import pandas as p


df = p.read_csv('Female_Stats.csv')


features = df.iloc[:,1:].values
labels = df.iloc[:, [0]].values

df.isnull().any(axis=0)


from sklearn.model_selection import train_test_split as tts

f_train, f_test, l_train, labels_test = tts(features, labels, test_size = 0.2, random_state = 0)


from sklearn.linear_model import LinearRegression as L
obj = L()
obj.fit(f_train, l_train)

Pred = obj.predict(f_test)

print (p.DataFrame(zip(n.round(Pred,2), labels_test)))
import statsmodels.api as sm

features_sm = sm.add_constant(features)
est = sm.OLS(labels, features_sm)
est2 = est.fit()

print (est2.summary())

print (obj.coef_[0][0])

print (obj.coef_[0][1])


























# Version 2 of solution 


