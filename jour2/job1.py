class Rectangle (): 
    def __init__(self, longueur, largeur):
        self._longueur = longueur # Attribut privé: _longueur
        self._largeur = largeur # Attribut privé: _largeur

    # Accesseurs 
    def getLongueur(self):
        return self._longueur

    def getLargeur(self):
        return self._largeur

    # Mutateurs 
    def setLongueur(self, longueur):
        self._longueur = longueur

    def setLargeur(self, largeur):
        self._largeur = largeur

    def afficher(self):
        return f"Longueur : {self._longueur}, Largeur : {self._largeur}"

# Exemple d'utilisation
 
# Création d'un rectangle
rectangle = Rectangle(10, 5)

# Affichage des dimensions initiales
print("Dimensions initiales :")
print(rectangle.afficher())

# Modification des dimensions
rectangle.setLongueur(15)
rectangle.setLargeur(8)

# Affichage des dimensions après modification
print("\nDimensions après modification :")
print(rectangle.afficher())

# Vérification des modifications
print("\nVérification des modifications :")
print(f"Longueur : {rectangle.getLongueur()}")
print(f"Largeur : {rectangle.getLargeur()}")

"""
Attributs privés : Les attributs _longueur et _largeur sont précédés d'un underscore (_). En Python, cela indique une convention
pour signifier que ces attributs sont destinés à être utilisés en interne dans la classe. Bien qu'ils ne soient pas strictement privés
(on peut toujours y accéder de l'extérieur avec rectangle._longueur), il est fortement recommandé de respecter cette convention et 
d'utiliser les accesseurs et mutateurs pour interagir avec ces attributs.

Constructeur (__init__) : Le constructeur initialise les attributs _longueur et _largeur avec les valeurs fournies lors de la création
du rectangle.

Accesseurs (getters) : Les méthodes getLongueur() et getLargeur() permettent d'accéder aux valeurs des attributs _longueur et _largeur
respectivement.

Mutateurs (setters) : Les méthodes setLongueur() et setLargeur() permettent de modifier les valeurs des attributs _longueur et _largeur
respectivement.

Méthode afficher : Cette méthode permet d'afficher les dimensions du rectangle dans un format lisible.

"""