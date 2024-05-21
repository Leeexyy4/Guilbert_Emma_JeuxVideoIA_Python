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
        self.__TURQUOISE = (175, 238, 238)
        self.__INDIGO = (60, 0, 225)
        self.__ORANGE = (255, 127, 0)
        self.__BLEU = (0, 204, 204)
        self.__BEIGE = (255, 255, 204)

    def get_Noir(self):
        """Getter de la couleur Noir."""
        return self.__NOIR

    def get_Blanc(self):
        """Getter de la couleur Blanche."""
        return self.__BLANC

    def get_Bleu(self):
        """Getter de la couleur Bleu."""
        return self.__BLEU

    def get_Jaune(self):
        """Getter de la couleur Jaune."""
        return self.__JAUNE

    def get_Orange(self):
        """Getter de la couleur Orange."""
        return self.__ORANGE

    def get_Gris(self):
        """Getter de la couleur Gris."""
        return self.__GRIS

    def get_Beige(self):
        """Getter de la couleur Beige."""
        return self.__BEIGE

    def get_Violet(self):
        """Getter de la couleur Violet."""
        return self.__VIOLET

    def get_Rose(self):
        """Getter de la couleur Rose."""
        return self.__ROSE

    def get_Rouge(self):
        """Getter de la couleur Rouge."""
        return self.__ROUGE

    def get_Turquoise(self):
        """Getter de la couleur Turquoise."""
        return self.__TURQUOISE

    def get_Indigo(self):
        """Getter de la couleur Indigo."""
        return self.__INDIGO

    def get_Vert(self):
        """Getter de la couleur Verte."""
        return self.__VERT

    # Les setters etant inutiles, je ne les ai pas definis.

# Tests des fonctions
"""
if __name__ == "__main__":
    nouvelle_couleur = Couleur()

    # Exemples d'utilisation
    noir = nouvelle_couleur.get_Noir()
    blanc = nouvelle_couleur.get_Blanc()
    bleu = nouvelle_couleur.get_Bleu()

    print("Exemples d'utilisation:")
    print(f"Couleur Noir: {noir}")
    print(f"Couleur Blanc: {blanc}")
    print(f"Couleur Bleu: {bleu}")
"""