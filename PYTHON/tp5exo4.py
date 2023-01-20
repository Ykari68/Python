x = int(input("Combien? "))

c = x//100
reste= x%100

f = reste//50
reste= reste%50

g = reste//20
reste= reste%20

d = reste//10
reste= reste%10

e = reste//2
reste= reste%2 

u = reste//1
reste= reste%1

print(x,"euros, c'est",c, "billet(s) de 100,",f, "billet(s) de 50,",g, "billet(s) de 20,",d, "billet(s) de 10,",e, "pièce(s) de 2,",u, "pièce(s) de 1,")
