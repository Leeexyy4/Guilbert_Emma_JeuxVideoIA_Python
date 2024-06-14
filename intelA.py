import pygame
import random
from math import sqrt
import joueur
from utils import image


from enum import Enum

class Nom(Enum):
    """La classe Nom(Enum) regroupe le nom des personnages jouables."""
    WATER = "Ondine"
    GRASS = "Flora"
    ROCK = "Pierre"
    TOWN = "Kevin"
class Element(Enum):
    """La classe Element(Enum) regroupe les 'titres' des personnages jouables"""
    WATER = "de la Riviere"
    GRASS = "de la Foret"
    ROCK = "du Rocher"
    TOWN = "de la Ville"

class IntelA (joueur.Joueur):
    def __init__(self,id:int, plateaux:int, plateauy:int,element:joueur.Element, inventaire:list=[]) -> None:

        self.__id:int = id
        self.__element:joueur.Element = element
        self.__plateaux:int = plateaux
        self.__plateauy:int = plateauy
        self.__pv:int = 700
        self.__attaque:int = 110
        self.__inventaire:list = inventaire
    
    def choix_case_IA(self):
        case_depart = [self.getPlateaux(), self.getPlateauy()]
        case_recompense = {
            "case_rose": {
                "coord": [],
                "probabilite": 0.1,
                "distance": 17
            },
            "case_violet": {
                "coord": [],
                "probabilite": 0.1,
                "distance": 17
            },
            "case_rouge": {
                "coord": [],
                "probabilite": 0.15,
                "distance": 17
            },
            "case_noir": {
                "coord": [],
                "probabilite": 0.01,
                "distance": 17
            },
            "case_bleu": {
                "coord": [],
                "probabilite": 0.02,
                "distance": 17
            },
            "case_orange": {
                "coord": [],
                "probabilite": 0.05,
                "distance": 17
            },
            "case_blanc": {
                "coord": [],
                "probabilite": 0.1,
                "distance": 17
            },
            "case_jaune": {
                "coord": [],
                "probabilite": 0.02,
                "distance": 17
            },
            "case_gris": {
                "coord": [],
                "probabilite": 0.05,
                "distance": 17
            },
            "case_turquoise": {
                "coord": [],
                "probabilite": 0.06,
                "distance": 17
            },
            "case_beige": {
                "coord": [],
                "probabilite": 0.25,
                "distance": 17
            },
            "case_indigo": {
                "coord": [],
                "probabilite": 0.04,
                "distance": 17
            }
        }

        # Les cases où l'IA peut se déplacer
        for i in interface.get_plateau_de_jeu().get_cases_decouvertes():
            distance = sqrt((case_depart[0] - i[0])**2 + (case_depart[1] - i[1])**2)
            if (distance == interface.get_de_jeu().get_face_choisie()):
                if (interface.get_plateau_de_jeu().get_cases(i[0],i[1]) == interface.get_couleur().get_Rose() and distance < case_recompense["case_rose"]["distance"]):
                    case_recompense["case_rose"]["coord"] = ([i[0],i[1]])
                    case_recompense["case_rose"]["distance"] = distance
                elif (interface.get_plateau_de_jeu().get_cases(i[0],i[1]) == interface.get_couleur().get_Rouge() and distance < case_recompense["case_rouge"]["distance"]):
                    case_recompense["case_rouge"]["coord"] = ([i[0],i[1]])
                    case_recompense["case_rouge"]["distance"] = distance
                elif (interface.get_plateau_de_jeu().get_cases(i[0],i[1]) == interface.get_couleur().get_Violet() and distance < case_recompense["case_violet"]["distance"]):
                    case_recompense["case_violet"]["coord"] = ([i[0],i[1]])
                    case_recompense["case_violet"]["distance"] = distance
                elif (interface.get_plateau_de_jeu().get_cases(i[0],i[1]) == interface.get_couleur().get_Bleu() and distance < case_recompense["case_bleu"]["distance"]):
                    case_recompense["case_bleu"]["coord"] = ([i[0],i[1]])
                    case_recompense["case_bleu"]["distance"] = distance
                elif (interface.get_plateau_de_jeu().get_cases(i[0],i[1]) == interface.get_couleur().get_Noir() and distance < case_recompense["case_noir"]["distance"]):
                    case_recompense["case_noir"]["coord"] = ([i[0],i[1]])
                    case_recompense["case_noir"]["distance"] = distance
                elif (interface.get_plateau_de_jeu().get_cases(i[0],i[1]) == interface.get_couleur().get_Orange() and distance < case_recompense["case_orange"]["distance"]):
                    case_recompense["case_orange"]["coord"] = ([i[0],i[1]])
                    case_recompense["case_orange"]["distance"] = distance
                elif (interface.get_plateau_de_jeu().get_cases(i[0],i[1]) == interface.get_couleur().get_Blanc() and distance < case_recompense["case_blanc"]["distance"]):
                    case_recompense["case_blanc"]["coord"] = ([i[0],i[1]])
                    case_recompense["case_blanc"]["distance"] = distance
                elif (interface.get_plateau_de_jeu().get_cases(i[0],i[1]) == interface.get_couleur().get_Indigo() and distance < case_recompense["case_indigo"]["distance"]):
                    case_recompense["case_indigo"]["coord"] = ([i[0],i[1]])
                    case_recompense["case_indigo"]["distance"] = distance
                elif (interface.get_plateau_de_jeu().get_cases(i[0],i[1]) == interface.get_couleur().get_Turquoise() and distance < case_recompense["case_turquoise"]["distance"]):
                    case_recompense["case_turquoise"]["coord"] = ([i[0],i[1]])
                    case_recompense["case_turquoise"]["distance"] = distance
                elif (interface.get_plateau_de_jeu().get_cases(i[0],i[1]) == interface.get_couleur().get_Jaune() and distance < case_recompense["case_jaune"]["distance"]):
                    case_recompense["case_jaune"]["coord"] = ([i[0],i[1]])
                    case_recompense["case_jaune"]["distance"] = distance
                elif (interface.get_plateau_de_jeu().get_cases(i[0],i[1]) == interface.get_couleur().get_Gris() and distance < case_recompense["case_gris"]["distance"]):
                    case_recompense["case_gris"]["coord"] = ([i[0],i[1]])
                    case_recompense["case_gris"]["distance"] = distance
                elif (interface.get_plateau_de_jeu().get_cases(i[0],i[1]) == interface.get_couleur().get_Beige() and distance < case_recompense["case_beige"]["distance"]):
                    case_recompense["case_beige"]["coord"] = ([i[0],i[1]])
                    case_recompense["case_beige"]["distance"] = distance
        

        liste_case = case_recompense.keys()
        liste_temp = []
        # Condition pour que l'IA se déplace sur les cases accessibles en fonction de la situation du jeu
        for i in liste_case:
            if case_recompense[i]["distance"] != 17:
                liste_temp.append(i)
        liste_case = liste_temp
        if (self.avoir_tt_cles() != True and "case_beige" in liste_case):
            liste_case.remove("case_beige")
        if (interface.get_plateau_de_jeu().get_cases(self.get_plateaux(),self.get_plateauy()) == interface.get_couleur().get_Jaune() and "case_jaune" in liste_case):
            liste_case.remove("case_jaune")
        case_recompense["case_rose"]["coord"]

        liste_proba = [case_recompense[choice]['probabilite'] for choice in liste_case]
        
        # Faire un choix aléatoire en utilisant random.choices avec les probabilités
        case_arrivee = case_recompense[random.choices(liste_case, weights=liste_proba)[0]]["coord"]

        while interface.get_de_jeu().get_face_choisie() != 0:
            if self.get_plateaux() < case_arrivee[0]:
                # La touche fleche vers le haut a ete enfoncee
                self.haut(47)
                interface.get_plateau_de_jeu().set_cases_decouvertes(interface.get_plateau_de_jeu().get_cases_decouvertes() + [[self.get_plateaux(),self.get_plateauy()]])
                interface.Mise_a_jour(self)
                interface.plateau_cache()
                interface.affichage_image_plateau(self)
                interface.get_de_jeu().desincrement_face_choisie(1)
                        
            elif self.get_plateaux() > case_arrivee[0]:
                # La touche fleche vers le bas a ete enfoncee
                self.bas(47)
                interface.get_plateau_de_jeu().set_cases_decouvertes(interface.get_plateau_de_jeu().get_cases_decouvertes() + [[self.get_plateaux(),self.get_plateauy()]])
                interface.Mise_a_jour(self)
                interface.plateau_cache()
                interface.affichage_image_plateau(self)
                interface.get_de_jeu().desincrement_face_choisie(1)
            
            elif self.get_plateauy() < case_arrivee[1]:
                # La touche fleche vers la droite a ete enfoncee
                self.droite(47) 
                interface.get_plateau_de_jeu().set_cases_decouvertes(interface.get_plateau_de_jeu().get_cases_decouvertes() + [[self.get_plateaux(),self.get_plateauy()]])
                interface.Mise_a_jour(self) 
                interface.plateau_cache()
                interface.affichage_image_plateau(self)
                interface.get_de_jeu().desincrement_face_choisie(1)

            elif self.get_plateauy() > case_arrivee[1]:
                # La touche fleche vers la gauche a ete enfoncee
                self.gauche(47) 
                interface.get_plateau_de_jeu().set_cases_decouvertes(interface.get_plateau_de_jeu().get_cases_decouvertes() + [[self.get_plateaux(),self.get_plateauy()]])  
                interface.Mise_a_jour(self)                
                interface.plateau_cache()
                interface.affichage_image_plateau(self)
                interface.get_de_jeu().desincrement_face_choisie(1)      
            pygame.display.update()   
