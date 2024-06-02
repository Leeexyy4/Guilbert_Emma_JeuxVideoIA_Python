# ----------------------- Jeu de plateau - Image  ------------------------ #

import pygame

class Image:
    """La classe Image est une classe qui permet d'afficher l'image sur l'interface"""
    
    def __init__(self, x, y, lien) -> None:
        """Initialisation de l'image."""
        self.__x = x
        self.__y = y
        self.__lien = lien
    
    def get_x(self):
        """Getter de la position x."""
        return self.__x
    
    def get_y(self):
        """Getter de la position y."""
        return self.__y
    
    def get_lien(self):
        """Getter du lien de l'image."""
        return self.__lien

    def affiche(self, surface):
        """Affiche l'image sur l'interface pygame (Surface surface)."""
        nouvelle_image = pygame.image.load(self.get_lien())
        surface.blit(nouvelle_image, (self.get_x(), self.get_y()))
        return
    
    def affichage_image_redimensionnee(self, x, y, surface):
        """Affiche une image redimensionnee sur l'interface (int x, int y, Surface surface)."""
        image = pygame.image.load(self.get_lien())
        image_redimensionnee = pygame.transform.scale(image, (x, y))
        surface.blit(image_redimensionnee, (self.get_x(), self.get_y()))
        pygame.display.update()
