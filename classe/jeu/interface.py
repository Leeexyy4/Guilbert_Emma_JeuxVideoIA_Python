# ----------------------- Jeu de plateau - Interface ------------------------ #

# Bibliothèques utilisées pour le code
import pygame, random
from classe.visuel import image, couleur, rectangle, texte
from classe.jeu.game import PageState

class Interface:
    def __init__(self, game) -> None:
        """Initialisation de l'interface."""
        self.__tailleCase = 800 // 17
        self.__police = pygame.font.Font('./assets/font/times-new-roman.ttf', 16)
        self.__couleur = couleur.Couleur()
        self.__game = game

        self.__fenetre = pygame.display.set_mode((800, 700))
        pygame.display.set_caption("Plateau de jeu")
        pygame.mixer_music.load("./assets/music/Musique_jeu.mp3")
        pygame.mixer_music.play(-1,0.0,8)

# ----------------------------------- Getter des élements ----------------------------------- #

    def getFenetre(self):
        """Getter de la fenetre."""
        return self.__fenetre

    def getPolice(self):
        """Getter de la police."""
        return self.__police
    
    def getCouleur(self):
        """Getter de la couleur."""
        return self.__couleur

    def getTailleCase(self):
        """Getter  de la taille de la case"""
        return self.__tailleCase
    
    def getGame(self):
        """Getter de la liste de joueur."""
        return self.__game

# ----------------------------------- Affichage des élements ----------------------------------- #
    
    def affichageFondEcran(self, imageFond):
        """
            La fonction affichageFondEcran permet d'afficher l'illustration de fond du jeu
        """
        self.getFenetre().fill((0, 0, 0))
        image.Image(0,0,imageFond).affichageImageRedimensionnee(800, 700,self.getFenetre())
        pygame.display.update()

    def affichagePlateau(self):
        """
            La fonction affichagePlateau permet d'afficher les cases découvertes du plateau et les personnages à leur position sur le plateau
        """
        for ligne in range(10):
            for colonne in range(17):
                x = colonne * self.getTailleCase()  # Coordonnée X du coin supérieur gauche du rectangle
                y = ligne * self.getTailleCase()  # Coordonnée Y du coin supérieur gauche du rectangle          
                rectangle = pygame.Rect(x, y, self.getTailleCase(), self.getTailleCase())  # Créer un rectangle
                pygame.draw.rect(self.getFenetre(), self.getCouleur().getNoir(), rectangle)  # Dessiner le rectangle avec la couleur
        """Met à jour le plateau en affichant les cases découvertes."""
        for i in self.getGame().getPlateau().getCasesDecouvertes():
            x = i[1] * self.getTailleCase()  # Coordonnée X du coin supérieur gauche du rectangle
            y = i[0] * self.getTailleCase()  # Coordonnée Y du coin supérieur gauche du rectangle          
            # Obtenir la couleur ou l'image de la case
            self.getFenetre().blit(self.getGame().getPlateau().getNom(i[0],i[1]), (x,y))
        """Affiche tous les joueurs sur le plateau."""
        for joueur in self.getGame().getListeJoueurs():
            image = pygame.transform.scale(pygame.image.load(joueur.getLien()), (47, 47))
            self.getFenetre().blit(image, (joueur.getX(), joueur.getY()))
        pygame.display.update()

    def affichageMenu(self, joueurActuel=None):
        """
            La fonction affichageMenu permet d'afficher le menu du jeu
        """
        # Dessiner la partie basse
        pygame.draw.rect(self.getFenetre(),self.getCouleur().getGris(),(10,580,780,102))
        
        # Dessiner la place pour montrer les cles
        rectangle.Rectangle(650,585,130,90,self.getCouleur().getRose()).affiche(self.getFenetre())
        
        # Dessiner le rectangle pour les pv du joueur
        rectangle.Rectangle(500,590,130,35,self.getCouleur().getVert()).affiche(self.getFenetre())
        
        # Dessiner les bords de la place pour les pv de l'adversaire
        rectangle.Rectangle(500,635,130,35,self.getCouleur().getRouge()).affiche(self.getFenetre())

        # Dessiner le rectangle pour les textes
        rectangle.Rectangle(100, 590, 390, 80, self.getCouleur().getBeige()).affiche(self.getFenetre())
        
        # Cadre pour mettre le personnage choisi
        rectangle.Rectangle(20,590,70,80,self.getCouleur().getRose()).affiche(self.getFenetre())
            
        if joueurActuel:
            # Affichage des clés
            for i in joueurActuel.getInventaire():
                if i == "clé de la Ville" :
                    image.Image(660,640,image.Cle.TOWN.value).affichageImageRedimensionnee(48,30,self.getFenetre())
                elif i == "clé de la Rivière" :
                    image.Image(660,595,image.Cle.WATER.value).affichageImageRedimensionnee(48,30,self.getFenetre())
                elif i == "clé de la Forêt" :
                    image.Image(725,595,image.Cle.GRASS.value).affichageImageRedimensionnee(48,30,self.getFenetre())
                elif i == "clé du Rocher" :
                    image.Image(725,640,image.Cle.ROCK.value).affichageImageRedimensionnee(48,30,self.getFenetre())
            pygame.draw.line(self.getFenetre(), self.getCouleur().getNoir(), (660, 632), (770, 632), 2)
            pygame.draw.line(self.getFenetre(), self.getCouleur().getNoir(), (715, 595), (715, 670), 2)
            
            # Affichage des potions
            if (joueurActuel.aGagner(self.getGame().getPlateau())):
                self.getFenetre().blit(image.Interaction.POTION.value, (668, 593))
                pygame.display.update()

            # Affichage du personnage
            self.getFenetre().blit(pygame.image.load(joueurActuel.getLien()), (24,598))
        pygame.display.update()
    
    def affichageDialogues(self, dialogues):
        """
            La fonction affichageDialogues permet d'afficher les dialogues
        """
        rectangle.Rectangle(100, 590, 390, 80, self.getCouleur().getBeige()).affiche(self.getFenetre())
        for idDialogue in range(len(dialogues)):
            texte.Texte(dialogues[idDialogue],self.getCouleur().getNoir(), 110, 600+(20*idDialogue)).affiche(self.getPolice(),self.getFenetre())
        pygame.display.update()

    def affichageAction(self, interraction, texte=None):
        """
            La fonction affichageAction permet d'afficher les interractions
        """   
        if len(interraction) == 1:
            self.getFenetre().blit(interraction[0],(360,485))
            if texte and len(texte) == 1:
                self.getFenetre().blit(self.getPolice().render(texte[0], True, self.getCouleur().getNoir()), (372,545))
        elif len(interraction) == 2:
            self.getFenetre().blit(interraction[0],(220,475))
            self.getFenetre().blit(interraction[1],(510,475))
            if texte and len(texte) == 2:
                self.getFenetre().blit(self.getPolice().render(texte[0], True, self.getCouleur().getBlanc()), (220,545))
                self.getFenetre().blit(self.getPolice().render(texte[1], True, self.getCouleur().getBlanc()), (510,545))
        elif len(interraction) == 3:
            self.getFenetre().blit(interraction[0],(225,475))
            self.getFenetre().blit(interraction[1],(325,475))
            self.getFenetre().blit(interraction[2],(425,475))
            if texte and len(texte) == 4:
                self.getFenetre().blit(self.getPolice().render(texte[0], True, self.getCouleur().getBlanc()), (240,545))
                self.getFenetre().blit(self.getPolice().render(texte[1], True, self.getCouleur().getBlanc()), (335,545))
                self.getFenetre().blit(self.getPolice().render(texte[2], True, self.getCouleur().getBlanc()), (437,545))
        elif len(interraction) == 4:
            self.getFenetre().blit(interraction[0],(225,475))
            self.getFenetre().blit(interraction[1],(325,475))
            self.getFenetre().blit(interraction[2],(425,475))
            self.getFenetre().blit(interraction[3],(525,475))
            if texte and len(texte) == 4:
                self.getFenetre().blit(self.getPolice().render(texte[0], True, self.getCouleur().getBlanc()), (240,545))
                self.getFenetre().blit(self.getPolice().render(texte[1], True, self.getCouleur().getBlanc()), (335,545))
                self.getFenetre().blit(self.getPolice().render(texte[2], True, self.getCouleur().getBlanc()), (437,545))
                self.getFenetre().blit(self.getPolice().render(texte[3], True, self.getCouleur().getBlanc()), (540,545))
        pygame.display.update()
        
    def affichageCombat(self,x,y,joueurActuel, adversaireActuel):
        """
            La fonction affichageCombat permet d'afficher l'image du joueur et de son ennemi dans un combat dans le menu.
        """
        image = pygame.image.load(joueurActuel.getLien())
        self.getFenetre().blit(image, (x,y))
        rectangle.Rectangle(500, 635, 130, 35, self.getCouleur().get_Rouge()).affiche(self.getFenetre())
        texte.Texte(joueurActuel.getPv(), self.getCouleur().getNoir(), 538, 645).affiche(self.getPolice(), self.getFenetre())

        image = pygame.image.load(adversaireActuel.getLien())
        self.getFenetre().blit(image, (620,400))
        rectangle.Rectangle(500, 635, 130, 35, self.getCouleur().get_Rouge()).affiche(self.getFenetre())
        texte.Texte(adversaireActuel.getPv(), self.getCouleur().getNoir(), 538, 645).affiche(self.getPolice(), self.getFenetre())
        pygame.display.update()

    def affichageAnimationDe(self):
        """La fonction Choix_De retourne la face aleatoire choisie du de (Surface surface).
        """
        # Affiche le de sur la face 2
        self.affichageAction([image.De.FACE2.value])
        pygame.time.delay(150)
        pygame.display.update()
        
        # Affiche le de sur la face 3
        self.affichageAction([image.De.FACE3.value])
        pygame.time.delay(200)
        pygame.display.update()

        # Affiche le de sur la face 4
        self.affichageAction([image.De.FACE4.value])
        pygame.time.delay(250)
        pygame.display.update()

        # Affiche le de sur la face 5
        self.affichageAction([image.De.FACE5.value])
        pygame.time.delay(300)
        pygame.display.update()

        # Affiche le de sur la face 1
        self.affichageAction([image.De.FACE1.value])
        pygame.time.delay(400)
        pygame.display.update()

        # Affiche le de sur la face 6
        self.affichageAction([image.De.FACE6.value])
        pygame.time.delay(450)
        pygame.display.update()
                            
        # Choisir la face aleatoire
        self.getGame().getDe().setFaceDe(random.randint(1,6))
        
        if self.getGame().getDe().getFaceDe() == 1:
            # Affiche le de sur la face 1
            self.affichageAction([image.De.FACE1.value])
            
        elif self.getGame().getDe().getFaceDe() == 2:
            # Affiche le de sur la face 2
            self.affichageAction([image.De.FACE2.value])
            
        elif self.getGame().getDe().getFaceDe() == 3:
            # Affiche le de sur la face 3
            self.affichageAction([image.De.FACE3.value])
            
        elif self.getGame().getDe().getFaceDe() == 4:
            # Affiche le de sur la face 4
            self.affichageAction([image.De.FACE4.value])
            
        elif self.getGame().getDe().getFaceDe() == 5:
            # Affiche le de sur la face 5
            self.affichageAction([image.De.FACE5.value])
            
        elif self.getGame().getDe().getFaceDe() == 6:
            # Affiche le de sur la face 6
            self.affichageAction([image.De.FACE6.value])
        pygame.display.update()

# ----------------------------------- Page du jeu ----------------------------------- #

    def affichagePageDemarrage(self):    
        self.affichageFondEcran(image.Page.DEBUT_JEU.value)

    def affichagePageStatistiques(self):
        self.affichageFondEcran(image.Page.STATS.value)
        
    def affichagePageCommande(self):
        self.affichageFondEcran(image.Page.COMMANDES.value)    

    def affichagePageNbJoueur(self):
        self.affichageFondEcran(image.Page.CHOIX_NB_JOUEUR.value)
        self.affichageAction([image.BtnMenu.BTN_1.value, image.BtnMenu.BTN_2.value, image.BtnMenu.BTN_3.value, image.BtnMenu.BTN_4.value])
        self.affichageMenu()
        self.affichageDialogues(["La sorciere du village vous a lancé un sort, pour vous en", "sortir récuper la potion chez elle.","Combien de joueurs souhaitent jouer au jeu ?"])
    
    def affichagePageNbIntelligenceA(self):
        self.affichageFondEcran(image.Page.CHOIX_NB_IA.value)
        self.affichageMenu()
        if self.getGame().getNbJoueur() == 1:
            self.affichageAction([image.BtnMenu.BTN_0.value, image.BtnMenu.BTN_1.value, image.BtnMenu.BTN_2.value, image.BtnMenu.BTN_3.value])
        elif self.getGame().getNbJoueur() == 2:
            self.affichageAction([image.BtnMenu.BTN_0.value, image.BtnMenu.BTN_1.value, image.BtnMenu.BTN_2.value])
        elif self.getGame().getNbJoueur() == 3:
            self.affichageAction([image.BtnMenu.BTN_0.value, image.BtnMenu.BTN_1.value])
        if self.getGame().getNbJoueur() != 4:
            self.affichageDialogues(["Tu as la possibilité d'ajouter des intelligences artificelles", "au jeu.", "Combien d'IA souhaites-tu intégrer au jeu ?"])
        else:
            self.affichageAction([image.BtnMenu.BTN_0.value])
            self.affichageDialogues(["Le nombre de joueurs est complet tu ne peux pas ajouter d'IA"])
       
    def affichagePageChoixPersonnage(self):  
        self.affichageFondEcran(image.Page.CHOIX_PERSO.value)
        self.affichageMenu()
        self.affichageAction([image.Personnages.ROCK.value, image.Personnages.WATER.value, image.Personnages.TOWN.value, image.Personnages.GRASS.value], ["Pierre", "Ondine", "Kevin", "Flora"])
        self.affichageDialogues(["Bienvenue à toi jeune aventurier..  C'est ici que demarre", "cette nouvelle aventure !" ,"Quel personnage souhaites-tu intégrer durant la partie ?"])
        
    def affichagePagePremierMouvement(self):
        self.affichageFondEcran(image.Page.JEU.value)
        self.affichageMenu(self.getGame().getJoueurActuel())        
        self.affichagePlateau()    
        self.affichageAction([image.De.FACE1.value])
        self.affichageDialogues(["Joueur {}, je t'invite à cliquer sur le dé. Récupère les 4 clés".format(str(self.getGame().getJoueurActuel().getId() + 1)), "de boss. N'oublie pas d'avoir assez de points de vie avant", "de te rendre chez la sorcière"])
               
    def affichagePageMouvement(self):
        self.affichageFondEcran(image.Page.CHOIX_DOUBLE.value)
        self.affichageMenu(self.getGame().getJoueurActuel())        
        self.affichagePlateau()
        self.affichageDialogues(["Joueur {}, je t'invite à cliquer sur le dé. Récupère les 4 clés".format(str(self.getGame().getJoueurActuel().getId() + 1)), "de boss. N'oublie pas d'avoir assez de points de vie avant", "de te rendre chez la sorcière"])
        self.affichageAction([image.Interaction.ATTAQUER.value, image.Interaction.DE.value], ["Attaquer", "Lancer de dé"])
           
    def affichagePageDirection(self):  
        self.affichageFondEcran(image.Page.JEU.value)
        self.affichageMenu(self.getGame().getJoueurActuel())        
        self.affichagePlateau()
        if (self.getGame().getDe().getFaceDe() == 0):
            self.affichageAnimationDe()
        self.affichageDialogues(["Bravo ! Tu peux avancer de {} cases ! Où veux-tu aller ?".format(self.getGame().getDe().getFaceDe()), "Lors des déplacements des joueurs sur le plateau, les cases", "apparaitront pour tous les joueurs"])
           
    def affichagePageHorsPlateau(self):
        self.affichageMenu(self.getGame().getJoueurActuel())
        self.affichagePlateau()    
        self.affichageDialogues(["Tu ne peux pas aller par là, tu as atteint un bord","ou il n'y a pas de cases dans cette direction", "rejoue ! Tu peux avancer de {} cases ! ".format(self.getGame().getDe().getFaceDe())])
    
    def affichagePageRejouer(self): 
        self.affichageFondEcran(image.Page.JEU.value)
        self.affichagePlateau()    
        self.affichageMenu(self.getGame().getJoueurActuel())
        self.affichageAction([image.De.FACE1.value])
        self.affichageDialogues(["Tu es le joueur " + str(self.getGame().getJoueurActuel().getId() + 1) + ", clique sur le de afin de faire ton" , "déplacement"]) 

    def affichagePageAttaque(self): 
        self.affichageFondEcran(image.Page.JEU.value)
        self.affichageMenu(self.getGame().getJoueurActuel())
        self.affichagePlateau()   

    def affichagePageActionCases(self):
        self.affichageFondEcran(image.Page.JEU.value)
        self.affichageMenu(self.getGame().getJoueurActuel())
        self.affichagePlateau()    
        self.affichageDialogues(["Tu as atterris sur une case {}".format(self.getGame().getPlateau().getNom(self.getGame().getJoueurActuel().getPlateauX(),self.getGame().getJoueurActuel().getPlateauY()))])
    
    def affichagePageSorciere(self):
        self.affichageFondEcran(image.Sorciere.MAISON.value)
        self.affichageMenu(self.getGame().getJoueurActuel())
        self.affichageDialogues(["Tu es chez la sorciere, mais j'ai l'impression","qu'elle est sortie de sa taniere...","profite-en pour fouiller dans ses affaires :)"])

    def affichagePageSorciereAstral(self):
        self.affichageFondEcran(image.Page.MAISON_SYMBOLE.value)
        self.affichageMenu(self.getGame().getJoueurActuel())
        self.affichageDialogues(["C'est un symbole astral, si c'est chez la","sorciere, il vaut mieux ne pas y toucher"])
        pygame.time.delay(2500)        
        self.getGame().setPageActuel(PageState.SORCIERE)

    def affichagePageSorciereDragon(self):
        self.affichageFondEcran(image.Page.MAISON_DRAGON.value)
        self.affichageMenu(self.getGame().getJoueurActuel())
        self.affichageDialogues(["Un dragon de pierre... ce n'est pas très","rassurant, trouvons vite un remède et sortons","d'ici très vite"])
        pygame.time.delay(2500)
        self.getGame().setPageActuel(PageState.SORCIERE)

    def affichagePageSorcierePotion(self):
        # Page de la sorcière quan don a réussi le jeu
        self.affichageFondEcran(image.Page.MAISON.value)
        self.affichageMenu(self.getGame().getJoueurActuel())
        self.affichageDialogues(["Tu as trouvé une potion... Potion inverstium","Tu décides de la boire afin d'inverser le","sortilège"])
        self.getGame().getJoueurActuel().set_inventaire(["Potion inverstium"])
        self.affichage_potion()

    def affichagePageFinPerdu(self):
        self.affichageFondEcran(image.Page.FIN_JEU.value)
        self.affichageMenu()
        self.affichageDialogues(["Aucun des joueurs n'a réussi à finir le jeu","Retentez votre chance une prochaine fois","pour profiter de cette aventure :)"])
                        
    def affichagePageFinGagne(self):
        self.affichageFondEcran(image.Page.FIN_JEU.value)
        self.affichageMenu()
        self.affichageDialogues(["Tu as terminé le jeu bravo à toi jeune aventurier","Tu es le premier a t'être libéré du sort !!"])

# ----------------------------------- Plateau du jeu ----------------------------------- #

    def affichagePageActionBleu(self):
        self.affichageFondEcran(image.Page.CHOIX_DOUBLE.value)
        self.affichageMenu(self.getGame().getJoueurActuel())
        self.affichagePlateau()    
        self.affichageDialogues(["Tu es tombe dans la case Puit... Pour t'en", "sortir, tu dois sacrifier une de tes cles", "ou 200 pv."])        
        self.affichageAction([image.Interaction.PV.value, image.Interaction.CLES.value], ["200 PV", "1 clée"])
        
    def affichagePageActionBlanc(self):
        self.affichageFondEcran(image.Page.JEU.value)
        self.affichageMenu(self.getGame().getJoueurActuel())
        self.affichagePlateau()    
        self.affichageDialogues(["Tu es sur une case vide, il ne t'arrivera rien", "mais dépêche toi de terminer le jeu en premier !"])        
        
    def affichagePageActionNoir(self):
        self.affichageFondEcran(image.Page.FIN_JEU.value)
        self.affichagePlateau()    
        self.affichageMenu(self.getGame().getJoueurActuel())
        self.affichageDialogues(["Tu n'as pas de chance...", "Tu es tombe sur la case de Mort...", "La partie est finie pour toi."])
        
    def affichagePageActionOrange(self):
        self.affichageFondEcran(image.Page.JEU.value)
        self.affichagePlateau()    
        self.affichageMenu(self.getGame().getJoueurActuel())
        self.affichageAction([image.Interaction.MALUS.value], ["Malus"])
        self.affichageDialogues(["Tu es sur une case Malus.", "Clique pour savoir quel sort", "le jeu te reserve."])

    def affichagePageActionRouge(self, un_ennemis):
        self.affichageFondEcran(image.Page.ARENE.value)
        self.affichageMenu(self.getGame().getJoueurActuel())
        self.affichageDialogues(["Tu as décidé de combattre un joueur. Le celebre ","{}. Prepare toi à le combattre afin de prendre".format(un_ennemis.get_prenom()), "l'avantage sur lui !"])
                    
    def affichagePageActionRose(self):
        self.affichageFondEcran(image.Page.JEU.value)
        self.affichagePlateau()    
        self.affichageMenu(self.getGame().getJoueurActuel())
        self.affichageAction([image.Interaction.CHANCE.value], ["Bonus"])
        self.affichageDialogues(["Tu es sur une case Chance","Clique pour decouvrir le pouvoir","que le jeu va te donner."])
                
    def affichagePageActionGris(self):
        self.affichageFondEcran(image.Page.CHOIX_DOUBLE.value)
        self.affichagePlateau()    
        self.affichageMenu(self.getGame().getJoueurActuel())
        self.affichageAction([image.Interaction.CLES.value, image.Interaction.RETOUR.value], ["1 clee", "Froussard !"])
        self.affichageDialogues(["Tu es sur une case Speciale ! Si tu tente ta chance", "tu as une chance sur deux gagner deux cles", "que tu n'as pas ou de tout perdre."])
                        
    def affichagePageActionViolet(self):
        self.affichageFondEcran(image.Page.JEU.value)
        self.affichagePlateau()    
        self.affichageMenu(self.getGame().getJoueurActuel())
        self.affichageDialogues(["Tu es sur une case Rejoue !","Relance le de pour avoir un", "deuxieme lance"])
        self.affichageAction([image.De.FACE1.value])

    def affichagePageActionBeige(self):
        self.affichageFondEcran(image.Page.CHOIX_DOUBLE.value)
        self.affichagePlateau()    
        self.affichageMenu(self.getGame().getJoueurActuel())
        self.affichageDialogues(["Tu es devant la Hutte de la sorciere.","Veux-tu essayer de l'ouvrir à l'aide", "des cles des quatre boss ?"])
        self.affichageAction([image.Interaction.CLES.value, image.Interaction.RETOUR.value], ["Entrer dans l'entre", "Plus tard"])

    def affichagePageActionJaune(self):
        self.affichageFondEcran(image.Page.JEU.value)
        self.affichagePlateau()
        self.affichageMenu(self.getGame().getJoueurActuel())
        self.affichageDialogues(["Tu es la case de Depart.","Depeche toi de recuperer les cles","avant les autres joueurs."])
                
    def affichagePageActionIndigo(self):
        self.affichageFondEcran(image.Page.CHOIX_DOUBLE.value)
        self.affichagePlateau()    
        self.affichageMenu(self.getGame().getJoueurActuel())
        self.affichageDialogues(["Tu es sur une case de Teleportation. Veux-tu etre teleporter","en passant par le passage secret ?"])
        self.affichageAction([image.Interaction.TP.value, image.Interaction.RETOUR.value], ["Avec plaisir", "Non merci"])
        
    def affichagePageActionVert(self):
        self.affichageFondEcran(image.Page.JEU.value)
        self.affichagePlateau()    
        self.affichageMenu(self.getGame().getJoueurActuel())
        self.affichageDialogues(["Tu es sur une case Grrr", "Un tremblement de terre surgit de nul part", "et teleporte tous les joueurs !!!"])        