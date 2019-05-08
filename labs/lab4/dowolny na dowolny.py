def dow_na_10(system_przed, liczba):
    dlugosc = len(liczba)
    suma = 0
    for i in range(dlugosc):
        if '0' <= liczba[i] <= '9':
            suma += int(liczba[i]) * pow(system_przed, dlugosc - 1 - i)
        elif liczba[i] == 'a':
            suma += 10 * pow(system_przed, dlugosc - 1 - i)
        elif liczba[i] == 'b':
            suma += 11 * pow(system_przed, dlugosc - 1 - i)
        elif liczba[i] == 'c':
            suma += 12 * pow(system_przed, dlugosc - 1 - i)
        elif liczba[i] == 'd':
            suma += 13 * pow(system_przed, dlugosc - 1 - i)
        elif liczba[i] == 'e':
            suma += 14 * pow(system_przed, dlugosc - 1 - i)
        elif liczba[i] == 'f':
            suma += 15 * pow(system_przed, dlugosc - 1 - i)
    return suma


def dzies_na_dow(system_po, suma):
    i = 1
    while (i * system_po) <= suma:
        i = i * system_po
    while suma != 0 or i >= 1:
        ile = 0
        while suma >= i:
            suma -= i
            ile += 1
        if ile == 10:
            print('a', end="")
        elif ile == 11:
            print('b', end="")
        elif ile == 12:
            print('c', end="")
        elif ile == 13:
            print('d', end="")
        elif ile == 14:
            print('e', end="")
        elif ile == 15:
            print('f', end="")
        elif 0 <= ile <= 9:
            print(ile, end="")
        else:
            print("o co chodzi")
        i /= system_po


system_przed = int(input("podaj system przed: "))
system_po = int(input("podaj system po: "))
liczba = input("podaj liczbę w systemie przed: ")
dzies_na_dow(system_po, dow_na_10(system_przed, liczba))
