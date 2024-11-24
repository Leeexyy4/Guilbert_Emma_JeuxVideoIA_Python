#BEAUREPAIRE Paul
#GUILBERT Emma
#VAXELAIRE Yohem
#VERFAILLIE Alexis


# ----------------------- Jeu de plateau - Bibliotheques  ------------------------ #

# Bibliotheques utilisees pour le code
import pygame
from classe.jeu import interface, logique, game
from classe.jeu.game import PageState

# ----------------------- Jeu de plateau - Logique du jeu ------------------------ #
class Main:
    def __init__(self):
        self.__game = game.Game()
        self.__logique = logique.Logique(self.getGame())
        self.__interface = interface.Interface(self.getGame())

# ----------------------------------- Getter des élements ----------------------------------- #
        
    def getLogique(self):
        """Getter de la liste de joueur."""
        return self.__logique

    def getInterface(self):
        """Getter du nb de joueur."""
        return self.__interface
        
    def getGame(self):
        """Getter des variables globales du jeu."""
        return self.__game

# ----------------------------------- Page du jeu ----------------------------------- #

    def PageDemarrage(self):
        self.getInterface().affichagePageDemarrage()
        self.getLogique().actionPageDemarrage()

    def PageStatistiques(self):
        self.getInterface().affichagePageStatistiques()
        self.getLogique().actionPageStatistiques()

    def PageCommande(self):
        self.getInterface().affichagePageCommande()
        self.getLogique().actionPageCommande()

    def PageNbJoueur(self):
        self.getInterface().affichagePageNbJoueur()
        self.getLogique().actionPageNbJoueur()

    def PageNbIntelligenceA(self):
        self.getInterface().affichagePageNbIntelligenceA()
        self.getLogique().actionPageNbIntelligenceA()

    def PageChoixPersonnage(self):
        self.getInterface().affichagePageChoixPersonnage()
        self.getLogique().actionPageChoixPersonnage()
        
    def PagePremierMouvement(self):
        self.getInterface().affichagePagePremierMouvement()
        self.getLogique().actionPagePremierMouvement()

    def PageMouvement(self):
        self.getInterface().affichagePageMouvement()
        self.getLogique().actionPageMouvement()

    def PageDirection(self):
        self.getInterface().affichagePageDirection()
        self.getLogique().actionPageDirection()

    def PageHorsPlateau(self):
        self.getInterface().affichagePageHorsPlateau()
        self.getLogique().actionPageHorsPlateau()

    def PageRejouer(self):
        self.getInterface().affichagePageRejouer()
        self.getLogique().actionPageRejouer()

    def PageAttaque(self):
        self.getInterface().affichagePageAttaque()
        self.getLogique().actionPageAttaque()

    def PageActionCases(self):
        self.getInterface().affichagePageActionCases()
        self.getLogique().actionPageActionCases()

    def PageActionCasesBeige(self):
        self.getInterface().affichagePageActionBeige()
        self.getLogique().actionPageActionBeige()

    def PageActionCasesBlanc(self):
        self.getInterface().affichagePageActionBlanc()
        self.getLogique().actionPageActionBlanc()

    def PageActionCasesBleu(self):
        self.getInterface().affichagePageActionBleu()
        self.getLogique().actionPageActionBleu()

    def PageActionCasesGris(self):
        self.getInterface().affichagePageActionGris()
        self.getLogique().actionPageActionGris()

    def PageActionCasesIndigo(self):
        self.getInterface().affichagePageActionIndigo()
        self.getLogique().actionPageActionIndigo()

    def PageActionCasesJaune(self):
        self.getInterface().affichagePageActionJaune()
        self.getLogique().actionPageActionJaune()

    def PageActionCasesOrange(self):
        self.getInterface().affichagePageActionGris()
        self.getLogique().actionPageActionGris()

    def PageActionCasesNoir(self):
        self.getInterface().affichagePageActionNoir()
        self.getLogique().actionPageActionNoir()

    def PageActionCasesRouge(self):
        self.getInterface().affichagePageActionRouge()
        self.getLogique().actionPageActionRouge()

    def PageActionCasesRose(self):
        self.getInterface().affichagePageActionRose()
        self.getLogique().actionPageActionRose()

    def PageActionCasesVert(self):
        self.getInterface().affichagePageActionVert()
        self.getLogique().actionPageActionVert()

    def PageActionCasesViolet(self):
        self.getInterface().affichagePageActionViolet()
        self.getLogique().actionPageActionViolet()

    def PageSorciere(self):
        self.getInterface().affichagePageSorciere()
        self.getLogique().actionPageSorciere()

    def PageSorciereAstral(self):
        self.getInterface().affichagePageSorciereAstral()
        self.getLogique().actionPageSorciereAstral()

    def PageSorciereDragon(self):
        self.getInterface().affichagePageSorciereDragon()
        self.getLogique().actionPageSorciereDragon()

    def PageSorcierePotion(self):
        self.getInterface().affichagePageSorcierePotion()
        self.getLogique().actionPageSorcierePotion()

    def PageFinGagne(self):
        self.getInterface().affichagePageFinGagne()
        self.getLogique().actionPageFinGagne()

    def PageFinPerdu(self):
        self.getInterface().affichagePageFinPerdu()
        self.getLogique().actionPageFinPerdu()

if __name__ == "__main__":
    # Initialisation du jeu
    pygame.init()
    self = Main()

    # Boucle de jeu pour tous les joueurs encore en vie
    while self.getGame().getPageActuel() != PageState.FINGAGNE or  self.getGame().getPageActuel() != PageState.FINPERDU:
        if self.getGame().getPageActuel().value is PageState.DEMARRAGE.value:
            self.PageDemarrage()

        elif self.getGame().getPageActuel().value is PageState.STATISTIQUE.value:
            self.PageStatistiques()

        elif self.getGame().getPageActuel().value == PageState.COMMANDE.value:
            self.PageCommande()

        elif self.getGame().getPageActuel().value == PageState.NBJOUEUR.value:
            self.PageNbJoueur()
            
        elif self.getGame().getPageActuel().value == PageState.NBIA.value:
            self.PageNbIntelligenceA()

        elif self.getGame().getPageActuel().value == PageState.CHOIXPERSONNAGE.value:
            self.PageChoixPersonnage()

        elif self.getGame().getPageActuel().value == PageState.PREMIERMOUVEMENT.value:
            self.PagePremierMouvement()
        
        elif self.getGame().getPageActuel().value == PageState.MOUVEMENT.value:
            self.PageMouvement()
            
        elif self.getGame().getPageActuel().value == PageState.DIRECTION.value:
            self.PageDirection()

        elif self.getGame().getPageActuel().value == PageState.HORSPLATEAU.value:
            self.PageHorsPlateau()

        elif self.getGame().getPageActuel().value == PageState.REJOUER.value:
            self.PageRejouer()
            
        elif self.getGame().getPageActuel().value == PageState.ATTAQUE.value:
            self.PageAttaque()

        elif self.getGame().getPageActuel().value == PageState.ACTIONCASE.value:
            self.PageActionCases()

        elif self.getGame().getPageActuel().value == PageState.ACTIONCASEBEIGE.value:
            self.PageActionCasesBeige()

        elif self.getGame().getPageActuel().value == PageState.ACTIONCASEBLANC.value:
            self.PageActionCasesBlanc()

        elif self.getGame().getPageActuel().value == PageState.ACTIONCASEBLEU.value:
            self.PageActionCasesBleu()

        elif self.getGame().getPageActuel().value == PageState.ACTIONCASEGRIS.value:
            self.PageActionCasesGris()

        elif self.getGame().getPageActuel().value == PageState.ACTIONCASEINDIGO.value:
            self.PageActionCasesIndigo()

        elif self.getGame().getPageActuel().value == PageState.ACTIONCASEJAUNE.value:
            self.PageActionCasesJaune()

        elif self.getGame().getPageActuel().value == PageState.ACTIONCASENOIR.value:
            self.PageActionCasesNoir()

        elif self.getGame().getPageActuel().value == PageState.ACTIONCASEORANGE.value:
            self.PageActionCasesOrange()

        elif self.getGame().getPageActuel().value == PageState.ACTIONCASEROUGE.value:
            self.PageActionCasesRouge()

        elif self.getGame().getPageActuel().value == PageState.ACTIONCASEROSE.value:
            self.PageActionCasesRose()

        elif self.getGame().getPageActuel().value == PageState.ACTIONCASEVERT.value:
            self.PageActionCasesVert()

        elif self.getGame().getPageActuel().value == PageState.ACTIONCASEVIOLET.value:
            self.PageActionCasesViolet()

        elif self.getGame().getPageActuel().value == PageState.SORCIERE.value:
            self.PageSorciere()

        elif self.getGame().getPageActuel().value == PageState.SORCIEREASTRAL.value:
            self.PageSorciereAstral()

        elif self.getGame().getPageActuel().value == PageState.SORCIEREDRAGON.value:
            self.PageSorciereDragon()

        elif self.getGame().getPageActuel().value == PageState.SORCIEREPOTION.value:
            self.PageSorcierePotion()

        elif self.getGame().getPageActuel().value == PageState.FINGAGNE.value:
            self.PageFinGagne()

        elif self.getGame().getPageActuel().value == PageState.FINPERDU.value:
            self.PageFinGagne()

        # Mettre à jour l'affichage
        pygame.display.update()
