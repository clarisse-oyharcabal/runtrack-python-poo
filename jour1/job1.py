class Operation:
    # Constructeur de la classe
    def __init__(self, nombre1=12, nombre2=3):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

# Instanciation de la classe avec les valeurs par défaut
operation_instance = Operation()

# Impression de l'objet en console
print(operation_instance)

"""
Constructeur (__init__) : Le constructeur est une méthode spéciale appelée lors de la création d'une instance de la classe.
Il initialise les attributs nombre1 et nombre2 avec des valeurs par défaut (0 dans ce cas).

Instanciation : Nous créons une instance de la classe Operation sans passer d'arguments, ce qui signifie que les valeurs par défaut
seront utilisées.

Impression : Lorsque nous imprimons l'objet, la méthode __str__ est appelée automatiquement, affichant les valeurs de nombre1 et nombre2.

"""