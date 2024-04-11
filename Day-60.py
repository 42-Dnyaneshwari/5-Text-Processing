# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 08:26:43 2023

@author: Nishant
"""

import gensim
import pandas as pd

df=pd.read_json("C:/Datasets/Cell_Phones_and_Accessories_5.json",lines=True)
df
df.shape#(194439, 9)

#simple preprocessing and tokenization
review_text=df.reviewText.apply(gensim.utils.simple_preprocess)
review_text
'''
0         [they, look, good, and, stick, good, just, don...
1         [these, stickers, work, like, the, review, say...
2         [these, are, awesome, and, make, my, phone, lo...
3         [item, arrived, in, great, time, and, was, in,...
4         [awesome, stays, on, and, looks, great, can, b...
                       
194434    [works, great, just, like, my, original, one, ...
194435    [great, product, great, packaging, high, quali...
194436    [this, is, great, cable, just, as, good, as, t...
194437    [really, like, it, becasue, it, works, well, w...
194438    [product, as, described, have, wasted, lot, of...
Name: reviewText, Length: 194439, dtype: object
'''
#check fist word of review
review_text.loc[0]
'''
['they',
 'look',
 'good',
 'and',
 'stick',
 'good',
 'just',
 'don',
 'like',
 'the',
 'rounded',
 'shape',
 'because',
 'was',
 'always',
 'bumping',
 'it',
 'and',
 'siri',
 'kept',
 'popping',
 'up',
 'and',
 'it',
 'was',
 'irritating',
 'just',
 'won',
 'buy',
 'product',
 'like',
 'this',
 'again']
'''
#get first row of dataframe
df.reviewText.loc[0]
'''
"They look good and stick good! 
I just don't like the rounded shape because 
I was always bumping it and Siri kept popping up and 
it was irritating. I just won't buy a product like this again"
'''

#
model=gensim.models.Word2Vec(
    window=10,
    min_count=2,
    workers=4)
'''
here window is how many words are u gong to consider as sliding window
u can choose any count min_count there must be 3 min 
words in each sentence
workers : no of thread
'''

#Build Vocabulary
model.build_vocab(review_text,progress_per=1000)

#train the model
model.train(review_text,total_examples=model.corpus_count,epochs=model.epochs)
#(61504536, 83868975)

#save the model
model.save('C:\Datasets\Cell_Phones_and_Accessories-reviews-short.model')


model.wv.most_similar('bad')

model.wv.similarity(w1='cheap',w2='inexpensive')
#0.5320099

model.wv.similarity(w1='bad',w2='good')
#0.587741

#_______________________________________________________________________#






