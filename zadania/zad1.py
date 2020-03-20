z = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus Page1Maker"
print(z)

imie1 = "Adrian"
imie2 = "Lukasz"
nazwisko1 = "Nachtygal"
nazwisko2 = "Zawislinski"

litera_1 = imie1[1]
litera_2 = nazwisko1[2]
print(litera_1)
print(litera_2)
print("\n W tekście jest", (z.count(litera_1)), "liter, oraz", (z.count(litera_2)), "liter \n")

litera_3 = imie2[1]
litera_4 = nazwisko2[2]
print(litera_3)
print(litera_4)
print("\n W tekście jest", (z.count(litera_3)), "liter, oraz", (z.count(litera_4)), "liter \n")

zmienna_typu_string = z
print(dir(zmienna_typu_string))
help(zmienna_typu_string.zfill)

print(imie1[::-1], nazwisko1[::-1], "\n")
print(imie2[::-1], nazwisko2[::-1], "\n")

lista = []
lista1 = []
for i in range(10):
    lista.append(i+1)

lista1 = lista[5:len(lista)]
lista = lista[0:5]

print(lista)
print(lista1)

lista = lista+lista1
lista.insert(0, 0)
lista2 = lista
print(lista)
lista2.reverse()
print(lista2, "\n")

lista_krotki = []
lista_krotki.append([125847, "A"])
lista_krotki.append([124353, "W"])
lista_krotki.append([125237, "X"])
lista_krotki = tuple(lista_krotki)


print(lista_krotki, "\n")
nowa_lista = list(lista_krotki)

slownik = dict(nowa_lista)
slownik[125847] = "Lukasz Zawislinski 25 admin@admin.com 1995 Olsztyn "
slownik[124353] = "Adrian Nachtygal 2 test@test.com 1995 Warszawa "
print(slownik)
print(slownik.keys(), "\n")



telefony = []
for i in range(10):
    telefony.append(i+645214785)
    telefony.append(i+645214785)

print(telefony)

telefony = list(set(telefony))

print(telefony, "\n")

for i in range(10):
    print(i+1, end=', ')

print("\n")

for i in range(100, 15, -5):
    print(i, end=', ')


slownik_1 = dict([("asd", 1), ("dasdds", 2), ("erwer", 3), ("dsdadsad", 4)])
slownik_2 = dict([("79", 5), ("2526", 6), ("41", 7), ("974", 8)])
lista = list(slownik_1) + list(slownik_2)
pom = " ".join(map(str, lista))
print(lista)
print(pom)