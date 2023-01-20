prenom = str.capitalize(input("Veuillez entrer un prénom: "))
nom = str.upper(input("Veuillez entrer un nom: "))
prenom2 = str.capitalize(input("Veuillez entrer un autre prénom: "))
nom2 = str.upper(input("Veuillez entrer un autre nom: "))

if nom<nom2:
    print(prenom, nom)
    print(prenom2, nom2)

elif nom>nom2:

    print(prenom2, nom2)
    print(prenom, nom)

elif nom==nom2:
    if prenom<prenom2:
        print(prenom, nom)
        print(prenom2, nom2)
    
    elif prenom>prenom2:
        print(prenom2, nom2)
        print(prenom, nom)