
from game import Game
class Interface():
    def __init__(self, is_online:bool) -> None:
        self.__is_online = is_online
        self.__nb_joueur = 4
        self.__nb_IA = 0
        print("interface online? "+ str(self.is_online()))
        
    def selectable_nb_ia(self)->list[int]:
        res = [0]
        if(self.__nb_joueur < 4): res.append(1)
        if(self.__nb_joueur < 3): res.append(2)
        if(self.__nb_joueur < 2): res.append(3)
        return res
        
    def is_online(self)->int:
        return self.__is_online
    def get_nb_IA(self)->bool:
        return self.__nb_IA
    def set_nb_IA(self, nb_ia:int):
        self.__nb_IA = nb_ia
        print(str(nb_ia) +" IAs")
    def get_nb_joueur(self)->int:
        return self.__nb_joueur
    def set_nb_joueur(self, nb_joueur:int):
        self.__nb_joueur = nb_joueur
        print(str(nb_joueur) +" players")
    
    def generate_Game(self)->Game:
        return Game(self.__nb_joueur, self.__nb_IA)