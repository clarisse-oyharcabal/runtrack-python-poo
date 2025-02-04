class Personnage:
    def __init__(self, x: int, y: int, largeur_plateau: int, hauteur_plateau: int):
        """Initialise le personnage avec sa position et les dimensions du plateau."""
        self.x = x
        self.y = y
        self.largeur_plateau = largeur_plateau
        self.hauteur_plateau = hauteur_plateau

    def gauche(self):
        """Déplace le personnage vers la gauche s'il ne sort pas du plateau."""
        if self.x > 0:
            self.x -= 1

    def droite(self):
        """Deplace le personnage vers la droite s'il ne sort pas du plateau."""
        if self.x < self.largeur_plateau - 1:
            self.x += 1

    def haut(self):
        """Deplace le personnage vers le haut s'il ne sort pas du plateau."""
        if self.y > 0:
            self.y -= 1

    def bas(self):
        """Deplace le personnage vers le bas s'il ne sort pas du plateau."""
        if self.y < self.hauteur_plateau - 1:
            self.y += 1

    def position(self):
        """Renvoie la position actuelle du personnage sous forme de tuple (x, y)."""
        return self.x, self.y


# Exemple d'utilisation :
plateau_largeur = 5
plateau_hauteur = 5
perso = Personnage(2, 2, plateau_largeur, plateau_hauteur)

perso.gauche()
print(perso.position())  # (1, 2)

perso.bas()
print(perso.position())  # (1, 3)

perso.droite()
print(perso.position())  # (2, 3)

perso.haut()
print(perso.position())  # (2, 2)

"""
Constructeur (__init__) : Initialise la position du personnage avec les coordonnées x et y. 
Définit également la largeur et la hauteur du plateau pour éviter que le personnage ne sorte des limites.

Méthode gauche : Déplace le personnage vers la gauche en décrémentant x, à condition qu'il ne soit pas
déjà sur le bord gauche du plateau.

Méthode droite : Déplace le personnage vers la droite en incrémentant x, sans dépasser la largeur du plateau.

Méthode haut : Déplace le personnage vers le haut en décrémentant y, tant qu'il ne dépasse pas la limite
supérieure du plateau.

Méthode bas : Déplace le personnage vers le bas en incrémentant y, sans dépasser la hauteur du plateau.

Méthode position : Retourne un tuple contenant la position actuelle (x, y) du personnage.

Instanciation et utilisation :

On crée une instance de la classe Personnage avec une position initiale et les dimensions du plateau.

On déplace le personnage vers la gauche et affiche sa nouvelle position.

On le déplace vers le bas et affiche la nouvelle position.

On le déplace vers la droite et affiche la nouvelle position.

On le déplace vers le haut et affiche la nouvelle position.

"""


