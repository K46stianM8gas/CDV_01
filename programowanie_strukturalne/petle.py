#pętle

licznik = 0

while (licznik < 3):
    #licznik = licznik + 1
    licznik += 1
    print("CDV")

################################

licznik = 0
while (licznik < 3):
    licznik += 1
    print(licznik, end="")
else:
    print("KONIEC PĘTLI")

################################

lista = ["Jan", "Anna", "Paweł"]

for i in lista:
    print(i)

text = "Janusz"

for i in text:
    print(i)

################################

slownik = dict()
slownik['a'] = 1
slownik['b'] = 2

for i in slownik:
    #print(i)
    print("%s %d" % (i, slownik[i]))


###############################

lista = ["kebab", "hot-dog", "fafalelel"]

for index in range(len(lista)):
    print(lista[index])


###############################

lista2 = ["1", "22", "333", "4444"]

for i in lista2:
    print(i)


###############

lista3 = []

ilosc = int(input())

for i in range(ilosc):
    lista3.append(i)
    #print(lista3)
    print(i)
    for y in range(ilosc):
        print(i, end="")





















