
import pandas as p

data = p.read_csv('cricket_salary_data.csv')

data.isnull().any(axis = 0)


features = data.iloc[:,0:3].values

labels = data.iloc[:,3].values

from sklearn.impute import SimpleImputer

from numpy import nan

imputer = SimpleImputer(missing_values = nan, strategy = 'mean')

features[:,1:2] = imputer.fit_transform(features[:,1:2])
