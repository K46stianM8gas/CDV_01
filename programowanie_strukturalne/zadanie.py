print("podaj znak")
znak = input()

print("podaj ilosc wyswietlen znaku")
ilosc = int(input())

licznik = 0

for i in range(ilosc):
    print(znak)
    for y in range(ilosc):
        print(znak, end="")