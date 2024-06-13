# ----------------------- Jeu de plateau - Texte  ------------------------ #
import pygame
pygame.init()
class Texte:
    """La classe Texte est une classe qui permet d'afficher le texte sur l'interface"""
    
    # Definir le Texte
    def __init__(self,texte,couleur,x,y) -> None:
        """_summary_
            Initialisation du texte
        """
        self.__x = x
        self.__y = y
        self.__texte = texte
        self.__couleur = couleur
    
    # Definir les getters
    def get_x(self):
        """_summary_
            renvoie la position(valeur) de X
        """
        return self.__x
    
    def get_y(self):
        """_summary_
            renvoie la position(valeur) de Y
        """
        return self.__y
    
    def get_texte(self):
        """_summary_
            Renvoie le texte à écrire
        """
        return self.__texte
    
    def get_couleur(self):
        """_summary_
            Renvoie la couleur du texte
        """
        return self.__couleur

    # Definir l'affichage du texte sur l'interface'
    def affiche(self,surface):
        """_summary_
            La fonction affiche affiche le texte sur l'interface pygame(Font font, Surface surface)
        """
        font = pygame.font.Font('./assets/font/times-new-roman.ttf',16)
        texte_surface = font.render(str(self.get_texte()), True, self.get_couleur())
        surface.blit(texte_surface, (self.get_x(), self.get_y()))
        return
    
    
 