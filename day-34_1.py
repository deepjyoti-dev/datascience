
import pandas as pd

df = pd.read_csv('cars.csv')

from sklearn.model_selection import train_test_split as tt

d_train, d_test = tt(df, test_size = 0.4)

d_train.to_csv('dataset_train.csv', index = False)
d_test.to_csv("dataset_test.csv", index = False)

