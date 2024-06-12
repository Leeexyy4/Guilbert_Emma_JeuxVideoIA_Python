from plateau import Plateau
import random
import joueur
from input import inputs, direction
from enum import Enum
class Game_State(Enum):
    """la classe Game_State regroupe les états de la partie selon les actions du joueur"""
    WAIT_PLAYER = 0 # attente d'action d'un joueur (idJOueur + Game_State action)
    
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
    def __init__(self, nb_player:int, nb_IA:int) -> None:
        self.__nb_player:int = nb_player
        self.__players:list[joueur.Joueur] = [None for i in range(nb_IA + nb_player)]
        self.__plateau:Plateau = Plateau()
        self.__current_player:int = 0
        self.__die_value:int = 0
        self.__state:Game_State = Game_State.SELECT_AVATAR
        
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
    
    def get_current_player(self)->joueur.Joueur:
        """_summary_
            Getter de l'etat du joueur
        """
        return self.__players[self.__current_player]
    def set_state(self,state:Game_State):
        """_summary_
            Setter l'etat du joueur
        """
        self.__state = state
    
    
    def get_plateau(self)->Plateau:
        """Renvoie l'état du plateau"""
        return self.__plateau
    
    def next_player(self):
        """Fonction qui décide quel est le joueur qui joue au prochain tour"""
        self.__current_player = self.__current_player+1 if self.__current_player < len(self.__players)-2 else 0
    
    def player_selectable(self):
        """Renvoie la liste des personnages sélectionnables"""
        elems = [joueur.Element.GRASS, joueur.Element.WATER, joueur.Element.TOWN, joueur.Element.ROCK]
        for player in self.__players:
            if isinstance(player, joueur.Joueur):
                elems.remove(player.get_element)
        return elems
    
    def loop(self, input:inputs):
        if self.__players[self.__current_player] == None:
            self.__state = Game_State.SELECT_AVATAR
        
        player:joueur.Joueur = self.__players[self.__current_player]
        match self.__state:
            case Game_State.SELECT_AVATAR:
                if input.is_clicked(): 
                    start:tuple[int, int] = self.__plateau.get_case_jaune()
                    if (500 <= input.get_cursor_x() <= 600 and 582 <= input.get_cursor_y() <= 652 and not joueur.Joueur.water_is_used):
                        self.__players[self.__current_player] = joueur.Joueur(self.__current_player, start[0], start[1], joueur.Element.WATER)
                        self.__state = Game_State.USE_DIE
                        # Si le personnage sur lequel on clique est Flora
                    elif (700 <= input.get_cursor_x() <= 800 and 582 <= input.get_cursor_y() <= 652 and not joueur.Joueur.grass_is_used): 
                        self.__players[self.__current_player] = joueur.Joueur(self.__current_player, start[0], start[1], joueur.Element.GRASS)
                        self.__state = Game_State.USE_DIE
                    # Si le personnage sur lequel on clique est Pierre
                    elif (400 <= input.get_cursor_x() <= 500 and 582 <= input.get_cursor_y() <= 652 and not joueur.Joueur.rock_is_used): 
                        self.__players[self.__current_player] = joueur.Joueur(self.__current_player, start[0], start[1], joueur.Element.ROCK)
                        self.__state = Game_State.USE_DIE
                    # Si le personnage sur lequel on clique est Kevin
                    elif (600 <= input.get_cursor_x() <= 700 and 582 <= input.get_cursor_y() <= 652 and not joueur.Joueur.town_is_used):
                        self.__players[self.__current_player] = joueur.Joueur(self.__current_player, start[0], start[1], joueur.Element.TOWN)
                        self.__state = Game_State.USE_DIE

            case Game_State.SELECT_ACTION:
                if input.is_clicked(): 
                    if 220 <= input.get_cursor_x() <= 284 and 480 <= input.get_cursor_y() <= 544: self.__state = Game_State.DO_FIGHT_ACTION
                    if 510 <= input.get_cursor_x() <= 574 and 480 <= input.get_cursor_y() <= 544: self.__state = Game_State.USE_DIE
            
            case Game_State.USE_DIE:
                if input.is_clicked(): 
                    if 350 <= input.get_cursor_x() <= 435 and 475 <= input.get_cursor_y() <= 560:
                        self.__die_value = random.randint(1,6)
                        print(self.__die_value)
                        self.__state = Game_State.MOVE_PLAYER
                        
            case Game_State.MOVE_PLAYER:
                if(self.__die_value == 0):
                    self.__state = Game_State.STAY_ON_CASE
                    return
                match input.get_direction():
                    case direction.NORTH :
                        player.set_plateauy(player.get_plateauy()-1)
                        self.__die_value -=1
                        print(self.__die_value)
                    case direction.EAST :
                        player.set_plateauy(player.get_plateauy()+1)
                        self.__die_value -=1
                        print(self.__die_value)
                    case direction.SOUTH :
                        player.set_plateaux(player.get_plateaux()+1)
                        self.__die_value -=1
                        print(self.__die_value)
                    case direction.WEST :
                        player.set_plateaux(player.get_plateaux()-1)
                        self.__die_value -=1
                        print(self.__die_value)
                
            case Game_State.STAY_ON_CASE:
                # Rajouté les effets de la case
                self.next_player()
                self.__state = Game_State.SELECT_ACTION
                
            case Game_State.FIGHT:
                pass
            case Game_State.WAIT_FIGHT_ACTION:
                pass
            case Game_State.DO_FIGHT_ACTION:
                self.__state = Game_State.USE_DIE
            case Game_State.DEAD:
                pass
            case Game_State.SWITCH_PLAYER:
                pass
