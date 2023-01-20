x= int(input("combien de temps de travail? "))
s= float(input("Quel est le salaire horaire? "))

if x <= 160:
    salaire = x * s

elif x <= 200:
    salaire = 160 * s + (x - 160) * s * 1.25
else:
    salaire = 160 * s + 40 * s * 1.25 + (x - 200) * s * 1.5
    

salaire = round(salaire, 2)
print(salaire)