"""Jeu de calcul mental avec mesure du temps de réponse."""

import random
import time


while True:
    try:
        nombre_questions = int(input("Combien de questions voulez-vous ? "))
        if nombre_questions > 0:
            break
        print("Entrez un nombre supérieur à zéro.")
    except ValueError:
        print("Entrez un nombre entier valide.")

bonnes_reponses = 0
mauvaises_reponses = 0
temps_total = 0.0
operations = ["+", "-", "*"]

for numero in range(1, nombre_questions + 1):
    operation = random.choice(operations)
    premier_nombre = random.randint(1, 20)
    deuxieme_nombre = random.randint(1, 20)

    if operation == "+":
        reponse_attendue = premier_nombre + deuxieme_nombre
    elif operation == "-":
        # Garde les soustractions positives pour faciliter le calcul mental.
        premier_nombre, deuxieme_nombre = max(premier_nombre, deuxieme_nombre), min(
            premier_nombre, deuxieme_nombre
        )
        reponse_attendue = premier_nombre - deuxieme_nombre
    else:
        reponse_attendue = premier_nombre * deuxieme_nombre

    debut = time.time()
    try:
        reponse = int(
            input(f"Question {numero}/{nombre_questions} : {premier_nombre} {operation} {deuxieme_nombre} = ")
        )
    except ValueError:
        reponse = None
        print("Réponse invalide; elle compte comme une mauvaise réponse.")
    fin = time.time()
    temps_total += fin - debut

    if reponse == reponse_attendue:
        print("Bonne réponse !")
        bonnes_reponses += 1
    else:
        print(f"Mauvaise réponse. La réponse était {reponse_attendue}.")
        mauvaises_reponses += 1

temps_moyen = temps_total / nombre_questions
print("\nRésultat final")
print(f"Score : {bonnes_reponses}/{nombre_questions}")
print(f"Bonnes réponses : {bonnes_reponses}")
print(f"Mauvaises réponses : {mauvaises_reponses}")
print(f"Temps total : {temps_total:.2f} secondes")
print(f"Temps moyen par question : {temps_moyen:.2f} secondes")
