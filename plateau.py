# ----------------------- Jeu de plateau - Plateau  ------------------------ #

# Bibliothèques utilisées pour le code
import pygame, couleur, texte
import random

pygame.init()

class Plateau:
    """La classe Plateau est une classe qui permet de créer le plateau de jeu."""
    
    # Initialisation du plateau
    def __init__(self) -> None:
        """_summary_
            Initialisation du Plateau
        """
        # Définir le plateau
        self.__plateau = []
        
        # Définir la taille d'une case
        self.__taille_case = 800 // 17
        
        # Définir les noms des cases
        self.__nom_case = {
            couleur.Couleur().get_Rouge(): "Boss",
            couleur.Couleur().get_Rose(): "Chance",
            couleur.Couleur().get_Orange(): "Malus",
            couleur.Couleur().get_Indigo(): "Pouf",
            couleur.Couleur().get_Violet(): "Rejoue",
            couleur.Couleur().get_Turquoise(): "Grrr",
            couleur.Couleur().get_Beige(): "Hutte",
            couleur.Couleur().get_Gris(): "Spéciale",
            couleur.Couleur().get_Bleu(): "Puit",
            couleur.Couleur().get_Blanc(): "Vide",
            couleur.Couleur().get_Noir(): "Mort",
            couleur.Couleur().get_Jaune(): "Départ"
        }
        
        self.__max_couleur = {
            couleur.Couleur().get_Rouge(): 4,
            couleur.Couleur().get_Rose(): 26,
            couleur.Couleur().get_Orange(): 29,
            couleur.Couleur().get_Indigo(): 2,
            couleur.Couleur().get_Violet(): 20,
            couleur.Couleur().get_Turquoise(): 20,
            couleur.Couleur().get_Beige(): 1,
            couleur.Couleur().get_Gris(): 10,
            couleur.Couleur().get_Bleu(): 1,
            couleur.Couleur().get_Noir(): 1,
            couleur.Couleur().get_Jaune():1,
            couleur.Couleur().get_Blanc():55
        }

        self.__case_decouverte = []

        
        # Afficher le plateau
        self.remplir_plateau_aleatoirement()
        

    def get_plateau(self):
        """Renvoie le plateau de jeu."""
        return self.__plateau
    
    def get_cases_decouvertes(self):
        """Renvoie le plateau de jeu."""
        return self.__case_decouverte

    def get_case_jaune(self):
        """Renvoie les coordonnées correspondant à la case jaune."""
        for ligne in range(10):
            for colonne in range(17):
                if self.get_plateau()[ligne][colonne] == couleur.Couleur().get_Jaune():
                    coord_case_jaune = (ligne, colonne)
        return coord_case_jaune

    def get_case_indigo(self, joueur):
        """Renvoie les coordonnées correspondant aux cases indigo."""
        for ligne in range(10):
            for colonne in range(17):
                if self.get_plateau()[ligne][colonne] == couleur.Couleur().get_Indigo():
                    if joueur.get_plateaux() == ligne and joueur.get_plateauy() == colonne:
                        pass
                    else:
                        coord_case_indigo = (ligne, colonne)
        return coord_case_indigo
    
    def get_cases(self, ligne, colonne):
        """Renvoie la couleur de la case à la position spécifiée."""
        return self.get_plateau()[ligne][colonne]
        
    def get_nom(self, ligne, colonne):
        """Renvoie le nom de la case à la position spécifiée."""
        couleur_case = self.get_plateau()[ligne][colonne]  # Obtenir la couleur de la case
        nom_case = self.__nom_case[couleur_case]
        return nom_case

    def set_plateau(self, plateau):
        """Modifie le plateau de jeu."""
        self.__plateau = plateau

    def set_cases_decouvertes(self, case_decouverte):
        """Modifie le plateau de jeu."""
        self.__case_decouverte = case_decouverte
        

    def remplir_plateau_aleatoirement(self):
        """Remplit le plateau de manière aléatoire en fonction de max_couleur."""
        # Crée une liste des couleurs disponibles en fonction de max_couleur
        couleurs_disponibles = []
        for couleurs, nombre_max in self.__max_couleur.items():
            couleurs_disponibles.extend([couleurs] * nombre_max)

         # Remplit le plateau de manière aléatoire
        for i in range(10):
            ligne_plateau = []
            for j in range(17):
                if couleurs_disponibles:  # Vérifiez si des couleurs sont disponibles
                    couleur_aleatoire = random.choice(couleurs_disponibles)
                    couleurs_disponibles.remove(couleur_aleatoire)  # Supprime la couleur de la liste
                    ligne_plateau.append(couleur_aleatoire)
        
            self.__plateau.append(ligne_plateau)
        return self.__plateau
    
    def plateau_cache(self, surface):
        """Cache le plateau en le dessinant entièrement en noir."""
        for ligne in range(10):
            for colonne in range(17):
                x = colonne * self.__taille_case  # Coordonnée X du coin supérieur gauche du rectangle
                y = ligne * self.__taille_case  # Coordonnée Y du coin supérieur gauche du rectangle          
                rectangle = pygame.Rect(x, y, self.__taille_case, self.__taille_case)  # Créer un rectangle
                pygame.draw.rect(surface, couleur.Couleur().get_Noir(), rectangle)  # Dessiner le rectangle avec la couleur

    def mise_a_jour_plateau(self, surface):
        """Met à jour le plateau en affichant les cases découvertes."""
        font = pygame.font.Font(('./assets/font/Dosis-VariableFont_wght.ttf'), 11)
        for i in self.get_cases_decouvertes():
            couleur_case = self.get_plateau()[i[0]][i[1]]  # Obtenir la couleur de la case
            x = i[1] * self.__taille_case  # Coordonnée X du coin supérieur gauche du rectangle
            y = i[0] * self.__taille_case  # Coordonnée Y du coin supérieur gauche du rectangle          
            rectangle = pygame.Rect(x, y, self.__taille_case, self.__taille_case)  # Créer un rectangle
            pygame.draw.rect(surface, couleur_case, rectangle)  # Dessiner le rectangle avec la couleur
            if (self.__nom_case[couleur_case] != "Vide") and (self.__nom_case[couleur_case] != "Mort") and (self.__nom_case[couleur_case] != "Départ/arrivée"):
                texte.Texte(self.__nom_case[couleur_case], couleur.Couleur().get_Noir(), x + 9, y + 15).affiche(font, surface)

            
        
# if __name__ == "__main__" :
#     plateau_de_jeu = Plateau()
#     plateau_de_jeu.remplir_plateau_aleatoirement()
#     surface = pygame.display.set_mode((800, 700))
#     plateau_de_jeu.plateau_cache(surface)
#     case_decouverte = [[i, j] for i in range(0, 10) for j in range(0, 17)]
#     plateau_de_jeu.mise_a_jour_plateau(surface)
#     pygame.display.update()
#     pygame.time.delay(2000)