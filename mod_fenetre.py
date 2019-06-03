#on l'appelle module fenêtre (pour créer la fenêtre)

import tkinter as tk
from tkinter import * # va chercher toutes les fonctionalités
from tkinter import messagebox #importer message box
#incenser 4 var de type bmi qu'on a crée tantôt donc importer module:
from mod_bmi_modele import Bmi
from calcul_imc import calcul_imc #reste à importer dans l'autre fenêtre

#puis définir la fonction calculer
def calculer():
    _poids = float (poids.get()) # va récupérer le poids
    _taille = float (taille.get())
    #ces chiffres sont des décimales donc pour le convertir: ajouter float
    _nom = nom.get()
    _age = age.get() #incenser 4 var de type bmi qu'on a crée tantôt donc importer module
    unpatient = Bmi(nom = _nom, age = age, poids = _poids, taille = taille)
    #le résultat: formule:
    txt_imc = calcul_imc(unpatient) #le voit pas, faut l'importer
    messagebox.showinfo("Résultat", message = "{0:5.3F}".format(txt_imc))
    #importer message box
    #mettre 3 chiffres après la décimale

#créer var appellé root de type tk
root=Tk()
root.title("Calcul de l'indice de masse corporelle")
root.geometry("680x400")

rootfont=('arial', 20, 'bold')
label = Label(root, text='Saisie des données Patient', font=rootfont)
label.grid(row=0, column=2)

Label(root, text='Nom').grid(row=1, column=1)
Label(root, text='Age').grid(row=2, column=1)
Label(root, text='Poids').grid(row=3, column=1)
Label(root, text='Taille').grid(row=4, column=1)
Label(root, text='Indice de masse corporelle').grid(row=5, column=1)
Label(root, text='Risque de santé').grid(row=6, column=1)

nom = Entry(root, width=30)
nom.grid(row=1, column=2, sticky = "w") #sticky aligner à gauche (west): https://effbot.org/tkinterbook/grid.htm
age = Entry(root, width=20)
age.grid(row=2, column=2, sticky = "w")
poids = Entry(root, width=20)
poids.grid(row=3, column=2, sticky = "w")
taille = Entry(root, width=20)
taille.grid(row=5, column=2, sticky = "w")
risque = Entry(root, width=50)
risque.grid(row=6, column=2, sticky = "w")

ok = Button(root, text='Calculer', width=20, command = calculer) #puis définir la fonction calculer
ok.grid(row=8, column=1)
enregistrer = Button(root, text='Enregistrer', width=20)
enregistrer.grid(row=8, column=2)
quitter = Button(root, text='Quitter', width=20, command = quit)
quitter.grid(row=10, column=1)

root.mainloop()

