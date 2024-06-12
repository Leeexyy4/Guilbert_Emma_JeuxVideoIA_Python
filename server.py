from enum import Enum
class ServerState(Enum):
    """La classe ServerState définit les états du serveur"""

    INIT = 1 # création d'une instance de serveur

    WAIT_CONNECION = 2 # attente que le MAX_PLAYER soit atteint
    
    IN_GAME = 3 # boucle de jeu principal

    ENDING = 4 # fin du serveur envoie des données à la bd pour les stats