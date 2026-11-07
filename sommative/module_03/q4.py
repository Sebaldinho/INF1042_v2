"""Simule des tirages de nombres de 1 à 4 et calcule leur pourcentage."""

import random

try:
    nombre_tirages = int(input("Combien de tirages effectuer ? "))
    if nombre_tirages <= 0:
        raise ValueError
except ValueError:
    print("Entrez un nombre entier supérieur à zéro.")
else:
    frequences = [0, 0, 0, 0]
    for _ in range(nombre_tirages):
        resultat = random.randint(1, 4)
        frequences[resultat - 1] += 1

    print(f"Résultats de {nombre_tirages} tirages :")
    for nombre in range(1, 5):
        quantite = frequences[nombre - 1]
        pourcentage = quantite / nombre_tirages * 100
        print(f"{nombre} : {quantite} fois ({pourcentage:.2f} %)")
    maximum = max(frequences)
    nombres_les_plus_tires = [str(index + 1) for index, quantite in enumerate(frequences)
                             if quantite == maximum]
    print("Nombre(s) tiré(s) le plus souvent : " + ", ".join(nombres_les_plus_tires)
          + f" ({maximum} fois)")
