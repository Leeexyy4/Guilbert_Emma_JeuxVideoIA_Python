# ----------------------- Jeu de plateau - De  ------------------------ #

# Bibliotheques utilisees pour le code
import pygame
from random import randint
from classe.personnage import intelA
from classe.visuel import image
#pour les images : De creees par Moi-meme side Piskel

class De:
    """La classe De est une classe qui permet de lancer le de."""

    def __init__(self) -> None:
        """Initialisation du de."""
        self.__faceDe = 0

    def getFaceDe(self):
        """Getter de la face aleatoire choisie."""
        return self.__faceDe

    def setFaceDe(self, faceDe):
        """Setter de la face aleatoire choisie."""
        self.__faceDe = faceDe

    def setFaceDeDesincremente(self, x):
        """Setter de la face aleatoire choisie."""
        self.__faceDe = self.__faceDe - x
