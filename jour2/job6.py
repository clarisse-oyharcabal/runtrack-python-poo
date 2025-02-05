class Commande:
    def __init__(self, numero_commande):
        self._numero_commande = numero_commande
        self._plats_commandes = {}  # Dictionnaire: {nom_plat: {prix: prix, statut: 'en cours'}}
        self._statut = 'en cours'

    def ajouter_plat(self, nom_plat, prix):
        if self._statut == 'en cours':
            self._plats_commandes[nom_plat] = {'prix': prix, 'statut': 'en cours'}
            print(f"Plat '{nom_plat}' ajouté à la commande {self._numero_commande}.")
        else:
            print(f"Impossible d'ajouter un plat à une commande {self._statut}.")

    def annuler_commande(self):
        if self._statut == 'en cours':
            self._statut = 'annulée'
            for plat in self._plats_commandes:
                self._plats_commandes[plat]['statut'] = 'annulé'
            print(f"Commande {self._numero_commande} annulée.")
        else:
            print(f"La commande {self._numero_commande} est déjà {self._statut}.")

    def _calculer_total(self):  # Méthode privée
        total = 0
        for plat, details in self._plats_commandes.items():
            if details['statut'] == 'en cours':  # Ne pas inclure les plats annulés
                total += details['prix']
        return total

    def afficher_commande(self):
        print(f"Commande N°{self._numero_commande}:")
        for plat, details in self._plats_commandes.items():
            print(f"- {plat}: {details['prix']}€ ({details['statut']})")
        total = self._calculer_total()
        print(f"Total: {total:.2f}€")

    def calculer_tva(self, taux_tva=0.20):  # Méthode pour calculer la TVA
        total = self._calculer_total()
        tva = total * taux_tva
        return tva

# Exemple d'utilisation
commande1 = Commande("001")

commande1.ajouter_plat("Tacos", 12)
commande1.ajouter_plat("Piquillos", 10)
commande1.ajouter_plat("Fondant chocolat", 6)

commande1.afficher_commande()

tva = commande1.calculer_tva()
print(f"TVA: {tva:.2f}€")

commande1.annuler_commande()
commande1.afficher_commande()


"""
Attributs privés : Les attributs _numero_commande, _plats_commandes et _statut sont privés (précédés de _).

Méthodes :
ajouter_plat(): Ajoute un plat à la commande avec son prix.
annuler_commande(): Annule la commande et met à jour le statut des plats.
_calculer_total(): Calcule le total de la commande (méthode privée).
afficher_commande(): Affiche la commande avec les détails et le total.
calculer_tva(): Calcule et retourne le montant de la TVA.

Encapsulation : Les attributs sont privés, et les méthodes permettent de les manipuler de l'extérieur.

Abstraction : L'utilisateur interagit avec des méthodes simples sans avoir à se soucier des détails internes.
Dictionnaire pour les plats : La liste des plats est un dictionnaire pour faciliter l'accès aux informations
(prix, statut).

"""