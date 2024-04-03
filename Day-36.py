# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 08:14:41 2023

@author: Dnyaneshwari...
"""
#PYTHON DECORATORS
#PREREQUISIT TO PYTHON DECORATERS
#Define a funtion
def plus_one(number):
        number=number+1 
        return number
plus_one(5)
#6 
#######################################################
#Defining Functions Inside other Functions 
def plus_one(number):
    def add_one(number): 
        number1=number+1 
        return number1
    result=add_one(number) 
    return result
plus_one(4)
#output : 5
#####################################################################
#passing funtion as a arguments
def plus_one(number):
        res1=number+1 
        return res1
def fun_call(funtion):
    res=funtion(5)  
    return res
fun_call(plus_one)
#output : 6
######################################################################
#Funtion returning other funtion
def hello_fun():
    def say_hi():
        return 'Hii'
    return say_hi
#hello_fun()#without assigning to variable
hello=hello_fun() #assign it to the variable.
hello()#then calling the variable.
#output : 'Hii'
#always remember when you call hello_fun() as it is a funtion.
#so we can not  call it.
#so assign it to the variable so we assign to hello.
#after that we have to call that variable so we call hello().
####################################################################
#a python decoraters is a funtion 
#that takes a funtion and
#returns it by adding some funtionality.
def say_hi():
    return 'hello Dnyaneshwari'
def uppercase_decorator(function): 
    def wrapper():
        func=function() 
        make_uppercase = func.upper() 
        return make_uppercase
    return wrapper
decorate=uppercase_decorator(say_hi)
decorate()
#output : 'HELLO DNYANESHWARI'
#######################################################################

#however we use that vaiable to use decoraters
#so we use @symbol instead of taking variable.
#before taking funtion name.
@uppercase_decorator
def say_hi():
    return 'hello Dnyaneshwari'
say_hi()
#output : 'HELLO DNYANESHWARI'
#########################################################################
#applying multiple decoraters to a single funtion
#we can use this
#to a Single Function
#We can use multiple decorators
#to a single function. However, 
#the decorators will be applied in the order
# that we've called them.
def split_string(function):
     def wrapper(): 
         func = function()
         splitted_string = func.split()
         return splitted_string
     return wrapper
@split_string
@uppercase_decorator
def say_hi():
    return 'hello Dnyaneshwari'
say_hi()
#output : ['HELLO', 'DNYANESHWARI']
##################################################################
numbers=[2,6,7,8]
def cal_square(numbers):
    result=[]
    for i in numbers: 
        result.append(i*i)
    return result
def cal_cube(numbers):
    result=[]
    for i in numbers:
        result.append(i*i*i) 
    return result
print(cal_square(numbers))#[4, 36, 49, 64]
print(cal_cube(numbers))#[8, 216, 343, 512]
#######################################################################
import time
def cal_square(numbers):
    start=time.time()
    result=[]
    for i in numbers: 
        result.append(i*i)
    end=time.time()
    #print((end-start)*1000)
    print("took "+str((end-start)*1000)+' mil sec')
    return result
#############################
def cal_cube(numbers):
    start=time.time()
    result=[]
    for i in numbers:
        result.append(i*i*i) 
    end=time.time()
    #print((end-start)*1000)
    print("took "+str((end-start)*1000)+' mil sec')
    return result
################################################
array=range(1,100000)
out_square=cal_square(array)#took 31.263351440429688 mil sec
out_cube=cal_cube(array)#took 31.25452995300293 mil sec
##################################################################
import time
def time_it(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        #print((end-start)*1000)
        print("took "+str((end-start)*1000)+' mil sec')
        return result
    return wrapper
@time_it
def cal_square(numbers):
    result=[]
    for i in numbers: 
        result.append(i*i)
    return result
def cal_cube(numbers):
    result=[]
    for i in numbers:
        result.append(i*i*i) 
    return result
array=range(1,100000)
out_square=cal_square(array)#took 16.03245735168457 mil sec
out_cube=cal_cube(array)#took 17.765522003173828 mil sec
################################################################


