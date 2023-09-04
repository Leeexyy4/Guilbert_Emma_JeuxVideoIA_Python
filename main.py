#Guilbert
#Emma

# ----------------------- Jeu de plateau - SAE C1 ------------------------ #

#pour les images : Pierre = https://www.flaticon.com/fr/icones-gratuites/age-de-pierre creees par Freepik - site web Flaticon
#                  Flora = https://www.flaticon.com/fr/icones-gratuites/gaia creees par BZZRINCANTATION - site web Flaticon
#                  Ondine = https://www.flaticon.com/fr/icones-gratuites/personnage creees par Freepik - site web Flaticon
#                  Kevin = https://www.flaticon.com/fr/icones-gratuites/garcon creees par Freepik - site web Flaticon
#                  Background1 = https://wall.alphacoders.com/big.php?i=1328702&lang=French Cree par GUSTLER - Site web Wallpaper Abyss


# ------------------------------------------------------------------------------------------------------ #

import pygame #importation de la bibliotheque Pygame afin de faire des graphiques

# ------------------------------------------------------------------------------------------------------ #

#La fonction permet de parametrer la fenetre du debut du jeu
def Fenetre_de_Jeu():
    
    # --- PARAMETRE FENETRE --- #
    pygame.init() #initialisation de la fenetre
    
    longueur_fenetre = 1280
    largeur_fenetre = 720
    
    pygame.display.set_caption("Jeu d'Emma Guilbert") #titre de la fenetre
    fenetre = pygame.display.set_mode((longueur_fenetre,largeur_fenetre)) #taille de la fenetre
    fond_jeu = pygame.image.load('assets\img\Background1.png') #importer le fond du jeu
    
    # ------------------------------------------------------------------------------------------------------ #
    
    # --- VARIABLE COULEURS --- #
    couleur_blanc = (255,255,255)
    couleur_noir = (0,0,0)
    
    # ------------------------------------------------------------------------------------------------------ #

    # --- BOUTON START --- #
    start_longueur = 200
    start_hauteur = 100
    start_x = longueur_fenetre/2 - start_longueur/2 #position du rectangle en x
    start_y = largeur_fenetre/2 - start_hauteur/2 #position du rectangle en y
    
    pygame.draw.rect(fond_jeu,couleur_blanc,(start_x,start_y,start_longueur,start_hauteur)) #bouton start
    police_texte_start = pygame.font.Font("./assets/font/Dosis-VariableFont_wght.ttf",50) #police du bouton start
    texte_start = police_texte_start.render("Start", True, couleur_noir) #texte du bouton
    
    # ------------------------------------------------------------------------------------------------------ #
    
    # --- JEU OUVERT --- #
    running = True #variable quand le jeu est ouvert
    while running == True: #boucle pour garder la fenetre ouverte
        
        fenetre.blit(fond_jeu,(0,0)) #appliquer l'arriere plan
        
        # --- GESTION BOUTON --- #
        fond_jeu.blit(texte_start, (start_x + start_longueur/4,start_y + start_hauteur/6)) #appliquer le bouton start
        
        mouse_x, mouse_y = pygame.mouse.get_pos() #recuperer les coordonnees de la souris

        pygame.display.flip() #mettre a jour l'affichage de la fenetre

        for event in pygame.event.get(): #pour verifier que l'evenement est la fermeture de la fenetre
            if event.type == pygame.QUIT : #si le joueur ferme la fenetre on quitte le jeu
                running = False #variable qui indique que le jeu se ferme
                pygame.quit() #quitte le jeu
            elif 540 <= mouse_x <= 740 and 310 <= mouse_y <= 410 :
                
                if event.type == pygame.MOUSEBUTTONDOWN : #si le joueur clique sur le bouton on passe à la prochaine page "introduction"
                    pygame.time.delay(1500) #met un delais avant d'effacer
                    fond_jeu.fill((0,0,0)) #change l'affichage en mettant tout en noir
                    texte_start = police_texte_start.render("Start", True, (0,0,0)) #texte du bouton
                    
                    import introduction #importe la prochaine page
         
# ------------------------------------------------------------------------------------------------------ #

if __name__ == "__main__":
    Fenetre_de_Jeu()
    