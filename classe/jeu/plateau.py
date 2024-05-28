# ----------------------- Jeu de plateau - Plateau  ------------------------ #

# Bibliothèques utilisées pour le code
import pygame, random
from classe.visuel import texte, couleur, rectangle, image
from classe.personnage import ennemis

pygame.init()

class Plateau:
    """La classe Plateau est une classe qui permet de créer le plateau de jeu."""
    
    # Initialisation du plateau
    def __init__(self) -> None:
        """_summary_
            Initialisation du Plateau
        """
        # Définir le plateau
        self.__plateau = []
        
        # Définir la taille d'une case
        self.__taille_case = 800 // 17
        
        # Définir les noms des cases
        self.__nom_case = {
            couleur.Couleur().get_Rouge(): "Boss",
            couleur.Couleur().get_Rose(): "Chance",
            couleur.Couleur().get_Orange(): "Malus",
            couleur.Couleur().get_Indigo(): "Pouf",
            couleur.Couleur().get_Violet(): "Rejoue",
            couleur.Couleur().get_Turquoise(): "Grrr",
            couleur.Couleur().get_Beige(): "Hutte",
            couleur.Couleur().get_Gris(): "Spéciale",
            couleur.Couleur().get_Bleu(): "Puit",
            couleur.Couleur().get_Blanc(): "Vide",
            couleur.Couleur().get_Noir(): "Mort",
            couleur.Couleur().get_Jaune(): "Départ"
        }
        
        self.__max_couleur = {
            couleur.Couleur().get_Rouge(): 4,
            couleur.Couleur().get_Rose(): 26,
            couleur.Couleur().get_Orange(): 29,
            couleur.Couleur().get_Indigo(): 2,
            couleur.Couleur().get_Violet(): 20,
            couleur.Couleur().get_Turquoise(): 20,
            couleur.Couleur().get_Beige(): 1,
            couleur.Couleur().get_Gris(): 10,
            couleur.Couleur().get_Bleu(): 1,
            couleur.Couleur().get_Noir(): 1,
            couleur.Couleur().get_Jaune():1,
            couleur.Couleur().get_Blanc():55
        }

        self.__cases_decouvertes = []

        self.remplir_plateau_aleatoirement()
        

    def get_plateau(self):
        """Renvoie le plateau de jeu."""
        return self.__plateau
    
    def get_cases_decouvertes(self):
        """Renvoie les cases decouvertes de jeu."""
        return self.__cases_decouvertes

    def get_cases(self, ligne, colonne):
        """Renvoie la couleur de la case à la position spécifiée."""
        return self.get_plateau()[ligne][colonne]
        
    def get_nom(self, ligne, colonne):
        """Renvoie le nom de la case à la position spécifiée."""
        couleur_case = self.get_plateau()[ligne][colonne]  # Obtenir la couleur de la case
        nom_case = self.__nom_case[couleur_case]
        return nom_case
    
    def get_case_jaune(self):
        """Renvoie les coordonnées correspondant à la case jaune."""
        for ligne in range(10):
            for colonne in range(17):
                if self.get_plateau()[ligne][colonne] == couleur.Couleur().get_Jaune():
                    coord_case_jaune = (ligne, colonne)
        return coord_case_jaune

    def get_case_indigo(self, joueur):
        """Renvoie les coordonnées correspondant aux cases indigo."""
        for ligne in range(10):
            for colonne in range(17):
                if self.get_plateau()[ligne][colonne] == couleur.Couleur().get_Indigo():
                    if joueur.get_plateaux() == ligne and joueur.get_plateauy() == colonne:
                        pass
                    else:
                        coord_case_indigo = (ligne, colonne)
        return coord_case_indigo

    def set_plateau(self, plateau):
        """Modifie le plateau de jeu."""
        self.__plateau = plateau

    def set_cases_decouvertes(self, cases_decouvertes):
        """Modifie les cases decouvertes de jeu."""
        self.__cases_decouvertes = cases_decouvertes
        
    def remplir_plateau_aleatoirement(self):
        """Remplit le plateau de manière aléatoire en fonction de max_couleur."""
        # Crée une liste des couleurs disponibles en fonction de max_couleur
        couleurs_disponibles = []
        for couleurs, nombre_max in self.__max_couleur.items():
            couleurs_disponibles.extend([couleurs] * nombre_max)

         # Remplit le plateau de manière aléatoire
        for i in range(10):
            ligne_plateau = []
            for j in range(17):
                if couleurs_disponibles:  # Vérifiez si des couleurs sont disponibles
                    couleur_aleatoire = random.choice(couleurs_disponibles)
                    couleurs_disponibles.remove(couleur_aleatoire)  # Supprime la couleur de la liste
                    ligne_plateau.append(couleur_aleatoire)
        
            self.__plateau.append(ligne_plateau)
        return self.__plateau
    
    def plateau_cache(self, interface):
        """Cache le plateau en le dessinant entièrement en noir."""
        for ligne in range(10):
            for colonne in range(17):
                x = colonne * self.__taille_case  # Coordonnée X du coin supérieur gauche du rectangle
                y = ligne * self.__taille_case  # Coordonnée Y du coin supérieur gauche du rectangle          
                rectangle = pygame.Rect(x, y, self.__taille_case, self.__taille_case)  # Créer un rectangle
                pygame.draw.rect(interface.get_fenetre(), couleur.Couleur().get_Noir(), rectangle)  # Dessiner le rectangle avec la couleur
        interface.get_plateau_de_jeu().mise_a_jour_plateau(interface)
        interface.affiche_tt_joueur()



    def mise_a_jour_plateau(self, interface):
        """Met à jour le plateau en affichant les cases découvertes."""
        font = pygame.font.Font(('./assets/font/Dosis-VariableFont_wght.ttf'), 11)
        for i in self.get_cases_decouvertes():
            couleur_case = self.get_plateau()[i[0]][i[1]]  # Obtenir la couleur de la case
            x = i[1] * self.__taille_case  # Coordonnée X du coin supérieur gauche du rectangle
            y = i[0] * self.__taille_case  # Coordonnée Y du coin supérieur gauche du rectangle          
            rectangle = pygame.Rect(x, y, self.__taille_case, self.__taille_case)  # Créer un rectangle
            pygame.draw.rect(interface.get_fenetre(), couleur_case, rectangle)  # Dessiner le rectangle avec la couleur
            if (self.__nom_case[couleur_case] != "Vide") and (self.__nom_case[couleur_case] != "Mort") and (self.__nom_case[couleur_case] != "Départ/arrivée"):
                texte.Texte(self.__nom_case[couleur_case], couleur.Couleur().get_Noir(), x + 9, y + 15).affiche(font, interface.get_fenetre())

    def Action_couleur_Bleu(self, interface, joueur):
        image.Image(0,468,'assets/img/illustrations/Page_choixdouble.png').affiche(interface.get_fenetre())
        interface.Menu_bas(joueur)
        # Dessiner le rectangle pour les dialogues
        rectangle.Rectangle(100, 590, 390, 80).affiche(interface.get_fenetre(), couleur.Couleur().get_Beige())
        texte.Texte("Tu es tombe dans la case Puit...",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())        
        texte.Texte("Pour t'en sortir, tu dois sacrifier une de",couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())        
        texte.Texte("tes cles ou 200 pv.",couleur.Couleur().get_Noir(),110, 640).affiche(interface.get_police(),interface.get_fenetre())
        pygame.display.update()
        pygame.time.delay(3200)
        
        # Cacher les anciens dialogues
        rectangle.Rectangle(100, 590, 390, 80).affiche(interface.get_fenetre(), couleur.Couleur().get_Beige())
        texte.Texte("Veux-tu sacrifier une de tes cles ou me donner 200 pv",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
        pygame.display.update() # mettre à jour l'affichage
        
        # Afficher les logos et texte des cles et des pv
        pv = pygame.image.load("./assets/img/interraction/Pv.png")
        interface.get_fenetre().blit(pv, (220, 480))
        cles = pygame.image.load("./assets/img/interraction/Cles.png")
        interface.get_fenetre().blit(cles, (510, 480))
        texte.Texte("200 PV",couleur.Couleur().get_Blanc(),235,545).affiche(interface.get_police(),interface.get_fenetre())
        texte.Texte("1 clee",couleur.Couleur().get_Blanc(),525,545).affiche(interface.get_police(),interface.get_fenetre())
        pygame.display.update()
        
        selection_utilisateur = False
        while selection_utilisateur != True:
            mouse_x, mouse_y = pygame.mouse.get_pos() # Recuperer les coordonnees de la souris
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # si le joueur quitte la interface.get_fenetre() # si le joueur quitte la interface.get_fenetre()
                    pygame.quit()
                    exit() 
                
                # Si le clique est presse
                if event.type == pygame.MOUSEBUTTONDOWN:  
                    if 220 < mouse_x < 284 and 480 < mouse_y < 544:
                        
                        # Si le joueur veut echanger des pv
                        if joueur.get_pv() > 200:
                            joueur.supprimer_pv(interface.get_liste_joueur(),200,interface.get_fenetre())                        
                            selection_utilisateur = True
                        else :
                            rectangle.Rectangle(100, 590, 390, 80).affiche(interface.get_fenetre(), couleur.Couleur().get_Beige())
                            texte.Texte("Tu n'as pas de cles, donne moi 200 pv",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
                            pygame.display.update()
                            
                    elif 510 < mouse_x < 574 and 480 < mouse_y < 544:
                        if joueur.get_inventaire() != []:
                            rectangle.Rectangle(500,590,130,35).affiche(interface.get_fenetre(),couleur.Couleur().get_Vert())
                            texte.Texte(joueur.get_pv(),couleur.Couleur().get_Noir(),538,598).affiche(interface.get_police(),interface.get_fenetre())
                            pygame.display.update()
                            selection_utilisateur = True  
                        
                        elif joueur.get_inventaire() == [] and joueur.get_pv() > 200:
                            rectangle.Rectangle(100, 590, 390, 80).affiche(interface.get_fenetre(), couleur.Couleur().get_Beige())
                            texte.Texte("Tu n'as pas de cles, donne moi 200 pv",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
                            pygame.display.update()
                        else :
                            rectangle.Rectangle(500,590,130,35).affiche(interface.get_fenetre(),couleur.Couleur().get_Vert())
                            rectangle.Rectangle(100, 590, 390, 80).affiche(interface.get_fenetre(), couleur.Couleur().get_Beige())
                            joueur.set_pv(0)
                            interface.Mise_a_jour(joueur)
                            texte.Texte(joueur.get_pv(),couleur.Couleur().get_Noir(),538,598).affiche(interface.get_police(),interface.get_fenetre())
                            texte.Texte("Tu n'as pas de cles, ni assez de pv",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())       
                            texte.Texte("Tu es donc condamne à devoir mourrir et arreter",couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())       
                            texte.Texte("la partie ici.",couleur.Couleur().get_Noir(),110, 640).affiche(interface.get_police(),interface.get_fenetre())  
                            pygame.display.update()  
                            selection_utilisateur = True
        
    def Action_couleur_Noir(self, interface, joueur):
        # Dessiner le rectangle pour les dialogues
        rectangle.Rectangle(100, 590, 390, 80).affiche(interface.get_fenetre(), couleur.Couleur().get_Beige())
        texte.Texte("Tu n'as pas de chance...",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
        texte.Texte("Tu es tombe sur la case de Mort...",couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())
        texte.Texte("La partie est finie pour toi.",couleur.Couleur().get_Noir(),110, 640).affiche(interface.get_police(),interface.get_fenetre())
        joueur.supprimer_pv(interface.get_liste_joueur(),joueur.get_pv(),interface.get_fenetre())
        pygame.display.update()
        pygame.time.delay(2000)
        
    def Action_couleur_Orange(self, interface, joueur):
        # Dessiner le rectangle pour les dialogues
        rectangle.Rectangle(100, 590, 390, 80).affiche(interface.get_fenetre(), couleur.Couleur().get_Beige())
        texte.Texte("Tu es sur une case Malus.",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
        texte.Texte("Clique pour savoir quel sort",couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())
        texte.Texte("le jeu te reserve.",couleur.Couleur().get_Noir(),110, 640).affiche(interface.get_police(),interface.get_fenetre())
        pygame.display.update()
        pygame.time.delay(3200)
            
        malus = pygame.image.load("./assets/img/interraction/Malus.png")
        interface.get_fenetre().blit(malus, (360,475))
        texte.Texte("Malus",couleur.Couleur().get_Noir(),372,545).affiche(interface.get_police(),interface.get_fenetre())
        pygame.display.update()

        selection_malus = False
        while selection_malus != True:
            mouse_x, mouse_y = pygame.mouse.get_pos() # Recuperer les coordonnees de la souris
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # si le joueur quitte la interface.get_fenetre() # si le joueur quitte la interface.get_fenetre()
                    pygame.quit()
                    exit() 
                
                # Si le clique est presse
                if event.type == pygame.MOUSEBUTTONDOWN:  
                    if 360 < mouse_x < 424 and 475 < mouse_y < 539:
                        liste_malus = ["perdre 20 pv","perdre 50 pv","perdre 80 pv","perdre 120 pv"]
                        malus = random.choice(liste_malus)
                        rectangle.Rectangle(100, 590, 390, 80).affiche(interface.get_fenetre(), couleur.Couleur().get_Beige())
                        texte.Texte("Tou-dou-dou-doum",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
                        pygame.time.delay(1000)
                        texte.Texte("Tu vas {}".format(malus),couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())
                        if malus == "perdre 20 pv":
                            if joueur.get_pv() > 20:
                                joueur.supprimer_pv(interface.get_liste_joueur(),20,interface.get_fenetre())
                                selection_malus = True
                                
                            else:
                                texte.Texte("Tu n'as plus assez de vie.",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
                                pygame.time.delay(1000)
                                self.Action_couleur_Noir()
                                
                        elif malus == "perdre 50 pv":
                            if joueur.get_pv() > 50:
                                # Definir les nouveaux pv suite à l'echange
                                joueur.supprimer_pv(interface.get_liste_joueur(),50,interface.get_fenetre())
                                selection_malus = True
                                
                            else:
                                texte.Texte("Tu n'as plus assez de vie.",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
                                pygame.time.delay(1000)
                                self.Action_couleur_Noir()
                                
                        elif malus == "perdre 80 pv":
                            if joueur.get_pv() > 80:
                                joueur.supprimer_pv(interface.get_liste_joueur(),80,interface.get_fenetre())
                                selection_malus = True
                                
                            else:
                                texte.Texte("Tu n'as plus assez de vie.",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
                                pygame.time.delay(1000)
                                self.Action_couleur_Noir()
                                
                        elif malus == "perdre 100 pv":
                            if joueur.get_pv() > 100:
                                # Definir les nouveaux pv suite à l'echange
                                joueur.supprimer_pv(interface.get_liste_joueur(),100,interface.get_fenetre())
                                selection_malus = True
                                
                            else:
                                texte.Texte("Tu n'as plus assez de vie.",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
                                pygame.time.delay(1000)
                                self.Action_couleur_Noir()

    def Action_couleur_Rouge(self, interface, joueur):
        if joueur.avoir_tt_cles() != True:
            un_ennemis = ennemis.Choix_ennemis(joueur)
        else:
            # Mettre la interface.get_fenetre() combat
            interface.get_fenetre().fill((couleur.Couleur().get_Noir()))
            image_Arene = pygame.image.load("./assets/img/ennemis/Arene.png")
            image_redimensionnee = pygame.transform.scale(image_Arene, (800, 500))
            interface.get_fenetre().blit(image_redimensionnee, (0, 0))
            interface.Menu_bas(joueur)
            
            #Afficher le joueur et l'adversaire
            interface.affichage_image(100,400,joueur)
                
            # Affiche le texte 
            texte.Texte("Tu as deja combatu tous les boss, deplace-toi ", couleur.Couleur().get_Noir(), 110, 600).affiche(interface.get_police(),interface.get_fenetre())
            texte.Texte("jusqu'à la hutte de la sorciere pour la tuer", couleur.Couleur().get_Noir(), 110, 620).affiche(interface.get_police(),interface.get_fenetre())
            texte.Texte("et recuperer ta taille.", couleur.Couleur().get_Noir(), 110, 640).affiche(interface.get_police(),interface.get_fenetre())
            pygame.display.update()
            pygame.time.delay(3500)
            
            combat_en_cours = False
        # Mettre la interface.get_fenetre() combat
        interface.get_fenetre().fill((couleur.Couleur().get_Noir()))
        image_Arene = pygame.image.load("./assets/img/ennemis/Arene.png")
        image_redimensionnee = pygame.transform.scale(image_Arene, (800, 500))
        interface.get_fenetre().blit(image_redimensionnee, (0, 0))
        interface.Menu_bas(joueur)
        
        #Afficher le joueur et l'adversaire
        interface.affichage_image(100,400,joueur)
        interface.affichage_image_adv(620,400,un_ennemis)
            
        # Affiche le texte 
        texte.Texte("Tu es en combat contre un ennemis feroce. Le celebre ", couleur.Couleur().get_Noir(), 110, 600).affiche(interface.get_police(),interface.get_fenetre())
        texte.Texte("{}. Prepare toi à le combattre afin d'obtenir".format(un_ennemis.get_prenom()), couleur.Couleur().get_Noir(), 110, 620).affiche(interface.get_police(),interface.get_fenetre())
        texte.Texte("la cle {}".format(un_ennemis.get_element()), couleur.Couleur().get_Noir(), 110, 640).affiche(interface.get_police(),interface.get_fenetre())
        pygame.display.update()
        pygame.time.delay(3500)
        
        combat_en_cours = True
        # Tant que l'ennemis est en vie
        while combat_en_cours:
            if joueur.get_pv()>0:
                interface.Menu_bas(joueur)
                interface.affichage_image(100,400,joueur)
                interface.affichage_image_adv(620,400,un_ennemis)
                # Dessiner le rectangle pour les pv du joueur
                texte.Texte("Que veux-tu faire ? Une attaque basique, une ", couleur.Couleur().get_Noir(), 110, 600).affiche(interface.get_police(),interface.get_fenetre())
                texte.Texte("attaque speciale, te defendre ou prendre", couleur.Couleur().get_Noir(), 110, 620).affiche(interface.get_police(),interface.get_fenetre())
                texte.Texte("la fuite ?", couleur.Couleur().get_Noir(), 110, 640).affiche(interface.get_police(),interface.get_fenetre())
                image.Image(100,508,'assets/img/illustrations/Basique.png').affiche(interface.get_fenetre())
                image.Image(250,508,'assets/img/illustrations/Speciale.png').affiche(interface.get_fenetre())
                image.Image(400,508,'assets/img/illustrations/Defense.png').affiche(interface.get_fenetre())
                image.Image(550,508,'assets/img/illustrations/Fuite.png').affiche(interface.get_fenetre())
                pygame.display.update()

            selection_combat = False
            while selection_combat != True:
                mouse_x, mouse_y = pygame.mouse.get_pos() # Recuperer les coordonnees de la souris
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: # si le joueur quitte la interface.get_fenetre() # si le joueur quitte la interface.get_fenetre()
                        pygame.quit()
                        exit() 
                    
                    # Si le clique est presse
                    if event.type == pygame.MOUSEBUTTONDOWN:  
                        if 100 < mouse_x < 164 and 508 < mouse_y < 572:
                            toucher = random.choice([True,False,True])
                            if toucher == True:
                                if joueur.get_element() == un_ennemis.get_element():
                                    #action_joueur = "attaque basique"
                                    pv = random.randint(120,180)
                                    un_ennemis.set_pv(un_ennemis.get_pv()-pv)
                                else:
                                    #action_joueur = "attaque basique"
                                    pv = random.randint(100,140)
                                    un_ennemis.set_pv(un_ennemis.get_pv()-pv)
                                interface.Menu_bas(joueur)
                                interface.affichage_image(100,400,joueur)
                                interface.affichage_image_adv(620,400,un_ennemis)
                                texte.Texte("Tu as choisi de faire une attaque basique,", couleur.Couleur().get_Noir(), 110, 600).affiche(interface.get_police(),interface.get_fenetre())
                                texte.Texte("bravo, l'ennemis a perdu {} pvs".format(pv), couleur.Couleur().get_Noir(), 110, 620).affiche(interface.get_police(),interface.get_fenetre())
                                joueur.set_x(620); joueur.set_y(400)
                                pygame.display.update()
                                pygame.time.delay(2000)
                                joueur.set_x(100); joueur.set_y(400)
                                selection_combat = True
                            else:
                                interface.Menu_bas(joueur)
                                interface.affichage_image(100,400,joueur)
                                interface.affichage_image_adv(620,400,un_ennemis)
                                texte.Texte("L'ennemis a esquive le coup, dommage", couleur.Couleur().get_Noir(), 110, 600).affiche(interface.get_police(),interface.get_fenetre())
                                texte.Texte("L'ennemis n'a pas perdu de pv", couleur.Couleur().get_Noir(), 110, 620).affiche(interface.get_police(),interface.get_fenetre())
                                pygame.display.update()
                                pygame.time.delay(2000)
                                selection_combat = True
                        if 250 < mouse_x < 314 and 508 < mouse_y < 572:
                            #action_joueur = "attaque speciale"
                            toucher = random.choice([True,False])
                            if toucher == True:
                                pv = 187
                                un_ennemis.set_pv(un_ennemis.get_pv()-pv)
                                interface.Menu_bas(joueur)
                                interface.affichage_image(100,400,joueur)
                                interface.affichage_image_adv(620,400,un_ennemis)
                                texte.Texte("Tu as choisi de faire une attaque speciale,", couleur.Couleur().get_Noir(), 110, 600).affiche(interface.get_police(),interface.get_fenetre())
                                texte.Texte("bravo, l'ennemis a perdu {} pvs".format(pv), couleur.Couleur().get_Noir(), 110, 620).affiche(interface.get_police(),interface.get_fenetre())
                                joueur.set_x(620); joueur.set_y(400)
                                pygame.display.update()
                                pygame.time.delay(2000)
                                joueur.set_x(100); joueur.set_y(400)
                                selection_combat = True
                            else:
                                interface.Menu_bas(joueur)
                                interface.affichage_image(100,400,joueur)
                                interface.affichage_image_adv(620,400,un_ennemis)
                                texte.Texte("L'ennemis a esquive le coup, dommage", couleur.Couleur().get_Noir(), 110, 600).affiche(interface.get_police(),interface.get_fenetre())
                                texte.Texte("L'ennemis n'a pas perdu de pv", couleur.Couleur().get_Noir(), 110, 620).affiche(interface.get_police(),interface.get_fenetre())
                                pygame.display.update()
                                pygame.time.delay(2000)
                                selection_combat = True
                        if 400 < mouse_x < 464 and 508 < mouse_y < 572:
                            #action_joueur = "se defendre"
                            toucher = random.choice([True,False])
                            if toucher == True:
                                un_ennemis.set_attaque(un_ennemis.get_attaque()-20)
                                interface.Menu_bas(joueur)
                                interface.affichage_image(100,400,joueur)
                                interface.affichage_image_adv(620,400,un_ennemis)
                                texte.Texte("Tu as choisi de te defendre, tu fais une", couleur.Couleur().get_Noir(), 110, 600).affiche(interface.get_police(),interface.get_fenetre())
                                texte.Texte("grimace au boss et cela reduit les degâts", couleur.Couleur().get_Noir(), 110, 620).affiche(interface.get_police(),interface.get_fenetre())
                                texte.Texte("qu'il peut t'infliger." ,couleur.Couleur().get_Noir(), 110, 640).affiche(interface.get_police(),interface.get_fenetre())
                                joueur.set_x(620); joueur.set_y(400)
                                pygame.display.update()
                                pygame.time.delay(2000)
                                joueur.set_x(100); joueur.set_y(400)
                                selection_combat = True
                            else:
                                interface.Menu_bas(joueur)
                                interface.affichage_image(100,400,joueur)
                                interface.affichage_image_adv(620,400,un_ennemis)
                                texte.Texte("L'ennemis n'a pas pris peur, les", couleur.Couleur().get_Noir(), 110, 600).affiche(interface.get_police(),interface.get_fenetre())
                                texte.Texte("degâts qu'il t'inflige ne sont pas", couleur.Couleur().get_Noir(), 110, 620).affiche(interface.get_police(),interface.get_fenetre())
                                texte.Texte("reduits.", couleur.Couleur().get_Noir(), 110, 640).affiche(interface.get_police(),interface.get_fenetre())
                                pygame.display.update()
                                pygame.time.delay(2000)
                                selection_combat = True
                        if 550 < mouse_x < 614 and 508 < mouse_y < 572:
                            #action_joueur = "prendre la fuite"
                            interface.Menu_bas(joueur)
                            interface.affichage_image(100,400,joueur)
                            interface.affichage_image_adv(620,400,un_ennemis)    
                            texte.Texte("Tu as choisi de prendre la fuite, c'est", couleur.Couleur().get_Noir(), 110, 600).affiche(interface.get_police(),interface.get_fenetre())
                            texte.Texte("surement le bon choix retente ta chance plus", couleur.Couleur().get_Noir(), 110, 620).affiche(interface.get_police(),interface.get_fenetre())
                            texte.Texte("tard et detruit moi ce BOSS !!!" ,couleur.Couleur().get_Noir(), 110, 640).affiche(interface.get_police(),interface.get_fenetre())
                            pygame.display.update()
                            pygame.time.delay(2000)
                            un_ennemis.set_pv(0)
                            interface.get_liste_joueur()[joueur.get_id()][5] = joueur.get_pv()
                            selection_combat = True; combat_en_cours =False
            if un_ennemis.get_pv()>0 and joueur.get_pv()>0:
                interface.Menu_bas(joueur)
                interface.affichage_image(100,400,joueur)
                interface.affichage_image_adv(620,400,un_ennemis)
                toucher = random.choice([True,False])
                if toucher == True:
                    pv = random.randint(un_ennemis.get_attaque(),un_ennemis.get_attaque() + 10)
                    joueur.set_pv(joueur.get_pv() - pv)
                    texte.Texte("Il te fais perdre {} pvs.".format(pv),couleur.Couleur().get_Noir(),110, 640).affiche(interface.get_police(),interface.get_fenetre())
                else:
                    texte.Texte("L'ennemi a rate son coup.",couleur.Couleur().get_Noir(),110, 640).affiche(interface.get_police(),interface.get_fenetre())
                interface.Menu_bas(joueur)
                interface.affichage_image(100,400,joueur)
                interface.affichage_image_adv(620,400,un_ennemis)
                texte.Texte("C'est au tour du boss d'attaquer",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
                texte.Texte("Le boss reflechit...",couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())
                un_ennemis.set_x(100); un_ennemis.set_y(400)
                pygame.display.update()
                pygame.time.delay(2000)
                un_ennemis.set_x(620); un_ennemis.set_y(400)
            elif joueur.get_pv()<=0:
                interface.get_liste_joueur()[joueur.get_id()][5] = joueur.get_pv()
                interface.Menu_bas(joueur)
                interface.affichage_image(100,400,joueur)
                interface.affichage_image_adv(620,400,un_ennemis)
                texte.Texte("Fin du combat... Tu n'as pas survecu",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
                texte.Texte("à l'attaque du boss...",couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())
                texte.Texte("Retour au plateau !",couleur.Couleur().get_Noir(),110, 640).affiche(interface.get_police(),interface.get_fenetre())
                pygame.display.update()
                pygame.time.delay(1500)
                combat_en_cours = False
                selection_combat = True
            elif un_ennemis.get_pv()<=0 and joueur.get_pv()>=0 and joueur.avoir_tt_cles() != True:
                interface.get_liste_joueur()[joueur.get_id()][5] = joueur.get_pv()
                interface.Menu_bas(joueur)
                interface.affichage_image(100,400,joueur)
                interface.affichage_image_adv(620,400,un_ennemis)
                texte.Texte("Fin du combat ! Bravo tu as vaincu le boss",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
                texte.Texte("{}, recupere les autres cles en tuant les".format(un_ennemis.get_element()),couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())
                texte.Texte("autres boss et detruit cette sorciere !!!",couleur.Couleur().get_Noir(),110, 640).affiche(interface.get_police(),interface.get_fenetre())
                joueur.set_inventaire(joueur.get_inventaire() + ["cle " + un_ennemis.get_element()])
                interface.get_liste_joueur()[joueur.get_id()][6] = joueur.get_inventaire() 
                interface.affichage_cle(joueur)           
                pygame.display.update()
                pygame.time.delay(1500)
                combat_en_cours =False
                selection_combat = True
            elif un_ennemis.get_pv()<=0 and joueur.get_pv()>=0 and joueur.avoir_tt_cles() == True:
                interface.get_liste_joueur()[joueur.get_id()][5] = joueur.get_pv()
                interface.Menu_bas(joueur)
                interface.affichage_image(100,400,joueur)
                interface.affichage_image_adv(620,400,un_ennemis)
                texte.Texte("Fin du combat ! Bravo tu as vaincu le boss",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
                texte.Texte("{}, en plus de ça tu as toutes les cles, depeche ".format(un_ennemis.get_element()),couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())
                texte.Texte("toi pour etre le premier à tuer la sorciere !!!",couleur.Couleur().get_Noir(),110, 640).affiche(interface.get_police(),interface.get_fenetre())
                joueur.set_inventaire(joueur.get_inventaire() + ["cle " + un_ennemis.get_element()])
                interface.get_liste_joueur()[joueur.get_id()][6] = joueur.get_inventaire() 
                interface.affichage_cle(joueur)           
                pygame.display.update()
                pygame.time.delay(1500)
                combat_en_cours =False
                selection_combat = True
            
    def Action_couleur_Rose(self, interface, joueur):
        # Dessiner le rectangle pour les dialogues
        rectangle.Rectangle(100, 590, 390, 80).affiche(interface.get_fenetre(), couleur.Couleur().get_Beige())
        texte.Texte("Tu es sur une case Chance",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
        texte.Texte("Clique pour decouvrir le pouvoir",couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())
        texte.Texte("que le jeu va te donner.",couleur.Couleur().get_Noir(),110, 640).affiche(interface.get_police(),interface.get_fenetre())
        pygame.display.update()
        pygame.time.delay(3200)
        
        chance = pygame.image.load("./assets/img/interraction/Chance.png")
        interface.get_fenetre().blit(chance, (360,475))
        texte.Texte("Chance",couleur.Couleur().get_Noir(),369,545).affiche(interface.get_police(),interface.get_fenetre())
        pygame.display.update()

        selection_malus = False
        while selection_malus != True:
            mouse_x, mouse_y = pygame.mouse.get_pos() # Recuperer les coordonnees de la souris
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # si le joueur quitte la interface.get_fenetre() # si le joueur quitte la interface.get_fenetre()
                    pygame.quit()
                    exit() 
                
                # Si le clique est presse
                if event.type == pygame.MOUSEBUTTONDOWN:  
                    if 360 < mouse_x < 424 and 475 < mouse_y < 539:
                        liste_chance = ["gagner 100 pv","gagner 200 pv","gagner 500 pv", "gagner 150 pv","gagner 400 pv","gagner 1050 pv"]
                        chance = random.choice(liste_chance)
                        rectangle.Rectangle(100, 590, 390, 80).affiche(interface.get_fenetre(), couleur.Couleur().get_Beige())
                        texte.Texte("Tou-dou-dou-doum",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
                        pygame.time.delay(1000)
                        texte.Texte("Tu vas {}".format(chance),couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())
                        # Definir les nouveaux pv suite à l'echange
                        if chance == "gagner 100 pv":
                            joueur.ajouter_pv(interface.get_liste_joueur(),100,interface.get_fenetre())
                            selection_malus = True
                            
                        elif chance == "gagner 200 pv":
                            joueur.ajouter_pv(interface.get_liste_joueur(),200,interface.get_fenetre())
                            selection_malus = True
                            
                        elif chance == "gagner 500 pv":
                            joueur.ajouter_pv(interface.get_liste_joueur(),500,interface.get_fenetre())
                            selection_malus = True
                            
                        elif chance == "gagner 150 pv":
                            joueur.ajouter_pv(interface.get_liste_joueur(),150,interface.get_fenetre())
                            selection_malus = True
                            
                        elif chance == "gagner 300 pv":
                            joueur.ajouter_pv(interface.get_liste_joueur(),300,interface.get_fenetre())
                            selection_malus = True
                            
                        elif chance == "gagner 1050 pv":
                            joueur.ajouter_pv(interface.get_liste_joueur(),1050,interface.get_fenetre())
                            selection_malus = True
                                                                                   
                
    def Action_couleur_Gris(self, interface, joueur):
        # Dessiner le rectangle pour les dialogues
        rectangle.Rectangle(100, 590, 390, 80).affiche(interface.get_fenetre(), couleur.Couleur().get_Beige())
        texte.Texte("Tu es sur une case Speciale ! Si tu tente",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
        texte.Texte("ta chance, tu as une chance sur deux gagner",couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())
        texte.Texte("deux cles que tu n'as pas ou de tout perdre.",couleur.Couleur().get_Noir(),110, 640).affiche(interface.get_police(),interface.get_fenetre())  
        pygame.display.update()
        pygame.time.delay(3200)
        
        # Cacher les anciens dialogues
        image.Image(0,468,'assets/img/illustrations/Page_choixdouble.png').affiche(interface.get_fenetre())
        interface.Menu_bas(joueur)
        rectangle.Rectangle(100, 590, 390, 80).affiche(interface.get_fenetre(), couleur.Couleur().get_Beige())
        texte.Texte("Veux-tu sacrifier une de tes cles afin de lancer le",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
        texte.Texte("tirage pour savoir si tu as la chance de gagner",couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())
        texte.Texte("deux cles que tu n'as pas",couleur.Couleur().get_Noir(),110, 640).affiche(interface.get_police(),interface.get_fenetre())
        pygame.display.update() # mettre à jour l'affichage
        
        # Afficher les logos et texte des cles et des pv
        cles = pygame.image.load("./assets/img/interraction/Cles.png")
        interface.get_fenetre().blit(cles, (220, 480))
        retour = pygame.image.load("./assets/img/interraction/Retour.png")
        interface.get_fenetre().blit(retour, (510,480))
        texte.Texte("1 clee",couleur.Couleur().get_Blanc(),215,545).affiche(interface.get_police(),interface.get_fenetre())
        
        texte.Texte("Passer son tour",couleur.Couleur().get_Blanc(),505,545).affiche(interface.get_police(),interface.get_fenetre())
        pygame.display.update() # mettre à jour l'affichage
        
        selection_speciale = False
        while selection_speciale != True:
            mouse_x, mouse_y = pygame.mouse.get_pos() # Recuperer les coordonnees de la souris
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # si le joueur quitte la interface.get_fenetre() # si le joueur quitte la interface.get_fenetre()
                    pygame.quit()
                    exit() 
                
                # Si le clique est presse
                if event.type == pygame.MOUSEBUTTONDOWN:  
                    if 220 < mouse_x < 284 and 480 < mouse_y < 544:
                    
                        # Si le joueur veut gagner la recompence
                        if joueur.get_inventaire() != []:    
                            choix_tirage = ["bravo", "oh non dommage"] 
                            tirage = random.choice(choix_tirage)   
                            if tirage == "bravo":
                                # Cacher les anciens dialogues
                                rectangle.Rectangle(100, 590, 390, 80).affiche(interface.get_fenetre(), couleur.Couleur().get_Beige())
                                texte.Texte("Bravo tu as gagner !!!",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
                                texte.Texte("Voilà deux cles supplementaires que tu peux",couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())
                                texte.Texte("voir apparaître dans ton inventaire.",couleur.Couleur().get_Noir(),110, 640).affiche(interface.get_police(),interface.get_fenetre())
                                
                                pygame.display.update() # Mettre à jour l'affichage    
                                selection_speciale = True
                                
                            
                            else:
                                # Cacher les anciens dialogues
                                rectangle.Rectangle(100, 590, 390, 80).affiche(interface.get_fenetre(), couleur.Couleur().get_Beige())
                                texte.Texte("Oh non dommage...",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
                                texte.Texte("Tu peux retenter ta chance si tu as",couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())
                                texte.Texte("d'autres cles :)",couleur.Couleur().get_Noir(),110, 640).affiche(interface.get_police(),interface.get_fenetre())
                                
                                pygame.display.update() # Mettre à jour l'affichage  
                                selection_speciale = True
                                
                        else:
                            # Cacher les anciens dialogues
                            rectangle.Rectangle(100, 590, 390, 80).affiche(interface.get_fenetre(), couleur.Couleur().get_Beige())
                            texte.Texte("Tu ne possede pas de cles.",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
                            texte.Texte("Obtient-en une en tuant un boss sur les",couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())
                            texte.Texte("cases rouges.",couleur.Couleur().get_Noir(),110, 640).affiche(interface.get_police(),interface.get_fenetre())
                            
                            pygame.display.update() # Mettre à jour l'affichage  
                            selection_speciale = True    
                            
                    elif 510 < mouse_x < 574 and 480 < mouse_y < 544:
                        # Si le joueur veut passer sont tour
                        # Cacher les anciens dialogues
                        rectangle.Rectangle(100, 590, 390, 80).affiche(interface.get_fenetre(), couleur.Couleur().get_Beige())
                        texte.Texte("Pas de soucis, retente ta chance une autre fois",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
                        pygame.display.update() # Mettre à jour l'affichage 
                        selection_speciale = True
                        
                
    def Action_couleur_Violet(self, interface, joueur):
        # Dessiner le rectangle pour les dialogues
        rectangle.Rectangle(100, 590, 390, 80).affiche(interface.get_fenetre(), couleur.Couleur().get_Beige())
        texte.Texte("Tu es sur une case Rejoue !",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
        texte.Texte("Relance le de pour avoir un",couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())
        texte.Texte("deuxieme lance",couleur.Couleur().get_Noir(),110, 640).affiche(interface.get_police(),interface.get_fenetre())
        pygame.display.update()
        pygame.time.delay(3200)
        
        # Cacher les anciens dialogues
        rectangle.Rectangle(100, 590, 390, 80).affiche(interface.get_fenetre(), couleur.Couleur().get_Beige())
        de_face1 = pygame.image.load("./assets/img/de/Face1.png")
        interface.get_fenetre().blit(de_face1,(350,475))
        texte.Texte("Clique sur le de ! ",couleur.Couleur().get_Noir(),110,600).affiche(interface.get_police(),interface.get_fenetre())
        pygame.display.update()    
        interface.Page_direction(joueur)
        interface.Mise_a_jour(joueur)
        interface.get_plateau_de_jeu().plateau_cache(interface)
        interface.Page_action(joueur)

    def Action_couleur_Beige(self, interface, joueur):
        image.Image(0,468,'assets/img/illustrations/Page_choixdouble.png').affiche(interface.get_fenetre())
        interface.Menu_bas(joueur)
        # Dessiner le rectangle pour les dialogues
        rectangle.Rectangle(100, 590, 390, 80).affiche(interface.get_fenetre(), couleur.Couleur().get_Beige())
        texte.Texte("Tu es devant la Hutte de la sorciere.",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
        texte.Texte("Veux-tu essayer de l'ouvrir à l'aide",couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())
        texte.Texte("des cles des quatre boss ?",couleur.Couleur().get_Noir(),110, 640).affiche(interface.get_police(),interface.get_fenetre())
        pygame.display.update()
        pygame.time.delay(3200)
        
        # Afficher les logos et texte des cles et des pv
        pv = pygame.image.load("./assets/img/interraction/Cles.png")
        interface.get_fenetre().blit(pv, (220, 480))
        retour = pygame.image.load("./assets/img/interraction/Retour.png")
        interface.get_fenetre().blit(retour, (510,480))
        texte.Texte("Ouvrir la porte",couleur.Couleur().get_Blanc(),212,545).affiche(interface.get_police(),interface.get_fenetre())
        texte.Texte("Passer son chemin",couleur.Couleur().get_Blanc(),485,545).affiche(interface.get_police(),interface.get_fenetre())
        pygame.display.update()
        
        selection_sorciere = False
        while selection_sorciere != True:
            mouse_x, mouse_y = pygame.mouse.get_pos() # Recuperer les coordonnees de la souris
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # si le joueur quitte la interface.get_fenetre() # si le joueur quitte la interface.get_fenetre()
                    pygame.quit()
                    exit() 
                
                # Si le clique est presse
                if event.type == pygame.MOUSEBUTTONDOWN:  
                    if 220 < mouse_x < 284 and 480 < mouse_y < 544:
                        if joueur.avoir_tt_cles() == True:
                            # Cacher les anciens dialogues
                            rectangle.Rectangle(100, 590, 390, 80).affiche(interface.get_fenetre(), couleur.Couleur().get_Beige())
                            texte.Texte("Bravo tu as trouve toutes les cles",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
                            texte.Texte("Ouvre la porte et apprete toi à",couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())
                            texte.Texte("affronter la sorciere.",couleur.Couleur().get_Noir(),110, 640).affiche(interface.get_police(),interface.get_fenetre())
                            pygame.display.update() # Mettre à jour l'affichage 
                            selection_sorciere = True
                        else:
                            # Cacher les anciens dialogues
                            rectangle.Rectangle(100, 590, 390, 80).affiche(interface.get_fenetre(), couleur.Couleur().get_Beige())
                            texte.Texte("Tu n'as pas encore recuperer toutes",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
                            texte.Texte("les cles afin d'ouvrir la porte de",couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())
                            texte.Texte("la sorciere. Depeche-toi !",couleur.Couleur().get_Noir(),110, 640).affiche(interface.get_police(),interface.get_fenetre())
                            pygame.display.update() # Mettre à jour l'affichage 
                            selection_sorciere = True
                        
                    elif 510 < mouse_x < 574 and 480 < mouse_y < 544:
                        # Si le joueur veut passer sont tour
                        # Cacher les anciens dialogues
                        rectangle.Rectangle(100, 590, 390, 80).affiche(interface.get_fenetre(), couleur.Couleur().get_Beige())
                        texte.Texte("Pas de soucis, recupere les cles afin",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
                        texte.Texte("d'ouvrir la porte en premier !",couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())
                        pygame.display.update() # Mettre à jour l'affichage 
                        selection_sorciere = True

    def Action_couleur_Indigo(self, interface, joueur):
        image.Image(0,468,'assets/img/illustrations/Page_choixdouble.png').affiche(interface.get_fenetre())
        interface.Menu_bas(joueur)
        # Dessiner le rectangle pour les dialogues
        rectangle.Rectangle(100, 590, 390, 80).affiche(interface.get_fenetre(), couleur.Couleur().get_Beige())
        texte.Texte("Tu es sur une case de Teleportation.",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
        texte.Texte("Veux-tu etre teleporter ?",couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())
        
        
        # Afficher les logos et texte des cles et des pv
        pv = pygame.image.load("./assets/img/interraction/Teleportation.png")
        interface.get_fenetre().blit(pv, (220, 480))
        retour = pygame.image.load("./assets/img/interraction/Retour.png")
        interface.get_fenetre().blit(retour, (510,480))
        texte.Texte("Se teleporter",couleur.Couleur().get_Blanc(),212,545).affiche(interface.get_police(),interface.get_fenetre())
        texte.Texte("Non merci",couleur.Couleur().get_Blanc(),502,545).affiche(interface.get_police(),interface.get_fenetre())
        pygame.display.update()
        pygame.time.delay(3200)
        
        selection_teleporte = False
        while selection_teleporte != True:
            mouse_x, mouse_y = pygame.mouse.get_pos() # Recuperer les coordonnees de la souris
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # si le joueur quitte la interface.get_fenetre() # si le joueur quitte la interface.get_fenetre()
                    pygame.quit()
                    exit() 
                
                # Si le clique est presse
                if event.type == pygame.MOUSEBUTTONDOWN:  
                    if 220 < mouse_x < 284 and 480 < mouse_y < 544:
                        # Cacher les anciens dialogues
                        rectangle.Rectangle(100, 590, 390, 80).affiche(interface.get_fenetre(), couleur.Couleur().get_Beige())
                        texte.Texte("Tou-dou-dou-doum",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
                        texte.Texte("Teleportation sur la deuxieme case",couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())
                        texte.Texte("de teleportation" ,couleur.Couleur().get_Noir(),110, 640).affiche(interface.get_police(),interface.get_fenetre())
                        
                        pygame.display.update() # Mettre à jour l'affichage 
                        coord_case_indigo = interface.get_plateau_de_jeu().get_case_indigo(joueur)
                        joueur.set_plateaux(coord_case_indigo[0])
                        joueur.set_plateauy(coord_case_indigo[1])
                        interface.Mise_a_jour(joueur)
                        selection_teleporte = True
                        
                        
                    elif 510 < mouse_x < 574 and 480 < mouse_y < 544:
                        # Si le joueur veut passer sont tour
                        # Cacher les anciens dialogues
                        rectangle.Rectangle(100, 590, 390, 80).affiche(interface.get_fenetre(), couleur.Couleur().get_Beige())
                        texte.Texte("Pas de soucis, essaye une prochaine",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
                        texte.Texte("fois si tu en as l'envie.",couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())
                        
                        pygame.display.update() # Mettre à jour l'affichage 
                        selection_teleporte = True
        
    def Action_couleur_Turquoise(self, interface):
        # Dessiner le rectangle pour les dialogues
        rectangle.Rectangle(100, 590, 390, 80).affiche(interface.get_fenetre(), couleur.Couleur().get_Beige())
        texte.Texte("Tu es sur une case Grrr",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
        texte.Texte("Un tremblement de terre surgit de nul part",couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())
        texte.Texte("et teleporte tous les joueurs !!!",couleur.Couleur().get_Noir(),110, 640).affiche(interface.get_police(),interface.get_fenetre())
        pygame.display.update()
        pygame.time.delay(1000)
        
        for i in interface.get_liste_joueur():
            i[3] = random.randint(0,9)
            i[4] = random.randint(0,16)
            interface.get_plateau_de_jeu().set_cases_decouvertes(interface.get_plateau_de_jeu().get_cases_decouvertes() + [[i[3],i[4]]])
        pygame.display.update()
        