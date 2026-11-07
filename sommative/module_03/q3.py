"""Calcule une facture avec rabais selon le sous-total, puis les taxes."""

TAUX_RABAIS_PETIT = 0.00  # Sous 50 $
TAUX_RABAIS_MOYEN = 0.05  # De 50 $ à 100 $, inclusivement
TAUX_RABAIS_GRAND = 0.10  # Plus de 100 $
TAUX_TAXES = 0.13  # TVH de 13 %

try:
    sous_total = float(input("Montant des achats avant rabais ($) : "))
    if sous_total < 0:
        raise ValueError
except ValueError:
    print("Veuillez entrer un montant positif valide.")
else:
    if sous_total < 50:
        taux_rabais = TAUX_RABAIS_PETIT
    elif sous_total <= 100:
        taux_rabais = TAUX_RABAIS_MOYEN
    else:
        taux_rabais = TAUX_RABAIS_GRAND

    montant_rabais = sous_total * taux_rabais
    montant_apres_rabais = sous_total - montant_rabais
    taxes = montant_apres_rabais * TAUX_TAXES
    total = montant_apres_rabais + taxes

    print(f"Montant initial : {sous_total:.2f} $")
    print(f"Pourcentage de rabais : {taux_rabais:.0%}")
    print(f"Montant économisé : {montant_rabais:.2f} $")
    print(f"Sous-total après rabais : {montant_apres_rabais:.2f} $")
    print(f"TVH (13 %) : {taxes:.2f} $")
    print(f"Total final : {total:.2f} $")
