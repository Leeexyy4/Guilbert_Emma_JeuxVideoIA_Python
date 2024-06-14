
from enum import Enum
import pygame, joueur
import interface, game
from utils import image, texte, logique, rectangle
from input import inputs, direction
import time, random, pickle, socket
from utils.rectangle import Rectangle

from database import creer_partie
from database import envoyer_donnees_bdd
from database import recuperer_donnees_bdd

host = '192.168.1.159'
firstport = 12345
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# clientSock.bind((host, firstport))

class ClientState(Enum):
    """ClientState(Enum) contient tous les états dans lesquels le client de jeu peut se trouver"""
    LOCAL = 1 # création de la map, envoi des donné au joueur

    ONLINE = 2 # attente que le MAX_PLAYER sois atteint

    MENU = 3 # creation d'une instance de serveur

    STARTING = 4 # création de la map, envoi des donné au joueur

    SORCIERE = 4 # attente que le MAX_PLAYER sois atteint

    STATS = 5 # boucle de jeu principal

    QUIT = 6 # fin du serveur envoi des donné à la bd pour les stat

class PartieState(Enum):
    """PartieState(Enum) contient tous les états dans lesquels la partie et le jeu peuvent se trouver"""
    INDEX = 1 # creation d'une instance de serveur

    GLOBALS_STATS = 4 # boucle de jeu principal

    HELPER = 5 # fin du serveur envoi des donné à la bd pour les stats

    NB_PLAYER = 6 

    NB_IA = 7
    
class END_MENU(Enum):
    SORCIERE=0
    SORCIERE_DRAGON=1
    SORCIERE_SYMBOLE=2
    SORCIERE_POTION=3

class END_MENU(Enum):
    SORCIERE=0
    SORCIERE_DRAGON=1
    SORCIERE_SYMBOLE=2
    SORCIERE_POTION=3

class Client():

# --------- Initialisation du client --------- #
    def __init__(self) -> None:
        self.__sorciere_parti_2:bool = False
        self.__sorciere:END_MENU = END_MENU.SORCIERE
        self.__clock:pygame.time.Clock =  pygame.time.Clock()
        self.__fenetre = pygame.display.set_mode((800, 700))
        self.__etatPartie:PartieState = PartieState.INDEX
        self.__etatClient:ClientState = ClientState.MENU
        self.__dialogues:str = ""
        self.__interface:interface.Interface = None
        self.__game:game.Game = None
        self.__sorciere:END_MENU = END_MENU.SORCIERE
        self.__joueurLocal:list[int] = []
        self.currentIdDe:int = 0
        self.currentImageDe:image.De = None
        self.__timerAnimation = {}

# --------- Getter et Setter du client --------- #
    
    def resetMenu(self):
        self.__etatPartie:PartieState = PartieState.INDEX
        self.__etatClient:ClientState = ClientState.MENU
        self.__dialogues:str = ""
        self.__interface:interface.Interface = None
        self.__game:game.Game = None
        self.__sorciere:END_MENU = END_MENU.SORCIERE
        self.__joueurLocal:list[int] = []
        self.currentIdDe:int = 0
        self.currentImageDe:image.De = None
        self.__timerAnimation = {}

    def resetMenu(self):
        self.__etatPartie:PartieState = PartieState.INDEX
        self.__etatClient:ClientState = ClientState.MENU
        self.__dialogues:str = ""
        self.__interface:interface.Interface = None
        self.__game:game.Game = None
        self.__sorciere:END_MENU = END_MENU.SORCIERE
        self.__joueurLocal:list[int] = []
        self.currentIdDe:int = 0
        self.currentImageDe:image.De = None
        self.__timerAnimation = {}
        
        
        
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
    
    def MenuBas(self, un_joueur):
        """Affichage de la partie basse du jeu en focntion du joueur qui joue"""
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
        
    def affichePlateau(self):
        """Met à jour le plateau en affichant les cases découvertes."""
        font = pygame.font.Font(('./assets/font/Dosis-VariableFont_wght.ttf'), 11)
        for i in self.getGame().getPlateau().getCasesDecouvertes():
            couleur_case = self.getGame().getPlateau().getCases(i[0],i[1]).value # Obtenir la couleur de la case
            x = i[1] * self.getGame().getPlateau().getTailleCase()  # Coordonnée X du coin supérieur gauche du rectangle
            y = i[0] * self.getGame().getPlateau().getTailleCase()  # Coordonnée Y du coin supérieur gauche du rectangle          
            rectangle = pygame.Rect(x, y, self.getGame().getPlateau().getTailleCase(), self.getGame().getPlateau().getTailleCase())  # Créer un rectangle
            pygame.draw.rect(self.getFenetre(), couleur_case.value, rectangle)  # Dessiner le rectangle avec la couleur
            if (self.getGame().getPlateau().getCases(i[0],i[1]).name != 'MORT' and self.getGame().getPlateau().getCases(i[0],i[1]).name != 'DEPART' and self.getGame().getPlateau().getCases(i[0],i[1]).name != 'VIDE'):
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
            La fonction afficheCle permet d'afficher les cle dans le menu(int x, int y, Surface surface, Font font)
        """
        for i in joueur.getInventaire():
            if i == "cle de la Ville" :
                image.Image(660,640,image.Cle.TOWN.value).afficheImageRedimensionnee(48,30,self.getFenetre())
            elif i == "cle de la Riviere" :
                image.Image(660,595,image.Cle.WATER.value).afficheImageRedimensionnee(48,30,self.getFenetre())
            elif i == "cle de la Foret" :
                image.Image(725,595,image.Cle.GRASS.value).afficheImageRedimensionnee(48,30,self.getFenetre())
            elif i == "cle du Rocher" :
                image.Image(725,640,image.Cle.ROCK.value).afficheImageRedimensionnee(48,30,self.getFenetre())
        pygame.draw.line(self.getFenetre(), logique.Couleur.NOIR.value, (660, 632), (770, 632), 2)
        pygame.draw.line(self.getFenetre(), logique.Couleur.NOIR.value, (715, 595), (715, 670), 2)

    # Definir l'affichage sur le menu
    def afficheImage(self,x,y,joueur):
        """La fonction afficheImage permet d'afficher le personnage dans le menu(int x, int y, Surface surface, Font font)"""        
        # Afficher l'image sur la fenetre
        self.getFenetre().blit(joueur.getImage(), (x, y))
        # Dessiner le rectangle pour les pv du joueur
        rectangle.Rectangle(500,590,130,35,logique.Couleur.VERT.value).affiche(self.getFenetre())
    
        # Charger les pv
        texte.Texte(joueur.getPv(),logique.Couleur.NOIR.value,538,598).affiche(self.getFenetre())
        
    # Definir l'affichage de l'adversaire lors des combats
    def afficheImageAdv(self,x,y,joueur):
        """La fonction afficheImageAdv affiche l'image de l'ennemi dans le menu."""
        self.getFenetre().blit(joueur.getImage(), (x, y))
        rectangle.Rectangle(500, 635, 130, 35, logique.Couleur.ROUGE.value).affiche(self.getFenetre())
        texte.Texte(joueur.getPv(), logique.Couleur.NOIR.value, 538, 645).affiche(self.getFenetre())
    
    def afficheImagePlateau(self, joueur):
        """La fonction afficheImagePlateau permet d'afficher le personnage dans le plateau(int x, int y, Surface surface)"""
        image_redimensionnee = pygame.transform.scale(joueur.getImage(), (47, 47))
        self.getFenetre().blit(image_redimensionnee, (joueur.getY(), joueur.getX()))
                

    # Definir l'affichage des joueurs sur le plateau
    def afficheJoueurs(self):
        """Affiche tous les joueurs sur le plateau."""
        if len(self.getGame().getListeJoueur()) != 0 and self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()] != None:
            for i in self.getGame().getListeJoueur():
                if i != None:
                    self.afficheImagePlateau(i)

    def affichePotion(self):
        """La fonction affichePotion permet d'afficher la potion dans l'inventaire du joueur"""
        potion = image.Sorciere.POTION.value
        self.getFenetre().blit(potion, (668, 593))
          
    def afficheAnimationDe(self):
        """La fonction afficheAnimationDe permet d'afficher les différentes face du dé lors du jet de dés"""
        listeDe = [image.De.FACE2.value, image.De.FACE1.value, image.De.FACE4.value, image.De.FACE6.value, image.De.FACE5.value, image.De.FACE3.value]
        if 'de' not in self.__timerAnimation.keys():
            self.__timerAnimation['de'] = time.time()
        if self.currentIdDe >= len(listeDe):
            self.__timerAnimation['de'] = time.time()
            self.currentIdDe = 0
            self.afficheResultatDe()
        else:
            self.getFenetre().blit(listeDe[self.currentIdDe],(350,475))
        animationDelay = 0.23 - int(0.19*(self.currentIdDe/len(listeDe)))
        if self.__timerAnimation['de'] + animationDelay < time.time() :
                self.currentIdDe += 1
                self.__timerAnimation['de'] = time.time()

    def afficheResultatDe(self):
        """La fonction afficheResultatDe renvoie l'image correspondant au résultat du lancer au joueur"""
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

# --------- Boucle principale du jeu qui fait l'affichage et la logique --------- #

    # Permets de switcher entre les affichage des pages
    def affichePartie(self):
        """La fonction affichePartie permet d'afficher les différentes pages du jeu et des menus"""
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
                        self.draw_stats()
                    
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
            case ClientState.LOCAL | ClientState.ONLINE:
                match self.getGame().getEtat():

                    # Page_ChoixPerso
                    case game.GameState.SELECT_AVATAR:
                        image.Image(0, 0, image.Page.CHOIX_PERSO.value).afficheImageRedimensionnee(800, 700,self.getFenetre())
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
                        self.affichePlateau()
                        self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.setDialogues(["Tu es le joueur " + str(self.getGame().getIdJoueurActuel() + 1) + ", clique sur le de afin de faire ton","déplacement : haut, bas, gauche ou droite"])
                        self.afficheDialogues()
                        image.Image(350,475,image.De.FACE1.value).affiche(self.getFenetre())
                    
                    case game.GameState.ATTACK:
                        pass

                    case game.GameState.COMBAT_JOUEUR1:
                        joueur_adv = self.getGame().getJoueurAdv()
                        self.getFenetre().blit(pygame.transform.scale(image.Page.ARENE.value, (800, 500)),(0, 0))
                        self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.afficheImage(100,400,self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.afficheImageAdv(620,400,joueur_adv)
                        self.setDialogues(["Tu as décidé de combattre un joueur. Le celebre ","{}. Prepare toi à le combattre afin de prendre".format(joueur_adv.getPrenom()), "l'avantage sur lui !"])
                        self.afficheDialogues()

                    # Page_Mouvement
                    case game.GameState.SELECT_ACTION:
                        player = self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()]
                        image.Image(0,468, image.Page.CHOIX_DOUBLE.value).affiche(self.getFenetre())
                        self.affichePlateau()
                        self.MenuBas(player)
                        self.setDialogues(["Joueur " + str(player.getId() + 1) + " : " + player.getPrenom() + " clique sur le de afin d'attaquer","un joueur ou de lancer le dé"])
                        self.afficheDialogues()
                        # Affiche le de sur la face 1
                        image.Image(220,480,image.Interaction.ATTAQUER.value).affiche(self.getFenetre())
                        image.Image(510, 480,image.Interaction.DE.value).affiche(self.getFenetre())
                        texte.Texte("Attaquer",logique.Couleur.BLANC.value,227,545).affiche(self.getFenetre())
                        texte.Texte("De",logique.Couleur.BLANC.value,532,545).affiche(self.getFenetre())

                    # Page_LancementDe
                    case game.GameState.LANCEMENT_DE:
                        image.Image(0,468,image.Page.BAS_PLATEAU.value).affiche(self.getFenetre())
                        self.affichePlateau()
                        self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.afficheAnimationDe()

                    # Page_Direction
                    case game.GameState.MOVE_PLAYER:
                        image.Image(0,468,image.Page.BAS_PLATEAU.value).affiche(self.getFenetre())
                        self.affichePlateau()
                        self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        temp_texte=("Bravo ! Tu peux avancer de {} cases ! Où ".format(self.getGame().getDeValue()))
                        self.setDialogues([temp_texte, "veux-tu aller ? (haut, bas, gauche, droite)"])
                        self.afficheDialogues()
                        listeDe = [image.De.FACE1.value, image.De.FACE2.value, image.De.FACE3.value, image.De.FACE4.value, image.De.FACE5.value, image.De.FACE6.value]
                        image.Image(350,475,listeDe[self.__game.getlastdeVal()-1]).affiche(self.getFenetre())

                    # Page_Action
                    case game.GameState.STAY_ON_CASE:
                        couleur_case = self.getGame().getPlateau().getCases(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()].getPlateaux(),self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()].getPlateauy()).value.value
                        if couleur_case == logique.Couleur.BEIGE.value:
                            image.Image(0,468,image.Page.CHOIX_DOUBLE.value).affiche(self.getFenetre())
                            self.affichePlateau()
                            self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                            self.setDialogues(["Tu es devant la Hutte de la sorciere.","Veux-tu essayer de l'ouvrir à l'aide","des cles des quatre boss ?"])
                            self.afficheDialogues()
                            self.getFenetre().blit(image.Interaction.CLES.value, (220, 480))
                            self.getFenetre().blit(image.Interaction.RETOUR.value, (510,480))
                            texte.Texte("Ouvrir la porte",logique.Couleur.BLANC.value,212,545).affiche(self.getFenetre())
                            texte.Texte("Passer son chemin",logique.Couleur.BLANC.value,485,545).affiche(self.getFenetre())
                            
                        elif couleur_case == logique.Couleur.BLANC.value:
                            image.Image(0,468,image.Page.BAS_PLATEAU.value).affiche(self.getFenetre())
                            self.affichePlateau()
                            self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                            self.setDialogues(["Tu es dans une case Vide.", "Il ne t'arrivera rien tu peux etre rassure."])
                            self.afficheDialogues()
                            
                        elif couleur_case == logique.Couleur.BLEU.value:
                            image.Image(0,468,image.Page.CHOIX_DOUBLE.value).affiche(self.getFenetre())
                            self.affichePlateau()
                            self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                            self.setDialogues(["Tu es tombe dans la case Puit... Pour t'en","sortir, tu dois sacrifier une de tes cles","ou 200 pv."])        
                            self.afficheDialogues()
                            self.getFenetre().blit(image.Interaction.PV.value, (220, 480))
                            self.getFenetre().blit(image.Interaction.CLES.value, (510, 480))
                            texte.Texte("200 PV",logique.Couleur.BLANC.value,235,545).affiche(self.getFenetre())
                            texte.Texte("1 clee",logique.Couleur.BLANC.value,525,545).affiche(self.getFenetre())

                        elif couleur_case == logique.Couleur.GRIS.value:
                            image.Image(0,468,image.Page.CHOIX_DOUBLE.value).affiche(self.getFenetre())
                            self.affichePlateau()
                            self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                            self.setDialogues(["Tu es sur une case Speciale ! Si tu tente","ta chance, tu as une chance sur deux gagner", "deux cles que tu n'as pas ou de tout perdre."])
                            self.afficheDialogues()
                            self.getFenetre().blit(image.Interaction.CLES.value, (220, 480))
                            self.getFenetre().blit(image.Interaction.RETOUR.value, (510,480))
                            texte.Texte("1 clee",logique.Couleur.BLANC.value,215,545).affiche(self.getFenetre())
                            texte.Texte("Passer son tour",logique.Couleur.BLANC.value,505,545).affiche(self.getFenetre())

                        elif couleur_case == logique.Couleur.INDIGO.value:
                            image.Image(0,468,image.Page.CHOIX_DOUBLE.value).affiche(self.getFenetre())
                            self.affichePlateau()
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
                            self.affichePlateau()
                            self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                            self.setDialogues(["Tu es la case de Depart, dépêche toi de","récupérer les clés avant les autres joueurs","afin de gagner le jeu"])
                            self.afficheDialogues()
                            
                        elif couleur_case == logique.Couleur.NOIR.value:
                            image.Image(0,468,image.Page.BAS_PLATEAU.value).affiche(self.getFenetre())
                            self.affichePlateau()
                            self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                            self.setDialogues(["Tu n'as pas de chance...", "Tu es tombe sur la case de Mort...", "La partie est finie pour toi."])
                            self.afficheDialogues()

                        elif couleur_case == logique.Couleur.ORANGE.value:
                            image.Image(0,468,image.Page.BAS_PLATEAU.value).affiche(self.getFenetre())
                            self.affichePlateau()
                            self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                            self.setDialogues(["Tu es sur une case Malus, clique sur le symbole chance", "afin de savoir quel sort le jeu te réserve."])
                            self.afficheDialogues()
                            self.getFenetre().blit(image.Interaction.MALUS.value, (360,475))
                            texte.Texte("Malus",logique.Couleur.NOIR.value,372,545).affiche(self.getFenetre())
        
                        elif couleur_case == logique.Couleur.ROSE.value:
                            image.Image(0,468,image.Page.BAS_PLATEAU.value).affiche(self.getFenetre())
                            self.affichePlateau()
                            self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                            self.setDialogues(["Tu es sur une case Chance, clique sur le symbole chance", "afin de savoir quel sort le jeu te réserve."])
                            self.afficheDialogues()
                            self.getFenetre().blit(image.Interaction.CHANCE.value, (360,475))
                            texte.Texte("Chance",logique.Couleur.NOIR.value,369,545).affiche(self.getFenetre())

                        elif couleur_case == logique.Couleur.ROUGE.value:
                            pass

                        elif couleur_case == logique.Couleur.TURQUOISE.value:
                            image.Image(0,468,image.Page.BAS_PLATEAU.value).affiche(self.getFenetre())
                            self.affichePlateau()
                            self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                            self.setDialogues(["Tu es sur une case Grrr", "Un tremblement de terre surgit de nul part", "et teleporte tous les joueurs !!!"])
                            self.afficheDialogues()

                        elif couleur_case == logique.Couleur.VIOLET.value:
                            image.Image(0,468,image.Page.BAS_PLATEAU.value).affiche(self.getFenetre())
                            self.affichePlateau()
                            self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                            self.setDialogues(["Tu es sur une case Rejoue ! Tu as la","chance de pouvoir relancer le dé pour avoir une","deuxième chance"])
                            self.afficheDialogues()
                            self.getFenetre().blit(image.De.FACE1.value,(350,475))
                    
                    case game.GameState.CASE_CHANCE:
                        image.Image(0,468,image.Page.BAS_PLATEAU.value).affiche(self.getFenetre())
                        self.affichePlateau()
                        self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.setDialogues(["Tou-dou-dou-doum","Tu vas gagner {} pvs, utilise les à bon escient".format(self.getGame().getChanceAction()),"afin de t'en sortir vainqueur"])
                        self.afficheDialogues()

                    case game.GameState.CASE_MALUS:
                        image.Image(0,468,image.Page.BAS_PLATEAU.value).affiche(self.getFenetre())
                        self.affichePlateau()
                        self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.setDialogues(["Tou-dou-dou-doum","Tu vas perdre {} pvs, fais attention où tu mets les pieds".format(self.getGame().getMalusAction()),"la prochaine fois"])
                        self.afficheDialogues()
                    
                    case game.GameState.CASE_RETOUR:
                        image.Image(0,468,image.Page.BAS_PLATEAU.value).affiche(self.getFenetre())
                        self.affichePlateau()
                        self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.setDialogues(["Dommage, retente ta chance une prochaine fois","et dépêche toi de récupérer les clés avant", "les autres joueurs !!!"])
                        self.afficheDialogues()
                    
                    case game.GameState.CASE_TELEPORTE:
                        image.Image(0,468,image.Page.BAS_PLATEAU.value).affiche(self.getFenetre())
                        self.affichePlateau()
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

                    case game.GameState.CASE_BOSS_TERMINE:
                        self.getFenetre().blit(pygame.transform.scale(image.Page.ARENE.value, (800, 500)),(0, 0))
                        self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.afficheImage(100,400,self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.setDialogues(["Tu as déja combatu tous les boss, déplace-toi ","jusqu'à la hutte de la sorciere pour la tuer", "et sortir vainqueur de cette partie !"])
                        self.afficheDialogues()

                    case game.GameState.FIGHT1:
                        boss = self.getGame().getBossActuel()
                        self.getFenetre().blit(pygame.transform.scale(image.Page.ARENE.value, (800, 500)),(0, 0))
                        self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.afficheImage(100,400,self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.afficheImageAdv(620,400,boss)
                        self.setDialogues(["Tu as décidé de combattre un joueur. Le celebre ","{}. Prepare toi à le combattre afin de prendre".format(boss.getPrenom()), "l'avantage sur lui !"])
                        self.afficheDialogues()

                    case game.GameState.FIGHT2:
                        boss = self.getGame().getBossActuel()
                        self.getFenetre().blit(pygame.transform.scale(image.Page.ARENE.value, (800, 500)),(0, 0))
                        self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.afficheImage(100,400,self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.afficheImageAdv(620,400,boss)
                        self.setDialogues(["Que veux-tu faire ? Une attaque basique, une ","attaque speciale, te defendre ou prendre", "la fuite ?"])
                        self.afficheDialogues()
                        image.Image(100, 508, image.BtnAttaque.BASIQUE.value).affiche(self.getFenetre())
                        image.Image(250, 508, image.BtnAttaque.SPECIALE.value).affiche(self.getFenetre())
                        image.Image(400, 508, image.BtnAttaque.DEFENSE.value).affiche(self.getFenetre())
                        image.Image(550, 508, image.BtnAttaque.FUITE.value).affiche(self.getFenetre())
                        
                    case game.GameState.FIGHT3:
                        boss = self.getGame().getBossActuel()
                        self.getFenetre().blit(pygame.transform.scale(image.Page.ARENE.value, (800, 500)),(0, 0))
                        self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.afficheImage(100,400,self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.afficheImageAdv(620,400,boss)
                        self.setDialogues(["Tu as choisi de faire une attaque basique,","tu as touché l'adversaire, il a perdu {} pvs".format(self.getGame().getPvInflige())])
                        self.afficheDialogues()
                    
                    case game.GameState.FIGHT4:
                        boss = self.getGame().getBossActuel()
                        self.getFenetre().blit(pygame.transform.scale(image.Page.ARENE.value, (800, 500)),(0, 0))
                        self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.afficheImage(100,400,self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.afficheImageAdv(620,400,boss)
                        self.setDialogues(["Tu as choisi de faire une attaque speciale,","tu as touché l'adversaire, il a perdu {} pvs".format(self.getGame().getPvInflige())])
                        self.afficheDialogues()
                    
                    case game.GameState.FIGHT5:
                        boss = self.getGame().getBossActuel()
                        self.getFenetre().blit(pygame.transform.scale(image.Page.ARENE.value, (800, 500)),(0, 0))
                        self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.afficheImage(100,400,self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.afficheImageAdv(620,400,boss)
                        self.setDialogues(["Tu as choisi de te defendre, tu fais une","grimace au boss et cela reduit les degâts","qu'il peut t'infliger."])
                        self.afficheDialogues()
                    
                    case game.GameState.FIGHT6:
                        boss = self.getGame().getBossActuel()
                        self.getFenetre().blit(pygame.transform.scale(image.Page.ARENE.value, (800, 500)),(0, 0))
                        self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.afficheImage(100,400,self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.afficheImageAdv(620,400,boss)
                        self.setDialogues(["Tu as choisi de prendre la fuite,","retente ta chance une prochaine fois."])
                        self.afficheDialogues()
                    
                    case game.GameState.FIGHT7:
                        boss = self.getGame().getBossActuel()
                        self.getFenetre().blit(pygame.transform.scale(image.Page.ARENE.value, (800, 500)),(0, 0))
                        self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.afficheImage(100,400,self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.afficheImageAdv(620,400,boss)
                        self.setDialogues(["L'ennemis a esquivé le coup,","c'est au tour du boss de joueur"])
                        self.afficheDialogues()
                    
                    case game.GameState.FIGHT8:
                        boss = self.getGame().getBossActuel()
                        self.getFenetre().blit(pygame.transform.scale(image.Page.ARENE.value, (800, 500)),(0, 0))
                        self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.afficheImage(100,400,boss)
                        self.afficheImageAdv(620,400,self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.setDialogues(["C'est au tour du boss d'attaquer","Le boss reflechit...","Il te fait perdre {} pvs".format(self.getGame().getPvInflige())])
                        self.afficheDialogues()
                    
                    case game.GameState.FIGHT9:
                        boss = self.getGame().getBossActuel()
                        self.getFenetre().blit(pygame.transform.scale(image.Page.ARENE.value, (800, 500)),(0, 0))
                        self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.afficheImage(100,400,boss)
                        self.afficheImageAdv(620,400,self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.setDialogues(["C'est au tour du boss d'attaquer","Le boss reflechit...","L'adversaire a raté son coup"])
                        self.afficheDialogues()
                    
                    case game.GameState.FIGHT10:
                        boss = self.getGame().getBossActuel()
                        self.getFenetre().blit(pygame.transform.scale(image.Page.ARENE.value, (800, 500)),(0, 0))
                        self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.afficheImageAdv(620,400,boss)
                        self.setDialogues(["Fin du combat... Tu n'as pas survecu","à l'attaque du boss...", "Retour au plateau !"])
                        self.afficheDialogues()
                    
                    case game.GameState.FIGHT11:
                        boss = self.getGame().getBossActuel()
                        self.getFenetre().blit(pygame.transform.scale(image.Page.ARENE.value, (800, 500)),(0, 0))
                        self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.afficheImage(620,400,self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.setDialogues(["Fin du combat... Tu as battu le boss", "recupere les autres cles en tuant les","autres boss et detruit cette sorciere !!!"])
                        self.afficheDialogues()
                    
                    case game.GameState.FIGHT12:
                        self.getFenetre().blit(pygame.transform.scale(image.Page.ARENE.value, (800, 500)),(0, 0))
                        self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.afficheImage(620,400,self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                        self.setDialogues(["Fin du combat... Tu as battu le boss", "en plus de ça tu as toutes les cles, depeche ","toi pour etre le premier à tuer la sorciere !!!"])
                        self.afficheDialogues()

                    case game.GameState.CASE_FIN_DU_JEU:
                            image.Image(0,468,image.Page.BAS_PLATEAU.value).affiche(self.getFenetre())
                            self.affichePlateau()
                            self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                            if(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()].avoirCles()):
                                self.setDialogues(["Bravo tu as trouve toutes les cles","Ouvre la porte et apprete toi à", "affronter la sorciere."])
                            else:
                                self.setDialogues(["Tu n'as pas encore recuperer toutes","et dépêche toi de récupérer les clés avant", "Tu n'as pas encore recuperer toutes","la sorciere. Depeche-toi !"])
                            self.afficheDialogues()
                    case game.GameState.SWITCH_PLAYER:
                        pass
            
            case ClientState.STATS:
                self.afficheStats()
            case ClientState.SORCIERE:
                self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()].setInventaire([])
                self.afficheSorciere()
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
                        self.__game = game.Game(4,0)
                        
                        clientSock.sendto(pickle.dumps("hello"), (host, firstport))
                        self.setEtatClient(ClientState.ONLINE)
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
                    if 500 <= mouse_x <= 600 and 582 <= mouse_y <= 652:
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
                        self.setEtatPartie(PartieState.NB_PLAYER)
                    # Si le personnage sur lequel on clique est J1
                    if (400 <= mouse_x <= 500 and 582 <= mouse_y <= 652) and 0 in selectable_nb_ia:   
                        self.getInterface().setNombreIA(0)
                        self.setGame(self.getInterface().genererPartie())
                        self.setJoueurLocal([i for i in range(len(self.getGame().getListeJoueur()))])
                        self.setEtatClient(ClientState.ONLINE if self.getInterface().getEnLigne() else ClientState.LOCAL)
                    # Si le personnage sur lequel on clique est J2   
                    if (500 <= mouse_x <= 600 and 582 <= mouse_y <= 652) and 1 in selectable_nb_ia:
                        self.getInterface().setNombreIA(1)
                        self.setGame(self.getInterface().genererPartie())
                        self.setJoueurLocal([i for i in range(len(self.getGame().getListeJoueur()))])
                        self.setEtatClient(ClientState.ONLINE if self.getInterface().getEnLigne() else ClientState.LOCAL)
                    # Si le personnage sur lequel on clique est J3
                    if (600 <= mouse_x <= 700 and 582 <= mouse_y <= 652) and 2 in selectable_nb_ia:   
                        self.getInterface().setNombreIA(2)
                        self.setGame(self.getInterface().genererPartie())
                        self.setJoueurLocal([i for i in range(len(self.getGame().getListeJoueur()))])
                        self.setEtatClient(ClientState.ONLINE if self.getInterface().getEnLigne() else ClientState.LOCAL)
                    # Si le personnage sur lequel on clique est J4
                    if (700 <= mouse_x <= 800 and 582 <= mouse_y <= 652) and 3 in selectable_nb_ia:   
                        self.getInterface().setNombreIA(3)
                        self.setGame(self.getInterface().genererPartie())
                        self.setJoueurLocal([i for i in range(len(self.getGame().getListeJoueur()))])
                        self.setEtatClient(ClientState.ONLINE if self.getInterface().getEnLigne() else ClientState.LOCAL)
    
    def sorciere_logique(self, input:inputs):
        match self.__sorciere:
            case END_MENU.SORCIERE:
                if input.estClique():
                    if 500 < input.getSourisx() < 725 and 150 < input.getSourisy() < 450:
                        self.__sorciere = END_MENU.SORCIERE_SYMBOLE                        
                    if 90 < input.getSourisx() < 190 and 180 < input.getSourisy() < 350:
                        self.__sorciere = END_MENU.SORCIERE_DRAGON                        
                    if 330 < input.getSourisx() < 430 and 480 < input.getSourisy() < 580:
                        self.__sorciere = END_MENU.SORCIERE_POTION                        
            case END_MENU.SORCIERE_DRAGON:
                animationDelay = 2.5
                if 'sorciere' not in self.__timerAnimation.keys() or self.__timerAnimation['sorciere'] == 0:
                    self.__timerAnimation['sorciere'] = time.time()
                if self.__timerAnimation['sorciere'] + animationDelay < time.time() :
                        self.__timerAnimation['sorciere'] = 0
                        if self.__sorciere_parti_2:
                            self.__sorciere_parti_2 = False
                            self.__sorciere = END_MENU.SORCIERE
                        else:
                            self.__sorciere_parti_2 = True
            case END_MENU.SORCIERE_SYMBOLE:
                animationDelay = 2.5
                if 'sorciere' not in self.__timerAnimation.keys() or self.__timerAnimation['sorciere'] == 0:
                    self.__timerAnimation['sorciere'] = time.time()
                if self.__timerAnimation['sorciere'] + animationDelay < time.time() :
                        self.__timerAnimation['sorciere'] = 0
                        if self.__sorciere_parti_2:
                            self.__sorciere_parti_2 = False
                            self.__sorciere = END_MENU.SORCIERE
                        else:
                            self.__sorciere_parti_2 = True
            case END_MENU.SORCIERE_POTION:
                animationDelay = 4
                if 'sorciere' not in self.__timerAnimation.keys() or self.__timerAnimation['sorciere'] == 0:
                    self.__timerAnimation['sorciere'] = time.time()
                if self.__timerAnimation['sorciere'] + animationDelay < time.time() :
                        self.__timerAnimation['sorciere'] = 0
                        if self.__sorciere_parti_2:
                            self.__sorciere_parti_2 = False
                            self.__etatClient = ClientState.STATS
                            self.setEtatPartie(PartieState.INDEX)
                            self.__sorciere = END_MENU.SORCIERE                            
                        else:
                            self.__sorciere_parti_2 = True

    def afficheSorciere(self):
        match self.__sorciere:
            case END_MENU.SORCIERE:
                image.Image(0,0,image.Sorciere.MAISON.value).afficheImageRedimensionnee(800, 700,self.getFenetre())
                self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                self.setDialogues(["Tu es chez la sorciere, mais j'ai l'impression","qu'elle est sortie de sa taniere...","profite-en pour fouiller dans ses affaires :)"])
            case END_MENU.SORCIERE_DRAGON:
                image.Image(0,0,image.Sorciere.MAISON_DRAGON.value).afficheImageRedimensionnee(800, 700,self.getFenetre())
                self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                if not self.__sorciere_parti_2:
                    self.setDialogues(["Un dragon de pierre... ce n'est pas très","rassurant, trouvons vite un remède et sortons","d'ici très vite"])
                else:
                    self.setDialogues(["Tu es chez la sorciere, mais on dirait","qu'elle est sortie de sa taniere...","profite-en pour fouiller dans ses affaires :)"])
            case END_MENU.SORCIERE_SYMBOLE:
                image.Image(0,0,image.Sorciere.MAISON_SYMBOLE.value).afficheImageRedimensionnee(800, 700,self.getFenetre())
                self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                if not self.__sorciere_parti_2:
                    self.setDialogues(["C'est un symbole astral, si c'est chez la","sorciere, il vaut mieux ne pas y toucher"])
                else:
                    self.setDialogues(["Tu es chez la sorciere, mais on dirait","qu'elle est sortie de sa taniere...","profite-en pour fouiller dans ses affaires :)"])
            case END_MENU.SORCIERE_POTION:
                if not self.__sorciere_parti_2:
                    image.Image(0,0,image.Sorciere.MAISON.value).afficheImageRedimensionnee(800, 700,self.getFenetre())
                    self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()].setInventaire(["Potion inverstium"])
                    self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                    self.affichePotion()
                    self.setDialogues(["Tu as trouvé une potion... Potion inverstium","Tu décides de la boire afin d'inverser le","sortilège"])
                else:
                    image.Image(0,0,image.Page.FIN_JEU.value).afficheImageRedimensionnee(800, 700,self.getFenetre())
                    self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
                    self.setDialogues(["Tu as terminé le jeu bravo à toi jeune aventurier","Tu es le premier a t'être libéré du sort !!"])
        self.afficheDialogues()
            
        pygame.display.update()
            
    def afficheStats(self):
        image.Image(0,0,image.Page.STATS.value).afficheImageRedimensionnee(800, 700,self.getFenetre())
    def stats_logique(self, input:inputs):
        if (input.estClique()):
            self.resetMenu()

    # Boucle du jeu lorsque le jeu est démarrer qui permet de gérer les événements
    def main(self):
        self.setEtatPartie(PartieState.INDEX)
        while (self.getEtatClient() != ClientState.QUIT):
            self.affichePartie()
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
                    if self.getGame().isEnd():
                        self.setEtatClient(ClientState.SORCIERE)
                        self.__sorciere = END_MENU.SORCIERE
                    else:
                        self.getGame().loop(inputs(mouse_x, mouse_y, click, dir))
                case ClientState.ONLINE:
                    # envoyé les inputs au server
                    try:
                        data, serveur = clientSock.recvfrom(20480)
                        resp  = 'OK'
                        data = pickle.loads(data)
                        if(type(data) == game.Game):
                            self.setGame(data)
                            
                        elif isinstance(data, dict):
                            if( 'end' in data.keys()):
                                if data['end']:
                                    self.setEtatClient(ClientState.SORCIERE)
                                    self.__sorciere = END_MENU.SORCIERE
                                else:
                                    self.setEtatClient(ClientState.STATS)
                            elif( 'input' in data.keys()):
                                clientSock.sendto(pickle.dumps(inputs(mouse_x, mouse_y, click, dir)), (host, firstport))
                    except TimeoutError:
                        pass
                case ClientState.SORCIERE:
                    self.sorciere_logique(inputs(mouse_x, mouse_y, click, dir))
                case ClientState.STATS:
                    self.stats_logique(inputs(mouse_x, mouse_y, click, dir))
                case ClientState.QUIT:
                    pass

    def sorciere_logique(self, input:inputs):
        match self.__sorciere:
            case END_MENU.SORCIERE:
                if input.estClique():
                    if 500 < input.getSourisx() < 725 and 150 < input.getSourisy() < 450:
                        self.__sorciere = END_MENU.SORCIERE_SYMBOLE                        
                    if 90 < input.getSourisx() < 190 and 180 < input.getSourisy() < 350:
                        self.__sorciere = END_MENU.SORCIERE_DRAGON                        
                    if 330 < input.getSourisx() < 430 and 480 < input.getSourisy() < 580:
                        self.__sorciere = END_MENU.SORCIERE_POTION                        
            case END_MENU.SORCIERE_DRAGON:
                animationDelay = 2.5
                if 'sorciere' not in self.__timerAnimation.keys() or self.__timerAnimation['sorciere'] == 0:
                    self.__timerAnimation['sorciere'] = time.time()
                if self.__timerAnimation['sorciere'] + animationDelay < time.time() :
                        self.__timerAnimation['sorciere'] = 0
                        if self.__sorciere_parti_2:
                            self.__sorciere_parti_2 = False
                            self.__sorciere = END_MENU.SORCIERE
                        else:
                            self.__sorciere_parti_2 = True
            case END_MENU.SORCIERE_SYMBOLE:
                animationDelay = 2.5
                if 'sorciere' not in self.__timerAnimation.keys() or self.__timerAnimation['sorciere'] == 0:
                    self.__timerAnimation['sorciere'] = time.time()
                if self.__timerAnimation['sorciere'] + animationDelay < time.time() :
                        self.__timerAnimation['sorciere'] = 0
                        if self.__sorciere_parti_2:
                            self.__sorciere_parti_2 = False
                            self.__sorciere = END_MENU.SORCIERE
                        else:
                            self.__sorciere_parti_2 = True
            case END_MENU.SORCIERE_POTION:
                animationDelay = 4
                if 'sorciere' not in self.__timerAnimation.keys() or self.__timerAnimation['sorciere'] == 0:
                    self.__timerAnimation['sorciere'] = time.time()
                if self.__timerAnimation['sorciere'] + animationDelay < time.time() :
                        self.__timerAnimation['sorciere'] = 0
                        if self.__sorciere_parti_2:
                            self.__sorciere_parti_2 = False
                            self.__etatClient = ClientState.STATS
                            self.setEtatPartie(PartieState.INDEX)
                            self.__sorciere = END_MENU.SORCIERE                            
                        else:
                            self.__sorciere_parti_2 = True

    def draw_sorciere(self):
        match self.__sorciere:
            case END_MENU.SORCIERE:
                image.Image(0,0,image.Sorciere.MAISON.value).affichageImageRedimensionnee(800, 700,self.getFenetre())
                self.setDialogues(["Tu es chez la sorciere, mais j'ai l'impression","qu'elle est sortie de sa taniere...","profite-en pour fouiller dans ses affaires :)"])
            case END_MENU.SORCIERE_DRAGON:
                image.Image(0,0,image.Sorciere.MAISON_DRAGON.value).affichageImageRedimensionnee(800, 700,self.getFenetre())
                if not self.__sorciere_parti_2:
                    self.setDialogues(["Un dragon de pierre... ce n'est pas très","rassurant, trouvons vite un remède et sortons","d'ici très vite"])
                else:
                    self.setDialogues(["Tu es chez la sorciere, mais on dirait","qu'elle est sortie de sa taniere...","profite-en pour fouiller dans ses affaires :)"])
            case END_MENU.SORCIERE_SYMBOLE:
                image.Image(0,0,image.Sorciere.MAISON_SYMBOLE.value).affichageImageRedimensionnee(800, 700,self.getFenetre())
                if not self.__sorciere_parti_2:
                    self.setDialogues(["C'est un symbole astral, si c'est chez la","sorciere, il vaut mieux ne pas y toucher"])
                else:
                    self.setDialogues(["Tu es chez la sorciere, mais on dirait","qu'elle est sortie de sa taniere...","profite-en pour fouiller dans ses affaires :)"])
            case END_MENU.SORCIERE_POTION:
                if not self.__sorciere_parti_2:
                    image.Image(0,0,image.Sorciere.MAISON.value).affichageImageRedimensionnee(800, 700,self.getFenetre())
                    self.setDialogues(["Tu as trouvé une potion... Potion inverstium","Tu décides de la boire afin d'inverser le","sortilège"])
                else:
                    image.Image(0,0,image.Page.FIN_JEU.value).affichageImageRedimensionnee(800, 700,self.getFenetre())
                    self.setDialogues(["Tu as terminé le jeu bravo à toi jeune aventurier","Tu es le premier a t'être libéré du sort !!"])
        self.MenuBas(self.getGame().getListeJoueur()[self.getGame().getIdJoueurActuel()])
        self.afficheDialogues()
            
        pygame.display.update()

    
    def calculer_moyennes(self, donnees):
        nombre_de_lignes = len(donnees)
        if nombre_de_lignes == 0:
            return []
        
        # Sommes initiales
        sommes = [0] * len(donnees[0])
        
        for ligne in donnees:
            for i, valeur in enumerate(ligne):
                sommes[i] += valeur
        
        # Calcul des moyennes
        moyennes = [somme / nombre_de_lignes for somme in sommes]
        return moyennes
            
    def draw_stats(self):
        image.Image(0,0,image.Page.STATS.value).afficheImageRedimensionnee(800, 700,self.getFenetre())
        donnees_bdd = recuperer_donnees_bdd()

        moyennes = self.calculer_moyennes(donnees_bdd)

        labels = [
            "Cases découvertes", 
            "Manches effectuées", "Morts", "Clés récupérées", 
            "Boss vaincus", "PV moyen"
        ]

        if len(moyennes) >= 6:
            # Affichage des statistiques par groupe de 3
            y1 = 170
            y2 = 200

            # Première moitié des statistiques
            for i in range(len(labels) // 2):
                label = labels[i]
                moyenne = moyennes[i]

                texte.Texte(f"{label}", logique.Couleur.BLANC.value, 200, y1).affiche(self.getFenetre())
                texte.Texte(f"{moyenne:.2f}", logique.Couleur.BLANC.value, 230, y2).affiche(self.getFenetre())

                y1 += 100
                y2 += 100

            # Seconde moitié des statistiques
            y1 = 170
            y2 = 200

            for i in range(len(labels) // 2, len(labels)):
                label = labels[i]
                moyenne = moyennes[i]

                texte.Texte(f"{label}", logique.Couleur.BLANC.value, 500, y1).affiche(self.getFenetre())
                texte.Texte(f"{moyenne:.2f}", logique.Couleur.BLANC.value, 530, y2).affiche(self.getFenetre())

                y1 += 100
                y2 += 100
        else:
            texte.Texte("Les statistiques ne sont pas disponibles pour le moment", logique.Couleur.BLANC.value, 240, 300).affiche(self.getFenetre())


        # Mettre à jour l'affichage
        pygame.display.update()
        
        # Faire un systeme pour la selection de la position du clic pour la selection du personnage
        stats = False
        # Boucle while pour voir quand le joueur clique sur start
        while (stats != True):
            mouse_x, mouse_y = pygame.mouse.get_pos() # Recuperer les coordonnees de la souris
            # Pour tous les evenements
            for event in pygame.event.get():
                # Si le joueur clique sur le bouton, on passe à la prochaine page "introduction"
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    if (40 <= mouse_x <= 100 and 40 <= mouse_y <= 100): # si appuie sur fleche retour
                        self.Page_demarrage(donnees_bdd)
                        stats = True
                # Si le joueur quitte la fenetre
                if (event.type == pygame.QUIT):
                    pygame.quit()
                    exit()


    def stats_logique(self, input:inputs):
        if (input.estClique()):
            self.resetMenu()
            
if __name__ == "__main__":
    Client().main()

