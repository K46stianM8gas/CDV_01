programowanie = ["Python", "C#", "PHP", "JS", "JAVA"]

print(programowanie)
print(type(programowanie))

pierwszy = programowanie[0]
print("pierwszy język programowania " + pierwszy)

trzyElementy = programowanie[0:3]
print(trzyElementy)

ostatni = programowanie[-1]
print(ostatni)

#dodawanie nowego elementu na końcu tablicy

programowanie.append("R")
print(programowanie)

#zliczanie elementów w liście

ile = programowanie.count("Python")
print(ile)

programowanie.append("Python")

ile = programowanie.count("Python")
print(ile)

print(programowanie)
iloscElementow = len(programowanie)
print("ilosc elementow w liscie:", iloscElementow)

print("Ilość elementów w liście: ", end="") #end nie zakończy linii
print(iloscElementow)


#połączenie list

print("===========================", "\n")

print(programowanie)
inneJezyki = ["C", "C++", "PASCAL"]
print(inneJezyki)
print("Połączenie list")
programowanie.extend(inneJezyki)
print(programowanie)

print("===========================", "\n")

#wyczyszczenie listy

nowa = programowanie
xd = ["delfi"]
programowanie.extend(xd)
print(nowa)
print(programowanie)
print("lista nowa", end="")
print(nowa)

nowa.clear()

print("Lista programowanie: ", programowanie)
print(programowanie)






