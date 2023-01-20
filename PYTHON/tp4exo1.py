x = float(input("Vous cherchez la table de multiplication de quel nombre ? "))

m = [[0 for col in range(2)] for row in range(10)]

for i in range(10):
    m[i][0] = i
    m[i][1] = round(x * m[i][0], 1)     
    print(f"{x} * {m[i][0]} = {m[i][1]}")
    