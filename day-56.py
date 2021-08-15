

import pandas as pd


dataset = pd.read_csv('movie.csv')


import re
import nltk

nltk.download('stopwords')
    
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


corpus = []
for i in range(0, dataset.shape[0]):
    review = re.sub('[^a-zA-Z]', ' ', dataset['text'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)


from sklearn.feature_extraction.text import CountVectorizer as CV
cv = CV(max_features = 4000)
features = cv.fit_transform(corpus).toarray()

labels = dataset.iloc[:, 0].values


from sklearn.preprocessing import LabelEncoder  as LE
le = LE()
labels = le.fit_transform(labels)


from sklearn.model_selection import train_test_split as TTS
features_train, features_test, labels_train, labels_test = TTS(features, labels, test_size = 0.25, random_state = 0)

from sklearn.linear_model import LogisticRegression as LR

model  = LR(max_iter=4000)

model.fit(features_train, labels_train)


labels_pred = model.predict(features_test)


from sklearn.metrics import confusion_matrix,accuracy_score
cm = confusion_matrix(labels_test, labels_pred)

score = accuracy_score(labels_test,labels_pred)

print ("Accuracy is : "+str(round(score*100, 2))+"%")