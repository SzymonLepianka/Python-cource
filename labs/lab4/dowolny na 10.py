system = int(input("system: "))
zla = 1
while zla != 0:
    liczba = input("podaj liczbę: ")
    # tab = [-1 for i in range(200)]
    dlugosc = len(liczba)
    # print("len(liczba): ", len(liczba))
    suma = 0
    zla = 0
    for i in range(dlugosc):
        if '0' <= liczba[i] <= '9':
            # print("i: ", i, "pow: ", int(liczba[i]) * pow(system, dlugosc - 1 - i), "sumaprzed: ", suma, "liczba[i]: ", liczba[i])
            suma += int(liczba[i]) * pow(system, dlugosc - 1 - i)
            # print("sumapo: ", suma)
        elif liczba[i] == 'a':
            suma += 10 * pow(system, dlugosc - 1 - i)
        elif liczba[i] == 'b':
            suma += 11 * pow(system, dlugosc - 1 - i)
        elif liczba[i] == 'c':
            suma += 12 * pow(system, dlugosc - 1 - i)
        elif liczba[i] == 'd':
            suma += 13 * pow(system, dlugosc - 1 - i)
        elif liczba[i] == 'e':
            suma += 14 * pow(system, dlugosc - 1 - i)
        elif liczba[i] == 'f':
            suma += 15 * pow(system, dlugosc - 1 - i)
        else:
            print("zła liczba")
            zla += 1
            # 3break
if zla == 0:
    print("liczba w dziesietnym: ", suma)
else:
    print("")
