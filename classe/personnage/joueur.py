# ----------------------- Jeu de plateau - Joueur  ------------------------ #

# Bibliotheques utilisees pour le code
import pygame, random
from classe.visuel import texte, couleur, image

class Joueur:
    """La classe Joueur est une classe qui permet d'utiliser un personnage."""
    
    # Definir un joueur
    def __init__(self,id,prenom,element, plateaux, plateauy) -> None:
        """_summary_
            Initialisation du joueur
        """
        self.__id = id
        self.__prenom = prenom
        self.__element = element
        self.__plateaux = plateaux
        self.__plateauy = plateauy      
        self.__x = self.getPlateauY() * 47
        self.__y = self.getPlateauX() * 47
        self.__lien = "./assets/img/personnages/" + prenom + ".png"
        self.__pv = 1000
        self.__attaque = 150
        self.__inventaire = ["clé de la Ville", "clé de la Rivière", "clé de la Forêt", "clé du Rocher"]

    # Definir les getters
    def getX(self):
        """_summary_
            Getter de la position x
        """
        return self.__x
    
    def getY(self):
        """_summary_
            Getter de la position y
        """
        return self.__y
    
    def getPrenom(self):
        """_summary_
            Getter du prenom du joueur
        """
        return self.__prenom
    
    def getLien(self):
        """_summary_
            Getter du lien de l'image du joueur
        """
        return self.__lien

    def getId(self):
        """_summary_
            Getter de l'id du joueur
        """
        return self.__id
    
    def getPv(self):
        """_summary_
            Getter des pv du joueur
        """
        return self.__pv
    
    def getAttaque(self):
        """_summary_
            Getter des attaques du joueur
        """
        return self.__attaque
    
    def getElement(self):
        """_summary_
            Getter de l'element du joueur
        """
        return self.__element
    
    def getInventaire(self):
        """_summary_
            Getter de l'inventaire du joueur
        """
        return self.__inventaire
    
    def getPlateauX(self):
            """_summary_
                Getter de la position x sur le plateau
            """
            return self.__plateaux
    
    def getPlateauY(self):
            """_summary_
                Getter de la position y sur le plateau
            """
            return self.__plateauy
    
    def getAttaque(self):
            """_summary_
                Getter de l'attaque sur le plateau
            """
            return self.__attaque
        
    # Definir les setters
    def setX(self,x):
        """_summary_
            Setter de la position x
        """
        self.__x = x
    
    def setY(self,y):
        """_summary_
            Setter de la position y
        """
        self.__y = y
        
    def setPrenom(self,prenom):
        """_summary_
            Setter du prenom
        """
        self.__prenom = prenom
    
    def setLien(self, lien):
        """_summary_
            Setter du lien de l'image du joueur
        """
        self.__lien = lien
    
    def setId(self, id):
        """_summary_
            Setter de l'id du joueur
        """
        self.id = id

    def setPv(self,pv):
        """_summary_
            Setter de la vie du joueur
        """
        self.__pv = pv
    
    def setElement(self, element):
        """_summary_
            Setter de l'element du joueur
        """
        self.element = element
        
    def setInventaire(self,inventaire):
        """_summary_
            Setter de l'inventaire du joueur
        """
        self.__inventaire = inventaire
    
    def setPlateauX(self,plateaux):
        """
            Setter de la position x sur le plateau
        """
        self.__plateaux = plateaux
    
    def setPlateauY(self,plateauy):
        """
            Setter de la position y sur le plateau
        """
        self.__plateauy = plateauy

    def setAttaque(self,attaque):
        """
            Setter de l'attaque sur le plateau
        """
        self.__attaque = attaque
    
    
    # Definir les deplacements du joueur
    def haut(self, dy):
        """
            La fonction haut permet de delacer un joueur vers le haut(int nombre_pixel)
        """
        avancer = False
        if self.getPlateauX() > 0:
            self.setY(self.getY() - dy)
            self.setPlateauX(self.getPlateauX() - 1)
            avancer = True
            return avancer
        else:
            return avancer

    def bas(self, dy):
        """
            La fonction bas permet de delacer un joueur vers le bas(int nombre_pixel)
        """
        avancer = False
        if self.getPlateauX() < 9:
            self.setY(self.getY() + dy)
            self.setPlateauX(self.getPlateauX() + 1)
            avancer = True
            return avancer
        else:
            return avancer

    def droite(self, dx):
        """
            La fonction droite permet de delacer un joueur vers la droite(int nombre_pixel)
        """
        avancer = False
        if self.getPlateauY() < 16:
            self.setX(self.getX() + dx)
            self.setPlateauY(self.getPlateauY() + 1)
            avancer = True
            return avancer
        else:
            return avancer

    def gauche(self, dx):
        """
            La fonction gauche permet de delacer un joueur vers la gauche(int nombre_pixel)
        """
        avancer = False
        if self.getPlateauY() > 0:
            self.setX(self.getX() - dx)
            self.setPlateauY(self.getPlateauY() - 1)
            avancer = True
            return avancer
        else:
            return avancer
    
    def advDisponible(self, liste_joueur):
        # Savoir si on a quelqu'un a attaqué
        attaquer = False
        x1 = self.getPlateauX()
        y1 = self.getPlateauY()
        for joueur in liste_joueur:
            if (((joueur.getPlateauX() == x1) or (joueur.getPlateauX() == x1 + 1) or (joueur.getPlateauX() == x1 - 1)) and ((joueur.getPlateauY() == y1) or (joueur.getPlateauY() == y1 + 1) or (joueur.getPlateauY() == y1 - 1)) and (joueur.getId()!= self.getId())):
                attaquer = True
        return attaquer
    
    def advNomDisponible(self, interface):
        # Quel adversaire on peut attaquer
        x1 = self.getPlateauX()
        y1 = self.getPlateauY()
        for i in interface.getListeJoueurs():
            if (((self.getPlateauX() == x1) or (self.getPlateauX() == x1 + 1) or (self.getPlateauX() == x1 - 1)) and ((self.getPlateauY() == y1) or (self.getPlateauY() == y1 + 1) or (self.getPlateauY() == y1 - 1)) and (self.getId() != self.getId())):
                return self.getId()
        return (-1)
    
    def combatJoueurs(self, interface, ordre_adv):
        # Combats des joueurs
        joueur_adv = Joueur(interface.getListeJoueurs()[ordre_adv][0],interface.getListeJoueurs()[ordre_adv][1],interface.getListeJoueurs()[ordre_adv][2],interface.getListeJoueurs()[ordre_adv][3],interface.getListeJoueurs()[ordre_adv][4],interface.getListeJoueurs()[ordre_adv][5],interface.getListeJoueurs()[ordre_adv][6],interface.getListeJoueurs()[ordre_adv][7])
                
        # Mettre la fenetre combat
        image_Arene = pygame.image.load("./assets/img/ennemis/Arene.png")
        image_redimensionnee = pygame.transform.scale(image_Arene, (800, 500))
        interface.affichageCombat(image_redimensionnee, (0, 0))
            
        #Afficher le joueur et l'adversaire
        interface.affichageMenu(self)
        interface.affichage_image(100,400,self)
        interface.affichage_image_adv(620,400,joueur_adv)
            
        # Affiche le texte 
        texte.Texte("Tu as décidé de combattre un joueur. Le celebre ", couleur.Couleur().getNoir(), 110, 600).affiche(interface.getPolice(),interface.getFenetre())
        texte.Texte("{}. Prepare toi à le combattre afin de prendre".format(joueur_adv.get_prenom()), couleur.Couleur().getNoir(), 110, 620).affiche(interface.getPolice(),interface.getFenetre())
        texte.Texte("l'avantage sur lui !", couleur.Couleur().getNoir(), 110, 640).affiche(interface.getPolice(),interface.getFenetre())
        pygame.time.delay(1500)

        image_Arene = pygame.image.load("./assets/img/ennemis/Arene.png")
        image_redimensionnee = pygame.transform.scale(image_Arene, (800, 500))
        interface.affichageCombat(image_redimensionnee, (0, 0))
        interface.affichageMenu(self)
        interface.affichage_image(100,400,self)
        interface.affichage_image_adv(620,400,joueur_adv)
        texte.Texte("Que veux-tu faire ? Une attaque basique, une ", couleur.Couleur().getNoir(), 110, 600).affiche(interface.getPolice(),interface.getFenetre())
        texte.Texte("attaque speciale, te defendre ou prendre", couleur.Couleur().getNoir(), 110, 620).affiche(interface.getPolice(),interface.getFenetre())
        texte.Texte("la fuite ?", couleur.Couleur().getNoir(), 110, 640).affiche(interface.getPolice(),interface.getFenetre())
        image.Image(100,508,'assets/img/illustrations/Basique.png').affiche(interface)
        image.Image(250,508,'assets/img/illustrations/Speciale.png').affiche(interface)
        image.Image(400,508,'assets/img/illustrations/Defense.png').affiche(interface)
        image.Image(550,508,'assets/img/illustrations/Fuite.png').affiche(interface)
        
        combat_en_cours = True
        # Tant que l'ennemis est en vie
        while combat_en_cours:
            if self.getPv()<=0:
                self.setPv(0)
                joueur_adv.set_inventaire(joueur_adv.get_inventaire() + self.get_inventaire())
                interface.affichageMenu(self)
                interface.affichage_image(100,400,self)
                interface.affichage_image_adv(620,400,joueur_adv)
                texte.Texte("Fin du combat... Tu n'as pas survecu",couleur.Couleur().getNoir(),110, 600).affiche(interface.getPolice(),interface.getFenetre())
                texte.Texte("à l'attaque de l'adversaire...",couleur.Couleur().getNoir(),110, 620).affiche(interface.getPolice(),interface.getFenetre())
                texte.Texte("Retour au plateau !",couleur.Couleur().getNoir(),110, 640).affiche(interface.getPolice(),interface.getFenetre())
                combat_en_cours = False
            elif joueur_adv.getPv()<=0:
                joueur_adv.setPv(0)
                interface.affichageMenu(self)
                interface.affichage_image(100,400,self)
                interface.affichage_image_adv(620,400,joueur_adv)
                texte.Texte("Fin du combat... Tu as tué",couleur.Couleur().getNoir(),110, 600).affiche(interface.getPolice(),interface.getFenetre())
                texte.Texte("l'adversaire, bravo.",couleur.Couleur().getNoir(),110, 620).affiche(interface.getPolice(),interface.getFenetre())
                texte.Texte("Retour au plateau !",couleur.Couleur().getNoir(),110, 640).affiche(interface.getPolice(),interface.getFenetre())
                combat_en_cours = False
            elif self.getPv()>0 and joueur_adv.getPv()>0:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: # si le joueur quitte la fenetre # si le joueur quitte la fenetre
                        pygame.quit()
                        exit() 
                    
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:  
                        mouse_x, mouse_y = pygame.mouse.get_pos() 
                        if 100 < mouse_x < 164 and 508 < mouse_y < 572:
                            #action_joueur = "attaque basique"
                            toucher = random.choice([True,False,True])
                            if toucher == True:
                                if self.get_element() == joueur_adv.get_element():
                                    pv = random.randint(self.get_attaque(),self.get_attaque()+20)
                                    joueur_adv.setPv(joueur_adv.getPv()-pv)
                                else:
                                    pv = random.randint(self.get_attaque()-20,self.get_attaque())
                                    joueur_adv.setPv(joueur_adv.getPv()-pv)
                                interface.affichageMenu(self)
                                interface.affichage_image(100,400,self)
                                interface.affichage_image_adv(620,400,joueur_adv)
                                texte.Texte("Tu as choisi de faire une attaque basique,", couleur.Couleur().getNoir(), 110, 600).affiche(interface.getPolice(),interface.getFenetre())
                                texte.Texte("bravo, l'adversaire a perdu {} pvs".format(pv), couleur.Couleur().getNoir(), 110, 620).affiche(interface.getPolice(),interface.getFenetre())
                            else:
                                interface.affichageMenu(self)
                                interface.affichage_image(100,400,self)
                                interface.affichage_image_adv(620,400,joueur_adv)
                                texte.Texte("L'adversaire a esquive le coup, dommage", couleur.Couleur().getNoir(), 110, 600).affiche(interface.getPolice(),interface.getFenetre())
                                texte.Texte("L'adversaire n'a pas perdu de pv", couleur.Couleur().getNoir(), 110, 620).affiche(interface.getPolice(),interface.getFenetre())
                        if 250 < mouse_x < 314 and 508 < mouse_y < 572:
                            #action_joueur = "attaque speciale"
                            toucher = random.choice([True,False])
                            if toucher == True:
                                pv = self.get_attaque()+50
                                joueur_adv.setPv(joueur_adv.getPv()-pv)
                                interface.affichageMenu(self)
                                interface.affichage_image(100,400,self)
                                interface.affichage_image_adv(620,400,joueur_adv)
                                texte.Texte("Tu as choisi de faire une attaque speciale,", couleur.Couleur().getNoir(), 110, 600).affiche(interface.getPolice(),interface.getFenetre())
                                texte.Texte("bravo, l'adversaire a perdu {} pvs".format(pv), couleur.Couleur().getNoir(), 110, 620).affiche(interface.getPolice(),interface.getFenetre())
                            else:
                                interface.affichageMenu(self)
                                interface.affichage_image(100,400,self)
                                interface.affichage_image_adv(620,400,joueur_adv)
                                texte.Texte("L'adversaire a esquive le coup, dommage", couleur.Couleur().getNoir(), 110, 600).affiche(interface.getPolice(),interface.getFenetre())
                                texte.Texte("L'adversaire n'a pas perdu de pv", couleur.Couleur().getNoir(), 110, 620).affiche(interface.getPolice(),interface.getFenetre())
                        if 400 < mouse_x < 464 and 508 < mouse_y < 572:
                            #action_joueur = "se defendre"
                            toucher = random.choice([True,False])
                            if toucher == True:
                                joueur_adv.set_attaque(joueur_adv.get_attaque()-20)
                                interface.affichageMenu(self)
                                interface.affichage_image(100,400,self)
                                interface.affichage_image_adv(620,400,joueur_adv)
                                texte.Texte("Tu as choisi de te defendre, tu fais une", couleur.Couleur().getNoir(), 110, 600).affiche(interface.getPolice(),interface.getFenetre())
                                texte.Texte("grimace au boss et cela reduit les degâts", couleur.Couleur().getNoir(), 110, 620).affiche(interface.getPolice(),interface.getFenetre())
                                texte.Texte("qu'il peut t'infliger." ,couleur.Couleur().getNoir(), 110, 640).affiche(interface.getPolice(),interface.getFenetre())
                            else:
                                interface.affichageMenu(self)
                                interface.affichage_image(100,400,self)
                                interface.affichage_image_adv(620,400,joueur_adv)
                                texte.Texte("L'ennemis n'a pas pris peur, les", couleur.Couleur().getNoir(), 110, 600).affiche(interface.getPolice(),interface.getFenetre())
                                texte.Texte("degâts qu'il t'inflige ne sont pas", couleur.Couleur().getNoir(), 110, 620).affiche(interface.getPolice(),interface.getFenetre())
                                texte.Texte("reduits.", couleur.Couleur().getNoir(), 110, 640).affiche(interface.getPolice(),interface.getFenetre())
                        if 550 < mouse_x < 614 and 508 < mouse_y < 572:
                            #action_joueur = "prendre la fuite"
                            interface.affichageMenu(self)
                            interface.affichage_image(100,400,self)
                            interface.affichage_image_adv(620,400,joueur_adv)
                            texte.Texte("Tu as choisi de prendre la fuite, c'est", couleur.Couleur().getNoir(), 110, 600).affiche(interface.getPolice(),interface.getFenetre())
                            texte.Texte("surement le bon choix retente ta chance plus", couleur.Couleur().getNoir(), 110, 620).affiche(interface.getPolice(),interface.getFenetre())
                            texte.Texte("tard et detruit moi cet adversaire !!!" ,couleur.Couleur().getNoir(), 110, 640).affiche(interface.getPolice(),interface.getFenetre())
                            combat_en_cours = False
                        pygame.time.delay(2500)
                        if self.getPv() >0 and joueur_adv.getPv()>0 and combat_en_cours == True:
                            temp = self ; self = joueur_adv ; joueur_adv = temp
                            image_Arene = pygame.image.load("./assets/img/ennemis/Arene.png")
                            image_redimensionnee = pygame.transform.scale(image_Arene, (800, 500))
                            interface.affichageCombat(image_redimensionnee, (0, 0))
                            interface.affichageMenu(self)
                            interface.affichage_image(100,400,self)
                            interface.affichage_image_adv(620,400,joueur_adv)
                            texte.Texte("Que veux-tu faire ? Une attaque basique, une ", couleur.Couleur().getNoir(), 110, 600).affiche(interface.getPolice(),interface.getFenetre())
                            texte.Texte("attaque speciale, te defendre ou prendre", couleur.Couleur().getNoir(), 110, 620).affiche(interface.getPolice(),interface.getFenetre())
                            texte.Texte("la fuite ?", couleur.Couleur().getNoir(), 110, 640).affiche(interface.getPolice(),interface.getFenetre())
                            image.Image(100,508,'assets/img/illustrations/Basique.png').affiche(interface)
                            image.Image(250,508,'assets/img/illustrations/Speciale.png').affiche(interface)
                            image.Image(400,508,'assets/img/illustrations/Defense.png').affiche(interface)
                            image.Image(550,508,'assets/img/illustrations/Fuite.png').affiche(interface)
    
    def aCles(self) -> bool : 
        """Verifie si le joueur a toutes les cles necessaires."""
        nombre_cles = 0
        for i in self.getInventaire():
            nombre_cles += 1
        if nombre_cles == 4:
            return True
        else:
            return False
    
    def aGagner(self,plateau) -> bool:
        """Verifie si le joueur a gagne en ayant toutes les cles et en etant dans une hutte."""
        gagne = False
        if self.aCles() == True and plateau.getNom(self.getPlateauX(),self.getPlateauY()) == "Hutte":
            gagne = True
        return gagne
    