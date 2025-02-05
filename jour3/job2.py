class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Numero de compte: {self.__numero_compte}")
        print(f"Nom: {self.__nom}")
        print(f"Prenom: {self.__prenom}")
        print(f"Solde: {self.__solde}")
        print(f"Decouvert autorise: {self.__decouvert}")

    def afficherSolde(self):
        print(f"Solde du compte: {self.__solde}")

    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant} effectue.")
        self.afficherSolde()

    def retrait(self, montant):
        if self.__solde >= montant or self.__decouvert:
            self.__solde -= montant
            print(f"Retrait de {montant} effectue.")
            self.afficherSolde()
        else:
            print("Solde insuffisant pour effectuer le retrait.")

    def agios(self):
        if self.__solde < 0:
            # Exemple : 10% d'agios
            agios = abs(self.__solde) * 0.10
            self.__solde -= agios
            print(f"Des agios de {agios} ont été appliqués.")
            self.afficherSolde()

    def virement(self, compte_destinataire, montant):
        if self.__solde >= montant or self.__decouvert:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant} effectue vers le compte {compte_destinataire.__numero_compte}.")
            self.afficherSolde()
        else:
            print("Solde insuffisant pour effectuer le virement.")

# Création de deux comptes
compte1 = CompteBancaire("12345", "Doe", "John", 1000)
compte2 = CompteBancaire("67890", "Pitt", "Anne", -500, decouvert=True)

# Tests des méthodes
compte1.afficher()
compte1.versement(500)
compte1.retrait(2000)
compte1.retrait(500)
compte1.agios()

compte2.afficher()
compte2.versement(1000)
compte2.virement(compte2, 500)

compte1.afficher()
compte2.afficher()


"""
Attributs : Les attributs numero_compte, nom, prenom et solde sont utilisés pour stocker les informations du compte.
L'attribut decouvert est un booléen qui indique si le compte a le droit à un découvert.

Méthodes : Les méthodes afficher, afficherSolde, versement, retrait, agios et virement implémentent les fonctionnalités demandées.

Gestion du découvert : Les méthodes retrait et virement vérifient si le solde est suffisant, sauf si le découvert est autorisé.

Agios : La méthode agios calcule et applique des agios si le solde est négatif.

Virement : La méthode virement effectue un virement vers un autre compte, en vérifiant le solde et en mettant à jour les deux comptes.

"""