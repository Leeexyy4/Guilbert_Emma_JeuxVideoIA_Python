from utils.logique import CASE_TYPE
import random
class Plateau():
    """La classe Plateau définit le type des cases présentes sur le plateau."""

    def __init__(self) -> None:
        """_summary_
            Initialisation du Plateau
        """
        # Définir le plateau
        self.__plateau:list[CASE_TYPE] = []
        self.__casesDecouvertes:list = []
        self.__tailleCase = 800 // 17

        self.__nomCase:dict = {
            CASE_TYPE.BOSS: "Boss",
            CASE_TYPE.BONUS: "Chance",
            CASE_TYPE.MALUS: "Malus",
            CASE_TYPE.POUF: "Pouf",
            CASE_TYPE.REJOUE: "Rejoue",
            CASE_TYPE.GRRR: "Grrr",
            CASE_TYPE.HUTTE: "Hutte",
            CASE_TYPE.SPECIALE: "Spéciale",
            CASE_TYPE.PUIT: "Puit",
            CASE_TYPE.VIDE: "Vide",
            CASE_TYPE.MORT: "Mort",
            CASE_TYPE.DEPART: "Départ"
        }

        self.__maxCases:dict = {
            CASE_TYPE.BOSS: 4,
            CASE_TYPE.BONUS: 26,
            CASE_TYPE.MALUS: 29,
            CASE_TYPE.POUF: 2,
            CASE_TYPE.REJOUE: 20,
            CASE_TYPE.GRRR: 20,
            CASE_TYPE.HUTTE: 1,
            CASE_TYPE.SPECIALE: 10,
            CASE_TYPE.PUIT: 1,
            CASE_TYPE.MORT: 1,
            CASE_TYPE.DEPART:1,
            CASE_TYPE.VIDE:55
        }
        self.remplirPlateauAleatoirement()
        self.setCasesDecouvertes(self.getCasesDecouvertes() + [[self.getCaseJaune()[0], self.getCaseJaune()[1]]])   
        for ligne in range(10):
            for colonne in range(17):
                self.setCasesDecouvertes(self.getCasesDecouvertes() + [[ligne, colonne]])     

    def getPlateau(self):
        """Renvoie le plateau de jeu."""
        return self.__plateau

    def getMaxCase(self):
        """Renvoie le plateau de jeu."""
        return self.__maxCases
    
    def getTailleCase(self):
        """Renvoie le plateau de jeu."""
        return self.__tailleCase

    def getNomCase(self):
        """Renvoie le nom_case de jeu."""
        return self.__nomCase
    
    def getCasesDecouvertes(self):
        """Renvoie les cases decouvertes de jeu."""
        return self.__casesDecouvertes

    def getCases(self, ligne, colonne):
        """Renvoie la couleur de la case à la position spécifiée."""
        return self.getPlateau()[ligne][colonne]
        
    def getNom(self, ligne, colonne):
        """Renvoie le nom de la case à la position spécifiée."""
        couleur_case = self.getPlateau()[ligne][colonne]  # Obtenir la couleur de la case
        nom_case = self.getNomCase()[couleur_case]
        return nom_case
    
    def getCaseJaune(self):
        """Renvoie les coordonnées correspondant à la case jaune."""
        for ligne in range(10):
            for colonne in range(17):
                if self.getPlateau()[ligne][colonne] == CASE_TYPE.SPAWN:
                    coord_case_jaune = (ligne, colonne)
        return coord_case_jaune

    def getCaseIndigo(self, joueur):
        """Renvoie les coordonnées correspondant aux cases indigo."""
        for ligne in range(10):
            for colonne in range(17):
                if self.getPlateau()[ligne][colonne] == CASE_TYPE.TP:
                    if joueur.getPlateaux() == ligne and joueur.getPlateauy() == colonne:
                        pass
                    else:
                        joueur.setPlateaux(ligne); joueur.setPlateauy(colonne)

    def setPlateau(self, plateau):
        """Modifie le plateau de jeu."""
        self.__plateau = plateau

    def setCasesDecouvertes(self, casesDecouvertes):
        """Modifie les cases decouvertes de jeu."""
        self.__casesDecouvertes = casesDecouvertes
        
    def remplirPlateauAleatoirement(self):
        """Remplit le plateau de manière aléatoire en fonction de max_couleur."""
        # Crée une liste des couleurs disponibles en fonction de max_couleur
        couleursDisponibles = []
        for couleurs, nombreMax in self.getMaxCase().items():
            couleursDisponibles.extend([couleurs] * nombreMax)

         # Remplit le plateau de manière aléatoire
        for i in range(10):
            lignePlateau = []
            for j in range(17):
                if couleursDisponibles:  # Vérifiez si des couleurs sont disponibles
                    couleur_aleatoire = random.choice(couleursDisponibles)
                    couleursDisponibles.remove(couleur_aleatoire)  # Supprime la couleur de la liste
                    lignePlateau.append(couleur_aleatoire)
        
            self.getPlateau().append(lignePlateau)
        return self.getPlateau()