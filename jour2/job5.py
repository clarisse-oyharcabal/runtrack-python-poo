class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self._marque = marque
        self._modele = modele
        self._annee = annee
        self._kilometrage = kilometrage
        self._en_marche = False
        self._reservoir = 50

    # Accesseurs 
    def get_marque(self):
        return self._marque

    def get_modele(self):
        return self._modele

    def get_annee(self):
        return self._annee

    def get_kilometrage(self):
        return self._kilometrage

    def est_en_marche(self):
        return self._en_marche

    # Mutateurs 
    def set_marque(self, marque):
        self._marque = marque

    def set_modele(self, modele):
        self._modele = modele

    def set_annee(self, annee):
        self._annee = annee

    def set_kilometrage(self, kilometrage):
        self._kilometrage = kilometrage

    # Méthodes
    def demarrer(self):
        if self._verifier_plein() > 5:
            self._en_marche = True
            print("La voiture démarre.")
        else:
            print("Le réservoir n'est pas assez plein pour démarrer.")

    def arreter(self):
        self._en_marche = False
        print("La voiture s'arrête.")

    def _verifier_plein(self):  # Méthode privée
        return self._reservoir

# Exemple d'utilisation
ma_voiture = Voiture("Citroen", "C3", 2004, 180000)

print(ma_voiture.get_marque())  # Affiche "Citroen"
print(ma_voiture.est_en_marche())  # Affiche False

ma_voiture.demarrer()  # Affiche "La voiture démarre."
print(ma_voiture.est_en_marche())  # Affiche True

ma_voiture.arreter()  # Affiche "La voiture s'arrête."
print(ma_voiture.est_en_marche())  # Affiche False


"""
Attributs privés : Les attributs _marque, _modele, _annee, _kilometrage, _en_marche et _reservoir sont précédés d'un underscore _ pour
indiquer qu'ils sont privés.

Accesseurs et mutateurs : Des méthodes get_nom_attribut() et set_nom_attribut() sont définies pour chaque attribut afin de permettre 
l'accès et la modification de ces attributs depuis l'extérieur de la classe.

Méthode demarrer() : Cette méthode permet de démarrer la voiture. Elle vérifie d'abord si le réservoir est suffisamment plein en appelant
la méthode privée _verifier_plein(). Si le réservoir contient plus de 5 unités de carburant, l'attribut _en_marche est mis à True.

Méthode arreter() : Cette méthode permet d'arrêter la voiture en mettant l'attribut _en_marche à False.

Méthode privée _verifier_plein() : Cette méthode retourne la valeur de l'attribut _reservoir. Elle est privée car elle est destinée à
être utilisée uniquement à l'intérieur de la classe.

Exemple d'utilisation : Un objet ma_voiture de la classe Voiture est créé. Les méthodes demarrer() et arreter() sont appelées pour 
démarrer et arrêter la voiture. Les valeurs des attributs sont affichées à l'aide des accesseurs.

"""