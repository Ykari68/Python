print("Question 1: ")

T = str(input("essaie: "))
taille = 0
for i in range(len(T)):
    if T[i] == '\0':
        break
    taille += 1

print(taille)

print("Question 2: ")

T = str(input("essaie: "))
taille = 0
voyelles = 0
for i in range(len(T)):
    if T[i] == '\0':
        break
    taille += 1
    if T[i] in "aeieoAEIEO"  :
        voyelles += 1
pourcentage = (voyelles/taille)*100
pourcentage = round(pourcentage, 2)

print("Il y a", voyelles, "voyelle(s) pour", taille, "caractère(s), soit", pourcentage,"% de voyelles")

print("Question 3: ")

#T = str(input("essaie: "))

#position = T.find("wagon")
#if position != -1:
    #print("Il y a wagon à", position)
#else:
    #print("Il n'y a pas wagon")

T = str(input("essaie: "))

trouvé = False

for i in range(len(T)):
    if T[i:i+5] == "wagon" or T[i:i+5] == "WAGON":
        print("Il y a wagon à", i)
        trouvé = True
        break
if not trouvé:
    print("Il n'y a pas wagon")

print("Question 4: ")

T = str(input("essaie: "))
occurence = 0
for i in range(len(T)):
    if T[i:i+5] == 'wagon':
        occurence += 1

print(occurence)





