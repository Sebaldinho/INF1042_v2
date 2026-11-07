"""Jeu de pierre, papier, ciseaux avec compte des résultats."""

import random

choix_possibles = ["pierre", "papier", "ciseaux"]
victoires = 0
defaites = 0
nulles = 0

while True:
    choix_joueur = input("Votre choix (pierre, papier, ciseaux ou quitter) : ").strip().lower()
    if choix_joueur == "quitter":
        break
    if choix_joueur not in choix_possibles:
        print("Choix invalide.")
        continue

    choix_ordinateur = random.choice(choix_possibles)
    print(f"Vous : {choix_joueur}")
    print(f"Ordinateur : {choix_ordinateur}")

    if choix_joueur == choix_ordinateur:
        print("Partie nulle.")
        nulles += 1
    elif (choix_joueur == "pierre" and choix_ordinateur == "ciseaux") or \
         (choix_joueur == "papier" and choix_ordinateur == "pierre") or \
         (choix_joueur == "ciseaux" and choix_ordinateur == "papier"):
        print("Vous gagnez !")
        victoires += 1
    else:
        print("Vous perdez.")
        defaites += 1

print("\nRésultats")
print(f"Victoires : {victoires}")
print(f"Défaites : {defaites}")
print(f"Parties nulles : {nulles}")
print(f"Total de parties : {victoires + defaites + nulles}")
