phrase = input("Entrez une phrase : ")
voyelles = "aeiouy"
nombre_voyelles = 0

for caractere in phrase.lower():
    if caractere in voyelles:
        nombre_voyelles = nombre_voyelles + 1

print("Nombre de voyelles :", nombre_voyelles)
