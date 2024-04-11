# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 08:39:44 2023

@author: Nishant
"""
'''
#spam mail classification
#disadv of BoW and tfidf
#1 is they produce sparse matrix i.e. more no of zeros are present.
# 2 is as the size of words increase it increase the sparse size.
# similar sentences/words similar vectors : word embedding
#dense matrix: 300 fixed size


word embedding
# Word2vec n
eg: king - man + woman = Queen

#doc embedding

#senetence embedding



'''

#TF-IDF
#how to use TF-IDF

import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
#___________________________________________________________________________

corpus=['the mous had a long nose and eye','this is a vey big news for me','hello i am ging learn nlp form nowonwords','this is vey biggg thing for me']
#initialising countvector
cv=CountVectorizer()
#___________________________________________________________________________


#to count total no of TF
word_count_vector=cv.fit_transform(corpus)
word_count_vector.shape
#___________________________________________________________________________


#applyinhg IDF
tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
tfidf_transformer.fit(word_count_vector)
#___________________________________________________________________________



#this matrix is a row matrix so convert it into dataframe
df=pd.DataFrame(tfidf_transformer.idf_,index=cv.get_feature_names_out(),columns=['idf_weights'])
#___________________________________________________________________________



#sort ascending
df.sort_values(by=['idf_weights'])
#___________________________________________________________________________

'''
idf_weights
vey            1.510826
for            1.510826
me             1.510826
is             1.510826
this           1.510826
thing          1.916291
the            1.916291
nowonwords     1.916291
nose           1.916291
nlp            1.916291
news           1.916291
mous           1.916291
am             1.916291
hello          1.916291
had            1.916291
ging           1.916291
form           1.916291
eye            1.916291
biggg          1.916291
big            1.916291
and            1.916291
long           1.916291
learn          1.916291
'''

#___________________________________________________________________________


import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
#___________________________________________________________________________


corpus=[
        'Thar eating pizza,lakhi is eating buger',
        'apple is announcement new iphone tommarow',
        'tesla is is announsing a new pixel-6 tommarow',
        'microsoft is is announsing a new task-6 tommarow',
        'Amezpn is is announsing a new product tommarow',
        'I am a eating biryani and u are eating pizza',
        ]
#___________________________________________________________________________


#lets create the vectorizer anf fit the corpus and tranformer according to them
v=TfidfVectorizer()
v.fit(corpus)
transform_output=v.transform(corpus)
#lets print the vocabulary
print(v.vocabulary_)
#___________________________________________________________________________



'''
{'thar': 20, 'eating': 9, 'pizza': 16, 'lakhi': 12, 'is': 11, 
 'buger': 8, 'apple': 5, 'announcement': 3, 'new': 14, 'iphone': 10,
 'tommarow': 21, 'tesla': 19, 'announsing': 4, 'pixel': 15,
 'microsoft': 13, 'task': 18, 'amezpn': 1, 'product': 17, 
 'am': 0, 'biryani': 7, 'and': 2, 'are': 6}
'''
#___________________________________________________________________________

all_feature_names=v.get_feature_names_out()
for word in all_feature_names:
    indx=v.vocabulary_.get(word)
    idf_score=v.idf_[indx]
    
###############################################################
import pandas as pd
df=pd.read_csv("C:/NLP/Ecommerce_Data.csv")
df.shape

#checking the distrbution of label
df['label'].value_counts()
'''
Household                   6000
Electronics                 6000
Clothing & Accessories      6000
Books                       5999
 especially Christianity       1
Name: label, dtype: int64
'''
#add the new column which gives the unique to each of these label
df['label_num']=df['label'].map({
    'Household':0,
    'Books':1,
    'Electronics':2,
    'Clothing & Accessories':3
    })

#checking results
df.head(5)


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(
    df.Text,
    df.label_num,
    test_size=0.2,#20% of samples will go to the test dataset
    random_state=2022,
    stratify=df.label_num
    )

print("shape of x_train",x_train.shape)
print("shape of x_test",x_test.shape)



