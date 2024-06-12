
from enum import Enum
import pygame, joueur
from interface import Interface
from game import Game, Game_State
from utils import image, texte, logique, rectangle
from input import inputs, direction
from utils.rectangle import Rectangle

class Client_State(Enum):


    LOCAL = 2 # création de la map, envoi des donné au joueur

    ONLINE = 3 # attente que le MAX_PLAYER sois atteint

    MENU = 1 # creation d'une instance de serveur

    STARTING = 2 # création de la map, envoi des donné au joueur

    WAIT_CONNECION = 3 # attente que le MAX_PLAYER sois atteint

    IN_GAME = 4 # boucle de jeu principal

    QUIT = 5 # fin du serveur envoi des donné à la bd pour les stat



class Menu_State(Enum):

    INDEX = 1 # creation d'une instance de serveur
    GLOBALS_STATS = 4 # boucle de jeu principal
    HELPER = 5 # fin du serveur envoi des donné à la bd pour les stat
    NB_PLAYER = 6
    NB_IA = 7

class Client():
    def __init__(self) -> None:
        self.__clock:pygame.time.Clock =  pygame.time.Clock()
        self.__screen = pygame.display.set_mode((800, 700))
        self.__stateMenu:Menu_State = None
        self.__stateClient:Client_State = None
        self.__dialogues = ""
        self.reset_out_of_game()

    def go_to_menu(self, menu_state:Menu_State):
        self.__stateMenu = menu_state
        print(self.__stateMenu)
        self.change_state(Client_State.MENU)

    def change_state(self, client_state:Client_State):
        self.__stateClient = client_state
        if self.__stateClient == Client_State.MENU and self.__stateMenu not in [Menu_State.NB_PLAYER, Menu_State.NB_IA]: self.reset_out_of_game()
        if client_state == Client_State.LOCAL :
            self.__game = self.__interface.generate_Game()
            self.__local_player =[i for i in range(len(self.__game.get_players()))]
        print(self.__stateClient)

    def reset_out_of_game(self):
        self.__interface = None
        self.__game = None
        self.__local_player:list[int] = []

    def set_dialogues(self, dialogues: list[str]):
        """Setter de la dialogues."""
        self.__dialogues = dialogues

    def draw_dialogues(self):
        """dessiner les dialogues."""
        Rectangle(100, 590, 390, 80, logique.Couleur.BEIGE.value).affiche(self.__screen)
        for idDialogue in range(len(self.__dialogues)):
            texte.Texte(self.__dialogues[idDialogue], logique.Couleur.NOIR.value, 110, 600 + (20 * idDialogue)).affiche(self.__screen)

    def draw_dialogues_deb(self):
        """dessiner les dialogues."""
        Rectangle(10, 580, 780, 100, logique.Couleur.GRIS.value).affiche(self.__screen)
        for idDialogue in range(len(self.__dialogues)):
            texte.Texte(self.__dialogues[idDialogue], logique.Couleur.NOIR.value, 30, 600 + (20 * idDialogue)).affiche(self.__screen)

    # 
    def draw(self):
        self.__screen.fill(logique.Couleur.NOIR.value)
        match self.__stateClient :

            case Client_State.LOCAL:
                match self.__game.get_state():
                    case Game_State.SELECT_AVARTAR:
                        image.Image(0, 0, image.Page.CHOIX_PERSO.value).affichage_image_redimensionnee(800, 700,self.__screen)
                        self.set_dialogues(["Bienvenue à toi jeune aventurier ! Amusez-vous bien",
                                            "ici demarre une nouvelle aventure ! Je t'invite à",
                                            "choisir un personnage parmi la liste suivante :"])
                        self.draw_dialogues_deb()
                        image.Image(400, 585, image.Personnages.ROCK.value).affiche(self.__screen)
                        texte.Texte(joueur.Nom.ROCK.value, logique.Couleur.NOIR.value, 413, 650).affiche(self.__screen)
                        image.Image(500, 585, image.Personnages.WATER.value).affiche(self.__screen)
                        texte.Texte(joueur.Nom.WATER.value, logique.Couleur.NOIR.value, 510, 650).affiche(self.__screen)
                        image.Image(600, 585, image.Personnages.TOWN.value).affiche(self.__screen)
                        texte.Texte(joueur.Nom.TOWN.value, logique.Couleur.NOIR.value, 613, 650).affiche(self.__screen)
                        image.Image(700, 585, image.Personnages.GRASS.value).affiche(self.__screen)
                        texte.Texte(joueur.Nom.GRASS.value, logique.Couleur.NOIR.value, 715, 650).affiche(self.__screen)
                        pass
                    case Game_State.SELECT_ACTION:
                        pass
                    case Game_State.USE_DIE:
                        image.Image(0,468,image.Page.BAS_PLATEAU.value).affiche(self.__screen)
                        self.Menu_bas(self.__game.get_current_player())
                        self.set_dialogues(["Tu es le joueur " + str(self.__game.get_current_player().get_id() + 1) + ", clique sur le de afin de faire","ton déplacement ↑ ↓ → ←"])
                        self.draw_dialogues()
                        # Affiche le de sur la face 1
                        image.Image(350,475,image.De.FACE1.value).affiche(self.__screen)
                    case Game_State.MOVE_PLAYER:
                        pass
                    case Game_State.STAY_ON_CASE:
                        pass
                    case Game_State.FIGHT:
                        pass
                    case Game_State.WAIT_FIGHT_ACTION:
                        pass
                    case Game_State.DO_FIGHT_ACTION:
                        pass
                    case Game_State.DEAD:
                        pass
                    case Game_State.SWITCH_PLAYER:
                        pass
                print(self.__game.get_state())

            case Client_State.MENU:
                match self.__stateMenu :
                    case Menu_State.INDEX:
                        # Affiche l'image de fond
                        image.Image(0,0,image.Page.DEBUT_JEU.value).affichage_image_redimensionnee(800, 700,self.__screen)
                    case Menu_State.GLOBALS_STATS:
                        image.Image(0,0,image.Page.STATS.value).affichage_image_redimensionnee(800, 700,self.__screen)
                    case Menu_State.HELPER:
                        image.Image(0, 0, image.Page.COMMANDES.value).affichage_image_redimensionnee(800, 700,self.__screen)
                    case Menu_State.NB_IA:
                        selectable_nb_ia = self.__interface.selectable_nb_ia()
                        image.Image(0, 0, image.Page.CHOIX_NB_IA.value).affichage_image_redimensionnee(800, 700,self.__screen)
                        if 1 in selectable_nb_ia :
                            image.Image(400, 595, image.BtnMenu.BTN_0.value).affiche(self.__screen)
                            image.Image(500, 595, image.BtnMenu.BTN_1.value).affiche(self.__screen)
                            image.Image(600, 595, image.BtnMenu.BTN_2.value).affiche(self.__screen)
                            image.Image(700, 595, image.BtnMenu.BTN_3.value).affiche(self.__screen)
                        if 2 in selectable_nb_ia :
                            image.Image(400, 595, image.BtnMenu.BTN_0.value).affiche(self.__screen)
                            image.Image(500, 595, image.BtnMenu.BTN_1.value).affiche(self.__screen)
                            image.Image(600, 595, image.BtnMenu.BTN_2.value).affiche(self.__screen)
                        if 3 in selectable_nb_ia :
                            image.Image(400, 595, image.BtnMenu.BTN_0.value).affiche(self.__screen)
                            image.Image(500, 595, image.BtnMenu.BTN_1.value).affiche(self.__screen)
                        if 4 in selectable_nb_ia :
                            texte.Texte("Le nombre de joueurs est complet tu ne peux pas ajouter d'IA", logique.Couleur.NOIR.value, 30, 600).affiche(self.get_police(),self.__screen)

                    case Menu_State.NB_PLAYER:
                        image.Image(0, 0, image.Page.CHOIX_NB_JOUEUR.value).affichage_image_redimensionnee(800, 700,self.__screen)
                        image.Image(400, 595, image.BtnMenu.BTN_1.value).affiche(self.__screen)
                        image.Image(500, 595, image.BtnMenu.BTN_2.value).affiche(self.__screen)
                        image.Image(600, 595, image.BtnMenu.BTN_3.value).affiche(self.__screen)
                        image.Image(700, 595, image.BtnMenu.BTN_4.value).affiche(self.__screen)
        pygame.display.update()
        self.__clock.tick(60)

    # Bouton de retour en arrière dans les pages Helper, Nb_joueur, Nb_ia, Fin_du_jeu   
    def mouse_on_btn_back(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return 40 <= mouse_x <= 100 and 40 <= mouse_y <= 100

    # Gestion des pages
    def menu_logical(self, mouse_x:int, mouse_y:int, is_cliked:bool):
        match self.__stateMenu :
            case Menu_State.INDEX:
                if is_cliked:
                    if (320 <= mouse_x <= 470 and 500 <= mouse_y <= 550) : # si appuie bouton stats
                        self.go_to_menu(Menu_State.GLOBALS_STATS)
                    if (170 <= mouse_x <= 350 and 550 <= mouse_y <= 600) : # si appuie bouton en local
                        self.go_to_menu(Menu_State.NB_PLAYER)
                        self.__interface = Interface(False)
                    if (450 <= mouse_x <= 630 and 550 <= mouse_y <= 600) : # si appuie bouton en ligne
                        self.go_to_menu(Menu_State.NB_PLAYER)
                        self.__interface = Interface(True)
                    if 700 <= mouse_x <= 764 and 25 <= mouse_y <= 89 : # si appuie sur info
                        self.go_to_menu(Menu_State.HELPER)
                pass
            case Menu_State.GLOBALS_STATS:
                if is_cliked:
                    if (self.mouse_on_btn_back()): # si appuie sur fleche retour
                        self.go_to_menu(Menu_State.INDEX)
                        stats = True
                pass
            case Menu_State.HELPER:
                if is_cliked:
                    if (self.mouse_on_btn_back()) : # si appuie bouton play
                        self.go_to_menu(Menu_State.INDEX)
                pass

            case Menu_State.NB_IA:
                # Recuperer les coordonnees de la souris
                selectable_nb_ia = self.__interface.selectable_nb_ia()
                if is_cliked:
                    if (self.mouse_on_btn_back()) : # si appuie bouton play
                        self.__interface.set_nb_IA(0)
                        self.go_to_menu(Menu_State.NB_PLAYER)

                    # Si le personnage sur lequel on clique est J1
                    if 400 <= mouse_x <= 500 and 582 <= mouse_y <= 652 and 0 in selectable_nb_ia:
                        self.__interface.set_nb_IA(0)
                        self.change_state(Client_State.ONLINE if self.__interface.is_online()  else Client_State.LOCAL)
                    # Si le personnage sur lequel on clique est J2
                    if 500 <= mouse_x <= 600 and 582 <= mouse_y <= 652 and 1 in selectable_nb_ia:
                        self.__interface.set_nb_IA(1)
                        self.change_state(Client_State.ONLINE if self.__interface.is_online() else Client_State.LOCAL)
                    # Si le personnage sur lequel on clique est J3
                    if 600 <= mouse_x <= 700 and 582 <= mouse_y <= 652 and 2 in selectable_nb_ia:
                        self.__interface.set_nb_IA(2)
                        self.change_state(Client_State.ONLINE if self.__interface.is_online() else Client_State.LOCAL)
                    # Si le personnage sur lequel on clique est J4
                    if 700 <= mouse_x <= 800 and 582 <= mouse_y <= 652 and 3 in selectable_nb_ia:
                        self.__interface.set_nb_IA(3)
                        self.change_state(Client_State.ONLINE if self.__interface.is_online() else Client_State.LOCAL)
                pass
            case Menu_State.NB_PLAYER:
                if is_cliked:
                    if (self.mouse_on_btn_back()) : # si appuie bouton play
                        self.__interface = None
                        self.go_to_menu(Menu_State.INDEX)
                    # Si le personnage sur lequel on clique est J2
                    if 500 <= mouse_x <= 600 and 582 <= mouse_y <= 652 :
                        self.__interface.set_nb_joueur(2)
                        if self.__interface.is_online():
                            self.change_state(Client_State.STARTING)
                        else:
                            self.go_to_menu(Menu_State.NB_IA)
                    # Si le personnage sur lequel on clique est J4
                    if 700 <= mouse_x <= 800 and 582 <= mouse_y <= 652 :
                        self.__interface.set_nb_joueur(4)
                        if self.__interface.is_online():
                            self.change_state(Client_State.STARTING)
                        else:
                            self.go_to_menu(Menu_State.NB_IA)
                    # Si le personnage sur lequel on clique est J1
                    if 400 <= mouse_x <= 500 and 582 <= mouse_y <= 652 :
                        self.__interface.set_nb_joueur(1)
                        if self.__interface.is_online():
                            self.change_state(Client_State.STARTING)
                        else:
                            self.go_to_menu(Menu_State.NB_IA)
                    # Si le personnage sur lequel on clique est J3
                    if 600 <= mouse_x <= 700 and 582 <= mouse_y <= 652 :
                        self.__interface.set_nb_joueur(3)
                        if self.__interface.is_online():
                            self.change_state(Client_State.STARTING)
                        else:
                            self.go_to_menu(Menu_State.NB_IA)
                    pass
    
    def affichage_cle(self,joueur):
        """
            La fonction affichage_cle permet d'afficher les cle dans le menu(int x, int y, Surface surface, Font font)
        """
        for i in joueur.get_inventaire():
            if i == "cle de la Ville" :
                image.Image(660,640,image.Cle.TOWN.value).affichage_image_redimensionnee(48,30,self.__screen)
            elif i == "cle de la Rivière" :
                image.Image(660,595,image.Cle.WATER.value).affichage_image_redimensionnee(48,30,self.__screen)
            elif i == "cle de la Forêt" :
                image.Image(725,595,image.Cle.GRASS.value).affichage_image_redimensionnee(48,30,self.__screen)
            elif i == "cle du Rocher" :
                image.Image(725,640,image.Cle.ROCK.value).affichage_image_redimensionnee(48,30,self.__screen)
        pygame.draw.line(self.__screen, logique.Couleur.NOIR.value, (660, 632), (770, 632), 2)
        pygame.draw.line(self.__screen, logique.Couleur.NOIR.value, (715, 595), (715, 670), 2)

    # Definir l'affichage sur le menu
    def affichage_image(self,x,y,joueur):
        """
            La fonction affichage_image permet d'afficher le personnage dans le menu(int x, int y, Surface surface, Font font)
        """        
        # Afficher l'image sur la fenetre
        self.__screen.blit(joueur.get_image(), (x, y))
        
        # Dessiner le rectangle pour les pv du joueur
        rectangle.Rectangle(500,590,130,35,logique.Couleur.VERT.value).affiche(self.__screen)
    
        # Charger les pv
        texte.Texte(joueur.get_pv(),logique.Couleur.NOIR.value,538,598).affiche(self.__screen)
        
    def affichage_image_adv(self,x,y,joueur):
        """Affiche l'image de l'ennemi dans le menu."""
        image = pygame.image.load(joueur.get_image())
        self.__screen.blit(image, (x,y))
        rectangle.Rectangle(500, 635, 130, 35, logique.Couleur.ROUGE.value).affiche(self.__screen)
        texte.Texte(joueur.get_pv(), logique.Couleur.NOIR.value, 538, 645).affiche(self.__screen)
    
    # Affichage de la partie basse du jeu en focntion du joueur qui joue
    def Menu_bas(self, un_joueur):
        # Dessiner la partie basse
        pygame.draw.rect(self.__screen,logique.Couleur.GRIS.value,(10,580,780,102))
        
        # Dessiner la place pour montrer les cles
        rectangle.Rectangle(650,585,130,90,logique.Couleur.ROSE.value).affiche(self.__screen)
        self.affichage_cle(un_joueur)
        
        # Dessiner le rectangle pour les pv du joueur
        rectangle.Rectangle(500,590,130,35,logique.Couleur.VERT.value).affiche(self.__screen)
        texte.Texte("PV joueur : ", logique.Couleur.NOIR.value, 500,590).affiche(self.__screen)
        
        # Dessiner les bords de la place pour les pv de l'adversaire
        rectangle.Rectangle(500,635,130,35,logique.Couleur.ROUGE.value).affiche(self.__screen)

        # Dessiner le rectangle pour les textes
        rectangle.Rectangle(100, 590, 390, 80, logique.Couleur.BEIGE.value).affiche(self.__screen)
        
        # Cadre pour mettre le personnage choisi
        rectangle.Rectangle(20,590,70,80,logique.Couleur.ROSE.value).affiche(self.__screen)
        
        # Prendre la variable du personnage choisi de "Position_choix_perso()""
        if un_joueur.get_prenom() == joueur.Nom.ROCK.value:
            # Ajouter la photo de Pierre
            self.affichage_image(24,598,un_joueur)
        
        if un_joueur.get_prenom() == joueur.Nom.WATER.value:
            # Ajouter la photo de Ondine
            self.affichage_image(24,598,un_joueur)
        
        if un_joueur.get_prenom() == joueur.Nom.GRASS.value:
            # Ajouter la photo de Pierre
            self.affichage_image(24,598,un_joueur)
        
        if un_joueur.get_prenom() == joueur.Nom.TOWN.value:
            # Ajouter la photo de Pierre
            self.affichage_image(24,598,un_joueur)
                
    # Boucle du jeu lorsque le jeu est démarrer qui permet de gérer les événements
    def main(self):
        self.go_to_menu(Menu_State.INDEX)
        while (self.__stateClient != Client_State.QUIT):
            self.draw()
            click = False
            dir = direction.ANY

            for event in pygame.event.get():
                if event.type == pygame.QUIT: # si le joueur quitte la fenetre
                    pygame.quit()
                    self.__stateClient = Client_State.QUIT

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
            match self.__stateClient :
                case Client_State.MENU:
                    self.menu_logical(mouse_x, mouse_y, click)
                case Client_State.LOCAL:
                    self.__game.loop(inputs(mouse_x, mouse_y, click, dir))
                case Client_State.ONLINE:
                    # envoyé les inputs au server
                    pass
                case Client_State.QUIT:
                    pass
            
            
            
if __name__ == "__main__":
    Client().main()
