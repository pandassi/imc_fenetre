#créer classe principale
class Bmi:
    #créer constructeur/initialisateur:
    def __init__(self,age,nom,poids,taille):
        self.age = age #self = var de la class, peut mettre x y mais mélanger encore +
        self.nom = nom
        self.poids = poids
        self.taille = taille

        #fonction pour afficher le résultat
    def __str__(self):
        return "Nom {}, poids {}, taille: {} Age {} ".format(self.nom, self.poids, self.taille, self.age) #afficher 3 valeurs

#créer un autre module pour notre fenêtre
#on l'appelle module fenêtre