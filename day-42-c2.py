

import pandas as p


df= p.read_csv('IQ_Size.csv')

features = df.iloc[:, 1:].values
labels = df.iloc[:, 0].values

from sklearn.model_selection import train_test_split as tts
f_train, f_test, l_train, l_test = tts(features, labels, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LinearRegression as L
obj = L()
obj.fit(f_train, l_train)
obj.predict([[90,70,150]])
import statsmodels.api as sm

features = sm.add_constant(features)

features_sm = features[:,[0,1,2,3]]

est = sm.OLS(labels, features_sm)
est = est.fit()

print (est.summary())

features_sm = features[:, [0, 1, 2]]
est = sm.OLS(labels, features_sm)
est = est.fit()

print (est.summary())

features_sm = features[:, [1, 2]]
est = sm.OLS(labels, features_sm)
est = est.fit()

print (est.summary())

features_sm = features[:, [1]]
est = sm.OLS(labels, features_sm)
est = est.fit()

print (est.summary())

print ("Brain Size is the only factor which is more useful in predicting intelligence.")




