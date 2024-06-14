# ----------------------- Jeu de plateau - Joueur  ------------------------ #

# Bibliotheques utilisees pour le code
from utils import image
from utils.logique import CASE_TYPE
# from utils import texte, couleur, image, rectangle, logique

from enum import Enum

class Nom(Enum):
    """La classe Nom(Enum) regroupe le nom des personnages jouables."""
    WATER = "Ondine"
    GRASS = "Flora"
    ROCK = "Pierre"
    TOWN = "Kevin"
class Element(Enum):
    """La classe Element(Enum) regroupe les 'titres' des personnages jouables"""
    WATER = "de la Riviere"
    GRASS = "de la Foret"
    ROCK = "du Rocher"
    TOWN = "de la Ville"


class Joueur:
    """La classe Joueur est une classe qui permet d'utiliser un personnage."""
    
    water_is_used = False 
    grass_is_used = False 
    town_is_used = False 
    rock_is_used = False 
    
    # Definir un joueur
    def __init__(self,id:int, plateaux:int, plateauy:int,element:Element, inventaire:list=[]) -> None:
        """_summary_
            Initialisation du joueur
        """
        self.__id:int = id
        self.__element:Element = element
        self.__plateaux:int = plateaux
        self.__plateauy:int = plateauy
        self.__pv:int = 700
        self.__attaque:int = 110
        self.__inventaire:list = ["cle de la Ville","cle de la Foret", "cle de la Riviere", "cle du Rocher"]
        

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
        if(self.getElement() == Element.GRASS): return Nom.GRASS.value
        if(self.getElement() == Element.WATER): return Nom.WATER.value
        if(self.getElement() == Element.TOWN): return Nom.TOWN.value
        if(self.getElement() == Element.ROCK): return Nom.ROCK.value
        return None
    
    def getImage(self):
        """Renvoie les images correspondantes aux personnages"""
        if(self.getElement() == Element.GRASS): return image.Personnages.GRASS.value
        elif(self.getElement() == Element.WATER): return image.Personnages.WATER.value
        elif(self.getElement() == Element.TOWN): return image.Personnages.TOWN.value
        elif(self.getElement() == Element.ROCK): return image.Personnages.ROCK.value
        else:
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
        elif(self.getElement() == Element.GRASS): Joueur.grass_is_used = False
        elif(self.getElement() == Element.WATER): Joueur.water_is_used = False
        elif(self.getElement() == Element.TOWN): Joueur.town_is_used = False
        else: Joueur.rock_is_used = False
        self.setElement(element)
        if(self.getElement() == Element.ROCK): Joueur.rock_is_used = True
        elif(self.getElement() == Element.GRASS): Joueur.grass_is_used = True
        elif(self.getElement() == Element.WATER): Joueur.water_is_used = True
        elif(self.getElement() == Element.TOWN): Joueur.town_is_used = True
        
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

    def avoirCles(self) -> bool : 
        """Verifie si le joueur a toutes les cles necessaires."""
        nombre_cles = 0
        print(self.getInventaire())
        for i in self.getInventaire():
            nombre_cles += 1
        if nombre_cles == 4:
            return True
        else:
            return False
    
    def aGagne(self,cases_plateau:list[CASE_TYPE]) -> bool:
        """Verifie si le joueur a gagne en ayant toutes les cles et en etant dans une hutte."""
        gagne = False
        if self.avoirCles() == True and cases_plateau[self.__plateaux][ self.__plateauy] == CASE_TYPE.HUTTE:
            gagne = True
        return gagne