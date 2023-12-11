#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 00:00:04 2020

@author: cy
"""

def factorial_using_recursion(num):
    return num*factorial_using_recursion(num-1) if num > 1 else 1

def factorial_using_for(num):
    rtn = 1
    for i in range(num):
        rtn = rtn * (i+1)
    return rtn

print(factorial_using_recursion(5))
print(factorial_using_for(4))