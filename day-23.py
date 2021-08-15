

import pandas as pd
'''
#### read json and plot overall column

df_reader = pd.read_json('part.json', lines =  True)
json_df = df_reader['overall'].value_counts().head(5)

print(json_df)

json_df.plot.bar()



#######  read json and plot reviewText column

df_reader1 = pd.read_json('part.json', lines =  True)
json_df1 = df_reader1['reviewText'].value_counts().head(5)

print(json_df1)

json_df1.plot.bar()



#######


'''

#######  read json and plot summary column

df_reader2 = pd.read_json('part.json', lines =  True, chunksize=500 , dtype=int)
#json_df2 = df_reader2['summary'].value_counts().head(5)

#print(json_df2)

#json_df1.plot.bar()



#######



### 
                                                     ######
counter = 1
for i in df_reader2:
    print(i)
    print(len(i))
    new_df = pd.DataFrame(i["overall"])
    
    '''
    new_df1 = df_reader2[df_reader2['overall'] == 1].sample(40)
    new_df2 = df_reader2[df_reader2['overall'] == 2].sample(40)
    new_df3 = df_reader2[df_reader2['overall'] == 4].sample(40)
    new_df4 = df_reader2[df_reader2['overall'] == 5].sample(40)
    new_df5 = df_reader2[df_reader2['overall'] == 3].sample(80)
   
    new_df6 = pd.concat([new_df1, new_df2, new_df3, new_df4, new_df5], axis = 0,ignore_index = True)
   '''
    new_df.to_csv(str(counter)+'.csv', index = False)
    counter = counter+1
    new_df.plot.bar()
    
    
    ######

from glob import glob

filenames = glob('*.csv')

dataframes = []

for f in filenames:
    dataframes.append(pd.read_csv(f))

finaldf = pd.concat(dataframes, axis = 0, ignore_index = True)

finaldf.to_csv("balanced_reviews_1.csv", index = False)


df = pd.read_csv('balanced_reviews_1.csv')




