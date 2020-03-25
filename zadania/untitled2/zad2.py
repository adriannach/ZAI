tekst = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"

print(tekst)



print ("W tekście jest ", (len(tekst)) ,"liter")

imie = "Lukasz"
nazwisko = "Zawislinski"

print ("2 litera imienia ",(imie[1]))
print ("3 litera nazwiska ",(nazwisko[2]))

print ("w tekscie jest", (tekst.index(imie[1])), "liter", imie[1])
print ("w tekscie jest", (tekst.index(nazwisko[2])), "liter", nazwisko[2])

print(dir(tekst))
help(tekst.center)

z = "Lukasz Zawislinski"
print ("Odwrocona kolejnosc:", (z [:: - 1]))


li = [1,2,3,4,5,6,7,8,9,10]
print ("lista:", (li))

