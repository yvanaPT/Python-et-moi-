# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 18:05:14 2022
deviner le nombre choisi par l'ordinateur'
@author: Yvana Tchamgoue
"""

import random


stop = 'Y'
nombre_ordi = random.randint(1, 8)
while stop =='Y':
    nombre_user = int(input("Deviner le nombre choisi par l'ordi : "))
    if nombre_ordi == nombre_user:
        print("felicitation, vous êtes un devin!!")
        break;
    elif nombre_ordi > nombre_user:
        print("Trop bas, reessayez!")
    elif nombre_ordi < nombre_user:
        print("Vous visez bien haut!")
    stop = input("Voulez vous continuer? Y/N")
    if stop == 'N': 
        print(f"l'ordi a choisi : {nombre_ordi}")