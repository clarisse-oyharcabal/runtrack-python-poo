class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self._nom = nom
        self._prenom = prenom
        self._numero_etudiant = numero_etudiant
        self._credits = 0
        self._level = self._student_eval()  # Niveau initialisé lors de la création

    def add_credits(self, nombre_credits):
        if nombre_credits > 0:
            self._credits += nombre_credits
            self._level = self._student_eval()  # Mettre à jour le niveau
        else:
            print("Le nombre de crédits doit être supérieur à zéro.")

    def _student_eval(self):  # Méthode privée
        if self._credits >= 90:
            return "Excellent"
        elif self._credits >= 80:
            return "Très bien"
        elif self._credits >= 70:
            return "Bien"
        elif self._credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def student_info(self):
        print(f"Nom = {self._nom}")
        print(f"Prénom = {self._prenom}")
        print(f"id = {self._numero_etudiant}")
        print(f"Niveau = {self._level}")

# Instanciation de l'étudiant John Doe
john_doe = Student("Doe", "John", 145)

# Ajout de crédits
john_doe.add_credits(30)
john_doe.add_credits(20)
john_doe.add_credits(20)

# Affichage du total de crédits
print(f"Le nombre de crédits de John Doe est de {john_doe._credits} points")

# Affichage des informations de l'étudiant
john_doe.student_info()


"""
Attributs privés : Les attributs _nom, _prenom, _numero_etudiant, _credits et _level sont précédés d'un underscore _ pour indiquer 
qu'ils sont privés.

Méthode add_credits : Cette méthode permet d'ajouter des crédits à l'étudiant. Elle vérifie si le nombre de crédits à ajouter est
positif avant de les ajouter.

Méthode privée _student_eval : Cette méthode évalue le niveau de l'étudiant en fonction de son nombre de crédits. Elle est privée 
car elle ne doit pas être accessible depuis l'extérieur de la classe.

Méthode student_info : Cette méthode affiche les informations de l'étudiant, y compris son niveau, en utilisant les attributs privés.
Instanciation et utilisation : Un objet john_doe de la classe Student est créé. Des crédits lui sont ajoutés à trois reprises, puis son
total de crédits et ses informations sont affichés.

"""