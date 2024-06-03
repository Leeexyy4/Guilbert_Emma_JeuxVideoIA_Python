from classe.personnage import joueur

class IntelA (joueur.Joueur):
    def __init__(self, id, prenom, element, plateaux, plateauy, pv, attaque, inventaire) -> None:
        super().__init__(id, prenom, element, plateaux, plateauy, pv, attaque, inventaire)
    
    