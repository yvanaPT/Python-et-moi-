# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 17:18:48 2022

@author: 3iL
"""

import random 

while True:
    x= int(input("cliquer sur 1 pour lancer et 0 pour quitter : "))
    
    if x== 0 : 
        print("A bientôt")
        break
    elif x==1 :
        print(random.randint(1,6))

    else : 
        print("Uniquement 0 ou 1 ")