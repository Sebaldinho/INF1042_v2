# Erreurs dans le code original :
# 1. Il manque : après la condition if.
# 2. L'instruction print après if doit être indentée.
# 3. L'instruction print après else doit être indentée.
# Bonne pratique : utiliser est_etudiant directement, sans == True.

age = 20
est_etudiant = True

if age >= 18 and est_etudiant:
    print("Tarif étudiant disponible")
else:
    print("Plein tarif")
