class Animal:
    # Constructeur de la classe
    def __init__(self):
        self.age = 0  # Initialisation de l'âge à 0
        self.prenom = ""  # Initialisation du prénom à une chaîne vide

    # Méthode pour afficher l'âge de l'animal
    def afficherAge(self):
        print(f"L'age de l'animal {self.age} ans")

    # Méthode pour faire vieillir l'animal
    def vieillir(self):
        self.age += 1
        print(f"L'animal a vieilli. Nouvel age : {self.age} ans")

    # Méthode pour nommer l'animal
    def nommer(self, nom):
        self.prenom = nom
        print(f"L'animal se nomme {self.prenom}")

# Instanciation d'un objet Animal
mon_animal = Animal()

# Affichage de l'âge initial
mon_animal.afficherAge()

# Faire vieillir l'animal
mon_animal.vieillir()

# Affichage de l'âge mis à jour
mon_animal.afficherAge()

# Nommer l'animal
mon_animal.nommer("Luna")

# Affichage du nom de l'animal
print(f"L'animal se nomme {mon_animal.prenom}")

"""
Constructeur (__init__) : Le constructeur initialise les attributs age à 0 et prenom à une chaîne vide.

Méthode afficherAge : Affiche l'âge actuel de l'animal.

Méthode vieillir : Incrémente l'âge de l'animal de 1 et affiche le nouvel âge.

Méthode nommer : Prend un paramètre nom et l'assigne à l'attribut prenom, puis affiche le nom de l'animal.

Instanciation et utilisation : 

On crée une instance de Animal.

On affiche l'âge initial.

On fait vieillir l'animal et on affiche l'âge mis à jour.

On nomme l'animal et on affiche son nom.

"""