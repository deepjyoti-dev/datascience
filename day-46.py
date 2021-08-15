
import numpy as n
import matplotlib.pyplot as pt
import pandas as p

dataset = p.read_csv('bluegills.csv')
features = dataset.iloc[:, 0:1].values
labels = dataset.iloc[:, 1].values

from sklearn.linear_model import LinearRegression as L
obj = L()
obj.fit(features, labels)

f_grid = n.arange(min(features), max(features), 0.2)
f_grid = f_grid.reshape(len(f_grid), 1)
pt.scatter(features, labels, color = 'orange')
pt.plot(f_grid, obj.predict(f_grid), color = 'green')
pt.title('Bluegill (Linear Regression)')
pt.xlabel('Age')
pt.ylabel('Length')
pt.show()

from sklearn.preprocessing import PolynomialFeatures as pf
higher_degree_gen = pf(degree = 2)
f_poly = higher_degree_gen.fit_transform(features)
obj2 = L()
obj2.fit(f_poly, labels)

features_grid = n.arange(min(features), max(features), 0.1)
features_grid = features_grid.reshape(len(features_grid), 1)
pt.scatter(features, labels, color = 'blue')
pt.plot(features_grid, obj2.predict(higher_degree_gen.fit_transform(features_grid)), color = 'yellow')
pt.title('Bluegill (Linear Regression)')
pt.xlabel('Age')
pt.ylabel('Length')
pt.show()

print ("Predicting result with Linear Regression :"+str(obj.predict([[5]])))


print ("Predicting result with Polynomial Regression :"+str(obj2.predict(higher_degree_gen.fit_transform([[5]]))))






