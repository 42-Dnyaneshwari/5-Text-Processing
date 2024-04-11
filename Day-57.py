# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 08:47:13 2023

@author: Dnyaneshwari
"""

import pandas as pd
import numpy as np


df=pd.read_csv('C:/NLP/spam.csv')
df.columns
df.head()


df.Category.value_counts()


df['spam']=df['Category'].apply(lambda x:1 if x=='spam' else 0)
df.shape
#(5572, 3)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(df.Message,df.spam,test_size=0.2)
x_train.shape
#(4457,)
x_test.shape
#(1115,)


print(type(x_test))
print(type(x_train))
#<class 'pandas.core.series.Series'>


from sklearn.feature_extraction.text import CountVectorizer
v=CountVectorizer()
x_train_cv=v.fit_transform(x_train.values)
x_train_cv.shape
#(4457, 7795)


from sklearn.naive_bayes import MultinomialNB
model=MultinomialNB()
model.fit(x_train_cv,y_train)

x_test_cv=v.transform(x_test)


from sklearn.metrics import classification_report
y_pred=model.predict(x_test_cv)
print(classification_report(y_test,y_pred))
'''
#Model is overfitted
 precision    recall  f1-score   support

           0       0.99      1.00      0.99       975
           1       0.98      0.94      0.96       140

    accuracy                           0.99      1115
   macro avg       0.98      0.97      0.98      1115
weighted avg       0.99      0.99      0.99      1115
'''










 