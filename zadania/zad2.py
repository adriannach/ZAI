#1
list1 = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
list2 = ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']

def funkcja(a_list, b_list):
    c_list = a_list
    for index, value in enumerate(a_list):
        if index % 2 == 0:
            c_list[index] = a_list[index]
        if index % 2 != 0:
            c_list[index] = b_list[index]
    return c_list

print(funkcja(list1, list2))

#2

tekst = "lorembladlalvk jdajsna dajdasd"


def funkcja_analizujaca_tekst(data_text):
    lista_liter_tekstu = []

    slownik = {'length': len(data_text), 'letters': lista_liter_tekstu, 'big_letters': 'tekst_WIELIKI',
               'small_letters': 'tekst_malymi'}

    for i in data_text:
        lista_liter_tekstu.append(i)

    slownik['letters'] = lista_liter_tekstu

    slownik['big_letters'] = data_text.upper()

    slownik['small_letters'] = data_text.lower()

    return slownik


print(funkcja_analizujaca_tekst(tekst))

#3
def deleteLetters(text, letter):
    text = text.replace(letter, "")
    return text

letter = input('Podaj znak: ')
letter = str(letter)
text = "testowy tekst"
print(deleteLetters(text, letter))

#4
def temperature(temperature_type, temperatura):
    if temperatura < -273.15:
        'Blad'
        return
    elif temperatura >= -275.15:
        if temperature_type == 'F':
            return (temperatura * 1.8) + 32
        elif temperature_type == 'R':  # Fahrenheit, Rankine, Kelvin
            return (temperatura + 273.15) * 1.8
        elif temperature_type == 'K':
            return temperatura + 273.15
        else:
            return 'Zla jednostka'
    else:
        return "Error 404"


print(temperature('K', 100))


#5
class Calculator:

    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2

    def add(self):
        return self.l1 + self.l2

    def difference(self):
        return self.l1 - self.l2

    def multiply(self):
        return self.l1 * self.l2

    def divide(self):
        return self.l1 / self.l2

calculator = Calculator(8, 2)
print(calculator.add())
print(calculator.difference())
print(calculator.multiply())
print(calculator.divide())

#6
class ScienceCalculator(Calculator):
    def potegowanie(self):
        return self.l1 ^ self.l2

    def reszta_z_dzielenia(self):
        return self.l1 % self.l2

    def devide(self):
        pass


kalkulator = ScienceCalculator(5, 3)
print(kalkulator.add())
print(kalkulator.difference())
print(kalkulator.multiply())
print(kalkulator.devide())
print(kalkulator.potegowanie())
print(kalkulator.reszta_z_dzielenia())


#7
def funkcja2(x):
    return x[::-1]

x = input('Podaj tekst: ')
x = str(x)
print(funkcja2(x))


