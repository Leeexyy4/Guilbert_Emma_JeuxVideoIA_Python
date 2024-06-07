from enum import Enum
class Server_State(Enum):

    INIT = 1 # creation d'une instance de serveur
    
    STARTING = 2 # création de la map, envoi des donné au joueur

    WAIT_CONNECION = 3 # attente que le MAX_PLAYER sois atteint
    
    IN_GAME = 4 # boucle de jeu principal

    ENDING = 5 # fin du serveur envoi des donné à la bd pour les stat
class Menu(Enum):

    INDEX = 1 # creation d'une instance de serveur
    
    LOCAL = 2 # création de la map, envoi des donné au joueur

    ONLINE = 3 # attente que le MAX_PLAYER sois atteint
    
    GLOBALS_STATS = 4 # boucle de jeu principal

    HELPER = 5 # fin du serveur envoi des donné à la bd pour les stat
    NB_PLAYER = 6
    NB_IA = 7
class Client_State(Enum):

    MENU = 1 # creation d'une instance de serveur
    
    CHOSE_CONNECTION = 2
    CHOSE_CONNECTION = 2
    
    STARTING = 2 # création de la map, envoi des donné au joueur

    WAIT_CONNECION = 3 # attente que le MAX_PLAYER sois atteint
    
    IN_GAME = 4 # boucle de jeu principal

    ENDING = 5 # fin du serveur envoi des donné à la bd pour les stat

class Player_State(Enum):

    SELECT_ACTION = 1 # si !0 = dée sinn fight
    
    USE_DIE = 2 # envoi NB MOVE
    
    MOVE_PLAYER = 3 # envoi nb déplacement restant + pos
    
    STAY_ON_CASE = 4 # envoi CASE_ACTION + changement en question

    WAIT_PLAYER = 2 # attente d'action d'un joueur (idJOueur + Player_State action)

    FIGHT = 3 # envoi les 2joueur dans l'ordre d'action
    
    WAIT_FIGHT_ACTION = 4 # att les action de l'autre joueur

    DO_FIGHT_ACTION = 5 # envoi l'action chois
    
    DEAD = 6 # envoi l'action chois
    
class CASE_ACTION(Enum):
    LUCK = 3 # click pour savoir le résultat
    UNLUCK = 4 # click pour savoir le résultat
    REPLAY = 5 # rejour à partir du lancé de dée
    SPECIAL = 6 # choisit de prendre le risque ou pas, SI choisit, att 2eme click
    RANDOM_TP = 1 # click pour être tp aléatoirement
    NOTHING = 0 # Se pas rien, pas de click
    DEATH = 0 # mort, pas de click
    WITCH = 0 # choix entre use clef si non rien, pour finir la partie
    WELL = 0 # Choisit quoi abandoné, Si n'as pas de clef, boucle sur lui meme
    BOSS = 7  # début du fight
    TP = 2 # click pour être tp

