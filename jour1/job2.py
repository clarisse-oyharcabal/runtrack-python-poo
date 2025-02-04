class Operation:
    # Constructeur de la classe
    def __init__(self, nombre1=12, nombre2=3):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

# Instanciation de la classe avec les valeurs par défaut
operation_instance = Operation()

# Accès aux attributs et impression en console
print(f"Le nombre1 est {operation_instance.nombre1}")
print(f"Le nombre2 est {operation_instance.nombre2}")

"""
Accès aux attributs :
operation_instance.nombre1 permet d'accéder à la valeur de l'attribut nombre1.
operation_instance.nombre2 permet d'accéder à la valeur de l'attribut nombre2.

Impression : 
Les valeurs des attributs sont imprimées en console à l'aide de la fonction print.

"""