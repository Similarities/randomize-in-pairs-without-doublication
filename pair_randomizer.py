# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 15:14:00 2018

@author: similarities
"""

# random choices with pairs - without double counts

import random




listex = range(0,100)

liste_pairs = []

def randomizer(liste, liste_pairs):
    i=0
    liste1 = []
    liste1 = liste
    print(liste1,len(liste))
    
    while i < len(liste)/2+2:
        
        a = random.randint(0,len(liste1))-1
        
        pair1 = liste1[a]
        
        del liste1[a]
        
        b = random.randint(0,len(liste1))-1
        
        
        pair2 = liste1[b]
        
        liste_pairs.append([pair1, pair2])
        
        del liste1[b]
        
        i = i+1
    
    liste_pairs.append([liste1[0],liste1[1]])
    
    del (liste1[0],liste1[1])
    return liste_pairs
    
    
print(randomizer(listex, liste_pairs))
print listex





    
    