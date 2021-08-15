import pandas as p

ds = p.read_csv("Salary_Classification.csv")

ds.shape

ds.columns

ds.dtypes

ds.isnull().any(axis = 0)

features = ds.iloc[:,0:4].values
labels = ds.iloc[:,-1].values


from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

cTransformer = ColumnTransformer([('encoder', OneHotEncoder(), [0])], remainder ='passthrough' )

import numpy as np
features = np.array(cTransformer.fit_transform(features), dtype = np.float32)

features = features[:,1:]

from sklearn.model_selection import train_test_split


features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2)

from sklearn.linear_model import LinearRegression as l

obj = l()

obj.fit(features_train, labels_train)

pred = obj.predict(features_test)



pd.DataFrame(zip(pred, labels_test))


pred_train = regressor.predict(features_train)
