"""Calcule le nombre d'heures, de minutes et de secondes dans une année."""

jours_par_annee = 365  # Une année normale (sans année bissextile).
heures_par_jour = 24
minutes_par_heure = 60
secondes_par_minute = 60

heures = jours_par_annee * heures_par_jour
minutes = heures * minutes_par_heure
secondes = minutes * secondes_par_minute

print(f"Dans une année de {jours_par_annee} jours :")
print(f"Jours : {jours_par_annee}")
print(f"{heures} heures")
print(f"{minutes} minutes")
print(f"{secondes} secondes")
