BASE = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400
nbConvives = int(input("Combien sommes-vous à manger ? "))
newFromage = (fromage*nbConvives)/BASE
newEau = (eau*nbConvives)/BASE
newAil = (ail*nbConvives)/BASE
newPain = (pain*nbConvives)/BASE
print("Afin de faire une fondue fribourgeoise pour", nbConvives,"personnes, il vous faut :")
print("- ",newFromage,"gr de fromage")
print("- ",newEau,"dl d'eau")
print("- ",newAil,"gousse(s) d'ail")
print("- ",newPain,"gr de pain")
