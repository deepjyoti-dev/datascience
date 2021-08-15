import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv('Automobile.csv')


dataframe['price'].dtype

dataframe["price"] = dataframe["price"].astype(float)


dataframe['price'].isnull().any(axis = 0)

dataframe["price"] = dataframe["price"].fillna(dataframe["price"].mean())

p_array = dataframe["price"].values

print (dataframe["price"].min())
print ( dataframe["price"].max())
print (  round( dataframe["price"].mean(), 2 ))
print ( round( dataframe["price"].std(), 2 ) ) 


series = dataframe["make"].value_counts()

topCarMakers = series.index[0:11]
vehicleCount = series.values[0:11]

plt.pie(vehicleCount, labels=topCarMakers, autopct='%.2f%%')

plt.show()

