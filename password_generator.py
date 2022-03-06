# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 17:33:23 2022
Generateur de mot de passe
@author: Yvana Tchamgoue
"""

import random

# variable qui contient la longueur du mdp

longueur = int((input("Donnez la longueur du mot de passe : ")))

""" on cree une chaine de caractère qui contient les lettres de l'alphabet
et les caractères spéciaux, de cette chaine on choisira des carctères
de facon aleatoire
""" 
caracteres= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&\()*+,-./:;<=>?@[]^_{|}~"

# join permet de regrouper les caratères en un seul mot
# random.saomple retourn e un tableau(liste) de caractères

password = "".join(random.sample(caracteres, longueur))

print(password)