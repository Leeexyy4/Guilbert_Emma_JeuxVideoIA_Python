#  ----------------------- Jeu de plateau - Interface ------------------------ #

# Bibliothèques utilisées pour le code
import pygame, random
from classe.personnage import joueur, intelA
from classe.visuel import couleur
from classe.jeu.game import PageState

# ----------------------- Jeu de plateau - Logique ------------------------ #
class Logique:
    def __init__(self, game) -> None:
        """Initialisation de l'interface."""
        self.__mouse = pygame.mouse
        self.__game = game
        self.__couleur = couleur.Couleur()

# ----------------------------------- Getter des élements ----------------------------------- #

    def getMouse(self):
        """Getter de la fenetre."""
        return self.__mouse
    
    def getCouleur(self):
        """Getter du nb d'IA."""
        return self.__couleur

    def getGame(self):
        """Getter du nb d'IA."""
        return self.__game

# ----------------------------------- Affichage des élements ----------------------------------- #
        
    def actionPageDemarrage(self): 
        demarrage = True
        while (demarrage):
            mouse_x, mouse_y = self.getMouse().get_pos()
            for event in pygame.event.get():
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    if (320 <= mouse_x <= 470 and 500 <= mouse_y <= 550) : # Stats
                        demarrage = False
                        self.getGame().setPageActuel(PageState.STATISTIQUE)
                    if (170 <= mouse_x <= 350 and 550 <= mouse_y <= 600) : # En local
                        demarrage = False
                        self.getGame().setHorsLigneOuLigne("HL")
                        self.getGame().setPageActuel(PageState.NBJOUEUR)
                    if (450 <= mouse_x <= 630 and 550 <= mouse_y <= 600) : # En ligne
                        demarrage = False
                        self.getGame().setHorsLigneOuLigne("EL")
                        self.getGame().setPageActuel(PageState.NBJOUEUR)
                    if (700 <= mouse_x <= 764 and 25 <= mouse_y <= 89) : # Info
                        demarrage = False
                        self.getGame().setPageActuel(PageState.COMMANDE)
                    if (10 <= mouse_x <= 70 and 630 <= mouse_y <= 690): # Retour
                        demarrage = False
                        self.getGame().setPageActuel(PageState.DEMARRAGE)
                if (event.type == pygame.QUIT): # Quitter
                    pygame.quit()
                    exit()

    def actionPageStatistiques(self):
        stats = True
        while (stats):
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    if (40 <= mouse_x <= 100 and 40 <= mouse_y <= 100): # Retour
                        stats = False
                        self.getGame().setPageActuel(PageState.DEMARRAGE)
                if (event.type == pygame.QUIT): # Quitter
                    pygame.quit()
                    exit()

    def actionPageCommande(self):
        commande = True
        while (commande):
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    if (20 <= mouse_x <= 70 and 630 <= mouse_y <= 680): # Retour
                        commande = False
                        self.getGame().setPageActuel(PageState.DEMARRAGE)
                if (event.type == pygame.QUIT): # Quitter
                    pygame.quit()
                    exit()

    def actionPageNbJoueur(self):
        nbJoueur = True
        while (nbJoueur):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN :
                    mouse_x, mouse_y = pygame.mouse.get_pos() 
                    if (40 <= mouse_x <= 100 and 40 <= mouse_y <= 100) : # Retour
                        nbJoueur = False
                        self.getGame().setNbJoueur(None)
                        self.getGame().setPageActuel(PageState.DEMARRAGE)
                    if (220 <= mouse_x <= 290 and 470 <= mouse_y <= 540) : # 1 joueur
                        nbJoueur = False
                        self.getGame().setNbJoueur(1)
                        self.getGame().setPageActuel(PageState.NBIA)
                    if (320 <= mouse_x <= 390 and 470 <= mouse_y <= 540) : # 2 joueurs
                        nbJoueur = False
                        self.getGame().setNbJoueur(2)
                        self.getGame().setPageActuel(PageState.NBIA)
                    if (420 <= mouse_x <= 490 and 470 <= mouse_y <= 540) : # 3 joueurs
                        nbJoueur = False
                        self.getGame().setNbJoueur(3)
                        self.getGame().setPageActuel(PageState.NBIA)
                    if (520 <= mouse_x <= 590 and 470 <= mouse_y <= 540) : # 4 joueurs
                        nbJoueur = False
                        self.getGame().setNbJoueur(4)
                        self.getGame().setPageActuel(PageState.NBIA)
                if event.type == pygame.QUIT: # Quitter
                    pygame.quit()
                    exit()

    def actionPageNbIntelligenceA(self):
        nbIA = True
        while (nbIA):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN :
                    mouse_x, mouse_y = pygame.mouse.get_pos() 
                    if (40 <= mouse_x <= 100 and 40 <= mouse_y <= 100) :
                        nbIA = False
                        self.getGame().setNbIntelligenceA(None)
                        self.getGame().setPageActuel(PageState.CHOIXPERSONNAGE)
                    if (220 <= mouse_x <= 290 and 470 <= mouse_y <= 540 and (self.getGame().getNbJoueur() == 1 or self.getGame().getNbJoueur() == 2 or self.getGame().getNbJoueur() == 3 or self.getGame().getNbJoueur() == 4)):   
                        nbIA = False
                        self.getGame().setNbIntelligenceA(0)
                        self.getGame().setPageActuel(PageState.CHOIXPERSONNAGE)
                    if (320 <= mouse_x <= 390 and 470 <= mouse_y <= 540 and (self.getGame().getNbJoueur() == 1 or self.getGame().getNbJoueur() == 2 or self.getGame().getNbJoueur() == 3)):
                        nbIA = False
                        self.getGame().setNbIntelligenceA(1)
                        self.getGame().setPageActuel(PageState.CHOIXPERSONNAGE)
                    if (420 <= mouse_x <= 490 and 470 <= mouse_y <= 540 and (self.getGame().getNbJoueur() == 1 or self.getGame().getNbJoueur() == 2)):   
                        nbIA = False
                        self.getGame().setNbIntelligenceA(2)
                        self.getGame().setPageActuel(PageState.CHOIXPERSONNAGE)
                    if (520 <= mouse_x <= 590 and 470 <= mouse_y <= 540 and self.getGame().getNbJoueur() == 1):   
                        nbIA = False
                        self.getGame().setNbIntelligenceA(3)
                        self.getGame().setPageActuel(PageState.CHOIXPERSONNAGE)
                if event.type == pygame.QUIT: # Quitter
                    pygame.quit()
                    exit()

    def actionPageChoixPersonnage(self):
        choixPerso = True
        while (choixPerso) :
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN : 
                    mouse_x, mouse_y = pygame.mouse.get_pos() 
                    if (220 <= mouse_x <= 290 and 470 <= mouse_y <= 540): # Pierre
                        self.getGame().setListeJoueurs(self.getGame().getListeJoueurs() + [joueur.Joueur(len(self.getGame().getListeJoueurs()), "Pierre", "du Rocher", self.getGame().getPlateau().getCaseJaune()[0], self.getGame().getPlateau().getCaseJaune()[1])])
                        self.getGame().setJoueurActuel(self.getGame().getListeJoueurs()[len(self.getGame().getListeJoueurs()) -1])
                        choixPerso = False
                        self.getGame().setPageActuel(PageState.PREMIERMOUVEMENT)
                    if (320 <= mouse_x <= 390 and 470 <= mouse_y <= 540): # Ondine
                        self.getGame().setListeJoueurs(self.getGame().getListeJoueurs() + [joueur.Joueur(len(self.getGame().getListeJoueurs()), "Ondine", "de la Rivière", self.getGame().getPlateau().getCaseJaune()[0], self.getGame().getPlateau().getCaseJaune()[1])])
                        self.getGame().setJoueurActuel(self.getGame().getListeJoueurs()[len(self.getGame().getListeJoueurs()) -1])
                        choixPerso = False
                        self.getGame().setPageActuel(PageState.PREMIERMOUVEMENT)
                    if (420 <= mouse_x <= 490 and 470 <= mouse_y <= 540): # Kevin
                        self.getGame().setListeJoueurs(self.getGame().getListeJoueurs() + [joueur.Joueur(len(self.getGame().getListeJoueurs()), "Kevin", "de la Ville", self.getGame().getPlateau().getCaseJaune()[0], self.getGame().getPlateau().getCaseJaune()[1])])
                        self.getGame().setJoueurActuel(self.getGame().getListeJoueurs()[len(self.getGame().getListeJoueurs()) -1])
                        choixPerso = False
                        self.getGame().setPageActuel(PageState.PREMIERMOUVEMENT)
                    if (520 <= mouse_x <= 590 and 470 <= mouse_y <= 540): # Flora
                        self.getGame().setListeJoueurs(self.getGame().getListeJoueurs() + [joueur.Joueur(len(self.getGame().getListeJoueurs()), "Flora", "de la Forêt", self.getGame().getPlateau().getCaseJaune()[0], self.getGame().getPlateau().getCaseJaune()[1])])
                        self.getGame().setJoueurActuel(self.getGame().getListeJoueurs()[len(self.getGame().getListeJoueurs()) -1])
                        choixPerso = False
                        self.getGame().setPageActuel(PageState.PREMIERMOUVEMENT)
                if event.type == pygame.QUIT: # Quitter
                    pygame.quit()
                    exit()
        
    def actionPagePremierMouvement(self):
        premierMouvement = True
        while (premierMouvement):
            mouse_x, mouse_y = pygame.mouse.get_pos() 
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:  
                    if 360 < mouse_x < 424 and 475 < mouse_y < 539:
                        premierMouvement = False
                        self.getGame().setPageActuel(PageState.DIRECTION)
                if event.type == pygame.QUIT:  
                    pygame.quit()
                    exit() 

    def actionPageMouvement(self):
        action_joueurActuel = ""
        while (action_joueurActuel == "") :
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN : # Si le joueurActuel clique sur le bouton, on passe à la prochaine page "introduction"
                    mouse_x, mouse_y = pygame.mouse.get_pos() 
                    # Si le personnage sur lequel on clique est Ondine   
                    if (220 <= mouse_x <= 284 and 480 <= mouse_y <= 544) :
                        action_joueurActuel = "Attaquer"
                        self.getGame().setPageActuel(PageState.ATTAQUE)
                    elif (510 <= mouse_x <= 574 and 480 <= mouse_y <= 544):
                        action_joueurActuel = "Lancer"
                        self.getGame().setPageActuel(PageState.DIRECTION)
                if event.type == pygame.QUIT: # si le joueurActuel quitte la fenetre # si le joueurActuel quitte la fenetre
                    pygame.quit()
                    exit()

    def actionPageDirection(self):
        direction = True
        while (direction):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    
                elif event.type == pygame.KEYDOWN:
                    touche_fleche = event.key

                    if touche_fleche == pygame.K_UP:
                        direction = False
                        if (self.getGame().getJoueurActuel().haut(47)):
                            self.getGame().getDe().setFaceDeDesincremente(1)
                        else:
                            self.getGame().setPageActuel(PageState.HORSPLATEAU)
                        
                    elif touche_fleche == pygame.K_DOWN:
                        direction = False
                        if (self.getGame().getJoueurActuel().bas(47)):
                            self.getGame().getDe().setFaceDeDesincremente(1)
                        else:
                            self.getGame().setPageActuel(PageState.HORSPLATEAU)
                    
                    elif touche_fleche == pygame.K_RIGHT:
                        direction = False
                        if (self.getGame().getJoueurActuel().droite(47)):
                            self.getGame().getDe().setFaceDeDesincremente(1)
                        else:
                            self.getGame().setPageActuel(PageState.HORSPLATEAU)
                    
                    elif touche_fleche == pygame.K_LEFT:
                        direction = False
                        if (self.getGame().getJoueurActuel().gauche(47)):
                            self.getGame().getDe().setFaceDeDesincremente(1)
                        else:
                            self.getGame().setPageActuel(PageState.HORSPLATEAU)
        
        if (self.getGame().getDe().getFaceDe() == 0):
            self.getGame().setPageActuel(PageState.ACTIONCASE)

                
                            
    def actionPageHorsPlateau(self):
        self.getGame().setPageActuel(PageState.DIRECTION)

    def actionPageRejouer(self): 
        self.getGame().setPageActuel(PageState.DIRECTION)

    def actionPageAttaque(self): 
        if self.getGame().getJoueurActuel().advDisponible(self.getGame().getListeJoueurs()) != True:
            self.getGame().setPageActuel(PageState.REJOUER)
        else:
            self.getGame().setPageActuel(PageState.COMBAT)

    def actionPageActionCases(self):
        couleur_case = self.getGame().getPlateau().getCases(self.getGame().getJoueurActuel().getPlateauX(), self.getGame().getJoueurActuel().getPlateauY())
        
        if self.getGame().getJoueurActuel().getPv() != 0:
            if couleur_case == self.getCouleur().getBeige():
                self.getGame().setPageActuel(PageState.ACTIONCASEBEIGE)
                
            elif couleur_case == self.getCouleur().getBlanc():
                self.getGame().setPageActuel(PageState.ACTIONCASEBLANC)

            elif couleur_case == self.getCouleur().getBleu():
                self.getGame().setPageActuel(PageState.ACTIONCASEBLEU)
                        
            elif couleur_case == self.getCouleur().getGris():
                self.getGame().setPageActuel(PageState.ACTIONCASEGRIS)
                
            elif couleur_case == self.getCouleur().getIndigo():
                self.getGame().setPageActuel(PageState.ACTIONCASEINDIGO)
                
            elif couleur_case == self.getCouleur().getJaune():
                self.getGame().setPageActuel(PageState.ACTIONCASEJAUNE)

            elif couleur_case == self.getCouleur().getNoir():
                self.getGame().setPageActuel(PageState.ACTIONCASENOIR)
                
            elif couleur_case == self.getCouleur().getOrange():
                self.getGame().setPageActuel(PageState.ACTIONCASEORANGE)

            elif couleur_case == self.getCouleur().getRose():
                self.getGame().setPageActuel(PageState.ACTIONCASEROSE)
                
            elif couleur_case == self.getCouleur().getRouge():
                self.getGame().setPageActuel(PageState.ACTIONCASEROUGE)
                
            elif couleur_case == self.getCouleur().getVert():
                self.getGame().setPageActuel(PageState.ACTIONCASEVERT)
                
            elif couleur_case == self.getCouleur().getViolet():
                self.getGame().setPageActuel(PageState.ACTIONCASEVIOLET)

            if (self.getGame().getJoueurActuel().getPv() <= 0):
                self.setListeJoueurs(self.getListeJoueurs().remove(self.getGame().getJoueurActuel()))

    def actionPageSorciere(self):
        selection_potion = False
        while selection_potion != True:
            mouse_x, mouse_y = pygame.mouse.get_pos() 
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # si le joueurActuel quitte la self.getFenetre() # si le joueurActuel quitte la self.getFenetre()
                    pygame.quit()
                    exit() 
                
                if event.type == pygame.MOUSEBUTTONDOWN:  
                    if 500 < mouse_x < 725 and 150 < mouse_y < 450:
                        self.getGame().setPageActuel(PageState.SORCIEREASTRAL)
                    elif 90 < mouse_x < 190 and 180 < mouse_y < 350:
                        self.getGame().setPageActuel(PageState.SORCIEREDRAGON)
                    elif 330 < mouse_x < 430 and 480 < mouse_y < 580:
                        self.getGame().setPageActuel(PageState.SORCIEREPOTION)
    
    def actionPageFin(self):
        selection_fin = False
        while selection_fin != True:
            mouse_x, mouse_y = pygame.mouse.get_pos() 
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # si le joueurActuel quitte la self.getFenetre() # si le joueurActuel quitte la self.getFenetre()
                    pygame.quit()
                    exit() 
                
                
                if event.type == pygame.MOUSEBUTTONDOWN:  
                    if 0 < mouse_x < 800 and 0 < mouse_y < 700:
                        self.getGame().setPageActuel(PageState.STATISTIQUE)

    def actionPageActionBleu(self):
        selection_utilisateur = False
        while selection_utilisateur != True:
            mouse_x, mouse_y = pygame.mouse.get_pos() 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    pygame.quit()
                    exit() 
                
                if event.type == pygame.MOUSEBUTTONDOWN:  
                    if 220 < mouse_x < 284 and 480 < mouse_y < 544:
                        
                        # Si le joueur veut echanger des pv
                        if joueur.getPv() > 200:
                            joueur.setPv(joueur.getPv() - 200)  
                                
                    elif 510 < mouse_x < 574 and 480 < mouse_y < 544:
                        if joueur.get_inventaire() == [] and joueur.getPv() > 200:
                            interface.affichageDialogues(["Tu n'as pas de cles, donne moi 200 pv"])
                        else :
                            joueur.setPv(0)
                            interface.affichageDialogues(["Tu n'as pas de cles, ni assez de pv", "Tu es donc condamne à devoir mourrir et arreter","la partie ici."])
                    selection_utilisateur = True
        
    def actionPageActionNoir(self):
        self.getGame().setJoueurActuel().setPv(0)
        pygame.time.delay(2500)
        self.getGame().joueurSuivant()
        self.getGame().setPageActuel(PageState.MOUVEMENT)

    def actionPageActionJaune(self):
        pygame.time.delay(2500)
        self.getGame().joueurSuivant()
        self.getGame().setPageActuel(PageState.MOUVEMENT)

    def actionPageActionBlanc(self):
        pygame.time.delay(2500)
        self.getGame().joueurSuivant()
        self.getGame().setPageActuel(PageState.MOUVEMENT)
        
    def actionPageActionOrange(self):
        selection_malus = False
        while selection_malus != True:
            mouse_x, mouse_y = pygame.mouse.get_pos() 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    pygame.quit()
                    exit() 
                
                
                if event.type == pygame.MOUSEBUTTONDOWN:  
                    if 360 < mouse_x < 424 and 475 < mouse_y < 539:
                        liste_malus = ["perdre 20 pv","perdre 50 pv","perdre 80 pv","perdre 120 pv"]
                        malus = random.choice(liste_malus)
                        if malus == "perdre 20 pv":
                            if joueur.getPv() > 20:
                                joueur.setPv(joueur.getPv() - 20)
                            else:
                                interface.affichageDialogues(["Tu n'as plus assez de vie."])
                                self.ActionCouleurNoir()
                                
                        elif malus == "perdre 50 pv":
                            if joueur.getPv() > 50:
                                joueur.setPv(joueur.getPv() - 50)
                            else:
                                interface.affichageDialogues(["Tu n'as plus assez de vie."])
                                self.ActionCouleurNoir()
                                
                        elif malus == "perdre 80 pv":
                            if joueur.getPv() > 80:
                                joueur.setPv(joueur.getPv() - 80)                                
                            else:                                
                                interface.affichageDialogues(["Tu n'as plus assez de vie."])
                                self.ActionCouleurNoir()
                                
                        elif malus == "perdre 100 pv":
                            if joueur.getPv() > 100:
                                joueur.setPv(joueur.getPv() - 100)
                            else:
                                interface.affichageDialogues(["Tu n'as plus assez de vie."])
                                self.ActionCouleurNoir()
                        
                        selection_malus = True
                        interface.affichageDialogues(["Tu vas {}".format(malus)])
                        
    def actionPageActionRouge(self):
        if joueur.aCles() != True:
            un_ennemis = ennemis.Choix_ennemis(joueur)

            interface.affichageFondEcran(image.Page.ARENE.value)
            interface.affichageMenu(joueur)
            interface.affichageDialogues(["Tu as décidé de combattre un joueur. Le celebre ","{}. Prepare toi à le combattre afin de prendre".format(un_ennemis.get_prenom()), "l'avantage sur lui !"])
            interface.affichage_image(100,400,joueur)
            interface.affichage_image_adv(620,400,un_ennemis)            
            pygame.time.delay(2500)
            
            interface.affichageMenu(joueur)
            interface.affichage_image(100, 400, joueur)
            interface.affichage_image_adv(620, 400, un_ennemis)
            interface.affichageDialogues(["Que veux-tu faire ? Une attaque basique, une ","attaque speciale, te defendre ou prendre", "la fuite ?"])
            
            interface.affichageAction([image.BtnAttaque.BASIQUE.value, image.BtnAttaque.SPECIALE.value, image.BtnAttaque.DEFENSE.value, image.BtnAttaque.FUITE.value], ["Attaque", "Coup Spéciale", "Defense", "Fuite"])
            combat_en_cours = True
        else:
            interface.affichageFondEcran(image.Page.ARENE.value)
            interface.affichageMenu(joueur)
            interface.affichage_image(100,400,joueur)
            interface.affichageDialogues(["Tu as deja combatu tous les boss, deplace-toi ","jusqu'à la hutte de la sorciere pour la tuer", "et recuperer ta taille."])
            
            combat_en_cours = False
        while combat_en_cours:
            if joueur.getPv() <= 0:
                joueur.setPv(0)
                interface.affichage_image_adv(620, 400, un_ennemis)
                interface.affichageDialogues(["Fin du combat... Tu n'as pas survecu","à l'attaque du boss...", "Retour au plateau !"])
                
                combat_en_cours = False
            elif un_ennemis.getPv() <= 0:
                if joueur.avoir_tt_cles() != True:
                    joueur.set_inventaire(joueur.get_inventaire() + ["cle " + un_ennemis.get_element()])
                    interface.affichage_image(100, 400, joueur)
                    interface.affichageDialogues(["Fin du combat... Tu n'as pas survecu","{}, recupere les autres cles en tuant les","autres boss et detruit cette sorciere !!!"])
                    
                else:
                    joueur.set_inventaire(joueur.get_inventaire() + ["cle " + un_ennemis.get_element()])
                    interface.affichage_image(100, 400, joueur)
                    interface.affichageDialogues(["Fin du combat... Tu n'as pas survecu","{}, en plus de ça tu as toutes les cles, depeche ","toi pour etre le premier à tuer la sorciere !!!"])
                    
                    combat_en_cours = False
            elif joueur.getPv() > 0 and un_ennemis.getPv() > 0:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        if 100 < mouse_x < 164 and 508 < mouse_y < 572:
                            #action_joueur = "attaque basique"
                            toucher = random.choice([True,False,True])
                            if toucher == True:
                                if joueur.get_element() == un_ennemis.get_element():
                                    pv = random.randint(joueur.get_attaque(),joueur.get_attaque()+20)
                                    un_ennemis.setPv(un_ennemis.getPv()-pv)
                                else:
                                    pv = random.randint(joueur.get_attaque()-20,joueur.get_attaque())
                                    un_ennemis.setPv(un_ennemis.getPv()-pv)
                                
                                interface.affichage_image(100,400,joueur)
                                interface.affichage_image_adv(620,400,un_ennemis)
                                interface.affichageDialogues(["Tu as choisi de faire une attaque basique,","bravo, l'adversaire a perdu {} pvs".format(pv)])
                                
                            else:
                                
                                interface.affichage_image(100,400,joueur)
                                interface.affichage_image_adv(620,400,un_ennemis)
                                interface.affichageDialogues(["L'adversaire a esquive le coup, dommage","L'adversaire n'a pas perdu de pv"])
                                
                        elif 250 < mouse_x < 314 and 508 < mouse_y < 572:
                            #action_joueur = "attaque speciale"
                            toucher = random.choice([True,False,False])
                            if toucher == True:
                                pv = joueur.get_attaque()+50
                                un_ennemis.setPv(un_ennemis.getPv()-pv)
                                
                                interface.affichage_image(100,400,joueur)
                                interface.affichage_image_adv(620,400,un_ennemis)
                                interface.affichageDialogues(["Tu as choisi de faire une attaque speciale,","bravo, l'adversaire a perdu {} pvs".format(pv)])
                                
                            else:
                                
                                interface.affichage_image(100,400,joueur)
                                interface.affichage_image_adv(620,400,un_ennemis)
                                interface.affichageDialogues(["L'adversaire a esquive le coup, dommage","L'adversaire n'a pas perdu de pv"])
                                
                        elif 400 < mouse_x < 464 and 508 < mouse_y < 572:
                            #action_joueur = "se defendre"
                            toucher = random.choice([True,False])
                            if toucher == True:
                                un_ennemis.set_attaque(un_ennemis.get_attaque()-20)
                                
                                interface.affichage_image(100,400,joueur)
                                interface.affichage_image_adv(620,400,un_ennemis)
                                interface.affichageDialogues(["Tu as choisi de te defendre, tu fais une","grimace au boss et cela reduit les degâts","qu'il peut t'infliger." ])
                                
                            else:
                                
                                interface.affichage_image(100,400,joueur)
                                interface.affichage_image_adv(620,400,un_ennemis)
                                interface.affichageDialogues(["L'ennemis n'a pas pris peur, les","degâts qu'il t'inflige ne sont pas","reduits."])
                                
                        elif 550 < mouse_x < 614 and 508 < mouse_y < 572:
                            
                            interface.affichage_image(100, 400, joueur)
                            interface.affichage_image_adv(620, 400, un_ennemis)
                            interface.affichageDialogues(["Tu as choisi de prendre la fuite,","retente ta chance une prochaine fois."])
                            
                            combat_en_cours = False
                        pygame.time.delay(1500)
                        if joueur.getPv() >0 and un_ennemis.getPv()>0 and combat_en_cours == True:
                            image_Arene = image.Page.ARENE.value
                            image_redimensionnee = pygame.transform.scale(image_Arene, (800, 500))
                            interface.affichageCombat(image_redimensionnee, (0, 0))
                            
                            interface.affichage_image(100, 400, un_ennemis)
                            interface.affichage_image_adv(620, 400, joueur)
                            toucher = random.choice([False,True])
                            if toucher == True:
                                pv = un_ennemis.get_attaque()+random.randint(0,50)
                                joueur.setPv(joueur.getPv()-pv)
                                interface.affichageDialogues(["C'est au tour du boss d'attaquer","Le boss reflechit...","Il te fait perdre {} pvs".format(pv)])
                                
                            elif toucher == False:
                                interface.affichageDialogues(["C'est au tour du boss d'attaquer","Le boss reflechit...","L'adversaire a raté son coup"])
                                pygame.time.delay(1500)
                            # Actualisation de l'interface
                            image_Arene = image.Page.ARENE.value
                            image_redimensionnee = pygame.transform.scale(image_Arene, (800, 500))
                            interface.affichageCombat(image_redimensionnee, (0, 0))
                            
                            interface.affichage_image(100, 400, joueur)
                            interface.affichage_image_adv(620, 400, un_ennemis)
                            interface.affichageDialogues(["Que veux-tu faire ? Une attaque basique, une ","attaque speciale, te defendre ou prendre","la fuite ?"])
                            
                            image.Image(100, 508, image.BtnAttaque.BASIQUE.value).affiche(interface.getFenetre())
                            image.Image(250, 508, image.BtnAttaque.SPECIALE.value).affiche(interface.getFenetre())
                            image.Image(400, 508, image.BtnAttaque.DEFENSE.value).affiche(interface.getFenetre())
                            image.Image(550, 508, image.BtnAttaque.FUITE.value).affiche(interface.getFenetre())
            
    def actionPageActionRose(self):
        selection_bonus = False
        while selection_bonus != True:
            mouse_x, mouse_y = pygame.mouse.get_pos() 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    pygame.quit()
                    exit() 
                
                if event.type == pygame.MOUSEBUTTONDOWN:  
                    if 360 < mouse_x < 424 and 475 < mouse_y < 539:
                        liste_chance = ["gagner 100 pv","gagner 200 pv","gagner 500 pv", "gagner 150 pv","gagner 400 pv","gagner 1050 pv"]
                        chance = random.choice(liste_chance)                        
                        interface.affichageDialogues(["Tou-dou-dou-doum","Tu vas {}".format(chance)])
                        
                        if chance == "gagner 100 pv":
                            joueur.setPv(joueur.getPv() + 100)
                            selection_bonus = True
                            
                        elif chance == "gagner 200 pv":
                            joueur.setPv(joueur.getPv() + 200)
                            selection_bonus = True
                            
                        elif chance == "gagner 500 pv":
                            joueur.setPv(joueur.getPv() + 500)
                            selection_bonus = True
                            
                        elif chance == "gagner 150 pv":
                            joueur.setPv(joueur.getPv() + 150)
                            selection_bonus = True
                            
                        elif chance == "gagner 300 pv":
                            joueur.setPv(joueur.getPv() + 300)
                            selection_bonus = True
                            
                        elif chance == "gagner 1050 pv":
                            joueur.setPv(joueur.getPv() + 1050)
                            selection_bonus = True
                                                                                   
    def actionPageActionGris(self):
        selection_speciale = False
        while selection_speciale != True:
            mouse_x, mouse_y = pygame.mouse.get_pos() 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    pygame.quit()
                    exit() 
                
                
                if event.type == pygame.MOUSEBUTTONDOWN:  
                    if 220 < mouse_x < 284 and 480 < mouse_y < 544:
                    
                        # Si le joueur veut gagner la recompence
                        if joueur.get_inventaire() != []:    
                            choix_tirage = ["bravo", "oh non dommage"] 
                            tirage = random.choice(choix_tirage)   
                            if tirage == "bravo":
                                interface.affichageDialogues(["Bravo tu as gagner !!!","Voilà deux cles supplementaires que tu peux", "voir apparaître dans ton inventaire."])
                                selection_speciale = True
                            else:
                                interface.affichageDialogues(["Oh non dommage...", "Tu pourras retenter ta chance si tu as", "d'autres cles :)"])       
                                selection_speciale = True
                        else:
                            interface.affichageDialogues(["Tu ne possede pas de cles.", "Obtient-en une en tuant un boss sur les", "cases rouges."])
                            selection_speciale = True    
                            
                    elif 510 < mouse_x < 574 and 480 < mouse_y < 544:
                        interface.affichageDialogues(["Pas de soucis, retente ta chance une autre fois"])
                        selection_speciale = True
                        
    def actionPageActionViolet(self):
        self.getGame().setPageActuel(PageState.REJOUER)

    def actionPageActionBeige(self):
        selection_sorciere = False
        while selection_sorciere != True:
            mouse_x, mouse_y = pygame.mouse.get_pos() 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    pygame.quit()
                    exit() 
                
                if event.type == pygame.MOUSEBUTTONDOWN:  
                    if 220 < mouse_x < 284 and 480 < mouse_y < 544:
                        if joueur.aCles() == True:
                            interface.affichageDialogues(["Bravo tu as trouve toutes les cles", "Ouvre la porte et apprete toi à","affronter la sorciere."])
                            selection_sorciere = True
                        else:
                            interface.affichageDialogues(["Tu n'as pas encore recuperer toutes","les cles afin d'ouvrir la porte de", "la sorciere. Depeche-toi !"])
                            selection_sorciere = True
                        
                    elif 510 < mouse_x < 574 and 480 < mouse_y < 544:
                        interface.affichageDialogues(["Pas de soucis, recupere les cles afin", "d'ouvrir la porte en premier !"])
                        selection_sorciere = True

    def actionPageActionIndigo(self):
        selection_teleporte = False
        while selection_teleporte != True:
            mouse_x, mouse_y = pygame.mouse.get_pos() 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    pygame.quit()
                    exit() 
                
                
                if event.type == pygame.MOUSEBUTTONDOWN:  
                    if 220 < mouse_x < 284 and 480 < mouse_y < 544:
                        interface.affichageDialogues(["Tou-dou-dou-doum", "Teleportation sur la deuxieme case", "de teleportation"])

                        coord_case_indigo = interface.getPlateau().getCaseIndigo(joueur)
                        joueur.setPlateauX(coord_case_indigo[0])
                        joueur.setPlateauY(coord_case_indigo[1])
                        interface.getPlateau().setCasesDecouvertes(interface.getPlateau().getCasesDecouvertes() + [[coord_case_indigo[0],coord_case_indigo[1]]])
                        selection_teleporte = True
                        
                        
                    elif 510 < mouse_x < 574 and 480 < mouse_y < 544:
                        interface.affichageDialogues(["Pas de soucis, essaye une prochaine fois si tu en as l'envie.", "Bonne chance à toi jeune aventurier"])
                        selection_teleporte = True
        
    def actionPageActionVert(self):
        for joueur in self.getGame().getListeJoueurs():
            joueur.setPlateauX(random.randint(0,9))
            joueur.setPlateauY(random.randint(0,16))
            joueur.setX(joueur.getPlateauY() * 47)
            joueur.setY(joueur.getPlateauX() * 47)
            self.getGame().getPlateau().setCasesDecouvertes(self.getGame().getPlateau().getCasesDecouvertes() + [[joueur.getPlateauX(), joueur.getPlateauY()]])
        pygame.time.delay(2500)
        self.getGame().joueurSuivant()
        self.getGame().setPageActuel(PageState.MOUVEMENT)