class Livre():
    def __init__(self, titre, auteur, nombre_pages):
        self._titre = titre
        self._auteur = auteur
        self._nombre_pages = nombre_pages

    # Accesseurs
    def getTitre(self):
        return self._titre

    def getAuteur(self):
        return self._auteur

    def getNombrePages(self): 
        return self._nombre_pages

    # Mutateurs 
    def setTitre(self, titre):
        self._titre = titre

    def setAuteur(self, auteur):
        self._auteur = auteur

    def setNombrePages(self, nombre_pages):  
        if isinstance(nombre_pages, int) and nombre_pages > 0:
            self._nombre_pages = nombre_pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")

    def afficher(self):
        return f"Titre : {self._titre}, Auteur : {self._auteur}, Nombre de pages : {self._nombre_pages}"


# Exemple d'utilisation 

# Création d'un livre
livre = Livre("Entre deux mondes", "Norek", 413)

# Affichage des informations initiales
print("Informations initiales :")
print(livre.afficher())

# Modification des attributs
livre.setTitre("La verite sur l'affaire Harry Quebert")
livre.setAuteur("Dicker")
livre.setNombrePages(854)

# Affichage des informations après modification
print("\nInformations après modification :")
print(livre.afficher())

# Tentative de modification du nombre de pages avec une valeur invalide
livre.setNombrePages(-10)  # Affiche le message d'erreur
livre.setNombrePages("abc")  # Affiche le message d'erreur

# Affichage des informations (le nombre de pages n'a pas été modifié)
print("\nInformations après tentative de modification invalide du nombre de pages :")
print(livre.afficher())

# Vérification des modifications
print("\nVérification des modifications :")
print(f"Titre : {livre.getTitre()}")
print(f"Auteur : {livre.getAuteur()}")
print(f"Nombre de pages : {livre.getNombrePages()}")  # Nom corrigé : getNombrePages


"""
Attributs privés : Les attributs _titre, _auteur et _nombre_pages sont précédés d'un underscore (_).
En Python, cela indique une convention pour signifier que ces attributs sont destinés à être utilisés
en interne dans la classe. Bien qu'ils ne soient pas strictement privés (on peut toujours y accéder de
l'extérieur avec livre._titre), il est fortement recommandé de respecter cette convention et d'utiliser
les accesseurs et mutateurs pour interagir avec ces attributs.

Constructeur (__init__) : Le constructeur initialise les attributs avec les valeurs fournies lors de la
création du livre.

Accesseurs : Les méthodes getTitre(), getAuteur() et getNombrePages() permettent d'accéder aux valeurs
des attributs.

Mutateurs : Les méthodes setTitre(), setAuteur() et setNombrePages() permettent de modifier les valeurs
des attributs.

La méthode setNombrePages() vérifie si la valeur fournie est un entier positif avant de modifier l'attribut.
Si la valeur est invalide, un message d'erreur est affiché et l'attribut n'est pas modifié.

Méthode afficher : Cette méthode permet d'afficher les informations du livre dans un format lisible.

"""