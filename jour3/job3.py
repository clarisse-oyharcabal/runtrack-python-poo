# Classes

class Tache:
    def __init__(self, titre, description, statut="a faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def __str__(self):  # Pour un affichage plus lisible
        return f"{self.titre} : {self.description} ({self.statut})"
    

class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, titre):
        self.taches = [t for t in self.taches if t.titre != titre]

    def marquerCommeFinie(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                tache.statut = "terminee"
                break

    def afficherListe(self):
        for tache in self.taches:
            print(tache)

    def filterListe(self, statut):
        return [t for t in self.taches if t.statut == statut]
    
# Tests

# Création de tâches
tache1 = Tache("Faire les runtrack", "Faire job3, job4 et job5")
tache2 = Tache("Approfondir mes softskills", "Terminer le CV, construire le pitch de 3 minutes")
tache3 = Tache("Modifier mon Portfolio", "Ajouter mes autres projets")

# Création de la liste de tâches
liste = ListeDeTaches()

# Ajout des tâches
liste.ajouterTache(tache1)
liste.ajouterTache(tache2)
liste.ajouterTache(tache3)

# Affichage de la liste
print("Liste des taches :")
liste.afficherListe()

# Suppression d'une tâche
liste.supprimerTache("Approfondir mes softskills")
print("\nListe des taches apres suppression :")
liste.afficherListe()

# Marquer une tâche comme terminée
liste.marquerCommeFinie("Faire les runtrack")
print("\nListe des taches apres avoir marque une tache comme terminee :")
liste.afficherListe()

# Filtrer les tâches à faire
taches_a_faire = liste.filterListe("a faire")
print("\nTaches a faire :")
for tache in taches_a_faire:
    print(tache)

"""
Classe Tache : Représente une tâche avec un titre, une description et un statut. La méthode __str__ permet d'afficher la tâche
de manière plus lisible.

Classe ListeDeTaches :
ajouterTache : Ajoute une tâche à la liste.
supprimerTache : Supprime une tâche de la liste en fonction de son titre.
marquerCommeFinie : Change le statut d'une tâche à "terminée".
afficherListe : Affiche toutes les tâches de la liste.
filterListe : Retourne une nouvelle liste contenant uniquement les tâches avec le statut spécifié.

"""