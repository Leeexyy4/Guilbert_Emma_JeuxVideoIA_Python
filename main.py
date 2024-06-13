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
import pygame
from classe.jeu import interfaces
from classe.visuel import texte, couleur, image
from classe.personnage import joueur
from database import nbCases
from database import creer_partie
from database import envoyer_donnees_bdd
from database import recuperer_donnees_bdd

# ----------------------- Jeu de plateau - Logique du jeu ------------------------ #
     
if __name__ == "__main__":
    # Initialisation de Pygame
    pygame.init()

    stat = recuperer_donnees_bdd()
    print(stat)

    nb_tour = 0
    nb_pv_j1 = []
    nb_pv_j2 = []
    nb_pv_j3 = []
    nb_pv_j4 = []
    nb_cle_j1 = 0
    nb_cle_j2 = 0
    nb_cle_j3 = 0
    nb_cle_j4 = 0
    nb_combat_j1 = 0
    nb_combat_j2 = 0
    nb_combat_j3 = 0
    nb_combat_j4 = 0
    pv_moy_j1 = 0
    pv_moy_j2 = 0
    pv_moy_j3 = 0
    pv_moy_j4 = 0
    nombre_case_decouverte = 0
    nb_mort = 0

    nb_pv_j1_final = nb_pv_j1[-1] if nb_pv_j1 else 0
    pv_moy_j1_final = sum(nb_pv_j1) / len(nb_pv_j1) if nb_pv_j1 else 0
    nb_pv_j2_final = nb_pv_j2[-1] if nb_pv_j2 else 0 
    pv_moy_j2_final = sum(nb_pv_j2) / len(nb_pv_j2) if nb_pv_j2 else 0
    nb_pv_j3_final = nb_pv_j3[-1] if nb_pv_j3 else 0
    pv_moy_j3_final = sum(nb_pv_j3) / len(nb_pv_j3) if nb_pv_j3 else 0
    nb_pv_j4_final = nb_pv_j4[-1] if nb_pv_j4 else 0
    pv_moy_j4_final = sum(nb_pv_j4) / len(nb_pv_j4) if nb_pv_j4 else 0


    donnees_bdd = recuperer_donnees_bdd()

    page = interfaces.Interface()
    page.Page_demarrage(donnees_bdd)
    # Pour tous les joueurs encore en vie
    while page.get_etat_de_jeu() != "fin_du_jeu": 
        print(nombre_case_decouverte)
        # Gerer les etats du jeu
        if page.get_etat_de_jeu() == "demarrage_jeu": # si le jeu demarre
            if page.get_nb_joueur() > 0:  # si le nombre de joueur est choisi
                for numero_joueur in range(page.get_nb_joueur()):
                    # Afficher la proposition pour choisir le personnage
                    prenom, element = page.Page_choixperso(numero_joueur)
                    un_joueur = joueur.Joueur(numero_joueur,prenom,element,page.get_plateau_de_jeu().get_case_jaune()[0],page.get_plateau_de_jeu().get_case_jaune()[1],700,110,["cle de la Ville", "cle de la Forêt", "cle du Rocher", "cle de la Rivière"])
                    page.set_liste_joueur(page.get_liste_joueur() + [[un_joueur.get_id(), un_joueur.get_prenom(), un_joueur.get_element(), un_joueur.get_plateaux(), un_joueur.get_plateauy(), un_joueur.get_pv(), un_joueur.get_attaque(), un_joueur.get_inventaire()]])
                    page.Page_premier_mouvement(un_joueur)
                    page.get_plateau_de_jeu().plateau_cache(page)
                    page.Page_direction(un_joueur)
                    page.Mise_a_jour(un_joueur)
                    page.get_plateau_de_jeu().plateau_cache(page)
                    page.Page_action(un_joueur)
                    numero_joueur = numero_joueur + 1
                    prenom = ""  
                page.set_etat_de_jeu("partie_en_cours")

        if page.get_etat_de_jeu() == "partie_en_cours":
            print("_________________________________________")
            nb_tour += 1
            pv_joueurs = { 'Pierre': None, 'Flora': None, 'Ondine': None, 'Kevin': None }
            combat_joueur = { 'Pierre': None, 'Flora': None, 'Ondine': None, 'Kevin': None }
            cles_joueurs = { 'Pierre': 0, 'Flora': 0, 'Ondine': 0, 'Kevin': 0 }

            for joueur_data in page.get_liste_joueur():
                un_joueur = joueur.Joueur(joueur_data[0], joueur_data[1], joueur_data[2], joueur_data[3], joueur_data[4], joueur_data[5], joueur_data[6], joueur_data[7])
                pv_joueurs[un_joueur.get_prenom()] = un_joueur.get_pv()
                combat_joueur[un_joueur.get_prenom()] = un_joueur.get_attaque()
                cles_joueurs[un_joueur.get_prenom()] = len(un_joueur.get_inventaire())

            if pv_joueurs['Pierre'] is not None:
                nb_pv_j1.append(pv_joueurs['Pierre'])
                nb_combat_j1 += combat_joueur["Pierre"]
            if pv_joueurs['Flora'] is not None:
                nb_pv_j2.append(pv_joueurs['Flora'])
                nb_combat_j2 += combat_joueur["Flora"]
            if pv_joueurs['Ondine'] is not None:
                nb_pv_j3.append(pv_joueurs['Ondine'])
                nb_combat_j3 += combat_joueur["Ondine"]
            if pv_joueurs['Kevin'] is not None:
                nb_pv_j4.append(pv_joueurs['Kevin'])
                nb_combat_j4 += combat_joueur["Kevin"]

            nb_cle_j1 = cles_joueurs['Pierre']
            nb_cle_j2 = cles_joueurs['Flora']
            nb_cle_j3 = cles_joueurs['Ondine']
            nb_cle_j4 = cles_joueurs['Kevin']

            nb_pv_j1_final = nb_pv_j1[-1] if nb_pv_j1 else 0
            pv_moy_j1_final = sum(nb_pv_j1) / len(nb_pv_j1) if nb_pv_j1 else 0
            nb_pv_j2_final = nb_pv_j2[-1] if nb_pv_j2 else 0 
            pv_moy_j2_final = sum(nb_pv_j2) / len(nb_pv_j2) if nb_pv_j2 else 0
            nb_pv_j3_final = nb_pv_j3[-1] if nb_pv_j3 else 0
            pv_moy_j3_final = sum(nb_pv_j3) / len(nb_pv_j3) if nb_pv_j3 else 0
            nb_pv_j4_final = nb_pv_j4[-1] if nb_pv_j4 else 0
            pv_moy_j4_final = sum(nb_pv_j4) / len(nb_pv_j4) if nb_pv_j4 else 0   

            nombre_case_decouverte = len(page.get_plateau_de_jeu().get_cases_decouvertes())
            print(f"nombre de tours : {nb_tour}"),
            print(f"PV du joueur 1 : {nb_pv_j1}"),
            print(f"PV du joueur 2 : {nb_pv_j2}"),
            print(f"PV du joueur 3 : {nb_pv_j3}"),
            print(f"PV du joueur 4 : {nb_pv_j4}"),
            print(f"Nb combat du joueur 1 : {nb_combat_j1}"),
            print(f"Nb combat du joueur 2 : {nb_combat_j2}"),
            print(f"Nb combat du joueur 3 : {nb_combat_j3}"),
            print(f"Nb combat du joueur 4 : {nb_combat_j4}"),
            print(f"Nb de clé du joueur 1 : {nb_cle_j1}"),
            print(f"Nb de clé du joueur 2 : {nb_cle_j2}"),
            print(f"Nb de clé du joueur 3 : {nb_cle_j3}"),
            print(f"Nb de clé du joueur 4 : {nb_cle_j4}"),
            print(f"Nombre de cases découvertes : {nombre_case_decouverte}"),
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
                        nb_mort += 1
                        print(f"Nombre de morts: {nb_mort}")
            else: 
                page.set_etat_de_jeu("fin_du_jeu")

        if page.get_etat_de_jeu() == "fin_du_jeu":

            if(un_joueur.avoir_tt_cles == True):
                gagnant = True
            else:
                gagnant = False

            print(gagnant)
            partie_id = creer_partie(gagnant)
            print(partie_id)

            for joueur_data in page.get_liste_joueur():
                envoyer_donnees_bdd(
                    partie_id,
                    2 if un_joueur.get_prenom() == 'Pierre' else 3 if un_joueur.get_prenom() == 'Flora' else 4 if un_joueur.get_prenom() == 'Ondine' else 5,
                    nombre_case_decouverte,
                    nb_tour,
                    nb_mort,
                    nb_cle_j1 if un_joueur.get_prenom() == 'Pierre' else nb_cle_j2 if un_joueur.get_prenom() == 'Flora' else nb_cle_j3 if un_joueur.get_prenom() == 'Ondine' else nb_cle_j4,
                    nb_pv_j1_final if un_joueur.get_prenom() == 'Pierre' else nb_pv_j2_final if un_joueur.get_prenom() == 'Flora' else nb_pv_j3_final if un_joueur.get_prenom() == 'Ondine' else nb_pv_j4_final,
                    nb_combat_j1 if un_joueur.get_prenom() == 'Pierre' else nb_combat_j2 if un_joueur.get_prenom() == 'Flora' else nb_combat_j3 if un_joueur.get_prenom() == 'Ondine' else nb_combat_j4,
                    pv_moy_j1_final if un_joueur.get_prenom() == 'Pierre' else pv_moy_j2_final if un_joueur.get_prenom() == 'Flora' else pv_moy_j3_final if un_joueur.get_prenom() == 'Ondine' else pv_moy_j4_final,
                )

            donnees_bdd = recuperer_donnees_bdd()

            if un_joueur.a_gagne(page.get_plateau_de_jeu()) == True:
                un_joueur.set_inventaire([])
                page.Page_sorciere( un_joueur, 
                                    nb_tour, 
                                    nb_pv_j1_final,
                                    nb_pv_j2_final ,
                                    nb_pv_j3_final,
                                    nb_pv_j4_final,
                                    nb_cle_j1,
                                    nb_cle_j2,
                                    nb_cle_j3,
                                    nb_cle_j4,
                                    nb_combat_j1,
                                    nb_combat_j2,
                                    nb_combat_j3,
                                    nb_combat_j4,
                                    pv_moy_j1_final,
                                    pv_moy_j2_final,
                                    pv_moy_j3_final,
                                    pv_moy_j4_final,
                                    nombre_case_decouverte,
                                    nb_mort,
                                    donnees_bdd
                                )
                pygame.quit()
            else:
                # Page de la sorcière quan don a réussi le jeu
                page.Page_fin(un_joueur, 
                                    nb_tour, 
                                    nb_pv_j1_final,
                                    nb_pv_j2_final ,
                                    nb_pv_j3_final,
                                    nb_pv_j4_final,
                                    nb_cle_j1,
                                    nb_cle_j2,
                                    nb_cle_j3,
                                    nb_cle_j4,
                                    nb_combat_j1,
                                    nb_combat_j2,
                                    nb_combat_j3,
                                    nb_combat_j4,
                                    pv_moy_j1_final,
                                    pv_moy_j2_final,
                                    pv_moy_j3_final,
                                    pv_moy_j4_final,
                                    nombre_case_decouverte,
                                    nb_mort,
                                    donnees_bdd)
                # Dessiner la partie basse
                pygame.draw.rect(page.get_fenetre(),page.get_couleur().get_Gris(),(10,580,780,102))
                texte.Texte("Aucun des joueurs n'a réussi à finir le jeu",couleur.Couleur().get_Noir(),30,600).affiche(page.get_police(),page.get_fenetre())
                texte.Texte("Retentez votre chance une prochaine fois",couleur.Couleur().get_Noir(),30,620).affiche(page.get_police(),page.get_fenetre())
                texte.Texte("pour profiter de cette aventure :)",couleur.Couleur().get_Noir(),30,640).affiche(page.get_police(),page.get_fenetre())
                pygame.display.update()
                pygame.time.delay(2500)
                pygame.quit()
