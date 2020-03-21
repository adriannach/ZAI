#1
def funkcja(a_list = [2,1,3,4,5,6],b_list = [9,8,7,6,5,4]):
    for p in a_list:
        if (p % 2==0):
            parzyste = [p]
            print (parzyste)
    for q in b_list:
        if (q % 2 == 1):
            nieparzyste = [q]
            print (nieparzyste)
    return()

funkcja()

#2
