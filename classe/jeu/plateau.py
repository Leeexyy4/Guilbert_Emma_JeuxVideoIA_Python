# ----------------------- Jeu de plateau - Plateau  ------------------------ #

# Bibliothèques utilisées pour le code
import pygame, random
from classe.visuel import texte, couleur, rectangle, image
from classe.personnage import ennemis

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
                
        # Définir les noms des cases
        self.__nom_case = {
            couleur.Couleur().getRouge(): image.Plateau.BOSS.value,
            couleur.Couleur().getRose(): image.Plateau.CHANCE.value,
            couleur.Couleur().getOrange(): image.Plateau.MALUS.value,
            couleur.Couleur().getIndigo(): image.Plateau.TELEPORTATION.value,
            couleur.Couleur().getViolet(): image.Plateau.REJOUE.value,
            couleur.Couleur().getVert(): image.Plateau.ALEATOIRE.value,
            couleur.Couleur().getBeige(): image.Plateau.SORCIERE.value,
            couleur.Couleur().getGris(): image.Plateau.SPECIALE.value,
            couleur.Couleur().getBleu(): image.Plateau.PUIT.value,
            couleur.Couleur().getBlanc(): image.Plateau.VIDE.value,
            couleur.Couleur().getNoir(): image.Plateau.MORT.value,
            couleur.Couleur().getJaune(): image.Plateau.DEPART.value
        }
        
        self.__max_couleur = {
            couleur.Couleur().getRouge(): 4,
            couleur.Couleur().getRose(): 26,
            couleur.Couleur().getOrange(): 29,
            couleur.Couleur().getIndigo(): 2,
            couleur.Couleur().getViolet(): 20,
            couleur.Couleur().getVert(): 20,
            couleur.Couleur().getBeige(): 1,
            couleur.Couleur().getGris(): 10,
            couleur.Couleur().getBleu(): 1,
            couleur.Couleur().getNoir(): 1,
            couleur.Couleur().getJaune():1,
            couleur.Couleur().getBlanc():55
        }

        self.__cases_decouvertes = []
        
        self.remplirPlateauAleatoirement()

        for ligne in range(10):
            for colonne in range(17):
                self.__cases_decouvertes.append((ligne, colonne))

    def getPlateau(self):
        """Renvoie le plateau de jeu."""
        return self.__plateau   
    
    def getNomCase(self):
        """Renvoie le nom_case de jeu."""
        return self.__nom_case
    
    def getCasesDecouvertes(self):
        """Renvoie les cases decouvertes de jeu."""
        return self.__cases_decouvertes

    def getCases(self, ligne, colonne):
        """Renvoie la couleur de la case à la position spécifiée."""
        return self.getPlateau()[ligne][colonne]
        
    def getNom(self, ligne, colonne):
        """Renvoie le nom de la case à la position spécifiée."""
        couleur_case = self.getPlateau()[ligne][colonne]  # Obtenir la couleur de la case
        nom_case = self.__nom_case[couleur_case]
        return nom_case
    
    def getCaseJaune(self):
        """Renvoie les coordonnées correspondant à la case jaune."""
        for ligne in range(10):
            for colonne in range(17):
                if self.getPlateau()[ligne][colonne] == couleur.Couleur().getJaune():
                    coord_case_jaune = (ligne, colonne)
        return coord_case_jaune

    def getCaseIndigo(self, joueur):
        """Renvoie les coordonnées correspondant aux cases indigo."""
        for ligne in range(10):
            for colonne in range(17):
                if self.getPlateau()[ligne][colonne] == couleur.Couleur().getIndigo():
                    if joueur.getPlateauX() == ligne and joueur.getPlateauY() == colonne:
                        pass
                    else:
                        coord_case_indigo = (ligne, colonne)
        return coord_case_indigo

    def setPlateau(self, plateau):
        """Modifie le plateau de jeu."""
        self.__plateau = plateau

    def setCasesDecouvertes(self, cases_decouvertes):
        """Modifie les cases decouvertes de jeu."""
        self.__cases_decouvertes = cases_decouvertes
        
    def remplirPlateauAleatoirement(self):
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

