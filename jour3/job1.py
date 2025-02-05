class Ville():
    def __init__(self, nom, nombrehabitants):
        self._nom = nom
        self._nombrehabitants = nombrehabitants

#Accesseur
    def getNom(self):
        return self._nom

    def getNombrehabitants(self):
        return self._nombrehabitants

#Mutateurs
    def setNom(self, nom):
        self._nom = nom

    def setNombre_habitants(self, nombrehabitants):
        self._nombrehabitants = nombrehabitants

    def afficher(self): 
        return f'Ville : {self._nom}, nombre habitants : {self._nombrehabitants}'


resultat1 = Ville("Marseille", 873000)

print(resultat1.afficher())

class Personne():  
    def __init__(self, nom, age, resultat1):
        self._nom = nom
        self._age = age
        self._resultat1 = resultat1

    def ajouterPopulation():
        



