# ----------------------- Jeu de plateau - Joueur  ------------------------ #

# Bibliotheques utilisees pour le code
import pygame, texte, couleur, rectangle, image

class Joueur:
    """La classe Joueur est une classe qui permet d'utiliser un personnage."""
    
    # Definir un joueur
    def __init__(self,id,prenom,element,plateaux,plateauy) -> None:
        """_summary_
            Initialisation du joueur
        """
        self.__id = id
        self.__x = plateauy * 47
        self.__y = plateaux * 47
        self.__prenom = prenom
        self.__lien = "./assets/img/personnages/" + prenom + ".png"
        self.__pv = 650
        self.__attaque = 110
        self.__element = element
        self.__plateaux = plateaux
        self.__plateauy = plateauy
        self.__inventaire = ["clé de la Forêt","clé de la Ville","clé de la Rivière", "clé de la Ville"]

    # Definir les getters
    def get_id(self):
            """_summary_
                Getter de l'id
            """
            return self.__id

    def get_x(self):
        """_summary_
            Getter de la position x
        """
        return self.__x
    
    def get_y(self):
        """_summary_
            Getter de la position y
        """
        return self.__y
    
    def get_prenom(self):
        """_summary_
            Getter du prenom du joueur
        """
        return self.__prenom
    
    def get_lien(self):
        """_summary_
            Getter du lien de l'image du joueur
        """
        return self.__lien

    def get_ordre(self):
        """_summary_
            Getter de l'ordre du jeu
        """
        return self.__ordre
    
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
            Getter de l'element du joueur
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
        
    # Definir les setters
    def set_x(self,x):
        """_summary_
            Setter de la position x
        """
        self.__x = x
    
    def set_y(self,y):
        """_summary_
            Setter de la position y
        """
        self.__y = y
        
    def set_prenom(self,prenom):
        """_summary_
            Setter du prenom
        """
        self.__prenom = prenom
    
    def set_lien(self, lien):
        """_summary_
            Setter du lien de l'image du joueur
        """
        self.__lien = lien
    
    def set_ordre(self, ordre):
        """_summary_
            Setter de l'ordre du joueur
        """
        self.ordre = ordre

    def set_pv(self,pv):
        """_summary_
            Setter de la vie du joueur
        """
        self.__pv = pv
    
    def set_element(self, element):
        """_summary_
            Setter de l'element du joueur
        """
        self.element = element
        
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
    
    
    # Definir les deplacements du joueur
    def haut(self, dy):
        """
            La fonction haut permet de delacer un joueur vers le haut(int nombre_pixel)
        """
        avancer = False
        if self.get_plateaux() > 0:
            self.set_y(self.__y - dy)
            self.set_plateaux(self.__plateaux - 1)
            avancer = True
            return avancer
        else:
            return avancer

    def bas(self, dy):
        """
            La fonction bas permet de delacer un joueur vers le bas(int nombre_pixel)
        """
        avancer = False
        if self.get_plateaux() < 9:
            self.set_y(self.__y + dy)
            self.set_plateaux(self.__plateaux + 1)
            avancer = True
            return avancer
        else:
            return avancer

    def droite(self, dx):
        """
            La fonction droite permet de delacer un joueur vers la droite(int nombre_pixel)
        """
        avancer = False
        if self.get_plateauy() < 16:
            self.set_x(self.__x + dx)
            self.set_plateauy(self.__plateauy + 1)
            avancer = True
            return avancer
        else:
            return avancer

    def gauche(self, dx):
        """
            La fonction gauche permet de delacer un joueur vers la gauche(int nombre_pixel)
        """
        avancer = False
        if self.get_plateauy() > 0:
            self.set_x(self.__x - dx)
            self.set_plateauy(self.__plateauy - 1)
            avancer = True
            return avancer
        else:
            return avancer
    
    def ajouter_pv(self,liste_joueur,nb_pv,surface):
        """Ajoute des points de vie au joueur et met à jour l'affichage."""
        self.set_pv((self.get_pv() + nb_pv))
        liste_joueur[self.get_id()][5] = self.get_pv()
        pygame.display.update() # Mettre à jour l'affichage
        return self
    
    def supprimer_pv(self,liste_joueur,nb_pv,surface):
        """Supprime des points de vie au joueur et met à jour l'affichage."""
        self.set_pv((self.get_pv() - nb_pv))
        liste_joueur[self.get_id()][5] = self.get_pv()
        pygame.display.update() # Mettre à jour l'affichage
        return self

    # Definir l'affichage sur le menu
    def affichage_image(self,x,y,surface,font):
        """
            La fonction affichage_image permet d'afficher le personnage dans le menu(int x, int y, Surface surface, Font font)
        """
        # Charger l'image
        image = pygame.image.load(self.get_lien())
        
        # Afficher l'image sur la fenetre
        surface.blit(image, (x, y))
        
        # Dessiner le rectangle pour les pv du joueur
        rectangle.Rectangle(500,590,130,35).affiche(surface,couleur.Couleur().get_Vert())
    
        # Charger les pv
        texte.Texte(self.get_pv(),couleur.Couleur().get_Noir(),538,598).affiche(font,surface)
        
        # Mettre à jour l'affichage
        pygame.display.update()
        return
    
    def affichage_pv_combat(self,surface,font):
        """
            La fonction affichage_image permet d'afficher le personnage dans le menu(int x, int y, Surface surface, Font font)
        """
        
        # Dessiner le rectangle pour les pv du joueur
        rectangle.Rectangle(500,590,130,35).affiche(surface,couleur.Couleur().get_Vert())
    
        # Charger les pv
        texte.Texte(self.get_pv(),couleur.Couleur().get_Noir(),538,598).affiche(font,surface)
        
        # Mettre à jour l'affichage
        pygame.display.update()
        return
    
    def affichage_pv_combat_adv(self,surface,font):
        """
            La fonction affichage_image permet d'afficher le personnage adverse dans le menu(int x, int y, Surface surface, Font font)
        """
        
        """Affiche les points de vie de l'ennemi en combat."""
        rectangle.Rectangle(500, 635, 130, 35).affiche(surface, couleur.Couleur().get_Rouge())
        texte.Texte(self.get_pv(), couleur.Couleur().get_Noir(), 538, 640).affiche(font, surface)
        pygame.display.update()

    def affichage_cle(self,surface):
        """
            La fonction affichage_cle permet d'afficher les cle dans le menu(int x, int y, Surface surface, Font font)
        """
        
        # Dessiner le rectangle pour les cles
        rectangle.Rectangle(650,585,130,90).affiche(surface,couleur.Couleur().get_Rose())
    
        for i in self.get_inventaire():
            if i == "cle de la Ville" :
                image.Image(660,640,"assets/img/cle/cle_ville.png").affichage_image_redimensionnee(48,30,surface)
            elif i == "cle de la Riviere" :
                image.Image(660,595,"assets/img/cle/cle_riviere.png").affichage_image_redimensionnee(48,30,surface)
            elif i == "cle de la Foret" :
                image.Image(725,595,"assets/img/cle/cle_foret.png").affichage_image_redimensionnee(48,30,surface)
            elif i == "cle du Rocher" :
                image.Image(725,640,"assets/img/cle/cle_rocher.png").affichage_image_redimensionnee(48,30,surface)
        pygame.draw.line(surface, couleur.Couleur().get_Noir(), (660, 632), (770, 632), 2)
        pygame.draw.line(surface, couleur.Couleur().get_Noir(), (715, 595), (715, 670), 2)
        # Mettre à jour l'affichage
        pygame.display.update()
        return
    
    # Definir l'affichage sur le plateau
    def affichage_image_plateau(self,x,y,surface):
        """
            La fonction affichage_image_plateau permet d'afficher le personnage dans le plateau(int x, int y, Surface surface)
        """
        # Charger l'image
        image = pygame.image.load(self.get_lien())
        image_redimensionnee = pygame.transform.scale(image, (47, 47))
        
        # Afficher l'image redimensionnee sur la fenetre
        surface.blit(image_redimensionnee, (x, y))
        
        # Mettre à jour l'affichage
        pygame.display.update()        


    def affiche_tt_joueur(self,liste_joueur, nombre_joueur,fenetre):
        """Affiche tous les joueurs sur le plateau."""
        if nombre_joueur == 0:
            J1  = Joueur(nombre_joueur,liste_joueur[0][1], liste_joueur[0][2],liste_joueur[0][3], liste_joueur[0][4])
            J1.affichage_image_plateau(J1.get_x(),J1.get_y(),fenetre)
            pygame.display.update()
            return J1
        elif nombre_joueur == 1:
            J1 = Joueur(nombre_joueur,liste_joueur[0][1], liste_joueur[0][2],liste_joueur[0][3], liste_joueur[0][4])
            J2 = Joueur(nombre_joueur + 1,liste_joueur[1][1], liste_joueur[1][2],liste_joueur[1][3], liste_joueur[1][4])
            J1.affichage_image_plateau(J1.get_x(),J1.get_y(),fenetre)
            J2.affichage_image_plateau(J2.get_x(),J2.get_y(),fenetre)
            pygame.display.update()
            return J1, J2
        elif nombre_joueur == 2:
            J1 = Joueur(nombre_joueur,liste_joueur[0][1], liste_joueur[0][2],liste_joueur[0][3], liste_joueur[0][4])
            J2 = Joueur(nombre_joueur + 1,liste_joueur[1][1], liste_joueur[1][2],liste_joueur[1][3], liste_joueur[1][4])
            J3 = Joueur(nombre_joueur + 2,liste_joueur[2][1], liste_joueur[2][2],liste_joueur[2][3], liste_joueur[2][4])
            J1.affichage_image_plateau(J1.get_x(),J1.get_y(),fenetre)
            J2.affichage_image_plateau(J2.get_x(),J2.get_y(),fenetre)
            J3.affichage_image_plateau(J3.get_x(),J3.get_y(),fenetre)
            pygame.display.update()
            return J1, J2, J3
        elif nombre_joueur == 3:
            J1 = Joueur(nombre_joueur,liste_joueur[0][1], liste_joueur[0][2],liste_joueur[0][3], liste_joueur[0][4])
            J2 = Joueur(nombre_joueur + 1,liste_joueur[1][1], liste_joueur[1][2],liste_joueur[1][3], liste_joueur[1][4])
            J3 = Joueur(nombre_joueur + 2,liste_joueur[2][1], liste_joueur[2][2],liste_joueur[2][3], liste_joueur[2][4])
            J4 = Joueur(nombre_joueur + 3,liste_joueur[3][1], liste_joueur[3][2],liste_joueur[3][3], liste_joueur[3][4])
            J1.affichage_image_plateau(J1.get_x(),J1.get_y(),fenetre)
            J2.affichage_image_plateau(J2.get_x(),J2.get_y(),fenetre)
            J3.affichage_image_plateau(J3.get_x(),J3.get_y(),fenetre)
            J4.affichage_image_plateau(J4.get_x(),J4.get_y(),fenetre)
            pygame.display.update()
            return J1, J2, J3, J4
    
    def affichage_potion(self,surface):
        """
            La fonction affichage_potion permet d'afficher la potion dans l'inventaire du joueur
        """
        # Charger l'image
        potion = pygame.image.load("assets\img\illustrations\Potion_inverstium.png")
        
        # Afficher l'image redimensionnee sur la fenetre
        surface.blit(potion, (668, 593))
        
        # Mettre à jour l'affichage
        pygame.display.update()  
    
    def avoir_tt_cles(self) -> bool : 
        """Verifie si le joueur a toutes les cles necessaires."""
        nombre_cles = 0
        for i in self.get_inventaire():
            if i == "cle de la Ville":
                nombre_cles = nombre_cles + 1
            elif i == "cle de la Riviere":
                nombre_cles = nombre_cles + 1
            elif i == "cle du Rocher":
                nombre_cles = nombre_cles + 1
            elif i == "cle de la Foret":
                nombre_cles = nombre_cles + 1
        if nombre_cles == 4:
            return True
        else:
            return False
    
    def a_gagne(self,plateau) -> bool:
        """Verifie si le joueur a gagne en ayant toutes les cles et en etant dans une hutte."""
        gagne = False
        if self.avoir_tt_cles() == True and plateau.get_nom(self.get_plateaux(),self.get_plateauy()) == "Hutte":
            gagne = True
        return gagne
        
    def adv_nb_attaquer(self,liste_joueur):
        # Combien d'adversaire on peut attaquer
        nbjoueur_attaque = 0
        x1 = self.get_plateaux()
        y1 = self.get_plateauy()
        for i in liste_joueur:
            if (((i[3] == x1) or (i[3] == x1 + 1) or (i[3] == x1 - 1)) and ((i[4] == y1) or (i[4] == y1 + 1) or (i[4] == y1 - 1)) and (i[0] != self.get_id())):
                nbjoueur_attaque = nbjoueur_attaque + 1
        return nbjoueur_attaque

    def adv_a_attaquer(self, liste_joueur):
        # Quel adversaire on peut attaquer
        x1 = self.get_plateaux()
        y1 = self.get_plateauy()
        for i in liste_joueur:
            if (((i[3] == x1) or (i[3] == x1 + 1) or (i[3] == x1 - 1)) and ((i[4] == y1) or (i[4] == y1 + 1) or (i[4] == y1 - 1)) and (i[0] != self.get_id())):
                return i[0]
        return (-1)
        
        
        
# Tests des fonctions

if __name__ == "__main__":
    fenetre = pygame.display.set_mode((800,700))
    nouveau_joueur = Joueur(1,"Ondine","Riviere",1,2)
    nouveau_joueur.set_inventaire(["cle de la Ville","cle de la Foret","cle du Rocher"])
    nouveau_joueur.affichage_image_plateau(300,400,fenetre)
    nouveau_joueur.affichage_cle(fenetre)
    nouveau_joueur.affichage_potion(fenetre)
    pygame.time.delay(3500)
