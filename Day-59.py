# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 08:21:15 2023

@author: Dnyaneshwari....
"""

#Word Embedding

#sampling technique: 2020,2021,2022.....
#assign the oarticukar number to each sample

#________________________________________________________________________
import pandas as pd
df=pd.read_csv("C:/NLP/Ecommerce_Data.csv")
print(df.shape)
df.head(5)

#check the distribution labels
df['label'].value_counts()

#add the new column gives a unique to each other of these lab

df['label_num'] =df['label'].map({
    'Household':0,
    'Books':1,
    'Electronics':2,
    'Clothing & Accessories':3
    
    })
#checking the result
df.head(5)

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(
    df.Text,
    df.label_num,
    test_size=0.2, #20% samples will go to test datasets
    random_state=2022,
    stratify=df.label_num ##Stratify = convert imbalanced data to balanced data 

    )

print('Shape of x_train:',x_train.shape)
print('shape of x_test:',x_test.shape)

y_train.value_counts()
x_train.value_counts()

################


#___________________________________________________________________
#apply the classifier

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

#___________________________________________________________________


#1. create a pipeline object
clf=Pipeline([
    ('vecorizer_tfidf',TfidfVectorizer(),
     ('KNN',KNeighborsClassifier()))])


#2. fit with x_train,x_test
clf.fit(x_train,y_train)


#3. getting the prediction for x_test and store itin y_pred
y_pred=clf.predict(x_test)