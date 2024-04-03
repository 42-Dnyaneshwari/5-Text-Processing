# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 08:17:34 2023

@author: Dnyaneshwari...
"""
import re
def get_pattern_match(pattern, text):
    matches = re.findall(pattern, text)
    if matches: 
        return matches

text=    '''
        Born Elon Reeve Musk
        June 28, 1971 (age 51)
        Pretoria, Transvaal, South Africa
        Education	University of Pennsylvania (BA, BS)
        Title	
        Founder, CEO and chief engineer of SpaceX
        CEO and product architect of Tesla, Inc.
        Owner, CTO and chairman of Twitter
        '''

def extract_personal_information(text):
    age = get_pattern_match('age (\d+)', text) 
    full_name = get_pattern_match('Born(.*)\n', text) 
    birth_date = get_pattern_match('Born.*\n(.*)\(age', text)
    #birth_date.strip()
    birth_place = get_pattern_match('\(age.*\n(.*)', text)
    #birth_place.strip()
    print('\nage', age)

    print('\nname', full_name)
        
    print('\nbirth_date', birth_date)
        
    print('\nbirth place', birth_place)
extract_personal_information(text)
'''
age : ['51']
name : [' Elon Reeve Musk']
birth_date : ['June 28, 1971 ']
birth place : ['Pretoria, Transvaal, South Africa']
'''
########################################################################


text='''
Born	Mukesh Dhirubhai Ambani
19 April 1957 (age 66)
Aden, Colony of Aden
(present-day Yemen)
Nationality	Indian
Alma mater	
St. Xavier's College, Mumbai
Institute of Chemical Technology (B.E.)
Occupation(s)	Chairman and MD, Reliance Industries
Spouse	Nita Ambani.
Children	3
Parent	
Dhirubhai Ambani (father)
Relatives	Anil Ambani (brother)
'''
age = get_pattern_match('age (\d+)', text) 
full_name = get_pattern_match('Born(.*)\n', text)
birth_date = get_pattern_match('Born.*\n(.*)\(age', text)
birth_place = get_pattern_match('\(age.*\n(.*)', text)
print('Age:',age)
print('Full Name:',full_name) 
print('Birth Date:',birth_date)
print('Birth Place:',birth_place)
'''
    OUTPUT:
Age: ['66']
Full Name: ['Mukesh Dhirubhai Ambani']
Birth Date: ['19 April 1957 ']
Birth Place: ['Aden, Colony of Aden']
'''
#######################################################################

#1. Extract all twitter handles from following text. 

text='''

Follow our leader Elon musk on twitter here: https://twitter.com/elonmusk, more information 
on Tesla's products can be found at https://www.tesla.com/. Also here are leading influencers 
for tesla related news,
https://twitter.com/teslarati
https://twitter.com/dummy_tesla
https://twitter.com/dummy_2_tesla

'''

pattern = 'https://twitter\.com/([a-zA-Z0-9_]+)'
re.findall(pattern,text)
#['elonmusk', 'teslarati', 'dummy_tesla', 'dummy2_tesla']
###########################################################################
#extract concentration of Risk. i.e. text after Concentration of Risk:
text='''

Concentration of Risk: Credit Risk 
Financial instruments that potentially subject us to a 
concentration of credit risk consist of cash, 
cash equivalents, marketable securities,
restricted cash, accounts receivable, 
convertible note hedges, and interest rate swaps. 
Concentration of Risk: Supply Risk 
Our cash balances are primarily invested in money 
market funds or on deposit at high credit quality financial 
institutions in the U.S. 
These deposits are typically in excess of insured limits. 
As of September 30, 2021 and December 31,

'''
pattern = 'Concentration of Risk: ([^\n]*)'
re.findall(pattern,text)
#['Credit Risk ', 'Supply Risk ']
#######################################################################

#Companies in europe reports their financial numbers of semi annual basis 
# and you can have a document like this. To exatract quarterly and semin ar 
#period you can use a regex as shown below
text ='''
 Tesla's gross cost of operating lease vehicles in FY2021 Q1 
 was $4.85 billion
 BMW's gross cost of operating vehicles in FY2021 S1 was $8 billion.
'''
pattern='FY(\d{4} (?:Q[1-4]|S[1-2]))'
re.findall(pattern, text)
#['2021 Q1', '2021 S1']
###################################################################
#extract phone numbers 
text='''

Elon musk's phone number is 9991116666, 
call him if Tesla's CFO number (999)-333-7777

'''

pattern='\(\d{3}\)-\d{3}-\d{4}|\d{10}'
re.findall(pattern, text) 
#['9991116666', '(999)-333-7777']
#######################################################################

text = '''
Note 1 - Overview
Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”) was incorporated in the State of Delaware on July 1, 2003. We design, develop, manufacture and sell high-performance fully electric vehicles and design, manufacture, install and sell solar energy generation and energy storage
products. Our Chief Executive Officer, as the chief operating decision maker (“CODM”), organizes our company, manages resource allocations and measures performance among two operating and reportable segments: (i) automotive and (ii) energy generation and storage.
Beginning in the first quarter of 2021, there has been a trend in many parts of the world of increasing availability and administration of vaccines
against COVID-19, as well as an easing of restrictions on social, business, travel and government activities and functions. On the other hand, infection
rates and regulations continue to fluctuate in various regions and there are ongoing global impacts resulting from the pandemic, including challenges
and increases in costs for logistics and supply chains, such as increased port congestion, intermittent supplier delays and a shortfall of semiconductor
supply. We have also previously been affected by temporary manufacturing closures, employment and compensation adjustments and impediments to
administrative activities supporting our product deliveries and deployments.
Note 2 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated balance sheet as of September 30, 2021, the consolidated statements of operations, the consolidated statements of
comprehensive income, the consolidated statements of redeemable noncontrolling interests and equity for the three and nine months ended September
30, 2021 and 2020 and the consolidated statements of cash flows for the nine months ended September 30, 2021 and 2020, as well as other information
disclosed in the accompanying notes, are unaudited. The consolidated balance sheet as of December 31, 2020 was derived from the audited
consolidated financial statements as of that date. The interim consolidated financial statements and the accompanying notes should be read in
conjunction with the annual consolidated financial statements and the accompanying notes contained in our Annual Report on Form 10-K for the year
ended December 31, 2020.
'''

pattern='Note \d - ([^\n]*)'
re.findall(pattern, text) 
#['Overview', 'Summary of Significant Accounting Policies']
########################################################################

#Extract financial periods from a company's financial reporting

text='''

The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.

In previous quarter 1.e. FY2028 Q4 it was $3 billion.
'''
pattern='FY\d{4} Q[1-4]'
re.findall(pattern, text) 
#['FY2021 Q1', 'FY2028 Q4']
####################################################################

#Case insensitive pattern match using flags

text='''
The gross cost of operating lease vehicles in FY2021 Q1In previous quarter i.e. 
fy2028 Q4 it was $3 billion. was $4.85 billion.
'''
pattern='FY\d{4} Q[1-4]'
matches = re.findall(pattern, text, flags=re.IGNORECASE)
matches
#['FY2021 Q1', 'fy2028 Q4']
########################################################################
#Extract only financial numbers

text ='''
Tesla's gross cost of operating lease vehicles in FY2021 01 was $4.85 61111
In previous quarter 1.e. FY2028 04 it was $3 billion.
'''
pattern='\$([0-9\.]+)'
re.findall(pattern, text) 
#['4.85', '3']
# #if we will put ([0-9\.]+), it will show all the digits, 
#but if will put \$([0-9\.]+) thentext after $ will get selected.
#############################################################
#TEXT PROCESSING IS OVER :)