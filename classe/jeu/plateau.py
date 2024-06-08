# ----------------------- Jeu de plateau - Plateau  ------------------------ #

# Bibliothèques utilisées pour le code
import pygame, random
from classe.visuel import texte, couleur, rectangle, image
from classe.jeu import interfaces
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
        for ligne in range(10):
            for colonne in range(17):
                self.__cases_decouvertes.append((ligne, colonne))
        
        self.remplir_plateau_aleatoirement()
        

    def get_plateau(self):
        """Renvoie le plateau de jeu."""
        return self.__plateau
    def get_nom_case(self):
        """Renvoie le nom_case de jeu."""
        return self.__nom_case
    
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
    


    def Action_couleur_Bleu(self, interface, joueur):
        image.Image(0,468,image.Page.CHOIX_DOUBLE.value).affiche(interface.get_fenetre())
        interface.Menu_bas(joueur)
        # Dessiner le rectangle pour les dialogues
        interface.Menu_bas(joueur)
        texte.Texte("Tu es tombe dans la case Puit... Pour t'en",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())        
        texte.Texte("sortir, tu dois sacrifier une de tes cles",couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())        
        texte.Texte("ou 200 pv.",couleur.Couleur().get_Noir(),110, 640).affiche(interface.get_police(),interface.get_fenetre())
        
        # Afficher les logos et texte des cles et des pv
        pv = image.Interaction.PV.value
        interface.get_fenetre().blit(pv, (220, 480))
        cles = image.Interaction.CLES.value
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
                            interface.Menu_bas(joueur)
                            texte.Texte("Tu n'as pas de cles, donne moi 200 pv",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
                            pygame.display.update()
                            
                    elif 510 < mouse_x < 574 and 480 < mouse_y < 544:
                        if joueur.get_inventaire() != []:
                            rectangle.Rectangle(500,590,130,35).affiche(interface.get_fenetre(),couleur.Couleur().get_Vert())
                            texte.Texte(joueur.get_pv(),couleur.Couleur().get_Noir(),538,598).affiche(interface.get_police(),interface.get_fenetre())
                            pygame.display.update()
                            selection_utilisateur = True  
                        
                        elif joueur.get_inventaire() == [] and joueur.get_pv() > 200:
                            interface.Menu_bas(joueur)
                            texte.Texte("Tu n'as pas de cles, donne moi 200 pv",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
                            pygame.display.update()
                        else :
                            rectangle.Rectangle(500,590,130,35).affiche(interface.get_fenetre(),couleur.Couleur().get_Vert())
                            interface.Menu_bas(joueur)
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
        interface.set_dialogues(["Tu n'as pas de chance...", "Tu es tombe sur la case de Mort...", "La partie est finie pour toi."])
        interface.draw_dialogues()
        
        joueur.set_pv(0)
        interface.Mise_a_jour(joueur)
        pygame.display.update()
        
    def Action_couleur_Orange(self, interface, joueur):
        # Dessiner le rectangle pour les dialogues
        interface.Menu_bas(joueur)
        interface.set_dialogues(["Tu es sur une case Malus.", "Clique pour savoir quel sort", "le jeu te reserve."])
        interface.draw_dialogues()
            
        malus = image.Interaction.MALUS.value
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
                        dias = ["Tou-dou-dou-doum"]
                        if malus == "perdre 20 pv":
                            if joueur.get_pv() > 20:
                                joueur.supprimer_pv(interface.get_liste_joueur(),20,interface.get_fenetre())
                                selection_malus = True
                                
                                dias[0] = "Tu vas {}".format(malus)
                            else:
                                dias[0] = "Tu n'as plus assez de vie."
                                interface.set_dialogues(dias)
                                interface.draw_dialogues()
                                self.Action_couleur_Noir()
                                
                        elif malus == "perdre 50 pv":
                            if joueur.get_pv() > 50:
                                # Definir les nouveaux pv suite à l'echange
                                joueur.supprimer_pv(interface.get_liste_joueur(),50,interface.get_fenetre())
                                selection_malus = True
                                dias[0] = "Tu vas {}".format(malus)
                                
                            else:
                                dias[0] = "Tu n'as plus assez de vie."
                                interface.set_dialogues(dias)
                                interface.draw_dialogues()
                                self.Action_couleur_Noir()
                                
                        elif malus == "perdre 80 pv":
                            if joueur.get_pv() > 80:
                                joueur.supprimer_pv(interface.get_liste_joueur(),80,interface.get_fenetre())
                                selection_malus = True
                                dias[0] = "Tu vas {}".format(malus)
                                
                            else:
                                dias[0] = "Tu n'as plus assez de vie."
                                interface.set_dialogues(dias)
                                interface.draw_dialogues()
                                self.Action_couleur_Noir()
                                
                        elif malus == "perdre 100 pv":
                            if joueur.get_pv() > 100:
                                # Definir les nouveaux pv suite à l'echange
                                joueur.supprimer_pv(interface.get_liste_joueur(),100,interface.get_fenetre())
                                selection_malus = True
                                dias[0] = "Tu vas {}".format(malus)
                                
                            else:
                                dias[0] = "Tu n'as plus assez de vie."
                                interface.set_dialogues(dias)
                                interface.draw_dialogues()
                                self.Action_couleur_Noir()
                        
                        interface.set_dialogues(dias)
                        interface.draw_dialogues()

    def Action_couleur_Rouge(self, interface, joueur):
        if joueur.avoir_tt_cles() != True:
            un_ennemis = ennemis.Choix_ennemis(joueur)
            # Mettre la fenetre combat
            interface.get_fenetre().fill((couleur.Couleur().get_Noir()))
            image_Arene = image.Page.ARENE.value
            image_redimensionnee = pygame.transform.scale(image_Arene, (800, 500))
            interface.get_fenetre().blit(image_redimensionnee, (0, 0))
                
            #Afficher le joueur et l'adversaire
            interface.Menu_bas(joueur)
            interface.affichage_image(100,400,joueur)
            interface.affichage_image_adv(620,400,un_ennemis)
                
            # Affiche le texte 
            
            interface.set_dialogues(["Tu as décidé de combattre un joueur. Le celebre ","{}. Prepare toi à le combattre afin de prendre".format(un_ennemis.get_prenom()), "l'avantage sur lui !"])
            interface.draw_dialogues()
            pygame.display.update()
            pygame.time.delay(2500)

            interface.get_fenetre().fill((couleur.Couleur().get_Noir()))
            image_Arene = image.Page.ARENE.value
            image_redimensionnee = pygame.transform.scale(image_Arene, (800, 500))
            interface.get_fenetre().blit(image_redimensionnee, (0, 0))
            interface.Menu_bas(joueur)
            interface.affichage_image(100, 400, joueur)
            interface.affichage_image_adv(620, 400, un_ennemis)
            interface.set_dialogues(["Que veux-tu faire ? Une attaque basique, une ","attaque speciale, te defendre ou prendre", "la fuite ?"])
            interface.draw_dialogues()
            image.Image(100, 508, image.BtnAttaque.BASIQUE.value).affiche(interface.get_fenetre())
            image.Image(250, 508, image.BtnAttaque.SPECIALE.value).affiche(interface.get_fenetre())
            image.Image(400, 508, image.BtnAttaque.DEFENSE.value).affiche(interface.get_fenetre())
            image.Image(550, 508, image.BtnAttaque.FUITE.value).affiche(interface.get_fenetre())
            pygame.display.update()
            combat_en_cours = True
        else:
            # Mettre la interface.get_fenetre() combat
            interface.get_fenetre().fill((couleur.Couleur().get_Noir()))
            image_Arene = image.Page.ARENE.value
            image_redimensionnee = pygame.transform.scale(image_Arene, (800, 500))
            interface.get_fenetre().blit(image_redimensionnee, (0, 0))
            interface.Menu_bas(joueur)
            
            #Afficher le joueur et l'adversaire
            interface.affichage_image(100,400,joueur)
                
            # Affiche le texte 
            interface.set_dialogues(["Tu as deja combatu tous les boss, deplace-toi ","jusqu'à la hutte de la sorciere pour la tuer", "et recuperer ta taille."])
            interface.draw_dialogues()
            pygame.display.update()
            combat_en_cours = False
        while combat_en_cours:
            if joueur.get_pv() <= 0:
                joueur.set_pv(0)
                interface.Menu_bas(joueur)
                interface.affichage_image_adv(620, 400, un_ennemis)
                interface.set_dialogues(["Fin du combat... Tu n'as pas survecu","à l'attaque du boss...", "Retour au plateau !"])
                interface.draw_dialogues()
                interface.Mise_a_jour(joueur)
                pygame.display.update()
                combat_en_cours = False
            elif un_ennemis.get_pv() <= 0:
                if joueur.avoir_tt_cles() != True:
                    joueur.set_inventaire(joueur.get_inventaire() + ["cle " + un_ennemis.get_element()])
                    interface.Menu_bas(joueur)
                    interface.affichage_image(100, 400, joueur)
                    interface.set_dialogues(["Fin du combat... Tu n'as pas survecu","{}, recupere les autres cles en tuant les","autres boss et detruit cette sorciere !!!"])
                    interface.draw_dialogues()
                else:
                    joueur.set_inventaire(joueur.get_inventaire() + ["cle " + un_ennemis.get_element()])
                    interface.Menu_bas(joueur)
                    interface.affichage_image(100, 400, joueur)
                    interface.set_dialogues(["Fin du combat... Tu n'as pas survecu","{}, en plus de ça tu as toutes les cles, depeche ","toi pour etre le premier à tuer la sorciere !!!"])
                    interface.draw_dialogues()
                interface.Mise_a_jour(joueur)
                pygame.display.update()
                combat_en_cours = False
            elif joueur.get_pv() > 0 and un_ennemis.get_pv() > 0:
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
                                    un_ennemis.set_pv(un_ennemis.get_pv()-pv)
                                else:
                                    pv = random.randint(joueur.get_attaque()-20,joueur.get_attaque())
                                    un_ennemis.set_pv(un_ennemis.get_pv()-pv)
                                interface.Menu_bas(joueur)
                                interface.affichage_image(100,400,joueur)
                                interface.affichage_image_adv(620,400,un_ennemis)
                                interface.set_dialogues(["Tu as choisi de faire une attaque basique,","bravo, l'adversaire a perdu {} pvs".format(pv)])
                                interface.draw_dialogues()
                            else:
                                interface.Menu_bas(joueur)
                                interface.affichage_image(100,400,joueur)
                                interface.affichage_image_adv(620,400,un_ennemis)
                                interface.set_dialogues(["L'adversaire a esquive le coup, dommage","L'adversaire n'a pas perdu de pv"])
                                interface.draw_dialogues()
                        elif 250 < mouse_x < 314 and 508 < mouse_y < 572:
                            #action_joueur = "attaque speciale"
                            toucher = random.choice([True,False])
                            if toucher == True:
                                pv = joueur.get_attaque()+50
                                un_ennemis.set_pv(un_ennemis.get_pv()-pv)
                                interface.Menu_bas(joueur)
                                interface.affichage_image(100,400,joueur)
                                interface.affichage_image_adv(620,400,un_ennemis)
                                interface.set_dialogues(["Tu as choisi de faire une attaque speciale,","bravo, l'adversaire a perdu {} pvs"])
                                interface.draw_dialogues()
                            else:
                                interface.Menu_bas(joueur)
                                interface.affichage_image(100,400,joueur)
                                interface.affichage_image_adv(620,400,un_ennemis)
                                interface.set_dialogues(["L'adversaire a esquive le coup, dommage","L'adversaire n'a pas perdu de pv"])
                                interface.draw_dialogues()
                        elif 400 < mouse_x < 464 and 508 < mouse_y < 572:
                            #action_joueur = "se defendre"
                            toucher = random.choice([True,False])
                            if toucher == True:
                                un_ennemis.set_attaque(un_ennemis.get_attaque()-20)
                                interface.Menu_bas(joueur)
                                interface.affichage_image(100,400,joueur)
                                interface.affichage_image_adv(620,400,un_ennemis)
                                interface.set_dialogues(["Tu as choisi de te defendre, tu fais une","grimace au boss et cela reduit les degâts","qu'il peut t'infliger." ])
                                interface.draw_dialogues()
                            else:
                                interface.Menu_bas(joueur)
                                interface.affichage_image(100,400,joueur)
                                interface.affichage_image_adv(620,400,un_ennemis)
                                interface.set_dialogues(["L'ennemis n'a pas pris peur, les","degâts qu'il t'inflige ne sont pas","reduits."])
                                interface.draw_dialogues()
                        elif 550 < mouse_x < 614 and 508 < mouse_y < 572:
                            interface.Mise_a_jour(joueur)
                            interface.Menu_bas(joueur)
                            interface.affichage_image(100, 400, joueur)
                            interface.affichage_image_adv(620, 400, un_ennemis)
                            interface.set_dialogues(["Tu as choisi de prendre la fuite,","retente ta chance une prochaine fois."])
                            interface.draw_dialogues()
                            pygame.display.update()
                            combat_en_cours = False
                        pygame.display.update()
                        pygame.time.delay(1500)
                        if joueur.get_pv() >0 and un_ennemis.get_pv()>0 and combat_en_cours == True:
                            interface.get_fenetre().fill((couleur.Couleur().get_Noir()))
                            image_Arene = image.Page.ARENE.value
                            image_redimensionnee = pygame.transform.scale(image_Arene, (800, 500))
                            interface.get_fenetre().blit(image_redimensionnee, (0, 0))
                            interface.Menu_bas(joueur)
                            interface.affichage_image(100, 400, un_ennemis)
                            interface.affichage_image_adv(620, 400, joueur)
                            toucher = random.choice([False,True])
                            if toucher == True:
                                pv = un_ennemis.get_attaque()+random.randint(0,50)
                                joueur.set_pv(joueur.get_pv()-pv)
                                interface.set_dialogues(["C'est au tour du boss d'attaquer","Le boss reflechit...","Il te fait perdre {} pvs".format(pv)])
                                interface.draw_dialogues()
                            elif toucher == False:
                                interface.set_dialogues(["C'est au tour du boss d'attaquer","Le boss reflechit...","L'adversaire a raté son coup"])
                                interface.draw_dialogues()
                            pygame.display.update()
                            pygame.time.delay(1500)
                            # Actualisation de l'interface
                            interface.Mise_a_jour(joueur)
                            interface.get_fenetre().fill((couleur.Couleur().get_Noir()))
                            image_Arene = image.Page.ARENE.value
                            image_redimensionnee = pygame.transform.scale(image_Arene, (800, 500))
                            interface.get_fenetre().blit(image_redimensionnee, (0, 0))
                            interface.Menu_bas(joueur)
                            interface.affichage_image(100, 400, joueur)
                            interface.affichage_image_adv(620, 400, un_ennemis)
                            interface.set_dialogues(["Que veux-tu faire ? Une attaque basique, une ","attaque speciale, te defendre ou prendre","la fuite ?"])
                            interface.draw_dialogues()
                            image.Image(100, 508, image.BtnAttaque.BASIQUE.value).affiche(interface.get_fenetre())
                            image.Image(250, 508, image.BtnAttaque.SPECIALE.value).affiche(interface.get_fenetre())
                            image.Image(400, 508, image.BtnAttaque.DEFENSE.value).affiche(interface.get_fenetre())
                            image.Image(550, 508, image.BtnAttaque.FUITE.value).affiche(interface.get_fenetre())
                            pygame.display.update()
        

                    
    def Action_couleur_Rose(self, interface, joueur):
        # Dessiner le rectangle pour les dialogues
        interface.Menu_bas(joueur)
        interface.set_dialogues(["Tu es sur une case Chance","Clique pour decouvrir le pouvoir","que le jeu va te donner."])
        interface.draw_dialogues()
        
        chance = image.Interaction.CHANCE.value
        interface.get_fenetre().blit(chance, (360,475))
        texte.Texte("Chance",couleur.Couleur().get_Noir(),369,545).affiche(interface.get_police(),interface.get_fenetre())
        pygame.display.update()

        selection_bonus = False
        while selection_bonus != True:
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
                        interface.Menu_bas(joueur)
                        
                        interface.set_dialogues(["Tou-dou-dou-doum","Tu vas {}".format(chance)])
                        interface.draw_dialogues()
                        if chance == "gagner 100 pv":
                            joueur.ajouter_pv(interface.get_liste_joueur(),100,interface.get_fenetre())
                            selection_bonus = True
                            
                        elif chance == "gagner 200 pv":
                            joueur.ajouter_pv(interface.get_liste_joueur(),200,interface.get_fenetre())
                            selection_bonus = True
                            
                        elif chance == "gagner 500 pv":
                            joueur.ajouter_pv(interface.get_liste_joueur(),500,interface.get_fenetre())
                            selection_bonus = True
                            
                        elif chance == "gagner 150 pv":
                            joueur.ajouter_pv(interface.get_liste_joueur(),150,interface.get_fenetre())
                            selection_bonus = True
                            
                        elif chance == "gagner 300 pv":
                            joueur.ajouter_pv(interface.get_liste_joueur(),300,interface.get_fenetre())
                            selection_bonus = True
                            
                        elif chance == "gagner 1050 pv":
                            joueur.ajouter_pv(interface.get_liste_joueur(),1050,interface.get_fenetre())
                            selection_bonus = True
                                                                                   
                
    def Action_couleur_Gris(self, interface, joueur):
        # Dessiner le rectangle pour les dialogues
        interface.Menu_bas(joueur)
        interface.set_dialogues(["Tu es sur une case Speciale ! Si tu tente","ta chance, tu as une chance sur deux gagner", "deux cles que tu n'as pas ou de tout perdre."])
        interface.draw_dialogues()

        # Afficher les logos et texte des cles et des pv
        cles = image.Interaction.CLES.value
        interface.get_fenetre().blit(cles, (220, 480))
        retour = image.Interaction.RETOUR.value
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
                                interface.Menu_bas(joueur)
                                interface.set_dialogues(["Bravo tu as gagner !!!","Voilà deux cles supplementaires que tu peux", "voir apparaître dans ton inventaire."])
                                interface.draw_dialogues()
                                texte.Texte("Bravo tu as gagner !!!",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
                                texte.Texte("Voilà deux cles supplementaires que tu peux",couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())
                                texte.Texte("voir apparaître dans ton inventaire.",couleur.Couleur().get_Noir(),110, 640).affiche(interface.get_police(),interface.get_fenetre())
                                
                                pygame.display.update() # Mettre à jour l'affichage    
                                selection_speciale = True
                                
                            
                            else:
                                # Cacher les anciens dialogues
                                interface.Menu_bas(joueur)
                                texte.Texte("Oh non dommage...",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
                                texte.Texte("Tu peux retenter ta chance si tu as",couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())
                                texte.Texte("d'autres cles :)",couleur.Couleur().get_Noir(),110, 640).affiche(interface.get_police(),interface.get_fenetre())
                                
                                pygame.display.update() # Mettre à jour l'affichage  
                                selection_speciale = True
                                
                        else:
                            # Cacher les anciens dialogues
                            interface.Menu_bas(joueur)
                            texte.Texte("Tu ne possede pas de cles.",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
                            texte.Texte("Obtient-en une en tuant un boss sur les",couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())
                            texte.Texte("cases rouges.",couleur.Couleur().get_Noir(),110, 640).affiche(interface.get_police(),interface.get_fenetre())
                            
                            pygame.display.update() # Mettre à jour l'affichage  
                            selection_speciale = True    
                            
                    elif 510 < mouse_x < 574 and 480 < mouse_y < 544:
                        # Si le joueur veut passer sont tour
                        # Cacher les anciens dialogues
                        interface.Menu_bas(joueur)
                        texte.Texte("Pas de soucis, retente ta chance une autre fois",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
                        pygame.display.update() # Mettre à jour l'affichage 
                        selection_speciale = True
                        
                
    def Action_couleur_Violet(self, interface, joueur):
        # Dessiner le rectangle pour les dialogues
        interface.Menu_bas(joueur)
        texte.Texte("Tu es sur une case Rejoue !",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
        texte.Texte("Relance le de pour avoir un",couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())
        texte.Texte("deuxieme lance",couleur.Couleur().get_Noir(),110, 640).affiche(interface.get_police(),interface.get_fenetre())
        de_face1 = image.De.FACE1.value
        interface.get_fenetre().blit(de_face1,(350,475))
        pygame.display.update()    
        interface.Page_direction(joueur)
        interface.Mise_a_jour(joueur)
        interface.plateau_cache()
        interface.Page_action(joueur)

    def Action_couleur_Beige(self, interface, joueur):
        image.Image(0,468,image.Page.CHOIX_DOUBLE.value).affiche(interface.get_fenetre())
        # Dessiner le rectangle pour les dialogues
        interface.Menu_bas(joueur)
        texte.Texte("Tu es devant la Hutte de la sorciere.",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
        texte.Texte("Veux-tu essayer de l'ouvrir à l'aide",couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())
        texte.Texte("des cles des quatre boss ?",couleur.Couleur().get_Noir(),110, 640).affiche(interface.get_police(),interface.get_fenetre())

        # Afficher les logos et texte des cles et des pv
        pv = image.Interaction.CLES
        interface.get_fenetre().blit(pv, (220, 480))
        retour = image.Interaction.RETOUR.value
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
                            interface.Menu_bas(joueur)
                            texte.Texte("Bravo tu as trouve toutes les cles",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
                            texte.Texte("Ouvre la porte et apprete toi à",couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())
                            texte.Texte("affronter la sorciere.",couleur.Couleur().get_Noir(),110, 640).affiche(interface.get_police(),interface.get_fenetre())
                            pygame.display.update() # Mettre à jour l'affichage 
                            interface.set_etat_de_jeu("fin_du_jeu")
                            selection_sorciere = True
                        else:
                            # Cacher les anciens dialogues
                            interface.Menu_bas(joueur)
                            texte.Texte("Tu n'as pas encore recuperer toutes",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
                            texte.Texte("les cles afin d'ouvrir la porte de",couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())
                            texte.Texte("la sorciere. Depeche-toi !",couleur.Couleur().get_Noir(),110, 640).affiche(interface.get_police(),interface.get_fenetre())
                            pygame.display.update() # Mettre à jour l'affichage 
                            selection_sorciere = True
                        
                    elif 510 < mouse_x < 574 and 480 < mouse_y < 544:
                        # Si le joueur veut passer sont tour
                        # Cacher les anciens dialogues
                        interface.Menu_bas(joueur)
                        texte.Texte("Pas de soucis, recupere les cles afin",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
                        texte.Texte("d'ouvrir la porte en premier !",couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())
                        pygame.display.update() # Mettre à jour l'affichage 
                        selection_sorciere = True

    def Action_couleur_Indigo(self, interface, joueur):
        image.Image(0,468,image.Page.CHOIX_DOUBLE.value).affiche(interface.get_fenetre())
        interface.Menu_bas(joueur)
        # Dessiner le rectangle pour les dialogues
        interface.Menu_bas(joueur)
        texte.Texte("Tu es sur une case de Teleportation.",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
        texte.Texte("Veux-tu etre teleporter ?",couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())
        
        
        # Afficher les logos et texte des cles et des pv
        pv = image.Interaction.TP.value
        interface.get_fenetre().blit(pv, (220, 480))
        retour = image.Interaction.RETOUR.value
        interface.get_fenetre().blit(retour, (510,480))
        texte.Texte("Se teleporter",couleur.Couleur().get_Blanc(),212,545).affiche(interface.get_police(),interface.get_fenetre())
        texte.Texte("Non merci",couleur.Couleur().get_Blanc(),502,545).affiche(interface.get_police(),interface.get_fenetre())
        pygame.display.update()
        
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
                        interface.Menu_bas(joueur)
                        texte.Texte("Tou-dou-dou-doum",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
                        texte.Texte("Teleportation sur la deuxieme case",couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())
                        texte.Texte("de teleportation" ,couleur.Couleur().get_Noir(),110, 640).affiche(interface.get_police(),interface.get_fenetre())
                        
                        pygame.display.update() # Mettre à jour l'affichage 
                        coord_case_indigo = interface.get_plateau_de_jeu().get_case_indigo(joueur)
                        joueur.set_plateaux(coord_case_indigo[0])
                        joueur.set_plateauy(coord_case_indigo[1])
                        interface.get_plateau_de_jeu().set_cases_decouvertes(self.get_plateau_de_jeu().get_cases_decouvertes() + [[coord_case_indigo[0],coord_case_indigo[1]]])

                        interface.Mise_a_jour(joueur)
                        selection_teleporte = True
                        
                        
                    elif 510 < mouse_x < 574 and 480 < mouse_y < 544:
                        # Si le joueur veut passer sont tour
                        # Cacher les anciens dialogues
                        interface.Menu_bas(joueur)
                        texte.Texte("Pas de soucis, essaye une prochaine",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
                        texte.Texte("fois si tu en as l'envie.",couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())
                        
                        pygame.display.update() # Mettre à jour l'affichage 
                        selection_teleporte = True
        
    def Action_couleur_Turquoise(self, interface, joueur):
        # Dessiner le rectangle pour les dialogues
        interface.Menu_bas(joueur)
        interface.set_dialogues(["Tu es sur une case Grrr", "Un tremblement de terre surgit de nul part", "et teleporte tous les joueurs !!!"])
        interface.draw_dialogues()
        
        for i in interface.get_liste_joueur():
            i[3] = random.randint(0,9)
            i[4] = random.randint(0,16)
            interface.get_plateau_de_jeu().set_cases_decouvertes(interface.get_plateau_de_jeu().get_cases_decouvertes() + [[i[3],i[4]]])
        pygame.display.update()
