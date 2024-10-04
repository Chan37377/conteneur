# -*- coding: utf-8 -*-
"""
Chapitre: NSIT_04_Strucutres lineaires
Activité: Conteneur / Pile

Created on Tue Sep 22 09:58:26 2020

@author: eric.buonocore
"""
import NSIT_04b_conteneur as pile
            
mon_conteneur = pile.Conteneur() # Instanciation de mon conteneur
print("*** Trajet aller ***")
print("Chargement à Shangai")
mon_conteneur.empile("s1")
mon_conteneur.empile("s2")
mon_conteneur.empile("s3")
mon_conteneur.empile("s4")
mon_conteneur.empile("s5")
print("Déchargement / Chargement à Houston")
mon_conteneur.depile()
mon_conteneur.depile()
mon_conteneur.depile()
mon_conteneur.empile("h1")
mon_conteneur.empile("h2")
mon_conteneur.empile("h3")
print("Déchargement au Havre")
while mon_conteneur.est_vide() == False:
    mon_conteneur.depile()
    
print("*** Trajet retour ***")
print("Chargement au Havre")
...
print("Déchargement / Chargement à Houston")
...
print("Déchargement à Shangai")
while mon_conteneur.est_vide() == False:
    mon_conteneur.depile()
