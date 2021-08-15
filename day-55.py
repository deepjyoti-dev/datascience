

import pandas as pd

df =  pd.read_csv('balanced_reviews.csv')



df.isnull().any(axis = 0)

#handle the missing data
df.dropna(inplace =  True)

#leaving the reviews with rating 3 and collect reviews with
#rating 1, 2, 4 and 5 onyl

df = df [df['overall'] != 3]

import numpy as np

#creating a label
#based on the values in overall column
df['Positivity'] = np.where(df['overall'] > 3 , 1 , 0)

#NLP
#reviewText - feature - df['reviewText']
#Positivity - label - df['Positivity']

#df['reviewText'][0]
#df.iloc[0,1]


import nltk
import re
nltk.download('stopwords')

from nltk.stem.porter import PorterStemmer

from nltk.corpus import stopwords

corpus = []
for i in range(0,df.shape[0]):
    review = re.sub('[^a-zA-Z]', ' ' , df.iloc[i,1])
    review = review.lower()
    
    review = review.split()
    
    #remove the stopwords
    review = [word for word in review if not word in stopwords.words('english')]
    
    #stemming
    ps = PorterStemmer()
    
    review = [ps.stem(word) for word in review]
    
    review = " ".join(review)
    corpus.append(review)


#features - corpus
#label -  df.iloc[:,-1]
    
from sklearn.feature_extraction.text import CountVectorizer

features_vectorized = CountVectorizer().fit_transform(corpus)

#fit - prepare the vocabulary
#transform - create so many columns, fill that matrix

labels = df.iloc[:,-1]

#train test split
#import class
#create object
#fit
#evaluate







