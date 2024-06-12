
from game import Game
class Interface():
    def __init__(self, estEnLigne:bool) -> None:
        self.__estEnLigne = estEnLigne
        self.__nb_joueur = 4
        self.__nb_IA = 0
        print("interface online? "+ str(self.estEnLigne()))
        
    def selectionnableNombreIA(self)->list[int]:
        res = [0]
        if(self.__nb_joueur < 4): res.append(1)
        if(self.__nb_joueur < 3): res.append(2)
        if(self.__nb_joueur < 2): res.append(3)
        return res
        
    def estEnLigne(self)->bool:
        """Booleen qui définit si le mode de partie est en mode multijoueur ou non"""
        return self.__estEnLigne
    
    def getNombreIA(self)->int:
        """Renvoie le nombre d'IA"""
        return self.__nb_IA
    
    def setNombreIA(self, nb_ia:int):
        """Modifie le nombre d'IA"""
        self.__nb_IA = nb_ia
        print(str(nb_ia) +" IAs")

    def getNombreJoueur(self)->int:
        """Renvoie le nombre de joueur(s)"""
        return self.__nb_joueur
    
    def setNombreJoueur(self, nb_joueur:int):
        """Modifie le nombre de joueur(s)"""
        self.__nb_joueur = nb_joueur
        print(str(nb_joueur) +" players")
    
    def genererPartie(self)->Game:
        """Fonction qui crée la partie"""
        return Game(self.__nb_joueur, self.__nb_IA)