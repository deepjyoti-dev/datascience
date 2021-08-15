import pandas as p

df = p.read_csv("Salary_Classification.csv")


df.shape

df.columns

df.dtypes

df.isnull().any(axis = 0)

features = df.iloc[:,0:4].values
labels = df.iloc[:,-1].values

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

cTransformer = ColumnTransformer([('encoder', OneHotEncoder(), [0])], remainder ='passthrough' )

import numpy as np
features = np.array(cTransformer.fit_transform(features), dtype = np.float32)

features = features[:,1:]

from sklearn.model_selection import train_test_split


features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2)



from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

features_train = sc.fit_transform(features_train)

features_test = sc.transform(features_test)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

regressor.fit(features_train, labels_train)


pred = regressor.predict(features_test)



p.DataFrame(zip(pred, labels_test))


pred_train = regressor.predict(features_train)



p.DataFrame(zip(pred_train, labels_train))


regressor.score(features_train, labels_train)

regressor.score(features_test, labels_test)

x = ['Development',1100, 2, 3]

x = np.array(x)

x = x.reshape(1,4)

x = np.array(cTransformer.transform(x), dtype = np.float32)


x = x[:,1:]


regressor.predict(x)







#backward elimination
import statsmodels.api as sm

features = sm.add_constant(features)


features_optimal = features[:,[0,1,2,3,4,5]]

regressor_ols = sm.OLS(endog = labels, exog = features_optimal).fit()

regressor_ols.summary()

regressor_ols.pvalues

features_optimal = features[:,[0,1,3,4,5]]
regressor_ols = sm.OLS(endog = labels, exog = features_optimal).fit()


regressor_ols.summary()


features_optimal = features[:,[0,1,3,5]]
regressor_ols = sm.OLS(endog = labels, exog = features_optimal).fit()


regressor_ols.summary()


features_optimal = features[:,[0,3,5]]
regressor_ols = sm.OLS(endog = labels, exog = features_optimal).fit()



regressor_ols.summary()



features_optimal = features[:,[0,5]]
regressor_ols = sm.OLS(endog = labels, exog = features_optimal).fit()



regressor_ols.summary()





















