#Guilbert
#Emma

# ----------------------- Jeu de plateau - SAE C1 ------------------------ #

import pygame #importation de la bibliotheque Pygame afin de faire des graphiques

# ------------------------------------------------------------------------------------------------------ #

def Fenetre_d_Introduction():
    
    # --- PARAMETRE FENETRE --- #
    pygame.init() #initialisation de la fenetre
    
    longueur_fenetre = 1200
    largeur_fenetre = 700
    
    pygame.display.set_caption("Jeu d'Emma Guilbert") #titre de la fenetre
    fenetre = pygame.display.set_mode((longueur_fenetre,largeur_fenetre)) #taille de la fenetre
    fond_jeu = pygame.image.load('assets\img\Background1.png') #importer le fond du jeu
    
    # ------------------------------------------------------------------------------------------------------ #

    # --- JEU OUVERT --- #
    running = True #variable quand le jeu est ouvert
    while running == True: #boucle pour garder la fenetre ouverte
        
        for event in pygame.event.get(): #pour verifier que l'evenement est la fermeture de la fenetre
            if event.type == pygame.QUIT : #si le joueur ferme la fenetre on quitte le jeu
                running = False #variabzle qui indique que le jeu se ferme
                pygame.quit() #quitte le jeu
        
        # Attendre un peu après l'affichage complet
        pygame.time.delay(1000)
        import plateau

# ------------------------------------------------------------------------------------------------------ #

if __name__ == "__main__":
    Fenetre_d_Introduction()