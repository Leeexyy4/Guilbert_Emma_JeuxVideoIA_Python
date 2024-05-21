# ----------------------- Jeu de plateau - Joueur  ------------------------ #

# Bibliothèques utilisées pour le code
import pygame, rectangle, texte, couleur, random, joueur

class Ennemis:
    """La classe Ennemis est une classe qui permet de créer un ennemi."""
    
    def __init__(self, prenom, element) -> None:
        """Initialisation de l'ennemi."""
        self.__x = 620
        self.__y = 400
        self.__prenom = prenom
        self.__lien = "./assets/img/ennemis/" + prenom + ".png"
        self.__pv = 750
        self.__attaque = 110
        self.__element = element
    
    def get_x(self):
        """Getter de la position x."""
        return self.__x
    
    def get_y(self):
        """Getter de la position y."""
        return self.__y
    
    def get_prenom(self):
        """Getter du prénom de l'ennemi."""
        return self.__prenom
    
    def get_lien(self):
        """Getter du lien de l'image de l'ennemi."""
        return self.__lien
    
    def get_pv(self):
        """Getter des points de vie de l'ennemi."""
        return self.__pv
    
    def get_attaque(self):
        """Getter de l'attaque de l'ennemi."""
        return self.__attaque
    
    def get_element(self):
        """Getter de l'élément de l'ennemi."""
        return self.__element
    
    def set_x(self, x):
        """Setter de la position x."""
        self.__x = x
    
    def set_y(self, y):
        """Setter de la position y."""
        self.__y = y
        
    def set_prenom(self, prenom):
        """Setter du prénom de l'ennemi."""
        self.__prenom = prenom
    
    def set_lien(self, lien):
        """Setter du lien de l'image de l'ennemi."""
        self.__lien = lien
    
    def set_pv(self, pv):
        """Setter des points de vie de l'ennemi."""
        self.__pv = pv
        
    def set_element(self, element):
        """Setter de l'élément de l'ennemi."""
        self.__element = element
    
    def set_attaque(self, attaque):
        """Setter de l'attaque de l'ennemi."""
        self.__attaque = attaque
        
    def affichage_image(self, surface, font):
        """Affiche l'image de l'ennemi dans le menu."""
        image = pygame.image.load(self.get_lien())
        surface.blit(image, (self.get_x(), self.get_y()))
        rectangle.Rectangle(500, 635, 130, 35).affiche(surface, couleur.Couleur().get_Rouge())
        texte.Texte(self.get_pv(), couleur.Couleur().get_Noir(), 538, 644).affiche(font, surface)
        pygame.display.update()
    
    def affichage_image_plateau(self, x, y, surface):
        """Affiche l'image de l'ennemi sur le plateau."""
        image = pygame.image.load(self.get_lien())
        image_redimensionnee = pygame.transform.scale(image, (47, 47))
        surface.blit(image_redimensionnee, (x, y))
        pygame.display.update()

    def affichage_pv_combat(self, surface, font):
        """Affiche les points de vie de l'ennemi en combat."""
        rectangle.Rectangle(500, 635, 130, 35).affiche(surface, couleur.Couleur().get_Rouge())
        texte.Texte(self.get_pv(), couleur.Couleur().get_Noir(), 538, 643).affiche(font, surface)
        pygame.display.update()

def Choix_ennemis(un_joueur):
    """Choisit un ennemi en fonction des clés obtenues par le joueur."""
    liste_ennemis = ["Ecureuil", "Crapaud", "Lezard", "Rat"]
    for i in un_joueur.get_inventaire():
        if i == "clé du Rocher":
            liste_ennemis.remove("Lezard")
        elif i == "clé de la Forêt":
            liste_ennemis.remove("Ecureuil")
        elif i == "clé de la Ville":
            liste_ennemis.remove("Rat")
        elif i == "clé de la Rivière":
            liste_ennemis.remove("Crapaud")
            
    ennemis_select = random.choice(liste_ennemis)
    if ennemis_select == "Rat":
        un_ennemi = Ennemis("Rat", "de la Ville")
    elif ennemis_select == "Crapaud":
        un_ennemi = Ennemis("Crapaud", "de la Rivière")
    elif ennemis_select == "Ecureuil":
        un_ennemi = Ennemis("Ecureuil", "de la Forêt")
    elif ennemis_select == "Lezard":
        un_ennemi = Ennemis("Lezard", "du Rocher")
    return un_ennemi

# Tests des fonctions
if __name__ == "__main__":
    font = pygame.font.Font('./assets/font/times-new-roman.ttf', 16)

    pygame.init()
    un_joueur = joueur.Joueur(1, "Ondine", "de la Rivière", 1, 2)
    fenetre = pygame.display.set_mode((800, 700))
    un_ennemi = Choix_ennemis(un_joueur)
    un_ennemi.affichage_image(fenetre, font)
    pygame.display.update()
    pygame.time.delay(3500)
