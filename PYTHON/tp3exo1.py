print("a)")
n = int(input("Entrez N: "))
s = 0
for i in range(n):
   s += n
   n -= 1
   print("Somme vaut",s)

print("b)")
w = int(input("Veuillez entrer une valeur : "))
while w != 100:
    w = int(input("Veuillez entrer une valeur (On veut quelque chose qui ressemble à 100): "))
print("Merci!")

print("c)")

dix = 0
quinze = 0
vingt = 0
for i in range(9):
    value = int(input(f"Veuillez entrez la variable numéro {i + 1}: "))
    while value < 0 or value > 20:
        value = int(input(f"Veuillez entrez la variable numéro {i + 1}: "))
    if 0 <= value < 10:
            dix += 1
    elif 10 <= value < 15:
            quinze += 1
    elif 15 <= value <= 20:
            vingt += 1
print(f"Il y a {dix} nombres dans l'interval [0;10[, {quinze} dans l'interval [10;15[ et {vingt} dans " 
    f"l'interval [15;20]")


         
print("d)")

x = int(input("Entrez un nombre > 1 : "))
n = 1
s = 0
while s <= x:
    s += n
    n += 1
print("Le plus grand nombre est", n - 2)




