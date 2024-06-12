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
            Getter de la position x
        """
        return self.__x
    
    def get_y(self):
        """_summary_
            Getter de la position y
        """
        return self.__y
    
    def get_texte(self):
        """_summary_
            Getter du texte à ecrire
        """
        return self.__texte
    
    def get_couleur(self):
        """_summary_
            Getter de la couleur du texte
        """
        return self.__couleur

    # Definir l'affichage du texte sur l'interface'
    def affiche(self,surface):
        """_summary_
            La fonction affiche affiche le texte sur l'interface pygame(Font font, Surface surface)
        """
        font = pygame.font.Font('./assets/font/times-new-roman.ttf')
        texte_surface = font.render(str(self.__texte), True, self.__couleur)
        surface.blit(texte_surface, (self.__x, self.__y))
        return
    
    
        
# Tests des fonctions
"""
if __name__ == "__main__":
    
    import pygame, couleur
    
    pygame.init()
    
    nouveau_dialogue = Texte("Coucou",couleur.Couleur().get_Beige(),20,50)
    nouveau_dialogue.affiche(pygame.font.Font('./assets/font/times-new-roman.ttf', 16),pygame.display.set_mode((700,800)))
"""