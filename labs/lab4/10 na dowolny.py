system = int(input("podaj system: "))
liczba = int(input("podaj liczbę w dziesietnym: "))
i = 1
while (i * system) <= liczba:
    i = i * system
# print("i = ", i)
while liczba != 0 or i >= 1:
    ile = 0
    while liczba >= i:
        liczba -= i
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
    i /= system
