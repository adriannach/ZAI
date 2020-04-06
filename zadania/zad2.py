#1
def funkcja(a_lista, b_lista):
    c_lista = a_lista
    for index, value in enumerate(a_lista):
        if index % 2 == 0:
            c_lista[index] = a_lista[index]
        if index % 2 != 0:
            c_lista[index] = b_lista[index]
    return c_lista


list1 = [a, a, a, a, a, a, a, a, a, a]
list2 = [b, b, b, b, b, b, b, b, b, b]
print(funkcja(list1, list2))

#2
