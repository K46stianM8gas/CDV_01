#!/usr/bin/python

import sys


nazwaPliku = input("Podaj nazwe pliku jaki chcesz utworzyc: ")
print(nazwaPliku)
print("\n")

plik = open(nazwaPliku, "w+")

if(plik != None):
    print("File opened successfully!")

content = input("Podaj zawartosc jaka chcesz umiescic w pliku: ")

plik.write(content)


plik.close()









