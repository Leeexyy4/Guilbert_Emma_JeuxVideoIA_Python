import pygame

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
largeur, hauteur = 800, 700

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Plateau de jeu")

# Définition des couleurs
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
JAUNE = (255, 255, 0)
VERT = (0, 255, 0)
VIOLET = (238, 130, 238)
ROUGE = (255, 0, 0)
GRIS = (128, 128, 128)
ROSE = (255, 192, 203)
TURQUOISE = (175,238,238)
INDIGO = (75, 0, 130)
ORANGE = (255, 127, 0)
BLEU = (0, 204, 204)
BEIGE = (255, 255, 204)

def Plateau_de_Jeu():
    # Taille d'une case
    taille_case = largeur // 17

    # Définition du plateau
    plateau = [
        [ROUGE, ROUGE, BLANC, BLANC, NOIR, NOIR, NOIR, NOIR, JAUNE, NOIR, NOIR, NOIR, NOIR, VIOLET, BLANC, ROUGE, ROUGE],
        [ROUGE, ROUGE, NOIR, ORANGE, NOIR, NOIR, NOIR, NOIR, ROSE, NOIR, NOIR, NOIR, NOIR, TURQUOISE, NOIR, ROUGE, ROUGE],
        [NOIR, NOIR, NOIR, BLANC, NOIR, VERT, VERT, NOIR, VIOLET, NOIR, VERT, VERT, NOIR, BLANC, NOIR, NOIR, NOIR],
        [VIOLET, BLANC, ROSE, BLANC, NOIR, NOIR, BLANC, NOIR, BLANC, NOIR, ROSE, NOIR, NOIR, BLANC, BLANC, ROSE, BLANC],
        [BLANC, NOIR, NOIR, NOIR,  NOIR, NOIR, BLANC, NOIR, ORANGE, NOIR, BLANC, NOIR, NOIR, NOIR, NOIR, NOIR, BLANC],
        [INDIGO, BLANC, BLANC, BLANC, BLANC, VIOLET, ROSE, BLANC, BLANC, TURQUOISE, BLANC, BLANC, TURQUOISE, BLANC, ORANGE, VIOLET, INDIGO],
        [ROSE, NOIR, NOIR, NOIR,  NOIR, BLANC, NOIR, NOIR, BLANC, NOIR, NOIR, BLEU, NOIR, NOIR, NOIR, NOIR, BLANC],
        [BLANC, TURQUOISE, ORANGE, BLANC, NOIR, ORANGE, NOIR, NOIR, BEIGE, NOIR, NOIR, BLANC, NOIR, BLANC, BLANC, BLANC, ORANGE],
        [NOIR, NOIR, NOIR, BLANC, NOIR, VERT, VERT, NOIR, BLEU, NOIR, GRIS, GRIS, NOIR, ROSE, NOIR, NOIR, NOIR],
        [ROUGE, ROUGE, NOIR, VIOLET, NOIR, NOIR, NOIR, NOIR, BLANC, NOIR, NOIR, NOIR, NOIR, VIOLET, NOIR, ROUGE, ROUGE],
        [ROUGE, ROUGE, BLANC, BLANC, NOIR, NOIR, NOIR, NOIR, JAUNE, NOIR, NOIR, NOIR, NOIR, BLANC, BLANC, ROUGE, ROUGE]
    ]

    # Définition des noms des cases
    nom_case = {
        ROUGE: "Boss",
        ROSE: "Chance",
        ORANGE: "Malus",
        INDIGO: "Move",
        VIOLET: "Replay",
        VERT: "Profit PV",
        TURQUOISE: "Retreat",
        BEIGE: "Witch",
        GRIS: "Special",
        BLEU: "Well"
    }

    # Police de texte
    font = pygame.font.Font(('./assets/font/Dosis-VariableFont_wght.ttf'), 12)

    # Boucle principale
    running = True
    while running:
        # Si le joueur quitte la fenêtre
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Dessiner le plateau de jeu
        for ligne in range(11):
            for colonne in range(17):
                couleur_case = plateau[ligne][colonne]
                pygame.draw.rect(fenetre, couleur_case, (colonne * taille_case, ligne * taille_case, taille_case, taille_case))

        # Écrire le nom de la case
                # Écrire le message de la case si la couleur correspond
                if couleur_case in nom_case:
                    message = nom_case[couleur_case]
                    text = font.render(message, True, NOIR)
                    fenetre.blit(text, (colonne * taille_case + taille_case/7, ligne * taille_case + taille_case/2.5))
                elif couleur_case == JAUNE and ligne == 0:
                    message = "Start"
                    text = font.render(message, True, NOIR)
                    fenetre.blit(text, (colonne * taille_case + taille_case/4.5, ligne * taille_case + taille_case/2.5))
                elif couleur_case == JAUNE and ligne == 10:
                    message = "Finish"
                    text = font.render(message, True, NOIR)
                    fenetre.blit(text, (colonne * taille_case + taille_case/4.5, ligne * taille_case + taille_case/2.5))
        
        # Dessiner les traits des cases
        for ligne in range(17):
            for colonne in range(13):
                if colonne != 12:
                    pygame.draw.line(fenetre,NOIR,(ligne * taille_case,colonne * taille_case),(ligne * taille_case + taille_case, colonne * taille_case),1)
                    pygame.draw.line(fenetre,NOIR,(ligne * taille_case,colonne * taille_case),(ligne * taille_case, colonne * taille_case + taille_case),1)
                else:
                    pygame.draw.line(fenetre,BLANC,(ligne * taille_case,colonne * taille_case),(ligne * taille_case + taille_case, colonne * taille_case),1)

        # Mettre à jour l'affichage
        pygame.display.flip()

    # Quitter Pygame
    pygame.quit()

# ------------------------------------------------------------------------------------------------------ #

if __name__ == "__main__":
    Plateau_de_Jeu()
    