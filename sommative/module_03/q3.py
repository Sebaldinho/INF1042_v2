"""Calcule une facture avec rabais selon le sous-total, puis les taxes."""

# Taux choisis, car l'énoncé ne précise pas les pourcentages.
TAUX_RABAIS_PETIT = 0.00  # Sous 50 $
TAUX_RABAIS_MOYEN = 0.05  # De 50 $ à 100 $, inclusivement
TAUX_RABAIS_GRAND = 0.10  # Plus de 100 $
TAUX_TAXES = 0.14975  # Exemple : TPS (5 %) + TVQ (9,975 %)

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

    print(f"Rabais ({taux_rabais:.0%}) : {montant_rabais:.2f} $")
    print(f"Taxes : {taxes:.2f} $")
    print(f"Total à payer : {total:.2f} $")
