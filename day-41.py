import pandas as p
import numpy as n

df = p.read_csv('Salary_Classification.csv')
df.shape
df.columns
df.dtypes
df.isnull().any(axis = 0)
features = df.iloc[:,0:4].values
labels = df.iloc[:,-1].values

from sklearn.preprocessing import OneHotEncoder as O
from sklearn.compose import ColumnTransformer as col

cT = col([('encoder', O(), [0])], remainder ='passthrough' )


features = n.array(cT.fit_transform(features), dtype = n.float32)

features = features[:,1:]

import statsmodels.api as sm

features = sm.add_constant(features)

fo = features[:, [0,1,2,3,4,5]]

while (1):
    obj = sm.OLS(endog = labels,exog =fo).fit()
    p_v = obj.pvalues
    if p_v.max() > 0.05 :
        fo = n.delete(fo, p_v.argmax(),1)
    else:
        break
   
print (fo.shape)


