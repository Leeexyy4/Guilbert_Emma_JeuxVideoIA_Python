#BEAUREPAIRE Paul
#GUILBERT Emma
#VAXELAIRE Yohem
#VERFAILLIE Alexis


# ----------------------- Jeu de plateau - Bibliotheques  ------------------------ #

# Bibliotheques utilisees pour le code
import pygame
from classe.jeu import interface, plateau, logique
from enum import Enum

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
    ACTIONCASE = 13
    SORCIERE = 14
    FIN = 15

# ----------------------- Jeu de plateau - Logique du jeu ------------------------ #
class Main:
    def __init__(self):
        self.plateau = plateau.Plateau()
        self.logique = logique.Logique()
        self.interface = interface.Interface()
        self.pageActuel = PageState.DEMARRAGE

    def PageDemarrage(self):
        self.interface.affichagePageDemarrage()
        self.pageActuel = self.logique.actionPageDemarrage()

    def PageStatistiques(self):
        self.interface.affichagePageStatistiques()
        self.logique.actionPageStatistiques()

    def PageCommande(self):
        self.interface.affichagePageCommande()
        self.logique.actionPageCommande()

    def PageChoixPersonnage(self):
        self.interface.affichagePageChoixPersonnage()
        self.logique.actionPageChoixPersonnage()

    def PageNbJoueur(self):
        self.interface.affichagePageNbJoueur()
        self.logique.actionPageNbJoueur()

    def PageNbIntelligenceA(self):
        self.interface.affichagePageNbIntelligenceA()
        self.logique.actionPageNbIntelligenceA()
        
    def PagePremierMouvement(self, joueurActuelId):
        self.interface.affichagePagePremierMouvement(joueurActuelId)
        self.logique.actionPagePremierMouvement()

    def PageMouvement(self, joueurActuelId):
        self.interface.affichagePageMouvement(joueurActuelId)
        self.logique.actionPageMouvement()

    def PageDirection(self, joueurActuelId):
        self.interface.affichagePageDirection(joueurActuelId)
        self.logique.actionPageDirection()

    def PageHorsPlateau(self, joueurActuelId , faceChoisie):
        self.interface.affichagePageHorsPlateau(joueurActuelId, faceChoisie)
        self.logique.actionPageHorsPlateau()

    def PageRejouer(self, joueurActuelId):
        self.interface.affichagePageRejouer(joueurActuelId)
        self.logique.actionPageRejouer()

    def PageAttaque(self, joueurActuelId):
        self.interface.affichagePageAttaque(joueurActuelId)
        self.logique.actionPageAttaque()

    def PageActionCases(self, joueurActuelId):
        self.interface.affichagePageActionCases(joueurActuelId)
        self.logique.actionPageActionCases()

    def PageSorciere(self, joueurActuelId):
        self.interface.affichagePageSorciere(joueurActuelId)
        self.logique.actionPageSorciere()

    def PageFin(self):
        self.interface.affichagePageFin()
        self.logique.actionPageFin()
        if self.interface.getListeJoueur() == None:
            self.interface.PageFin()
        else:
            for joueurActuel in self.interface.getListeJoueur():
                if joueurActuel.aGagner(self.interface.getPlateauJeu()) == True:
                    joueurActuel.set_inventaire([])
                    self.interface.PageSorciere(joueurActuel)

if __name__ == "__main__":
    # Initialisation du jeu
    pygame.init()
    self = Main()

    # Boucle de jeu pour tous les joueurs encore en vie
    while self.pageActuel != PageState.FIN:
        if self.pageActuel == PageState.DEMARRAGE:
            self.PageDemarrage()

        elif self.pageActuel is PageState.STATISTIQUE:
            self.PageStatistiques()

        elif self.pageActuel == PageState.COMMANDE:
            self.PageCommande()

        elif self.pageActuel == PageState.CHOIXPERSONNAGE:
            self.PageChoixPersonnage()

        elif self.pageActuel == PageState.NBJOUEUR:
            self.PageNbJoueur()
            
        elif self.pageActuel == PageState.NBIA:
            self.PageNbIntelligenceA()

        elif self.pageActuel == PageState.PREMIERMOUVEMENT:
            self.PagePremierMouvement()
        
        elif self.pageActuel == PageState.MOUVEMENT:
            self.PageMouvement()
            
        elif self.pageActuel == PageState.DIRECTION:
            self.PageDirection()

        elif self.pageActuel == PageState.HORSPLATEAU:
            self.PageHorsPlateau()

        elif self.pageActuel == PageState.REJOUER:
            self.PageRejouer()
            
        elif self.pageActuel == PageState.ATTAQUE:
            self.PageAttaque()

        elif self.pageActuel == PageState.ACTIONCASE:
            self.PageActionCases()

        elif self.pageActuel == PageState.SORCIERE:
            self.PageSorciere()

        # Mettre à jour l'affichage
        pygame.display.update()
