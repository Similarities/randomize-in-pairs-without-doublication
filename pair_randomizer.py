# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 15:14:00 2018

@author: similarities
"""

# random choices with pairs - without double counts

import random




liste = [0,1,2,3,4,5,6,7,8,9]

liste_pairs = []

def randomizer(liste, liste_pairs):
    i=0
    
    while i < 4:
        
        a = random.randint(0,len(liste))-1
        
        pair1 = liste[a]
        
        del liste[a]
        
        b = random.randint(0,len(liste))
        
        pair2 = liste[b]
        
        liste_pairs.append([pair1, pair2])
        
        del liste[b]
        
        i = i+1
    
    liste_pairs.append([liste[0],liste[1]])
    return liste_pairs
    
    
print(randomizer(liste, liste_pairs))


    
    