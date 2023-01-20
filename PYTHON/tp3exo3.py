import random
n = random.randint(0, 100)

reponse=int(input("Donnez un nombre entre 0 et 100: "))
count=1

if reponse == n:
    count=0
    print("BINGO, il vous aura fallu",count,"essai")
else:
    while reponse != n:
        reponse = int(input("Mince, redonnez un nombre entre 0 et 100: "))
        if reponse>n:
            print("Essayez une valeur plus petite")
            count+=1

        else:
            print("Essayez une valeur plus grande")
            count+=1

print("BINGO, il vous aura fallu",count,"essai")

