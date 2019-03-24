#listy

programowanie = ["php", "python", "Java"]
print(programowanie)
print(type(programowanie))

programowanie.append("C#")
print(programowanie)

ile = programowanie.count("php")
print(ile)

#tuple

imiona = ("Julia", "Anna", "Sara")
print(imiona)
print(type(imiona))
print(imiona[1])


#słownik

osoba = {"imie":"Julia", "nazwisko":"Nowak", "wiek": 20}
print(osoba)
print(type(osoba))

print(osoba["imie"])

print(osoba.keys())

print(osoba.get("wzrost", "NULL"))
print(osoba.get("wiek", "NULL"))


