class Ville:
    def __init__(self, nom, nb_habitants):
        self._nom = nom
        self._nb_habitants = nb_habitants

    def get_nb_habitants(self):
        return self._nb_habitants

    def ajouter_habitant(self):
        self._nb_habitants += 1

class Personne:
    def __init__(self, nom, age, ville):
        self._nom = nom
        self._age = age
        self._ville = ville

    def ajouterPopulation(self):
        self._ville.ajouter_habitant()

# Création des villes
paris = Ville("Paris", 2103000)
marseille = Ville("Marseille", 873076)

# Affichage du nombre d'habitants initial
print(f"Population de la ville de Paris: {paris.get_nb_habitants()} habitants")
print(f"Population de la ville de Marseille: {marseille.get_nb_habitants()} habitants")

# Création des personnes
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

# Ajout de population
john.ajouterPopulation()
myrtille.ajouterPopulation()
chloe.ajouterPopulation()

# Affichage du nombre d'habitants après l'arrivée des personnes
print(f"Mise a jour de la population de la ville de Paris {paris.get_nb_habitants()} habitants")
print(f"Mise a jour de la population de la ville de Marseille {marseille.get_nb_habitants()} habitants")


"""
Classe Ville :

Attributs privés : _nom et _nb_habitants.

Méthodes :
__init__: Constructeur pour initialiser une ville avec son nom et son nombre d'habitants.
get_nb_habitants: Retourne le nombre d'habitants de la ville.
ajouter_habitant: Incrémente le nombre d'habitants de la ville.

Classe Personne :

Attributs privés : _nom, _age et _ville (un objet de la classe Ville).

Méthodes :
__init__: Constructeur pour initialiser une personne avec son nom, son âge et la ville où elle habite.
ajouterPopulation: Appelle la méthode ajouter_habitant de l'objet Ville pour augmenter la population de la ville où habite la personne.

Création des objets :

Deux objets Ville (Paris et Marseille) sont créés avec leurs populations initiales.
Trois objets Personne (John, Myrtille et Chloé) sont créés, chacun habitant dans une des villes.

Ajout de population : Les méthodes ajouterPopulation de chaque objet Personne sont appelées pour ajouter une personne à la population
de sa ville.

Affichage des résultats : Le nombre d'habitants de Paris et de Marseille est affiché avant et après l'arrivée des nouvelles personnes.

"""