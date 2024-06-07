from enum import Enum
class Server_State(Enum):

    INIT = 1 # creation d'une instance de serveur

    WAIT_CONNECION = 2 # attente que le MAX_PLAYER sois atteint
    
    IN_GAME = 3 # boucle de jeu principal

    ENDING = 4 # fin du serveur envoi des donné à la bd pour les stat