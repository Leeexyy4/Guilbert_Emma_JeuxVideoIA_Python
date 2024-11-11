#  ----------------------- Jeu de plateau - Interface ------------------------ #

# Bibliothèques utilisées pour le code
import pygame
from classe.personnage import joueur, intelA
from main import PageState

# ----------------------- Jeu de plateau - Logique ------------------------ #
class Logique:
    def __init__(self) -> None:
        """Initialisation de l'interface."""
        self.__mouse = pygame.mouse
        self.__etatJeu = "demarrage_jeu"
        self.__horsLigneOuLigne = "HL"
        self.__listeJoueurs = []
        self.__nbJoueur = -1
        self.__nbIntelligenceA = -1

    def getMouse(self):
        """Getter de la fenetre."""
        return self.__mouse
    
    def getInterface(self):
        """Getter de la fenetre."""
        return self.__interface
    
    def getEtatJeu(self):
        """Getter de l'etat de jeu."""
        return self.__etatJeu

    def setEtatJeu(self, etat_jeu):
        """Setter de l'etat de jeu."""
        self.__etatJeu = etat_jeu
        
    def getListeJoueur(self):
        """Getter de la liste de joueur."""
        return self.__listeJoueurs

    def setListeJoueur(self, listeJoueur):
        """Setter de la liste de joueur."""
        self.__listeJoueurs = listeJoueur

    def getNbJoueur(self):
        """Getter du nb de joueur."""
        return self.__nbJoueur

    def setNbJoueur(self, nbJoueur):
        """Setter du nb de joueur."""
        self.__nbJoueur = nbJoueur

    def getHorsLigneOuLigne(self):
        """Getter du mode de jeu."""
        return self.__horsLigneOuLigne

    def setHorsLigneOuLigne(self, horsLigneOuLigne):
        """Setter du mode de jeu."""
        self.__horsLigneOuLigne = horsLigneOuLigne

    def getNbIntelligenceA(self):
        """Getter du nb d'IA."""
        return self.__nbIntelligenceA

    def setNbIntelligenceA(self, nbIntelligenceA):
        """Setter du nb d'IA."""
        self.__nbIntelligenceA = nbIntelligenceA

# ----------------------------------- Affichage des élements ----------------------------------- #
        
    def actionPageDemarrage(self): 
        demarrage = True
        while (demarrage):
            mouse_x, mouse_y = self.getMouse().get_pos()
            for event in pygame.event.get():
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    if (320 <= mouse_x <= 470 and 500 <= mouse_y <= 550) : # Stats
                        demarrage = False
                        return PageState.STATISTIQUE
                    if (170 <= mouse_x <= 350 and 550 <= mouse_y <= 600) : # En local
                        self.setHorsLigneOuLigne("HL")
                        self.actionPageNbJoueur()
                    if (450 <= mouse_x <= 630 and 550 <= mouse_y <= 600) : # En ligne
                        self.setHorsLigneOuLigne("EL")
                        self.actionPageNbJoueur()
                    if (700 <= mouse_x <= 764 and 25 <= mouse_y <= 89) : # Info
                        self.actionPageCommande()
                    if (10 <= mouse_x <= 70 and 630 <= mouse_y <= 690): # Retour
                        self.actionPageDemarrage()
                if (event.type == pygame.QUIT): # Quitter
                    pygame.quit()
                    exit()

    def actionPageStatistiques(self):
        stats = False
        while (stats != True):
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    if (40 <= mouse_x <= 100 and 40 <= mouse_y <= 100): # Retour
                        self.PageDemarrage()
                        stats = True
                if (event.type == pygame.QUIT): # Quitter
                    pygame.quit()
                    exit()

    def actionPageCommande(self):
        stats = False
        while (stats != True):
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    if (40 <= mouse_x <= 100 and 40 <= mouse_y <= 100): # Retour
                        self.PageDemarrage()
                        stats = True
                if (event.type == pygame.QUIT): # Quitter
                    pygame.quit()
                    exit()

    def actionPageNbJoueur(self):
        while (self.getNbJoueur() == -1):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN :
                    mouse_x, mouse_y = pygame.mouse.get_pos() 
                    if (40 <= mouse_x <= 100 and 40 <= mouse_y <= 100) : # Retour
                        self.setNbJoueur(-1)
                        self.PageDemarrage()
                    if (200 <= mouse_x <= 260 and 470 <= mouse_y <= 540) : # 1 joueur
                        self.setNbJoueur(1)
                        if self.getHorsLigneOuLigne() == "HL":
                            self.PageNbIntelligenceA()
                        else:
                            self.setEtatJeu("demarrage_jeu")
                    if (300 <= mouse_x <= 360 and 470 <= mouse_y <= 540) : # 2 joueurs
                        self.setNbJoueur(2)
                        if self.getHorsLigneOuLigne() == "HL":
                            self.PageNbIntelligenceA()
                        else:
                            self.setEtatJeu("demarrage_jeu")
                    if (400 <= mouse_x <= 460 and 470 <= mouse_y <= 540) : # 3 joueurs
                        self.setNbJoueur(3)
                        if self.getHorsLigneOuLigne() == "HL":
                            self.PageNbIntelligenceA()
                        else:
                            self.setEtatJeu("demarrage_jeu")
                    if (500 <= mouse_x <= 560 and 470 <= mouse_y <= 540) : # 4 joueurs
                        self.setNbJoueur(4)
                        if self.getHorsLigneOuLigne() == "HL":
                            self.PageNbIntelligenceA()
                        else:
                            self.setEtatJeu("demarrage_jeu")
                if event.type == pygame.QUIT: # Quitter
                    pygame.quit()
                    exit()

    def actionPageNbIntelligenceA(self):
        while (self.getNbIntelligenceA() == -1):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN :
                    mouse_x, mouse_y = pygame.mouse.get_pos() 
                    if (40 <= mouse_x <= 100 and 40 <= mouse_y <= 100) :
                        self.setNbIntelligenceA(-1)
                        self.setNbJoueur(-1)
                        self.PageNbJoueur()
                    if (200 <= mouse_x <= 260 and 470 <= mouse_y <= 540 and (self.getNbJoueur() == 1 or self.getNbJoueur() == 2 or self.getNbJoueur() == 3 or self.getNbJoueur() == 4)):   
                        self.setNbIntelligenceA(0)
                    if (300 <= mouse_x <= 340 and 470 <= mouse_y <= 540 and (self.getNbJoueur() == 1 or self.getNbJoueur() == 2 or self.getNbJoueur() == 3)):
                        self.setNbIntelligenceA(1)
                    if (400 <= mouse_x <= 440 and 470 <= mouse_y <= 540 and (self.getNbJoueur() == 1 or self.getNbJoueur() == 2)):   
                        self.setNbIntelligenceA(2)
                    if (500 <= mouse_x <= 540 and 470 <= mouse_y <= 540 and self.getNbJoueur() == 1):   
                        self.setNbIntelligenceA(3)
                if event.type == pygame.QUIT: # Quitter
                    pygame.quit()
                    exit()

    def actionPageChoixPersonnage(self, joueurActuelId): 
        tempNb = self.getListeJoueur().count
        while (tempNb == self.getListeJoueur().count) :
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN : 
                    mouse_x, mouse_y = pygame.mouse.get_pos() 
                    if (200 <= mouse_x <= 260 and 470 <= mouse_y <= 540): # Pierre
                        prenom = joueur.Nom.ROCK.value
                        element = joueur.Element.ROCK.value
                        self.setListeJoueur(self.getListeJoueur() + [joueur.Joueur(joueurActuelId, prenom, element, self)])
                    if (300 <= mouse_x <= 360 and 470 <= mouse_y <= 540): # Ondine
                        prenom = joueur.Nom.WATER.value
                        element = joueur.Element.WATER.value
                        self.setListeJoueur(self.getListeJoueur() + [joueur.Joueur(joueurActuelId, "Ondine","de la Rivière", self)])
                    if (400 <= mouse_x <= 460 and 470 <= mouse_y <= 540): # Kevin
                        prenom = joueur.Nom.TOWN.value
                        element = joueur.Element.ROCK.value
                        self.setListeJoueur(self.getListeJoueur() + [joueur.Joueur(joueurActuelId, prenom, element, self)])
                    if (500 <= mouse_x <= 560 and 470 <= mouse_y <= 540): # Flora
                        prenom = joueur.Nom.GRASS.value
                        element = joueur.Element.GRASS.value
                        self.setListeJoueur(self.getListeJoueur() + [joueur.Joueur(joueurActuelId, prenom, element, self)])
                if event.type == pygame.QUIT: # Quitter
                    pygame.quit()
                    exit()
        
    def actionPagePremierMouvement(self, joueurActuel):
        pass

    def actionPageMouvement(self, joueurActuel):
        if isinstance(joueurActuel, intelA.IntelA):
            joueurActuel.choix_mouvement_combat_IA(self)
        else:
            action_joueurActuel = ""
            while (action_joueurActuel == "") :
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN : # Si le joueurActuel clique sur le bouton, on passe à la prochaine page "introduction"
                        mouse_x, mouse_y = pygame.mouse.get_pos() 
                        # Si le personnage sur lequel on clique est Ondine   
                        if (220 <= mouse_x <= 284 and 480 <= mouse_y <= 544) :
                            self.PageAttaque(joueurActuel)
                            action_joueurActuel = "Attaquer"
                        elif (510 <= mouse_x <= 574 and 480 <= mouse_y <= 544):
                            self.PageRejouer(joueurActuel)
                            action_joueurActuel = "Lancer"
                    if event.type == pygame.QUIT: # si le joueurActuel quitte la fenetre # si le joueurActuel quitte la fenetre
                        pygame.quit()
                        exit()

    def actionPageDirection(self, joueurActuel):
        face_choisie = self.getDe().getFaceAleatoireDe(self,joueurActuel)
        if isinstance(joueurActuel, intelA.IntelA):
            joueurActuel.choix_case_IA(self)
        else:
            # Tant que : Le joueurActuel n'a pas choisi de direction (haut, bas, gauche, droite)
            while self.getDe().getFaceDe() != 0 :
                # Pour tout : Les evenements de pygame
                for event in pygame.event.get():
                    
                    # Si le joueurActuel quitte la fenetre
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                        
                    elif event.type == pygame.KEYDOWN:
                        touche_fleche = event.key

                        if touche_fleche == pygame.K_UP:
                            # La touche fleche vers le haut a ete enfoncee
                            avancer = joueurActuel.haut(47)
                            self.getPlateauJeu().setCasesDecouvertes(self.getPlateauJeu().getCasesDecouvertes() + [[joueurActuel.getPlateauX(),joueurActuel.getPlateauY()]])
                            self.affichagePlateau()
                            if avancer == True :
                                self.getDe().setFaceDeDesincremente(1)
                            else:
                                self.PageHorsPlateau(joueurActuel, face_choisie)
                        
                        elif touche_fleche == pygame.K_DOWN:
                            # La touche fleche vers le bas a ete enfoncee
                            avancer = joueurActuel.bas(47)
                            self.getPlateauJeu().setCasesDecouvertes(self.getPlateauJeu().getCasesDecouvertes() + [[joueurActuel.getPlateauX(),joueurActuel.getPlateauY()]])
                            self.affichagePlateau()
                            
                            if avancer == True :
                                self.getDe().setFaceDeDesincremente(1)
                            else:
                                self.PageHorsPlateau(joueurActuel, face_choisie)
                        
                        elif touche_fleche == pygame.K_RIGHT:
                            # La touche fleche vers la droite a ete enfoncee
                            avancer = joueurActuel.droite(47) 
                            self.getPlateauJeu().setCasesDecouvertes(self.getPlateauJeu().getCasesDecouvertes() + [[joueurActuel.getPlateauX(),joueurActuel.getPlateauY()]])
                            self.affichagePlateau()
                            
                            if avancer == True :
                                self.getDe().setFaceDeDesincremente(1)
                            else:
                                self.PageHorsPlateau(joueurActuel, face_choisie)

                        elif touche_fleche == pygame.K_LEFT:
                            # La touche fleche vers la gauche a ete enfoncee
                            avancer = joueurActuel.gauche(47) 
                            self.getPlateauJeu().setCasesDecouvertes(self.getPlateauJeu().getCasesDecouvertes() + [[joueurActuel.getPlateauX(),joueurActuel.getPlateauY()]])  
                            self.affichagePlateau()
                            
                            if avancer == True :
                                self.getDe().setFaceDeDesincremente(1)
                            else:
                                self.PageHorsPlateau(joueurActuel, face_choisie)
                            
    def actionPageHorsPlateau(self, joueurActuel, face_choisie):
        pass

    def actionPageRejouer(self, joueurActuel): 
        self.PageDirection(joueurActuel)
        self.PageActionCases(joueurActuel)   

    def actionPageAttaque(self, joueurActuel): 
        if joueurActuel.advDisponible(self.getListeJoueur()) != True:
            self.PageRejouer(joueurActuel)

    def actionPageActionCases(self, joueurActuel):
        couleur_case = self.getPlateauJeu().getCases(joueurActuel.getPlateauX(), joueurActuel.getPlateauY())
        
        if joueurActuel.getPv() != 0:
            if couleur_case == self.getCouleur().getBeige():
                self.getPlateauJeu().ActionCouleurBeige(self, joueurActuel)
                
            elif couleur_case == self.getCouleur().getBlanc():
                self.affichageMenu(joueurActuel)
                self.affichageDialogues(["Tu es dans une case Vide.", "Il ne t'arrivera rien tu peux etre rassure."])
                
            elif couleur_case == self.getCouleur().getBleu():
                self.getPlateauJeu().ActionCouleurBleu(self, joueurActuel)
                        
            elif couleur_case == self.getCouleur().getGris():
                self.getPlateauJeu().ActionCouleurGris(self, joueurActuel)
                
            elif couleur_case == self.getCouleur().getIndigo():
                self.getPlateauJeu().ActionCouleurIndigo(self, joueurActuel)
                
            elif couleur_case == self.getCouleur().getJaune():
                self.affichageMenu(joueurActuel)
                self.affichageDialogues(["Tu es la case de Depart.","Depeche toi de recuperer les cles","avant les autres joueurs."])
                
            elif couleur_case == self.getCouleur().getNoir():
                self.getPlateauJeu().ActionCouleurNoir(self, joueurActuel)     
                
            elif couleur_case == self.getCouleur().getOrange():
                self.getPlateauJeu().ActionCouleurOrange(self, joueurActuel)

            elif couleur_case == self.getCouleur().getRose():
                self.getPlateauJeu().ActionCouleurRose(self, joueurActuel)
                
            elif couleur_case == self.getCouleur().getRouge():
                self.getPlateauJeu().ActionCouleurRouge(self, joueurActuel)
                
            elif couleur_case == self.getCouleur().getVert():
                self.getPlateauJeu().ActionCouleurVert(self,joueurActuel)
                
            elif couleur_case == self.getCouleur().getViolet():
                self.getPlateauJeu().ActionCouleurViolet(self, joueurActuel)

            if (joueurActuel.getPv() <= 0):
                self.setListeJoueur(self.getListeJoueur().remove(joueurActuel))
            pygame.time.delay(1000)

    def actionPageSorciere(self, joueurActuel):
        selection_potion = False
        while selection_potion != True:
            mouse_x, mouse_y = pygame.mouse.get_pos() 
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # si le joueurActuel quitte la self.getFenetre() # si le joueurActuel quitte la self.getFenetre()
                    pygame.quit()
                    exit() 
                
                
                if event.type == pygame.MOUSEBUTTONDOWN:  
                    if 500 < mouse_x < 725 and 150 < mouse_y < 450:
                        image.Image(0,0,image.Sorciere.MAISON_SYMBOLE.value).affichage_image_redimensionnee(800, 700,self.getFenetre())
                        self.affichageMenu(joueurActuel)
                        self.affichageDialogues(["C'est un symbole astral, si c'est chez la","sorciere, il vaut mieux ne pas y toucher"])
                        
                        pygame.time.delay(2500)
                        image.Image(0,0,image.Sorciere.MAISON.value).affichage_image_redimensionnee(800, 700,self.getFenetre())
                        self.affichageMenu(joueurActuel)
                        self.affichageDialogues(["Tu es chez la sorciere, mais on dirait","qu'elle est sortie de sa taniere...","profite-en pour fouiller dans ses affaires :)"])
                        
                    elif 90 < mouse_x < 190 and 180 < mouse_y < 350:
                        image.Image(0,0,image.Sorciere.MAISON_DRAGON.value).affichage_image_redimensionnee(800, 700,self.getFenetre())
                        self.affichageMenu(joueurActuel)
                        self.affichageDialogues(["Un dragon de pierre... ce n'est pas très","rassurant, trouvons vite un remède et sortons","d'ici très vite"])
                        
                        pygame.time.delay(2500)
                        image.Image(0,0,image.Sorciere.MAISON.value).affichage_image_redimensionnee(800, 700,self.getFenetre())
                        self.affichageMenu(joueurActuel)
                        self.affichageDialogues(["Tu es chez la sorciere, mais on dirait","qu'elle est sortie de sa taniere...","profite-en pour fouiller dans ses affaires :)"])
                        
                    elif 330 < mouse_x < 430 and 480 < mouse_y < 580:
                        image.Image(0,0,image.Sorciere.MAISON.value).affichage_image_redimensionnee(800, 700,self.getFenetre())
                        self.affichageMenu(joueurActuel)
                        self.affichageDialogues(["Tu as trouvé une potion... Potion inverstium","Tu décides de la boire afin d'inverser le","sortilège"])
                        
                        joueurActuel.set_inventaire(["Potion inverstium"])
                        self.affichage_potion()
                        pygame.time.delay(2500)
                        image.Image(0,0,image.Page.FIN_JEU).affichage_image_redimensionnee(800, 700,self.getFenetre())
                        self.affichageMenu(joueurActuel)
                        self.affichageDialogues(["Tu as terminé le jeu bravo à toi jeune aventurier","Tu es le premier a t'être libéré du sort !!"])
                        
                        pygame.time.delay(2500)
    
    def actionPageFin(self):
        self.affichageFondEcran(image.Page.FIN_JEU.value)
        self.affichageMenu()
        self.affichageDialogues(["Aucun des joueurs n'a réussi à finir le jeu","Retentez votre chance une prochaine fois","pour profiter de cette aventure :)"])

        selection_fin = False
        while selection_fin != True:
            mouse_x, mouse_y = pygame.mouse.get_pos() 
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # si le joueurActuel quitte la self.getFenetre() # si le joueurActuel quitte la self.getFenetre()
                    pygame.quit()
                    exit() 
                
                
                if event.type == pygame.MOUSEBUTTONDOWN:  
                    if 0 < mouse_x < 800 and 0 < mouse_y < 700:
                        self.PageStatistiques()

    def actionCouleurBleu(self, joueur):
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
        
    def actionCouleurNoir(self, interface, joueur):
        interface.affichageFondEcran(image.Page.FIN_JEU.value)
        interface.affichagePlateau()   
        interface.affichageMenu(joueur)
        interface.affichageDialogues(["Tu n'as pas de chance...", "Tu es tombe sur la case de Mort...", "La partie est finie pour toi."])
        joueur.setPv(0)
        
    def actionCouleurOrange(self, interface, joueur):
        interface.affichageFondEcran(image.Page.JEU.value)
        interface.affichagePlateau()   
        interface.affichageMenu(joueur)
        interface.affichageAction([image.Interaction.MALUS.value], ["Malus"])
        interface.affichageDialogues(["Tu es sur une case Malus.", "Clique pour savoir quel sort", "le jeu te reserve."])
            
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
                        
    def actionCouleurRouge(self, interface, joueur):
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
            
    def actionCouleurRose(self, interface, joueur):
        interface.affichageFondEcran(image.Page.JEU.value)
        interface.affichagePlateau()   
        interface.affichageMenu(joueur)
        interface.affichageAction([image.Interaction.CHANCE.value], ["Bonus"])
        interface.affichageDialogues(["Tu es sur une case Chance","Clique pour decouvrir le pouvoir","que le jeu va te donner."])
        
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
                                                                                   
    def actionCouleurGris(self, interface, joueur):
        interface.affichageFondEcran(image.Page.CHOIX_DOUBLE.value)
        interface.affichagePlateau()   
        interface.affichageMenu(joueur)
        interface.affichageAction([image.Interaction.CLES.value, image.Interaction.RETOUR.value], ["1 clee", "Froussard !"])
        interface.affichageDialogues(["Tu es sur une case Speciale ! Si tu tente ta chance", "tu as une chance sur deux gagner deux cles", "que tu n'as pas ou de tout perdre."])
        
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
                        
    def actionCouleurViolet(self, interface, joueur):
        interface.affichageFondEcran(image.Page.JEU.value)
        interface.affichagePlateau()   
        interface.affichageMenu(joueur)
        interface.affichageDialogues(["Tu es sur une case Rejoue !","Relance le de pour avoir un", "deuxieme lance"])
        interface.affichageAction([image.De.FACE1.value])
        interface.PageDirection(interface.getListeJoueur()[joueur.getId()])
        interface.PageActionCases(interface.getListeJoueur()[joueur.getId()])

    def actionCouleurBeige(self, interface, joueur):
        interface.affichageFondEcran(image.Page.CHOIX_DOUBLE.value)
        interface.affichagePlateau()   
        interface.affichageMenu(joueur)
        interface.affichageDialogues(["Tu es devant la Hutte de la sorciere.","Veux-tu essayer de l'ouvrir à l'aide", "des cles des quatre boss ?"])
        interface.affichageAction([image.Interaction.CLES.value, image.Interaction.RETOUR.value], ["Entrer dans l'entre", "Plus tard"])
        
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
                            interface.setEtatJeu("fin_du_jeu")
                            selection_sorciere = True
                        else:
                            interface.affichageDialogues(["Tu n'as pas encore recuperer toutes","les cles afin d'ouvrir la porte de", "la sorciere. Depeche-toi !"])
                            selection_sorciere = True
                        
                    elif 510 < mouse_x < 574 and 480 < mouse_y < 544:
                        interface.affichageDialogues(["Pas de soucis, recupere les cles afin", "d'ouvrir la porte en premier !"])
                        selection_sorciere = True

    def actionCouleurIndigo(self, interface, joueur):
        interface.affichageFondEcran(image.Page.CHOIX_DOUBLE.value)
        interface.affichagePlateau()   
        interface.affichageMenu(joueur)
        interface.affichageDialogues(["Tu es sur une case de Teleportation. Veux-tu etre teleporter","en passant par le passage secret ?"])
        interface.affichageAction([image.Interaction.TP.value, image.Interaction.RETOUR.value], ["Avec plaisir", "Non merci"])
        
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

                        coord_case_indigo = interface.getPlateauJeu().getCaseIndigo(joueur)
                        joueur.setPlateauX(coord_case_indigo[0])
                        joueur.setPlateauY(coord_case_indigo[1])
                        interface.getPlateauJeu().setCasesDecouvertes(interface.getPlateauJeu().getCasesDecouvertes() + [[coord_case_indigo[0],coord_case_indigo[1]]])
                        selection_teleporte = True
                        
                        
                    elif 510 < mouse_x < 574 and 480 < mouse_y < 544:
                        interface.affichageDialogues(["Pas de soucis, essaye une prochaine fois si tu en as l'envie.", "Bonne chance à toi jeune aventurier"])
                        selection_teleporte = True
        
    def actionCouleurVert(self, interface, joueur):
        interface.affichageFondEcran(image.Page.JEU.value)
        interface.affichagePlateau()   
        interface.affichageMenu(joueur)
        interface.affichageDialogues(["Tu es sur une case Grrr", "Un tremblement de terre surgit de nul part", "et teleporte tous les joueurs !!!"])        
        for joueur in interface.getListeJoueur():
            joueur.setPlateauX(random.randint(0,9))
            joueur.setPlateauY(random.randint(0,16))
            joueur.setX(joueur.getPlateauY() * 47)
            joueur.setY(joueur.getPlateauX() * 47)
            interface.getPlateauJeu().setCasesDecouvertes(interface.getPlateauJeu().getCasesDecouvertes() + [[joueur.getPlateauX(), joueur.getPlateauY()]])