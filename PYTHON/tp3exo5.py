début = int(input("Indiquez l'heure de début de la location (un nombre entier) : "))
fin = int(input("Indiquez l'heure de fin de la location (un nombre entier) : "))
if début<0 or début>24 or fin<0 or fin>24:
    print("Les heures doivent être comprises entre 0 et 24 ! ")
elif début==fin:
    print("Attention ! L'heure de fin est identique à l'heure de début.")
elif début>fin:
    print("Attention ! Le début de la location est après la fin ...")

un=0
deux=0

if fin<7:
    un = fin - début
else:
    if début<7:
        un = 7 - début
        début = 7

    if fin<17:
        deux=2*(fin-début)
    else:
        if début<17:
            deux=2*(17-début)
            début=17
        un+=fin-début

print("Vous avez loué votre vélo pour")
if un>0:
    print(un, "heure(s) au taux horaire de 1,0 euro(s)")
if deux>0:
    print(deux//2, "heure(s) au taux horaire de 2,0 euro(s)")
print("Le montant total à payer est de", float(deux+un), "euro(s).")