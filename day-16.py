import pandas as p

#print(dir(p))

df=p.read_csv('Salaries.csv')
print(type(df))

df.shape

df.head()

df.tail()
df.sample()

df['phd']
df['phd'].value_counts(normalize=True)

df[['rank','service']]

df['phd'].unique()

df['salary'].max()

df['salary'].min()
df['salary'].mean()