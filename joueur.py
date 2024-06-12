# ----------------------- Jeu de plateau - Joueur  ------------------------ #

# Bibliotheques utilisees pour le code
import pygame, random
from utils import image
# from utils import texte, couleur, image, rectangle, logique

from enum import Enum
class Nom(Enum):
    """La classe Nom regroupe le nom des personnages jouables."""
    WATER = "Ondine"
    GRASS = "Flora"
    ROCK = "Pierre"
    TOWN = "Kevin"
class Element(Enum):
    """La classe Element regroupe les 'titres' des personnages jouables"""
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
    def __init__(self,id:int, plateaux:int, plateauy:int,element:Element) -> None:
        """_summary_
            Initialisation du joueur
        """
        self.__id:int = id
        self.__element:Element = element
        self.__plateaux:int = plateaux
        self.__plateauy:int = plateauy
        self.__pv:int = 700
        self.__attaque:int = 110
        self.__inventaire:list = []
        

    # Definir les getters
    def get_x(self):
        """_summary_
            Getter de la position x
        """
        return self.__plateaux *47
    
    def get_y(self):
        """_summary_
            Getter de la position y
        """
        return self.__plateauy *47
    
    def get_prenom(self)->str:
        """_summary_
            Getter du prenom du joueur
        """
        if(self.__element == Element.GRASS): return Nom.GRASS.value
        if(self.__element == Element.WATER): return Nom.WATER.value
        if(self.__element == Element.TOWN): return Nom.TOWN.value
        if(self.__element == Element.ROCK): return Nom.ROCK.value
        return None
    
    def get_image(self):
        if(self.__element == Element.GRASS): return image.Personnages.GRASS.value
        if(self.__element == Element.WATER): return image.Personnages.WATER.value
        if(self.__element == Element.TOWN): return image.Personnages.TOWN.value
        if(self.__element == Element.ROCK): return image.Personnages.ROCK.value
        return None

    def get_id(self):
        """_summary_
            Getter de l'id du joueur
        """
        return self.__id
    
    def get_pv(self):
        """_summary_
            Getter des pv du joueur
        """
        return self.__pv
    
    def get_attaque(self):
        """_summary_
            Getter des attaques du joueur
        """
        return self.__attaque
    
    def get_element(self):
        """_summary_
            Getter de l'__element du joueur
        """
        return self.__element
    
    def get_inventaire(self):
        """_summary_
            Getter de l'inventaire du joueur
        """
        return self.__inventaire
    
    def getPlateaux(self):
            """_summary_
                Getter de la position x sur le plateau
            """
            return self.__plateaux
    
    def getPlateauy(self):
            """_summary_
                Getter de la position y sur le plateau
            """
            return self.__plateauy
    
    def get_attaque(self):
            """_summary_
                Getter de l'attaque sur le plateau
            """
            return self.__attaque
        
        
            
    def set_lien(self, lien):
        """_summary_
            Setter du lien de l'image du joueur
        """
        self.__lien = lien
    
    def set_pv(self,pv):
        """_summary_
            Setter de la vie du joueur
        """
        self.__pv = pv
    
    def set_element(self, element):
        """_summary_
            Setter de l'__element du joueur
        """
        if(self.__element == None): pass
        elif(self.__element == Element.GRASS): Joueur.grass_is_used = False
        elif(self.__element == Element.WATER): Joueur.water_is_used = False
        elif(self.__element == Element.TOWN): Joueur.town_is_used = False
        else: Joueur.rock_is_used = False
        self.__element = element
        if(self.__element == Element.ROCK): Joueur.rock_is_used = True
        elif(self.__element == Element.GRASS): Joueur.grass_is_used = True
        elif(self.__element == Element.WATER): Joueur.water_is_used = True
        elif(self.__element == Element.TOWN): Joueur.town_is_used = True
        
    def set_inventaire(self,inventaire):
        """_summary_
            Setter de l'inventaire du joueur
        """
        self.__inventaire = inventaire
    
    def setPlateaux(self,plateaux):
        """
            Setter de la position x sur le plateau
        """
        self.__plateaux = plateaux
    
    def setPlateauy(self,plateauy):
        """
            Setter de la position y sur le plateau
        """
        self.__plateauy = plateauy

    def set_attaque(self,attaque):
        """
            Setter de l'attaque sur le plateau
        """
        self.__attaque = attaque
