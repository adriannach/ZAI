#1
def funkcja(a_list, b_list):
    c_list = a_list
    for index, value in enumerate(a_list):
        if index % 2 == 0:
            c_list[index] = a_list[index]
        if index % 2 != 0:
            c_list[index] = b_list[index]
    return c_list


list1 = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
list2 = ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']
print(funkcja(list1, list2))

#3
def deleteLetters(text, letter):
    text = text.replace(letter, "")
    return text

letter = input('Podaj znak: ')
letter = str(letter)
text = "testowy tekst"
print(deleteLetters(text, letter))

#5
class Calculator:
    def add(self):
        return 'add'

    def difference(self):
        return 'difference'

    def multiply(self):
        return 'multiply'

    def divide(self):
        return 'divide'

calculator = Calculator()
print(calculator.add())
print(calculator.difference())
print(calculator.multiply())
print(calculator.divide())
