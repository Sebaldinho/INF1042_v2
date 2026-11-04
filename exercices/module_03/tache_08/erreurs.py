"""Programme de fidélité et d'épargne corrigé."""


def prix_vip(prix):
    """Retourne le prix après le rabais VIP de 20 %."""
    rabais = 0.20
    return prix * (1 - rabais)


def points_fidelite(nombre_achats):
    """Accorde 10 points par achat."""
    points_par_achat = 10
    return nombre_achats * points_par_achat


def epargne_apres_mois(montant_initial, depot_mensuel, nombre_mois):
    """Calcule l'épargne sans intérêts après les dépôts mensuels."""
    return montant_initial + depot_mensuel * nombre_mois


if __name__ == "__main__":
    prix = prix_vip(50)
    points = points_fidelite(5)
    epargne = epargne_apres_mois(100, 30, 4)

    print(f"Prix VIP obtenu = {prix:.2f} $")
    print(f"Points de fidélité pour 5 achats = {points} points")
    print(f"Épargne sur 4 mois = {epargne:.2f} $")
