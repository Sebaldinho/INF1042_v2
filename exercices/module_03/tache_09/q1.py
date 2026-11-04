"""Génère un identifiant et un mot de passe à partir des renseignements fournis."""

import random
import string


prenom = input("Entrez votre prénom : ").strip()
nom = input("Entrez votre nom : ").strip()
annee_naissance = input("Entrez votre année de naissance : ").strip()
ville = input("Entrez votre ville : ").strip()

# L'identifiant est simplifié en minuscules et sans espaces.
identifiant = (
    f"{prenom.lower().replace(' ', '')}."
    f"{nom.lower().replace(' ', '')}@"
    f"{ville.lower().replace(' ', '')}.ca"
)

# Le mot de passe combine des extraits des réponses et quatre caractères aléatoires.
extrait_prenom = prenom[:2]
extrait_nom = nom[-2:]
extrait_annee = annee_naissance[-2:]
extrait_ville = ville[:2]
caracteres_aleatoires = "".join(random.choices(string.ascii_letters + string.digits + "!@#$%", k=4))
mot_de_passe = (
    f"{extrait_prenom}{extrait_nom}{extrait_annee}"
    f"{extrait_ville}{caracteres_aleatoires}"
)

print(f"Identifiant : {identifiant}")
print(f"Mot de passe généré : {mot_de_passe}")
