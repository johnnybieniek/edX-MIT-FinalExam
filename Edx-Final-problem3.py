#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 15:21:18 2019

@author: janbieniek
"""

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    sum = 0
    
    for number in range(1,k+1):
        sum += number
        if sum == k:
            return True
        if sum > k:
            return False