
b = int(input("Choisissez la boucle (1 pour for, 0 pour while)"))
if b != 1 or b != 0:
    print("Ne peut pas choisir une boucle")

if b==1:
    n = int(input('Entrez un nombre : '))
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    print (n,'! = ',fact)







