class Point:
    # Constructeur de la classe
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Méthode pour afficher les coordonnées du point
    def afficherLesPoints(self):
        print(f"Coordonnees du point : ({self.x}, {self.y})")

    # Méthode pour afficher la coordonnée x
    def afficherX(self):
        print(f"La coordonnee x est : {self.x}")

    # Méthode pour afficher la coordonnée y
    def afficherY(self):
        print(f"La coordonnee y est : {self.y}")

    # Méthode pour changer la valeur de x
    def changerX(self, nouvelle_valeur_x):
        self.x = nouvelle_valeur_x
        print(f"La coordonnee x a ete mise a jour a : {self.x}")

    # Méthode pour changer la valeur de y
    def changerY(self, nouvelle_valeur_y):
        self.y = nouvelle_valeur_y
        print(f"La coordonnee y a ete mise à jour a : {self.y}")

# Exemple d'utilisation de la classe Point
point = Point(3, 5)

# Affichage des coordonnées
point.afficherLesPoints()

# Affichage de x et y séparément
point.afficherX()
point.afficherY()

# Changement des valeurs de x et y
point.changerX(10)
point.changerY(15)

# Affichage des nouvelles coordonnées
point.afficherLesPoints()

"""
Constructeur (__init__) : Le constructeur prend deux paramètres, x et y, et les utilise
pour initialiser les attributs de l'objet.

Méthode afficherLesPoints : Affiche les coordonnées du point sous la forme (x, y).

Méthodes afficherX et afficherY : Affichent respectivement les valeurs de x et y.

Méthodes changerX et changerY : Permettent de modifier les valeurs de x et y respectivement.

Exemple d'utilisation :
On crée une instance de Point avec les coordonnées initiales (3, 5).
On affiche les coordonnées, puis on change les valeurs de x et y et on affiche à nouveau les coordonnées.
"""