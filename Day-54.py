# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 16:03:32 2023

@author: Nishant
"""
#TEXT MINING 
sentence="we are learning  TextMining from sanjivani AI"
sentence.index('learning')
#7 getting position of learning.
#this is going to show postion start from 0

sentence.split().index('TextMining')
#3 
#first splited into each word after that got the index.

sentence.split()[2][::-1]
#'gninrael' reverse of learning

sentence.split()[3][::-1]
#'gniniMtxeT' reverse of TextMining


words=sentence.split()
words
#['we', 'are', 'learning', 'TextMining', 'from', 'sanjivani', 'AI']


fw=words[0]#we
print(words[3])#TextMining
lw=words[-1]#AI
conc=fw + " " + lw
conc


[words[i] for i in range(len(words)) if i%2==0]
#['we', 'learning', 'from', 'AI']
#gettting only even no of words


sentence[-2::]
#'AI' charcter from rhs we will get


sentence[::-1]
#'IA inavijnas morf gniniMtxeT  gninrael era ew' 
#entire sentence in reverse order


print(" ".join(i[::-1] for i in words))
#'IA inavijnas morf gniniMtxeT  gninrael era ew'

#tokenization
import nltk

# Specify a custom download directory using a raw string
nltk.download('punkt', download_dir='C:\Datasets', quiet=True, halt_on_error=False, raise_on_error=False)


from nltk import word_tokenize
words=word_tokenize("i am reading nltk fundamentals")
print(words)


#part of speech
nltk.download('averaged_perceptron_tagger', download_dir='C:\Datasets', quiet=True, halt_on_error=False, raise_on_error=False)

nltk.pos_tag(words)

from nltk.corpus import stopwords
stop_words=stopwords.words('English')
stop_words
sentence1="i am learing nlp"

sentence_words=word_tokenize(sentence1)
sentence_words

sentence_no_stops=" ".join([words for word in sentence_words])


