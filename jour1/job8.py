class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon

    def afficherInfos(self):
        print(f"Rayon : {self.rayon}")

    def circonference(self):
        return 2 * 3.14159 * self.rayon

    def aire(self):
        return 3.14159 * self.rayon ** 2

    def diametre(self):
        return 2 * self.rayon
    
# Exemple d'utilisation 

# Création des cercles
cercle1 = Cercle(4)
cercle2 = Cercle(7)

# Affichage des informations et calculs pour le cercle 1
print("Cercle 1 :")
cercle1.afficherInfos()
print(f"Circonference : {cercle1.circonference()}")
print(f"Diametre : {cercle1.diametre()}")
print(f"Aire : {cercle1.aire()}")

# Affichage des informations et calculs pour le cercle 2
print("\nCercle 2 :")
cercle2.afficherInfos()
print(f"Circonference : {cercle2.circonference()}")
print(f"Diametre : {cercle2.diametre()}")
print(f"Aire : {cercle2.aire()}")


"""
Constructeur (__init__) : Le constructeur initialise l'attribut rayon avec la valeur fournie
lors de la création du cercle.
   - self.rayon = rayon  # Le rayon du cercle est défini.

Méthode changerRayon : Permet de modifier la valeur du rayon du cercle.
   - self.rayon = nouveau_rayon  # Le rayon est mis à jour avec la nouvelle valeur.

Méthode afficherInfos : Affiche les informations du cercle, notamment son rayon.
   - print(f"Rayon du cercle : {self.rayon}")

Méthode circonference : Calcule et retourne la circonférence du cercle.
   - return 2 * 3.14159 * self.rayon  # La circonférence est calculée et retournée.

Méthode aire : Calcule et retourne l'aire du cercle.
   - return 3.14159 * self.rayon ** 2  # L'aire est calculée et retournée.

Méthode diametre : Calcule et retourne le diamètre du cercle.
   - return 2 * self.rayon  # Le diamètre est calculé et retourné.

Instanciation et utilisation :
   - cercle1 = Cercle(4)  # On crée un cercle avec un rayon de 4.
   - cercle2 = Cercle(7)  # On crée un autre cercle avec un rayon de 7.

   - cercle1.afficherInfos()  # Affiche "Rayon du cercle : 4"
   - print(f"Circonférence du cercle 1 : {cercle1.circonference()}")  # Affiche la circonférence du cercle 1.
   - print(f"Aire du cercle 1 : {cercle1.aire()}")  # Affiche l'aire du cercle 1.
   - print(f"Diamètre du cercle 1 : {cercle1.diametre()}")  # Affiche le diamètre du cercle 1.

   - cercle2.afficherInfos()  # Affiche "Rayon du cercle : 7"
   - print(f"Circonférence du cercle 2 : {cercle2.circonference()}")  # Affiche la circonférence du cercle 2.
   - print(f"Aire du cercle 2 : {cercle2.aire()}")  # Affiche l'aire du cercle 2.
   - print(f"Diamètre du cercle 2 : {cercle2.diametre()}")  # Affiche le diamètre du cercle 2.

**self **: Dans les méthodes d'une classe, self est une référence à l'instance de la classe elle-même.
 Il est utilisé pour accéder aux attributs et aux autres méthodes de cette instance.
**Attributs **: Les attributs sont des variables associées à un objet (ici, rayon).
Ils stockent les données de l'objet.
**Méthodes **: Les méthodes sont des fonctions associées à un objet. Elles définissent les actions que l'objet peut effectuer (ici, changerRayon, afficherInfos, circonference, aire, diametre).

"""