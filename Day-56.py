# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 09:00:26 2023

@author: Dnyaneshwari...
"""
#BAg Of Words
#diff btw document and corpus
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
corpus=['At least seven indian pharma componies are working on develpoing vaccine against corona virus ','the deadly virus that has already been coming from china now has come to india','but our country bharat is now foghting agianst the corona virus with oour doctors']
bow=CountVectorizer()
print(bow.fit_transform(corpus).todense())
bow_df=pd.DataFrame(bow.fit_transform(corpus).todense())

bow_df.colums=sorted(bow.vocabulary_)
bow_df.head()
#here 36 columns
####################################

#bag of words model:small
#here 5 columns only
bow_small=CountVectorizer(max_features=5)
print(bow_small.fit_transform(corpus).todense())
bow_small_df=pd.DataFrame(bow_small.fit_transform(corpus).todense())

bow_small_df.colums=sorted(bow.vocabulary_)
bow_small_df.head()

