
import re
from glob import glob as g
import pandas as p


f_names = g('baby_names/*.txt')
    
ssa_df_list = []

for file in f_names:
    t_df = p.read_csv(file, names = ['names','sex','count'])
    
    year = int(re.findall('\d\d\d\d', file)[0])
    
    if year > 2010: 
        break

     
    t_df['year'] = year
   
    ssa_df_list.append(t_df)


finaldf = p.concat(ssa_df_list, axis = 0, ignore_index = True)


df_2010 = finaldf[finaldf['year'] ==  2010]

female_names = df_2010[df_2010['sex'] == 'F']

female_names_sort_by_count = female_names.sort_values('count', ascending = False, ignore_index = True)

print (female_names_sort_by_count['names'][0:5]) 

male_names = df_2010[df_2010['sex'] == 'M']

male_names_sort_by_count = male_names.sort_values('count', ascending = False, ignore_index = True)

print (male_names_sort_by_count['names'][0:5]) 


grouped_multiple = finaldf.groupby(['year', 'sex']).agg({'count': ['sum']})

print(grouped_multiple)



grouped_multiple.plot(kind='bar')

grouped_multiple[0:10].plot(kind='bar')







