notes = []
for i in range(5):
    note = input(f"Entrez la {i+1}e note et son coefficient: ")
    notes.append(note.split())


for i in range(5):
    notes[i][0] = float(notes[i][0])
    notes[i][1] = float(notes[i][1])


coeff_total = 0
note_total = 0
for i in range(5):
    coeff_total += notes[i][1]
    note_total += notes[i][0] * notes[i][1]
m = note_total / coeff_total

m = round(m, 2)

print(f"Votre moyenne est {m}")

passed = True
for i in range(5):
    if notes[i][0] < 8:
        passed = False
        break
if m > 10 and passed:
    print("Admis!")
else:
    print("Pas admis!")