class Operation:
    # Constructeur de la classe
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    # Méthode pour additionner nombre1 et nombre2
    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print(f"Le résultat de l'addition est : {resultat}")

# Instanciation de la classe
operation_instance = Operation(5, 10)

# Appel de la méthode addition
operation_instance.addition()

"""
Méthode addition : La méthode addition additionne les valeurs des attributs nombre1 et nombre2.
Le résultat est stocké dans une variable resultat.
Le résultat est ensuite affiché en console à l'aide de print.
Appel de la méthode : Après avoir instancié la classe, on appelle la méthode addition en utilisant
operation_instance.addition().
"""