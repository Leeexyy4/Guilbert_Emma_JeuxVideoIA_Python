#  Donné in GAME envoyé:
# State:Player_State:PlayerId:Data
import socket, pickle
from classe.personnage import joueur
from classe.jeu import logique

class Server:
    id = 0;
    def __init__(self, sock:socket.socket) -> None:
        self.__id = id;
        id +=1
        self.__sock = sock
        self.__players:dict[str, joueur.Joueur] = {}
        self.__maxPlayers:int = 4
        self.__currentPlayer:int  = 0
        self.__state:logique.State = logique.State.INIT
        
    
    def get_id(self)->int:
        """Getter de la id."""
        return self.__id
    
    def get_sock(self)->int:
        """Getter de la sock."""
        return self.__sock

    def get_players(self)->dict[str, joueur.Joueur]:
        """Getter de la players."""
        return self.__players
    def addPlayer(self, playersData:tuple[str, joueur.Joueur]):
        """Getter de la players."""
        if self.__maxPlayers == len(self.__players.keys()) | playersData[0] in self.__players.keys() : return False
        self.__players[playersData[0]] = playersData[1]
        return True

    def set_players(self, players:dict[str, joueur.Joueur]):
        """Setter de la players."""
        self.__players = players
        
    def get_maxPlayers(self)->int:
        """Getter de la maxPlayers."""
        return self.__maxPlayers

    def set_maxPlayers(self, maxPlayers:int):
        """Setter de la maxPlayers."""
        self.__maxPlayers = maxPlayers
        
    def get_currentPlayer(self)->int:
        """Getter de la currentPlayer."""
        return self.__currentPlayer

    def set_currentPlayer(self, currentPlayer:int):
        """Setter de la currentPlayer."""
        self.__currentPlayer = currentPlayer
        
    def get_state(self) -> logique.State:
        """Getter de la state."""
        return self.__state

    def set_state(self, state:logique.State):
        """Setter de la state."""
        self.__state = state
    
    def WaitingPlayer(self):
        data, addr = self.sock.recvfrom(2048)
        j = joueur.Joueur(queu,joueur.Nom(queu).value , joueur.Element(queu).value, 0,0,0,0,[]) 
        self.addPlayer(addr, j)
        queu = len(self.__players.keys());
        data = pickle.loads(data)
        
