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
import joueur, rectangle, texte, de, plateau, couleur, ennemis, image # Importation des classes crees
import random # Importation de la bibliotheque aleatoire

# ----------------------- Jeu de plateau - Fenetre de jeu ------------------------ #

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenetre
largeur, hauteur = 800, 700

# Creation de la fenetre
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Plateau de jeu")

# Police de texte
police = pygame.font.Font('./assets/font/times-new-roman.ttf', 16)

# Definir les variables utiles
plateau_de_jeu=plateau.Plateau()
de_jeu = de.De()
liste_joueur = []
case_decouverte = []

# ----------------------- Jeu de plateau - Plateau de jeu ------------------------ #

# Taille d'une case
taille_case = largeur // 17

def Menu_bas():
    # Dessiner la partie basse
    pygame.draw.rect(fenetre,couleur.Couleur().get_Gris(),(10,580,780,102))
    
    # Dessiner la place pour montrer les cles
    rectangle.Rectangle(650,585,130,90).affiche(fenetre,couleur.Couleur().get_Rose())
    un_joueur.affichage_cle(fenetre)
    
    # Dessiner le rectangle pour les pv du joueur
    rectangle.Rectangle(500,590,130,35).affiche(fenetre,couleur.Couleur().get_Vert())
    texte.Texte("PV joueur : ", couleur.Couleur().get_Noir(), 500,590).affiche(police,fenetre)
    
    # Dessiner les bords de la place pour les pv de l'adversaire
    rectangle.Rectangle(500,635,130,35).affiche(fenetre,couleur.Couleur().get_Rouge())

    # Dessiner le rectangle pour les textes
    rectangle.Rectangle(100, 590, 390, 80).affiche(fenetre,couleur.Couleur().get_Beige())
    
    # Cadre pour mettre le personnage choisi
    rectangle.Rectangle(20,590,70,80).affiche(fenetre,couleur.Couleur().get_Rose())
    
    # Prendre la variable du personnage choisi de "Position_choix_perso()""
    if un_joueur.get_prenom() == "Pierre":
        # Ajouter la photo de Pierre
        un_joueur.affichage_image(24,598,fenetre,police)
    
    if un_joueur.get_prenom() == "Ondine":
        # Ajouter la photo de Ondine
        un_joueur.affichage_image(24,598,fenetre,police)
    
    if un_joueur.get_prenom() == "Flora":
        # Ajouter la photo de Pierre
        un_joueur.affichage_image(24,598,fenetre,police)
    
    if un_joueur.get_prenom() == "Kevin":
        # Ajouter la photo de Pierre
        un_joueur.affichage_image(24,598,fenetre,police)
    
    # Mettre à jour l'affichage
    pygame.display.update()
        
# ----------------------- Jeu de plateau - Deroulement de la partie ------------------------ #

def Page_demarrage():    
    # Affiche l'image de fond 
    image.Image(0,0,'assets/img/illustrations/Page_demarrage.png').affichage_image_redimensionnee(800, 700,fenetre)
    # Mettre à jour l'affichage
    pygame.display.update()
    
    # Faire un systeme pour la selection de la position du clic pour la selection du personnage
    start = False
    # Boucle while pour voir quand le joueur clique sur start
    while (start != True):
        mouse_x, mouse_y = pygame.mouse.get_pos() # Recuperer les coordonnees de la souris
        # Pour tous les evenements
        for event in pygame.event.get():
            # Si le joueur clique sur le bouton, on passe à la prochaine page "introduction"
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (340 <= mouse_x <= 465 and 510 <= mouse_y <= 560) : # si appuie bouton play
                    start = True
                if 700 <= mouse_x <= 764 and 25 <= mouse_y <= 89 : # si appuie sur info
                    image.Image(0,0,'assets/img/illustrations/Page_commentjouer.png').affichage_image_redimensionnee(800, 700,fenetre)
                    # Mettre à jour l'affichage
                    pygame.display.update()
                    start = False
                if (10 <= mouse_x <= 70 and 630 <= mouse_y <= 690): # si appuie sur fleche retour
                    image.Image(0,0,'assets/img/illustrations/Page_demarrage.png').affichage_image_redimensionnee(800, 700,fenetre)
                    # Mettre à jour l'affichage
                    pygame.display.update()
                    start = False
            # Si le joueur quitte la fenetre
            if (event.type == pygame.QUIT):
                pygame.quit()
                exit()

def Page_nb_joueur():
     # Affiche l'image de fond 
    image.Image(0,0,'assets/img/illustrations/Page_sortilege.png').affichage_image_redimensionnee(800, 700,fenetre)
    rectangle.Rectangle(10,580,780,100).affiche(fenetre,couleur.Couleur().get_Gris())
    texte.Texte("La sorciere du village vous a lancé un sort qui vous rend minuscule, il va falloir vous en sortir en récupérant la potion", couleur.Couleur().get_Noir(), 20,600).affiche(police,fenetre)
    texte.Texte("d'inversion du sortilège chez elle.", couleur.Couleur().get_Noir(), 20,620).affiche(police,fenetre)

    # Mettre à jour l'affichage
    pygame.display.update()
    pygame.time.delay(3000)
    
    image.Image(0,0,'assets/img/illustrations/Page_nbjoueurs.png').affichage_image_redimensionnee(800, 700,fenetre)
    rectangle.Rectangle(10,580,780,100).affiche(fenetre,couleur.Couleur().get_Gris())
    # Texte pour choisir le nombre de joueur
    texte.Texte("Combien de joueurs souhaitent jouer au jeu ? ", couleur.Couleur().get_Noir(), 20,620).affiche(police,fenetre)

    # Ajouter les photos des chifres
    image.Image(400,595,"./assets/img/illustrations/1.png").affiche(fenetre)
    image.Image(500,595,"./assets/img/illustrations/2.png").affiche(fenetre)
    image.Image(600,595,"./assets/img/illustrations/3.png").affiche(fenetre)
    image.Image(700,595,"./assets/img/illustrations/4.png").affiche(fenetre)
    
    # Mettre à jour l'affichage
    pygame.display.update()
    
    # Faire un systeme pour la selection de la position du clic pour la selection du personnage
    nb = 0
    
    #Tant que le prenom n'est pas selectionne
    while (nb != 2) or (nb != 3) or (nb != 4) or (nb != 1):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN : # Si le joueur clique sur le bouton, on passe à la prochaine page "introduction"
                mouse_x, mouse_y = pygame.mouse.get_pos() # Recuperer les coordonnees de la souris
                if (40 <= mouse_x <= 100 and 40 <= mouse_y <= 100) : # si appuie bouton play
                    nb = 5
                    return nb
                # Si le personnage sur lequel on clique est J2   
                if 500 <= mouse_x <= 600 and 582 <= mouse_y <= 652 :
                    nb = 2
                    return nb
                # Si le personnage sur lequel on clique est J4
                if 700 <= mouse_x <= 800 and 582 <= mouse_y <= 652 :   
                    nb = 4
                    return nb
                # Si le personnage sur lequel on clique est J1
                if 400 <= mouse_x <= 500 and 582 <= mouse_y <= 652 :   
                    nb = 1
                    return nb
                # Si le personnage sur lequel on clique est J3
                if 600 <= mouse_x <= 700 and 582 <= mouse_y <= 652 :   
                    nb = 3
                    return nb
            if event.type == pygame.QUIT: # si le joueur quitte la fenetre # si le joueur quitte la fenetre
                pygame.quit()
                exit()

def Page_choixperso():  
      
    image.Image(0,0,'assets/img/illustrations/Page_choixperso.png').affichage_image_redimensionnee(800, 700,fenetre)
    # Dessiner le cadre du bas afin de cacher les anciennes ecritures
    rectangle.Rectangle(10,580,780,100).affiche(fenetre,couleur.Couleur().get_Gris())
    
    # Texte pour choisir le personnage
    texte.Texte("Bienvenue à toi jeune aventurier !",couleur.Couleur().get_Noir() ,20,590).affiche(police, fenetre)
    texte.Texte("Je t'invite à choisir un personnage parmi la liste suivante :",couleur.Couleur().get_Noir() ,20,620).affiche(police, fenetre)
    texte.Texte("Pierre, Ondine, Kevin ou Flora",couleur.Couleur().get_Noir() ,20,650).affiche(police,fenetre)
    
    # Ajouter les photos des personnages
    image.Image(400,585,"./assets/img/personnages/Pierre.png").affiche(fenetre)
    texte.Texte("Pierre",couleur.Couleur().get_Noir(), 413, 650).affiche(police,fenetre)
    image.Image(500,585,"./assets/img/personnages/Ondine.png").affiche(fenetre)
    texte.Texte("Ondine",couleur.Couleur().get_Noir(), 510, 650).affiche(police,fenetre)
    image.Image(600,585,"./assets/img/personnages/Kevin.png").affiche(fenetre)
    texte.Texte("Kevin",couleur.Couleur().get_Noir(), 613, 650).affiche(police,fenetre)
    image.Image(700,585,"./assets/img/personnages/Flora.png").affiche(fenetre)
    texte.Texte("Flora",couleur.Couleur().get_Noir(), 715, 650).affiche(police,fenetre)
    
    # Texte pour animer la page
    texte.Texte("Amusez-vous bien ici demarre une nouvelle aventure !",couleur.Couleur().get_Blanc(),230, 530).affiche(police,fenetre)
    
    # Mettre à jour l'affichage
    pygame.display.update()
    
    # Faire un systeme pour la selection de la position du clic pour la selection du personnage
    prenom = ""
    
    #Tant que le prenom n'est pas selectionne
    while (prenom != "Ondine") or (prenom != "Pierre") or (prenom != "Flora") or (prenom != "Kevin") :
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN : # Si le joueur clique sur le bouton, on passe à la prochaine page "introduction"
                mouse_x, mouse_y = pygame.mouse.get_pos() # Recuperer les coordonnees de la souris
                if (40 <= mouse_x <= 100 and 40 <= mouse_y <= 100) : # si appuie bouton play
                    prenom = "Aucun"
                    element = "Aucun"
                    return prenom, element
                # Si le personnage sur lequel on clique est Ondine   
                if 500 <= mouse_x <= 600 and 582 <= mouse_y <= 652 :
                    prenom = "Ondine"
                    element = "de la Riviere"
                    return prenom, element
                # Si le personnage sur lequel on clique est Flora
                if 700 <= mouse_x <= 800 and 582 <= mouse_y <= 652 :   
                    prenom = "Flora"
                    element = "de la Foret"
                    return prenom, element
                # Si le personnage sur lequel on clique est Pierre
                if 400 <= mouse_x <= 500 and 582 <= mouse_y <= 652 :   
                    prenom = "Pierre"
                    element = "du Rocher"
                    return prenom, element
                # Si le personnage sur lequel on clique est Kevin
                if 600 <= mouse_x <= 700 and 582 <= mouse_y <= 652 :   
                    prenom = "Kevin"
                    element = "de la Ville"
                    return prenom, element
            if event.type == pygame.QUIT: # si le joueur quitte la fenetre # si le joueur quitte la fenetre
                pygame.quit()
                exit()
    
def Page_premier_mouvement():
    image.Image(0,468,'assets/img/illustrations/Page_plateau.png').affiche(fenetre)
    Menu_bas()    
    # cacher le Texte
    rectangle.Rectangle(100, 590, 390, 80).affiche(fenetre,couleur.Couleur().get_Beige())
    texte.Texte("Tu es le joueur " + str(un_joueur.get_ordre() + 1) + ", clique sur le de afin de faire",couleur.Couleur().get_Noir(),110,600).affiche(police,fenetre)
    texte.Texte("ton deplacement",couleur.Couleur().get_Noir(),110,620).affiche(police,fenetre)
    
    # Affiche le de sur la face 1
    image.Image(350,475,"./assets/img/de/Face1.png").affiche(fenetre)
    
    # Mettre à jour l'affichage
    pygame.display.update()
    
def Page_mouvement():
    image.Image(0,468,'assets/img/illustrations/Page_choixdouble.png').affiche(fenetre)
    Menu_bas()
    rectangle.Rectangle(100, 590, 390, 80).affiche(fenetre,couleur.Couleur().get_Beige())
    texte.Texte("Joueur " + str(un_joueur.get_ordre() + 1) + " : " + un_joueur.get_prenom() + " clique sur le de afin ",couleur.Couleur().get_Noir(),110,600).affiche(police,fenetre)
    texte.Texte("d'attaquer un joueur ou de lancer le de",couleur.Couleur().get_Noir(),110,620).affiche(police,fenetre)
    
    # Affiche le de sur la face 1
    image.Image(220,480,"./assets/img/interraction/Attaquer.png").affiche(fenetre)
    image.Image(510, 480,"./assets/img/interraction/De.png").affiche(fenetre)
    texte.Texte("Attaquer",couleur.Couleur().get_Blanc(),227,545).affiche(police,fenetre)
    texte.Texte("De",couleur.Couleur().get_Blanc(),532,545).affiche(police,fenetre)
    
    # Mettre à jour l'affichage
    pygame.display.update()
    
    # Faire un systeme pour la selection de la position du clic pour la selection du personnage
    action_joueur = ""
    
    #Tant que le prenom n'est pas selectionne
    while (action_joueur != "Attaquer") or (action_joueur != "Lancer") :
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN : # Si le joueur clique sur le bouton, on passe à la prochaine page "introduction"
                mouse_x, mouse_y = pygame.mouse.get_pos() # Recuperer les coordonnees de la souris
                # Si le personnage sur lequel on clique est Ondine   
                if 220 <= mouse_x <= 284 and 480 <= mouse_y <= 544 :
                    
                    action_joueur = "Attaquer"
                    image.Image(0,468,'assets/img/illustrations/Page_plateau.png').affiche(fenetre)
                    return action_joueur
                elif 510 <= mouse_x <= 574 and 480 <= mouse_y <= 544:
                    
                    action_joueur = "Lancer"
                    image.Image(0,468,'assets/img/illustrations/Page_plateau.png').affiche(fenetre)
                    de_face1 = pygame.image.load("./assets/img/de/Face1.png")
                    fenetre.blit(de_face1,(350,475))
                    pygame.display.update()
                    return action_joueur
            if event.type == pygame.QUIT: # si le joueur quitte la fenetre # si le joueur quitte la fenetre
                pygame.quit()
                exit()

def Page_direction(case_decouverte):
    """Genere la page qui permet de faire le deplacement en demandant le choix de direction

    Return:
        event.key touche_fleche: Retourne la touche appuyer par le joueur pour faire le deplacement
    """    
    # Lance le de
    de_jeu.Choix_de(fenetre)
    face_choisie = de_jeu.get_face_choisie()
    
    # help(Page_direction)
    pygame.time.delay(1000)
    
    # Rectangle : Reinitialise la fenetre de Texte
    rectangle.Rectangle(100, 590, 390, 80).affiche(fenetre,couleur.Couleur().get_Beige())

    # Texte : Lancer le de
    texte.Texte("Bravo ! Tu peux avancer de {} cases ! Où ".format(face_choisie),couleur.Couleur().get_Noir(),110,600).affiche(police,fenetre)
    texte.Texte("veux-tu aller ? (haut, bas, gauche, droite)",couleur.Couleur().get_Noir(),110,620).affiche(police,fenetre)
    

    # Mise à jour de l'affichage
    pygame.display.update()
    
    
    # Tant que : Le joueur n'a pas choisi de direction (haut, bas, gauche, droite)
    while face_choisie != 0 :
        # Pour tout : Les evenements de pygame
        for event in pygame.event.get():
            
            # Si le joueur quitte la fenetre
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
            elif event.type == pygame.KEYDOWN:
                touche_fleche = event.key

                if touche_fleche == pygame.K_UP:
                    # La touche fleche vers le haut a ete enfoncee
                    avancer = un_joueur.haut(47)
                    case_decouverte = case_decouverte + [[un_joueur.get_plateaux(),un_joueur.get_plateauy()]]
                    Mise_a_jour(un_joueur.get_ordre())
                    plateau_de_jeu.plateau_cache(fenetre)
                    plateau_de_jeu.mise_a_jour_plateau(case_decouverte,fenetre)
                    un_joueur.affiche_tt_joueur(liste_joueur,numero_joueur,fenetre)
                    un_joueur.affichage_image_plateau(un_joueur.get_x(),un_joueur.get_y(),fenetre)
                    if avancer == True :
                        face_choisie = face_choisie - 1
                    else:
                        Page_rejouer(face_choisie)
                
                elif touche_fleche == pygame.K_DOWN:
                    # La touche fleche vers le bas a ete enfoncee
                    avancer = un_joueur.bas(47)
                    case_decouverte = case_decouverte + [[un_joueur.get_plateaux(),un_joueur.get_plateauy()]]
                    Mise_a_jour(un_joueur.get_ordre())
                    plateau_de_jeu.plateau_cache(fenetre)
                    plateau_de_jeu.mise_a_jour_plateau(case_decouverte,fenetre)
                    un_joueur.affiche_tt_joueur(liste_joueur,numero_joueur,fenetre)
                    un_joueur.affichage_image_plateau(un_joueur.get_x(),un_joueur.get_y(),fenetre)
                    if avancer == True :
                        face_choisie = face_choisie - 1
                    else:
                        Page_rejouer(face_choisie)
                
                elif touche_fleche == pygame.K_RIGHT:
                    # La touche fleche vers la droite a ete enfoncee
                    avancer = un_joueur.droite(47) 
                    case_decouverte = case_decouverte + [[un_joueur.get_plateaux(),un_joueur.get_plateauy()]]
                    Mise_a_jour(un_joueur.get_ordre()) 
                    plateau_de_jeu.plateau_cache(fenetre)
                    plateau_de_jeu.mise_a_jour_plateau(case_decouverte,fenetre)
                    un_joueur.affiche_tt_joueur(liste_joueur,numero_joueur,fenetre)
                    un_joueur.affichage_image_plateau(un_joueur.get_x(),un_joueur.get_y(),fenetre)
                    if avancer == True :
                        face_choisie = face_choisie - 1
                    else:
                        Page_rejouer(face_choisie)

                elif touche_fleche == pygame.K_LEFT:
                    # La touche fleche vers la gauche a ete enfoncee
                    avancer = un_joueur.gauche(47) 
                    case_decouverte = case_decouverte + [[un_joueur.get_plateaux(),un_joueur.get_plateauy()]]  
                    Mise_a_jour(un_joueur.get_ordre())                
                    plateau_de_jeu.plateau_cache(fenetre)
                    plateau_de_jeu.mise_a_jour_plateau(case_decouverte,fenetre)
                    un_joueur.affiche_tt_joueur(liste_joueur,numero_joueur,fenetre)
                    un_joueur.affichage_image_plateau(un_joueur.get_x(),un_joueur.get_y(),fenetre)
                    if avancer == True :
                        face_choisie = face_choisie - 1
                    else:
                        Page_rejouer(face_choisie)
    return case_decouverte
                        
def Page_rejouer(face_choisie):
        # Dessiner le rectangle pour les dialogues
        rectangle.Rectangle(100, 590, 390, 80).affiche(fenetre, couleur.Couleur().get_Beige())
        # Texte pour dire au joueur de rejouer
        texte.Texte("Tu ne peux pas aller par là, tu as atteint un bord", couleur.Couleur().get_Noir(), 110, 600).affiche(police,fenetre)
        texte.Texte("ou il n'y a pas de cases dans cette direction", couleur.Couleur().get_Noir(), 110, 620).affiche(police,fenetre)
        texte.Texte("rejoue ! clique sur une des fleches", couleur.Couleur().get_Noir(), 110, 640).affiche(police,fenetre)
        un_joueur.affiche_tt_joueur(liste_joueur,numero_joueur-1,fenetre)
        pygame.display.update()
        pygame.time.delay(1500)
        Menu_bas()
        texte.Texte("Tu peux avancer de {} cases ! Où ".format(face_choisie),couleur.Couleur().get_Noir(),110,600).affiche(police,fenetre)
        texte.Texte("veux-tu aller ? (haut, bas, gauche, droite)",couleur.Couleur().get_Noir(),110,620).affiche(police,fenetre)
        pygame.display.update()
        return

def Page_action(case_decouverte):
        # Dessiner le rectangle pour les dialogues
        rectangle.Rectangle(100, 590, 390, 80).affiche(fenetre, couleur.Couleur().get_Beige())
        # Texte pour dire au joueur de rejouer
        texte.Texte("Tu as atterris sur une case {}".format(plateau_de_jeu.get_nom(un_joueur.get_plateaux(),un_joueur.get_plateauy())), couleur.Couleur().get_Noir(), 110, 600).affiche(police,fenetre)
        pygame.display.update()
        couleur_case = plateau_de_jeu.get_plateau()[un_joueur.get_plateaux()][un_joueur.get_plateauy()]
        image.Image(0,468,'assets/img/illustrations/Page_plateau.png').affiche(fenetre)
        Menu_bas()  
        if un_joueur.get_pv() != 0:
            if couleur_case == couleur.Couleur().get_Beige():
                Action_couleur_Beige()
                
            elif couleur_case == couleur.Couleur().get_Blanc():
                # Dessiner le rectangle pour les dialogues
                rectangle.Rectangle(100, 590, 390, 80).affiche(fenetre, couleur.Couleur().get_Beige())
                texte.Texte("Tu es dans une case Vide.",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
                texte.Texte("Il ne t'arrivera rien tu peux etre rassure.",couleur.Couleur().get_Noir(),110, 620).affiche(police,fenetre)
                
            elif couleur_case == couleur.Couleur().get_Bleu():
                Action_couleur_Bleu()
                        
            elif couleur_case == couleur.Couleur().get_Gris():
                Action_couleur_Gris()
                
            elif couleur_case == couleur.Couleur().get_Indigo():
                Action_couleur_Indigo()
                
            elif couleur_case == couleur.Couleur().get_Jaune():
                # Dessiner le rectangle pour les dialogues
                rectangle.Rectangle(100, 590, 390, 80).affiche(fenetre, couleur.Couleur().get_Beige())
                texte.Texte("Tu es la case de Depart.",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
                texte.Texte("Depeche toi de recuperer les cles",couleur.Couleur().get_Noir(),110, 620).affiche(police,fenetre)
                texte.Texte("avant les autres joueurs.",couleur.Couleur().get_Noir(),110, 640).affiche(police,fenetre)
                
            elif couleur_case == couleur.Couleur().get_Noir():
                Action_couleur_Noir()     
                
            elif couleur_case == couleur.Couleur().get_Orange():
                Action_couleur_Orange()

            elif couleur_case == couleur.Couleur().get_Rose():
                Action_couleur_Rose()
                
            elif couleur_case == couleur.Couleur().get_Rouge():
                Action_couleur_Rouge()
                
            elif couleur_case == couleur.Couleur().get_Turquoise():
                Action_couleur_Turquoise()
                
            elif couleur_case == couleur.Couleur().get_Violet():
                case_decouverte = Action_couleur_Violet(case_decouverte,liste_joueur)
            pygame.display.update()
            return case_decouverte, liste_joueur
   
def Action_couleur_Bleu():
    image.Image(0,468,'assets/img/illustrations/Page_choixdouble.png').affiche(fenetre)
    Menu_bas()
    # Dessiner le rectangle pour les dialogues
    rectangle.Rectangle(100, 590, 390, 80).affiche(fenetre, couleur.Couleur().get_Beige())
    texte.Texte("Tu es tombe dans la case Puit...",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)        
    texte.Texte("Pour t'en sortir, tu dois sacrifier une de",couleur.Couleur().get_Noir(),110, 620).affiche(police,fenetre)        
    texte.Texte("tes cles ou 200 pv.",couleur.Couleur().get_Noir(),110, 640).affiche(police,fenetre)
    pygame.display.update()
    pygame.time.delay(3200)
    
    # Cacher les anciens dialogues
    rectangle.Rectangle(100, 590, 390, 80).affiche(fenetre, couleur.Couleur().get_Beige())
    texte.Texte("Veux-tu sacrifier une de tes cles ou me donner 200 pv",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
    pygame.display.update() # mettre à jour l'affichage
    
    # Afficher les logos et texte des cles et des pv
    pv = pygame.image.load("./assets/img/interraction/Pv.png")
    fenetre.blit(pv, (220, 480))
    cles = pygame.image.load("./assets/img/interraction/Cles.png")
    fenetre.blit(cles, (510, 480))
    texte.Texte("200 PV",couleur.Couleur().get_Blanc(),235,545).affiche(police,fenetre)
    texte.Texte("1 clee",couleur.Couleur().get_Blanc(),525,545).affiche(police,fenetre)
    pygame.display.update()
    
    selection_utilisateur = False
    while selection_utilisateur != True:
        mouse_x, mouse_y = pygame.mouse.get_pos() # Recuperer les coordonnees de la souris
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # si le joueur quitte la fenetre # si le joueur quitte la fenetre
                pygame.quit()
                exit() 
            
            # Si le clique est presse
            if event.type == pygame.MOUSEBUTTONDOWN:  
                if 220 < mouse_x < 284 and 480 < mouse_y < 544:
                    
                    # Si le joueur veut echanger des pv
                    if un_joueur.get_pv() > 200:
                        un_joueur.supprimer_pv(liste_joueur,200,fenetre)                        
                        selection_utilisateur = True
                        return liste_joueur
                    else :
                        rectangle.Rectangle(100, 590, 390, 80).affiche(fenetre, couleur.Couleur().get_Beige())
                        texte.Texte("Tu n'as pas de cles, donne moi 200 pv",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
                        pygame.display.update()
                        
                elif 510 < mouse_x < 574 and 480 < mouse_y < 544:
                    if un_joueur.get_inventaire() != []:
                        rectangle.Rectangle(500,590,130,35).affiche(fenetre,couleur.Couleur().get_Vert())
                        texte.Texte(un_joueur.get_pv(),couleur.Couleur().get_Noir(),538,598).affiche(police,fenetre)
                        pygame.display.update()
                        selection_utilisateur = True  
                        return liste_joueur
                    
                    elif un_joueur.get_inventaire() == [] and un_joueur.get_pv() > 200:
                        rectangle.Rectangle(100, 590, 390, 80).affiche(fenetre, couleur.Couleur().get_Beige())
                        texte.Texte("Tu n'as pas de cles, donne moi 200 pv",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
                        pygame.display.update()
                    else :
                        rectangle.Rectangle(500,590,130,35).affiche(fenetre,couleur.Couleur().get_Vert())
                        rectangle.Rectangle(100, 590, 390, 80).affiche(fenetre, couleur.Couleur().get_Beige())
                        un_joueur.set_pv(0)
                        Mise_a_jour(un_joueur.get_ordre())
                        texte.Texte(un_joueur.get_pv(),couleur.Couleur().get_Noir(),538,598).affiche(police,fenetre)
                        texte.Texte("Tu n'as pas de cles, ni assez de pv",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)       
                        texte.Texte("Tu es donc condamne à devoir mourrir et arreter",couleur.Couleur().get_Noir(),110, 620).affiche(police,fenetre)       
                        texte.Texte("la partie ici.",couleur.Couleur().get_Noir(),110, 640).affiche(police,fenetre)  
                        pygame.display.update()  
                        selection_utilisateur = True
                        return liste_joueur
    
def Action_couleur_Noir():
    # Dessiner le rectangle pour les dialogues
    rectangle.Rectangle(100, 590, 390, 80).affiche(fenetre, couleur.Couleur().get_Beige())
    texte.Texte("Tu n'as pas de chance...",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
    texte.Texte("Tu es tombe sur la case de Mort...",couleur.Couleur().get_Noir(),110, 620).affiche(police,fenetre)
    texte.Texte("La partie est finie pour toi.",couleur.Couleur().get_Noir(),110, 640).affiche(police,fenetre)
    un_joueur.supprimer_pv(liste_joueur,un_joueur.get_pv(),fenetre)
    pygame.display.update()
    pygame.time.delay(2000)
    
def Action_couleur_Orange():
    # Dessiner le rectangle pour les dialogues
    rectangle.Rectangle(100, 590, 390, 80).affiche(fenetre, couleur.Couleur().get_Beige())
    texte.Texte("Tu es sur une case Malus.",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
    texte.Texte("Clique pour savoir quel sort",couleur.Couleur().get_Noir(),110, 620).affiche(police,fenetre)
    texte.Texte("le jeu te reserve.",couleur.Couleur().get_Noir(),110, 640).affiche(police,fenetre)
    pygame.display.update()
    pygame.time.delay(3200)
        
    malus = pygame.image.load("./assets/img/interraction/Malus.png")
    fenetre.blit(malus, (360,475))
    texte.Texte("Malus",couleur.Couleur().get_Noir(),372,545).affiche(police,fenetre)
    pygame.display.update()

    selection_malus = False
    while selection_malus != True:
        mouse_x, mouse_y = pygame.mouse.get_pos() # Recuperer les coordonnees de la souris
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # si le joueur quitte la fenetre # si le joueur quitte la fenetre
                pygame.quit()
                exit() 
            
            # Si le clique est presse
            if event.type == pygame.MOUSEBUTTONDOWN:  
                if 360 < mouse_x < 424 and 475 < mouse_y < 539:
                    liste_malus = ["reculer d'une case","reculer de deux cases","reculer de trois cases","perdre 20 pv","perdre 50 pv","perdre 80 pv","perdre 120 pv"]
                    malus = random.choice(liste_malus)
                    rectangle.Rectangle(100, 590, 390, 80).affiche(fenetre, couleur.Couleur().get_Beige())
                    texte.Texte("Tou-dou-dou-doum",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
                    pygame.time.delay(1000)
                    texte.Texte("Tu vas {}".format(malus),couleur.Couleur().get_Noir(),110, 620).affiche(police,fenetre)
                    if "reculer" in malus:
                        if malus == "reculer d'une case":
                            if un_joueur.get_plateaux() > 0:
                                # Definir les nouveaux pv suite à l'echange
                                un_joueur.set_plateaux((un_joueur.get_plateaux() - 1))
                                liste_joueur[un_joueur.get_ordre()][3] = un_joueur.get_plateaux()
                                
                                pygame.display.update() # Mettre à jour l'affichage
                                selection_malus = True
                                return liste_joueur
                            elif un_joueur.get_plateauy() > 0 and un_joueur.get_plateaux() <= 0:
                                # Definir les nouveaux pv suite à l'echange
                                un_joueur.set_plateauy((un_joueur.get_plateauy() - 1))
                                liste_joueur[un_joueur.get_ordre()][4] = un_joueur.get_plateauy()
                                
                                pygame.display.update() # Mettre à jour l'affichage
                                selection_malus = True
                                return liste_joueur
                            elif un_joueur.get_plateaux() <= 0 and un_joueur.get_plateauy() <= 0:
                                # Definir les nouveaux pv suite à l'echange
                                un_joueur.set_plateauy((un_joueur.get_plateaux() + 2))
                                liste_joueur[un_joueur.get_ordre()][4] = un_joueur.get_plateaux()
                                
                                pygame.display.update() # Mettre à jour l'affichage
                                selection_malus = True
                                return liste_joueur
                            
                        elif malus == "reculer de deux cases":
                            if un_joueur.get_plateaux() > 1:
                                # Definir les nouveaux pv suite à l'echange
                                un_joueur.set_plateaux((un_joueur.get_plateaux() - 2))
                                liste_joueur[un_joueur.get_ordre()][3] = un_joueur.get_plateaux()
                                
                                pygame.display.update() # Mettre à jour l'affichage
                                selection_malus = True
                                return liste_joueur
                            elif un_joueur.get_plateaux() <= 1 and un_joueur.get_plateauy() > 1:
                                # Definir les nouveaux pv suite à l'echange
                                un_joueur.set_plateauy((un_joueur.get_plateauy() - 2))
                                liste_joueur[un_joueur.get_ordre()][4] = un_joueur.get_plateauy()
                                
                                pygame.display.update() # Mettre à jour l'affichage
                                selection_malus = True
                                return liste_joueur
                            elif un_joueur.get_plateaux() <= 1 and un_joueur.get_plateauy() <= 1:
                                # Definir les nouveaux pv suite à l'echange
                                un_joueur.set_plateauy((un_joueur.get_plateaux() + 3))
                                liste_joueur[un_joueur.get_ordre()][4] = un_joueur.get_plateaux()
                                
                                pygame.display.update() # Mettre à jour l'affichage
                                selection_malus = True
                                return liste_joueur
                            
                        elif malus == "reculer de trois cases":
                            if un_joueur.get_plateaux() > 2:
                                # Definir les nouveaux pv suite à l'echange
                                un_joueur.set_plateaux((un_joueur.get_plateaux() - 3))
                                liste_joueur[un_joueur.get_ordre()][3] = un_joueur.get_plateaux()
                                
                                pygame.display.update() # Mettre à jour l'affichage
                                selection_malus = True
                                return liste_joueur
                            elif un_joueur.get_plateaux() <= 2 and un_joueur.get_plateauy() > 2:
                                # Definir les nouveaux pv suite à l'echange
                                un_joueur.set_plateauy((un_joueur.get_plateauy() - 3))
                                liste_joueur[un_joueur.get_ordre()][4] = un_joueur.get_plateauy()
                                
                                pygame.display.update() # Mettre à jour l'affichage
                                selection_malus = True
                                return liste_joueur
                            elif un_joueur.get_plateaux() <= 2 and un_joueur.get_plateauy() <= 2:
                                # Definir les nouveaux pv suite à l'echange
                                un_joueur.set_plateauy((un_joueur.get_plateaux() + 4))
                                liste_joueur[un_joueur.get_ordre()][4] = un_joueur.get_plateaux()
                                
                                pygame.display.update() # Mettre à jour l'affichage
                                selection_malus = True
                                return liste_joueur
                    else:
                        if malus == "perdre 20 pv":
                            if un_joueur.get_pv() > 20:
                                un_joueur.supprimer_pv(liste_joueur,20,fenetre)
                                selection_malus = True
                                return liste_joueur
                            else:
                                texte.Texte("Tu n'as plus assez de vie.",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
                                pygame.time.delay(1000)
                                Action_couleur_Noir()
                                
                        elif malus == "perdre 50 pv":
                            if un_joueur.get_pv() > 50:
                                # Definir les nouveaux pv suite à l'echange
                                un_joueur.supprimer_pv(liste_joueur,50,fenetre)
                                selection_malus = True
                                return liste_joueur
                            else:
                                texte.Texte("Tu n'as plus assez de vie.",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
                                pygame.time.delay(1000)
                                Action_couleur_Noir()
                                
                        elif malus == "perdre 80 pv":
                            if un_joueur.get_pv() > 80:
                                un_joueur.supprimer_pv(liste_joueur,80,fenetre)
                                selection_malus = True
                                return liste_joueur
                            else:
                                texte.Texte("Tu n'as plus assez de vie.",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
                                pygame.time.delay(1000)
                                Action_couleur_Noir()
                                
                        elif malus == "perdre 100 pv":
                            if un_joueur.get_pv() > 100:
                                # Definir les nouveaux pv suite à l'echange
                                un_joueur.supprimer_pv(liste_joueur,100,fenetre)
                                selection_malus = True
                                return liste_joueur
                            else:
                                texte.Texte("Tu n'as plus assez de vie.",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
                                pygame.time.delay(1000)
                                Action_couleur_Noir()

def Action_couleur_Rouge():
    if un_joueur.avoir_tt_cles() != True:
        un_ennemis = ennemis.Choix_ennemis(un_joueur)
    else:
         # Mettre la fenetre combat
        fenetre.fill((couleur.Couleur().get_Noir()))
        image_Arene = pygame.image.load("./assets/img/ennemis/Arene.png")
        image_redimensionnee = pygame.transform.scale(image_Arene, (800, 500))
        fenetre.blit(image_redimensionnee, (0, 0))
        Menu_bas()
        
        #Afficher le joueur et l'adversaire
        un_joueur.affichage_image(100,400,fenetre,police)
            
        # Affiche le texte 
        texte.Texte("Tu as deja combatu tous les boss, deplace-toi ", couleur.Couleur().get_Noir(), 110, 600).affiche(police,fenetre)
        texte.Texte("jusqu'à la hutte de la sorciere pour la tuer", couleur.Couleur().get_Noir(), 110, 620).affiche(police,fenetre)
        texte.Texte("et recuperer ta taille.", couleur.Couleur().get_Noir(), 110, 640).affiche(police,fenetre)
        pygame.display.update()
        pygame.time.delay(3500)
        
        combat_en_cours = False
        return un_joueur
    # Mettre la fenetre combat
    fenetre.fill((couleur.Couleur().get_Noir()))
    image_Arene = pygame.image.load("./assets/img/ennemis/Arene.png")
    image_redimensionnee = pygame.transform.scale(image_Arene, (800, 500))
    fenetre.blit(image_redimensionnee, (0, 0))
    Menu_bas()
    
    #Afficher le joueur et l'adversaire
    un_joueur.affichage_image(100,400,fenetre,police)
    un_ennemis.affichage_image(fenetre,police)
        
    # Affiche le texte 
    texte.Texte("Tu es en combat contre un ennemis feroce. Le celebre ", couleur.Couleur().get_Noir(), 110, 600).affiche(police,fenetre)
    texte.Texte("{}. Prepare toi à le combattre afin d'obtenir".format(un_ennemis.get_prenom()), couleur.Couleur().get_Noir(), 110, 620).affiche(police,fenetre)
    texte.Texte("la cle {}".format(un_ennemis.get_element()), couleur.Couleur().get_Noir(), 110, 640).affiche(police,fenetre)
    pygame.display.update()
    pygame.time.delay(3500)
    
    combat_en_cours = True
    # Tant que l'ennemis est en vie
    while combat_en_cours:
        if un_joueur.get_pv()>0:
            Menu_bas()
            un_ennemis.affichage_pv_combat(fenetre,police)
            # Dessiner le rectangle pour les pv du joueur
            texte.Texte("Que veux-tu faire ? Une attaque basique, une ", couleur.Couleur().get_Noir(), 110, 600).affiche(police,fenetre)
            texte.Texte("attaque speciale, te defendre ou prendre", couleur.Couleur().get_Noir(), 110, 620).affiche(police,fenetre)
            texte.Texte("la fuite ?", couleur.Couleur().get_Noir(), 110, 640).affiche(police,fenetre)
            image.Image(100,508,'assets/img/illustrations/Basique.png').affiche(fenetre)
            image.Image(250,508,'assets/img/illustrations/Speciale.png').affiche(fenetre)
            image.Image(400,508,'assets/img/illustrations/Defense.png').affiche(fenetre)
            image.Image(550,508,'assets/img/illustrations/Fuite.png').affiche(fenetre)
            pygame.display.update()

        selection_combat = False
        while selection_combat != True:
            mouse_x, mouse_y = pygame.mouse.get_pos() # Recuperer les coordonnees de la souris
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # si le joueur quitte la fenetre # si le joueur quitte la fenetre
                    pygame.quit()
                    exit() 
                
                # Si le clique est presse
                if event.type == pygame.MOUSEBUTTONDOWN:  
                    if 100 < mouse_x < 164 and 508 < mouse_y < 572:
                        toucher = random.choice([True,False,True])
                        if toucher == True:
                            if un_joueur.get_element() == un_ennemis.get_element():
                                #action_joueur = "attaque basique"
                                pv = random.randint(120,180)
                                un_ennemis.set_pv(un_ennemis.get_pv()-pv)
                            else:
                                #action_joueur = "attaque basique"
                                pv = random.randint(100,140)
                                un_ennemis.set_pv(un_ennemis.get_pv()-pv)
                            Menu_bas()
                            un_ennemis.affichage_pv_combat(fenetre,police)
                            texte.Texte("Tu as choisi de faire une attaque basique,", couleur.Couleur().get_Noir(), 110, 600).affiche(police,fenetre)
                            texte.Texte("bravo, l'ennemis a perdu {} pvs".format(pv), couleur.Couleur().get_Noir(), 110, 620).affiche(police,fenetre)
                            un_joueur.set_x(620); un_joueur.set_y(400)
                            pygame.display.update()
                            pygame.time.delay(2000)
                            un_joueur.set_x(100); un_joueur.set_y(400)
                            selection_combat = True
                        else:
                            Menu_bas()
                            un_ennemis.affichage_pv_combat(fenetre,police)
                            texte.Texte("L'ennemis a esquive le coup, dommage", couleur.Couleur().get_Noir(), 110, 600).affiche(police,fenetre)
                            texte.Texte("L'ennemis n'a pas perdu de pv", couleur.Couleur().get_Noir(), 110, 620).affiche(police,fenetre)
                            pygame.display.update()
                            pygame.time.delay(2000)
                            selection_combat = True
                    if 250 < mouse_x < 314 and 508 < mouse_y < 572:
                        #action_joueur = "attaque speciale"
                        toucher = random.choice([True,False])
                        if toucher == True:
                            pv = 187
                            un_ennemis.set_pv(un_ennemis.get_pv()-pv)
                            Menu_bas()
                            un_ennemis.affichage_pv_combat(fenetre,police)
                            texte.Texte("Tu as choisi de faire une attaque speciale,", couleur.Couleur().get_Noir(), 110, 600).affiche(police,fenetre)
                            texte.Texte("bravo, l'ennemis a perdu {} pvs".format(pv), couleur.Couleur().get_Noir(), 110, 620).affiche(police,fenetre)
                            un_joueur.set_x(620); un_joueur.set_y(400)
                            pygame.display.update()
                            pygame.time.delay(2000)
                            un_joueur.set_x(100); un_joueur.set_y(400)
                            selection_combat = True
                        else:
                            Menu_bas()
                            un_ennemis.affichage_pv_combat(fenetre,police)
                            texte.Texte("L'ennemis a esquive le coup, dommage", couleur.Couleur().get_Noir(), 110, 600).affiche(police,fenetre)
                            texte.Texte("L'ennemis n'a pas perdu de pv", couleur.Couleur().get_Noir(), 110, 620).affiche(police,fenetre)
                            pygame.display.update()
                            pygame.time.delay(2000)
                            selection_combat = True
                    if 400 < mouse_x < 464 and 508 < mouse_y < 572:
                        #action_joueur = "se defendre"
                        toucher = random.choice([True,False])
                        if toucher == True:
                            Menu_bas()
                            un_ennemis.set_attaque(un_ennemis.get_attaque()-20)
                            un_ennemis.affichage_pv_combat(fenetre,police)
                            texte.Texte("Tu as choisi de te defendre, tu fais une", couleur.Couleur().get_Noir(), 110, 600).affiche(police,fenetre)
                            texte.Texte("grimace au boss et cela reduit les degâts", couleur.Couleur().get_Noir(), 110, 620).affiche(police,fenetre)
                            texte.Texte("qu'il peut t'infliger." ,couleur.Couleur().get_Noir(), 110, 640).affiche(police,fenetre)
                            un_joueur.set_x(620); un_joueur.set_y(400)
                            pygame.display.update()
                            pygame.time.delay(2000)
                            un_joueur.set_x(100); un_joueur.set_y(400)
                            selection_combat = True
                        else:
                            Menu_bas()
                            un_ennemis.affichage_pv_combat(fenetre,police)
                            texte.Texte("L'ennemis n'a pas pris peur, les", couleur.Couleur().get_Noir(), 110, 600).affiche(police,fenetre)
                            texte.Texte("degâts qu'il t'inflige ne sont pas", couleur.Couleur().get_Noir(), 110, 620).affiche(police,fenetre)
                            texte.Texte("reduits.", couleur.Couleur().get_Noir(), 110, 640).affiche(police,fenetre)
                            pygame.display.update()
                            pygame.time.delay(2000)
                            selection_combat = True
                    if 550 < mouse_x < 614 and 508 < mouse_y < 572:
                        #action_joueur = "prendre la fuite"
                        Menu_bas()
                        un_ennemis.affichage_pv_combat(fenetre,police)      
                        texte.Texte("Tu as choisi de prendre la fuite, c'est", couleur.Couleur().get_Noir(), 110, 600).affiche(police,fenetre)
                        texte.Texte("surement le bon choix retente ta chance plus", couleur.Couleur().get_Noir(), 110, 620).affiche(police,fenetre)
                        texte.Texte("tard et detruit moi ce BOSS !!!" ,couleur.Couleur().get_Noir(), 110, 640).affiche(police,fenetre)
                        pygame.display.update()
                        pygame.time.delay(2000)
                        un_ennemis.set_pv(0)
                        liste_joueur[un_joueur.get_ordre()][5] = un_joueur.get_pv()
                        selection_combat = True; combat_en_cours =False
                        return un_joueur 
        if un_ennemis.get_pv()>0 and un_joueur.get_pv()>0:
            Menu_bas()
            toucher = random.choice([True,False])
            if toucher == True:
                pv = random.randint(un_ennemis.get_attaque(),un_ennemis.get_attaque() + 10)
                un_joueur.set_pv(un_joueur.get_pv() - pv)
                texte.Texte("Il te fais perdre {} pvs.".format(pv),couleur.Couleur().get_Noir(),110, 640).affiche(police,fenetre)
            else:
                texte.Texte("L'ennemi a rate son coup.",couleur.Couleur().get_Noir(),110, 640).affiche(police,fenetre)
            un_ennemis.affichage_pv_combat(fenetre,police)
            texte.Texte("C'est au tour du boss d'attaquer",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
            texte.Texte("Le boss reflechit...",couleur.Couleur().get_Noir(),110, 620).affiche(police,fenetre)
            un_ennemis.set_x(100); un_ennemis.set_y(400)
            pygame.display.update()
            pygame.time.delay(2000)
            un_ennemis.set_x(620); un_ennemis.set_y(400)
        elif un_joueur.get_pv()<=0:
            Menu_bas()
            liste_joueur[un_joueur.get_ordre()][5] = un_joueur.get_pv()
            un_ennemis.affichage_pv_combat(fenetre,police)
            texte.Texte("Fin du combat... Tu n'as pas survecu",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
            texte.Texte("à l'attaque du boss...",couleur.Couleur().get_Noir(),110, 620).affiche(police,fenetre)
            texte.Texte("Retour au plateau !",couleur.Couleur().get_Noir(),110, 640).affiche(police,fenetre)
            pygame.display.update()
            pygame.time.delay(1500)
            combat_en_cours = False
            selection_combat = True
            return un_joueur
        elif un_ennemis.get_pv()<=0 and un_joueur.get_pv()>=0 and un_joueur.avoir_tt_cles() != True:
            Menu_bas()
            liste_joueur[un_joueur.get_ordre()][5] = un_joueur.get_pv()
            un_ennemis.affichage_pv_combat(fenetre,police)
            texte.Texte("Fin du combat ! Bravo tu as vaincu le boss",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
            texte.Texte("{}, recupere les autres cles en tuant les".format(un_ennemis.get_element()),couleur.Couleur().get_Noir(),110, 620).affiche(police,fenetre)
            texte.Texte("autres boss et detruit cette sorciere !!!",couleur.Couleur().get_Noir(),110, 640).affiche(police,fenetre)
            un_joueur.set_inventaire(un_joueur.get_inventaire() + ["cle " + un_ennemis.get_element()])
            liste_joueur[un_joueur.get_ordre()][6] = un_joueur.get_inventaire() 
            un_joueur.affichage_cle(fenetre)           
            pygame.display.update()
            pygame.time.delay(1500)
            combat_en_cours =False
            selection_combat = True
            return un_joueur
        elif un_ennemis.get_pv()<=0 and un_joueur.get_pv()>=0 and un_joueur.avoir_tt_cles() == True:
            Menu_bas()
            liste_joueur[un_joueur.get_ordre()][5] = un_joueur.get_pv()
            un_ennemis.affichage_pv_combat(fenetre,police)
            texte.Texte("Fin du combat ! Bravo tu as vaincu le boss",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
            texte.Texte("{}, en plus de ça tu as toutes les cles, depeche ".format(un_ennemis.get_element()),couleur.Couleur().get_Noir(),110, 620).affiche(police,fenetre)
            texte.Texte("toi pour etre le premier à tuer la sorciere !!!",couleur.Couleur().get_Noir(),110, 640).affiche(police,fenetre)
            un_joueur.set_inventaire(un_joueur.get_inventaire() + ["cle " + un_ennemis.get_element()])
            liste_joueur[un_joueur.get_ordre()][6] = un_joueur.get_inventaire() 
            un_joueur.affichage_cle(fenetre)           
            pygame.display.update()
            pygame.time.delay(1500)
            combat_en_cours =False
            selection_combat = True
            return un_joueur     
        
def Action_couleur_Rose():
    # Dessiner le rectangle pour les dialogues
    rectangle.Rectangle(100, 590, 390, 80).affiche(fenetre, couleur.Couleur().get_Beige())
    texte.Texte("Tu es sur une case Chance",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
    texte.Texte("Clique pour decouvrir le pouvoir",couleur.Couleur().get_Noir(),110, 620).affiche(police,fenetre)
    texte.Texte("que le jeu va te donner.",couleur.Couleur().get_Noir(),110, 640).affiche(police,fenetre)
    pygame.display.update()
    pygame.time.delay(3200)
    
    chance = pygame.image.load("./assets/img/interraction/Chance.png")
    fenetre.blit(chance, (360,475))
    texte.Texte("Chance",couleur.Couleur().get_Noir(),369,545).affiche(police,fenetre)
    pygame.display.update()

    selection_malus = False
    while selection_malus != True:
        mouse_x, mouse_y = pygame.mouse.get_pos() # Recuperer les coordonnees de la souris
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # si le joueur quitte la fenetre # si le joueur quitte la fenetre
                pygame.quit()
                exit() 
            
            # Si le clique est presse
            if event.type == pygame.MOUSEBUTTONDOWN:  
                if 360 < mouse_x < 424 and 475 < mouse_y < 539:
                    liste_chance = ["gagner 100 pv","gagner 200 pv","gagner 500 pv", "gagner 150 pv","gagner 400 pv","gagner 1050 pv"]
                    chance = random.choice(liste_chance)
                    rectangle.Rectangle(100, 590, 390, 80).affiche(fenetre, couleur.Couleur().get_Beige())
                    texte.Texte("Tou-dou-dou-doum",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
                    pygame.time.delay(1000)
                    texte.Texte("Tu vas {}".format(chance),couleur.Couleur().get_Noir(),110, 620).affiche(police,fenetre)
                    # Definir les nouveaux pv suite à l'echange
                    if chance == "gagner 100 pv":
                        un_joueur.ajouter_pv(liste_joueur,100,fenetre)
                        selection_malus = True
                        return liste_joueur
                    elif chance == "gagner 200 pv":
                        un_joueur.ajouter_pv(liste_joueur,200,fenetre)
                        selection_malus = True
                        return liste_joueur
                    elif chance == "gagner 500 pv":
                        un_joueur.ajouter_pv(liste_joueur,500,fenetre)
                        selection_malus = True
                        return liste_joueur
                    elif chance == "gagner 150 pv":
                        un_joueur.ajouter_pv(liste_joueur,150,fenetre)
                        selection_malus = True
                        return liste_joueur
                    elif chance == "gagner 300 pv":
                        un_joueur.ajouter_pv(liste_joueur,300,fenetre)
                        selection_malus = True
                        return liste_joueur
                    elif chance == "gagner 1050 pv":
                        un_joueur.ajouter_pv(liste_joueur,1050,fenetre)
                        selection_malus = True
                        return liste_joueur                                                       
               
def Action_couleur_Gris():
    # Dessiner le rectangle pour les dialogues
    rectangle.Rectangle(100, 590, 390, 80).affiche(fenetre, couleur.Couleur().get_Beige())
    texte.Texte("Tu es sur une case Speciale ! Si tu tente",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
    texte.Texte("ta chance, tu as une chance sur deux gagner",couleur.Couleur().get_Noir(),110, 620).affiche(police,fenetre)
    texte.Texte("deux cles que tu n'as pas ou de tout perdre.",couleur.Couleur().get_Noir(),110, 640).affiche(police,fenetre)  
    pygame.display.update()
    pygame.time.delay(3200)
    
    # Cacher les anciens dialogues
    image.Image(0,468,'assets/img/illustrations/Page_choixdouble.png').affiche(fenetre)
    Menu_bas()
    rectangle.Rectangle(100, 590, 390, 80).affiche(fenetre, couleur.Couleur().get_Beige())
    texte.Texte("Veux-tu sacrifier une de tes cles afin de lancer le",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
    texte.Texte("tirage pour savoir si tu as la chance de gagner",couleur.Couleur().get_Noir(),110, 620).affiche(police,fenetre)
    texte.Texte("deux cles que tu n'as pas",couleur.Couleur().get_Noir(),110, 640).affiche(police,fenetre)
    pygame.display.update() # mettre à jour l'affichage
    
    # Afficher les logos et texte des cles et des pv
    cles = pygame.image.load("./assets/img/interraction/Cles.png")
    fenetre.blit(cles, (220, 480))
    retour = pygame.image.load("./assets/img/interraction/Retour.png")
    fenetre.blit(retour, (510,480))
    texte.Texte("1 clee",couleur.Couleur().get_Blanc(),215,545).affiche(police,fenetre)
    
    texte.Texte("Passer son tour",couleur.Couleur().get_Blanc(),505,545).affiche(police,fenetre)
    pygame.display.update() # mettre à jour l'affichage
    
    selection_speciale = False
    while selection_speciale != True:
        mouse_x, mouse_y = pygame.mouse.get_pos() # Recuperer les coordonnees de la souris
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # si le joueur quitte la fenetre # si le joueur quitte la fenetre
                pygame.quit()
                exit() 
            
            # Si le clique est presse
            if event.type == pygame.MOUSEBUTTONDOWN:  
                if 220 < mouse_x < 284 and 480 < mouse_y < 544:
                
                    # Si le joueur veut gagner la recompence
                    if un_joueur.get_inventaire() != []:    
                        choix_tirage = ["bravo", "oh non dommage"] 
                        tirage = random.choice(choix_tirage)   
                        if tirage == "bravo":
                            # Cacher les anciens dialogues
                            rectangle.Rectangle(100, 590, 390, 80).affiche(fenetre, couleur.Couleur().get_Beige())
                            texte.Texte("Bravo tu as gagner !!!",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
                            texte.Texte("Voilà deux cles supplementaires que tu peux",couleur.Couleur().get_Noir(),110, 620).affiche(police,fenetre)
                            texte.Texte("voir apparaître dans ton inventaire.",couleur.Couleur().get_Noir(),110, 640).affiche(police,fenetre)
                            
                            pygame.display.update() # Mettre à jour l'affichage    
                            selection_speciale = True
                            return liste_joueur
                        
                        else:
                            # Cacher les anciens dialogues
                            rectangle.Rectangle(100, 590, 390, 80).affiche(fenetre, couleur.Couleur().get_Beige())
                            texte.Texte("Oh non dommage...",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
                            texte.Texte("Tu peux retenter ta chance si tu as",couleur.Couleur().get_Noir(),110, 620).affiche(police,fenetre)
                            texte.Texte("d'autres cles :)",couleur.Couleur().get_Noir(),110, 640).affiche(police,fenetre)
                            
                            pygame.display.update() # Mettre à jour l'affichage  
                            selection_speciale = True
                            return liste_joueur
                    else:
                        # Cacher les anciens dialogues
                        rectangle.Rectangle(100, 590, 390, 80).affiche(fenetre, couleur.Couleur().get_Beige())
                        texte.Texte("Tu ne possede pas de cles.",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
                        texte.Texte("Obtient-en une en tuant un boss sur les",couleur.Couleur().get_Noir(),110, 620).affiche(police,fenetre)
                        texte.Texte("cases rouges.",couleur.Couleur().get_Noir(),110, 640).affiche(police,fenetre)
                        
                        pygame.display.update() # Mettre à jour l'affichage  
                        selection_speciale = True    
                        return liste_joueur
                elif 510 < mouse_x < 574 and 480 < mouse_y < 544:
                    # Si le joueur veut passer sont tour
                    # Cacher les anciens dialogues
                    rectangle.Rectangle(100, 590, 390, 80).affiche(fenetre, couleur.Couleur().get_Beige())
                    texte.Texte("Pas de soucis, retente ta chance une autre fois",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
                    pygame.display.update() # Mettre à jour l'affichage 
                    selection_speciale = True
                    return liste_joueur
            
def Action_couleur_Violet(case_decouverte,liste_joueur):
    # Dessiner le rectangle pour les dialogues
    rectangle.Rectangle(100, 590, 390, 80).affiche(fenetre, couleur.Couleur().get_Beige())
    texte.Texte("Tu es sur une case Rejoue !",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
    texte.Texte("Relance le de pour avoir un",couleur.Couleur().get_Noir(),110, 620).affiche(police,fenetre)
    texte.Texte("deuxieme lance",couleur.Couleur().get_Noir(),110, 640).affiche(police,fenetre)
    pygame.display.update()
    pygame.time.delay(3200)
    
    # Cacher les anciens dialogues
    rectangle.Rectangle(100, 590, 390, 80).affiche(fenetre, couleur.Couleur().get_Beige())
    de_face1 = pygame.image.load("./assets/img/de/Face1.png")
    fenetre.blit(de_face1,(350,475))
    texte.Texte("Clique sur le de ! ",couleur.Couleur().get_Noir(),110,600).affiche(police,fenetre)
    pygame.display.update()    
    case_decouverte = Page_direction(case_decouverte)
    Mise_a_jour(un_joueur.get_ordre())
    un_joueur.affiche_tt_joueur(liste_joueur,numero_joueur,fenetre)
    case_decouverte, liste_joueur = Page_action(case_decouverte)

    return case_decouverte

def Action_couleur_Beige():
    image.Image(0,468,'assets/img/illustrations/Page_choixdouble.png').affiche(fenetre)
    Menu_bas()
    # Dessiner le rectangle pour les dialogues
    rectangle.Rectangle(100, 590, 390, 80).affiche(fenetre, couleur.Couleur().get_Beige())
    texte.Texte("Tu es devant la Hutte de la sorciere.",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
    texte.Texte("Veux-tu essayer de l'ouvrir à l'aide",couleur.Couleur().get_Noir(),110, 620).affiche(police,fenetre)
    texte.Texte("des cles des quatre boss ?",couleur.Couleur().get_Noir(),110, 640).affiche(police,fenetre)
    pygame.display.update()
    pygame.time.delay(3200)
    
    # Afficher les logos et texte des cles et des pv
    pv = pygame.image.load("./assets/img/interraction/Cles.png")
    fenetre.blit(pv, (220, 480))
    retour = pygame.image.load("./assets/img/interraction/Retour.png")
    fenetre.blit(retour, (510,480))
    texte.Texte("Ouvrir la porte",couleur.Couleur().get_Blanc(),212,545).affiche(police,fenetre)
    texte.Texte("Passer son chemin",couleur.Couleur().get_Blanc(),485,545).affiche(police,fenetre)
    pygame.display.update()
    
    selection_sorciere = False
    while selection_sorciere != True:
        mouse_x, mouse_y = pygame.mouse.get_pos() # Recuperer les coordonnees de la souris
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # si le joueur quitte la fenetre # si le joueur quitte la fenetre
                pygame.quit()
                exit() 
            
            # Si le clique est presse
            if event.type == pygame.MOUSEBUTTONDOWN:  
                if 220 < mouse_x < 284 and 480 < mouse_y < 544:
                    if un_joueur.avoir_tt_cles() == True:
                        # Cacher les anciens dialogues
                        rectangle.Rectangle(100, 590, 390, 80).affiche(fenetre, couleur.Couleur().get_Beige())
                        texte.Texte("Bravo tu as trouve toutes les cles",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
                        texte.Texte("Ouvre la porte et apprete toi à",couleur.Couleur().get_Noir(),110, 620).affiche(police,fenetre)
                        texte.Texte("affronter la sorciere.",couleur.Couleur().get_Noir(),110, 640).affiche(police,fenetre)
                        pygame.display.update() # Mettre à jour l'affichage 
                        selection_sorciere = True
                        return liste_joueur
                    else:
                        # Cacher les anciens dialogues
                        rectangle.Rectangle(100, 590, 390, 80).affiche(fenetre, couleur.Couleur().get_Beige())
                        texte.Texte("Tu n'as pas encore recuperer toutes",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
                        texte.Texte("les cles afin d'ouvrir la porte de",couleur.Couleur().get_Noir(),110, 620).affiche(police,fenetre)
                        texte.Texte("la sorciere. Depeche-toi !",couleur.Couleur().get_Noir(),110, 640).affiche(police,fenetre)
                        pygame.display.update() # Mettre à jour l'affichage 
                        selection_sorciere = True
                        return liste_joueur
                    
                elif 510 < mouse_x < 574 and 480 < mouse_y < 544:
                    # Si le joueur veut passer sont tour
                    # Cacher les anciens dialogues
                    rectangle.Rectangle(100, 590, 390, 80).affiche(fenetre, couleur.Couleur().get_Beige())
                    texte.Texte("Pas de soucis, recupere les cles afin",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
                    texte.Texte("d'ouvrir la porte en premier !",couleur.Couleur().get_Noir(),110, 620).affiche(police,fenetre)
                    pygame.display.update() # Mettre à jour l'affichage 
                    selection_sorciere = True
                    return liste_joueur

def Page_sorciere():
    # Page de la sorcière quan don a réussi le jeu
    image.Image(0,0,'assets/img/illustrations/Page_maisonsorciere.png').affichage_image_redimensionnee(800, 700,fenetre)
    Menu_bas()
    texte.Texte("Tu es chez la sorciere, mais j'ai l'impression",couleur.Couleur().get_Noir(),110,600).affiche(police,fenetre)
    texte.Texte("qu'elle est sortie de sa taniere...",couleur.Couleur().get_Noir(),110,620).affiche(police,fenetre)
    texte.Texte("profite-en pour fouiller dans ses affaires :)",couleur.Couleur().get_Noir(),110,640).affiche(police,fenetre)
    pygame.display.update()
    pygame.time.delay(2500)
    selection_potion = False
    while selection_potion != True:
        mouse_x, mouse_y = pygame.mouse.get_pos() # Recuperer les coordonnees de la souris
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # si le joueur quitte la fenetre # si le joueur quitte la fenetre
                pygame.quit()
                exit() 
            
            # Si le clique est presse
            if event.type == pygame.MOUSEBUTTONDOWN:  
                if 500 < mouse_x < 725 and 150 < mouse_y < 450:
                    image.Image(0,0,'assets/img/illustrations/Page_maisonsymbole.png').affichage_image_redimensionnee(800, 700,fenetre)
                    Menu_bas()
                    texte.Texte("C'est un symbole astral, si c'est chez la",couleur.Couleur().get_Noir(),110,600).affiche(police,fenetre)
                    texte.Texte("sorciere, il vaut mieux ne pas y toucher",couleur.Couleur().get_Noir(),110,620).affiche(police,fenetre)
                    pygame.display.update()
                    pygame.time.delay(2500)
                    image.Image(0,0,'assets/img/illustrations/Page_maisonsorciere.png').affichage_image_redimensionnee(800, 700,fenetre)
                    Menu_bas()
                    texte.Texte("Tu es chez la sorciere, mais on dirait",couleur.Couleur().get_Noir(),110,600).affiche(police,fenetre)
                    texte.Texte("qu'elle est sortie de sa taniere...",couleur.Couleur().get_Noir(),110,620).affiche(police,fenetre)
                    texte.Texte("profite-en pour fouiller dans ses affaires :)",couleur.Couleur().get_Noir(),110,640).affiche(police,fenetre)
                    pygame.display.update()
                elif 90 < mouse_x < 190 and 180 < mouse_y < 350:
                    image.Image(0,0,'assets/img/illustrations/Page_maisondragon.png').affichage_image_redimensionnee(800, 700,fenetre)
                    Menu_bas()
                    texte.Texte("Un dragon de pierre... ce n'est pas très",couleur.Couleur().get_Noir(),110,600).affiche(police,fenetre)
                    texte.Texte("rassurant, trouvons vite un remède et sortons",couleur.Couleur().get_Noir(),110,620).affiche(police,fenetre)
                    texte.Texte("d'ici très vite",couleur.Couleur().get_Noir(),110,640).affiche(police,fenetre)
                    pygame.display.update()
                    pygame.time.delay(2500)
                    image.Image(0,0,'assets/img/illustrations/Page_maisonsorciere.png').affichage_image_redimensionnee(800, 700,fenetre)
                    Menu_bas()
                    texte.Texte("Tu es chez la sorciere, mais on dirait",couleur.Couleur().get_Noir(),110,600).affiche(police,fenetre)
                    texte.Texte("qu'elle est sortie de sa taniere...",couleur.Couleur().get_Noir(),110,620).affiche(police,fenetre)
                    texte.Texte("profite-en pour fouiller dans ses affaires :)",couleur.Couleur().get_Noir(),110,640).affiche(police,fenetre)
                    pygame.display.update()
                elif 330 < mouse_x < 430 and 480 < mouse_y < 580:
                    image.Image(0,0,'assets/img/illustrations/Page_maisonsorciere.png').affichage_image_redimensionnee(800, 700,fenetre)
                    Menu_bas()
                    texte.Texte("Tu as trouvé une potion... Potion inverstium",couleur.Couleur().get_Noir(),110,600).affiche(police,fenetre)
                    texte.Texte("Tu décides de la boire afin d'inverser le",couleur.Couleur().get_Noir(),110,620).affiche(police,fenetre)
                    texte.Texte("sortilège",couleur.Couleur().get_Noir(),110,640).affiche(police,fenetre)
                    un_joueur.set_inventaire(["Potion inverstium"])
                    un_joueur.affichage_potion(fenetre)
                    pygame.display.update()
                    pygame.time.delay(2500)
                    image.Image(0,0,'assets/img/illustrations/Page_findujeu.png').affichage_image_redimensionnee(800, 700,fenetre)
                    Menu_bas()
                    texte.Texte("Tu as terminé le jeu bravo à toi jeune aventurier",couleur.Couleur().get_Noir(),110,600).affiche(police,fenetre)
                    texte.Texte("Tu es le premier a t'être libéré du sort !!",couleur.Couleur().get_Noir(),110,620).affiche(police,fenetre)
                    pygame.display.update()
                    pygame.time.delay(2500)
 
def Action_couleur_Indigo():
    image.Image(0,468,'assets/img/illustrations/Page_choixdouble.png').affiche(fenetre)
    Menu_bas()
    # Dessiner le rectangle pour les dialogues
    rectangle.Rectangle(100, 590, 390, 80).affiche(fenetre, couleur.Couleur().get_Beige())
    texte.Texte("Tu es sur une case de Teleportation.",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
    texte.Texte("Veux-tu etre teleporter ?",couleur.Couleur().get_Noir(),110, 620).affiche(police,fenetre)
    
    
    # Afficher les logos et texte des cles et des pv
    pv = pygame.image.load("./assets/img/interraction/Teleportation.png")
    fenetre.blit(pv, (220, 480))
    retour = pygame.image.load("./assets/img/interraction/Retour.png")
    fenetre.blit(retour, (510,480))
    texte.Texte("Se teleporter",couleur.Couleur().get_Blanc(),212,545).affiche(police,fenetre)
    texte.Texte("Non merci",couleur.Couleur().get_Blanc(),502,545).affiche(police,fenetre)
    pygame.display.update()
    pygame.time.delay(3200)
    
    selection_teleporte = False
    while selection_teleporte != True:
        mouse_x, mouse_y = pygame.mouse.get_pos() # Recuperer les coordonnees de la souris
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # si le joueur quitte la fenetre # si le joueur quitte la fenetre
                pygame.quit()
                exit() 
            
            # Si le clique est presse
            if event.type == pygame.MOUSEBUTTONDOWN:  
                if 220 < mouse_x < 284 and 480 < mouse_y < 544:
                    # Cacher les anciens dialogues
                    rectangle.Rectangle(100, 590, 390, 80).affiche(fenetre, couleur.Couleur().get_Beige())
                    texte.Texte("Tou-dou-dou-doum",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
                    texte.Texte("Teleportation sur la deuxieme case",couleur.Couleur().get_Noir(),110, 620).affiche(police,fenetre)
                    texte.Texte("de teleportation" ,couleur.Couleur().get_Noir(),110, 640).affiche(police,fenetre)
                    
                    pygame.display.update() # Mettre à jour l'affichage 
                    coord_case_indigo = plateau_de_jeu.get_case_indigo(un_joueur)
                    un_joueur.set_plateaux(coord_case_indigo[0])
                    un_joueur.set_plateauy(coord_case_indigo[1])
                    Mise_a_jour(un_joueur.get_ordre())
                    selection_teleporte = True
                    return liste_joueur
                    
                elif 510 < mouse_x < 574 and 480 < mouse_y < 544:
                    # Si le joueur veut passer sont tour
                    # Cacher les anciens dialogues
                    rectangle.Rectangle(100, 590, 390, 80).affiche(fenetre, couleur.Couleur().get_Beige())
                    texte.Texte("Pas de soucis, essaye une prochaine",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
                    texte.Texte("fois si tu en as l'envie.",couleur.Couleur().get_Noir(),110, 620).affiche(police,fenetre)
                    
                    pygame.display.update() # Mettre à jour l'affichage 
                    selection_teleporte = True
                    return liste_joueur
    
def Action_couleur_Turquoise():
    # Dessiner le rectangle pour les dialogues
    rectangle.Rectangle(100, 590, 390, 80).affiche(fenetre, couleur.Couleur().get_Beige())
    texte.Texte("Tu es sur une case Grrr",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
    texte.Texte("Un tremblement de terre surgit de nul part",couleur.Couleur().get_Noir(),110, 620).affiche(police,fenetre)
    texte.Texte("et teleporte tous les joueurs !!!",couleur.Couleur().get_Noir(),110, 640).affiche(police,fenetre)
    pygame.display.update()
    pygame.time.delay(1000)
    
    for i in liste_joueur:
        i[3] = random.randint(0,9)
        i[4] = random.randint(0,16)
    pygame.display.update()
    
    return liste_joueur      

def Mise_a_jour(numero_joueur):
    # Met à jour la liste des joueurs
    if liste_joueur[numero_joueur][5] > 0:
        liste_joueur[numero_joueur][0] = un_joueur.get_ordre()
        liste_joueur[numero_joueur][1] = un_joueur.get_prenom()
        liste_joueur[numero_joueur][2] = un_joueur.get_element()
        liste_joueur[numero_joueur][3] = un_joueur.get_plateaux()
        liste_joueur[numero_joueur][4] = un_joueur.get_plateauy()
        liste_joueur[numero_joueur][5] = un_joueur.get_pv()
    else:
        liste_joueur.pop(un_joueur.get_ordre())
        Nombre_joueur()
    return liste_joueur
            
def Nombre_joueur():
    # Nombre de joueurs en vie
    for i in liste_joueur:
        numero_joueur = 0
        if i[0] > numero_joueur:
            numero_joueur = i[0]
    return numero_joueur
                   
def Combien_Attaquer():
    # Combien d'adversaire on peut attaquer
    nbjoueur_attaque = 0
    x1 = un_joueur.get_plateaux()
    y1 = un_joueur.get_plateauy()
    for i in liste_joueur:
        if (((i[3] == x1) or (i[3] == x1 + 1) or (i[3] == x1 - 1)) and ((i[4] == y1) or (i[4] == y1 + 1) or (i[4] == y1 - 1)) and (i[0] != un_joueur.get_ordre())):
            nbjoueur_attaque = nbjoueur_attaque + 1
    return nbjoueur_attaque

def Qui_Attaquer():
    # Quel adversaire on peut attaquer
    x1 = un_joueur.get_plateaux()
    y1 = un_joueur.get_plateauy()
    for i in liste_joueur:
        if (((i[3] == x1) or (i[3] == x1 + 1) or (i[3] == x1 - 1)) and ((i[4] == y1) or (i[4] == y1 + 1) or (i[4] == y1 - 1)) and (i[0] != un_joueur.get_ordre())):
            return i[0]
    return (-1)

def Peut_Attaquer():
    # Savoir si on a quelqu'un a attaqué
    attaquer = False
    x1 = un_joueur.get_plateaux()
    y1 = un_joueur.get_plateauy()
    for i in liste_joueur:
        if (((i[3] == x1) or (i[3] == x1 + 1) or (i[3] == x1 - 1)) and ((i[4] == y1) or (i[4] == y1 + 1) or (i[4] == y1 - 1)) and (i[0] != un_joueur.get_ordre())):
            attaquer = True
    return attaquer

def Combat_joueurs(ordre_adv):
    # Combats des joueurs
    joueur_adv = joueur.Joueur(liste_joueur[ordre_adv][0],liste_joueur[ordre_adv][1],liste_joueur[ordre_adv][2],liste_joueur[ordre_adv][3],liste_joueur[ordre_adv][4])
    joueur_adv.set_inventaire(liste_joueur[ordre_adv][6])
    joueur_adv.set_pv(liste_joueur[ordre_adv][5])
            
    # Mettre la fenetre combat
    fenetre.fill((couleur.Couleur().get_Noir()))
    image_Arene = pygame.image.load("./assets/img/ennemis/Arene.png")
    image_redimensionnee = pygame.transform.scale(image_Arene, (800, 500))
    fenetre.blit(image_redimensionnee, (0, 0))
    Menu_bas()
        
    #Afficher le joueur et l'adversaire
    un_joueur.affichage_image(100,400,fenetre,police)
    un_joueur.affichage_pv_combat(fenetre,police)
    joueur_adv.affichage_image(620,400,fenetre,police)
    joueur_adv.affichage_pv_combat_adv(fenetre,police)
        
    # Affiche le texte 
    texte.Texte("Tu as décidé de combattre un joueur. Le celebre ", couleur.Couleur().get_Noir(), 110, 600).affiche(police,fenetre)
    texte.Texte("{}. Prepare toi à le combattre afin de prendre".format(joueur_adv.get_prenom()), couleur.Couleur().get_Noir(), 110, 620).affiche(police,fenetre)
    texte.Texte("l'avantage sur lui !", couleur.Couleur().get_Noir(), 110, 640).affiche(police,fenetre)
    pygame.display.update()
    pygame.time.delay(3500)
    
    combat_en_cours = True
    # Tant que l'ennemis est en vie
    while combat_en_cours:
        if un_joueur.get_pv()>0:
            Menu_bas()
            joueur_adv.affichage_pv_combat_adv(fenetre,police)
            # Dessiner le rectangle pour les pv du joueur
            texte.Texte("Que veux-tu faire ? Une attaque basique, une ", couleur.Couleur().get_Noir(), 110, 600).affiche(police,fenetre)
            texte.Texte("attaque speciale, te defendre ou prendre", couleur.Couleur().get_Noir(), 110, 620).affiche(police,fenetre)
            texte.Texte("la fuite ?", couleur.Couleur().get_Noir(), 110, 640).affiche(police,fenetre)
            image.Image(100,508,'assets/img/illustrations/Basique.png').affiche(fenetre)
            image.Image(250,508,'assets/img/illustrations/Speciale.png').affiche(fenetre)
            image.Image(400,508,'assets/img/illustrations/Fuite.png').affiche(fenetre)
            pygame.display.update()

        selection_combat = False
        while selection_combat != True:
            if un_joueur.get_pv()<=0:
                Menu_bas()
                liste_joueur[un_joueur.get_ordre()][5] = un_joueur.get_pv()
                joueur_adv.affichage_pv_combat_adv(fenetre,police)
                texte.Texte("Fin du combat... Tu n'as pas survecu",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
                texte.Texte("à l'attaque de l'adversaire...",couleur.Couleur().get_Noir(),110, 620).affiche(police,fenetre)
                texte.Texte("Retour au plateau !",couleur.Couleur().get_Noir(),110, 640).affiche(police,fenetre)
                pygame.display.update()
                pygame.time.delay(1500)
                Mise_a_jour(joueur_adv.get_ordre())
                selection_combat = True
                combat_en_cours = False
                return un_joueur
            mouse_x, mouse_y = pygame.mouse.get_pos() # Recuperer les coordonnees de la souris
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # si le joueur quitte la fenetre # si le joueur quitte la fenetre
                    pygame.quit()
                    exit() 
                
                # Si le clique est presse
                if event.type == pygame.MOUSEBUTTONDOWN:  
                    if 100 < mouse_x < 164 and 508 < mouse_y < 572:
                        toucher = random.choice([True,False,True])
                        if toucher == True:
                            if un_joueur.get_element() == joueur_adv.get_element():
                                #action_joueur = "attaque basique"
                                pv = random.randint(120,180)
                                joueur_adv.set_pv(joueur_adv.get_pv()-pv)
                            else:
                                #action_joueur = "attaque basique"
                                pv = random.randint(100,140)
                                joueur_adv.set_pv(joueur_adv.get_pv()-pv)
                            Menu_bas()
                            joueur_adv.affichage_pv_combat_adv(fenetre,police)
                            texte.Texte("Tu as choisi de faire une attaque basique,", couleur.Couleur().get_Noir(), 110, 600).affiche(police,fenetre)
                            texte.Texte("bravo, l'adversaire a perdu {} pvs".format(pv), couleur.Couleur().get_Noir(), 110, 620).affiche(police,fenetre)
                            un_joueur.set_x(620); un_joueur.set_y(400)
                            pygame.display.update()
                            pygame.time.delay(2000)
                            un_joueur.set_x(100); un_joueur.set_y(400)
                            selection_combat = True
                        else:
                            Menu_bas()
                            joueur_adv.affichage_pv_combat_adv(fenetre,police)
                            texte.Texte("L'adversaire a esquive le coup, dommage", couleur.Couleur().get_Noir(), 110, 600).affiche(police,fenetre)
                            texte.Texte("L'adversaire n'a pas perdu de pv", couleur.Couleur().get_Noir(), 110, 620).affiche(police,fenetre)
                            un_joueur.set_x(620); un_joueur.set_y(400)
                            pygame.display.update()
                            pygame.time.delay(2000)
                            un_joueur.set_x(100); un_joueur.set_y(400)
                            selection_combat = True
                    if 250 < mouse_x < 314 and 508 < mouse_y < 572:
                        #action_joueur = "attaque speciale"
                        toucher = random.choice([True,False])
                        if toucher == True:
                            pv = 187
                            joueur_adv.set_pv(joueur_adv.get_pv()-pv)
                            Menu_bas()
                            joueur_adv.affichage_pv_combat_adv(fenetre,police)
                            texte.Texte("Tu as choisi de faire une attaque speciale,", couleur.Couleur().get_Noir(), 110, 600).affiche(police,fenetre)
                            texte.Texte("bravo, l'adversaire a perdu {} pvs".format(pv), couleur.Couleur().get_Noir(), 110, 620).affiche(police,fenetre)
                            un_joueur.set_x(620); un_joueur.set_y(400)
                            pygame.display.update()
                            pygame.time.delay(2000)
                            un_joueur.set_x(100); un_joueur.set_y(400)
                            selection_combat = True
                        else:
                            Menu_bas()
                            joueur_adv.affichage_pv_combat_adv(fenetre,police)
                            texte.Texte("L'adversaire a esquive le coup, dommage", couleur.Couleur().get_Noir(), 110, 600).affiche(police,fenetre)
                            texte.Texte("L'adversaire n'a pas perdu de pv", couleur.Couleur().get_Noir(), 110, 620).affiche(police,fenetre)
                            un_joueur.set_x(620); un_joueur.set_y(400)
                            pygame.display.update()
                            pygame.time.delay(2000)
                            un_joueur.set_x(100); un_joueur.set_y(400)
                            selection_combat = True
                    if 400 < mouse_x < 464 and 508 < mouse_y < 572:
                        #action_joueur = "prendre la fuite"
                        Menu_bas()
                        joueur_adv.affichage_pv_combat_adv(fenetre,police)      
                        texte.Texte("Tu as choisi de prendre la fuite, c'est", couleur.Couleur().get_Noir(), 110, 600).affiche(police,fenetre)
                        texte.Texte("surement le bon choix retente ta chance plus", couleur.Couleur().get_Noir(), 110, 620).affiche(police,fenetre)
                        texte.Texte("tard et detruit moi cet adversaire !!!" ,couleur.Couleur().get_Noir(), 110, 640).affiche(police,fenetre)
                        pygame.display.update()
                        pygame.time.delay(2000)
                        joueur_adv.set_pv(0)
                        liste_joueur[un_joueur.get_ordre()][5] = un_joueur.get_pv()
                        Mise_a_jour(joueur_adv.get_ordre())
                        selection_combat = True; combat_en_cours =False
                        return un_joueur
        if joueur_adv.get_pv()>0 and un_joueur.get_pv()>0:
            Menu_bas()
            toucher = random.choice([True,False])
            if toucher == True:
                pv = random.randint(joueur_adv.get_attaque(),joueur_adv.get_attaque() + 10)
                un_joueur.set_pv(un_joueur.get_pv() - pv)
                texte.Texte("Il te fais perdre {} pvs.".format(pv),couleur.Couleur().get_Noir(),110, 640).affiche(police,fenetre)
            else:
                texte.Texte("L'ennemi a rate son coup.",couleur.Couleur().get_Noir(),110, 640).affiche(police,fenetre)
            joueur_adv.affichage_pv_combat_adv(fenetre,police)
            texte.Texte("C'est au tour de l'adversaire d'attaquer",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
            texte.Texte("l'adversaire reflechit...",couleur.Couleur().get_Noir(),110, 620).affiche(police,fenetre)
            joueur_adv.set_x(100); joueur_adv.set_y(400)
            pygame.display.update()
            pygame.time.delay(2000)
            joueur_adv.set_x(620); joueur_adv.set_y(400)
        elif un_joueur.get_pv()<=0:
            Menu_bas()
            liste_joueur[un_joueur.get_ordre()][5] = un_joueur.get_pv()
            joueur_adv.affichage_pv_combat_adv(fenetre,police)
            texte.Texte("Fin du combat... Tu n'as pas survecu",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
            texte.Texte("à l'attaque de l'adversaire...",couleur.Couleur().get_Noir(),110, 620).affiche(police,fenetre)
            texte.Texte("Retour au plateau !",couleur.Couleur().get_Noir(),110, 640).affiche(police,fenetre)
            pygame.display.update()
            pygame.time.delay(1500)
            Mise_a_jour(joueur_adv.get_ordre())
            Menu_bas()
            plateau_de_jeu.plateau_cache(fenetre)
            plateau_de_jeu.mise_a_jour_plateau(case_decouverte,fenetre)
            un_joueur.affiche_tt_joueur(liste_joueur,numero_joueur,fenetre)
            selection_combat = True
            combat_en_cours = False
            return un_joueur
        elif joueur_adv.get_pv()<=0 and un_joueur.get_pv()>=0:
            Menu_bas()
            liste_joueur[un_joueur.get_ordre()][5] = un_joueur.get_pv()
            joueur_adv.affichage_pv_combat_adv(fenetre,police)
            texte.Texte("Fin du combat ! Bravo tu as vaincu l'adversaire",couleur.Couleur().get_Noir(),110, 600).affiche(police,fenetre)
            texte.Texte("tu as la chance de pouvoir lui voler tous ce qu'il".format(joueur_adv.get_element()),couleur.Couleur().get_Noir(),110, 620).affiche(police,fenetre)
            texte.Texte("avait sur lui en pv et en clé.",couleur.Couleur().get_Noir(),110, 640).affiche(police,fenetre)
            pygame.display.update()
            pygame.time.delay(1500)
            un_joueur.set_inventaire(un_joueur.get_inventaire() + joueur_adv.get_inventaire())
            un_joueur.set_pv(un_joueur.get_pv() + joueur_adv.get_pv())
            Mise_a_jour(un_joueur.get_ordre())
            Mise_a_jour(joueur_adv.get_ordre())
            Menu_bas()
            plateau_de_jeu.plateau_cache(fenetre)
            plateau_de_jeu.mise_a_jour_plateau(case_decouverte,fenetre)
            un_joueur.affiche_tt_joueur(liste_joueur,numero_joueur,fenetre)
            selection_combat = True
            combat_en_cours =False
            return un_joueur
                    
# ------------------------------------------------------------------------------------------------------ #

if __name__ == "__main__":
    # Initialisation de Pygame
    pygame.init()
    
    # Définir la musique
    song = pygame.mixer_music.load("assets/musique/Musique_jeu.mp3")
    pygame.mixer_music.play(-1,0.0,0)
    
    # etat initial du jeu
    etat_jeu = "demarrage_jeu"
    # Pour tous les joueurs encore en vie
    while etat_jeu != "fin_du_jeu": 
        # Gerer les etats du jeu
        
        while etat_jeu == "demarrage_jeu": # si le jeu demarre
            Page_demarrage()
            # Afficher le plateau
            plateau_de_jeu.remplir_plateau_aleatoirement()
            plateau_de_jeu.mise_a_jour_plateau(case_decouverte,fenetre)
            # Recuperer les coordonnees de la case jaune pour y afficher le joueur au demarrage du jeu
            coord_case_jaune = plateau_de_jeu.get_case_jaune()
            etat_jeu = "lancement_jeu"
            
        while etat_jeu == "lancement_jeu":  # si le joueur a clique sur start + affichage plateau
            # Affiche a page pour choisir le nombre de joueurs
            nb = Page_nb_joueur()
            while nb == 5:
                Page_demarrage()
                nb = Page_nb_joueur()
            numero_joueur = 0
            
            # tant qu'on a pas atteint le nombre final de joueur
            while numero_joueur != nb:
                # Afficher la proposition pour choisir le personnage
                prenom, element = Page_choixperso()
                while prenom == "Aucun":
                    nb = Page_nb_joueur()
                    while nb == 5:
                        Page_demarrage()
                        nb = Page_nb_joueur()
                    prenom, element = Page_choixperso()
                un_joueur = joueur.Joueur(numero_joueur,prenom,element,coord_case_jaune[0],coord_case_jaune[1])
                case_decouverte = case_decouverte + [[coord_case_jaune[0],coord_case_jaune[1]]]
                image.Image(0,0,'assets/img/illustrations/Page_jeu.png').affichage_image_redimensionnee(800, 700,fenetre)
                Menu_bas() # Affiche le plateau de jeu avec le personnage choisi
                Page_premier_mouvement()
                plateau_de_jeu.plateau_cache(fenetre)
                plateau_de_jeu.mise_a_jour_plateau(case_decouverte,fenetre)
                liste_joueur = liste_joueur + [[un_joueur.get_ordre(), un_joueur.get_prenom(), un_joueur.get_element(), un_joueur.get_plateaux(), un_joueur.get_plateauy(), un_joueur.get_pv(), un_joueur.get_inventaire()]]
                un_joueur.affiche_tt_joueur(liste_joueur,numero_joueur,fenetre)
                case_decouverte = Page_direction(case_decouverte)
                Mise_a_jour(un_joueur.get_ordre())
                un_joueur.affiche_tt_joueur(liste_joueur,numero_joueur,fenetre)
                case_decouverte, liste_joueur = Page_action(case_decouverte)
                numero_joueur = Nombre_joueur()
                pygame.time.delay(3400)
                Menu_bas()
                plateau_de_jeu.plateau_cache(fenetre)
                plateau_de_jeu.mise_a_jour_plateau(case_decouverte,fenetre)
                un_joueur.affiche_tt_joueur(liste_joueur,numero_joueur,fenetre)
                numero_joueur = numero_joueur + 1
                prenom = ""
                if un_joueur.a_gagne(plateau_de_jeu) == True:
                    etat_jeu = "fin_du_jeu"
                else:
                    etat_jeu = "partie_en_cours"    

        while etat_jeu == "partie_en_cours":
            if liste_joueur != []:
                for i in liste_joueur:
                    numero_joueur = i[0]
                    un_joueur = joueur.Joueur(i[0],i[1],i[2],i[3],i[4])
                    un_joueur.set_pv(i[5])
                    if un_joueur.get_pv()>=0:
                        un_joueur.set_inventaire(i[6])
                        un_joueur.affiche_tt_joueur(liste_joueur,numero_joueur,fenetre)
                        action_joueur = Page_mouvement()
                        numero_joueur = Nombre_joueur()
                        
                        # Si le joueur veut attaquer
                        if action_joueur == "Attaquer":
                            if Peut_Attaquer() == True:
                                Peut_Attaquer()
                                ordre_adv = Qui_Attaquer()
                                if ordre_adv != 2:
                                    Combat_joueurs(ordre_adv)
                            else:
                                Menu_bas() # Affiche le plateau de jeu avec le personnage choisi
                                texte.Texte("Personne n'est assez proche de toi pour ",couleur.Couleur().get_Noir(),110,600).affiche(police,fenetre)
                                texte.Texte("être attaquer. Rééssaye quand le joueur",couleur.Couleur().get_Noir(),110,620).affiche(police,fenetre)
                                texte.Texte("adverse sera plus proche de toi.",couleur.Couleur().get_Noir(),110,640).affiche(police,fenetre)
                                pygame.display.update()
                                pygame.time.delay(2000)
                            Menu_bas()
                            plateau_de_jeu.plateau_cache(fenetre)
                            plateau_de_jeu.mise_a_jour_plateau(case_decouverte,fenetre)
                            un_joueur.affiche_tt_joueur(liste_joueur,numero_joueur,fenetre)
                        else:
                        # Sinon le joueur lance le dé
                            Menu_bas() # Affiche le plateau de jeu avec le personnage choisi
                            texte.Texte("Clique sur le de ! ",couleur.Couleur().get_Noir(),110,600).affiche(police,fenetre)
                            numero_joueur = Nombre_joueur()
                            un_joueur.affiche_tt_joueur(liste_joueur,numero_joueur,fenetre)
                            case_decouverte = Page_direction(case_decouverte)
                            pygame.display.update()
                            Mise_a_jour(un_joueur.get_ordre())
                            un_joueur.affiche_tt_joueur(liste_joueur,numero_joueur,fenetre)
                            case_decouverte, liste_joueur = Page_action(case_decouverte)
                            numero_joueur = Nombre_joueur()
                            pygame.time.delay(3400)
                            Menu_bas()
                            plateau_de_jeu.plateau_cache(fenetre)
                            plateau_de_jeu.mise_a_jour_plateau(case_decouverte,fenetre)
                            un_joueur.affiche_tt_joueur(liste_joueur,numero_joueur,fenetre)
                            if un_joueur.a_gagne(plateau_de_jeu) == True:
                                etat_jeu = "fin_du_jeu"
                            else:
                                etat_jeu = "partie_en_cours"
                    else:
                        liste_joueur.pop(un_joueur.get_ordre())
                        print(numero_joueur)
                        numero_joueur = Nombre_joueur()
                        un_joueur.affiche_tt_joueur(liste_joueur,numero_joueur,fenetre)
                        texte.Texte("Tu es mort au combat, reviens vite ",couleur.Couleur().get_Noir(),110,600).affiche(police,fenetre)
                        texte.Texte("tenter ta chance jeune aventurier !",couleur.Couleur().get_Noir(),110,620).affiche(police,fenetre)
                        pygame.display.update()
                        pygame.time.delay(3400)
                        Menu_bas()
                        plateau_de_jeu.plateau_cache(fenetre)
                        plateau_de_jeu.mise_a_jour_plateau(case_decouverte,fenetre)
                        un_joueur.affiche_tt_joueur(liste_joueur,numero_joueur,fenetre)
            else: 
                etat_jeu = "fin_du_jeu"
                print(liste_joueur)

        if etat_jeu == "fin_du_jeu":
            if un_joueur.a_gagne(plateau_de_jeu) == True:
                un_joueur.set_inventaire([])
                Page_sorciere()
            else:
                print("Le jeu s'arrete à ce moment")
            pygame.quit()
