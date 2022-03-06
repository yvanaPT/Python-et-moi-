# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 21:04:03 2022

@author: Yvana Tchamgoue
"""

import random

choix = ['Ciseaux', 'Papier', 'Pierre']

score_joueur = 0
score_ordi = 0
while True:
    choix_ordi = random.choice(choix)
    choix_joueur = input('choisir  : C:Ciseaux, P:Papier, Pi:Pierre . Pour terminer : 0: ')
    if choix_joueur == 'C':
        if choix_ordi == 'Ciseaux':
            print('Egalité')
        if choix_ordi == 'Papier':
            print('Gagné')
            score_joueur += 1
        if choix_ordi == 'Pierre':
            print('perdu')
            score_ordi += 1
    elif choix_joueur == 'P':
        if choix_ordi == 'Ciseaux':
            print('Gagné')
            score_joueur += 1
        if choix_ordi == 'Papier':
            print('Egalité')
        if choix_ordi == 'Pierre':
            print('perdu')
            score_ordi += 1
    elif choix_joueur == 'Pi':
        if choix_ordi == 'Ciseaux':
            print('Gagné')
            score_joueur += 1
        if choix_ordi == 'Papier':
            print('Perdu')
            score_ordi += 1
        if choix_ordi == 'Pierre':
            print('Egalité')
    elif choix_joueur == '0':
        break
    else :
        print('Entrez une valeur valide !')

print(f'Score ordi :  {score_ordi} \nscore Joueur : {score_joueur}')