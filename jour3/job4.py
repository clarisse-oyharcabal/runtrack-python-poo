# Classes

class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.buts += 1

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        print(f"Statistiques de {self.nom} (Numero {self.numero}, Poste {self.position}) :")
        print(f"- Buts : {self.buts}")
        print(f"- Passes decisives : {self.passes_decisives}")
        print(f"- Cartons jaunes : {self.cartons_jaunes}")
        print(f"- Cartons rouges : {self.cartons_rouges}")


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        print(f"Statistiques des joueurs de l'equipe {self.nom} :")
        for joueur in self.joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, numero, buts=0, passes_decisives=0, cartons_jaunes=0, cartons_rouges=0):
        for joueur in self.joueurs:
            if joueur.numero == numero:
                joueur.buts += buts
                joueur.passes_decisives += passes_decisives
                joueur.cartons_jaunes += cartons_jaunes
                joueur.cartons_rouges += cartons_rouges
                break

# Tests

# Création de joueurs
joueur1 = Joueur("Oyarzabal", 10, "Attaquant")
joueur2 = Joueur("Aramburu", 19, "Defenseur")
joueur3 = Joueur("Pedri", 8, "Milieu de terrain")
joueur4 = Joueur("Raphinha", 11, "Attaquant")

# Création d'équipes
equipe1 = Equipe("Real Sociedad")
equipe2 = Equipe("FC Barcelone")

# Ajout de joueurs aux équipes
equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)
equipe2.ajouterJoueur(joueur3)
equipe2.ajouterJoueur(joueur4)

# Affichage des statistiques initiales
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()

# Simulation de match
joueur1.marquerUnBut()
joueur1.effectuerUnePasseDecisive()
joueur2.recevoirUnCartonJaune()
joueur4.recevoirUnCartonRouge()

# Mise à jour des statistiques via l'équipe
equipe1.mettreAJourStatistiquesJoueur(7, buts=1)  # Oyarzabal marque un autre but
equipe2.mettreAJourStatistiquesJoueur(30, passes_decisives=2)  # Raphinha fait deux passes décisives

# Affichage des statistiques après le match
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()


"""
Classe Joueur :
Les attributs sont initialisés dans le constructeur.
Les méthodes permettent de mettre à jour les statistiques individuelles du joueur.

Classe Equipe :
L'attribut joueurs est une liste initialement vide.

ajouterJoueur : Ajoute un joueur à l'équipe.

afficherStatistiquesJoueurs : Affiche les statistiques de tous les joueurs de l'équipe.

mettreAJourStatistiquesJoueur : Met à jour les statistiques d'un joueur spécifique en fonction de son numéro.

"""