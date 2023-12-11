#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 00:49:42 2020

@author: cy
"""

def palindrome(num):
    cnt = 0
    for i in range((len(num)//2)+1):
        if num[i] == num[len(num)-i-1]:
            cnt +=1
    return cnt == (len(num)//2+1)

def palindrome2(num):
    return num == num[::-1]

print(palindrome(list('ABBAABBA')))