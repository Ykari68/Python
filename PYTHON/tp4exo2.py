n = int(input("nombre d'etudiants : "))
moyenne = 0.0
sum = 0.0

notes = [0] * n

for i in range(n):
    notes[i] = float(input(f"Note étudiant {i} : "))
    sum = sum + notes[i]

mean = sum / n
print(f"Moyenne de la classe : {mean}")

print("Numéro de l’Etudiant | note | ecart a la moyenne")
for i in range(n):
    gap = notes[i] - mean
    print(f"{i} | {notes[i]} | {gap}")