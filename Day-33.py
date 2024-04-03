# -*- coding: utf-8 -*-
"""
Created on Tuesdayy Jun  6 08:10:57 2023

@author: Dnyaneshwari...
"""
#regex101.com
#python for NLP
#extract,read pdf file
#pip install PyPDF2

# importing required modules 
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfReader

# creating a pdf reader object
reader = PdfReader('C:/1-Python/Vector Integration.pdf') 

#to get how many pages are in that pdf
print(len(reader.pages))#8
####################################################

#geting a sepecific page from pdf
page=reader.pages[2]

#extraction of page content
text=page.extract_text(2)
print(text)
##############################################
import re
chat2='Hi: I have a problem with my order number 77535423'
pattern = 'order[^\d]*(\d*)'
matches=re.findall(pattern, chat2)
print(matches) 
#['77535423']