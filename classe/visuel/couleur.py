class Couleur:
    """La classe Couleur est une classe qui permet de recuperer la couleur voulue grâce au getter."""
    
    def __init__(self) -> None:
        """Initialisation des couleurs."""
        self.__NOIR = (0, 0, 0)
        self.__BLANC = (255, 255, 255)
        self.__JAUNE = (255, 255, 0)
        self.__VERT = (0, 255, 0)
        self.__VIOLET = (238, 130, 238)
        self.__ROUGE = (255, 24, 40)
        self.__GRIS = (192, 192, 192)
        self.__ROSE = (255, 192, 203)
        self.__INDIGO = (60, 0, 225)
        self.__ORANGE = (255, 127, 0)
        self.__BLEU = (0, 204, 204)
        self.__BEIGE = (255, 255, 204)

    def getNoir(self):
        """Getter de la couleur Noir."""
        return self.__NOIR

    def getBlanc(self):
        """Getter de la couleur Blanche."""
        return self.__BLANC

    def getBleu(self):
        """Getter de la couleur Bleu."""
        return self.__BLEU

    def getJaune(self):
        """Getter de la couleur Jaune."""
        return self.__JAUNE

    def getOrange(self):
        """Getter de la couleur Orange."""
        return self.__ORANGE

    def getGris(self):
        """Getter de la couleur Gris."""
        return self.__GRIS

    def getBeige(self):
        """Getter de la couleur Beige."""
        return self.__BEIGE

    def getViolet(self):
        """Getter de la couleur Violet."""
        return self.__VIOLET

    def getRose(self):
        """Getter de la couleur Rose."""
        return self.__ROSE

    def getRouge(self):
        """Getter de la couleur Rouge."""
        return self.__ROUGE
    
    def getIndigo(self):
        """Getter de la couleur Indigo."""
        return self.__INDIGO

    def getVert(self):
        """Getter de la couleur Verte."""
        return self.__VERT

    # Les setters etant inutiles, je ne les ai pas definis.

# Tests des fonctions
"""
if __name__ == "__main__":
    nouvelle_couleur = Couleur()

    # Exemples d'utilisation
    noir = nouvelle_couleur.getNoir()
    blanc = nouvelle_couleur.getBlanc()
    bleu = nouvelle_couleur.get_Bleu()

"""