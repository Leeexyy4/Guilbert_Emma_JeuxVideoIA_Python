from enum import Enum
import pickle
import socket
from game import Game
from input import inputs
from joueur import Joueur
class ServerState(Enum):
    """La classe ServerState définit les états du serveur"""

    INIT = 1 # création d'une instance de serveur

    WAIT_CONNECION = 2 # attente que le MAX_PLAYER soit atteint
    
    IN_GAME = 3 # boucle de jeu principal

    ENDING = 4 # fin du serveur envoie des données à la bd pour les stats
    
host = '192.168.1.15'
firstport = 12345
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
players = []

state = ServerState.INIT
sock.bind((host, firstport))

isOn = True

while isOn:
    match state:
        case ServerState.INIT :
            game = Game(4,0)
            game.auto_init_player()
            state = ServerState.INIT
        case ServerState.WAIT_CONNECION:
            data, addr = sock.recvfrom(2048)
            if addr not in players:
                players.append(addr)
            if len(players) == 4:
                state = ServerState.IN_GAME
                message['id'] = id
                message['wait'] = 'waitingRoom'
        case ServerState.IN_GAME:
            id = game.getIDJoueurActuel()
            message = {}
            message['id'] = id
            message['input'] = game.getEtat()
            sock.sendto(pickle.dumps(message), players[id])
            
            data, addr = sock.recvfrom(2048)
            input = pickle.loads(data)
            if (type(input) == inputs):
                game.loop(input)
                for player in players:
                    sock.sendto(pickle.dumps(game), player) 
        case ServerState.ENDING:
            # Envoi donné à la bd
            for player in players:
                sock.sendto(pickle.dumps(game), player) 
            isOn = False
sock.close()