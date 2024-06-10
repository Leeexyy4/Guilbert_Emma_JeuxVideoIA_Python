from plateau import Plateau
import joueur
from input import inputs
from enum import Enum
class Game_State(Enum):
    WAIT_PLAYER = 0 # attente d'action d'un joueur (idJOueur + Game_State action)
    
    SELECT_AVARTAR = 1 # si !0 = dée sinn fight
    
    SELECT_ACTION = 2 # si !0 = dée sinn fight
    
    USE_DIE = 3 # envoi NB MOVE
    
    MOVE_PLAYER = 4 # envoi nb déplacement restant + pos
    
    STAY_ON_CASE = 5 # envoi CASE_ACTION + changement en question


    FIGHT = 6 # envoi les 2joueur dans l'ordre d'action
    
    WAIT_FIGHT_ACTION = 7 # att les action de l'autre joueur

    DO_FIGHT_ACTION = 8 # envoi l'action chois
    
    DEAD = 9 # envoi l'action chois
    
    SWITCH_PLAYER = 10
class Game():
    def __init__(self, nb_player:int, nb_IA:int) -> None:
        self.__nb_player:int = nb_player
        self.__players:list[joueur.Joueur] = [None for i in range(nb_IA + nb_player)]
        self.__plateau:Plateau = Plateau()
        self.__current_player:int = 0
        self.__state:Game_State = Game_State.SELECT_AVARTAR
        
    def get_players(self):
        """_summary_
            Getter de l'etat du joueur
        """
        return self.__players
    def get_state(self):
        """_summary_
            Getter de l'etat du joueur
        """
        return self.__state
    def set_state(self,state:Game_State):
        """_summary_
            Setter l'etat du joueur
        """
        self.__state = state
    
    def get_current_player(self)->int:
        return self.__current_player
    
    
    def get_plateau(self)->Plateau:
        return self.__plateau
    
    def next_player(self):
        self.__current_player = self.__current_player+1 if self.__current_player < len(self.__players()-2) else 0
    
    def player_selectable(self):
        elems = [joueur.Element.GRASS, joueur.Element.WATER, joueur.Element.TOWN, joueur.Element.ROCK]
        for player in self.__players:
            if isinstance(player, joueur.Joueur):
                elems.remove(player.get_element)
        return elems
    
    def loop(self, intput:inputs):
        if self.__players[self.__current_player] == None:
            self.__state = Game_State.SELECT_AVARTAR
        
        
        match self.__state:
            case Game_State.SELECT_AVARTAR:
                pass
            case Game_State.SELECT_ACTION:
                pass
            case Game_State.USE_DIE:
                pass
            case Game_State.MOVE_PLAYER:
                pass
            case Game_State.STAY_ON_CASE:
                pass
            case Game_State.FIGHT:
                pass
            case Game_State.WAIT_FIGHT_ACTION:
                pass
            case Game_State.DO_FIGHT_ACTION:
                pass
            case Game_State.DEAD:
                pass
            case Game_State.SWITCH_PLAYER:
                pass
