#podstawy
#print("CDV eloeloeloelo")

#potega

#potega = 2 ** 10
#print(potega)


# wypisanie dwa razy tekstu
#tekst = "CDV"
#print(tekst * 2)


# pobieranie danych z  + konkatenacja stringów

#print("PODAJ IMIE GRZESZNIKU")
#imie = input()
#print ("Twoje imie podane z klawiatury " + imie)

#nazwisko = "Nowak"

#print("TWOJE DANE GRZESZNIKU: " + imie + " " + nazwisko)

#dlugosc = len(nazwisko)
#print("DLUGOSC TWOJEGO NAZWISKA GRZESZNIKU = ")
#print(dlugosc)

#print(type(imie))
#print(type(nazwisko))

#wiek = input()
#print("TWOJ WIEK: " + wiek)
#print(type(wiek))

tekst = "Paweł, Anna, Michał"

tab = tekst.split(",")
print(tekst)
print(tab)

imie1 = tab[0]
print("Pierwsze imie w tablicy "+ imie1)

imiemale = imie1.lower()
print(imiemale)

zawartosc = imie1.isalpha()
print(zawartosc)

imie2 = ""
zawartosc2 = imie2.isalpha()
print(zawartosc2)

imie = "Julia"
print("\n dane użytkownika \n Masz na imie:" + imie)


text1 = "JAN\n"
text2 = "NOWAK"
print(text1 + text2)

text1 = text1.rstrip()
print(text1 + text2)


#wyświetlanie łańcuchów znaków

#wszystkie wersje pythona
text = "%s, Java i %s" % ("PHP", "Python")
print(text)

#nowsze wersje
text3 = "{0}, Java i {1}".format("PHP", "Python")
print(text3)


#help(text.replace)

new = text.replace("PHP", "C#")
print(new)

#wypisanie danych

dzien = 23
miesiac = 3
rok = 2019
print("DATA: ", end="")
print(dzien, miesiac, rok)

