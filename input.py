import pygame
from enum import Enum

class direction(Enum):
    """La classe direction définit la liste des mouvement possible, haut/bas/gauche/droite"""
    ANY = 0
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4
    

class inputs:
    """La classe inputs permet de récuperer les actions claviers/souris du joueur"""
    
    def __init__(self, cursor_x:int, cursor_y:int, clicked:bool = False, direction:direction = direction.ANY) -> None:
        self.__cursor_x:int = cursor_x
        self.__cursor_y:int = cursor_y
        self.__clicked = clicked
        self.__direction:direction = direction
    
    def getSourisx(self)->int:
        return self.__cursor_x
    def getSourisy(self)->int:
        return self.__cursor_y
    def estClique(self)->bool:
        return self.__clicked
    def getDirection(self)->direction:
        return self.__direction