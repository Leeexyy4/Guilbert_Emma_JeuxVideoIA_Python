import pygame, math, random
from random import randint
from classe.personnage import joueur
from classe.visuel import image

class IntelA (joueur.Joueur):
    def __init__(self, id, prenom, element, plateaux, plateauy, pv, attaque, inventaire) -> None:
        super().__init__(id, prenom, element, plateaux, plateauy, pv, attaque, inventaire)
    
    def definitionPersonnageIA(self, interface):
        pass

    def lancementDeIA(self, interface) -> int:
        de_cliquer = False
        while de_cliquer == False:
            # Affiche le de sur la face 2
            de_face2 = image.De.FACE2.value
            interface.affichageAction(de_face2)
            pygame.time.delay(150)
            
            # Affiche le de sur la face 3
            de_face3 = image.De.FACE3.value
            interface.affichageAction(de_face3)
            pygame.time.delay(200)
            
            # Affiche le de sur la face 4
            de_face4 = image.De.FACE4.value
            interface.affichageAction(de_face4)
            pygame.time.delay(250)
            
            # Affiche le de sur la face 5
            de_face5 = image.De.FACE5.value
            interface.affichageAction(de_face5)
            pygame.time.delay(300)
            
            # Affiche le de sur la face 1
            de_face1 = image.De.FACE1.value
            interface.affichageAction(de_face1)
            pygame.time.delay(400)
            
            # Affiche le de sur la face 6
            de_face6 = image.De.FACE6.value
            interface.affichageAction(de_face6)
            pygame.time.delay(450)
            de_cliquer = True 
        # Choisir la face aleatoire
        interface.get_de_jeu().set_face_choisie(randint(1,6))

        if interface.get_de_jeu().get_face_choisie() == 1:
            # Affiche le de sur la face 1
            de_face1 = image.De.FACE1.value
            interface.affichageAction(de_face1)
            
    
        elif interface.get_de_jeu().get_face_choisie() == 2:
            # Affiche le de sur la face 2
            de_face2 = image.De.FACE2.value
            interface.affichageAction(de_face2)
            
    
        elif interface.get_de_jeu().get_face_choisie() == 3:
            # Affiche le de sur la face 3
            de_face3 = image.De.FACE3.value
            interface.affichageAction(de_face3)
            
    
        elif interface.get_de_jeu().get_face_choisie() == 4:
            # Affiche le de sur la face 4
            de_face4 = image.De.FACE4.value
            interface.affichageAction(de_face4)
            
    
        elif interface.get_de_jeu().get_face_choisie() == 5:
            # Affiche le de sur la face 5
            de_face5 = image.De.FACE5.value
            interface.affichageAction(de_face5)
            
    
        elif interface.get_de_jeu().get_face_choisie() == 6:
            # Affiche le de sur la face 6
            de_face6 = image.De.FACE6.value
            interface.affichageAction(de_face6)
            
    
        return interface.get_de_jeu().get_face_choisie()
                

       
    def choixDirectionIA(self, interface):
        case_depart = [self.getPlateauX(), self.getPlateauY()]
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
            "case_vert": {
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
        for i in interface.getPlateauJeu().getCasesDecouvertes():
            distance = math.sqrt((case_depart[0] - i[0])**2 + (case_depart[1] - i[1])**2)
            if (distance == interface.get_de_jeu().get_face_choisie()):
                if (interface.getPlateauJeu().get_cases(i[0],i[1]) == interface.getCouleur().getRose() and distance < case_recompense["case_rose"]["distance"]):
                    case_recompense["case_rose"]["coord"] = ([i[0],i[1]])
                    case_recompense["case_rose"]["distance"] = distance
                elif (interface.getPlateauJeu().get_cases(i[0],i[1]) == interface.getCouleur().get_Rouge() and distance < case_recompense["case_rouge"]["distance"]):
                    case_recompense["case_rouge"]["coord"] = ([i[0],i[1]])
                    case_recompense["case_rouge"]["distance"] = distance
                elif (interface.getPlateauJeu().get_cases(i[0],i[1]) == interface.getCouleur().get_Violet() and distance < case_recompense["case_violet"]["distance"]):
                    case_recompense["case_violet"]["coord"] = ([i[0],i[1]])
                    case_recompense["case_violet"]["distance"] = distance
                elif (interface.getPlateauJeu().get_cases(i[0],i[1]) == interface.getCouleur().get_Bleu() and distance < case_recompense["case_bleu"]["distance"]):
                    case_recompense["case_bleu"]["coord"] = ([i[0],i[1]])
                    case_recompense["case_bleu"]["distance"] = distance
                elif (interface.getPlateauJeu().get_cases(i[0],i[1]) == interface.getCouleur().getNoir() and distance < case_recompense["case_noir"]["distance"]):
                    case_recompense["case_noir"]["coord"] = ([i[0],i[1]])
                    case_recompense["case_noir"]["distance"] = distance
                elif (interface.getPlateauJeu().get_cases(i[0],i[1]) == interface.getCouleur().get_Orange() and distance < case_recompense["case_orange"]["distance"]):
                    case_recompense["case_orange"]["coord"] = ([i[0],i[1]])
                    case_recompense["case_orange"]["distance"] = distance
                elif (interface.getPlateauJeu().get_cases(i[0],i[1]) == interface.getCouleur().getBlanc() and distance < case_recompense["case_blanc"]["distance"]):
                    case_recompense["case_blanc"]["coord"] = ([i[0],i[1]])
                    case_recompense["case_blanc"]["distance"] = distance
                elif (interface.getPlateauJeu().get_cases(i[0],i[1]) == interface.getCouleur().get_Indigo() and distance < case_recompense["case_indigo"]["distance"]):
                    case_recompense["case_indigo"]["coord"] = ([i[0],i[1]])
                    case_recompense["case_indigo"]["distance"] = distance
                elif (interface.getPlateauJeu().get_cases(i[0],i[1]) == interface.getCouleur().get_Vert() and distance < case_recompense["case_vert"]["distance"]):
                    case_recompense["case_vert"]["coord"] = ([i[0],i[1]])
                    case_recompense["case_vert"]["distance"] = distance
                elif (interface.getPlateauJeu().get_cases(i[0],i[1]) == interface.getCouleur().get_Jaune() and distance < case_recompense["case_jaune"]["distance"]):
                    case_recompense["case_jaune"]["coord"] = ([i[0],i[1]])
                    case_recompense["case_jaune"]["distance"] = distance
                elif (interface.getPlateauJeu().get_cases(i[0],i[1]) == interface.getCouleur().getGris() and distance < case_recompense["case_gris"]["distance"]):
                    case_recompense["case_gris"]["coord"] = ([i[0],i[1]])
                    case_recompense["case_gris"]["distance"] = distance
                elif (interface.getPlateauJeu().get_cases(i[0],i[1]) == interface.getCouleur().get_Beige() and distance < case_recompense["case_beige"]["distance"]):
                    case_recompense["case_beige"]["coord"] = ([i[0],i[1]])
                    case_recompense["case_beige"]["distance"] = distance
        

        # Filtrer les cases qui ont des coordonnées valides et une probabilité > 0
        liste_case = [i for i in case_recompense if case_recompense[i]["coord"] and case_recompense[i]["probabilite"] > 0]

        if (self.avoir_tt_cles() != True and "case_beige" in liste_case):
            liste_case.remove("case_beige")
        if (interface.getPlateauJeu().get_cases(self.getPlateauX(),self.getPlateauY()) == interface.getCouleur().get_Jaune() and "case_jaune" in liste_case):
            liste_case.remove("case_jaune")
        case_recompense["case_rose"]["coord"]
        
         # Générer les probabilités pour les cases valides
        liste_proba = [case_recompense[choice]['probabilite'] for choice in liste_case]

        # Vérifier si les listes sont non vides
        if not liste_case or not liste_proba:
            print("Aucune case valide ou probabilité trouvée.")
            return None
        assert len(liste_case) == len(liste_proba), "Les longueurs de liste_case et liste_proba ne correspondent pas"
        
        # Sélection aléatoire de la case d'arrivée
        case_arrivee = case_recompense[random.choices(liste_case, weights=liste_proba)[0]]["coord"]


        while interface.get_de_jeu().get_face_choisie() != 0:
            if self.getPlateauX() < case_arrivee[0]:
                # La touche fleche vers le haut a ete enfoncee
                self.haut(47)
                interface.getPlateauJeu().setCasesDecouvertes(interface.getPlateauJeu().getCasesDecouvertes() + [[self.getPlateauX(),self.getPlateauY()]])
                
                interface.affichage_image_plateau(self)
                interface.get_de_jeu().desincrement_face_choisie(1)
                
                        
            elif self.getPlateauX() > case_arrivee[0]:
                # La touche fleche vers le bas a ete enfoncee
                self.bas(47)
                interface.getPlateauJeu().setCasesDecouvertes(interface.getPlateauJeu().getCasesDecouvertes() + [[self.getPlateauX(),self.getPlateauY()]])
                
                interface.affichage_image_plateau(self)
                interface.get_de_jeu().desincrement_face_choisie(1)
            
            elif self.getPlateauY() < case_arrivee[1]:
                # La touche fleche vers la droite a ete enfoncee
                self.droite(47) 
                interface.getPlateauJeu().setCasesDecouvertes(interface.getPlateauJeu().getCasesDecouvertes() + [[self.getPlateauX(),self.getPlateauY()]])
                
                interface.affichage_image_plateau(self)
                interface.get_de_jeu().desincrement_face_choisie(1)

            elif self.getPlateauY() > case_arrivee[1]:
                # La touche fleche vers la gauche a ete enfoncee
                self.gauche(47) 
                interface.getPlateauJeu().setCasesDecouvertes(interface.getPlateauJeu().getCasesDecouvertes() + [[self.getPlateauX(),self.getPlateauY()]])  
                
                interface.affichage_image_plateau(self)
                interface.get_de_jeu().desincrement_face_choisie(1)      
                pygame.time.delay(1500)


    def choixActionCombatIA(self, interface):
        if self.adv_a_attaquer(interface.getListeJoueur()) == True:
            self.adv_a_attaquer(interface.getListeJoueur())
            ordre_adv = self.adv_nom_attaquer(interface.getListeJoueur())
            if ordre_adv != -1:
                self.combat_joueurs(interface, ordre_adv)
        else:
            for k in interface.getListeJoueur():
                if (interface.getPlateauJeu().getCasesDecouvertes()[k.getPlateauX()][k.getPlateauY()] != "case_rouge"):
                    self.choix_case_IA(interface)