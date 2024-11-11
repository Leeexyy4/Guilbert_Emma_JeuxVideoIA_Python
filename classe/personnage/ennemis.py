# ----------------------- Jeu de plateau - Joueur  ------------------------ #

# Bibliothèques utilisées pour le code
import random

class Ennemis:
    """La classe Ennemis est une classe qui permet de créer un ennemi."""
    
    def __init__(self, prenom, element) -> None:
        """Initialisation de l'ennemi."""
        self.__x = 620
        self.__y = 400
        self.__prenom = prenom
        self.__lien = "./assets/img/ennemis/" + prenom + ".png"
        self.__pv = 1500
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
    
    def getPv(self):
        """Getter des points de vie de l'ennemi."""
        return self.__pv
    
    def get_attaque(self):
        """Getter de l'attaque de l'ennemi."""
        return self.__attaque
    
    def get_element(self):
        """Getter de l'élément de l'ennemi."""
        return self.__element
    
    def setX(self, x):
        """Setter de la position x."""
        self.__x = x
    
    def setY(self, y):
        """Setter de la position y."""
        self.__y = y
        
    def set_prenom(self, prenom):
        """Setter du prénom de l'ennemi."""
        self.__prenom = prenom
    
    def set_lien(self, lien):
        """Setter du lien de l'image de l'ennemi."""
        self.__lien = lien
    
    def setPv(self, pv):
        """Setter des points de vie de l'ennemi."""
        self.__pv = pv
        
    def set_element(self, element):
        """Setter de l'élément de l'ennemi."""
        self.__element = element
    
    def set_attaque(self, attaque):
        """Setter de l'attaque de l'ennemi."""
        self.__attaque = attaque
    
def Choix_ennemis(joueurActuel):
    """Choisit un ennemi en fonction des clés obtenues par le joueur."""
    liste_ennemis = ["Ecureuil", "Crapaud", "Lezard", "Rat"]
    for i in joueurActuel.get_inventaire():
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
