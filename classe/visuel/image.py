# ----------------------- Jeu de plateau - Image  ------------------------ #

import pygame

from enum import Enum  

class Page(Enum):
    CHOIX_DOUBLE = pygame.image.load("./assets/img/illustrations/Page_choixdouble.png")
    CHOIX_PERSO = pygame.image.load("./assets/img/illustrations/Page_choixperso.png")
    COMMANDES = pygame.image.load("./assets/img/illustrations/Page_commentjouer.png")
    DEBUT_JEU = pygame.image.load("./assets/img/illustrations/Page_demarrage.png")
    FIN_JEU = pygame.image.load("./assets/img/illustrations/Page_findujeu.png")
    CHOIX_NB_IA = pygame.image.load("./assets/img/illustrations/Page_nbia.png")
    CHOIX_NB_JOUEUR = pygame.image.load("./assets/img/illustrations/Page_nbjoueurs.png")
    JEU = pygame.image.load("./assets/img/illustrations/Page_jeu.png")
    STATS = pygame.image.load("./assets/img/illustrations/Page_statistiques.png")
    ARENE= pygame.image.load("./assets/img/illustrations/Page_arene.png")
    MAISON_DRAGON = pygame.image.load("./assets/img/illustrations/Page_maisondragon.png")
    MAISON = pygame.image.load("./assets/img/illustrations/Page_maisonsorciere.png")
    MAISON_SYMBOLE = pygame.image.load("./assets/img/illustrations/Page_maisonsymbole.png")

class BtnMenu(Enum):
    BTN_0 = pygame.image.load("./assets/img/interraction/Bouton0.png")
    BTN_1 = pygame.image.load("./assets/img/interraction/Bouton1.png")
    BTN_2 = pygame.image.load("./assets/img/interraction/Bouton2.png")
    BTN_3 = pygame.image.load("./assets/img/interraction/Bouton3.png")
    BTN_4 = pygame.image.load("./assets/img/interraction/Bouton4.png")

class De(Enum):
    FACE1 = pygame.image.load("./assets/img/de/Face1.png")
    FACE2 = pygame.image.load("./assets/img/de/Face2.png")
    FACE3 = pygame.image.load("./assets/img/de/Face3.png")
    FACE4 = pygame.image.load("./assets/img/de/Face4.png")
    FACE5 = pygame.image.load("./assets/img/de/Face5.png")
    FACE6 = pygame.image.load("./assets/img/de/Face6.png")

class Cle(Enum):
    WATER = pygame.image.load("./assets/img/cle/CleRiviere.png")
    GRASS = pygame.image.load("./assets/img/cle/CleForet.png")
    ROCK = pygame.image.load("./assets/img/cle/CleRocher.png")
    TOWN = pygame.image.load("./assets/img/cle/CleVille.png")

class Ennemis(Enum):
    CRAPAUD = pygame.image.load("./assets/img/ennemis/Crapaud.png")
    ECUREUIL = pygame.image.load("./assets/img/ennemis/Ecureuil.png")
    LEZARD = pygame.image.load("./assets/img/ennemis/Lezard.png")
    RAT = pygame.image.load("./assets/img/ennemis/Rat.png")

class Interaction(Enum):
    BASIQUE = pygame.image.load("./assets/img/interraction/BoutonBasique.png")
    DEFENSE = pygame.image.load("./assets/img/interraction/BoutonDefense.png")
    SPECIALE = pygame.image.load("./assets/img/interraction/BoutonSpeciale.png")
    FUITE = pygame.image.load("./assets/img/interraction/BoutonFuite.png")
    PV = pygame.image.load("./assets/img/interraction/Pv.png")
    ATTAQUER = pygame.image.load("./assets/img/interraction/Attaquer.png")
    CLES = pygame.image.load("./assets/img/interraction/Cles.png")
    CHANCE = pygame.image.load("./assets/img/interraction/Chance.png")
    MALUS = pygame.image.load("./assets/img/interraction/Malus.png")
    RETOUR = pygame.image.load("./assets/img/interraction/Retour.png")
    TP = pygame.image.load("./assets/img/interraction/Teleportation.png")
    DE = pygame.image.load("./assets/img/interraction/De.png")
    POTION = pygame.image.load("./assets/img/cle/Potion.png")

class Personnages(Enum):
    WATER = pygame.image.load("./assets/img/personnages/Ondine.png")
    GRASS = pygame.image.load("./assets/img/personnages/Flora.png")
    ROCK = pygame.image.load("./assets/img/personnages/Pierre.png")
    TOWN = pygame.image.load("./assets/img/personnages/Kevin.png")

class Plateau(Enum):
    ALEATOIRE = pygame.image.load("./assets/img/plateau/Aleatoire.png")
    BOSS = pygame.image.load("./assets/img/plateau/Boss.png")
    CHANCE = pygame.image.load("./assets/img/plateau/Chance.png")
    DEPART = pygame.image.load("./assets/img/plateau/Depart.png")
    MALUS = pygame.image.load("./assets/img/plateau/Malus.png")
    MORT = pygame.image.load("./assets/img/plateau/Mort.png")
    PUIT = pygame.image.load("./assets/img/plateau/Puit.png")
    REJOUE = pygame.image.load("./assets/img/plateau/Rejoue.png")
    SORCIERE = pygame.image.load("./assets/img/plateau/Sorciere.png")
    SPECIALE = pygame.image.load("./assets/img/plateau/Speciale.png")
    TELEPORTATION = pygame.image.load("./assets/img/plateau/Teleportation.png")
    VIDE = pygame.image.load("./assets/img/plateau/Vide.png")

class Image:
    """La classe Image est une classe qui permet d'afficher l'image sur l'interface"""
    
    def __init__(self, x:int, y:int, surface:pygame.Surface) -> None:
        """Initialisation de l'image."""
        self.__x = x
        self.__y = y
        self.__surface = surface
    
    def getX(self):
        """Getter de la position x."""
        return self.__x
    
    def getY(self):
        """Getter de la position y."""
        return self.__y
    
    def getSurface(self)-> pygame.Surface:
        """Getter du surface de l'image."""
        return self.__surface
    
    def affiche(self, surface:pygame.Surface):
        """Affiche l'image sur l'interface pygame (Surface surface)."""
        surface.blit(self.getSurface(), (self.getX(), self.getY()))
        return
    
    def affichageImageRedimensionnee(self, x:int, y:int, surface:pygame.Surface):
        """Affiche une image redimensionnee sur l'interface (int x, int y, Surface surface)."""
        image_redimensionnee = pygame.transform.scale(self.getSurface(), (x, y))
        surface.blit(image_redimensionnee, (self.getX(), self.getY()))
