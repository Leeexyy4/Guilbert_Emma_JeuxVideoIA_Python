from plateau import Plateau
class Game():
    def __init__(self, nb_player:int, nb_IA:int) -> None:
        self.__nb_player:int = nb_player
        self.__players:list = [None for i in range(nb_IA + nb_player)]
        self.__plateau:Plateau = Plateau()
        self.__current_player:int = 0
    
    def get_plateau(self)->Plateau:
        return self.__plateau
    
    def next_player(self):
        self.__current_player = self.__current_player+1 if self.__current_player < len(self.__players()-2) else 0
    
    def loop(self):
        if self.__players[self.__current_player] == None:
            pass
            # chose player