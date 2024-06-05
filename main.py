#BEAUREPAIRE Paul
#GUILBERT Emma
#VAXELAIRE Yohem
#VERFAILLIE Alexis


# ----------------------- Jeu de plateau - Bibliotheques  ------------------------ #

# Bibliotheques utilisees pour le code
import pygame
from classe.jeu import interfaces
from classe.visuel import texte, couleur, image
from classe.personnage import joueur, intelA

# ----------------------- Jeu de plateau - Logique du jeu ------------------------ #

if __name__ == "__main__":
    # Initialisation de Pygame
    pygame.init()
    
    page = interfaces.Interface()
    page.Page_demarrage()
    # Pour tous les joueurs encore en vie
    while page.get_etat_de_jeu() != "fin_du_jeu": 
        # Gerer les etats du jeu
        if page.get_etat_de_jeu() == "demarrage_jeu": # si le jeu demarre
            if page.get_nb_joueur() > 0:  # si le nombre de joueur est choisi
                for numero_joueur in range(page.get_nb_joueur()):
                    # Afficher la proposition pour choisir le personnage
                    prenom, element = page.Page_choixperso()
                    un_joueur = joueur.Joueur(numero_joueur,prenom,element,page.get_plateau_de_jeu().get_case_jaune()[0],page.get_plateau_de_jeu().get_case_jaune()[1],700,110,[])
                    page.set_liste_joueur(page.get_liste_joueur() + [[un_joueur.get_id(), un_joueur.get_prenom(), un_joueur.get_element(), un_joueur.get_plateaux(), un_joueur.get_plateauy(), un_joueur.get_pv(), un_joueur.get_attaque(), un_joueur.get_inventaire()]])
                    page.Page_premier_mouvement(un_joueur)
                    page.get_plateau_de_jeu().plateau_cache(page)
                    page.Page_direction(un_joueur)
                    page.Mise_a_jour(un_joueur)
                    page.get_plateau_de_jeu().plateau_cache(page)
                    page.Page_action(un_joueur)
            if page.get_nb_ia() > 0:
                for numero_ia in range(page.get_nb_ia()):
                    prenom, element = page.Page_choixperso()
                    une_ia = intelA.IntelA(numero_ia + page.get_nb_joueur(),prenom,element,page.get_plateau_de_jeu().get_case_jaune()[0],page.get_plateau_de_jeu().get_case_jaune()[1],700,110,[])
                    page.set_liste_joueur(page.get_liste_joueur() + [[une_ia.get_id(), une_ia.get_prenom(), une_ia.get_element(), une_ia.get_plateaux(), une_ia.get_plateauy(), une_ia.get_pv(), une_ia.get_attaque(), une_ia.get_inventaire()]])
                    page.Page_premier_mouvement(une_ia)
                    page.get_plateau_de_jeu().plateau_cache(page)
                    page.Page_direction(une_ia)
                    page.Mise_a_jour(une_ia)
                    page.get_plateau_de_jeu().plateau_cache(page)
                    page.Page_action(une_ia)
            page.set_etat_de_jeu("partie_en_cours")

        if page.get_etat_de_jeu() == "partie_en_cours":
            if page.get_liste_joueur() != []:
                for i in page.get_liste_joueur():
                    un_joueur = joueur.Joueur(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7])
                    if un_joueur.get_pv()>=0:
                        page.get_plateau_de_jeu().plateau_cache(page)
                        action_joueur = page.Page_mouvement(un_joueur)
                        page.get_plateau_de_jeu().plateau_cache(page)

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
                                texte.Texte("être attaquer. Clique sur le dé",couleur.Couleur().get_Noir(),110,620).affiche(page.get_police(),page.get_fenetre())
                                texte.Texte("pour avancer dans la partie.",couleur.Couleur().get_Noir(),110,640).affiche(page.get_police(),page.get_fenetre())
                                pygame.display.update()
                                page.get_plateau_de_jeu().plateau_cache(page)
                                de_face1 = pygame.image.load("./assets/img/de/Face1.png")
                                page.get_fenetre().blit(de_face1,(350,475))
                                pygame.display.update()
                                page.Page_direction(un_joueur)
                                page.Mise_a_jour(un_joueur)
                                page.get_plateau_de_jeu().plateau_cache(page)
                                page.Page_action(un_joueur)
                                page.Menu_bas(un_joueur)
                                page.get_plateau_de_jeu().plateau_cache(page)
                                if un_joueur.a_gagne(page.get_plateau_de_jeu()) == True:
                                    page.set_etat_de_jeu("fin_du_jeu")
                                else:
                                    page.set_etat_de_jeu("partie_en_cours")
                        else:
                        # Sinon le joueur lance le dé
                            page.Menu_bas(un_joueur) # Affiche le plateau de jeu avec le personnage choisi
                            texte.Texte("Clique sur le de ! ",couleur.Couleur().get_Noir(),110,600).affiche(page.get_police(),page.get_fenetre())
                            pygame.display.update()
                            page.get_plateau_de_jeu().plateau_cache(page)
                            page.Page_direction(un_joueur)
                            page.Mise_a_jour(un_joueur)
                            page.get_plateau_de_jeu().plateau_cache(page)
                            page.Page_action(un_joueur)
                            page.Menu_bas(un_joueur)
                            page.get_plateau_de_jeu().plateau_cache(page)
                            page.get_plateau_de_jeu().plateau_cache(page)
                            if un_joueur.a_gagne(page.get_plateau_de_jeu()) == True:
                                page.set_etat_de_jeu("fin_du_jeu")
                            else:
                                page.set_etat_de_jeu("partie_en_cours")
            else: 
                page.set_etat_de_jeu("fin_du_jeu")

        if page.get_etat_de_jeu() == "fin_du_jeu":
            if un_joueur.a_gagne(page.get_plateau_de_jeu()) == True:
                un_joueur.set_inventaire([])
                page.Page_sorciere(un_joueur)
                pygame.quit()
            else:
                # Page de la sorcière quan don a réussi le jeu
                image.Image(0,0,'assets/img/illustrations/Page_findujeu.png').affichage_image_redimensionnee(800, 700,page.get_fenetre())
                # Dessiner la partie basse
                pygame.draw.rect(page.get_fenetre(),page.get_couleur().get_Gris(),(10,580,780,102))
                texte.Texte("Aucun des joueurs n'a réussi à finir le jeu",couleur.Couleur().get_Noir(),30,600).affiche(page.get_police(),page.get_fenetre())
                texte.Texte("Retentez votre chance une prochaine fois",couleur.Couleur().get_Noir(),30,620).affiche(page.get_police(),page.get_fenetre())
                texte.Texte("pour profiter de cette aventure :)",couleur.Couleur().get_Noir(),30,640).affiche(page.get_police(),page.get_fenetre())
                pygame.display.update()
                pygame.time.delay(2500)
                pygame.quit()
