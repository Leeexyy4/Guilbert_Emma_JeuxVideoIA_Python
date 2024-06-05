# ----------------------- Jeu de plateau - Interface ------------------------ #

# Bibliothèques utilisées pour le code
import pygame
from classe.visuel import image, couleur, rectangle, texte
from classe.jeu import plateau, de
from classe.personnage import joueur
class Interface:
    """La classe Interface est une classe qui permet de gérer les pages."""
    
    def __init__(self) -> None:
        """Initialisation de l'interface."""
        
        self.__etat_jeu = "menu_jeu"
        self.__jeuHLouEL = "HL"
        # Creation de la fenetre
        self.__fenetre = pygame.display.set_mode((800, 700))
        pygame.display.set_caption("Plateau de jeu")

        # Police de texte
        self.__police = pygame.font.Font('./assets/font/times-new-roman.ttf', 16)
    
        # Définir la musique
        pygame.mixer_music.load("assets/musique/Musique_jeu.mp3")
        pygame.mixer_music.play(-1,0.0,8)
    
        # Definir les variables utiles
        self.__plateau_de_jeu= plateau.Plateau()
        self.__de_jeu = de.De()
        self.__couleur = couleur.Couleur()
        self.__liste_joueur = []
        self.__nb_joueur = 0
        self.__nb_ia = 0

    def get_fenetre(self):
        """Getter de la fenetre."""
        return self.__fenetre

    def set_fenetre(self, fenetre):
        """Setter de la fenetre."""
        self.__fenetre = fenetre
        
    def get_police(self):
        """Getter de la police."""
        return self.__police

    def set_police(self, police):
        """Setter de la police."""
        self.__police = police
        
    def get_plateau_de_jeu(self):
        """Getter de la plateau_de_jeu."""
        return self.__plateau_de_jeu

    def set_plateau_de_jeu(self, plateau_de_jeu):
        """Setter de la plateau_de_jeu."""
        self.__plateau_de_jeu = plateau_de_jeu

    def get_etat_de_jeu(self):
        """Getter de l'etat de jeu."""
        return self.__etat_jeu

    def set_etat_de_jeu(self, etat_jeu):
        """Setter de l'etat de jeu."""
        self.__etat_jeu = etat_jeu
        
    def get_de_jeu(self):
        """Getter de la de_jeu."""
        return self.__de_jeu

    def set_de_jeu(self, de_jeu):
        """Setter de la de_jeu."""
        self.__de_jeu = de_jeu
        
    def get_couleur(self):
        """Getter de la couleur."""
        return self.__couleur

    def set_fenetre(self, couleur):
        """Setter de la couleur."""
        self.__couleur = couleur
        
    def get_liste_joueur(self):
        """Getter de la liste_joueur."""
        return self.__liste_joueur

    def set_liste_joueur(self, liste_joueur):
        """Setter de la liste_joueur."""
        self.__liste_joueur = liste_joueur

    def get_nb_joueur(self):
        """Getter du nb de joueur."""
        return self.__nb_joueur

    def set_nb_joueur(self, nb_joueur):
        """Setter du nb de joueur."""
        self.__nb_joueur = nb_joueur

    def get_jeuHlouEL(self):
        """Getter du mode de jeu."""
        return self.__jeuHLouEL

    def set_jeuHlouEL(self, HLouEL):
        """Setter du mode de jeu."""
        self.__jeuHLouEL = HLouEL

    def get_nb_ia(self):
        """Getter du nb d'IA."""
        return self.__nb_ia

    def set_nb_ia(self, nb_ia):
        """Setter du nb d'IA."""
        self.__nb_ia = nb_ia

    def Mise_a_jour(self, joueur):
        # Met à jour la liste des joueurs
        if self.get_liste_joueur()[joueur.get_id()][5] > 0:
            self.get_liste_joueur()[joueur.get_id()][0] = joueur.get_id()
            self.get_liste_joueur()[joueur.get_id()][1] = joueur.get_prenom()
            self.get_liste_joueur()[joueur.get_id()][2] = joueur.get_element()
            self.get_liste_joueur()[joueur.get_id()][3] = joueur.get_plateaux()
            self.get_liste_joueur()[joueur.get_id()][4] = joueur.get_plateauy()
            self.get_liste_joueur()[joueur.get_id()][5] = joueur.get_pv()
            self.get_liste_joueur()[joueur.get_id()][6] = joueur.get_attaque()
            self.get_liste_joueur()[joueur.get_id()][7] = joueur.get_inventaire()
        else:
            self.get_liste_joueur().pop(joueur.get_id())
    
    def Page_demarrage(self):    
        # Affiche l'image de fond 
        image.Image(0,0,image.Page.DEBUT_JEU.value).affichage_image_redimensionnee(800, 700,self.get_fenetre())
        # Mettre à jour l'affichage
        pygame.display.update()
        
        # Boucle while pour voir quand le joueur clique sur start
        while (self.get_etat_de_jeu() != "demarrage_jeu"):
            mouse_x, mouse_y = pygame.mouse.get_pos() # Recuperer les coordonnees de la souris
            # Pour tous les evenements
            for event in pygame.event.get():
                # Si le joueur clique sur le bouton, on passe à la prochaine page "introduction"
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    if (320 <= mouse_x <= 470 and 500 <= mouse_y <= 550) : # si appuie bouton stats
                        self.Page_statistiques()
                    if (170 <= mouse_x <= 350 and 550 <= mouse_y <= 600) : # si appuie bouton en local
                        self.Page_nb_joueur()
                    if (450 <= mouse_x <= 630 and 550 <= mouse_y <= 600) : # si appuie bouton en ligne
                        self.set_jeuHlouEL("EL")
                        self.Page_nb_joueur()
                    if 700 <= mouse_x <= 764 and 25 <= mouse_y <= 89 : # si appuie sur info
                        image.Image(0,0,image.Page.COMMANDES.value).affichage_image_redimensionnee(800, 700,self.get_fenetre())
                        # Mettre à jour l'affichage
                        pygame.display.update()
                    if (10 <= mouse_x <= 70 and 630 <= mouse_y <= 690): # si appuie sur fleche retour
                        self.Page_demarrage()
                # Si le joueur quitte la fenetre
                if (event.type == pygame.QUIT):
                    pygame.quit()
                    exit()

    def Menu_bas(self, joueur_actuel):
        # Dessiner la partie basse
        pygame.draw.rect(self.get_fenetre(),self.get_couleur().get_Gris(),(10,580,780,102))
        
        # Dessiner la place pour montrer les cles
        rectangle.Rectangle(650,585,130,90).affiche(self.get_fenetre(),self.get_couleur().get_Rose())
        self.affichage_cle(joueur_actuel)
        
        # Dessiner le rectangle pour les pv du joueur
        rectangle.Rectangle(500,590,130,35).affiche(self.get_fenetre(),self.get_couleur().get_Vert())
        texte.Texte("PV joueur : ", self.get_couleur().get_Noir(), 500,590).affiche(self.get_police(),self.get_fenetre())
        
        # Dessiner les bords de la place pour les pv de l'adversaire
        rectangle.Rectangle(500,635,130,35).affiche(self.get_fenetre(),self.get_couleur().get_Rouge())

        # Dessiner le rectangle pour les textes
        rectangle.Rectangle(100, 590, 390, 80).affiche(self.get_fenetre(),self.get_couleur().get_Beige())
        
        # Cadre pour mettre le personnage choisi
        rectangle.Rectangle(20,590,70,80).affiche(self.get_fenetre(),self.get_couleur().get_Rose())
        
        # Prendre la variable du personnage choisi de "Position_choix_perso()""
        if joueur_actuel.get_prenom() == joueur.Nom.ROCK.value:
            # Ajouter la photo de Pierre
            self.affichage_image(24,598,joueur_actuel)
        
        if joueur_actuel.get_prenom() == joueur.Nom.WATER.value:
            # Ajouter la photo de Ondine
            self.affichage_image(24,598,joueur_actuel)
        
        if joueur_actuel.get_prenom() == joueur.Nom.GRASS.value:
            # Ajouter la photo de Pierre
            self.affichage_image(24,598,joueur_actuel)
        
        if joueur_actuel.get_prenom() == joueur.Nom.TOWN.value:
            # Ajouter la photo de Pierre
            self.affichage_image(24,598,joueur_actuel)
                
        # Mettre à jour l'affichage
        pygame.display.update()
    
    def Page_statistiques(self):    
        # Affiche l'image de fond 
        image.Image(0,0,image.Page.STATS.value).affichage_image_redimensionnee(800, 700,self.get_fenetre())
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
                        self.Page_demarrage()
                        stats = True
                # Si le joueur quitte la fenetre
                if (event.type == pygame.QUIT):
                    pygame.quit()
                    exit()
            
    def Page_nb_ia(self):
        un_visible = True; deux_visible = True; trois_visible = True; quatre_visible = True
        self.set_nb_ia(0)
        image.Image(0,0,image.Page.CHOIX_NB_IA.value).affichage_image_redimensionnee(800, 700,self.get_fenetre())
        pygame.draw.rect(self.get_fenetre(),self.get_couleur().get_Gris(),(10,580,780,102))
    
        if self.get_nb_joueur() == 4 :
            texte.Texte("Le nombre de joueurs est complet tu ne peux pas ajouter d'IA", self.get_couleur().get_Noir(), 30,600).affiche(self.get_police(),self.get_fenetre())
        elif self.get_nb_joueur() == 3:
            image.Image(400,595,image.BtnMenu.BTN_1.value).affiche(self.get_fenetre())
            deux_visible = False; trois_visible = False; quatre_visible = False
        elif self.get_nb_joueur() == 2:
            image.Image(400,595,image.BtnMenu.BTN_1.value).affiche(self.get_fenetre())
            image.Image(500,595,image.BtnMenu.BTN_2.value).affiche(self.get_fenetre())
            trois_visible = False; quatre_visible = False
        elif self.get_nb_joueur() == 1:
            image.Image(400,595,image.BtnMenu.BTN_1.value).affiche(self.get_fenetre())
            image.Image(500,595,image.BtnMenu.BTN_2.value).affiche(self.get_fenetre())
            image.Image(600,595,image.BtnMenu.BTN_3.value).affiche(self.get_fenetre())
            quatre_visible = False
        if self.get_nb_joueur() != 4:
            # Texte pour choisir le nombre de joueur
            texte.Texte("Combien d'IA souhaites-tu intégrer au jeu ?", self.get_couleur().get_Noir(), 30,600).affiche(self.get_police(),self.get_fenetre())
        
        pygame.display.update()

        #Tant que le prenom n'est pas selectionne
        while (self.get_nb_ia() == 0):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN : # Si le joueur clique sur le bouton, on passe à la prochaine page "introduction"
                    mouse_x, mouse_y = pygame.mouse.get_pos() # Recuperer les coordonnees de la souris
                    if (40 <= mouse_x <= 100 and 40 <= mouse_y <= 100) : # si appuie bouton play
                        self.set_nb_ia(-1)
                        self.Page_nb_joueur()
                    # Si le personnage sur lequel on clique est J1
                    if 400 <= mouse_x <= 500 and 582 <= mouse_y <= 652 and un_visible == True:   
                        self.set_nb_ia(1)
                        self.set_etat_de_jeu("demarrage_jeu")
                    # Si le personnage sur lequel on clique est J2   
                    if 500 <= mouse_x <= 600 and 582 <= mouse_y <= 652 and deux_visible == True:
                        self.set_nb_ia(2)
                        self.set_etat_de_jeu("demarrage_jeu")
                    # Si le personnage sur lequel on clique est J3
                    if 600 <= mouse_x <= 700 and 582 <= mouse_y <= 652 and trois_visible == True:   
                        self.set_nb_ia(3)
                        self.set_etat_de_jeu("demarrage_jeu")
                    # Si le personnage sur lequel on clique est J4
                    if 700 <= mouse_x <= 800 and 582 <= mouse_y <= 652 and quatre_visible == True:   
                        self.set_nb_ia(4)
                        self.set_etat_de_jeu("demarrage_jeu")
                if event.type == pygame.QUIT: # si le joueur quitte la fenetre # si le joueur quitte la fenetre
                    pygame.quit()
                    exit()

    def Page_nb_joueur(self):
        self.set_nb_joueur(0)

        image.Image(0,0,image.Page.CHOIX_NB_JOUEUR.value).affichage_image_redimensionnee(800, 700,self.get_fenetre())
        # Dessiner la partie basse
        pygame.draw.rect(self.get_fenetre(),self.get_couleur().get_Gris(),(10,580,780,102))
        # Texte pour choisir le nombre de joueur
        texte.Texte("La sorciere du village vous a lancé un sort, pour", self.get_couleur().get_Noir(), 30,590).affiche(self.get_police(),self.get_fenetre())
        texte.Texte("vous en sortir récuper la potion chez elle.", self.get_couleur().get_Noir(), 30,620).affiche(self.get_police(),self.get_fenetre())
        texte.Texte("Combien de joueurs souhaitent jouer au jeu ? ", self.get_couleur().get_Noir(), 30,650).affiche(self.get_police(),self.get_fenetre())

        # Ajouter les photos des chifres
        image.Image(400,595,image.BtnMenu.BTN_1.value).affiche(self.get_fenetre())
        image.Image(500,595,image.BtnMenu.BTN_2.value).affiche(self.get_fenetre())
        image.Image(600,595,image.BtnMenu.BTN_3.value).affiche(self.get_fenetre())
        image.Image(700,595,image.BtnMenu.BTN_4.value).affiche(self.get_fenetre())
        
        # Mettre à jour l'affichage
        pygame.display.update()

        #Tant que le prenom n'est pas selectionne
        while (self.get_nb_joueur() == 0):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN : # Si le joueur clique sur le bouton, on passe à la prochaine page "introduction"
                    mouse_x, mouse_y = pygame.mouse.get_pos() # Recuperer les coordonnees de la souris
                    if (40 <= mouse_x <= 100 and 40 <= mouse_y <= 100) : # si appuie bouton play
                        self.set_nb_joueur(-1)
                        self.Page_demarrage()
                    # Si le personnage sur lequel on clique est J2   
                    if 500 <= mouse_x <= 600 and 582 <= mouse_y <= 652 :
                        self.set_nb_joueur(2)
                        if self.get_jeuHlouEL() == "HL":
                            self.Page_nb_ia()
                        else:
                            self.set_etat_de_jeu("demarrage_jeu")
                    # Si le personnage sur lequel on clique est J4
                    if 700 <= mouse_x <= 800 and 582 <= mouse_y <= 652 :   
                        self.set_nb_joueur(4)
                        if self.get_jeuHlouEL() == "HL":
                            self.Page_nb_ia()
                        else:
                            self.set_etat_de_jeu("demarrage_jeu")
                    # Si le personnage sur lequel on clique est J1
                    if 400 <= mouse_x <= 500 and 582 <= mouse_y <= 652 :   
                        self.set_nb_joueur(1)
                        if self.get_jeuHlouEL() == "HL":
                            self.Page_nb_ia()
                        else:
                            self.set_etat_de_jeu("demarrage_jeu")
                    # Si le personnage sur lequel on clique est J3
                    if 600 <= mouse_x <= 700 and 582 <= mouse_y <= 652 :   
                        self.set_nb_joueur(3)
                        if self.get_jeuHlouEL() == "HL":
                            self.Page_nb_ia()
                        else:
                            self.set_etat_de_jeu("demarrage_jeu")
                if event.type == pygame.QUIT: # si le joueur quitte la fenetre # si le joueur quitte la fenetre
                    pygame.quit()
                    exit()

    def Page_choixperso(self, numero_joueur):  
        P_click = True
        O_click = True
        F_click = True
        K_click = True
        image.Image(0,0,image.Page.CHOIX_PERSO.value).affichage_image_redimensionnee(800, 700,self.get_fenetre())
        # Dessiner le cadre du bas afin de cacher les anciennes ecritures
        rectangle.Rectangle(10,580,780,100).affiche(self.get_fenetre(),self.get_couleur().get_Gris())
        
        # Texte pour choisir le personnage
        texte.Texte("Bienvenue à toi jeune aventurier !",self.get_couleur().get_Noir() ,30,590).affiche(self.get_police(), self.get_fenetre())
        texte.Texte("Je t'invite à choisir un personnage parmi la liste suivante :",self.get_couleur().get_Noir() ,30,620).affiche(self.get_police(), self.get_fenetre())

        texte.Texte(joueur.Nom.ROCK.value+", "+joueur.Nom.WATER.value+", "+joueur.Nom.TOWN.value+" ou "+joueur.Nom.GRASS.value,self.get_couleur().get_Noir() ,30,650).affiche(self.get_police(),self.get_fenetre())
        
        noms_joueurs = []
        if self.get_liste_joueur() != []:
            for i in self.get_liste_joueur():
                noms_joueurs.append(i[1])
            if joueur.Nom.ROCK.value not in noms_joueurs:
                # Ajouter les photos des personnages
                image.Image(400,585,image.Personnages.ROCK.value).affiche(self.get_fenetre())
                
                texte.Texte(joueur.Nom.ROCK.value,self.get_couleur().get_Noir(), 413, 650).affiche(self.get_police(),self.get_fenetre())
            else:
                P_click = False
            if joueur.Nom.WATER.value not in noms_joueurs:
                image.Image(500,585,image.Personnages.WATER.value).affiche(self.get_fenetre())
                texte.Texte(joueur.Nom.WATER.value,self.get_couleur().get_Noir(), 510, 650).affiche(self.get_police(),self.get_fenetre())
            else:
                O_click = False
            if joueur.Nom.TOWN.value not in noms_joueurs:
                image.Image(600,585,image.Personnages.TOWN.value).affiche(self.get_fenetre())
                texte.Texte(joueur.Nom.TOWN.value,self.get_couleur().get_Noir(), 613, 650).affiche(self.get_police(),self.get_fenetre())
            else:
                K_click = False
            if joueur.Nom.GRASS.value not in noms_joueurs:
                image.Image(700,585,image.Personnages.GRASS.value).affiche(self.get_fenetre())
                texte.Texte(joueur.Nom.GRASS.value,self.get_couleur().get_Noir(), 715, 650).affiche(self.get_police(),self.get_fenetre())
            else:
                F_click = False
        else:
            # Ajouter les photos des personnages
            image.Image(400,585,image.Personnages.ROCK.value).affiche(self.get_fenetre())
            texte.Texte(joueur.Nom.ROCK.value,self.get_couleur().get_Noir(), 413, 650).affiche(self.get_police(),self.get_fenetre())
            image.Image(500,585,image.Personnages.WATER.value).affiche(self.get_fenetre())
            texte.Texte(joueur.Nom.WATER.value,self.get_couleur().get_Noir(), 510, 650).affiche(self.get_police(),self.get_fenetre())
            image.Image(600,585,image.Personnages.TOWN.value).affiche(self.get_fenetre())
            texte.Texte(joueur.Nom.TOWN.value,self.get_couleur().get_Noir(), 613, 650).affiche(self.get_police(),self.get_fenetre())
            image.Image(700,585,image.Personnages.GRASS.value).affiche(self.get_fenetre())
            texte.Texte(joueur.Nom.GRASS.value,self.get_couleur().get_Noir(), 715, 650).affiche(self.get_police(),self.get_fenetre())

        # Texte pour animer la page
        texte.Texte("Amusez-vous bien ici demarre une nouvelle aventure !",self.get_couleur().get_Blanc(),230, 530).affiche(self.get_police(),self.get_fenetre())
        
        # Mettre à jour l'affichage
        pygame.display.update()
        
        # Faire un systeme pour la selection de la position du clic pour la selection du personnage
        prenom = ""
        
        #Tant que le prenom n'est pas selectionne
        while (prenom != joueur.Nom.ROCK.value) or (prenom != joueur.Nom.WATER.value) or (prenom != joueur.Nom.GRASS.value) or (prenom != joueur.Nom.TOWN.value) :
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN : # Si le joueur clique sur le bouton, on passe à la prochaine page "introduction"
                    mouse_x, mouse_y = pygame.mouse.get_pos() # Recuperer les coordonnees de la souris
                    # Si le personnage sur lequel on clique est Ondine   
                    if (500 <= mouse_x <= 600 and 582 <= mouse_y <= 652 and O_click == True):
                        prenom = joueur.Nom.WATER.value
                        element = joueur.Element.WATER.value
                        return prenom, element
                    # Si le personnage sur lequel on clique est Flora
                    if (700 <= mouse_x <= 800 and 582 <= mouse_y <= 652 and F_click == True): 
                        prenom = joueur.Nom.GRASS.value
                        element = joueur.Element.GRASS.value
                        return prenom, element
                    # Si le personnage sur lequel on clique est Pierre
                    if (400 <= mouse_x <= 500 and 582 <= mouse_y <= 652 and P_click == True): 
                        prenom = joueur.Nom.ROCK.value
                        element = joueur.Element.ROCK.value
                        return prenom, element
                    # Si le personnage sur lequel on clique est Kevin
                    if (600 <= mouse_x <= 700 and 582 <= mouse_y <= 652 and K_click == True):
                        prenom = joueur.Nom.TOWN.value
                        element = joueur.Element.TOWN.value
                        return prenom, element
                if event.type == pygame.QUIT: # si le joueur quitte la fenetre # si le joueur quitte la fenetre
                    pygame.quit()
                    exit()
        
    def Page_premier_mouvement(self, joueur):
        self.get_plateau_de_jeu().set_cases_decouvertes(self.get_plateau_de_jeu().get_cases_decouvertes() + [[self.get_plateau_de_jeu().get_case_jaune()[0],self.get_plateau_de_jeu().get_case_jaune()[1]]])
        image.Image(0,468, image.Page.BAS_PLATEAU.value).affiche(self.get_fenetre())
        self.Menu_bas(joueur)
        # cacher le Texte
        rectangle.Rectangle(100, 590, 390, 80).affiche(self.get_fenetre(),self.get_couleur().get_Beige())
        texte.Texte("Tu es le joueur " + str(joueur.get_id() + 1) + ", clique sur le de afin de faire",self.get_couleur().get_Noir(),110,600).affiche(self.get_police(),self.get_fenetre())
        texte.Texte("ton deplacement",self.get_couleur().get_Noir(),110,620).affiche(self.get_police(),self.get_fenetre())
        
        # Affiche le de sur la face 1
        image.Image(350,475,image.De.FACE1.value).affiche(self.get_fenetre())
        
        # Mettre à jour l'affichage
        pygame.display.update()
        
    def Page_mouvement(self, joueur):
        image.Image(0,468, image.Page.CHOIX_DOUBLE.value).affiche(self.get_fenetre())
        self.Menu_bas(joueur)
        rectangle.Rectangle(100, 590, 390, 80).affiche(self.get_fenetre(),self.get_couleur().get_Beige())
        texte.Texte("Joueur " + str(joueur.get_id() + 1) + " : " + joueur.get_prenom() + " clique sur le de afin ",self.get_couleur().get_Noir(),110,600).affiche(self.get_police(),self.get_fenetre())
        texte.Texte("d'attaquer un joueur ou de lancer le de",self.get_couleur().get_Noir(),110,620).affiche(self.get_police(),self.get_fenetre())
        
        # Affiche le de sur la face 1
        image.Image(220,480,image.Interaction.ATTAQUER.value).affiche(self.get_fenetre())
        image.Image(510, 480,image.Interaction.DE.value).affiche(self.get_fenetre())
        texte.Texte("Attaquer",self.get_couleur().get_Blanc(),227,545).affiche(self.get_police(),self.get_fenetre())
        texte.Texte("De",self.get_couleur().get_Blanc(),532,545).affiche(self.get_police(),self.get_fenetre())
        
        # Mettre à jour l'affichage
        pygame.display.update()
        
        # Faire un systeme pour la selection de la position du clic pour la selection du personnage
        action_joueur = ""
        
        #Tant que le prenom n'est pas selectionne
        while (action_joueur != "Attaquer") or (action_joueur != "Lancer") :
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN : # Si le joueur clique sur le bouton, on passe à la prochaine page "introduction"
                    mouse_x, mouse_y = pygame.mouse.get_pos() # Recuperer les coordonnees de la souris
                    # Si le personnage sur lequel on clique est Ondine   
                    if 220 <= mouse_x <= 284 and 480 <= mouse_y <= 544 :
                        
                        action_joueur = "Attaquer"
                        image.Image(0,468,image.Page.BAS_PLATEAU.value).affiche(self.get_fenetre())
                        return action_joueur
                    elif 510 <= mouse_x <= 574 and 480 <= mouse_y <= 544:
                        
                        action_joueur = "Lancer"
                        image.Image(0,468,image.Page.BAS_PLATEAU.value).affiche(self.get_fenetre())
                        de_face1 = image.De.FACE1.value
                        self.get_fenetre().blit(de_face1,(350,475))
                        pygame.display.update()
                        return action_joueur
                if event.type == pygame.QUIT: # si le joueur quitte la fenetre # si le joueur quitte la fenetre
                    pygame.quit()
                    exit()

    def Page_direction(self, joueur):
        """Genere la page qui permet de faire le deplacement en demandant le choix de direction

        Return:
            event.key touche_fleche: Retourne la touche appuyer par le joueur pour faire le deplacement
        """    
        # Lance le de
        self.get_de_jeu().Choix_de(self.get_fenetre())
        face_choisie = self.get_de_jeu().get_face_choisie()
                
        # Rectangle : Reinitialise la fenetre de Texte
        rectangle.Rectangle(100, 590, 390, 80).affiche(self.get_fenetre(),self.get_couleur().get_Beige())

        # Texte : Lancer le de
        texte.Texte("Bravo ! Tu peux avancer de {} cases ! Où ".format(face_choisie),self.get_couleur().get_Noir(),110,600).affiche(self.get_police(),self.get_fenetre())
        texte.Texte("veux-tu aller ? (haut, bas, gauche, droite)",self.get_couleur().get_Noir(),110,620).affiche(self.get_police(),self.get_fenetre())
        

        # Mise à jour de l'affichage
        pygame.display.update()
        
        
        # Tant que : Le joueur n'a pas choisi de direction (haut, bas, gauche, droite)
        while face_choisie != 0 :
            # Pour tout : Les evenements de pygame
            for event in pygame.event.get():
                
                # Si le joueur quitte la fenetre
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    
                elif event.type == pygame.KEYDOWN:
                    touche_fleche = event.key

                    if touche_fleche == pygame.K_UP:
                        # La touche fleche vers le haut a ete enfoncee
                        avancer = joueur.haut(47)
                        self.get_plateau_de_jeu().set_cases_decouvertes(self.get_plateau_de_jeu().get_cases_decouvertes() + [[joueur.get_plateaux(),joueur.get_plateauy()]])
                        self.Mise_a_jour(joueur)
                        self.get_plateau_de_jeu().plateau_cache(self)
                        self.affichage_image_plateau(joueur)
                        if avancer == True :
                            face_choisie = face_choisie - 1
                        else:
                            self.Page_rejouer(face_choisie)
                    
                    elif touche_fleche == pygame.K_DOWN:
                        # La touche fleche vers le bas a ete enfoncee
                        avancer = joueur.bas(47)
                        self.get_plateau_de_jeu().set_cases_decouvertes(self.get_plateau_de_jeu().get_cases_decouvertes() + [[joueur.get_plateaux(),joueur.get_plateauy()]])
                        self.Mise_a_jour(joueur)
                        self.get_plateau_de_jeu().plateau_cache(self)
                        self.affichage_image_plateau(joueur)
                        if avancer == True :
                            face_choisie = face_choisie - 1
                        else:
                            self.Page_rejouer(face_choisie)
                    
                    elif touche_fleche == pygame.K_RIGHT:
                        # La touche fleche vers la droite a ete enfoncee
                        avancer = joueur.droite(47) 
                        self.get_plateau_de_jeu().set_cases_decouvertes(self.get_plateau_de_jeu().get_cases_decouvertes() + [[joueur.get_plateaux(),joueur.get_plateauy()]])
                        self.Mise_a_jour(joueur) 
                        self.get_plateau_de_jeu().plateau_cache(self)
                        self.affichage_image_plateau(joueur)
                        if avancer == True :
                            face_choisie = face_choisie - 1
                        else:
                            self.Page_rejouer(face_choisie)

                    elif touche_fleche == pygame.K_LEFT:
                        # La touche fleche vers la gauche a ete enfoncee
                        avancer = joueur.gauche(47) 
                        self.get_plateau_de_jeu().set_cases_decouvertes(self.get_plateau_de_jeu().get_cases_decouvertes() + [[joueur.get_plateaux(),joueur.get_plateauy()]])  
                        self.Mise_a_jour(joueur)                
                        self.get_plateau_de_jeu().plateau_cache(self)
                        self.affichage_image_plateau(joueur)
                        if avancer == True :
                            face_choisie = face_choisie - 1
                        else:
                            self.Page_rejouer(face_choisie)
                            
    def Page_rejouer(self, face_choisie):
            # Dessiner le rectangle pour les dialogues
            rectangle.Rectangle(100, 590, 390, 80).affiche(self.get_fenetre(), self.get_couleur().get_Beige())
            # Texte pour dire au joueur de rejouer
            texte.Texte("Tu ne peux pas aller par là, tu as atteint un bord", self.get_couleur().get_Noir(), 110, 600).affiche(self.get_police(),self.get_fenetre())
            texte.Texte("ou il n'y a pas de cases dans cette direction", self.get_couleur().get_Noir(), 110, 620).affiche(self.get_police(),self.get_fenetre())
            texte.Texte("rejoue ! Tu peux avancer de {} cases ! ".format(face_choisie), self.get_couleur().get_Noir(), 110, 640).affiche(self.get_police(),self.get_fenetre())
            self.get_plateau_de_jeu().plateau_cache(self)
            pygame.display.update()

    def Page_action(self, joueur):
            # Dessiner le rectangle pour les dialogues
            rectangle.Rectangle(100, 590, 390, 80).affiche(self.get_fenetre(), self.get_couleur().get_Beige())
            # Texte pour dire au joueur de rejouer
            texte.Texte("Tu as atterris sur une case {}".format(self.get_plateau_de_jeu().get_nom(joueur.get_plateaux(),joueur.get_plateauy())), self.get_couleur().get_Noir(), 110, 600).affiche(self.get_police(),self.get_fenetre())
            pygame.display.update()
            couleur_case = self.get_plateau_de_jeu().get_plateau()[joueur.get_plateaux()][joueur.get_plateauy()]
            image.Image(0,468,image.Page.BAS_PLATEAU.value).affiche(self.get_fenetre())
            self.Menu_bas(joueur)  
            if joueur.get_pv() != 0:
                if couleur_case == self.get_couleur().get_Beige():
                    self.get_plateau_de_jeu().Action_couleur_Beige(self, joueur)
                    
                elif couleur_case == self.get_couleur().get_Blanc():
                    # Dessiner le rectangle pour les dialogues
                    rectangle.Rectangle(100, 590, 390, 80).affiche(self.get_fenetre(), self.get_couleur().get_Beige())
                    texte.Texte("Tu es dans une case Vide.",self.get_couleur().get_Noir(),110, 600).affiche(self.get_police(),self.get_fenetre())
                    texte.Texte("Il ne t'arrivera rien tu peux etre rassure.",self.get_couleur().get_Noir(),110, 620).affiche(self.get_police(),self.get_fenetre())
                    
                elif couleur_case == self.get_couleur().get_Bleu():
                    self.get_plateau_de_jeu().Action_couleur_Bleu(self, joueur)
                            
                elif couleur_case == self.get_couleur().get_Gris():
                    self.get_plateau_de_jeu().Action_couleur_Gris(self, joueur)
                    
                elif couleur_case == self.get_couleur().get_Indigo():
                    self.get_plateau_de_jeu().Action_couleur_Indigo(self, joueur)
                    
                elif couleur_case == self.get_couleur().get_Jaune():
                    # Dessiner le rectangle pour les dialogues
                    rectangle.Rectangle(100, 590, 390, 80).affiche(self.get_fenetre(), self.get_couleur().get_Beige())
                    texte.Texte("Tu es la case de Depart.",self.get_couleur().get_Noir(),110, 600).affiche(self.get_police(),self.get_fenetre())
                    texte.Texte("Depeche toi de recuperer les cles",self.get_couleur().get_Noir(),110, 620).affiche(self.get_police(),self.get_fenetre())
                    texte.Texte("avant les autres joueurs.",self.get_couleur().get_Noir(),110, 640).affiche(self.get_police(),self.get_fenetre())
                    
                elif couleur_case == self.get_couleur().get_Noir():
                    self.get_plateau_de_jeu().Action_couleur_Noir(self, joueur)     
                    
                elif couleur_case == self.get_couleur().get_Orange():
                    self.get_plateau_de_jeu().Action_couleur_Orange(self, joueur)

                elif couleur_case == self.get_couleur().get_Rose():
                    self.get_plateau_de_jeu().Action_couleur_Rose(self, joueur)
                    
                elif couleur_case == self.get_couleur().get_Rouge():
                    self.get_plateau_de_jeu().Action_couleur_Rouge(self, joueur)
                    
                elif couleur_case == self.get_couleur().get_Turquoise():
                    self.get_plateau_de_jeu().Action_couleur_Turquoise(self)
                    
                elif couleur_case == self.get_couleur().get_Violet():
                    self.get_plateau_de_jeu().Action_couleur_Violet(self, joueur)
            pygame.display.update()
            pygame.time.delay(1500)


    
    def Page_sorciere(self, joueur):
        # Page de la sorcière quan don a réussi le jeu
        image.Image(0,0,image.Sorciere.MAISON.value).affichage_image_redimensionnee(800, 700,self.get_fenetre())
        self.Menu_bas(joueur)
        texte.Texte("Tu es chez la sorciere, mais j'ai l'impression",couleur.Couleur().get_Noir(),110,600).affiche(self.get_police(),self.get_fenetre())
        texte.Texte("qu'elle est sortie de sa taniere...",couleur.Couleur().get_Noir(),110,620).affiche(self.get_police(),self.get_fenetre())
        texte.Texte("profite-en pour fouiller dans ses affaires :)",couleur.Couleur().get_Noir(),110,640).affiche(self.get_police(),self.get_fenetre())
        pygame.display.update()
        selection_potion = False
        while selection_potion != True:
            mouse_x, mouse_y = pygame.mouse.get_pos() # Recuperer les coordonnees de la souris
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # si le joueur quitte la self.get_fenetre() # si le joueur quitte la self.get_fenetre()
                    pygame.quit()
                    exit() 
                
                # Si le clique est presse
                if event.type == pygame.MOUSEBUTTONDOWN:  
                    if 500 < mouse_x < 725 and 150 < mouse_y < 450:
                        image.Image(0,0,image.Sorciere.MAISON_SYMBOLE.value).affichage_image_redimensionnee(800, 700,self.get_fenetre())
                        self.Menu_bas(joueur)
                        texte.Texte("C'est un symbole astral, si c'est chez la",couleur.Couleur().get_Noir(),110,600).affiche(self.get_police(),self.get_fenetre())
                        texte.Texte("sorciere, il vaut mieux ne pas y toucher",couleur.Couleur().get_Noir(),110,620).affiche(self.get_police(),self.get_fenetre())
                        pygame.display.update()
                        pygame.time.delay(2500)
                        image.Image(0,0,image.Sorciere.MAISON.value).affichage_image_redimensionnee(800, 700,self.get_fenetre())
                        self.Menu_bas(joueur)
                        texte.Texte("Tu es chez la sorciere, mais on dirait",couleur.Couleur().get_Noir(),110,600).affiche(self.get_police(),self.get_fenetre())
                        texte.Texte("qu'elle est sortie de sa taniere...",couleur.Couleur().get_Noir(),110,620).affiche(self.get_police(),self.get_fenetre())
                        texte.Texte("profite-en pour fouiller dans ses affaires :)",couleur.Couleur().get_Noir(),110,640).affiche(self.get_police(),self.get_fenetre())
                        pygame.display.update()
                    elif 90 < mouse_x < 190 and 180 < mouse_y < 350:
                        image.Image(0,0,image.Sorciere.MAISON_DRAGON.value).affichage_image_redimensionnee(800, 700,self.get_fenetre())
                        self.Menu_bas(joueur)
                        texte.Texte("Un dragon de pierre... ce n'est pas très",couleur.Couleur().get_Noir(),110,600).affiche(self.get_police(),self.get_fenetre())
                        texte.Texte("rassurant, trouvons vite un remède et sortons",couleur.Couleur().get_Noir(),110,620).affiche(self.get_police(),self.get_fenetre())
                        texte.Texte("d'ici très vite",couleur.Couleur().get_Noir(),110,640).affiche(self.get_police(),self.get_fenetre())
                        pygame.display.update()
                        pygame.time.delay(2500)
                        image.Image(0,0,image.Sorciere.MAISON.value).affichage_image_redimensionnee(800, 700,self.get_fenetre())
                        self.Menu_bas(joueur)
                        texte.Texte("Tu es chez la sorciere, mais on dirait",couleur.Couleur().get_Noir(),110,600).affiche(self.get_police(),self.get_fenetre())
                        texte.Texte("qu'elle est sortie de sa taniere...",couleur.Couleur().get_Noir(),110,620).affiche(self.get_police(),self.get_fenetre())
                        texte.Texte("profite-en pour fouiller dans ses affaires :)",couleur.Couleur().get_Noir(),110,640).affiche(self.get_police(),self.get_fenetre())
                        pygame.display.update()
                    elif 330 < mouse_x < 430 and 480 < mouse_y < 580:
                        image.Image(0,0,image.Sorciere.MAISON.value).affichage_image_redimensionnee(800, 700,self.get_fenetre())
                        self.Menu_bas(joueur)
                        texte.Texte("Tu as trouvé une potion... Potion inverstium",couleur.Couleur().get_Noir(),110,600).affiche(self.get_police(),self.get_fenetre())
                        texte.Texte("Tu décides de la boire afin d'inverser le",couleur.Couleur().get_Noir(),110,620).affiche(self.get_police(),self.get_fenetre())
                        texte.Texte("sortilège",couleur.Couleur().get_Noir(),110,640).affiche(self.get_police(),self.get_fenetre())
                        joueur.set_inventaire(["Potion inverstium"])
                        self.affichage_potion()
                        pygame.display.update()
                        pygame.time.delay(2500)
                        image.Image(0,0,image.Page.FIN_JEU).affichage_image_redimensionnee(800, 700,self.get_fenetre())
                        self.Menu_bas(joueur)
                        texte.Texte("Tu as terminé le jeu bravo à toi jeune aventurier",couleur.Couleur().get_Noir(),110,600).affiche(self.get_police(),self.get_fenetre())
                        texte.Texte("Tu es le premier a t'être libéré du sort !!",couleur.Couleur().get_Noir(),110,620).affiche(self.get_police(),self.get_fenetre())
                        pygame.display.update()
                        pygame.time.delay(2500)
    
    # Definir l'affichage sur le menu
    def affichage_image(self,x,y,joueur):
        """
            La fonction affichage_image permet d'afficher le personnage dans le menu(int x, int y, Surface surface, Font font)
        """
        # Charger l'image
        image = pygame.image.load(joueur.get_lien())
        
        # Afficher l'image sur la fenetre
        self.get_fenetre().blit(image, (x, y))
        
        # Dessiner le rectangle pour les pv du joueur
        rectangle.Rectangle(500,590,130,35).affiche(self.get_fenetre(),couleur.Couleur().get_Vert())
    
        # Charger les pv
        texte.Texte(joueur.get_pv(),couleur.Couleur().get_Noir(),538,598).affiche(self.get_police(),self.get_fenetre())
        
        # Mettre à jour l'affichage
        pygame.display.update()
    
    def affichage_image_adv(self,x,y,joueur):
        """Affiche l'image de l'ennemi dans le menu."""
        image = pygame.image.load(joueur.get_lien())
        self.get_fenetre().blit(image, (x,y))
        rectangle.Rectangle(500, 635, 130, 35).affiche(self.get_fenetre(), couleur.Couleur().get_Rouge())
        texte.Texte(joueur.get_pv(), couleur.Couleur().get_Noir(), 538, 645).affiche(self.get_police(), self.get_fenetre())
        pygame.display.update()

    def affichage_cle(self,joueur):
        """
            La fonction affichage_cle permet d'afficher les cle dans le menu(int x, int y, Surface surface, Font font)
        """
        for i in joueur.get_inventaire():
            if i == "cle de la Ville" :
                image.Image(660,640,image.Cle.TOWN.value).affichage_image_redimensionnee(48,30,self.get_fenetre())
            elif i == "cle de la Rivière" :
                image.Image(660,595,image.Cle.WATER.value).affichage_image_redimensionnee(48,30,self.get_fenetre())
            elif i == "cle de la Forêt" :
                image.Image(725,595,image.Cle.GRASS.value).affichage_image_redimensionnee(48,30,self.get_fenetre())
            elif i == "cle du Rocher" :
                image.Image(725,640,image.Cle.ROCK.value).affichage_image_redimensionnee(48,30,self.get_fenetre())
        pygame.draw.line(self.get_fenetre(), couleur.Couleur().get_Noir(), (660, 632), (770, 632), 2)
        pygame.draw.line(self.get_fenetre(), couleur.Couleur().get_Noir(), (715, 595), (715, 670), 2)
        # Mettre à jour l'affichage
        pygame.display.update()
    
    # Definir l'affichage sur le plateau
    def affichage_image_plateau(self,joueur):
        """
            La fonction affichage_image_plateau permet d'afficher le personnage dans le plateau(int x, int y, Surface surface)
        """
        # Charger l'image
        image = pygame.image.load(joueur.get_lien())
        image_redimensionnee = pygame.transform.scale(image, (47, 47))
        
        # Afficher l'image redimensionnee sur la fenetre
        self.get_fenetre().blit(image_redimensionnee, (joueur.get_x(), joueur.get_y()))
        
        # Mettre à jour l'affichage
        pygame.display.update()        


    def affiche_tt_joueur(self):
        """Affiche tous les joueurs sur le plateau."""
        if len(self.get_liste_joueur()) == 1:
            J1  = joueur.Joueur(0,self.get_liste_joueur()[0][1], self.get_liste_joueur()[0][2],self.get_liste_joueur()[0][3], self.get_liste_joueur()[0][4], self.get_liste_joueur()[0][5], self.get_liste_joueur()[0][6], self.get_liste_joueur()[0][7])
            self.affichage_image_plateau(J1)
            pygame.display.update()
        elif len(self.get_liste_joueur()) == 2:
            J1 = joueur.Joueur(0,self.get_liste_joueur()[0][1], self.get_liste_joueur()[0][2],self.get_liste_joueur()[0][3], self.get_liste_joueur()[0][4], self.get_liste_joueur()[0][5], self.get_liste_joueur()[0][6], self.get_liste_joueur()[0][7])
            J2 = joueur.Joueur(1,self.get_liste_joueur()[1][1], self.get_liste_joueur()[1][2],self.get_liste_joueur()[1][3], self.get_liste_joueur()[1][4], self.get_liste_joueur()[1][5], self.get_liste_joueur()[1][6], self.get_liste_joueur()[1][7])
            self.affichage_image_plateau(J1)
            self.affichage_image_plateau(J2)
            pygame.display.update()
        elif len(self.get_liste_joueur()) == 3:
            J1 = joueur.Joueur(0,self.get_liste_joueur()[0][1], self.get_liste_joueur()[0][2],self.get_liste_joueur()[0][3], self.get_liste_joueur()[0][4], self.get_liste_joueur()[0][5], self.get_liste_joueur()[0][6], self.get_liste_joueur()[0][7])
            J2 = joueur.Joueur(1,self.get_liste_joueur()[1][1], self.get_liste_joueur()[1][2],self.get_liste_joueur()[1][3], self.get_liste_joueur()[1][4], self.get_liste_joueur()[1][5], self.get_liste_joueur()[1][6], self.get_liste_joueur()[1][7])
            J3 = joueur.Joueur(2,self.get_liste_joueur()[2][1], self.get_liste_joueur()[2][2],self.get_liste_joueur()[2][3], self.get_liste_joueur()[2][4], self.get_liste_joueur()[2][5], self.get_liste_joueur()[2][6], self.get_liste_joueur()[2][7])
            self.affichage_image_plateau(J1)
            self.affichage_image_plateau(J2)
            self.affichage_image_plateau(J3)
            pygame.display.update()
        elif len(self.get_liste_joueur()) == 4:
            J1 = joueur.Joueur(0,self.get_liste_joueur()[0][1], self.get_liste_joueur()[0][2],self.get_liste_joueur()[0][3], self.get_liste_joueur()[0][4], self.get_liste_joueur()[0][5], self.get_liste_joueur()[0][6], self.get_liste_joueur()[0][7])
            J2 = joueur.Joueur(1,self.get_liste_joueur()[1][1], self.get_liste_joueur()[1][2],self.get_liste_joueur()[1][3], self.get_liste_joueur()[1][4], self.get_liste_joueur()[1][5], self.get_liste_joueur()[1][6], self.get_liste_joueur()[1][7])
            J3 = joueur.Joueur(2,self.get_liste_joueur()[2][1], self.get_liste_joueur()[2][2],self.get_liste_joueur()[2][3], self.get_liste_joueur()[2][4], self.get_liste_joueur()[2][5], self.get_liste_joueur()[2][6], self.get_liste_joueur()[2][7])
            J4 = joueur.Joueur(3,self.get_liste_joueur()[3][1], self.get_liste_joueur()[3][2],self.get_liste_joueur()[3][3], self.get_liste_joueur()[3][4], self.get_liste_joueur()[3][5], self.get_liste_joueur()[3][6], self.get_liste_joueur()[3][7])
            self.affichage_image_plateau(J1)
            self.affichage_image_plateau(J2)
            self.affichage_image_plateau(J3)
            self.affichage_image_plateau(J4)
            pygame.display.update()
    
    def affichage_potion(self):
        """
            La fonction affichage_image_plateau permet d'afficher le personnage dans le plateau(int x, int y, Surface surface)
        """
        # Charger l'image
        potion = image.Sorciere.POTION.value
        
        # Afficher l'image redimensionnee sur la fenetre
        self.get_fenetre().blit(potion, (668, 593))
        
        # Mettre à jour l'affichage
        pygame.display.update()  