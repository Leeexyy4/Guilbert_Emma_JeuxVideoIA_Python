from enum import Enum
import pickle
import socket
from game import Game, GameState
from input import inputs
from joueur import Joueur
class ServerState(Enum):
    """La classe ServerState définit les états du serveur"""

    INIT = 1 # création d'une instance de serveur

    WAIT_CONNECION = 2 # attente que le MAX_PLAYER soit atteint
    
    IN_GAME = 3 # boucle de jeu principal

    ENDING = 4 # fin du serveur envoie des données à la bd pour les stats
    
host = '192.168.1.159'
firstport = 12345
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
players = []

state = ServerState.INIT
sock.bind((host, firstport))

isOn = True

while isOn:
    match state:
        case ServerState.INIT :
            game = Game(2,0, False)
            game.autoInitPlayer()
            state = ServerState.WAIT_CONNECION
        case ServerState.WAIT_CONNECION:
            data, addr = sock.recvfrom(20480)
            if addr not in players:
                players.append(addr)
            if len(players) == game.getNombreJoueur():
                state = ServerState.IN_GAME
                for player in players:
                    sock.sendto(pickle.dumps(game), player)
        case ServerState.IN_GAME:
            id = game.getIdJoueurActuel()
            message = {}
            message['id'] = id
            message['input'] = game.getEtat()
            sock.sendto(pickle.dumps(message), players[id])
            
            data, addr = sock.recvfrom(20480)
            input = pickle.loads(data)
            if (type(input) == inputs):
                game.loop(input)
                for player in players:
                    sock.sendto(pickle.dumps(game), player)
            if (game.isEnd()):
                for i in range(len(game.getListeJoueur())):
                    if game.getListeJoueur()[i].aGagne(game.getPlateau().getPlateau()):
                        sock.sendto(pickle.dumps({'end': True}), players[i])
                    else:
                        sock.sendto(pickle.dumps({'end': False}), players[i])
        case ServerState.ENDING:
            # Envoi donné à la bd
            for player in players:
                sock.sendto(pickle.dumps(game), player) 
            isOn = False
sock.close()