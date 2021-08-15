import pandas as pd
dataframe = pd.read_csv('titanic.csv')


disaster_survived = dataframe['Survived'].value_counts()[1]
print(str(disaster_survived) + " People Survived")


disaster_died = dataframe['Survived'].value_counts()[0]
print(str(disaster_died)  + " People Died")


disaster_survived_percentage = dataframe['Survived'].value_counts(normalize=True)[1]
print(str(round(float(disaster_survived_percentage)*100,2)) + "% People Survived")

disaster_died_percentage = dataframe['Survived'].value_counts(normalize=True)[0]
print(str(round(float(disaster_died_percentage)*100,2)) + "% People Died")


m_survived = dataframe['Survived'][dataframe['Sex'] == 'male'].value_counts(normalize=True)[1]
m_passed_away =  dataframe['Survived'][dataframe['Sex'] == 'male'].value_counts(normalize=True)[0]
print ("Total_male_survived : "+str(round(m_survived*100,2))+"%")
print ("Total_male_passed_away : "+str(round(m_passed_away*100,2))+"%")

f_survived = dataframe['Survived'][dataframe['Sex'] == 'female'].value_counts(normalize=True)[1]
f_passed_away =  dataframe['Survived'][dataframe['Sex'] == 'female'].value_counts(normalize=True)[0]
print ("Total_female_survived : "+str(round(f_survived*100,2))+"%")
print ("Total_female_passed_away : "+str(round(f_passed_away*100,2))+"%")

def filter_data(value):
    if 0 <= value <= 18:
        return 1
    else:
        return 0


dataframe['Child'] = dataframe['Age'].apply(filter_data)
c =  dataframe['Survived'][dataframe['Child'] == 1].value_counts(normalize=True)
print ("Child Survived : "+str(round(c[1]*100, 2))+"%")



