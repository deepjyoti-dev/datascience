import pandas as p

df=p.read_csv('Salaries.csv')

df.columns

df.columns.tolist()

df['salary']
df['salary'] >100000

df[(df['salary'] > 10000) & (df['sex'] == 'Female')]

filter1=df['salary'] > 100000

df[filter1]

df.isnull()

df.isnull().any(axis=0)  #column wise
df.isnull().any(axis=1) #row wise
df[df.isnull().any(axis=1)]   #rowwise not column wise


df['phd'].mean()

df['phd']=df['phd'].fillna(df['phd'].mean())  #add mean value to the nan in phd column

df2=df.fillna(100)  # add 100 to all the nan in the whole data frame

df.dropna(inplace = True)  # row with missing data nan are deleted 
df=p.read_csv('Salaries.csv')
df.iloc[0:10,2:4]  #0:10 row selection and 2:4 are column selection but 2:4-1

df.iloc[10,:]  # only row 10 and all columns

df.iloc[[10,15],:]  # row 10 and 15 and all columns

df.iloc[:,2]  # all row but only 2 column 