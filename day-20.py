
import pandas as p

import numpy as n

df = p.read_csv('Baltimore.csv')


#1. Remove the dollar signs in the AnnualSalary field and assign it as a float

df['AnnualSalary'] = df['AnnualSalary'].astype(str)

df['AnnualSalary'] = df['AnnualSalary'].apply(lambda x: x.replace('$',''))

df['AnnualSalary'] = df['AnnualSalary'].astype(float)


group = df.groupby(['JobTitle'])['AnnualSalary']
aggregate = group.agg([n.sum, n.mean])

print(aggregate)



df['JobTitle'].value_counts()[0:10].plot(kind = 'bar')


a_name_id = df[['Agency','AgencyID']]
a_name_id.drop_duplicates(inplace=True)
print(a_name_id)

filter1 = df['GrossPay'].isnull()
len(df['GrossPay'][filter1])
#or below approach
df['GrossPay'].isnull().sum()




