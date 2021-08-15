
import pandas as p


df = p.read_csv("Foodtruck.csv")


features = df.iloc[:,0:1].values
labels = df.iloc[:,1:2].values

from sklearn.model_selection import train_test_split as tt
f_train, f_test, l_train, l_test = tt(features, labels, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LinearRegression as l

obj = l()

obj.fit(f_train, l_train)

obj.predict([[0.57]])
obj.predict([[5.32]])

obj.predict([[89.32]])