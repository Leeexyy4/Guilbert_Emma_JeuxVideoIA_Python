from enum import Enum

class Couleur(Enum):
    """La classe Couleur est une classe qui permet de récuperer la couleur choisie grâce au getter."""
    
    NOIR = (0, 0, 0)
    BLANC = (255, 255, 255)
    JAUNE = (255, 255, 0)
    VERT = (0, 255, 0)
    VIOLET = (238, 130, 238)
    ROUGE = (255, 24, 40)
    GRIS = (192, 192, 192)
    ROSE = (255, 192, 203)
    TURQUOISE = (175, 238, 238)
    INDIGO = (60, 0, 225)
    ORANGE = (255, 127, 0)
    BLEU = (0, 204, 204)
    BEIGE = (255, 255, 204)

class CASE_TYPE(Enum):
    """La classe CASE_TYPE définit le type de case présent sur le plateau."""
    BONUS = Couleur.ROSE # click pour savoir le résultat
    MALUS = Couleur.ORANGE # click pour savoir le résultat
    SPECIALE = Couleur.GRIS # choisit de prendre le risque ou pas, SI choisit, att 2eme click
    VIDE = Couleur.BLANC # Se pas rien, pas de click
    MORT = Couleur.NOIR
    HUTTE = Couleur.BEIGE # choix entre use clef si non rien, pour finir la partie
    POUF = Couleur.INDIGO# click pour être tp aléatoirement
    REJOUE = Couleur.VIOLET# rejour à partir du lancé de dée
    PUIT = Couleur.BLEU # Choisit quoi abandoné, Si n'as pas de clef, boucle sur lui meme
    GRRR = Couleur.TURQUOISE # click pour être tp
    DEPART = Couleur.JAUNE # Se pas rien, pas de click
    BOSS = Couleur.ROUGE  # début du fight