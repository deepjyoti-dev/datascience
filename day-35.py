
import pandas as p


df = p.read_csv("Box_Office.csv")

feature = df.iloc[:, 0:1].values
l_bahubali = df.iloc[:, 1:2].values   
l_dangal = df.iloc[:, 2:3].values   



from sklearn.linear_model import LinearRegression as l

obj = l() 
obj.fit(feature, l_bahubali) 

obj1 = l() 
obj1.fit(feature, l_dangal)

day = 10

b_collection = obj.predict([[day]])


d_collection = obj1.predict([[day]])

if b_collection > d_collection:
 print ("Therefore, Bahubali 2 will earn more on the {0}th day".format(day))
else:
 print ("Therefore, Dangal will earn more on the {0}th day".format(day))
 
 
 
 
 
 
 
 
 
 