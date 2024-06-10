from enum import Enum



class Couleur(Enum):
    """La classe Couleur est une classe qui permet de recuperer la couleur voulue grâce au getter."""
    
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
    LUCK = Couleur.ROSE # click pour savoir le résultat
    UNLUCK = Couleur.ORANGE # click pour savoir le résultat
    SPECIAL = Couleur.GRIS # choisit de prendre le risque ou pas, SI choisit, att 2eme click
    NOTHING = Couleur.BLANC # Se pas rien, pas de click
    DEATH = Couleur.NOIR
    WITCH = Couleur.BEIGE # choix entre use clef si non rien, pour finir la partie
    RANDOM_TP = Couleur.TURQUOISE# click pour être tp aléatoirement
    REPLAY = Couleur.VIOLET# rejour à partir du lancé de dée
    WELL = Couleur.BLEU # Choisit quoi abandoné, Si n'as pas de clef, boucle sur lui meme
    TP = Couleur.INDIGO # click pour être tp
    SPAWN = Couleur.JAUNE # Se pas rien, pas de click
    BOSS = Couleur.ROUGE  # début du fight