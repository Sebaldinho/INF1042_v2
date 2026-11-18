phrase = input("Entrez une phrase : ")
mots = phrase.split()

print("Nombre de mots :", len(mots))
phrase_avec_tirets = "-".join(mots)
print("Phrase avec des tirets :", phrase_avec_tirets)
