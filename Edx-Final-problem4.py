#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 15:25:51 2019

@author: janbieniek
"""
import operator

def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    if len(L1) != len(L2):
        return False
    if len(L1) == 0 and len(L2) == 0:
        return (None, None, None)
    
    dictL1 = {}
    dictL2 = {}
    
    for element in L1:
        if not element in dictL1:
            dictL1[element] = 1    
        else:
            dictL1[element] += 1
            
    for element in L2:
        if not element in dictL2:
            dictL2[element] = 1           
        else:
            dictL2[element] += 1
            
    if dictL1 != dictL2:
        return False
   
    max_value = 0
    
    for key in dictL1:
        if dictL1[key] > max_value:
            max_value = dictL1[key]
            
    mostCommon = ""
    
    for key in dictL1:
        if dictL1[key] == max_value:
            mostCommon = key
    
    return (mostCommon, max_value, type(mostCommon))
    
            
    