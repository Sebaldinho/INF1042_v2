"""Calcule des frais de stationnement selon la durée et le type de véhicule."""

import math

try:
    reponse_electrique = input("Le véhicule est-il électrique ? (oui/non) : ").strip().lower()
    if reponse_electrique not in ("oui", "o", "non", "n"):
        raise ValueError("Répondez par oui ou non.")
    duree = float(input("Durée du stationnement en heures : "))
    if duree <= 0:
        raise ValueError("La durée doit être supérieure à zéro.")
except ValueError as erreur:
    print(f"Saisie invalide : {erreur}")
else:
    heures_facturees = math.ceil(duree)
    prix_avant_rabais = min(4.00 + max(heures_facturees - 1, 0) * 2.50, 20.00)
    rabais = prix_avant_rabais * 0.20 if reponse_electrique in ("oui", "o") else 0.00
    total = prix_avant_rabais - rabais

    print(f"Durée : {duree:g} heures")
    print(f"Heures facturées : {heures_facturees}")
    print(f"Prix avant rabais : {prix_avant_rabais:.2f} $")
    print(f"Rabais véhicule électrique : {rabais:.2f} $")
    print(f"Total : {total:.2f} $")
