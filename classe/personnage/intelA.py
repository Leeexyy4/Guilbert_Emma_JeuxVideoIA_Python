import pygame
from random import randint
from classe.personnage import joueur
from classe.visuel import image

class IntelA (joueur.Joueur):
    def __init__(self, id, prenom, element, plateaux, plateauy, pv, attaque, inventaire) -> None:
        super().__init__(id, prenom, element, plateaux, plateauy, pv, attaque, inventaire)
    
    def choix_perso(self, interface):
        pass

    def lancement_de(self, interface) -> int:
        de_cliquer = False
        while de_cliquer == False:
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
                

