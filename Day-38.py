# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 08:24:19 2023

@author: Nishant
"""
import unicodedata
#UTF-unicodedata transformation format
'''
it means 8 bit value are used in the encoding
it is one of the most convient and efficient encoding formats
among various encoding formats
'''

s1='apple'
s2='happy3'
s3='shine54'
s4='greps89'
s1.encode(encoding='UTF-8',errors='strict')#b'apple'
s2.encode(encoding='UTF-8',errors='strict')#b'happy3'
s3.encode(encoding='UTF-8',errors='strict')#b'shine54'
s4.encode(encoding='UTF-8',errors='strict')#b'greps89'
#########################################################
'''
ENCODE:-
we encode the strings into a byte using the utf-8 encoding
'''
text='one 🐘 and three 🐋'
print(text)#one 🐘 and three 🐋
print(len(text))#17
a=text.encode('utf-8')
print(a)#b'one \xf0\x9f\x90\x98 and three \xf0\x9f\x90\x8b'
print(len(a))#23
#################################################################
'''
DECODE:-
'''
f1=open('C:/1-Python/data.txt','rb')
content=f1.read()
print(content)#b'one \xf0\x9f\x90\x98 and three \xf0\x9f\x90\x8b'
print(type(content))#<class 'bytes'>
print(content.decode('utf-8'))#one 🐘 and three 🐋
#########################################################
import unicodedata
