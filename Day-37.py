# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 08:16:31 2023

@author: Nishant
"""

'''
*****************Shallo copy and deep copy********************************
In Python, assignment statements (obj_bob) a) do not create real copies. 
It only creates a new variable with the same reference. 
So when you want to make actual copies of mutable objects (lists, dicts)
and want to modify the copy without affecting the original, 
you have to be careful.
For 'real copies we can use the copy module,
However, for compound/nested objects (e.g. nested lists or dicts)
and custom objects there is an 
**********Important difference between shallow and deep copying:********
    
*********** shallow copies **************************
    Only one level deep. 
It creates a new collection object and populates 
it with references to the nested objects. 
This means sodyfing a nested object in the copy deeper 
than one level affects the original. 
*********** deep copies ****************
     A full independent clone. 
It creates a new collection object and then 
recursively populates it with copies of the 
nested objects found in the original.
'''
#Assignment operation 
#This will only create a new variable with the same reference. 
#Modifying one will affect the other.

list_a = [1, 2, 3, 4, 51]
list_b=list_a
print(list_a)
print(list_b)
list_a[0] = -10 
print(list_a)
#[-10, 2, 3, 4, 51]
############################################################

#Shallow copy

#One level deep. Modifying on level 1 does not affect the other list.

#Use copy.copy(), or object-specific copy Functions/copy constructors.

import copy 
list_a=[1, 2, 3, 4, 51]
list_b = copy.copy(list_a)

#not affects the other 
list_a[0]= -10

print(list_a) 
print(list_b)
#[-10, 2, 3, 4, 51]
#[1, 2, 3, 4, 51]
###########################################################

#But with nested objects, modifying on level 2 or deeper does affect the other!

import copy 
list_a=[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
list_b=copy.copy(list_a)
# affects the other! 
list_a[0][0]=-10
print(list_a)
print(list_b) 
#[[-10, 2, 3, 4, 5], [6, 7, 8, 9, 10]] 
#[[10, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
#######################################################
#Deep copies
#Full independent clones. Use copy.deepcopy()

import copy 
list_a=[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
list_b = copy.deepcopy(list_a)

#not affects the other 
list_a[0][0]= -10

print(list_a) 
print(list_b)
#[-10, 2, 3, 4, 5], [6, 7, 8, 9, 10]] 
#[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]] 
