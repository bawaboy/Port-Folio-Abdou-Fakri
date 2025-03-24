essais = 0
valeur = int (input("Entrez un nombre à chercher(entre 1 et 100) : "))

while valeur < 1 or valeur > 100 :
    print("Erreur ! Veuillez entrer une valeur entre 1 et 100.")
    valeur = int (input("Entrez un nombre à chercher(entre 1 et 100) : "))

reponse = int(input("Le nombre caché est : "))

while reponse != valeur :
    print("HellNaaah ! C'est faux !")
    reponse = int(input("Réessaie : "))
    essais += 1

if reponse == valeur :
    print("HELLLYEAAAAH ! Bien joué ! Vous avez deviné en " + str(essais) + " essais !")