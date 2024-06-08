import pygame
import random
from math import sqrt
from classe.personnage import joueur
from classe.visuel import image

class IntelA (joueur.Joueur):
    def __init__(self, id, prenom, element, plateaux, plateauy, pv, attaque, inventaire) -> None:
        super().__init__(id, prenom, element, plateaux, plateauy, pv, attaque, inventaire)

    def lancement_de_IA(self, interface) -> int:
        de_cliquer = False
        while de_cliquer == False:
            # Affiche le de sur la face 2
            de_face2 = image.De.FACE2.value
            interface.get_fenetre().blit(de_face2,(350,475))
            # Mettre à jour l'affichage
            pygame.display.update()
            pygame.time.delay(150)
            
            # Affiche le de sur la face 3
            de_face3 = image.De.FACE3.value
            interface.get_fenetre().blit(de_face3,(350,475))
            # Mettre à jour l'affichage
            pygame.display.update()
            pygame.time.delay(200)
            
            # Affiche le de sur la face 4
            de_face4 = image.De.FACE4.value
            interface.get_fenetre().blit(de_face4,(350,475))
            # Mettre à jour l'affichage
            pygame.display.update()
            pygame.time.delay(250)
            
            # Affiche le de sur la face 5
            de_face5 = image.De.FACE5.value
            interface.get_fenetre().blit(de_face5,(350,475))
            # Mettre à jour l'affichage
            pygame.display.update()
            pygame.time.delay(300)
            
            # Affiche le de sur la face 1
            de_face1 = image.De.FACE1.value
            interface.get_fenetre().blit(de_face1,(350,475))
            # Mettre à jour l'affichage
            pygame.display.update()
            pygame.time.delay(400)
            
            # Affiche le de sur la face 6
            de_face6 = image.De.FACE6.value
            interface.get_fenetre().blit(de_face6,(350,475))
            # Mettre à jour l'affichage
            pygame.display.update()
            pygame.time.delay(450)
            de_cliquer = True 
        # Choisir la face aleatoire
        interface.get_de_jeu().set_face_choisie(random.randint(1,6))

        if interface.get_de_jeu().get_face_choisie() == 1:
            # Affiche le de sur la face 1
            de_face1 = image.De.FACE1.value
            interface.get_fenetre().blit(de_face1,(350,475))
            # Mettre à jour l'affichage
            pygame.display.update()

        elif interface.get_de_jeu().get_face_choisie() == 2:
            # Affiche le de sur la face 2
            de_face2 = image.De.FACE2.value
            interface.get_fenetre().blit(de_face2,(350,475))
            # Mettre à jour l'affichage
            pygame.display.update()

        elif interface.get_de_jeu().get_face_choisie() == 3:
            # Affiche le de sur la face 3
            de_face3 = image.De.FACE3.value
            interface.get_fenetre().blit(de_face3,(350,475))
            # Mettre à jour l'affichage
            pygame.display.update()

        elif interface.get_de_jeu().get_face_choisie() == 4:
            # Affiche le de sur la face 4
            de_face4 = image.De.FACE4.value
            interface.get_fenetre().blit(de_face4,(350,475))
            # Mettre à jour l'affichage
            pygame.display.update()

        elif interface.get_de_jeu().get_face_choisie() == 5:
            # Affiche le de sur la face 5
            de_face5 = image.De.FACE5.value
            interface.get_fenetre().blit(de_face5,(350,475))
            # Mettre à jour l'affichage
            pygame.display.update()

        elif interface.get_de_jeu().get_face_choisie() == 6:
            # Affiche le de sur la face 6
            de_face6 = image.De.FACE6.value
            interface.get_fenetre().blit(de_face6,(350,475))
            # Mettre à jour l'affichage
            pygame.display.update()

        return interface.get_de_jeu().get_face_choisie()
                
    def choix_case_IA(self, interface):
        case_depart = [self.get_plateaux(),self.get_plateauy()]
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
        

        liste_case = list(case_recompense.keys())
        # Si l'IA n'a pas toutes les clés ne pas se rendre sur la case sorcière
        if (self.avoir_tt_cles() != True):
            liste_case.pop(10)

        liste_proba = [case_recompense[choice]['probabilite'] for choice in liste_case]
        
        # Faire un choix aléatoire en utilisant random.choices avec les probabilités
        case_arrivee = case_recompense[random.choices(liste_case, weights=liste_proba)[0]]["coord"]

        print(case_arrivee)

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
            pygame.time.delay(1000) 
