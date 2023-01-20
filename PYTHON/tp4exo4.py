L1 = [2, 2, 6, 6, 7, 1, 6, 6, 1, 7, 6]

amount = 0

for i in L1:
    counter = L1.count(i)
    if counter > amount:
        amount = counter
        high = i

print(f"Le nombre le plus frequent dans la liste est le : {high} ({amount} x)")
