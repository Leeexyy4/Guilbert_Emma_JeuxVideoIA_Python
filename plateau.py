from utils import couleur 

class Plateau():
    nom_case:dict = {
            couleur.Couleur().get_Rousge(): "Boss",
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
    max_couleur:dict = {
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
    taille_case = 800 // 17
    def __init__(self) -> None:
        """_summary_
            Initialisation du Plateau
        """
        # Définir le plateau
        self.__plateau:list = []
        # Définir la taille d'une case
        self.__cases_decouvertes:list = []
        for ligne in range(10):
            for colonne in range(17):
                self.__cases_decouvertes.append((ligne, colonne))
        
        self.remplir_plateau_aleatoirement()
                

    def get_nb_IA(self)-> int:
        return self.__nb_IA
    def get_nb_players(self)-> int:
        return self.__nb_player

    def get_plateau(self):
        """Renvoie le plateau de jeu."""
        return self.__plateau
    def get_nom_case(self):
        """Renvoie le nom_case de jeu."""
        return self.__nom_case
    
    def get_cases_decouvertes(self):
        """Renvoie les cases decouvertes de jeu."""
        return self.__cases_decouvertes

    def get_cases(self, ligne, colonne):
        """Renvoie la couleur de la case à la position spécifiée."""
        return self.get_plateau()[ligne][colonne]
        
    def get_nom(self, ligne, colonne):
        """Renvoie le nom de la case à la position spécifiée."""
        couleur_case = self.get_plateau()[ligne][colonne]  # Obtenir la couleur de la case
        nom_case = self.__nom_case[couleur_case]
        return nom_case
    
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

    
    def set_plateau(self, plateau):
        """Modifie le plateau de jeu."""
        self.__plateau = plateau

    def set_cases_decouvertes(self, cases_decouvertes):
        """Modifie les cases decouvertes de jeu."""
        self.__cases_decouvertes = cases_decouvertes
        
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