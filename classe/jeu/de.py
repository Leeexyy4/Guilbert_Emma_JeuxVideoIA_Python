# ----------------------- Jeu de plateau - De  ------------------------ #

# Bibliotheques utilisees pour le code
import pygame
from random import randint
from classe.personnage import intelA
from classe.visuel import image
#pour les images : De creees par Moi-meme side Piskel

class De:
    """La classe De est une classe qui permet de lancer le de."""

    def __init__(self) -> None:
        """Initialisation du de."""
        self.__face_choisie = 0

    def get_face_choisie(self):
        """Getter de la face aleatoire choisie."""
        return self.__face_choisie

    def set_face_choisie(self, face_choisie):
        """Setter de la face aleatoire choisie."""
        self.__face_choisie = face_choisie

    def desincrement_face_choisie(self, x):
        """Setter de la face aleatoire choisie."""
        self.__face_choisie = self.__face_choisie - x

    def Choix_de(self, interface, joueur):
        """La fonction Choix_De retourne la face aleatoire choisie du de (Surface surface).

        Returns:
            int face_choisie: Retourne la face aleatoire choisie
        """
        if isinstance(joueur,intelA.IntelA):
            joueur.lancement_de(interface)
        else:
            de_cliquer = False
            while de_cliquer == False:
                mouse_x, mouse_y = pygame.mouse.get_pos() # Recuperer les coordonnees de la souris
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: # si le joueur quitte la fenetre # si le joueur quitte la fenetre
                        pygame.quit()
                        exit()   
                    # Si le personnage sur lequel on clique est Kevin
                    if 350 <= mouse_x <= 435 and 475 <= mouse_y <= 560 :   
                        if event.type == pygame.MOUSEBUTTONDOWN : # Si le joueur clique sur le bouton, on passe à la prochaine page "introduction"
                            
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
            self.set_face_choisie(randint(1,6))
            
            if self.get_face_choisie() == 1:
                # Affiche le de sur la face 1
                de_face1 = image.De.FACE1.value
                interface.get_fenetre().blit(de_face1,(350,475))
                # Mettre à jour l'affichage
                pygame.display.update()
                
            elif self.get_face_choisie() == 2:
                # Affiche le de sur la face 2
                de_face2 = image.De.FACE2.value
                interface.get_fenetre().blit(de_face2,(350,475))
                # Mettre à jour l'affichage
                pygame.display.update()
                
            elif self.get_face_choisie() == 3:
                # Affiche le de sur la face 3
                de_face3 = image.De.FACE3.value
                interface.get_fenetre().blit(de_face3,(350,475))
                # Mettre à jour l'affichage
                pygame.display.update()
                
            elif self.get_face_choisie() == 4:
                # Affiche le de sur la face 4
                de_face4 = image.De.FACE4.value
                interface.get_fenetre().blit(de_face4,(350,475))
                # Mettre à jour l'affichage
                pygame.display.update()
                
            elif self.get_face_choisie() == 5:
                # Affiche le de sur la face 5
                de_face5 = image.De.FACE5.value
                interface.get_fenetre().blit(de_face5,(350,475))
                # Mettre à jour l'affichage
                pygame.display.update()
                
            elif self.get_face_choisie() == 6:
                # Affiche le de sur la face 6
                de_face6 = image.De.FACE6.value
                interface.get_fenetre().blit(de_face6,(350,475))
                # Mettre à jour l'affichage
                pygame.display.update()
                
            return self.get_face_choisie()
        

