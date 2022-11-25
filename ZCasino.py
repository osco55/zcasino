import os
from random import randint
from math import ceil

capital_depart = int(input("Saisissez votre capital de départ "))

while capital_depart>0:
    lancer = randint(0,49)

    if lancer%2==0:
        lancer_pair=True
        lancer_impair=False
    else:
        lancer_impair=True
        lancer_pair=False
    
    somme_misée = int(input("Quelle somme souhaitez vous miser ?"))
    while somme_misée>capital_depart:
        somme_misée = int(input("Merci de saisir une nouvelle somme misée "))

    arreter=True
    while arreter:
        nombre = randint(0,49)
        if nombre >= 0 and nombre <= 49:
            if nombre%2==0:
                paire=True
                impair=False
                arreter=False
            else:
                impair=True
                paire=False
                arreter=False
            
    print("Le nombre gagnant était le nombre", lancer)

    if nombre == lancer:
        somme_gagnée = 3*somme_misée
        print("Felicitations, en misant sur ", nombre," vous avez gagné :", somme_gagnée,"euros !")
        capital_depart=capital_depart+somme_gagnée
    elif lancer_pair and paire:
        somme_gagnée = ceil(0.5*somme_misée)
        print("Felicitations, en misant sur ", nombre," vous avez gagné :", somme_gagnée,"euros !")
        capital_depart=capital_depart+somme_gagnée
    elif lancer_impair and impair:
        somme_gagnée = ceil(0.5*somme_misée)
        print("Felicitations, en misant sur ", nombre," vous avez gagné :", somme_gagnée,"euros !")
        capital_depart=capital_depart+somme_gagnée
    else:
        somme_gagnée=0
        print("Vous avez perdu")
        capital_depart=capital_depart-somme_misée
    print("Votre capital est de ", capital_depart," euros")
    
print("Vous n'avez plus d'argent la partie est finie")

os.system("pause")
            



     