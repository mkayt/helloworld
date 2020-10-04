# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 13:05:34 2020

@author: Kamran
"""

def hello(name):
    if name=='kamran':
        print('Hello kamran')
        return '1'
    else:
        print('invalid name')
        return '0'
print(hello('karan'))
import random as r
print(r.randint(1,100)) 
print(hello(r.randint(1,3))) 
def spam():
    print(x)
    print(x)
x='no'
spam()       
print(x)
import random as rd
num=rd.randint(1,10)
print('guess a number between 1 and 10')

for i in range(6):
    print('take a guess')
    gnum=int(input())
    if gnum<num:
        print('too low')
    elif gnum>num:
        print('too high')
    else:
        break
if gnum==num:
    print('correct guess.You have guessed in '+str(i)+' turns')
if i==6:
    print('lost game the correct answer is'+ str(num))
    
def collatz(n):
        if n%2 == 0:
            x=n//2
            print(x)
            return x
        else:
            x=3*n+1
            print(x)
            return x
print('enter a number')
try:
    n=int(input())
except:
    ValueError
    print('integer needed')    
y=n
while True:
        y=collatz(y)
        if y!=1:
            continue
        else:
            break
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    