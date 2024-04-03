# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 08:22:31 2023

@author: Dnyaneshwari...
"""

import re
text1="My mobile no is 7864321891"
text2="My alternate mobile no is 9887653407"
text3="My international mobile no is (123)-456-789"
#select digit of 10 number
pat1='\d{10}'
re.findall(pat1,text1) #['7864321891']
#####################################################################3
pat2='\(\d{3}\)-\d{3}-\d{3}'
re.findall(pat2,text3) #['(123)-456-789']
#or
text3="My international mobile no is 123-456-789"
digits = re.findall(r"\d", text3)
digits
mob_no = ''.join(digits)
print(mob_no)
#######################################################################

import re
pat=r'[a-z]*\.[a-z]*@[a-z]*\.org.in'
text="My EmailID is dnyaneshwari.dolzake@sanjivani.org.in"
re.findall(pat,text)#dnyaneshwari.dolzake@sanjivani.org.in

########################################################

import re
pat3=r'[0-9a-z]*@[a-z]*\.com'
text="My EmailID is 32dnyaneshwaridolzake@gmail.com"
re.findall(pat3,text)#32dnyaneshwaridolzake@gmail.com

########################################################

import re
pat4=r'order[^\d]*\d*'
text1="hii my order #68787877 is not received"
re.findall(pat4,text1) #['order #68787877']

#########################################################

pat5=r'order[^\d]*(\d*)'
text2="hie, i have problem with orderno 7547537"
re.findall(pat5,text2)#['7547537']

###############################################################

chat1='hie, i have problem with orderno 7547537'
chat1 = 'Hi: you ask lot of questions 1235678912, abc@xyz.com'
chat2 = 'Hi: here it is: (123)-567-8912, abc@xyz.com?' 
chat3 = 'Hi: yes, phone: 1235678912 email: abc@xyz.com'


def get_pattern_match(pattern, text):
    matches = re.findall(pattern, text)
    if matches: 
        return matches
get_pattern_match('order[^\d]*(\d*)', chat1)
#['7547537']

get_pattern_match('[a-zA-Z0-9_]+@[a-z]*\.[a-zA-Z0-9]*', chat1)


get_pattern_match('[a-zA-Z0-9_] @[a-z]*\.[a-zA-Z0-9]*', chat2)

get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*', chat3)
                  

################################################################
txt=    '''
        Born Elon Reeve Musk
        June 28, 1971 (age 51)
        Pretoria, Transvaal, South Africa
        Education	University of Pennsylvania (BA, BS)
        Title	
        Founder, CEO and chief engineer of SpaceX
        CEO and product architect of Tesla, Inc.
        Owner, CTO and chairman of Twitter
        '''
import re
def get_pattern_match(pattern, text):
    matches = re.findall(pattern, text)
    if matches: 
        return matches
get_pattern_match((r'age (\d+)'), txt)
#['51']
##########################################################

#.* to select all after Born 
match=get_pattern_match((r'Born(.*)'), txt)
match[0].strip()
#'Elon Reeve Musk'
###################################################3

#1 Way
match=get_pattern_match((r'Born.*\n(.*)'), txt)
match[0].strip()
#'June 28, 1971 (age 51)'

#2 Way
get_pattern_match((r'[a-zA-Z]*.[0-9]*.\s\d{4}\s*.[a-z0-9].*'), txt)
#['June 28, 1971 (age 51)']
########################################################
#1 Way
match=get_pattern_match((r'Born.*\n(.*)\(age'), txt)
match[0].strip()
#'June 28, 1971'
#2 Way
get_pattern_match((r'[a-zA-Z]*.[0-9]*.\s\d{4}'), txt)
#['June 28, 1971']
#############################################################

match=get_pattern_match((r'\(age.*\n(.*)'), txt)
match[0].strip()
#'Pretoria, Transvaal, South Africa'

################################################################
