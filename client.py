
from enum import Enum
import pygame, joueur
import interface, game
from utils import image, texte, logique, rectangle
from input import inputs, direction
import time, random
from utils.rectangle import Rectangle

class ClientState(Enum):

    LOCAL = 1 # création de la map, envoi des donné au joueur

    ONLINE = 2 # attente que le MAX_PLAYER sois atteint

    MENU = 3 # creation d'une instance de serveur

    STARTING = 4 # création de la map, envoi des donné au joueur

    WAIT_CONNECION = 4 # attente que le MAX_PLAYER sois atteint

    IN_GAME = 5 # boucle de jeu principal

    QUIT = 6 # fin du serveur envoi des donné à la bd pour les stat

class PartieState(Enum):

    INDEX = 1 # creation d'une instance de serveur

    GLOBALS_STATS = 4 # boucle de jeu principal

    HELPER = 5 # fin du serveur envoi des donné à la bd pour les stats

    NB_PLAYER = 6 

    NB_IA = 7

class Client():

# --------- Initialisation du client --------- #
    def __init__(self) -> None:
        self.__clock:pygame.time.Clock =  pygame.time.Clock()
        self.__fenetre = pygame.display.set_mode((800, 700))
        self.__etatPartie:PartieState = PartieState.INDEX
        self.__etatClient:ClientState = ClientState.MENU
        self.__dialogues:str = ""
        self.__interface:interface.Interface = None
        self.__game:game.Game = None
        self.__joueurLocal:list[int] = []
        self.currentIdDe:int = 0
        self.currentImageDe:image.De = None
        self.__timerAnimation = {}

# --------- Getter et Setter du client --------- #

    def getClock(self):
        """Renvoie le temps écoulé dans la partie"""
        return self.__clock

    def setClock(self, clock):
        """Modifie le temps écoulé dans la partie"""
        self.__clock = clock

    def getFenetre(self):
        """Renvoie la surface de la partie"""
        return self.__fenetre

    def setFenetre(self, fenetre):
        """Modifie la surface de la partie"""
        self.__fenetre = fenetre

    def getEtatPartie(self):
        """Renvoie l'état de la partie"""
        return self.__etatPartie

    def setEtatPartie(self, etatPartie):
        """Modifie l'état de la partie"""
        self.__etatPartie = etatPartie
    
    def getEtatClient(self):
        """Renvoie l'état du client"""
        return self.__etatClient

    def setEtatClient(self, etatClient):
        """Modifie l'état du client"""
        self.__etatClient = etatClient
    
    def getDialogues(self):
        """Renvoie les dialogues actuels affiché dans le menu"""
        return self.__dialogues

    def setDialogues(self, dialogues: list[str]):
        """Modifie les dialogues affiché dans le menu"""
        self.__dialogues = dialogues

    def getInterface(self):
        """Renvoie l'interface du jeu"""
        return self.__interface

    def setInterface(self, interface):
        """Modifie l'interface du jeu"""
        self.__interface = interface
    
    def getGame(self):
        """Renvoie la game"""
        return self.__game

    def setGame(self, game):
        """Modifie la game"""
        self.__game = game

    def getJoueurLocal(self):
        """Renvoie le joueur local du jeu"""
        return self.__joueurLocal

    def setJoueurLocal(self, joueurLocal):
        """Modifie le joueur local du jeu"""
        self.__joueurLocal = joueurLocal
    
    def boutonRetour(self):
        """Bouton de retour en arrière sur les pages"""
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return 40 <= mouse_x <= 100 and 40 <= mouse_y <= 100
    
    # Affichage de la partie basse du jeu en focntion du joueur qui joue
    def MenuBas(self, un_joueur):
        # Dessiner la partie basse
        pygame.draw.rect(self.getFenetre(),logique.Couleur.GRIS.value,(10,580,780,102))
        
        # Dessiner la place pour montrer les cles
        rectangle.Rectangle(650,585,130,90,logique.Couleur.ROSE.value).affiche(self.getFenetre())
        self.afficheCle(un_joueur)
        
        # Dessiner le rectangle pour les pv du joueur
        rectangle.Rectangle(500,590,130,35,logique.Couleur.VERT.value).affiche(self.getFenetre())
        texte.Texte("PV joueur : ", logique.Couleur.NOIR.value, 500,590).affiche(self.getFenetre())
        
        # Dessiner les bords de la place pour les pv de l'adversaire
        rectangle.Rectangle(500,635,130,35,logique.Couleur.ROUGE.value).affiche(self.getFenetre())

        # Dessiner le rectangle pour les textes
        rectangle.Rectangle(100, 590, 390, 80, logique.Couleur.BEIGE.value).affiche(self.getFenetre())
        
        # Cadre pour mettre le personnage choisi
        rectangle.Rectangle(20,590,70,80,logique.Couleur.ROSE.value).affiche(self.getFenetre())
        
        # Prendre la variable du personnage choisi de "Position_choix_perso()""
        if un_joueur.getPrenom() == joueur.Nom.ROCK.value:
            # Ajouter la photo de Pierre
            self.afficheImage(24,598,un_joueur)
        
        if un_joueur.getPrenom() == joueur.Nom.WATER.value:
            # Ajouter la photo de Ondine
            self.afficheImage(24,598,un_joueur)
        
        if un_joueur.getPrenom() == joueur.Nom.GRASS.value:
            # Ajouter la photo de Pierre
            self.afficheImage(24,598,un_joueur)
        
        if un_joueur.getPrenom() == joueur.Nom.TOWN.value:
            # Ajouter la photo de Pierre
            self.afficheImage(24,598,un_joueur)
        
    def affichagePlateau(self):
        """Met à jour le plateau en affichant les cases découvertes."""
        font = pygame.font.Font(('./assets/font/Dosis-VariableFont_wght.ttf'), 11)
        for i in self.getGame().getPlateau().getCasesDecouvertes():
            couleur_case = self.getGame().getPlateau().getCases(i[0],i[1]).value # Obtenir la couleur de la case
            x = i[1] * self.getGame().getPlateau().getTailleCase()  # Coordonnée X du coin supérieur gauche du rectangle
            y = i[0] * self.getGame().getPlateau().getTailleCase()  # Coordonnée Y du coin supérieur gauche du rectangle          
            rectangle = pygame.Rect(x, y, self.getGame().getPlateau().getTailleCase(), self.getGame().getPlateau().getTailleCase())  # Créer un rectangle
            pygame.draw.rect(self.getFenetre(), couleur_case.value, rectangle)  # Dessiner le rectangle avec la couleur
            if (self.getGame().getPlateau().getCases(i[0],i[1]).name != 'MORT' and self.getGame().getPlateau().getCases(i[0],i[1]).name != 'SPAWN' and self.getGame().getPlateau().getCases(i[0],i[1]).name != 'NOTHING'):
                texte_surface = font.render(str(self.getGame().getPlateau().getCases(i[0],i[1]).name), True, logique.Couleur.NOIR.value)
                self.getFenetre().blit(texte_surface, (x + 9, y + 15))
        self.afficheJoueurs()

    
    def afficheDialogues(self):
        """Afficher les dialogues."""
        Rectangle(100, 590, 390, 80, logique.Couleur.BEIGE.value).affiche(self.getFenetre())
        for idDialogue in range(len(self.getDialogues())):
            texte.Texte(self.getDialogues()[idDialogue], logique.Couleur.NOIR.value, 110, 600 + (20 * idDialogue)).affiche(self.getFenetre())

    def afficheDialoguesDeb(self):
        """Afficher les dialogues du début"""
        Rectangle(10, 580, 780, 100, logique.Couleur.GRIS.value).affiche(self.getFenetre())
        for idDialogue in range(len(self.getDialogues())):
            texte.Texte(self.getDialogues()[idDialogue], logique.Couleur.NOIR.value, 30, 600 + (20 * idDialogue)).affiche(self.getFenetre())

    # Définir l'affichage des clés dans l'inventaire du joueur
    def afficheCle(self,joueur):
        """
            La fonction affichage_cle permet d'afficher les cle dans le menu(int x, int y, Surface surface, Font font)
        """
        for i in joueur.getInventaire():
            if i == "cle de la Ville" :
                image.Image(660,640,image.Cle.TOWN.value).affichageImageRedimensionnee(48,30,self.getFenetre())
            elif i == "cle de la Rivière" :
                image.Image(660,595,image.Cle.WATER.value).affichageImageRedimensionnee(48,30,self.getFenetre())
            elif i == "cle de la Forêt" :
                image.Image(725,595,image.Cle.GRASS.value).affichageImageRedimensionnee(48,30,self.getFenetre())
            elif i == "cle du Rocher" :
                image.Image(725,640,image.Cle.ROCK.value).affichageImageRedimensionnee(48,30,self.getFenetre())
        pygame.draw.line(self.getFenetre(), logique.Couleur.NOIR.value, (660, 632), (770, 632), 2)
        pygame.draw.line(self.getFenetre(), logique.Couleur.NOIR.value, (715, 595), (715, 670), 2)

    # Definir l'affichage sur le menu
    def afficheImage(self,x,y,joueur):
        """
            La fonction afficheImage permet d'afficher le personnage dans le menu(int x, int y, Surface surface, Font font)
        """        
        # Afficher l'image sur la fenetre
        self.getFenetre().blit(joueur.getImage(), (x, y))
        
        # Dessiner le rectangle pour les pv du joueur
        rectangle.Rectangle(500,590,130,35,logique.Couleur.VERT.value).affiche(self.getFenetre())
    
        # Charger les pv
        texte.Texte(joueur.getPv(),logique.Couleur.NOIR.value,538,598).affiche(self.getFenetre())
        
    # Definir l'affichage de l'adversaire lors des combats
    def afficheImage_adv(self,x,y,joueur):
        """Affiche l'image de l'ennemi dans le menu."""
        image = pygame.image.load(joueur.getImage())
        self.getFenetre().blit(image, (x,y))
        rectangle.Rectangle(500, 635, 130, 35, logique.Couleur.ROUGE.value).affiche(self.getFenetre())
        texte.Texte(joueur.getPv(), logique.Couleur.NOIR.value, 538, 645).affiche(self.getFenetre())
    
    # Definir l'affichage sur le plateau
    def afficheImagePlateau(self, joueur):
        """
            La fonction afficheImage_plateau permet d'afficher le personnage dans le plateau(int x, int y, Surface surface)
        """
        # Charger l'image
        image_redimensionnee = pygame.transform.scale(joueur.getImage(), (47, 47))
        
        # Afficher l'image redimensionnee sur la fenetre
        self.getFenetre().blit(image_redimensionnee, (joueur.getY(), joueur.getX()))
                

    # Definir l'affichage des joueurs sur le plateau
    def afficheJoueurs(self):
        """Affiche tous les joueurs sur le plateau."""
        if len(self.getGame().getListeJoueur()) != 0 and self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()] != None:
            for i in self.getGame().getListeJoueur():
                self.afficheImagePlateau(i)

    
    # Définir l'affichage de la potion
    def affichePotion(self):
        """
            La fonction afficheImage_plateau permet d'afficher le personnage dans le plateau(int x, int y, Surface surface)
        """
        # Charger l'image
        potion = image.Sorciere.POTION.value
        
        # Afficher l'image redimensionnee sur la fenetre
        self.getFenetre().blit(potion, (668, 593))
          
    
    def afficheAnimationDe(self):
        listeDe = [image.De.FACE2.value, image.De.FACE1.value, image.De.FACE4.value, image.De.FACE6.value, image.De.FACE5.value, image.De.FACE3.value]
        if 'de' not in self.__timerAnimation.keys():
            self.__timerAnimation['de'] = time.time()
        if self.currentIdDe >= len(listeDe):
            self.__timerAnimation['de'] = time.time()
            self.currentIdDe = 0
            self.affichageResultatDe()
        else:
            self.getFenetre().blit(listeDe[self.currentIdDe],(350,475))
        animationDelay = 0.23 - int(0.19*(self.currentIdDe/len(listeDe)))
        if self.__timerAnimation['de'] + animationDelay < time.time() :
                self.currentIdDe += 1
                self.__timerAnimation['de'] = time.time()

    def affichageResultatDe(self):
        if self.getGame().getDeValue() == 1:
            # Affiche le de sur la face 1
            self.currentImageDe = image.De.FACE1.value
            self.getFenetre().blit(self.currentImageDe,(350,475))
            
        elif self.getGame().getDeValue() == 2:
            # Affiche le de sur la face 2
            self.currentImageDe = image.De.FACE2.value
            self.getFenetre().blit(self.currentImageDe,(350,475))
            
        elif self.getGame().getDeValue() == 3:
            # Affiche le de sur la face 3
            self.currentImageDe = image.De.FACE3.value
            self.getFenetre().blit(self.currentImageDe,(350,475))
            
        elif self.getGame().getDeValue() == 4:
            # Affiche le de sur la face 4
            self.currentImageDe = image.De.FACE4.value
            self.getFenetre().blit(self.currentImageDe,(350,475))
            
        elif self.getGame().getDeValue() == 5:
            # Affiche le de sur la face 5
            self.currentImageDe = image.De.FACE5.value
            self.getFenetre().blit(self.currentImageDe,(350,475))
            
        elif self.getGame().getDeValue() == 6:
            # Affiche le de sur la face 6
            self.currentImageDe = image.De.FACE6.value
            self.getFenetre().blit(self.currentImageDe,(350,475))
        self.getGame().setEtat(game.GameState.MOVE_PLAYER)

# --------- Boucle principale du jeu qui fait l'affichage et la logique --------- #

    # Permets de switcher entre les affichage des pages
    def affichagePartie(self):
        self.getFenetre().fill(logique.Couleur.NOIR.value)
        match self.getEtatClient() :
            
            # Boucle du Menu
            case ClientState.MENU:
                match self.getEtatPartie() : # Gestion de l'etat du menu
                    
                    # Page du menu
                    case PartieState.INDEX:
                        image.Image(0,0,image.Page.DEBUT_JEU.value).affiche(self.getFenetre())
                    
                    # Page de statistiques
                    case PartieState.GLOBALS_STATS:
                        image.Image(0,0,image.Page.STATS.value).affiche(self.getFenetre())
                    
                    # Page des règles du jeu
                    case PartieState.HELPER:
                        image.Image(0, 0, image.Page.COMMANDES.value).affiche(self.getFenetre())
                    
                    # Page du nombre de joueurs
                    case PartieState.NB_PLAYER:
                        image.Image(0, 0, image.Page.CHOIX_NB_JOUEUR.value).affiche(self.getFenetre())
                        self.setDialogues(["La sorciere du village vous a lancé un sort, pour","vous en sortir récuper la potion chez elle.","Combien de joueurs souhaitent jouer au jeu ?"])
                        self.afficheDialoguesDeb()
                        image.Image(400, 595, image.BtnMenu.BTN_1.value).affiche(self.getFenetre())
                        image.Image(500, 595, image.BtnMenu.BTN_2.value).affiche(self.getFenetre())
                        image.Image(600, 595, image.BtnMenu.BTN_3.value).affiche(self.getFenetre())
                        image.Image(700, 595, image.BtnMenu.BTN_4.value).affiche(self.getFenetre())

                    # Page du nombre de ia
                    case PartieState.NB_IA:
                        selectable_nb_ia = self.getInterface().selectionnableNombreIA()
                        image.Image(0, 0, image.Page.CHOIX_NB_IA.value).affiche(self.getFenetre())
                        self.setDialogues(["Combien d'IA souhaites-tu ajouter au jeu ?"])
                        self.afficheDialoguesDeb()
                        if 1 in selectable_nb_ia :
                            image.Image(400, 595, image.BtnMenu.BTN_0.value).affiche(self.getFenetre())
                            image.Image(500, 595, image.BtnMenu.BTN_1.value).affiche(self.getFenetre())
                            image.Image(600, 595, image.BtnMenu.BTN_2.value).affiche(self.getFenetre())
                            image.Image(700, 595, image.BtnMenu.BTN_3.value).affiche(self.getFenetre())
                        if 2 in selectable_nb_ia :
                            image.Image(400, 595, image.BtnMenu.BTN_0.value).affiche(self.getFenetre())
                            image.Image(500, 595, image.BtnMenu.BTN_1.value).affiche(self.getFenetre())
                            image.Image(600, 595, image.BtnMenu.BTN_2.value).affiche(self.getFenetre())
                        if 3 in selectable_nb_ia :
                            image.Image(400, 595, image.BtnMenu.BTN_0.value).affiche(self.getFenetre())
                            image.Image(500, 595, image.BtnMenu.BTN_1.value).affiche(self.getFenetre())
                        if 4 in selectable_nb_ia :
                            texte.Texte("Le nombre de joueurs est complet tu ne peux pas ajouter d'IA", logique.Couleur.NOIR.value, 30, 600).affiche(self.getFenetre())

                
            # En local
            case ClientState.LOCAL:
                match self.getGame().getEtat():

                    # Page_ChoixPerso
                    case game.GameState.SELECT_AVATAR:
                        image.Image(0, 0, image.Page.CHOIX_PERSO.value).affichageImageRedimensionnee(800, 700,self.getFenetre())
                        self.setDialogues(["Bienvenue à toi jeune aventurier ! Amusez-vous bien","ici demarre une nouvelle aventure ! Je t'invite à","choisir un personnage parmi la liste suivante :"])
                        self.afficheDialoguesDeb()
                        image.Image(400, 585, image.Personnages.ROCK.value).affiche(self.getFenetre())
                        texte.Texte(joueur.Nom.ROCK.value, logique.Couleur.NOIR.value, 413, 650).affiche(self.getFenetre())
                        image.Image(500, 585, image.Personnages.WATER.value).affiche(self.getFenetre())
                        texte.Texte(joueur.Nom.WATER.value, logique.Couleur.NOIR.value, 510, 650).affiche(self.getFenetre())
                        image.Image(600, 585, image.Personnages.TOWN.value).affiche(self.getFenetre())
                        texte.Texte(joueur.Nom.TOWN.value, logique.Couleur.NOIR.value, 613, 650).affiche(self.getFenetre())
                        image.Image(700, 585, image.Personnages.GRASS.value).affiche(self.getFenetre())
                        texte.Texte(joueur.Nom.GRASS.value, logique.Couleur.NOIR.value, 715, 650).affiche(self.getFenetre())
                    
                    # Page_PremierMouvement
                    case game.GameState.USE_DIE:
                        image.Image(0,468,image.Page.BAS_PLATEAU.value).affiche(self.getFenetre())
                        self.affichagePlateau()
                        self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.setDialogues(["Tu es le joueur " + str(self.getGame().getIdJoueurActuel() + 1) + ", clique sur le de afin de faire ton","déplacement : haut, bas, gauche ou droite"])
                        self.afficheDialogues()
                        image.Image(350,475,image.De.FACE1.value).affiche(self.getFenetre())
                    
                    # Page_Mouvement
                    case game.GameState.SELECT_ACTION:
                        player = self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()]
                        image.Image(0,468, image.Page.CHOIX_DOUBLE.value).affiche(self.getFenetre())
                        self.affichagePlateau()
                        self.MenuBas(player)
                        
                        texte.Texte("Joueur " + str(player.getId() + 1) + " : " + player.getPrenom() + " clique sur le de afin ",logique.Couleur.NOIR.value,110,600).affiche(self.getFenetre())
                        texte.Texte("d'attaquer un joueur ou de lancer le de",logique.Couleur.NOIR.value,110,620).affiche(self.getFenetre())
                        
                        # Affiche le de sur la face 1
                        image.Image(220,480,image.Interaction.ATTAQUER.value).affiche(self.getFenetre())
                        image.Image(510, 480,image.Interaction.DE.value).affiche(self.getFenetre())
                        texte.Texte("Attaquer",logique.Couleur.BLANC.value,227,545).affiche(self.getFenetre())
                        texte.Texte("De",logique.Couleur.BLANC.value,532,545).affiche(self.getFenetre())

                    # Page_LancementDe
                    case game.GameState.LANCEMENT_DE:
                        image.Image(0,468,image.Page.BAS_PLATEAU.value).affiche(self.getFenetre())
                        self.affichagePlateau()
                        self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.afficheAnimationDe()

                    # Page_Direction
                    case game.GameState.MOVE_PLAYER:
                        image.Image(0,468,image.Page.BAS_PLATEAU.value).affiche(self.getFenetre())
                        self.affichagePlateau()
                        self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        temp_texte=("Bravo ! Tu peux avancer de {} cases ! Où ".format(self.getGame().getDeValue()))
                        self.setDialogues([temp_texte, "veux-tu aller ? (haut, bas, gauche, droite)"])
                        self.afficheDialogues()
                        image.Image(350,475,self.currentImageDe).affiche(self.getFenetre())

                    # Page_Action
                    case game.GameState.STAY_ON_CASE:
                        couleur_case = self.getGame().getPlateau().getCases(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()].getPlateaux(),self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()].getPlateauy()).value.value
                        if couleur_case == logique.Couleur.BEIGE.value:
                            image.Image(0,468,image.Page.CHOIX_DOUBLE.value).affiche(self.getFenetre())
                            self.affichagePlateau()
                            self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                            self.setDialogues(["Tu es devant la Hutte de la sorciere.","Veux-tu essayer de l'ouvrir à l'aide","des cles des quatre boss ?"])
                            self.afficheDialogues()
                            self.getFenetre().blit(image.Interaction.CLES.value, (220, 480))
                            self.getFenetre().blit(image.Interaction.RETOUR.value, (510,480))
                            texte.Texte("Ouvrir la porte",logique.Couleur.BLANC.value,212,545).affiche(self.getFenetre())
                            texte.Texte("Passer son chemin",logique.Couleur.BLANC.value,485,545).affiche(self.getFenetre())
                            
                        elif couleur_case == logique.Couleur.BLANC.value:
                            image.Image(0,468,image.Page.BAS_PLATEAU.value).affiche(self.getFenetre())
                            self.affichagePlateau()
                            self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                            self.setDialogues(["Tu es dans une case Vide.", "Il ne t'arrivera rien tu peux etre rassure."])
                            self.afficheDialogues()
                            
                        elif couleur_case == logique.Couleur.BLEU.value:
                            image.Image(0,468,image.Page.CHOIX_DOUBLE.value).affiche(self.getFenetre())
                            self.affichagePlateau()
                            self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                            self.setDialogues(["Tu es tombe dans la case Puit... Pour t'en","sortir, tu dois sacrifier une de tes cles","ou 200 pv."])        
                            self.getFenetre().blit(image.Interaction.PV.value, (220, 480))
                            self.getFenetre().blit(image.Interaction.CLES.value, (510, 480))
                            texte.Texte("200 PV",logique.Couleur.BLANC.value,235,545).affiche(self.getFenetre())
                            texte.Texte("1 clee",logique.Couleur.BLANC.value,525,545).affiche(self.getFenetre())

                        elif couleur_case == logique.Couleur.GRIS.value:
                            image.Image(0,468,image.Page.CHOIX_DOUBLE.value).affiche(self.getFenetre())
                            self.affichagePlateau()
                            self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                            self.setDialogues(["Tu es sur une case Speciale ! Si tu tente","ta chance, tu as une chance sur deux gagner", "deux cles que tu n'as pas ou de tout perdre."])
                            self.afficheDialogues()
                            self.getFenetre().blit(image.Interaction.CLES.value, (220, 480))
                            self.getFenetre().blit(image.Interaction.RETOUR.value, (510,480))
                            texte.Texte("1 clee",logique.Couleur.BLANC.value,215,545).affiche(self.getFenetre())
                            texte.Texte("Passer son tour",logique.Couleur.BLANC.value,505,545).affiche(self.getFenetre())

                        elif couleur_case == logique.Couleur.INDIGO.value:
                            image.Image(0,468,image.Page.CHOIX_DOUBLE.value).affiche(self.getFenetre())
                            self.affichagePlateau()
                            self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                            self.setDialogues(["Tu es sur une case de Teleportation.","Veux-tu etre teleporter ?"])
                            self.afficheDialogues()
                            self.getFenetre().blit(image.Interaction.TP.value, (220, 480))
                            self.getFenetre().blit(image.Interaction.RETOUR.value, (510,480))
                            texte.Texte("Se teleporter",logique.Couleur.BLANC.value,212,545).affiche(self.getFenetre())
                            texte.Texte("Non merci",logique.Couleur.BLANC.value,502,545).affiche(self.getFenetre())
                            pygame.display.update()

                        elif couleur_case == logique.Couleur.JAUNE.value:
                            image.Image(0,468,image.Page.BAS_PLATEAU.value).affiche(self.getFenetre())
                            self.affichagePlateau()
                            self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                            self.setDialogues(["Tu es la case de Depart.","Depeche toi de recuperer les cles","avant les autres joueurs."])
                            self.afficheDialogues()
                            
                        elif couleur_case == logique.Couleur.NOIR.value:
                            image.Image(0,468,image.Page.BAS_PLATEAU.value).affiche(self.getFenetre())
                            self.affichagePlateau()
                            self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                            self.setDialogues(["Tu n'as pas de chance...", "Tu es tombe sur la case de Mort...", "La partie est finie pour toi."])
                            self.afficheDialogues()

                        elif couleur_case == logique.Couleur.ORANGE.value:
                            image.Image(0,468,image.Page.BAS_PLATEAU.value).affiche(self.getFenetre())
                            self.affichagePlateau()
                            self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                            self.setDialogues(["Tu es sur une case Malus.", "Clique pour savoir quel sort", "le jeu te reserve."])
                            self.afficheDialogues()
                            self.getFenetre().blit(image.Interaction.MALUS.value, (360,475))
                            texte.Texte("Malus",logique.Couleur.NOIR.value,372,545).affiche(self.getFenetre())
        
                        elif couleur_case == logique.Couleur.ROSE.value:
                            image.Image(0,468,image.Page.BAS_PLATEAU.value).affiche(self.getFenetre())
                            self.affichagePlateau()
                            self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                            self.setDialogues(["Tu es sur une case Chance","Clique pour decouvrir le pouvoir","que le jeu va te donner."])
                            self.afficheDialogues()
                            self.getFenetre().blit(image.Interaction.CHANCE.value, (360,475))
                            texte.Texte("Chance",logique.Couleur.NOIR.value,369,545).affiche(self.getFenetre())

                        elif couleur_case == logique.Couleur.ROUGE.value:
                            pass

                        elif couleur_case == logique.Couleur.TURQUOISE.value:
                            image.Image(0,468,image.Page.BAS_PLATEAU.value).affiche(self.getFenetre())
                            self.affichagePlateau()
                            self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                            self.setDialogues(["Tu es sur une case Grrr", "Un tremblement de terre surgit de nul part", "et teleporte tous les joueurs !!!"])
                            self.afficheDialogues()

                        elif couleur_case == logique.Couleur.VIOLET.value:
                            image.Image(0,468,image.Page.BAS_PLATEAU.value).affiche(self.getFenetre())
                            self.affichagePlateau()
                            self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                            self.setDialogues(["Tu es sur une case Rejoue !","Relance le de pour avoir un","deuxieme lance"])
                            self.afficheDialogues()
                            self.getFenetre().blit(image.De.FACE1.value,(350,475))
                    
                    case game.GameState.CASE_CHANCE:
                        image.Image(0,468,image.Page.BAS_PLATEAU.value).affiche(self.getFenetre())
                        self.affichagePlateau()
                        self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.setDialogues(["Tou-dou-dou-doum","Tu vas {}".format(self.getGame().getChanceAction())])
                        self.afficheDialogues()

                    case game.GameState.CASE_MALUS:
                        image.Image(0,468,image.Page.BAS_PLATEAU.value).affiche(self.getFenetre())
                        self.affichagePlateau()
                        self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.setDialogues(["Tou-dou-dou-doum","Tu vas {}".format(self.getGame().getMalusAction())])
                        self.afficheDialogues()
                    
                    case game.GameState.CASE_RETOUR:
                        image.Image(0,468,image.Page.BAS_PLATEAU.value).affiche(self.getFenetre())
                        self.affichagePlateau()
                        self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.setDialogues(["Dommage, retente ta chance une prochaine fois","et dépêche toi de récupérer les clés avant", "les autres joueurs !!!"])
                        self.afficheDialogues()
                    
                    case game.GameState.CASE_TELEPORTE:
                        image.Image(0,468,image.Page.BAS_PLATEAU.value).affiche(self.getFenetre())
                        self.affichagePlateau()
                        self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.setDialogues(["Tou-dou-dou-doum","Teleportation sur la deuxieme case de téléportation"])
                        self.afficheDialogues()

                    case game.GameState.CASE_PV_PUIT:
                        self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        dialogue = ["Tu as donnée 200PV, tu peux sortir du puis"]if self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()].getPv()>0 else ["Tu as donnée 200PV, Mais tu est mort"]
                        self.afficheDialogues()
                        self.setDialogues(dialogue)
                    case game.GameState.CASE_CLE_PUIT:
                        self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.setDialogues(["Tu as donnée 1 clef, tu peux sortir du puis"])
                        self.afficheDialogues()
                    case game.GameState.CASE_CLE_SPECIALE:
                        self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        dialogue = ["Bravo tu as gagner !!!","Voilà deux cles supplementaires que tu peux", "voir apparaître dans ton inventaire."] if self.__game.getSpecialAction()  == "bravo" else ["Oh non dommage...","Tu peux retenter ta chance si tu as", "d'autres cles :)"]
                        self.setDialogues(dialogue)
                        self.afficheDialogues()
                    case game.GameState.FIGHT:
                        pass
                    case game.GameState.WAIT_FIGHT_ACTION:
                        pass
                    case game.GameState.DO_FIGHT_ACTION:
                        pass
                    case game.GameState.DEAD:
                        pass
                    case game.GameState.SWITCH_PLAYER:
                        pass
            
            # En ligne
            case ClientState.ONLINE:
                pass
            
        pygame.display.update()
        self.getClock().tick(60)  

    # Gestion des pages
    def menu_logical(self, mouse_x:int, mouse_y:int, is_cliked:bool):
        match self.getEtatPartie() :
            case PartieState.INDEX:
                if is_cliked:
                    if (320 <= mouse_x <= 470 and 500 <= mouse_y <= 550) : # si appuie bouton stats
                        self.setEtatPartie(PartieState.GLOBALS_STATS)
                    if (170 <= mouse_x <= 350 and 550 <= mouse_y <= 600) : # si appuie bouton en local
                        self.setEtatPartie(PartieState.NB_PLAYER)
                        self.setInterface(interface.Interface(False))
                    if (450 <= mouse_x <= 630 and 550 <= mouse_y <= 600) : # si appuie bouton en ligne
                        self.setEtatPartie(PartieState.NB_PLAYER)
                        self.setInterface(interface.Interface(True))
                    if 700 <= mouse_x <= 764 and 25 <= mouse_y <= 89 : # si appuie sur info
                        self.setEtatPartie(PartieState.HELPER)
                pass
            case PartieState.GLOBALS_STATS:
                if is_cliked:
                    if (self.boutonRetour()): # si appuie sur fleche retour
                        self.setEtatPartie(PartieState.INDEX)
                        stats = True
                pass
            case PartieState.HELPER:
                if is_cliked:
                    if (self.boutonRetour()) : # si appuie bouton play
                        self.setEtatPartie(PartieState.INDEX)
                        
            case PartieState.NB_PLAYER:
                if is_cliked:
                    if (self.boutonRetour()) : # si appuie bouton play
                        self.setEtatPartie(PartieState.INDEX)
                    # Si le personnage sur lequel on clique est J2
                    if 500 <= mouse_x <= 600 and 582 <= mouse_y <= 652 :
                        self.getInterface().setNombreJoueur(2)
                        if self.getInterface().getEnLigne():
                            self.setEtatClient(ClientState.STARTING)
                        else:
                            self.setEtatPartie(PartieState.NB_IA)
                    # Si le personnage sur lequel on clique est J4
                    if 700 <= mouse_x <= 800 and 582 <= mouse_y <= 652 :
                        self.getInterface().setNombreJoueur(4)
                        if self.getInterface().getEnLigne():
                            self.setEtatClient(ClientState.STARTING)
                        else:
                            self.setEtatPartie(PartieState.NB_IA)
                    # Si le personnage sur lequel on clique est J1
                    if 400 <= mouse_x <= 500 and 582 <= mouse_y <= 652 :
                        self.getInterface().setNombreJoueur(1)
                        if self.getInterface().getEnLigne():
                            self.setEtatClient(ClientState.STARTING)
                        else:
                            self.setEtatPartie(PartieState.NB_IA)
                    # Si le personnage sur lequel on clique est J3
                    if 600 <= mouse_x <= 700 and 582 <= mouse_y <= 652 :
                        self.getInterface().setNombreJoueur(3)
                        if self.getInterface().getEnLigne():
                            self.setEtatClient(ClientState.STARTING)
                        else:
                            self.setEtatPartie(PartieState.NB_IA)
                    pass
            case PartieState.NB_IA:
                # Recuperer les coordonnees de la souris
                selectable_nb_ia = self.getInterface().selectionnableNombreIA()
                if is_cliked:
                    if (40 <= mouse_x <= 100 and 40 <= mouse_y <= 100) : # si appuie bouton play
                        self.getInterface().setNombreIA(0)
                        self.setEtatPartie(PartieState.NB_PLAYER)
                    
                    # Si le personnage sur lequel on clique est J1
                    if 400 <= mouse_x <= 500 and 582 <= mouse_y <= 652 and 0 in selectable_nb_ia:   
                        self.getInterface().setNombreIA(0)
                    # Si le personnage sur lequel on clique est J2   
                    if 500 <= mouse_x <= 600 and 582 <= mouse_y <= 652 and 1 in selectable_nb_ia:
                        self.getInterface().setNombreIA(1)
                    # Si le personnage sur lequel on clique est J3
                    if 600 <= mouse_x <= 700 and 582 <= mouse_y <= 652 and 2 in selectable_nb_ia:   
                        self.getInterface().setNombreIA(2)
                    # Si le personnage sur lequel on clique est J4
                    if 700 <= mouse_x <= 800 and 582 <= mouse_y <= 652 and 3 in selectable_nb_ia:   
                        self.getInterface().setNombreIA(3)
                    self.setGame(self.getInterface().genererPartie())
                    self.setJoueurLocal([i for i in range(len(self.getGame().getListeJoueur()))])
                    self.setEtatClient(ClientState.ONLINE if self.getInterface().getEnLigne() else ClientState.LOCAL)

    # Boucle du jeu lorsque le jeu est démarrer qui permet de gérer les événements
    def main(self):
        self.setEtatPartie(PartieState.INDEX)
        while (self.getEtatClient() != ClientState.QUIT):
            self.affichagePartie()
            click = False
            dir = direction.ANY

            for event in pygame.event.get():
                if event.type == pygame.QUIT: # si le joueur quitte la fenetre
                    pygame.quit()
                    self.setEtatClient(ClientState.QUIT)

                if(event.type == pygame.MOUSEBUTTONUP): click = True
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_z:
                        dir = direction.NORTH
                    elif event.key == pygame.K_UP:
                        dir = direction.NORTH
                    elif event.key == pygame.K_d:
                        dir = direction.EAST
                    elif event.key == pygame.K_RIGHT:
                        dir = direction.EAST
                    elif event.key == pygame.K_s:
                        dir = direction.SOUTH
                    elif event.key == pygame.K_DOWN:
                        dir = direction.SOUTH
                    elif event.key == pygame.K_q:
                        dir = direction.WEST
                    elif event.key == pygame.K_LEFT:
                        dir = direction.WEST
                     
            mouse_x, mouse_y = pygame.mouse.get_pos()
            match self.getEtatClient():
                case ClientState.MENU:
                    self.menu_logical(mouse_x, mouse_y, click)
                case ClientState.LOCAL:
                    self.getGame().loop(inputs(mouse_x, mouse_y, click, dir))
                case ClientState.ONLINE:
                    # envoyé les inputs au server
                    pass
                case ClientState.QUIT:
                    pass
            
            
if __name__ == "__main__":
    Client().main()
