"""
Chapitre: NSIT_04_Strucutres lineaires
Activité: Spool d'impression / Spool

Test de 3 implémentations différentes du type File

@author: eric.buonocore
"""

import NSIT_04d_spool as sp
import NSIT_04d_file as fl
from collections import deque
import time

# ***** ***** ***** ***** ***** ***** ***** *****
# Test de l'implémentation de la File avec Spool
# ***** ***** ***** ***** ***** ***** ***** *****
a = sp.Spool() # Instancie a en tant qu'objet de type Spool défini dans NSIT_04d_spool.py
tps_debut = time.time() # Relève le chronomètre à ce moment

# Remplie et vide la file 10.000 fois de suite
for n in range(100000):
    # Ajoute 10 éléments: Remplie entièrement la file
    for i in range(10):
        a.ajoute("un nouveau document")

    # Extrait 10 éléments: Vide la file
    for i in range(10):
        a.extrait()

tps_fin = time.time() # Relève la nouvelle caleur du chronomètre

print("Durée totale avec l'implémentation Spool", tps_fin - tps_debut)

# ***** ***** ***** ***** ***** ***** ***** *****
# Test de l'implémentation de la File avec File
# ***** ***** ***** ***** ***** ***** ***** *****
f = fl.File() # Instancie a en tant qu'objet de type File défini dans NSIT_04d_file.py
tps_debut = time.time() # Relève le chronomètre à ce moment

# Remplie et vide la file 10.000 fois de suite
for n in range(100000):
    # Ajoute 10 éléments: Remplie entièrement la file
    for i in range(10):
        f.ajoute("un nouveau document")

    # Extrait 10 éléments: Vide la file
    for i in range(10):
        f.extrait()

tps_fin = time.time() # Relève la nouvelle caleur du chronomètre

print("Durée totale avec l'implémentation File", tps_fin - tps_debut)



# ***** ***** ***** ***** ***** ***** ***** *****
# Test de l'implémentation de la File avec deque
# ***** ***** ***** ***** ***** ***** ***** *****
d = deque([]) # Crée une collection vide 
tps_debut = time.time() # Relève le chronomètre à ce moment

# Remplie et vide la file 10.000 fois de suite
for n in range(100000):
    # Ajoute 10 éléments: Remplie entièrement la file
    for i in range(10):
        d.appendleft("un nouveau document")

    # Extrait 10 éléments: Vide la file
    for i in range(10):
        d.popleft()

tps_fin = time.time() # Relève la nouvelle caleur du chronomètre

print("Durée totale avec l'implémentation deque", tps_fin - tps_debut)

