from plateau import Plateau
import random
import joueur
from input import inputs, direction
from enum import Enum
class GameState(Enum):
    """la classe GameState regroupe les états de la partie selon les actions du joueur"""
    WAIT_PLAYER = 0 # attente d'action d'un joueur (idJOueur + GameState action)
    
    SELECT_AVATAR = 1 # si !0 = dée sinn fight
    
    SELECT_ACTION = 2 # si !0 = dée sinn fight
    
    USE_DIE = 3 # envoie NB MOVE
    
    MOVE_PLAYER = 4 # envoie nb déplacement restant + pos
    
    STAY_ON_CASE = 5 # envoie CASE_ACTION + changement en question


    FIGHT = 6 # envoi les 2joueur dans l'ordre d'action
    
    WAIT_FIGHT_ACTION = 7 # att les action de l'autre joueur

    DO_FIGHT_ACTION = 8 # envoi l'action chois
    
    DEAD = 9 # envoi l'action chois
    
    SWITCH_PLAYER = 10
class Game():
    """la Classe Game initialise les paramètres de la partie"""
    def __init__(self, nb_player:int, nb_IA:int) -> None:
        self.__nb_player:int = nb_player
        self.__players:list[joueur.Joueur] = [None for i in range(nb_IA + nb_player)]
        self.__plateau:Plateau = Plateau()
        self.__current_player:int = 0
        self.__die_value:int = 0
        self.__state:GameState = GameState.SELECT_AVATAR
        
    def getJoueur(self):
        """_summary_
            Getter de l'etat du joueur
        """
        return self.__players
    def getEtat(self):
        """_summary_
            Getter de l'etat du joueur
        """
        return self.__state
    
    def getJoueurActuel(self)->joueur.Joueur:
        """_summary_
            Getter de l'etat du joueur
        """
        return self.__players[self.__current_player]
    def setEtat(self,state:GameState):
        """_summary_
            Setter l'etat du joueur
        """
        self.__state = state
    
    
    def getPlateau(self)->Plateau:
        """Renvoie l'état du plateau"""
        return self.__plateau
    
    def joueurSuivant(self):
        """Fonction qui décide quel est le joueur qui joue au prochain tour"""
        self.__current_player = self.__current_player+1 if self.__current_player < len(self.__players)-2 else 0
    
    def personnageSelectionnable(self):
        """Renvoie la liste des personnages sélectionnables"""
        elems = [joueur.Element.GRASS, joueur.Element.WATER, joueur.Element.TOWN, joueur.Element.ROCK]
        for player in self.__players:
            if isinstance(player, joueur.Joueur):
                elems.remove(player.get_element)
        return elems
    
    def loop(self, input:inputs):
        if self.__players[self.__current_player] == None:
            self.__state = GameState.SELECT_AVATAR
        
        player:joueur.Joueur = self.__players[self.__current_player]
        match self.__state:
            case GameState.SELECT_AVATAR:
                if input.estClique(): 
                    start:tuple[int, int] = self.__plateau.getCaseJaune()
                    if (500 <= input.getSourisx() <= 600 and 582 <= input.getSourisy() <= 652 and not joueur.Joueur.water_is_used):
                        self.__players[self.__current_player] = joueur.Joueur(self.__current_player, start[0], start[1], joueur.Element.WATER)
                        self.__state = GameState.USE_DIE
                        # Si le personnage sur lequel on clique est Flora
                    elif (700 <= input.getSourisx() <= 800 and 582 <= input.getSourisy() <= 652 and not joueur.Joueur.grass_is_used): 
                        self.__players[self.__current_player] = joueur.Joueur(self.__current_player, start[0], start[1], joueur.Element.GRASS)
                        self.__state = GameState.USE_DIE
                    # Si le personnage sur lequel on clique est Pierre
                    elif (400 <= input.getSourisx() <= 500 and 582 <= input.getSourisy() <= 652 and not joueur.Joueur.rock_is_used): 
                        self.__players[self.__current_player] = joueur.Joueur(self.__current_player, start[0], start[1], joueur.Element.ROCK)
                        self.__state = GameState.USE_DIE
                    # Si le personnage sur lequel on clique est Kevin
                    elif (600 <= input.getSourisx() <= 700 and 582 <= input.getSourisy() <= 652 and not joueur.Joueur.town_is_used):
                        self.__players[self.__current_player] = joueur.Joueur(self.__current_player, start[0], start[1], joueur.Element.TOWN)
                        self.__state = GameState.USE_DIE

            case GameState.SELECT_ACTION:
                if input.estClique(): 
                    if 220 <= input.getSourisx() <= 284 and 480 <= input.getSourisy() <= 544: self.__state = GameState.DO_FIGHT_ACTION
                    if 510 <= input.getSourisx() <= 574 and 480 <= input.getSourisy() <= 544: self.__state = GameState.USE_DIE
            
            case GameState.USE_DIE:
                if input.estClique(): 
                    if 350 <= input.getSourisx() <= 435 and 475 <= input.getSourisy() <= 560:
                        self.__die_value = random.randint(1,6)
                        print(self.__die_value)
                        self.__state = GameState.MOVE_PLAYER
                        
            case GameState.MOVE_PLAYER:
                if(self.__die_value == 0):
                    self.__state = GameState.STAY_ON_CASE
                    return
                match input.getDirection():
                    case direction.NORTH :
                        player.setPlateauy(player.getPlateauy()-1)
                        self.__die_value -=1
                        print(self.__die_value)
                    case direction.EAST :
                        player.setPlateauy(player.getPlateauy()+1)
                        self.__die_value -=1
                        print(self.__die_value)
                    case direction.SOUTH :
                        player.setPlateaux(player.getPlateaux()+1)
                        self.__die_value -=1
                        print(self.__die_value)
                    case direction.WEST :
                        player.setPlateaux(player.getPlateaux()-1)
                        self.__die_value -=1
                        print(self.__die_value)
                
            case GameState.STAY_ON_CASE:
                # Rajouté les effets de la case
                self.joueurSuivant()
                self.__state = GameState.SELECT_ACTION
                
            case GameState.FIGHT:
                pass
            case GameState.WAIT_FIGHT_ACTION:
                pass
            case GameState.DO_FIGHT_ACTION:
                self.__state = GameState.USE_DIE
            case GameState.DEAD:
                pass
            case GameState.SWITCH_PLAYER:
                pass
