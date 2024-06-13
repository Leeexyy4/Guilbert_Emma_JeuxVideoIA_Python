from plateau import Plateau
import random, joueur, time
from input import inputs, direction
from enum import Enum
from utils import logique
class GameState(Enum):
    """la classe GameState regroupe les états de la partie selon les actions du joueur"""
    # attente d'action d'un joueur (idJOueur + GameState action)
    WAIT_PLAYER = 0 
    
    # Avatar ou Action
    SELECT_AVATAR = 1 # si !0 = dée sinn fight
    SELECT_ACTION = 2 # si !0 = dée sinn fight

    # De
    USE_DIE = 3 # envoie NB MOVE
    LANCEMENT_DE = 4 # Lance l'animation du dé et envoie le nb de déplacement possible
    
    # Direction
    MOVE_PLAYER = 5 # envoie nb déplacement restant + pos

    # Action_Case
    STAY_ON_CASE = 6 # envoie CASE_ACTION
    CASE_CHANCE = 7 # envoie CASE_CHANCE
    CASE_MALUS = 8 # envoie CASE_MALUS
    CASE_REJOUE = 9 # envoie CASE_REJOUE
    CASE_CLE_PUIT = 10 # envoie CASE_CLE_PUIT
    CASE_PV_PUIT = 10 # envoie CASE_CLE_PUIT
    CASE_TELEPORTE = 11 # envoie CASE_TELEPORTE
    CASE_CLE_SPECIALE = 12 # envoie CASE_CLE_SPECIALE
    CASE_PERDU_SPECIALE = 12 # envoie CASE_CLE_SPECIALE
    CASE_RETOUR = 13 # envoie CASE_CLE_SPECIALE

    # Sorciere
    CASE_FIN_DU_JEU = 15
    CASE_SORCIERE_SANS_CLE = 16

    # Combat
    ATTACK = 17
    FIGHT = 17
    WAIT_FIGHT_ACTION = 18
    DO_FIGHT_ACTION = 19 
    
    SWITCH_PLAYER = 20

    # Mort du joueur
    DEAD = 21
    

class Game():
    """la Classe Game initialise les paramètres de la partie"""
    def __init__(self, nombreJoueur:int, nombreIA:int, isLocal:bool = True) -> None:
        self.__nombreJoueur:int = nombreJoueur
        self.__listeJoueur:list[joueur.Joueur] = [None for i in range(nombreIA + nombreJoueur)]
        self.__plateau:Plateau = Plateau()
        self.__idJoueurActuel:int = 0
        self.__deValue:int = 0
        self.__etat:GameState = GameState.SELECT_AVATAR
        self.__timeaction:int = 0
        self.__delay:int = 150
        self.__chance_action:str = None
        self.__malus_action:str = None
        self.__special_action:str = None
        self.__deCd:int = 0
        self.__lastdeVal = 1
        self.__tours = 0
        self.__isLocal = isLocal
        self.resetTours()

    def autoInitPlayer(self) :
        start = self.__plateau.getCaseJaune()
        elems = [joueur.Element.GRASS, joueur.Element.WATER, joueur.Element.TOWN, joueur.Element.ROCK]
        self.__listeJoueur:list[joueur.Joueur] = [joueur.Joueur(i, start[0], start[1],elems[i] ) for i in range(self.__nombreJoueur)]

    def getlastdeVal(self)->int:
        """_summary_
            Getter de l'etat du joueur
        """
        return self.__lastdeVal

    def getNombreJoueur(self)->int:
        """_summary_
            Getter du nombre de joueur
        """
        return self.__nombreJoueur

    def setNombreJoueur(self, nombreJoueur):
        """_summary_
            Setter du nombre du joueur
        """
        self.__nombreJoueur = nombreJoueur

    def getListeJoueur(self)->list[joueur.Joueur]:
        """_summary_
            Getter de l'etat du joueur
        """
        return self.__listeJoueur

    def setListeJoueur(self, listeJoueur):
        """_summary_
            Setter de l'etat du joueur
        """
        self.__listeJoueur = listeJoueur
    
    def getIdJoueurActuel(self)->int:
        """_summary_
            Getter de l'etat du joueur
        """
        return self.__idJoueurActuel
    
    def setIdJoueurActuel(self, idJoueurActuel):
        """_summary_
            Setter de l'etat du joueur
        """
        self.__idJoueurActuel = idJoueurActuel

    def getSpecialAction(self)->str:
        """_summary_
            Getter de l'etat du joueur
        """
        return self.__special_action
    
    def setSpecialAction(self, Specialaction):
        """_summary_
            Setter de l'etat du joueur
        """
        self.__special_action = Specialaction
    

    def getChanceAction(self)->str:
        """_summary_
            Getter de l'etat du joueur
        """
        return self.__chance_action
    
    def setChanceAction(self, chanceaction):
        """_summary_
            Setter de l'etat du joueur
        """
        self.__chance_action = chanceaction
    
    def getMalusAction(self)->str:
        """_summary_
            Getter de l'etat du joueur
        """
        return self.__malus_action
    
    def setMalusAction(self, malusaction):
        """_summary_
            Setter de l'etat du joueur
        """
        self.__malus_action = malusaction
    
    def getDeValue(self)->int:
        """_summary_
            Getter de l'etat du joueur
        """
        return self.__deValue
    
    def setDeValue(self, deValue):
        """_summary_
            Setter de l'etat du joueur
        """
        self.__deValue = deValue
    
    def getEtat(self)->GameState:
        """_summary_
            Getter de l'etat du joueur
        """
        return self.__etat
    
    def setEtat(self,etat:GameState):
        """_summary_
            Setter l'etat du joueur
        """
        self.__etat = etat
        print(etat)
    
    def getPlateau(self)->Plateau:
        """Renvoie l'état du plateau"""
        return self.__plateau

    def setPlateau(self,plateau:Plateau):
        """_summary_
            Setter l'etat du joueur
        """
        self.__plateau = plateau
    
    def joueurSuivant(self):
        """Fonction qui décide quel est le joueur qui joue au prochain tour"""
        print(self.getIdJoueurActuel())
        print(len(self.getListeJoueur()))
        if self.getListeJoueur()[self.getIdJoueurActuel()].getPv() == 0:
            self.setListeJoueur(self.getListeJoueur().pop(self.getIdJoueurActuel()))
        if self.getIdJoueurActuel() < len(self.getListeJoueur())-1:
            self.setIdJoueurActuel(self.getIdJoueurActuel()+1)
        else:
            self.setIdJoueurActuel(0)
            self.__tours +=1
        print(self.getIdJoueurActuel())
    
    def personnageSelectionnable(self):
        """Renvoie la liste des personnages sélectionnables"""
        elems = [joueur.Element.GRASS, joueur.Element.WATER, joueur.Element.TOWN, joueur.Element.ROCK]
        for player in self.getListeJoueur():
            if isinstance(player, joueur.Joueur):
                elems.remove(player.getElement())
        return elems

    def resetTours(self):
        if self.__tours == 0:
            self.setEtat(GameState.SELECT_AVATAR if self.__isLocal else GameState.USE_DIE)
        else:
            self.setEtat(GameState.SELECT_ACTION)
    
    def loop(self, input:inputs):
        if self.getListeJoueur()[self.getIdJoueurActuel()] == None:
            self.setEtat(GameState.SELECT_AVATAR)
        player:joueur.Joueur = self.getListeJoueur()[self.getIdJoueurActuel()]
        match self.getEtat():

            # Logique_ChoixPerso
            case GameState.SELECT_AVATAR:
                if input.estClique(): 
                    start:tuple[int, int] = self.getPlateau().getCaseJaune()
                    if (500 <= input.getSourisx() <= 600 and 582 <= input.getSourisy() <= 652 and not joueur.Joueur.water_is_used):
                        self.getListeJoueur()[self.getIdJoueurActuel()] = joueur.Joueur(self.getIdJoueurActuel(), start[0], start[1], joueur.Element.WATER)
                        self.setEtat(GameState.USE_DIE)
                        # Si le personnage sur lequel on clique est Flora
                    elif (700 <= input.getSourisx() <= 800 and 582 <= input.getSourisy() <= 652 and not joueur.Joueur.grass_is_used): 
                        self.getListeJoueur()[self.getIdJoueurActuel()] = joueur.Joueur(self.getIdJoueurActuel(), start[0], start[1], joueur.Element.GRASS)
                        self.setEtat(GameState.USE_DIE)
                    # Si le personnage sur lequel on clique est Pierre
                    elif (400 <= input.getSourisx() <= 500 and 582 <= input.getSourisy() <= 652 and not joueur.Joueur.rock_is_used): 
                        self.getListeJoueur()[self.getIdJoueurActuel()] = joueur.Joueur(self.getIdJoueurActuel(), start[0], start[1], joueur.Element.ROCK)
                        self.setEtat(GameState.USE_DIE)
                    # Si le personnage sur lequel on clique est Kevin
                    elif (600 <= input.getSourisx() <= 700 and 582 <= input.getSourisy() <= 652 and not joueur.Joueur.town_is_used):
                        self.getListeJoueur()[self.getIdJoueurActuel()] = joueur.Joueur(self.getIdJoueurActuel(), start[0], start[1], joueur.Element.TOWN)
                        self.setEtat(GameState.USE_DIE)

            # Logique_PremierMouvement
            case GameState.USE_DIE:
                if input.estClique(): 
                    if 350 <= input.getSourisx() <= 435 and 475 <= input.getSourisy() <= 560:
                        self.setDeValue(random.randint(1,6))
                        self.__lastdeVal = self.__deValue
                        self.setEtat(GameState.LANCEMENT_DE)
            
            # Logique_Mouvement
            case GameState.SELECT_ACTION:
                if input.estClique(): 
                    if 220 <= input.getSourisx() <= 284 and 480 <= input.getSourisy() <= 544: self.setEtat(GameState.DO_FIGHT_ACTION)
                    if 510 <= input.getSourisx() <= 574 and 480 <= input.getSourisy() <= 544: self.setEtat(GameState.USE_DIE)
            
            # Logique_LancementDe
            case GameState.LANCEMENT_DE:
                delay = 0.23
                for i in range(6):
                    delay += 0.23 - int(0.19*(i/6))
                if(self.__deCd == 0):
                    self.__deCd = time.time()
                elif(self.__deCd+delay+0.5 <= time.time()):
                    self.setEtat(GameState.MOVE_PLAYER)
                    self.__deCd = 0
            
            # Logique_Direction
            case GameState.MOVE_PLAYER:
                if(self.getDeValue() == 0):
                    self.setEtat(GameState.STAY_ON_CASE)
                    return
                match input.getDirection():
                    case direction.NORTH:
                        if (self.getListeJoueur()[self.getIdJoueurActuel()].getPlateaux() -1 >= 0):
                            self.getListeJoueur()[self.getIdJoueurActuel()].setPlateaux(self.getListeJoueur()[self.getIdJoueurActuel()].getPlateaux()-1)
                            self.setDeValue(self.getDeValue() - 1)
                            if ([[self.getListeJoueur()[self.getIdJoueurActuel()].getPlateaux(),self.getListeJoueur()[self.getIdJoueurActuel()].getPlateauy()]] not in self.getPlateau().getCasesDecouvertes()):
                                self.getPlateau().setCasesDecouvertes(self.getPlateau().getCasesDecouvertes() + [[self.getListeJoueur()[self.getIdJoueurActuel()].getPlateaux(),self.getListeJoueur()[self.getIdJoueurActuel()].getPlateauy()]])
            
                    case direction.EAST:
                        if (self.getListeJoueur()[self.getIdJoueurActuel()].getPlateauy() +1 < 17):
                            self.getListeJoueur()[self.getIdJoueurActuel()].setPlateauy(self.getListeJoueur()[self.getIdJoueurActuel()].getPlateauy()+1)
                            self.setDeValue(self.getDeValue() - 1)
                            if ([[self.getListeJoueur()[self.getIdJoueurActuel()].getPlateaux(),self.getListeJoueur()[self.getIdJoueurActuel()].getPlateauy()]] not in self.getPlateau().getCasesDecouvertes()):
                                self.getPlateau().setCasesDecouvertes(self.getPlateau().getCasesDecouvertes() + [[self.getListeJoueur()[self.getIdJoueurActuel()].getPlateaux(),self.getListeJoueur()[self.getIdJoueurActuel()].getPlateauy()]])
            
                    case direction.SOUTH:
                        if (self.getListeJoueur()[self.getIdJoueurActuel()].getPlateaux() +1 < 10):
                            self.getListeJoueur()[self.getIdJoueurActuel()].setPlateaux(self.getListeJoueur()[self.getIdJoueurActuel()].getPlateaux()+1)
                            self.setDeValue(self.getDeValue() - 1)
                            if ([[self.getListeJoueur()[self.getIdJoueurActuel()].getPlateaux(),self.getListeJoueur()[self.getIdJoueurActuel()].getPlateauy()]] not in self.getPlateau().getCasesDecouvertes()):
                                self.getPlateau().setCasesDecouvertes(self.getPlateau().getCasesDecouvertes() + [[self.getListeJoueur()[self.getIdJoueurActuel()].getPlateaux(),self.getListeJoueur()[self.getIdJoueurActuel()].getPlateauy()]])
            
                    case direction.WEST:
                        if (self.getListeJoueur()[self.getIdJoueurActuel()].getPlateauy() -1 >= 0):
                            self.getListeJoueur()[self.getIdJoueurActuel()].setPlateauy(self.getListeJoueur()[self.getIdJoueurActuel()].getPlateauy()-1)
                            self.setDeValue(self.getDeValue() - 1)
                            if ([[self.getListeJoueur()[self.getIdJoueurActuel()].getPlateaux(),self.getListeJoueur()[self.getIdJoueurActuel()].getPlateauy()]] not in self.getPlateau().getCasesDecouvertes()):
                                self.getPlateau().setCasesDecouvertes(self.getPlateau().getCasesDecouvertes() + [[self.getListeJoueur()[self.getIdJoueurActuel()].getPlateaux(),self.getListeJoueur()[self.getIdJoueurActuel()].getPlateauy()]])
            
                
            # Logique_Action
            case GameState.STAY_ON_CASE:
                couleur_case = self.getPlateau().getCases(self.getListeJoueur()[self.getIdJoueurActuel()].getPlateaux(),self.getListeJoueur()[self.getIdJoueurActuel()].getPlateauy()).value.value
                print(self.getPlateau().getCases(self.getListeJoueur()[self.getIdJoueurActuel()].getPlateaux(),self.getListeJoueur()[self.getIdJoueurActuel()].getPlateauy()))
                match couleur_case:

                    case logique.Couleur.BEIGE.value:
                        if input.estClique():
                            if 220 <= input.getSourisx() <= 284 and 480 <= input.getSourisy() <= 544: 
                                if self.getListeJoueur()[self.getIdJoueurActuel()].avoirCles() == True:
                                    self.setEtat(GameState.CASE_FIN_DU_JEU)
                            elif 510 <= input.getSourisx() <= 574 and 480 <= input.getSourisy() <= 544:
                                self.setEtat(GameState.CASE_RETOUR)

                    case logique.Couleur.BLANC.value:
                        if self.__timeaction > time.time():
                            self.__delay = 150; self.__timeaction=0

                            self.setEtat(GameState.SWITCH_PLAYER)
                        else:
                            self.__delay -= 1
                            self.__timeaction = time.time() - self.__delay

                    case logique.Couleur.BLEU.value:
                        if input.estClique():
                            if (self.getListeJoueur()[self.getIdJoueurActuel()].getPv() > 200 and self.getListeJoueur()[self.getIdJoueurActuel()].getInventaire() != []):
                                if 220 <= input.getSourisx() <= 284 and 480 <= input.getSourisy() <= 544: 
                                    if self.getListeJoueur()[self.getIdJoueurActuel()].getPv() > 200:
                                        self.getListeJoueur()[self.getIdJoueurActuel()].setPv(self.getListeJoueur()[self.getIdJoueurActuel()] - 200)
                                        self.setEtat(GameState.SWITCH_PLAYER)
                                elif 510 <= input.getSourisx() <= 574 and 480 <= input.getSourisy() <= 544:
                                    if self.getListeJoueur()[self.getIdJoueurActuel()].getInventaire() != []:
                                        self.getListeJoueur()[self.getIdJoueurActuel()].setInventaire(self.getListeJoueur()[self.getIdJoueurActuel()].pop(random.randint(0,len(self.getListeJoueur()[self.getIdJoueurActuel()].getInventaire()))))
                                        self.setEtat(GameState.SWITCH_PLAYER)
                            else:
                                self.getListeJoueur()[self.getIdJoueurActuel()].setPv(0)
                                self.setEtat(GameState.DEAD)

                    case logique.Couleur.GRIS.value:
                        if input.estClique():
                            if 220 <= input.getSourisx() <= 284 and 480 <= input.getSourisy() <= 544: 
                                if self.getListeJoueur()[self.getIdJoueurActuel()].getInventaire() != []:
                                    self.getListeJoueur()[self.getIdJoueurActuel()].setPv(self.getListeJoueur()[self.getIdJoueurActuel()] - 200)
                                    self.setEtat(GameState.SWITCH_PLAYER)
                            elif 510 <= input.getSourisx() <= 574 and 480 <= input.getSourisy() <= 544:
                                self.setEtat(GameState.CASE_RETOUR)

                    case logique.Couleur.INDIGO.value:
                        if input.estClique():
                            if 220 <= input.getSourisx() <= 284 and 480 <= input.getSourisy() <= 544: 
                                self.getPlateau().getCaseIndigo(self.getListeJoueur()[self.getIdJoueurActuel()])
                                self.setEtat(GameState.CASE_TELEPORTE)
                            elif 510 <= input.getSourisx() <= 574 and 480 <= input.getSourisy() <= 544:
                                self.setEtat(GameState.CASE_RETOUR)
                    
                    case logique.Couleur.JAUNE.value:
                        self.setEtat(GameState.SWITCH_PLAYER)
                    
                    case logique.Couleur.NOIR.value:
                        if self.__timeaction > time.time():
                            self.__delay = 150; self.__timeaction=0

                            self.getListeJoueur()[self.getIdJoueurActuel()].setPv(0)
                            self.setEtat(GameState.DEAD)
                        else:
                            self.__delay -= 1
                            self.__timeaction = time.time() - self.__delay
                            
                    case logique.Couleur.ORANGE.value:
                        if input.estClique():
                            if 360 < input.getSourisx() < 424 and 475 < input.getSourisy() < 539:
                                liste_malus = [20,50,80,120,750]
                                self.setMalusAction(random.choice(liste_malus))
                                self.getListeJoueur()[self.getIdJoueurActuel()].setPv(self.getListeJoueur()[self.getIdJoueurActuel()].getPv() - self.getMalusAction())
                                self.setEtat(GameState.CASE_MALUS)
                        
                    case logique.Couleur.ROSE.value:
                        if input.estClique():
                            if 360 < input.getSourisx() < 424 and 475 < input.getSourisy() < 539:
                                liste_chance = [100,200,500,150,400,1050]
                                self.setChanceAction(random.choice(liste_chance))
                                self.getListeJoueur()[self.getIdJoueurActuel()].setPv(self.getListeJoueur()[self.getIdJoueurActuel()].getPv() + self.getChanceAction())
                                self.setEtat(GameState.CASE_CHANCE)

                    case logique.Couleur.GRIS.value:
                        if input.estClique():
                            if 220 < input.getSourisx() < 284 and 480 < input.getSourisy() < 544:
                                liste_special = ["bravo", "oh non dommage"]
                                self.setSpecialAction(random.choice(liste_special))
                                self.setEtat(GameState.CASE_CLE_SPECIALE)

                    case logique.Couleur.BLEU.value:
                        if input.estClique():
                            if 220 < input.getSourisx() < 284 and 480 < input.getSourisy() < 544:
                                if player.getPv() > 200:  
                                    player.setPv(player.getPv()-200)
                                    self.setEtat(GameState.CASE_CLE_PUIT)
                                else :
                                    player.setPv(0)
                                    self.setEtat(GameState.CASE_PV_PUIT)
                            elif 510 < input.getSourisx() < 574 and 480 < input.getSourisy() < 544:
                                if player.getInventaire() != []:
                                    player.getInventaire().pop(0)
                                    self.setEtat(GameState.CASE_PV_PUIT)
                                    
                        
                    case logique.Couleur.ROUGE.value:
                        pass
                        
                    case logique.Couleur.TURQUOISE.value:
                        self.getListeJoueur()[self.getIdJoueurActuel()].setPlateaux(random.randint(0,9))
                        self.getListeJoueur()[self.getIdJoueurActuel()].setPlateauy(random.randint(0,16))
                        if self.__timeaction > time.time():
                            self.__delay = 150; self.__timeaction=0
                            self.setEtat(GameState.SWITCH_PLAYER)
                        else:
                            self.__delay -= 1
                            self.__timeaction = time.time() - self.__delay
                            

                    case logique.Couleur.VIOLET.value:
                        self.setEtat(GameState.USE_DIE)

            case GameState.CASE_CHANCE:
                if self.__timeaction > time.time():
                    self.__delay = 150; self.__timeaction=0
                    self.setEtat(GameState.SWITCH_PLAYER)
                else:
                    self.__delay -= 1
                    self.__timeaction = time.time() - self.__delay

            case GameState.CASE_MALUS:
                if self.__timeaction > time.time(): 
                    self.__delay = 150; self.__timeaction=0
                    self.setEtat(GameState.SWITCH_PLAYER)
                else:
                    self.__delay -= 1
                    self.__timeaction = time.time() - self.__delay

            case GameState.CASE_CLE_SPECIALE:
                if self.__timeaction > time.time():
                    self.__delay = 150; self.__timeaction=0

                    self.setEtat(GameState.SWITCH_PLAYER)
                else:
                    self.__delay -= 1
                    self.__timeaction = time.time() - self.__delay


            case GameState.CASE_CLE_PUIT:
                if self.__timeaction > time.time():
                    self.__delay = 150; self.__timeaction=0

                    self.setEtat(GameState.SWITCH_PLAYER)
                else:
                    self.__delay -= 1
                    self.__timeaction = time.time() - self.__delay


            case GameState.CASE_PV_PUIT:
                if self.__timeaction > time.time():
                    self.__delay = 150; self.__timeaction=0
                    self.setEtat(GameState.SWITCH_PLAYER if(player.getPv()>0) else GameState.DEAD)
                else:
                    self.__delay -= 1
                    self.__timeaction = time.time() - self.__delay

                    
            case GameState.CASE_RETOUR:
                if self.__timeaction > time.time():
                    self.__delay = 150; self.__timeaction=0

                    self.setEtat(GameState.SWITCH_PLAYER)
                else:
                    self.__delay -= 1
                    self.__timeaction = time.time() - self.__delay

            
            case GameState.CASE_TELEPORTE:
                if self.__timeaction > time.time():
                    self.__delay = 150; self.__timeaction=0
                    self.setEtat(GameState.SWITCH_PLAYER)
                else:
                    self.__delay -= 1
                    self.__timeaction = time.time() - self.__delay

        
            # Combat
            case GameState.SELECT_ACTION:
                if 220 < input.getSourisx() < 284 and 480 < input.getSourisy() < 544:
                    self.setEtat(GameState.ATTACK)
                elif 510 <= input.getSourisx() <= 574 and 480 < input.getSourisy() < 544:
                    self.setEtat(GameState.USE_DIE)
            case GameState.FIGHT:
                pass
            case GameState.WAIT_FIGHT_ACTION:
                pass
            case GameState.DO_FIGHT_ACTION:
                self.setEtat(GameState.USE_DIE)
            case GameState.DEAD:
                pass
            case GameState.SWITCH_PLAYER:
                self.joueurSuivant()
                self.resetTours()