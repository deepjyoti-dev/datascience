
import pandas as p

import matplotlib.pyplot as plt

df = p.read_csv("Claims_Paid.csv")

df.dtypes

df.isnull().any(axis = 0)

features = df.iloc[:,0:1].values

labels = df.iloc[:,1:2].values

plt.scatter(features, labels)

from sklearn.linear_model import LinearRegression as L
obj = L()

obj.fit(features, labels)

obj.predict([[1981]])
#array([[106.03933333]])


plt.scatter(features, labels)
plt.plot(features, obj.predict(features), color = 'green')


from sklearn.preprocessing import PolynomialFeatures

features_higher_degree = PolynomialFeatures(degree = 5)

features_ndata = features_higher_degree.fit_transform(features)

regressor_ndata = L()


regressor_ndata.fit(features_ndata, labels)


plt.scatter(features, labels)
plt.plot(features, regressor_ndata.predict(features_higher_degree.transform(features)), color = 'green')


regressor_ndata.predict(features_higher_degree.transform([[1981]]))
#array([[148.44609171]])
