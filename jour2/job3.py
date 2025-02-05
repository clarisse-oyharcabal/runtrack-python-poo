class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        self._titre = titre
        self._auteur = auteur
        self._nombre_pages = 0
        self.set_nombre_pages(nombre_pages)  # Utilisation du mutateur pour la validation
        self._disponible = True

    # Accesseurs 
    def get_titre(self):
        return self._titre

    def get_auteur(self):
        return self._auteur

    def get_nombre_pages(self):
        return self._nombre_pages

    def est_disponible(self):
        return self._disponible

    # Mutateurs 
    def set_titre(self, nouveau_titre):
        self._titre = nouveau_titre

    def set_auteur(self, nouvel_auteur):
        self._auteur = nouvel_auteur

    def set_nombre_pages(self, nouveau_nombre_pages):
        if isinstance(nouveau_nombre_pages, int) and nouveau_nombre_pages > 0:
            self._nombre_pages = nouveau_nombre_pages
        else:
            print("Erreur : Le nombre de pages doit etre un entier positif.")

    def set_disponibilite(self, disponibilite):
        self._disponible = disponibilite

    def verification(self):
        return self.est_disponible()

    def emprunter(self):
        if self.verification():
            self.set_disponibilite(False)
            print(f"Le livre '{self.get_titre()}' a ete emprunte.")
        else:
            print(f"Le livre '{self.get_titre()}' n'est pas disponible.")

    def rendre(self):
        if not self.verification():
            self.set_disponibilite(True)
            print(f"Le livre '{self.get_titre()}' a ete rendu.")
        else:
            print(f"Le livre '{self.get_titre()}' n'avait pas ete emprunte.")

# Exemple d'utilisation
mon_livre = Livre("Entre deux mondes", "Norek", 413)

print(mon_livre.get_titre())  # Affiche "Entre deux mondes"

mon_livre.emprunter()
print(mon_livre.est_disponible())  # Affiche False

mon_livre.rendre()
print(mon_livre.est_disponible())  # Affiche True


"""
Attribut _disponible : Un nouvel attribut privé _disponible a été ajouté et initialisé à True
dans le constructeur.

Méthode verification() : Cette méthode retourne simplement la valeur de l'attribut _disponible.

Méthode emprunter() : Elle utilise self.verification() pour vérifier si le livre est disponible 
avant de le rendre indisponible. Elle affiche un message indiquant si l'emprunt a réussi ou non.

Méthode rendre() : Elle vérifie d'abord si le livre a été emprunté en utilisant not self.verification().
Si c'est le cas, elle le rend disponible et affiche un message. Sinon, elle affiche un message indiquant
que le livre n'avait pas été emprunté.

"""