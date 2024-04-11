# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 08:25:48 2023

@author: Nishant
"""
import nltk
from nltk import word_tokenize

nltk.download('maxent_ne_chunker')
nltk.download("words")
sentences="we are learning NLP by sanjivani AI"

words=word_tokenize(sentences)
words=nltk.pos_tag(words)
i=nltk.ne_chunk(words,binary=True)
[a for a in i if len(a)==1]
################################



import re
sen="shared twitting ,wittnessing 70th republic day of india"
re.sub(r'([^\s\w]|_)+',' ',sen).split()
#['shared', 'twitting', 'wittnessing', '70th', 'republic', 'day', 'of', 'india']

#n-gram

def n_gram_extract(input_str,n):
    tokens=re.sub(r'([^\s\w]|_)+',' ',input_str).split()
    for i in range(len(tokens)-n+1):
        print(tokens[i:i+n])
        
       
n_gram_extract("the cute little boy is playing with kittens",2)#digram tokenization 
'''
['the', 'cute']
['cute', 'little']
['little', 'boy']
['boy', 'is']
['is', 'playing']
['playing', 'with']
['with', 'kittens']
'''
n_gram_extract("the cute little boy is playing with kittens",3)#trigram tokenization    
'''
['the', 'cute', 'little']
['cute', 'little', 'boy']
['little', 'boy', 'is']
['boy', 'is', 'playing']
['is', 'playing', 'with']
['playing', 'with', 'kittens']
'''  

#################################################################

from nltk import ngrams

list(ngrams("the cute little boy is playing with kittens".split(),2))#digram tokenization
'''
[('the', 'cute'),
 ('cute', 'little'),
 ('little', 'boy'),
 ('boy', 'is'),
 ('is', 'playing'),
 ('playing', 'with'),
 ('with', 'kittens')]
''' 
list(ngrams("the cute little boy is playing with kittens".split(),3))#trigram tokenization    
'''
[('the', 'cute', 'little'),
 ('cute', 'little', 'boy'),
 ('little', 'boy', 'is'),
 ('boy', 'is', 'playing'),
 ('is', 'playing', 'with'),
 ('playing', 'with', 'kittens')]
'''
######################################################################

from textblob import TextBlob

blob=TextBlob("the cute little boy is playing with kittens")
blob.ngrams(n=2)
blob.ngrams(n=3)



####################################################################

from keras.preprocessing.text import text_to_word_sequence
text_to_word_sequence(sentences)

###############################################################


from textblob import TextBlob
blob=TextBlob(sentences)
blob.words

######################################################

#TweetTokenizer

from nltk.tokenize import TweetTokenizer
tweet_tokenizer=TweetTokenizer()
tweet_tokenizer.tokenize(sentences)

######################################

#MWETokenizer

from nltk.tokenize import MWETokenizer
mwe_tokenizer=MWETokenizer([('republic','day')])
mwe_tokenizer.tokenize(sentences.split())
mwe_tokenizer.tokenize(sentences.replace('i'," ").split())

######################################

#RegexpTokenizer

from nltk.tokenize import RegexpTokenizer
regex_tokenize=RegexpTokenizer('\w+|\$[\d\.]+|\S+')
#the pattern means 
'''
1st Alternative \w+
\w matches any word character (equivalent to [a-zA-Z0-9_])
+ matches the previous token between one and unlimited times, as many times as possible, giving back as needed (greedy)
2nd Alternative \$[\d\.]+
\$ matches the character $ with index 3610 (2416 or 448) literally (case sensitive)
Match a single character present in the list below [\d\.]
+ matches the previous token between one and unlimited times, as many times as possible, giving back as needed (greedy)
\d matches a digit (equivalent to [0-9])
\. matches the character . with index 4610 (2E16 or 568) literally (case sensitive)
3rd Alternative \S+
\S matches any non-whitespace character (equivalent to [^\r\n\t\f\v ])
+ matches the previous token between one and unlimited times, as many times as possible, giving back as needed (greedys
'''
regex_tokenize.tokenize(sentences)

##########################################################

#white space tokenizer

from nltk.tokenize import WhitespaceTokenizer
ws_tokenizer=WhitespaceTokenizer()
ws_tokenizer.tokenize(sentences)

################################################

#WordPunctTokenizer

from nltk.tokenize import WordPunctTokenizer
wp_tokenizer=WordPunctTokenizer()
wp_tokenizer.tokenize(sentences)

#############################################

sentences="i love playing cricket.criket players practices in"
from nltk.stem import RegexpStemmer
rs=RegexpStemmer('ing$')#removing ing
" ".join(rs.stem(wd)for wd in sentences.split())
#'i love play cricket.criket players practices in'


################################################

from nltk.stem.porter import PorterStemmer
ps_stemmer=PorterStemmer()#removing ing
words=sentences.split()
" ".join(ps_stemmer.stem(wd)for wd in words)
#'i love play cricket.criket player practic in'

#######################################################


import nltk
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenizer
nltk.download('wordnet')
lemmatizer=WordNetLemmatizer()
sentences="the codes executed today are for better that want"
words=word_tokenize(sentences)
" ".join(lemmatizer.lemmatize(words)for word in words)

#########################################################

from textblob import TextBlob
sentences=TextBlob("she snells seachells an the seashare")
words=sentences.words
sentences.words[2].singularize()
sentences.words[5].plularize()

########################################################

from textblob import TextBlob
en_blob=TextBlob(u'muy bien')
en_blob.translate(from_lang='es',to='en')
#TextBlob("very good")

##########################################################

from nltk import word_tokenize
sentences=TextBlob("she snells seachells an the seashare")
csl=['she','is','is','an','the']
words=word_tokenize(sentences)
" ".join([word for word in words if word.lower() 
         not in csl])
#select words which are not defied in the given list

#################################################

import pandas as pd

df=pd.DataFrame(['the codive vaicine is disrtibuted in every one'],['hiii every one i know u dont know me so uue '],['all the the students of sanjivani take a change that'])
df.columns=['text']
df
###############################################

from textblob import TextBlob
df['number_of_words']=df['text'].apply(lambda x:len(TextBlob(x).words))
df['number_of_words']

######################################################

df_words=set(['why','who','which','what','where','how'])
df['words']=df['text'].apply(lambda x:True if len(set(TextBlob(x).words)) else False)
df['words']

#BOOK-NLP: 
















