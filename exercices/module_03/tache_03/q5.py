import random

options = ["Pierre", "Papier", "Ciseaux"]
choix_ordinateur = random.choice(options)
choix_utilisateur = input("Choisissez Pierre, Papier ou Ciseaux : ")

if choix_utilisateur == choix_ordinateur:
    print("Égalité !")
else:
    print("Choix différents !")
