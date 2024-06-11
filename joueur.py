# ----------------------- Jeu de plateau - Joueur  ------------------------ #

# Bibliotheques utilisees pour le code
import pygame, random
# from utils import texte, couleur, image, rectangle, logique

from enum import Enum
class Nom(Enum):
    WATER = "Ondine"
    GRASS = "Flora"
    ROCK = "Pierre"
    TOWN = "Kevin"
class Element(Enum):
    WATER = "de la Riviere"
    GRASS = "de la Foret"
    ROCK = "du Rocher"
    TOWN = "de la Ville"


class Joueur:
    """La classe Joueur est une classe qui permet d'utiliser un personnage."""
    
    water_is_used = False 
    grass_is_used = False 
    town_is_used = False 
    rock_is_used = False 
    
    # Definir un joueur
    def __init__(self,id:int, plateaux:int, plateauy:int,element:Element) -> None:
        """_summary_
            Initialisation du joueur
        """
        self.__id:int = id
        self.__element:Element = element
        self.__plateaux:int = plateaux
        self.__plateauy:int = plateauy
        self.__pv:int = 700
        self.__attaque:int = 110
        self.__inventaire:list = []
        

    # Definir les getters
    def get_x(self):
        """_summary_
            Getter de la position x
        """
        return self.__plateaux *47
    
    def get_y(self):
        """_summary_
            Getter de la position y
        """
        return self.__plateauy *47
    
    def get_prenom(self)->str:
        """_summary_
            Getter du prenom du joueur
        """
        if(self.__element == Element.GRASS): return Nom.GRASS.value
        if(self.__element == Element.WATER): return Nom.WATER.value
        if(self.__element == Element.TOWN): return Nom.TOWN.value
        if(self.__element == Element.ROCK): return Nom.ROCK.value
        return None
    
    def get_image(self):
        if(self.__element == Element.GRASS): return image.Personnages.GRASS.value
        if(self.__element == Element.WATER): return image.Personnages.WATER.value
        if(self.__element == Element.TOWN): return image.Personnages.TOWN.value
        if(self.__element == Element.ROCK): return image.Personnages.ROCK.value
        return None

    def get_id(self):
        """_summary_
            Getter de l'id du joueur
        """
        return self.__id
    
    def get_pv(self):
        """_summary_
            Getter des pv du joueur
        """
        return self.__pv
    
    def get_attaque(self):
        """_summary_
            Getter des attaques du joueur
        """
        return self.__attaque
    
    def get_element(self):
        """_summary_
            Getter de l'__element du joueur
        """
        return self.__element
    
    def get_inventaire(self):
        """_summary_
            Getter de l'inventaire du joueur
        """
        return self.__inventaire
    
    def get_plateaux(self):
            """_summary_
                Getter de la position x sur le plateau
            """
            return self.__plateaux
    
    def get_plateauy(self):
            """_summary_
                Getter de la position y sur le plateau
            """
            return self.__plateauy
    
    def get_attaque(self):
            """_summary_
                Getter de l'attaque sur le plateau
            """
            return self.__attaque
        
        
            
    def set_lien(self, lien):
        """_summary_
            Setter du lien de l'image du joueur
        """
        self.__lien = lien
    
    def set_pv(self,pv):
        """_summary_
            Setter de la vie du joueur
        """
        self.__pv = pv
    
    def set_element(self, element):
        """_summary_
            Setter de l'__element du joueur
        """
        if(self.__element == None): pass
        elif(self.__element == Element.GRASS): Joueur.grass_is_used = False
        elif(self.__element == Element.WATER): Joueur.water_is_used = False
        elif(self.__element == Element.TOWN): Joueur.town_is_used = False
        else: Joueur.rock_is_used = False
        self.__element = element
        if(self.__element == Element.ROCK): Joueur.rock_is_used = True
        elif(self.__element == Element.GRASS): Joueur.grass_is_used = True
        elif(self.__element == Element.WATER): Joueur.water_is_used = True
        elif(self.__element == Element.TOWN): Joueur.town_is_used = True
        
    def set_inventaire(self,inventaire):
        """_summary_
            Setter de l'inventaire du joueur
        """
        self.__inventaire = inventaire
    
    def set_plateaux(self,plateaux):
        """
            Setter de la position x sur le plateau
        """
        self.__plateaux = plateaux
    
    def set_plateauy(self,plateauy):
        """
            Setter de la position y sur le plateau
        """
        self.__plateauy = plateauy

    def set_attaque(self,attaque):
        """
            Setter de l'attaque sur le plateau
        """
        self.__attaque = attaque
    
    
    # Definir les deplacements du joueur
    # def haut(self, dy):
    #     """
    #         La fonction haut permet de delacer un joueur vers le haut(int nombre_pixel)
    #     """
    #     avancer = False
    #     if self.get_plateaux() > 0:
    #         self.set_y(self.__y - dy)
    #         self.set_plateaux(self.__plateaux - 1)
    #         avancer = True
    #         return avancer
    #     else:
    #         return avancer

    # def bas(self, dy):
    #     """
    #         La fonction bas permet de delacer un joueur vers le bas(int nombre_pixel)
    #     """
    #     avancer = False
    #     if self.get_plateaux() < 9:
    #         self.set_y(self.__y + dy)
    #         self.set_plateaux(self.__plateaux + 1)
    #         avancer = True
    #         return avancer
    #     else:
    #         return avancer

    # def droite(self, dx):
    #     """
    #         La fonction droite permet de delacer un joueur vers la droite(int nombre_pixel)
    #     """
    #     avancer = False
    #     if self.get_plateauy() < 16:
    #         self.set_x(self.__x + dx)
    #         self.set_plateauy(self.__plateauy + 1)
    #         avancer = True
    #         return avancer
    #     else:
    #         return avancer

    # def gauche(self, dx):
    #     """
    #         La fonction gauche permet de delacer un joueur vers la gauche(int nombre_pixel)
    #     """
    #     avancer = False
    #     if self.get_plateauy() > 0:
    #         self.set_x(self.__x - dx)
    #         self.set_plateauy(self.__plateauy - 1)
    #         avancer = True
    #         return avancer
    #     else:
    #         return avancer
    
    # def ajouter_pv(self,liste_joueur,nb_pv,surface):
    #     """Ajoute des points de vie au joueur et met à jour l'affichage."""
    #     self.set_pv((self.get_pv() + nb_pv))
    #     liste_joueur[self.get_id()][5] = self.get_pv()
    #     pygame.display.update() # Mettre à jour l'affichage
    #     return self
    
    # def supprimer_pv(self,liste_joueur,nb_pv,surface):
    #     """Supprime des points de vie au joueur et met à jour l'affichage."""
    #     self.set_pv((self.get_pv() - nb_pv))
    #     liste_joueur[self.get_id()][5] = self.get_pv()
    #     pygame.display.update() # Mettre à jour l'affichage
    #     return self      
    
    # def adv_a_attaquer(self, liste_joueur):
    #     # Savoir si on a quelqu'un a attaqué
    #     attaquer = False
    #     x1 = self.get_plateaux()
    #     y1 = self.get_plateauy()
    #     for i in liste_joueur:
    #         if (((i[3] == x1) or (i[3] == x1 + 1) or (i[3] == x1 - 1)) and ((i[4] == y1) or (i[4] == y1 + 1) or (i[4] == y1 - 1)) and (i[0] != self.get_id())):
    #             attaquer = True
    #     return attaquer
    
    # def adv_nom_attaquer(self, liste_joueur):
    #     # Quel adversaire on peut attaquer
    #     x1 = self.get_plateaux()
    #     y1 = self.get_plateauy()
    #     for i in liste_joueur:
    #         if (((i[3] == x1) or (i[3] == x1 + 1) or (i[3] == x1 - 1)) and ((i[4] == y1) or (i[4] == y1 + 1) or (i[4] == y1 - 1)) and (i[0] != self.get_id())):
    #             return i[0]
    #     return (-1)
    
        
    # def combat_joueurs(self, interface, ordre_adv):
    #     # Combats des joueurs
    #     joueur_adv = Joueur(interface.get_liste_joueur()[ordre_adv][0],interface.get_liste_joueur()[ordre_adv][1],interface.get_liste_joueur()[ordre_adv][2],interface.get_liste_joueur()[ordre_adv][3],interface.get_liste_joueur()[ordre_adv][4],interface.get_liste_joueur()[ordre_adv][5],interface.get_liste_joueur()[ordre_adv][6],interface.get_liste_joueur()[ordre_adv][7])
                
    #     # Mettre la fenetre combat
    #     interface.get_fenetre().fill((couleur.Couleur().get_Noir()))
    #     image_Arene = pygame.image.load("./assets/img/ennemis/Arene.png")
    #     image_redimensionnee = pygame.transform.scale(image_Arene, (800, 500))
    #     interface.get_fenetre().blit(image_redimensionnee, (0, 0))
            
    #     #Afficher le joueur et l'adversaire
    #     interface.Menu_bas(self)
    #     interface.affichage_image(100,400,self)
    #     interface.affichage_image_adv(620,400,joueur_adv)
            
    #     # Affiche le texte 
    #     texte.Texte("Tu as décidé de combattre un joueur. Le celebre ", couleur.Couleur().get_Noir(), 110, 600).affiche(interface.get_police(),interface.get_fenetre())
    #     texte.Texte("{}. Prepare toi à le combattre afin de prendre".format(joueur_adv.get_prenom()), couleur.Couleur().get_Noir(), 110, 620).affiche(interface.get_police(),interface.get_fenetre())
    #     texte.Texte("l'avantage sur lui !", couleur.Couleur().get_Noir(), 110, 640).affiche(interface.get_police(),interface.get_fenetre())
    #     pygame.display.update()
    #     pygame.time.delay(1500)

    #     interface.get_fenetre().fill((couleur.Couleur().get_Noir()))
    #     image_Arene = pygame.image.load("./assets/img/ennemis/Arene.png")
    #     image_redimensionnee = pygame.transform.scale(image_Arene, (800, 500))
    #     interface.get_fenetre().blit(image_redimensionnee, (0, 0))
    #     interface.Menu_bas(self)
    #     interface.affichage_image(100,400,self)
    #     interface.affichage_image_adv(620,400,joueur_adv)
    #     texte.Texte("Que veux-tu faire ? Une attaque basique, une ", couleur.Couleur().get_Noir(), 110, 600).affiche(interface.get_police(),interface.get_fenetre())
    #     texte.Texte("attaque speciale, te defendre ou prendre", couleur.Couleur().get_Noir(), 110, 620).affiche(interface.get_police(),interface.get_fenetre())
    #     texte.Texte("la fuite ?", couleur.Couleur().get_Noir(), 110, 640).affiche(interface.get_police(),interface.get_fenetre())
    #     image.Image(100,508,'assets/img/illustrations/Basique.png').affiche(interface)
    #     image.Image(250,508,'assets/img/illustrations/Speciale.png').affiche(interface)
    #     image.Image(400,508,'assets/img/illustrations/Defense.png').affiche(interface)
    #     image.Image(550,508,'assets/img/illustrations/Fuite.png').affiche(interface)
    #     pygame.display.update()
        
    #     combat_en_cours = True
    #     # Tant que l'ennemis est en vie
    #     while combat_en_cours:
    #         if self.get_pv()<=0:
    #             self.set_pv(0)
    #             joueur_adv.set_inventaire(joueur_adv.get_inventaire() + self.get_inventaire())
    #             interface.Menu_bas(self)
    #             interface.affichage_image(100,400,self)
    #             interface.affichage_image_adv(620,400,joueur_adv)
    #             texte.Texte("Fin du combat... Tu n'as pas survecu",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
    #             texte.Texte("à l'attaque de l'adversaire...",couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())
    #             texte.Texte("Retour au plateau !",couleur.Couleur().get_Noir(),110, 640).affiche(interface.get_police(),interface.get_fenetre())
    #             interface.Mise_a_jour(self)
    #             interface.Mise_a_jour(joueur_adv)
    #             pygame.display.update()
    #             combat_en_cours = False
    #         elif joueur_adv.get_pv()<=0:
    #             joueur_adv.set_pv(0)
    #             interface.Menu_bas(self)
    #             interface.affichage_image(100,400,self)
    #             interface.affichage_image_adv(620,400,joueur_adv)
    #             texte.Texte("Fin du combat... Tu as tué",couleur.Couleur().get_Noir(),110, 600).affiche(interface.get_police(),interface.get_fenetre())
    #             texte.Texte("l'adversaire, bravo.",couleur.Couleur().get_Noir(),110, 620).affiche(interface.get_police(),interface.get_fenetre())
    #             texte.Texte("Retour au plateau !",couleur.Couleur().get_Noir(),110, 640).affiche(interface.get_police(),interface.get_fenetre())
    #             interface.Mise_a_jour(self)
    #             interface.Mise_a_jour(joueur_adv)
    #             pygame.display.update()
    #             combat_en_cours = False
    #         elif self.get_pv()>0 and joueur_adv.get_pv()>0:
    #             for event in pygame.event.get():
    #                 if event.type == pygame.QUIT: # si le joueur quitte la fenetre # si le joueur quitte la fenetre
    #                     pygame.quit()
    #                     exit() 
                    
    #                 # Si le clique est presse
    #                 if event.type == pygame.MOUSEBUTTONDOWN:  
    #                     mouse_x, mouse_y = pygame.mouse.get_pos() # Recuperer les coordonnees de la souris
    #                     if 100 < mouse_x < 164 and 508 < mouse_y < 572:
    #                         #action_joueur = "attaque basique"
    #                         toucher = random.choice([True,False,True])
    #                         if toucher == True:
    #                             if self.get_element() == joueur_adv.get_element():
    #                                 pv = random.randint(self.get_attaque(),self.get_attaque()+20)
    #                                 joueur_adv.set_pv(joueur_adv.get_pv()-pv)
    #                             else:
    #                                 pv = random.randint(self.get_attaque()-20,self.get_attaque())
    #                                 joueur_adv.set_pv(joueur_adv.get_pv()-pv)
    #                             interface.Menu_bas(self)
    #                             interface.affichage_image(100,400,self)
    #                             interface.affichage_image_adv(620,400,joueur_adv)
    #                             texte.Texte("Tu as choisi de faire une attaque basique,", couleur.Couleur().get_Noir(), 110, 600).affiche(interface.get_police(),interface.get_fenetre())
    #                             texte.Texte("bravo, l'adversaire a perdu {} pvs".format(pv), couleur.Couleur().get_Noir(), 110, 620).affiche(interface.get_police(),interface.get_fenetre())
    #                         else:
    #                             interface.Menu_bas(self)
    #                             interface.affichage_image(100,400,self)
    #                             interface.affichage_image_adv(620,400,joueur_adv)
    #                             texte.Texte("L'adversaire a esquive le coup, dommage", couleur.Couleur().get_Noir(), 110, 600).affiche(interface.get_police(),interface.get_fenetre())
    #                             texte.Texte("L'adversaire n'a pas perdu de pv", couleur.Couleur().get_Noir(), 110, 620).affiche(interface.get_police(),interface.get_fenetre())
    #                     if 250 < mouse_x < 314 and 508 < mouse_y < 572:
    #                         #action_joueur = "attaque speciale"
    #                         toucher = random.choice([True,False])
    #                         if toucher == True:
    #                             pv = self.get_attaque()+50
    #                             joueur_adv.set_pv(joueur_adv.get_pv()-pv)
    #                             interface.Menu_bas(self)
    #                             interface.affichage_image(100,400,self)
    #                             interface.affichage_image_adv(620,400,joueur_adv)
    #                             texte.Texte("Tu as choisi de faire une attaque speciale,", couleur.Couleur().get_Noir(), 110, 600).affiche(interface.get_police(),interface.get_fenetre())
    #                             texte.Texte("bravo, l'adversaire a perdu {} pvs".format(pv), couleur.Couleur().get_Noir(), 110, 620).affiche(interface.get_police(),interface.get_fenetre())
    #                         else:
    #                             interface.Menu_bas(self)
    #                             interface.affichage_image(100,400,self)
    #                             interface.affichage_image_adv(620,400,joueur_adv)
    #                             texte.Texte("L'adversaire a esquive le coup, dommage", couleur.Couleur().get_Noir(), 110, 600).affiche(interface.get_police(),interface.get_fenetre())
    #                             texte.Texte("L'adversaire n'a pas perdu de pv", couleur.Couleur().get_Noir(), 110, 620).affiche(interface.get_police(),interface.get_fenetre())
    #                     if 400 < mouse_x < 464 and 508 < mouse_y < 572:
    #                         #action_joueur = "se defendre"
    #                         toucher = random.choice([True,False])
    #                         if toucher == True:
    #                             joueur_adv.set_attaque(joueur_adv.get_attaque()-20)
    #                             interface.Menu_bas(self)
    #                             interface.affichage_image(100,400,self)
    #                             interface.affichage_image_adv(620,400,joueur_adv)
    #                             texte.Texte("Tu as choisi de te defendre, tu fais une", couleur.Couleur().get_Noir(), 110, 600).affiche(interface.get_police(),interface.get_fenetre())
    #                             texte.Texte("grimace au boss et cela reduit les degâts", couleur.Couleur().get_Noir(), 110, 620).affiche(interface.get_police(),interface.get_fenetre())
    #                             texte.Texte("qu'il peut t'infliger." ,couleur.Couleur().get_Noir(), 110, 640).affiche(interface.get_police(),interface.get_fenetre())
    #                         else:
    #                             interface.Menu_bas(self)
    #                             interface.affichage_image(100,400,self)
    #                             interface.affichage_image_adv(620,400,joueur_adv)
    #                             texte.Texte("L'ennemis n'a pas pris peur, les", couleur.Couleur().get_Noir(), 110, 600).affiche(interface.get_police(),interface.get_fenetre())
    #                             texte.Texte("degâts qu'il t'inflige ne sont pas", couleur.Couleur().get_Noir(), 110, 620).affiche(interface.get_police(),interface.get_fenetre())
    #                             texte.Texte("reduits.", couleur.Couleur().get_Noir(), 110, 640).affiche(interface.get_police(),interface.get_fenetre())
    #                     if 550 < mouse_x < 614 and 508 < mouse_y < 572:
    #                         #action_joueur = "prendre la fuite"
    #                         interface.Menu_bas(self)
    #                         interface.affichage_image(100,400,self)
    #                         interface.affichage_image_adv(620,400,joueur_adv)
    #                         texte.Texte("Tu as choisi de prendre la fuite, c'est", couleur.Couleur().get_Noir(), 110, 600).affiche(interface.get_police(),interface.get_fenetre())
    #                         texte.Texte("surement le bon choix retente ta chance plus", couleur.Couleur().get_Noir(), 110, 620).affiche(interface.get_police(),interface.get_fenetre())
    #                         texte.Texte("tard et detruit moi cet adversaire !!!" ,couleur.Couleur().get_Noir(), 110, 640).affiche(interface.get_police(),interface.get_fenetre())
    #                         combat_en_cours = False
    #                     pygame.display.update()
    #                     pygame.time.delay(2500)
    #                     if self.get_pv() >0 and joueur_adv.get_pv()>0 and combat_en_cours == True:
    #                         temp = self ; self = joueur_adv ; joueur_adv = temp
    #                         interface.Mise_a_jour(self)
    #                         interface.Mise_a_jour(joueur_adv)
    #                         interface.get_fenetre().fill((couleur.Couleur().get_Noir()))
    #                         image_Arene = pygame.image.load("./assets/img/ennemis/Arene.png")
    #                         image_redimensionnee = pygame.transform.scale(image_Arene, (800, 500))
    #                         interface.get_fenetre().blit(image_redimensionnee, (0, 0))
    #                         interface.Menu_bas(self)
    #                         interface.affichage_image(100,400,self)
    #                         interface.affichage_image_adv(620,400,joueur_adv)
    #                         texte.Texte("Que veux-tu faire ? Une attaque basique, une ", couleur.Couleur().get_Noir(), 110, 600).affiche(interface.get_police(),interface.get_fenetre())
    #                         texte.Texte("attaque speciale, te defendre ou prendre", couleur.Couleur().get_Noir(), 110, 620).affiche(interface.get_police(),interface.get_fenetre())
    #                         texte.Texte("la fuite ?", couleur.Couleur().get_Noir(), 110, 640).affiche(interface.get_police(),interface.get_fenetre())
    #                         image.Image(100,508,'assets/img/illustrations/Basique.png').affiche(interface)
    #                         image.Image(250,508,'assets/img/illustrations/Speciale.png').affiche(interface)
    #                         image.Image(400,508,'assets/img/illustrations/Defense.png').affiche(interface)
    #                         image.Image(550,508,'assets/img/illustrations/Fuite.png').affiche(interface)
    #                         pygame.display.update()

    # def avoir_tt_cles(self) -> bool : 
    #     """Verifie si le joueur a toutes les cles necessaires."""
    #     nombre_cles = 0
    #     for i in self.get_inventaire():
    #         nombre_cles += 1
    #     if nombre_cles == 4:
    #         return True
    #     else:
    #         return False
    
    # def a_gagne(self,plateau) -> bool:
    #     """Verifie si le joueur a gagne en ayant toutes les cles et en etant dans une hutte."""
    #     gagne = False
    #     if self.avoir_tt_cles() == True and plateau.get_nom(self.get_plateaux(),self.get_plateauy()) == "Hutte":
    #         gagne = True
    #     return gagne
    