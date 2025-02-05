# Classes

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        # Méthode attaquer : inflige des dégâts à l'adversaire
        degats = 10  # Points de dégâts fixes pour simplifier
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} dégâts.")

class Jeu:
    def __init__(self):
        self.niveau = 0

    def choisirNiveau(self):
        # Méthode choisirNiveau : définit la difficulté et les points de vie
        while self.niveau not in [1, 2, 3]:
            self.niveau = int(input("Choisissez le niveau de difficulté (1, 2 ou 3) : "))

    def lancerJeu(self):
        # Méthode lancerJeu : initialise les personnages en fonction du niveau
        if self.niveau == 1:
            vie_joueur = 100
            vie_ennemi = 80
        elif self.niveau == 2:
            vie_joueur = 80
            vie_ennemi = 100
        else:  # niveau 3
            vie_joueur = 60
            vie_ennemi = 120

        self.joueur = Personnage("Joueur", vie_joueur)
        self.ennemi = Personnage("Ennemi", vie_ennemi)

        self.deroulementPartie()

    def verifierSante(self):
        # Méthode verifierSante : vérifie si un personnage est vaincu
        if self.joueur.vie <= 0:
            print("Le joueur est vaincu !")
            return True
        if self.ennemi.vie <= 0:
            print("L'ennemi est vaincu !")
            return True
        return False

    def determinerGagnant(self):
        # Méthode determinerGagnant : affiche le résultat final
        if self.joueur.vie > self.ennemi.vie:
            print("Le joueur a gagne !")
        else:
            print("L'ennemi a gagne !")

    def deroulementPartie(self):
        # Méthode deroulementPartie : gère le déroulement du jeu
        while True:
            # Tour du joueur
            self.joueur.attaquer(self.ennemi)
            if self.verifierSante():
                self.determinerGagnant()
                break

            # Tour de l'ennemi
            self.ennemi.attaquer(self.joueur)
            if self.verifierSante():
                self.determinerGagnant()
                break

            print(f"Vie du joueur : {self.joueur.vie}")
            print(f"Vie de l'ennemi : {self.ennemi.vie}")

# Déroulement du jeu 

jeu = Jeu()
jeu.choisirNiveau()
jeu.lancerJeu()


"""
Classe Personnage :
__init__ : initialise le nom et la vie du personnage.
attaquer : inflige des dégâts à l'adversaire.

Classe Jeu :
__init__ : initialise le niveau à 0.

choisirNiveau : demande au joueur de choisir la difficulté.

lancerJeu : crée les personnages avec les points de vie appropriés.

verifierSante : vérifie si un personnage est mort.

determinerGagnant : affiche le vainqueur.

deroulementPartie : gère les tours et les interactions.

"""