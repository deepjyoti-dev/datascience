# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 07:19:41 2021

@author: deepj
"""
# Apriori

# Importing the libraries
import pandas as pd
from apyori import apriori

# Data Preprocessing
# Column names of the first row is missing, header - None
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)

print([str(dataset.values[1,j]) for j in range(0, 20) ])

#type(dataset.iloc[1,0]) is float
#type(dataset.iloc[1,3]) is float
#print([str(dataset.values[1,j]) for j in range(0, 20) ])
#print([str(dataset.values[1,j]) for j in range(0, 20) if (type(dataset.values[1,j]) is not float )])

transactions = []
for i in range(0, 7501):
    #transactions.append(str(dataset.iloc[i,:].values)) #need to check this one
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])


# Training Apriori on the dataset
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.25, min_lift = 4)

print(type(rules))

# next(rules)

"""
Shortcut to write a generator

q = (i**2 for i in [1,2,3,4,5])
print(type(q))
next(q)
p = list(q)
print(p)
"""


# Visualising the results
results = list(rules)
print(len(results))

results[0]
results[0].items
results[0][0]


results[0].support 
results[0][1]  #--> support


results[0].confidence
# at index = 2 we have ordered_statistics
results[0][2]
results[0][2][2]
results[0][2][0]
results[0][2][0][2]  #--> Confidence
results[0][2][0][3]  #--> Lift


for item in results:
    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")
