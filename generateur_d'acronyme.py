# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 17:48:13 2022

@author: Yvana Tchamgoue
"""

texte = str(input('donner une chaine de caractères (constituée de plusieurs mots) : '))

"""
on utilise une boucle for each, et pour chaque mot du texte, on recupère 
la première lettre et on l'associe à celle du mot précédent
"""
def accronyme_gen(texte):
    mots =texte.split() # on divise la chaine en plusieurs mots
    
    accronyme = '' #on initialise la variable qui contiendra l'accronyme
    for mot in mots :
        accronyme = accronyme+str(mot[0]).upper()
    return accronyme

print(f"voici l'accronyme {accronyme_gen(texte)}")