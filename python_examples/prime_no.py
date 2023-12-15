#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 01:53:42 2020

@author: cy
"""

def prime_no(num):
    if num < 2:
        return 'prime'
    for i in range(2,num//2+1):
        print(num % i, num, i)
        if num % i == 0:
            return 'not a prime'     
    return 'prime'

print(prime_no(4))

print([int(i) for i in list(str(124))])
