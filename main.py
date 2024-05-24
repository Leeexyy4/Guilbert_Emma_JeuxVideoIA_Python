#Guilbert
#Emma



# ----------------------- Jeu de plateau - SAE C1 Main ------------------------ #

#pour les images : Pierre et Pierre2 creees par Freepik - site web Flaticon
#                  Flora et Flora2 creees par Freepik - site web Flaticon
#                  Ondine et Ondine2 = creees par Freepik - site web Flaticon
#                  Kevin et Kevin2  = creees par Freepik - site web Flaticon
#                  Crapaud et Crapaud2 = creees par Freepik - site web Flaticon
#                  Ecureil et Ecureil2 = creees par Freepik - site web Flaticon
#                  Lezard et Lezard2 = creees par Freepik - site web Flaticon
#                  Rat et Rat2 = creees par Freepik - site web Flaticon
#                  J1, J2, J3 et J4 = site web Alarmy Stock Photo


# ----------------------- Jeu de plateau - Bibliotheques  ------------------------ #

# Bibliotheques utilisees pour le code
import pygame # Importation de la bibliotheque pygame
from model.jeu import interfaces
from model.visuel import texte, couleur, image, rectangle
from model.personnage import ennemis, joueur
import random # Importation de la bibliotheque aleatoire

# ----------------------- Jeu de plateau - Logique du jeu ------------------------ #
     
if __name__ == "__main__":
    # Initialisation de Pygame
    pygame.init()
    
    page = interfaces.Interface()
    # etat initial du jeu
    etat_jeu = "demarrage_jeu"
    # Pour tous les joueurs encore en vie
    while etat_jeu != "fin_du_jeu": 
        # Gerer les etats du jeu
        
        while etat_jeu == "demarrage_jeu": # si le jeu demarre
            page.Page_demarrage()
            etat_jeu = "lancement_jeu"
            
        while etat_jeu == "lancement_jeu":  # si le joueur a clique sur start + affichage plateau
            # Affiche a page pour choisir le nombre de joueurs
            page.Page_nb_joueur()
            while page.get_nb_joueur() == 5:
                page.Page_demarrage()
                page.Page_nb_joueur()
            
            # tant qu'on a pas atteint le nombre final de joueur
            for numero_joueur in range(page.get_nb_joueur()):
                # Afficher la proposition pour choisir le personnage
                prenom, element = page.Page_choixperso()
                while prenom == "Aucun":
                    page.Page_nb_joueur()
                    while page.get_nb_joueur() == 5:
                        page.Page_nb_joueur()
                    prenom, element = page.Page_choixperso()
                un_joueur = joueur.Joueur(numero_joueur,prenom,element,page.get_plateau_de_jeu().get_case_jaune()[0],page.get_plateau_de_jeu().get_case_jaune()[1])
                page.get_plateau_de_jeu().set_cases_decouvertes(page.get_plateau_de_jeu().get_cases_decouvertes() + [[page.get_plateau_de_jeu().get_case_jaune()[0],page.get_plateau_de_jeu().get_case_jaune()[1]]])
                image.Image(0,0,'assets/img/illustrations/Page_jeu.png').affichage_image_redimensionnee(800, 700,page.get_fenetre())
                page.Menu_bas(un_joueur) # Affiche le plateau de jeu avec le personnage choisi
                page.Page_premier_mouvement(un_joueur)
                page.get_plateau_de_jeu().plateau_cache(page.get_fenetre())
                page.get_plateau_de_jeu().mise_a_jour_plateau(page.get_fenetre())
                page.set_liste_joueur(page.get_liste_joueur() + [[un_joueur.get_id(), un_joueur.get_prenom(), un_joueur.get_element(), un_joueur.get_plateaux(), un_joueur.get_plateauy(), un_joueur.get_pv(), un_joueur.get_inventaire()]])
                un_joueur.affiche_tt_joueur(page.get_liste_joueur(),page.get_fenetre())
                page.Page_direction(un_joueur)
                page.Mise_a_jour(un_joueur)
                un_joueur.affiche_tt_joueur(page.get_liste_joueur(),page.get_fenetre())
                page.Page_action(un_joueur)
                pygame.time.delay(3400)
                page.Menu_bas(un_joueur)
                page.get_plateau_de_jeu().plateau_cache(page.get_fenetre())
                page.get_plateau_de_jeu().mise_a_jour_plateau(page.get_fenetre())
                un_joueur.affiche_tt_joueur(page.get_liste_joueur(),page.get_fenetre())
                numero_joueur = numero_joueur + 1
                prenom = ""
                if un_joueur.a_gagne(page.get_plateau_de_jeu()) == True:
                    etat_jeu = "fin_du_jeu"
                else:
                    etat_jeu = "partie_en_cours"    

        while etat_jeu == "partie_en_cours":
            if page.get_liste_joueur() != []:
                for i in page.get_liste_joueur():
                    numero_joueur = i[0]
                    un_joueur = joueur.Joueur(i[0],i[1],i[2],i[3],i[4])
                    un_joueur.set_pv(i[5])
                    if un_joueur.get_pv()>=0:
                        un_joueur.set_inventaire(i[6])
                        un_joueur.affiche_tt_joueur(page.get_liste_joueur(),page.get_fenetre())
                        action_joueur = page.Page_mouvement(un_joueur)
                        
                        # Si le joueur veut attaquer
                        if action_joueur == "Attaquer":
                            if un_joueur.adv_a_attaquer(page.get_liste_joueur()) == True:
                                un_joueur.adv_a_attaquer(page.get_liste_joueur())
                                ordre_adv = un_joueur.adv_nom_attaquer(page.get_liste_joueur())
                                if ordre_adv != -1:
                                    un_joueur.combat_joueurs(page, ordre_adv)
                            else:
                                page.Menu_bas(un_joueur) # Affiche le plateau de jeu avec le personnage choisi
                                texte.Texte("Personne n'est assez proche de toi pour ",couleur.Couleur().get_Noir(),110,600).affiche(page.get_police(),page.get_fenetre())
                                texte.Texte("être attaquer. Rééssaye quand le joueur",couleur.Couleur().get_Noir(),110,620).affiche(page.get_police(),page.get_fenetre())
                                texte.Texte("adverse sera plus proche de toi.",couleur.Couleur().get_Noir(),110,640).affiche(page.get_police(),page.get_fenetre())
                                pygame.display.update()
                                pygame.time.delay(2000)
                            page.Menu_bas(un_joueur)
                            page.get_plateau_de_jeu().plateau_cache(page.get_fenetre())
                            page.get_plateau_de_jeu().mise_a_jour_plateau(page.get_fenetre())
                            un_joueur.affiche_tt_joueur(page.get_liste_joueur(),page.get_fenetre())
                        else:
                        # Sinon le joueur lance le dé
                            page.Menu_bas(un_joueur) # Affiche le plateau de jeu avec le personnage choisi
                            texte.Texte("Clique sur le de ! ",couleur.Couleur().get_Noir(),110,600).affiche(page.get_police(),page.get_fenetre())
                            un_joueur.affiche_tt_joueur(page.get_liste_joueur(),page.get_fenetre())
                            page.Page_direction(un_joueur)
                            pygame.display.update()
                            page.Mise_a_jour(un_joueur)
                            un_joueur.affiche_tt_joueur(page.get_liste_joueur(),page.get_fenetre())
                            page.Page_action(un_joueur)
                            pygame.time.delay(3400)
                            page.Menu_bas(un_joueur)
                            page.get_plateau_de_jeu().plateau_cache(page.get_fenetre())
                            page.get_plateau_de_jeu().mise_a_jour_plateau(page.get_fenetre())
                            un_joueur.affiche_tt_joueur(page.get_liste_joueur(),page.get_fenetre())
                            if un_joueur.a_gagne(page.get_plateau_de_jeu()) == True:
                                etat_jeu = "fin_du_jeu"
                            else:
                                etat_jeu = "partie_en_cours"
                    else:
                        page.set_liste_joueur(page.get_liste_joueur().pop(un_joueur.get_id()))
                        un_joueur.affiche_tt_joueur(page.get_liste_joueur(),page.get_fenetre())
                        texte.Texte("Tu es mort au combat, reviens vite ",couleur.Couleur().get_Noir(),110,600).affiche(page.get_police(),page.get_fenetre())
                        texte.Texte("tenter ta chance jeune aventurier !",couleur.Couleur().get_Noir(),110,620).affiche(page.get_police(),page.get_fenetre())
                        pygame.display.update()
                        pygame.time.delay(3400)
                        page.Menu_bas(un_joueur)
                        page.get_plateau_de_jeu().plateau_cache(page.get_fenetre())
                        page.get_plateau_de_jeu().mise_a_jour_plateau(page.get_fenetre())
                        un_joueur.affiche_tt_joueur(page.get_liste_joueur(),page.get_fenetre())
            else: 
                etat_jeu = "fin_du_jeu"

        if etat_jeu == "fin_du_jeu":
            if un_joueur.a_gagne(page.get_plateau_de_jeu()) == True:
                un_joueur.set_inventaire([])
                page.Page_sorciere(un_joueur)
                pygame.quit()
