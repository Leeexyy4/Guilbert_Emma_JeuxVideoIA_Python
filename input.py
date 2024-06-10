import pygame
from enum import Enum

class direction(Enum):
    ANY = 0
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4
    

class inputs:
    
    def __init__(self, cursor_x:int, cursor_y:int, clicked:bool = False, direction:direction = direction.ANY) -> None:
        self.__cursor_x:int = cursor_x
        self.__cursor_y:int = cursor_y
        self.__clicked = clicked
        self.__direction:direction = direction
    
    def get_cursor_x(self)->int:
        return self.__cursor_x
    def get_cursor_y(self)->int:
        return self.__cursor_y
    def get_clicked(self)->bool:
        return self.__clicked
    def get_direction(self)->direction:
        return self.__direction