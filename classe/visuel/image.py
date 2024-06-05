# ----------------------- Jeu de plateau - Image  ------------------------ #

import pygame

from enum import Enum
class Sorciere(Enum):
    MAISON_DRAGON = pygame.image.load("./assets/img/illustrations/Page_maisondragon.png")
    MAISON = pygame.image.load("./assets/img/illustrations/Page_maisonsorciere.png")
    MAISON_SYMBOLE = pygame.image.load("./assets/img/illustrations/Page_maisonsymbole.png")
    # FACE1 = pygame.image.load("./assets/img/illustrations/Page_sorciere.png")
    POTION = pygame.image.load("./assets/img/illustrations/Potion_inverstium.png")
class Page(Enum):
    CHOIX_DOUBLE = pygame.image.load("./assets/img/illustrations/Page_choixdouble.png")
    CHOIX_PERSO = pygame.image.load("./assets/img/illustrations/Page_choixperso.png")
    COMMANDES = pygame.image.load("./assets/img/illustrations/Page_commentjouer.png")
    DEBUT_JEU = pygame.image.load("./assets/img/illustrations/Page_demarrage.png")
    FIN_JEU = pygame.image.load("./assets/img/illustrations/Page_findujeu.png")
    # PAGE_JEU = pygame.image.load("./assets/img/illustrations/Page_jeu.png")
    CHOIX_NB_IA = pygame.image.load("./assets/img/illustrations/Page_nbia.png")
    CHOIX_NB_JOUEUR = pygame.image.load("./assets/img/illustrations/Page_nbjoueurs.png")
    BAS_PLATEAU = pygame.image.load("./assets/img/illustrations/Page_plateau.png")
    STATS = pygame.image.load("./assets/img/illustrations/Page_statistiques.png")
    ARENE= pygame.image.load("./assets/img/ennemis/Arene.png")
class BtnAttaque(Enum):
    BASIQUE = pygame.image.load("./assets/img/illustrations/Basique.png")
    DEFENSE = pygame.image.load("./assets/img/illustrations/Defense.png")
    SPECIALE = pygame.image.load("./assets/img/illustrations/Speciale.png")
    FUITE = pygame.image.load("./assets/img/illustrations/Fuite.png")
class BtnMenu(Enum):
    BTN_0 = pygame.image.load("./assets/img/illustrations/0.png")
    BTN_1 = pygame.image.load("./assets/img/illustrations/1.png")
    BTN_2 = pygame.image.load("./assets/img/illustrations/2.png")
    BTN_3 = pygame.image.load("./assets/img/illustrations/3.png")
    BTN_4 = pygame.image.load("./assets/img/illustrations/4.png")
class De(Enum):
    FACE1 = pygame.image.load("./assets/img/de/Face1.png")
    FACE2 = pygame.image.load("./assets/img/de/Face2.png")
    FACE3 = pygame.image.load("./assets/img/de/Face3.png")
    FACE4 = pygame.image.load("./assets/img/de/Face4.png")
    FACE5 = pygame.image.load("./assets/img/de/Face5.png")
    FACE6 = pygame.image.load("./assets/img/de/Face6.png")
class Cle(Enum):
    WATER = pygame.image.load("./assets/img/cle/cle_riviere.png")
    GRASS = pygame.image.load("./assets/img/cle/cle_foret.png")
    ROCK = pygame.image.load("./assets/img/cle/cle_rocher.png")
    TOWN = pygame.image.load("./assets/img/cle/cle_ville.png")
class Ennemis(Enum):
    CRAPAUD = pygame.image.load("./assets/img/ennemis/Crapaud.png")
    ECUREUIL = pygame.image.load("./assets/img/ennemis/Ecureuil.png")
    LEZARD = pygame.image.load("./assets/img/ennemis/Lezard.png")
    RAT = pygame.image.load("./assets/img/ennemis/Rat.png")
class Interaction(Enum):
    PV = pygame.image.load("./assets/img/interraction/Pv.png")
    ATTAQUER = pygame.image.load("./assets/img/interraction/Attaquer.png")
    CLES = pygame.image.load("./assets/img/interraction/Cles.png")
    CHANCE = pygame.image.load("./assets/img/interraction/Chance.png")
    MALUS = pygame.image.load("./assets/img/interraction/Malus.png")
    RETOUR = pygame.image.load("./assets/img/interraction/Retour.png")
    TP = pygame.image.load("./assets/img/interraction/Teleportation.png")
    DE = pygame.image.load("./assets/img/interraction/De.png")
class Personnages(Enum):
    WATER = pygame.image.load("./assets/img/personnages/Ondine.png")
    GRASS = pygame.image.load("./assets/img/personnages/Flora.png")
    ROCK = pygame.image.load("./assets/img/personnages/Pierre.png")
    TOWN = pygame.image.load("./assets/img/personnages/Kevin.png")

class Image:
    """La classe Image est une classe qui permet d'afficher l'image sur l'interface"""
    
    def __init__(self, x:int, y:int, surface:pygame.Surface) -> None:
        """Initialisation de l'image."""
        self.__x = x
        self.__y = y
        self.__surface = surface
    
    def get_x(self):
        """Getter de la position x."""
        return self.__x
    
    def get_y(self):
        """Getter de la position y."""
        return self.__y
    
    def get_surface(self)-> pygame.Surface:
        """Getter du surface de l'image."""
        return self.__surface
    
    def affiche(self, surface):
        """Affiche l'image sur l'interface pygame (Surface surface)."""
        nouvelle_image = self.get_surface()
        surface.blit(nouvelle_image, (self.get_x(), self.get_y()))
        return
    
    def affichage_image_redimensionnee(self, x, y, surface):
        """Affiche une image redimensionnee sur l'interface (int x, int y, Surface surface)."""
        image = self.get_surface()
        image_redimensionnee = pygame.transform.scale(image, (x, y))
        surface.blit(image_redimensionnee, (self.get_x(), self.get_y()))
        pygame.display.update()
