from enum import Enum
from classe.jeu import plateau
from classe.visuel import de

class PageState(Enum):
    DEMARRAGE = 1
    STATISTIQUE = 2
    COMMANDE = 3
    CHOIXPERSONNAGE = 4
    NBJOUEUR = 5
    NBIA = 6
    PREMIERMOUVEMENT = 7
    MOUVEMENT = 8
    DIRECTION = 9
    HORSPLATEAU = 10
    REJOUER = 11
    ATTAQUE = 12
    COMBAT = 13
    ACTIONCASE = 14
    ACTIONCASEBEIGE = 15
    ACTIONCASEBLANC = 16
    ACTIONCASEBLEU = 17
    ACTIONCASEGRIS = 18
    ACTIONCASEINDIGO = 19
    ACTIONCASEJAUNE = 20
    ACTIONCASEORANGE = 21
    ACTIONCASENOIR = 22
    ACTIONCASEROUGE = 23
    ACTIONCASEROSE = 24
    ACTIONCASEVERT = 25
    ACTIONCASEVIOLET = 26
    SORCIERE = 27
    SORCIEREASTRAL = 28
    SORCIEREDRAGON = 29
    SORCIEREPOTION = 30
    FINGAGNE = 31
    FINPERDU = 32

class Game:
    def __init__(self):
        self.__plateau = plateau.Plateau()
        self.__listeJoueurs = []
        self.__joueurActuel = None
        self.__de = de.De()
        self.__pageActuel = PageState.DEMARRAGE
        self.__horsLigneOuLigne = None
        self.__nbJoueur = -1
        self.__nbIntelligenceA = -1
 
    # Getters
    def getPlateau(self):
        """Getter du plateau."""
        return self.__plateau

    def getListeJoueurs(self):
        """Getter de la liste des joueurs."""
        return self.__listeJoueurs

    def getJoueurActuel(self):
        """Getter du joueur actuel."""
        return self.__joueurActuel
    
    def getPageActuel(self):
        """Getter de la page actuelle."""
        return self.__pageActuel
    
    def getDe(self):
        """Getter du dé."""
        return self.__de
    
    def getHorsLigneOuLigne(self):
        """Getter du mode de jeu."""
        return self.__horsLigneOuLigne
    
    def getNbJoueur(self):
        """Getter du nb de joueur."""
        return self.__nbJoueur
    
    def getNbIntelligenceA(self):
        """Getter du nb d'IA."""
        return self.__nbIntelligenceA
    
    # Setters
    def setPlateau(self, plateau):
        """Setter du plateau."""
        self.__plateau = plateau

    def setListeJoueurs(self, listeJoueurs):
        """Setter de la liste des joueurs."""
        self.__listeJoueurs = listeJoueurs

    def setJoueurActuel(self, joueurActuel):
        """Setter du joueur actuel."""
        self.__joueurActuel = joueurActuel
    
    def setPageActuel(self, pageActuel):
        """Setter de la page actuelle."""
        self.__pageActuel = pageActuel

    def setNbJoueur(self, nbJoueur):
        """Setter du nb de joueur."""
        self.__nbJoueur = nbJoueur

    def setNbIntelligenceA(self, nbIntelligenceA):
        """Setter du nb d'IA."""
        self.__nbIntelligenceA = nbIntelligenceA

    def setHorsLigneOuLigne(self, horsLigneOuLigne):
        """Setter du mode de jeu."""
        self.__horsLigneOuLigne = horsLigneOuLigne

    def joueurSuivant(self):
        """Fait passer au joueur suivant dans la liste."""
        if self.__joueurActuel is None:
            self.__joueurActuel = self.__listeJoueurs[0]
        else:
            index_actuel = self.__listeJoueurs.index(self.__joueurActuel)
            index_suivant = (index_actuel + 1) % len(self.__listeJoueurs)
            self.__joueurActuel = self.__listeJoueurs[index_suivant]

        return self.__joueurActuel
