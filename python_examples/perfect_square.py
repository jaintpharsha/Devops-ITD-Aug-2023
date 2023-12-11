#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 01:40:32 2020

@author: cy
"""
from math import sqrt

def perfect_square(num):
    return int(sqrt(num)) == sqrt(num)

print(perfect_square(36))

def sqrs_btn_numbers(a,b):
    sqrs = []
    for i in range (a,b+1):
        if perfect_square(i):
            sqrs.append(i)
    return sqrs

print(sqrs_btn_numbers(9,100))