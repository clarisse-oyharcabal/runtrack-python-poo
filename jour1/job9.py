class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA)

    def afficherInfos(self):
        return f"Nom: {self.nom}, Prix HT: {self.prixHT}, TVA: {self.TVA}, Prix TTC: {self.calculerPrixTTC()}"

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrix(self, nouveau_prix):
        self.prixHT = nouveau_prix

    def getNom(self):
        return self.nom

    def getPrixHT(self):
        return self.prixHT

    def getTVA(self):
        return self.TVA
    
# Exemple d'utilisation  

# Création des produits
produit1 = Produit("Téléphone", 200, 0.20)
produit2 = Produit("Ordinateur", 800, 0.20)
produit3 = Produit("Tablette", 300, 0.20)

# Affichage des informations initiales
print("Informations initiales :")
print(produit1.afficherInfos())
print(produit2.afficherInfos())
print(produit3.afficherInfos())

# Modification du nom et du prix
produit1.modifierNom("Nouveau téléphone")
produit1.modifierPrix(250)
produit2.modifierNom("Nouvel ordinateur")
produit2.modifierPrix(900)
produit3.modifierNom("Nouvelle tablette")
produit3.modifierPrix(350)

# Affichage des informations mises à jour
print("\nInformations mises à jour :")
print(produit1.afficherInfos())
print(produit2.afficherInfos())
print(produit3.afficherInfos())

# Accès aux informations individuelles
print("\nAccès aux informations individuelles :")
print(f"Nom du produit 1 : {produit1.getNom()}")
print(f"Prix HT du produit 2 : {produit2.getPrixHT()}")
print(f"TVA du produit 3 : {produit3.getTVA()}")


"""
__init__ : Le constructeur initialise les attributs nom, prixHT et TVA avec les valeurs fournies.

calculerPrixTTC : Calcule et retourne le prix TTC en utilisant la formule prixHT * (1 + TVA).

afficherInfos : Retourne une chaîne de caractères formatée contenant toutes les informations du produit.

modifierNom : Modifie l'attribut nom du produit.

modifierPrix : Modifie l'attribut prixHT du produit.

getNom , getPrixHT , getTVA : Retournent respectivement les valeurs des attributs nom, prixHT et TVA.

"""