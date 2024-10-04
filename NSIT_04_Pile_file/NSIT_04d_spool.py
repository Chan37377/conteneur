"""
Chapitre: NSIT_04_Strucutres lineaires
Activité: Spool d'impression / Spool

Created on Tue Sep 22 09:58:26 2020

@author: eric.buonocore
"""

class Spool():
    """ Les documents sont envoyés à l'imprimante dans l'ordre de leur arrivée :
        premier entré - premier sorti (anglais first in-first out abr. FIFO)
        Les éléments à stocker sont désignés par une référence (une chaîne de caractère)
        Par exemple « doc1 » ou « img3 ».
    """
    def __init__(self,maxi = 10):
        # Constructeur de la classe Conteneur
        self.nb_doc_max = maxi
        self.documents = []
    
    def est_vide(self)->bool:
        """ Renvoie True si la Spool est vide
            Sinon renvoie False
        """
        if len(self.documents) == 0:
            return True
        return False
    
    def est_plein(self)->bool:
        """ Renvoie True si le spool est plein.
            Sinon renvoie False
        """
        if len(self.documents) >= self.nb_doc_max:
            return True
        else:
            return False
    
    def ajoute(self, doc)->bool:
        """ Ajoute l'élément doc en tête du spool (premier élément de self.documents) si le spool n'est pas plein.
            Renvoie True si c'est possible, sinon, affiche un message d'alerte et renvoie False
        """
        if self.est_plein():
            print("ERREUR: La mémoire tampon est pleine")
            return False
        else:
            self.documents.append(None) # Création d'une case 'vide' en fin de Spool
            for i in range(len(self.documents)-1, 0, -1): # Décale tous les éléments présents vers la droite
                self.documents[i] = self.documents[i-1]
            self.documents[0] = doc # Ajoute le nouveau document à l'indice 0
            return True
    
    def extrait(self)->str:
        """ Si le spool n'est pas vide, enlève le dernier élément de la liste self.documents.
            Affiche et renvoie le nom de l'élément enlevé.
            Sinon affiche un message d'alerte et renvoie None.
        """
        pass
    
a = Spool()
a.ajoute("img1")
a.ajoute("doc1")
a.ajoute("doc2")
a.ajoute("doc3")
a.ajoute("img2")
a.ajoute("doc4")
a.ajoute("doc5")
a.extrait()
a.extrait()
a.extrait()
a.ajoute("img3")
a.ajoute("doc6")
a.ajoute("doc7")
while a.est_vide() != True:
    a.extrait()
    
b = Spool()    
b.ajoute("img4")
b.ajoute("img5")
b.ajoute("doc8")
b.extrait()
b.extrait()
b.extrait()
b.extrait()
for i in range(12):
    nom_doc = "doc"+str(i+9)
    b.ajoute(nom_doc)
while b.est_vide() != True:
    b.extrait()
