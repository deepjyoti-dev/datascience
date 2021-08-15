import pandas as p

df=p.read_csv("student_scores.csv")
df.shape
df.columns.tolist()
df.isnull().any(axis=0)


features=df['Hours'].values
labels = df['Scores'].values

import matplotlib.pyplot as plt

plt.scatter(features,labels)

from sklearn.linear_model import LinearRegression as L

features=features.reshape(25,1)

obj=L()

obj.fit(features,labels)

m=obj.coef_
c=obj.intercept_

x=.498

print(m*x+c)

obj.predict([[14]])
pre = obj.predict(features)

plt.plot(features, pre)