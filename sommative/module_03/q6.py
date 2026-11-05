"""Calcule des frais de stationnement et applique un rabais pour véhicule électrique."""

# Barème progressif choisi pour rendre l'exercice exécutable :
# 3 $/h pour les 2 premières heures, puis 2 $/h jusqu'à 5 h,
# puis 1 $/h au-delà. Le rabais électrique est de 20 %.
RABAIS_ELECTRIQUE = 0.20

try:
    heures = float(input("Durée du stationnement en heures : "))
    if heures < 0:
        raise ValueError
except ValueError:
    print("Entrez une durée positive valide.")
else:
    heures_premier_tarif = min(heures, 2)
    heures_deuxieme_tarif = min(max(heures - 2, 0), 3)
    heures_troisieme_tarif = max(heures - 5, 0)
    frais = (heures_premier_tarif * 3
             + heures_deuxieme_tarif * 2
             + heures_troisieme_tarif * 1)

    reponse = input("Voiture électrique ? (oui/non) : ").strip().lower()
    if reponse in ("oui", "o"):
        rabais = frais * RABAIS_ELECTRIQUE
    elif reponse in ("non", "n"):
        rabais = 0
    else:
        rabais = 0
        print("Réponse non reconnue; aucun rabais appliqué.")

    total = frais - rabais
    print(f"Frais avant rabais : {frais:.2f} $")
    print(f"Rabais : {rabais:.2f} $")
    print(f"Total à payer : {total:.2f} $")
