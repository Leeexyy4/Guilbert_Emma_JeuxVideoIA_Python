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

    def getFaceDe(self):
        """Getter de la face aleatoire choisie."""
        return self.__face_choisie

    def setFaceDe(self, face_choisie):
        """Setter de la face aleatoire choisie."""
        self.__face_choisie = face_choisie

    def setFaceDeDesincremente(self, x):
        """Setter de la face aleatoire choisie."""
        self.__face_choisie = self.__face_choisie - x

    def getFaceAleatoireDe(self, interface, joueur):
        """La fonction Choix_De retourne la face aleatoire choisie du de (Surface surface).

        Returns:
            int face_choisie: Retourne la face aleatoire choisie
        """
        if isinstance(joueur,intelA.IntelA):
            joueur.lancement_de_IA(interface)
            pygame.time.delay(1500)
        else:
            de_cliquer = False
            while de_cliquer == False:
                mouse_x, mouse_y = pygame.mouse.get_pos() 
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: # si le joueur quitte la fenetre # si le joueur quitte la fenetre
                        pygame.quit()
                        exit()   
                    # Si le personnage sur lequel on clique est Kevin
                    if 360 <= mouse_x <= 435 and 475 <= mouse_y <= 560 :   
                        if event.type == pygame.MOUSEBUTTONDOWN : # Si le joueur clique sur le bouton, on passe à la prochaine page "introduction"
                            
                            # Affiche le de sur la face 2
                            interface.affichageAction([image.De.FACE2.value])
                            pygame.time.delay(150)
                            pygame.display.update()
                            
                            # Affiche le de sur la face 3
                            interface.affichageAction([image.De.FACE3.value])
                            pygame.time.delay(200)
                            pygame.display.update()

                            # Affiche le de sur la face 4
                            interface.affichageAction([image.De.FACE4.value])
                            pygame.time.delay(250)
                            pygame.display.update()

                            # Affiche le de sur la face 5
                            interface.affichageAction([image.De.FACE5.value])
                            pygame.time.delay(300)
                            pygame.display.update()

                            # Affiche le de sur la face 1
                            interface.affichageAction([image.De.FACE1.value])
                            pygame.time.delay(400)
                            pygame.display.update()

                            # Affiche le de sur la face 6
                            interface.affichageAction([image.De.FACE6.value])
                            pygame.time.delay(450)
                            pygame.display.update()
                            de_cliquer = True
                            
            # Choisir la face aleatoire
            self.setFaceDe(randint(1,6))
            
            if self.getFaceDe() == 1:
                # Affiche le de sur la face 1
                interface.affichageAction([image.De.FACE1.value])
                
            elif self.getFaceDe() == 2:
                # Affiche le de sur la face 2
                interface.affichageAction([image.De.FACE2.value])
                
            elif self.getFaceDe() == 3:
                # Affiche le de sur la face 3
                interface.affichageAction([image.De.FACE3.value])
                
            elif self.getFaceDe() == 4:
                # Affiche le de sur la face 4
                interface.affichageAction([image.De.FACE4.value])
                
            elif self.getFaceDe() == 5:
                # Affiche le de sur la face 5
                interface.affichageAction([image.De.FACE5.value])
                
            elif self.getFaceDe() == 6:
                # Affiche le de sur la face 6
                interface.affichageAction([image.De.FACE6.value])
            
            return self.getFaceDe()
        

