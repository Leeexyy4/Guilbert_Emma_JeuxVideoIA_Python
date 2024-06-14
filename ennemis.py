# ----------------------- Jeu de plateau - Joueur  ------------------------ #

# Bibliothèques utilisées pour le code
from utils import image
from enum import Enum
import random

class Nom(Enum):
    """La classe Nom(Enum) regroupe le nom des ennemis affrontables."""
    ECUREUIL = "Ecureuil"
    CRAPAUD = "Crapaud"
    LEZARD = "Lezard"
    RAT = "Rat"

class Element(Enum):
    """La classe Element(Enum) regroupe les 'titres' des ennemis affrontables"""
    CRAPAUD = "de la Riviere"
    ECUREUIL = "de la Foret"
    LEZARD = "du Rocher"
    RAT = "de la Ville"

class Ennemis:
    """La classe Ennemis est une classe qui permet de créer un ennemi."""
    
    lezard_is_used = False 
    rat_is_used = False 
    crapaud_is_used = False 
    ecureuil_is_used = False 

    def __init__(self, prenom, element) -> None:
        """Initialisation de l'ennemi."""
        self.__x:int = 620
        self.__y:int = 400
        self.__prenom:str = prenom
        self.__pv = 100
        self.__attaque = 110
        self.__element = element
    
    # Definir les getters
    def getX(self):
        """_summary_
            Renvoie la position(valeur) de X
        """
        return self.__plateaux *47
    
    def getY(self):
        """_summary_
            Renvoie la position(valeur) de Y
        """
        return self.__plateauy *47
    
    def getPrenom(self)->str:
        """_summary_
            Renvoie le prénom du joueur
        """
        if(self.getElement() == Element.ECUREUIL.value): return Nom.ECUREUIL.value
        if(self.getElement() == Element.CRAPAUD.value): return Nom.CRAPAUD.value
        if(self.getElement() == Element.RAT.value): return Nom.RAT.value
        if(self.getElement() == Element.LEZARD.value): return Nom.LEZARD.value
        return None
    
    def getImage(self):
        """Renvoie les images correspondantes aux personnages"""
        if(self.getElement() == Element.ECUREUIL.value): return image.Ennemis.ECUREUIL.value
        if(self.getElement() == Element.CRAPAUD.value): return image.Ennemis.CRAPAUD.value
        if(self.getElement() == Element.RAT.value): return image.Ennemis.RAT.value
        if(self.getElement() == Element.LEZARD.value): return image.Ennemis.LEZARD.value
        return None

    def getId(self):
        """_summary_
            Renvoie l'id du joueur
        """
        return self.__id
    
    def getPv(self):
        """_summary_
            Renvoie les points de vie du joueur
        """
        return self.__pv
    
    def getAttaque(self):
        """_summary_
            Renvoie les "attaques" du joueur
        """
        return self.__attaque
    
    def getElement(self):
        """_summary_
            Renvoie l'élément du joueur
        """
        return self.__element
    
    def getInventaire(self):
        """_summary_
            Renvoie l'inventaire du joueur
        """
        return self.__inventaire
    
    def getPlateaux(self):
            """_summary_
                Renvoie la position(valeur) de X sur le plateau
            """
            return self.__plateaux
    
    def getPlateauy(self):
            """_summary_
                Renvoie la position(valeur) de X sur le plateau
            """
            return self.__plateauy
    
    def getAttaque(self):
            """_summary_
                Renvoie "l'attaque" sur le plateau
            """
            return self.__attaque
            
    def setLien(self, lien):
        """_summary_
            Modifie le lien de l'image du joueur
        """
        self.__lien = lien
    
    def setPv(self,pv):
        """_summary_
            Modifie la vie du joueur
        """
        self.__pv = pv
    
    def setElement(self, element):
        """_summary_
            Modifie l'élément du joueur
        """
        if(self.getElement() == None): pass
        elif(self.getElement() == Element.ECUREUIL.value): Ennemis.ecureuil_is_used = False
        elif(self.getElement() == Element.CRAPAUD.value): Ennemis.crapaud_is_used = False
        elif(self.getElement() == Element.RAT.value): Ennemis.rat_is_used = False
        else: Ennemis.lezard_is_used = False
        self.setElement(element)
        if(self.getElement() == Element.LEZARD.value): Ennemis.lezard_is_used = True
        elif(self.getElement() == Element.ECUREUIL.value): Ennemis.ecureuil_is_used = True
        elif(self.getElement() == Element.CRAPAUD.value): Ennemis.crapaud_is_used = True
        elif(self.getElement() == Element.RAT.value): Ennemis.rat_is_used = True
        
    def setInventaire(self,inventaire):
        """_summary_
            Modifie l'inventaire du joueur
        """
        self.__inventaire = inventaire
    
    def setPlateaux(self,plateaux):
        """
            Modifie la position X sur le plateau
        """
        self.__plateaux = plateaux
    
    def setPlateauy(self,plateauy):
        """
            Modifie la position Y sur le plateau
        """
        self.__plateauy = plateauy

    def setAttaque(self,attaque):
        """
            Modifie l'attaque sur le plateau
        """
        self.__attaque = attaque
    
    def Choix_ennemis(joueur):
        """Choisit un ennemi en fonction des clés obtenues par le joueur."""
        liste_ennemis = ["Ecureuil", "Crapaud", "Lezard", "Rat"]
        for i in joueur.getInventaire():
            if i == "cle du Rocher":
                liste_ennemis.remove("Lezard")
            elif i == "cle de la Foret":
                liste_ennemis.remove("Ecureuil")
            elif i == "cle de la Ville":
                liste_ennemis.remove("Rat")
            elif i == "cle de la Riviere":
                liste_ennemis.remove("Crapaud")
                
        ennemis_select = random.choice(liste_ennemis)
        if ennemis_select == "Rat":
            un_ennemi = Ennemis("Rat", "de la Ville")
        elif ennemis_select == "Crapaud":
            un_ennemi = Ennemis("Crapaud", "de la Riviere")
        elif ennemis_select == "Ecureuil":
            un_ennemi = Ennemis("Ecureuil", "de la Foret")
        elif ennemis_select == "Lezard":
            un_ennemi = Ennemis("Lezard", "du Rocher")
        return un_ennemi
