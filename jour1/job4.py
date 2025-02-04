class Personne:
    # Constructeur de la classe
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    # Méthode pour retourner le nom et le prénom
    def SePresenter(self):
        return f"Je suis {self.prenom} {self.nom}."

# Instanciation de plusieurs personnes
personne1 = Personne("Doe", "John")
personne2 = Personne("Dupond", "Jean")

# Appel de la méthode SePresenter pour chaque personne
print(personne1.SePresenter())
print(personne2.SePresenter())


"""
Constructeur (__init__) : Le constructeur prend deux paramètres, nom et prenom,
et les utilise pour initialiser les attributs de l'objet.

Méthode SePresenter : Cette méthode retourne une chaîne de caractères qui présente la personne en utilisant
les attributs nom et prenom.

Instanciation : Nous créons trois instances de la classe Personne avec des valeurs différentes pour nom et
prenom.

Appel de la méthode SePresenter : Nous appelons la méthode SePresenter pour chaque instance et imprimons
le résultat en console.

"""