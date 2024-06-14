from plateau import Plateau
import random, joueur, time, ennemis, intelA
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
    ATTACK = 7 # attaquer joueur proche
    COMBAT_JOUEUR1 = 8 #le joueur adv est proche
    COMBAT_JOUEUR2 = 9 #attend la decision du joueur

    COMBAT_JOUEUR3 = 10 #attaque basique
    COMBAT_JOUEUR4 = 11 #attaque speciale
    COMBAT_JOUEUR5 = 12 #defence
    COMBAT_JOUEUR6 = 13 #prendre la fuite
    COMBAT_JOUEUR7 = 14 #attaque raté

    COMBAT_JOUEUR8 = 15 #joueur perdu
    COMBAT_JOUEUR9 = 16 #joueur_adv perdu

    CASE_CHANCE = 17 # envoie CASE_CHANCE
    CASE_MALUS = 18 # envoie CASE_MALUS
    CASE_REJOUE = 19 # envoie CASE_REJOUE
    CASE_CLE_PUIT = 20 # envoie CASE_CLE_PUIT
    CASE_PV_PUIT = 21 # envoie CASE_CLE_PUIT
    CASE_TELEPORTE = 22 # envoie CASE_TELEPORTE
    CASE_CLE_SPECIALE = 23 # envoie CASE_CLE_SPECIALE
    CASE_PERDU_SPECIALE = 24 # envoie CASE_CLE_SPECIALE
    CASE_RETOUR = 25 # envoie CASE_CLE_SPECIALE
    CASE_BOSS_TERMINE = 26 # envoie CASE_BOSS_TERMINE

    # Sorciere
    CASE_FIN_DU_JEU = 27

    # Combat
    FIGHT1 = 28 #affichage debut combat
    FIGHT2 = 29 #attend la decision du joueur

    FIGHT3 = 30 #attaque basique
    FIGHT4 = 31 #attaque spéciale
    FIGHT5 = 32 #defence
    FIGHT6 = 33 #Prendre la fuite
    FIGHT7 = 34 #attaque raté

    FIGHT8 = 35 #attaque boss reussie
    FIGHT9 = 36 #attaque boss raté

    FIGHT10 = 37 #joueur perdu
    FIGHT11 = 38 #boss perdu
    FIGHT12 = 39 #boss perdu + joueur.avoirCles()
    
    SWITCH_PLAYER = 40

    

class Game():
    """la Classe Game initialise les paramètres de la partie"""
    def __init__(self, nombreJoueur:int, nombreIA:int, isLocal:bool = True) -> None:
        self.__nombreJoueur:int = nombreJoueur
        self.__nombreIA:int = nombreIA
        self.__listeJoueur:list[joueur.Joueur] = [None for i in range(nombreIA + nombreJoueur)]
        self.__plateau:Plateau = Plateau()
        self.__idJoueurActuel:int = 0
        self.__bossActuel:ennemis.Ennemis = None
        self.__joueurAdverse:joueur.Joueur = None
        self.__pvInflige:int = 0
        self.__deValue:int = 0
        self.__etat:GameState = GameState.SELECT_AVATAR
        self.__timeaction:int = 0
        self.__delay:int = 75
        self.__chance_action:str = None
        self.__malus_action:str = None
        self.__special_action:str = None
        self.__deCd:int = 0
        self.__lastdeVal = 1
        self.__tours = 0
        self.__isLocal = isLocal
        self.__fin = False
        self.resetTours()

    def autoInitPlayer(self) :
        start = self.__plateau.getCaseJaune()
        elems = [joueur.Element.GRASS, joueur.Element.WATER, joueur.Element.TOWN, joueur.Element.ROCK]
        self.__listeJoueur:list[joueur.Joueur] = [joueur.Joueur(i, start[0], start[1],elems[i]) for i in range(self.__nombreJoueur)]

    def isEnd(self)->bool:
        """_summary_
            la partie est fin?
        """
        return self.__fin

    def isEnd(self)->bool:
        """_summary_
            la partie est fin?
        """
        return self.__fin

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
    
    def getNombreIA(self)->int:
        """_summary_
            Getter du nombre d'IA
        """
        return self.__nombreIA

    def setNombreIA(self, nombreIA):
        """_summary_
            Setter du nombre d'IA
        """
        self.__nombreIA = nombreIA

    def getJoueurAdv(self)->int:
        """_summary_
            Getter du joueur adversaire
        """
        return self.__joueurAdverse

    def setJoueurAdv(self, joueurAdv):
        """Setter du joueur adversaire"""
        self.__joueurAdverse = joueurAdv

    def getPvInflige(self)->int:
        """_summary_
            Getter du nombre de pv inflige par le boss ou le joueur
        """
        return self.__pvInflige

    def setPvInflige(self, pvInflige):
        """_summary_
            Setter du nombre de pv inflige par le boss ou le joueur
        """
        self.__pvInflige = pvInflige

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

    def getBossActuel(self)->ennemis.Ennemis:
        """_summary_
            Getter du boss a affronter
        """
        return self.__bossActuel
    
    def setBossActuel(self, bossActuel):
        """_summary_
            Setter du boss a affronter
        """
        self.__bossActuel = bossActuel

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
        if self.getListeJoueur()[self.getIdJoueurActuel()].getPv() <= 0:
            self.setListeJoueur(self.getListeJoueur().pop(self.getIdJoueurActuel()))
        if self.getIdJoueurActuel() < len(self.getListeJoueur())-1:
            self.setIdJoueurActuel(self.getIdJoueurActuel()+1)
        else:
            self.setIdJoueurActuel(0)
            self.__tours +=1
    
    def personnageSelectionnable(self):
        """Renvoie la liste des personnages sélectionnables"""
        elems = [joueur.Element.GRASS, joueur.Element.WATER, joueur.Element.TOWN, joueur.Element.ROCK]
        for player in self.getListeJoueur():
            if player != None:
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
        if self.getIdJoueurActuel() < self.getNombreJoueur():
            player:joueur.Joueur = self.getListeJoueur()[self.getIdJoueurActuel()]
        else:
            player:intelA.IntelA = self.getListeJoueur()[self.getIdJoueurActuel()]
        
        match self.getEtat():
            # Logique_ChoixPerso
            case GameState.SELECT_AVATAR:
                if input.estClique(): 
                    start:tuple[int, int] = self.getPlateau().getCaseJaune()
                    if (500 <= input.getSourisx() <= 600 and 582 <= input.getSourisy() <= 652 and joueur.Element.WATER in self.personnageSelectionnable()):
                        self.getListeJoueur()[self.getIdJoueurActuel()] = joueur.Joueur(self.getIdJoueurActuel(), start[0], start[1], joueur.Element.WATER)
                        self.setEtat(GameState.USE_DIE)
                        # Si le personnage sur lequel on clique est Flora
                    elif (700 <= input.getSourisx() <= 800 and 582 <= input.getSourisy() <= 652 and joueur.Element.GRASS in self.personnageSelectionnable()): 
                        self.getListeJoueur()[self.getIdJoueurActuel()] = joueur.Joueur(self.getIdJoueurActuel(), start[0], start[1], joueur.Element.GRASS)
                        self.setEtat(GameState.USE_DIE)
                    # Si le personnage sur lequel on clique est Pierre
                    elif (400 <= input.getSourisx() <= 500 and 582 <= input.getSourisy() <= 652 and joueur.Element.ROCK in self.personnageSelectionnable()): 
                        self.getListeJoueur()[self.getIdJoueurActuel()] = joueur.Joueur(self.getIdJoueurActuel(), start[0], start[1], joueur.Element.ROCK)
                        self.setEtat(GameState.USE_DIE)
                    # Si le personnage sur lequel on clique est Kevin
                    elif (600 <= input.getSourisx() <= 700 and 582 <= input.getSourisy() <= 652 and joueur.Element.TOWN in self.personnageSelectionnable()):
                        self.getListeJoueur()[self.getIdJoueurActuel()] = joueur.Joueur(self.getIdJoueurActuel(), start[0], start[1], joueur.Element.TOWN)
                        self.setEtat(GameState.USE_DIE)
                else:
                    if isinstance(player, intelA.IntelA) and player == None:
                        start:tuple[int, int] = self.getPlateau().getCaseJaune()
                        self.getListeJoueur()[self.getIdJoueurActuel()] = intelA.IntelA(self.getIdJoueurActuel(), start[0], start[1], random.choice(self.personnageSelectionnable()))
                        self.setEtat(GameState.USE_DIE)

            # Logique_PremierMouvement
            case GameState.USE_DIE:
                if input.estClique(): 
                    if 350 <= input.getSourisx() <= 435 and 475 <= input.getSourisy() <= 560:
                        self.setDeValue(random.randint(1,6))
                        self.__lastdeVal = self.__deValue
                        self.setEtat(GameState.LANCEMENT_DE)
                else:
                    if isinstance(player, intelA.IntelA):
                        self.setDeValue(random.randint(1,6))
                        self.__lastdeVal = self.__deValue
                        self.setEtat(GameState.LANCEMENT_DE)
            
            # Logique_Mouvement
            case GameState.SELECT_ACTION:
                if input.estClique(): 
                    if 220 <= input.getSourisx() <= 284 and 480 <= input.getSourisy() <= 544: self.setEtat(GameState.ATTACK)
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
                        if (player.getPlateaux() -1 >= 0):
                            player.setPlateaux(player.getPlateaux()-1)
                            self.setDeValue(self.getDeValue() - 1)
                            if ([[player.getPlateaux(),player.getPlateauy()]] not in self.getPlateau().getCasesDecouvertes()):
                                self.getPlateau().setCasesDecouvertes(self.getPlateau().getCasesDecouvertes() + [[player.getPlateaux(),player.getPlateauy()]])
            
                    case direction.EAST:
                        if (player.getPlateauy() +1 < 17):
                            player.setPlateauy(player.getPlateauy()+1)
                            self.setDeValue(self.getDeValue() - 1)
                            if ([[player.getPlateaux(),player.getPlateauy()]] not in self.getPlateau().getCasesDecouvertes()):
                                self.getPlateau().setCasesDecouvertes(self.getPlateau().getCasesDecouvertes() + [[player.getPlateaux(),player.getPlateauy()]])
            
                    case direction.SOUTH:
                        if (player.getPlateaux() +1 < 10):
                            player.setPlateaux(player.getPlateaux()+1)
                            self.setDeValue(self.getDeValue() - 1)
                            if ([[player.getPlateaux(),player.getPlateauy()]] not in self.getPlateau().getCasesDecouvertes()):
                                self.getPlateau().setCasesDecouvertes(self.getPlateau().getCasesDecouvertes() + [[player.getPlateaux(),player.getPlateauy()]])
            
                    case direction.WEST:
                        if (player.getPlateauy() -1 >= 0):
                            player.setPlateauy(player.getPlateauy()-1)
                            self.setDeValue(self.getDeValue() - 1)
                            if ([[player.getPlateaux(),player.getPlateauy()]] not in self.getPlateau().getCasesDecouvertes()):
                                self.getPlateau().setCasesDecouvertes(self.getPlateau().getCasesDecouvertes() + [[player.getPlateaux(),player.getPlateauy()]])
                if (isinstance(player, intelA.IntelA)):
                    player.choix_case_IA(self.getPlateau())
                
            # Logique_Action
            case GameState.STAY_ON_CASE:
                couleur_case = self.getPlateau().getCases(player.getPlateaux(),player.getPlateauy()).value.value
                match couleur_case:

                    case logique.Couleur.BEIGE.value:
                        if input.estClique():
                            if 220 <= input.getSourisx() <= 284 and 480 <= input.getSourisy() <= 544: 
                                if player.avoirCles():
                                    self.setEtat(GameState.CASE_FIN_DU_JEU)
                                else:
                                    self.setEtat(GameState.CASE_RETOUR)
                            elif 510 <= input.getSourisx() <= 574 and 480 <= input.getSourisy() <= 544:
                                self.setEtat(GameState.CASE_RETOUR)

                    case logique.Couleur.BLANC.value:
                        if self.__timeaction > time.time():
                            self.__delay = 75; self.__timeaction=0

                            self.setEtat(GameState.SWITCH_PLAYER)
                        else:
                            self.__delay -= 1
                            self.__timeaction = time.time() - self.__delay

                    case logique.Couleur.BLEU.value:
                        if input.estClique():
                            if (player.getPv() > 200 and player.getInventaire() != []):
                                if 220 <= input.getSourisx() <= 284 and 480 <= input.getSourisy() <= 544: 
                                    if player.getPv() > 200:
                                        player.setPv(player - 200)
                                        self.setEtat(GameState.SWITCH_PLAYER)
                                elif 510 <= input.getSourisx() <= 574 and 480 <= input.getSourisy() <= 544:
                                    if player.getInventaire() != []:
                                        player.setInventaire(player.pop(random.randint(0,len(player.getInventaire()))))
                                        self.setEtat(GameState.SWITCH_PLAYER)
                            else:
                                player.setPv(0)

                    case logique.Couleur.GRIS.value:
                        if input.estClique():
                            if 220 <= input.getSourisx() <= 284 and 480 <= input.getSourisy() <= 544: 
                                if player.getInventaire() != []:
                                    player.setPv(player - 200)
                                    self.setEtat(GameState.SWITCH_PLAYER)
                            elif 510 <= input.getSourisx() <= 574 and 480 <= input.getSourisy() <= 544:
                                self.setEtat(GameState.CASE_RETOUR)

                    case logique.Couleur.INDIGO.value:
                        if input.estClique():
                            if 220 <= input.getSourisx() <= 284 and 480 <= input.getSourisy() <= 544: 
                                self.getPlateau().getCaseIndigo(player)
                                self.setEtat(GameState.CASE_TELEPORTE)
                            elif 510 <= input.getSourisx() <= 574 and 480 <= input.getSourisy() <= 544:
                                self.setEtat(GameState.CASE_RETOUR)
                    
                    case logique.Couleur.JAUNE.value:
                        self.setEtat(GameState.SWITCH_PLAYER)
                    
                    case logique.Couleur.NOIR.value:
                        if self.__timeaction > time.time():
                            self.__delay = 75; self.__timeaction=0
                            player.setPv(0)
                        else:
                            self.__delay -= 1
                            self.__timeaction = time.time() - self.__delay
                            
                    case logique.Couleur.ORANGE.value:
                        if input.estClique():
                            if 360 < input.getSourisx() < 424 and 475 < input.getSourisy() < 539:
                                liste_malus = [20,50,80,120,750]
                                self.setMalusAction(random.choice(liste_malus))
                                player.setPv(player.getPv() - self.getMalusAction())
                                self.setEtat(GameState.CASE_MALUS)
                        
                    case logique.Couleur.ROSE.value:
                        if input.estClique():
                            if 360 < input.getSourisx() < 424 and 475 < input.getSourisy() < 539:
                                liste_chance = [100,200,500,150,400,1050]
                                self.setChanceAction(random.choice(liste_chance))
                                player.setPv(player.getPv() + self.getChanceAction())
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
                        if player.avoirCles():
                            self.setEtat(GameState.CASE_BOSS_TERMINE)
                        else:
                            self.setBossActuel(ennemis.Ennemis.Choix_ennemis(self.getListeJoueur()[self.getIdJoueurActuel()]))
                            self.setEtat(GameState.FIGHT1)
                        
                    case logique.Couleur.TURQUOISE.value:
                        player.setPlateaux(random.randint(0,9))
                        player.setPlateauy(random.randint(0,16))
                        self.getPlateau().setCasesDecouvertes(self.getPlateau().getCasesDecouvertes() + [[player.setPlateaux(),player.setPlateauy()]])
                        if self.__timeaction > time.time():
                            self.__delay = 75; self.__timeaction=0
                            self.setEtat(GameState.SWITCH_PLAYER)
                        else:
                            self.__delay -= 1
                            self.__timeaction = time.time() - self.__delay

                    case logique.Couleur.VIOLET.value:
                        self.setEtat(GameState.USE_DIE)

            case GameState.CASE_CHANCE:
                if self.__timeaction > time.time():
                    self.__delay = 75; self.__timeaction=0
                    self.setEtat(GameState.SWITCH_PLAYER)
                else:
                    self.__delay -= 1
                    self.__timeaction = time.time() - self.__delay

            case GameState.CASE_MALUS:
                if self.__timeaction > time.time(): 
                    self.__delay = 75; self.__timeaction=0
                    self.setEtat(GameState.SWITCH_PLAYER)
                else:
                    self.__delay -= 1
                    self.__timeaction = time.time() - self.__delay

            case GameState.CASE_CLE_SPECIALE:
                if self.__timeaction > time.time():
                    self.__delay = 75; self.__timeaction=0
                    self.setEtat(GameState.SWITCH_PLAYER)
                else:
                    self.__delay -= 1
                    self.__timeaction = time.time() - self.__delay


            case GameState.CASE_CLE_PUIT:
                if self.__timeaction > time.time():
                    self.__delay = 75; self.__timeaction=0
                    self.setEtat(GameState.SWITCH_PLAYER)
                else:
                    self.__delay -= 1
                    self.__timeaction = time.time() - self.__delay


            case GameState.CASE_PV_PUIT:
                if self.__timeaction > time.time():
                    self.__delay = 75; self.__timeaction=0
                    self.setEtat(GameState.SWITCH_PLAYER)
                else:
                    self.__delay -= 1
                    self.__timeaction = time.time() - self.__delay

                    
            case GameState.CASE_RETOUR:
                if self.__timeaction > time.time():
                    self.__delay = 75; self.__timeaction=0
                    self.setEtat(GameState.SWITCH_PLAYER)
                else:
                    self.__delay -= 1
                    self.__timeaction = time.time() - self.__delay

            
            case GameState.CASE_TELEPORTE:
                if self.__timeaction > time.time():
                    self.__delay = 75; self.__timeaction=0
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
            
            case GameState.ATTACK:
                if player.advPossibleAttaquer(self.getListeJoueur()) != - 1:
                    listeadvPossible = player.advPossibleAttaquer(self.getListeJoueur())
                    if len(listeadvPossible) == 1:
                        self.setJoueurAdv(self.getListeJoueur()[listeadvPossible[0]])
                        self.setEtat(GameState.COMBAT_JOUEUR1)
                    else:
                        self.setEtat(GameState.USE_DIE)
                else:
                    self.setEtat(GameState.USE_DIE)

            case GameState.COMBAT_JOUEUR1:
                if self.__timeaction > time.time():
                    self.__delay = 75; self.__timeaction=0
                    self.setEtat(GameState.COMBAT_JOUEUR2)
                else:
                    self.__delay -= 1
                    self.__timeaction = time.time() - self.__delay
            
            case GameState.COMBAT_JOUEUR2:
                if player.getPv() <= 0:
                    self.getListeJoueur()[self.getIdJoueurActuel()].setPv(0)
                    self.setEtat(GameState.COMBAT_JOUEUR7)
                elif self.getBossActuel().getPv() <= 0:
                    self.getListeJoueur()[self.getIdJoueurActuel()].setInventaire(self.getListeJoueur()[self.getIdJoueurActuel()].getInventaire() + ["cle " + self.getBossActuel().getElement()])
                    self.setEtat(GameState.COMBAT_JOUEUR8)
                elif self.getBossActuel().getPv() <= 0 and self.getListeJoueur()[self.getIdJoueurActuel()].avoirCles():
                    self.getListeJoueur()[self.getIdJoueurActuel()].setInventaire(self.getListeJoueur()[self.getIdJoueurActuel()].getInventaire() + ["cle " + self.getBossActuel().getElement()])
                    self.setEtat(GameState.COMBAT_JOUEUR9)
                elif self.getBossActuel().getPv() > 0 and self.getListeJoueur()[self.getIdJoueurActuel()].getPv() > 0:
                    if input.estClique():
                        if 100 < input.getSourisx() < 164 and 508 < input.getSourisy() < 572:
                            #action_joueur = "attaque basique"
                            toucher = random.choice([True,False,True])
                            if toucher == True:
                                self.setPvInflige(random.randint(player.getAttaque(),player.getAttaque()))
                                self.getBossActuel().setPv(self.getBossActuel().getPv()-self.getPvInflige())
                                if self.getBossActuel().getPv() > 0 and self.getListeJoueur()[self.getIdJoueurActuel()].getPv() > 0:
                                    self.setEtat(GameState.FIGHT3)
                                else:
                                    self.setEtat(GameState.FIGHT2)
                            else:
                                self.setEtat(GameState.FIGHT7)

                        elif 250 < input.getSourisx() < 314 and 508 < input.getSourisy() < 572:
                            #action_joueur = "attaque speciale"
                            toucher = random.choice([True,False])
                            if toucher == True:
                                self.setPvInflige(random.randint(player.getAttaque(),player.getAttaque()+50))
                                self.getBossActuel().setPv(self.getBossActuel().getPv()-self.getPvInflige())
                                if self.getBossActuel().getPv() > 0 and self.getListeJoueur()[self.getIdJoueurActuel()].getPv() > 0:
                                    self.setEtat(GameState.FIGHT4)
                                else:
                                    self.setEtat(GameState.FIGHT2)
                            else:
                                self.setEtat(GameState.FIGHT7)
                        
                        elif 400 < input.getSourisx() < 464 and 508 < input.getSourisy() < 572:
                            #action_joueur = "se defendre"
                            toucher = random.choice([True,False])
                            if toucher == True:
                                self.getBossActuel().setAttaque(self.getBossActuel().getAttaque()-20)
                                if self.getBossActuel().getPv() > 0 and self.getListeJoueur()[self.getIdJoueurActuel()].getPv() > 0:
                                    self.setEtat(GameState.FIGHT5)
                                else:
                                    self.setEtat(GameState.FIGHT2)
                            else:
                                self.setEtat(GameState.FIGHT7)

                        elif 550 < input.getSourisx() < 614 and 508 < input.getSourisy() < 572:
                            self.setEtat(GameState.FIGHT6)
            
            case GameState.CASE_BOSS_TERMINE:
                if self.__timeaction > time.time():
                    self.__delay = 75; self.__timeaction=0
                    self.setEtat(GameState.SWITCH_PLAYER)
                else:
                    self.__delay -= 1
                    self.__timeaction = time.time() - self.__delay
            
            case GameState.FIGHT1:
                if self.__timeaction > time.time():
                    self.__delay = 75; self.__timeaction=0
                    self.setEtat(GameState.FIGHT2)
                else:
                    self.__delay -= 1
                    self.__timeaction = time.time() - self.__delay
            
            case GameState.FIGHT2:
                if self.getListeJoueur()[self.getIdJoueurActuel()].getPv() <= 0:
                    self.getListeJoueur()[self.getIdJoueurActuel()].setPv(0)
                    self.setEtat(GameState.FIGHT10)
                elif self.getBossActuel().getPv() <= 0:
                    self.getListeJoueur()[self.getIdJoueurActuel()].setInventaire(self.getListeJoueur()[self.getIdJoueurActuel()].getInventaire() + ["cle " + self.getBossActuel().getElement()])
                    self.setEtat(GameState.FIGHT11)
                elif self.getBossActuel().getPv() <= 0 and self.getListeJoueur()[self.getIdJoueurActuel()].avoirCles():
                    self.getListeJoueur()[self.getIdJoueurActuel()].setInventaire(self.getListeJoueur()[self.getIdJoueurActuel()].getInventaire() + ["cle " + self.getBossActuel().getElement()])
                    self.setEtat(GameState.FIGHT12)
                elif self.getBossActuel().getPv() > 0 and self.getListeJoueur()[self.getIdJoueurActuel()].getPv() > 0:
                    if input.estClique():
                        if 100 < input.getSourisx() < 164 and 508 < input.getSourisy() < 572:
                            #action_joueur = "attaque basique"
                            toucher = random.choice([True,False,True])
                            if toucher == True:
                                self.setPvInflige(random.randint(player.getAttaque(),player.getAttaque()))
                                self.getBossActuel().setPv(self.getBossActuel().getPv()-self.getPvInflige())
                                if self.getBossActuel().getPv() > 0 and self.getListeJoueur()[self.getIdJoueurActuel()].getPv() > 0:
                                    self.setEtat(GameState.FIGHT3)
                                else:
                                    self.setEtat(GameState.FIGHT2)
                            else:
                                self.setEtat(GameState.FIGHT7)

                        elif 250 < input.getSourisx() < 314 and 508 < input.getSourisy() < 572:
                            #action_joueur = "attaque speciale"
                            toucher = random.choice([True,False])
                            if toucher == True:
                                self.setPvInflige(random.randint(player.getAttaque(),player.getAttaque()+50))
                                self.getBossActuel().setPv(self.getBossActuel().getPv()-self.getPvInflige())
                                if self.getBossActuel().getPv() > 0 and self.getListeJoueur()[self.getIdJoueurActuel()].getPv() > 0:
                                    self.setEtat(GameState.FIGHT4)
                                else:
                                    self.setEtat(GameState.FIGHT2)
                            else:
                                self.setEtat(GameState.FIGHT7)
                        
                        elif 400 < input.getSourisx() < 464 and 508 < input.getSourisy() < 572:
                            #action_joueur = "se defendre"
                            toucher = random.choice([True,False])
                            if toucher == True:
                                self.getBossActuel().setAttaque(self.getBossActuel().getAttaque()-20)
                                if self.getBossActuel().getPv() > 0 and self.getListeJoueur()[self.getIdJoueurActuel()].getPv() > 0:
                                    self.setEtat(GameState.FIGHT5)
                                else:
                                    self.setEtat(GameState.FIGHT2)
                            else:
                                self.setEtat(GameState.FIGHT7)

                        elif 550 < input.getSourisx() < 614 and 508 < input.getSourisy() < 572:
                            self.setEtat(GameState.FIGHT6)
            
            case GameState.FIGHT3:
                if self.__timeaction > time.time():
                    self.__delay = 75; self.__timeaction=0
                    self.setEtat(GameState.FIGHT7)
                else:
                    self.__delay -= 1
                    self.__timeaction = time.time() - self.__delay
            
            case GameState.FIGHT4:
                if self.__timeaction > time.time():
                    self.__delay = 75; self.__timeaction=0
                    self.setEtat(GameState.FIGHT7)
                else:
                    self.__delay -= 1
                    self.__timeaction = time.time() - self.__delay
            
            case GameState.FIGHT5:
                if self.__timeaction > time.time():
                    self.__delay = 75; self.__timeaction=0
                    self.setEtat(GameState.FIGHT7)
                else:
                    self.__delay -= 1
                    self.__timeaction = time.time() - self.__delay
            
            case GameState.FIGHT6:
                if self.__timeaction > time.time():
                    self.__delay = 75; self.__timeaction=0
                    self.setEtat(GameState.SWITCH_PLAYER)
                else:
                    self.__delay -= 1
                    self.__timeaction = time.time() - self.__delay
            
            case GameState.FIGHT7:
                if self.__timeaction > time.time():
                    self.__delay = 75; self.__timeaction=0
                    if self.getBossActuel().getPv() > 0 and self.getListeJoueur()[self.getIdJoueurActuel()].getPv() >0:
                        self.setEtat(random.choice([GameState.FIGHT8,GameState.FIGHT9]))
                    else:
                        self.setEtat(GameState.FIGHT2)
                else:
                    self.__delay -= 1
                    self.__timeaction = time.time() - self.__delay

            case GameState.FIGHT8:
                if self.__delay == 95:
                    self.setPvInflige(random.randint(self.getBossActuel().getAttaque(),self.getBossActuel().getAttaque()))
                    self.getListeJoueur()[self.getIdJoueurActuel()].setPv(self.getListeJoueur()[self.getIdJoueurActuel()].getPv()-self.getPvInflige())
                if self.__timeaction > time.time():
                    self.__delay = 95; self.__timeaction=0
                    self.setEtat(GameState.FIGHT2)
                else:
                    self.__delay -= 1
                    self.__timeaction = time.time() - self.__delay
            
            case GameState.FIGHT9:
                if self.__timeaction > time.time():
                    self.__delay = 95; self.__timeaction=0
                    self.setEtat(GameState.FIGHT2)
                else:
                    self.__delay -= 1
                    self.__timeaction = time.time() - self.__delay
            
            case GameState.FIGHT10:
                if self.__timeaction > time.time():
                    self.__delay = 120; self.__timeaction=0
                    self.setEtat(GameState.SWITCH_PLAYER)
                else:
                    self.__delay -= 1
                    self.__timeaction = time.time() - self.__delay
            
            case GameState.FIGHT11:
                if self.__timeaction > time.time():
                    self.__delay = 120; self.__timeaction=0
                    self.setEtat(GameState.SWITCH_PLAYER)
                else:
                    self.__delay -= 1
                    self.__timeaction = time.time() - self.__delay
            
            case GameState.FIGHT12:
                if self.__timeaction > time.time():
                    self.__delay = 120; self.__timeaction=0
                    self.setEtat(GameState.SWITCH_PLAYER)
                else:
                    self.__delay -= 1
                    self.__timeaction = time.time() - self.__delay
            
            case GameState.CASE_FIN_DU_JEU:
                if self.__timeaction > time.time():
                    self.__delay = 150; self.__timeaction=0
                    self.__fin = True
                else:
                    self.__delay -= 1
                    self.__timeaction = time.time() - self.__delay
            
            case GameState.SWITCH_PLAYER:
                self.joueurSuivant()
                self.resetTours()