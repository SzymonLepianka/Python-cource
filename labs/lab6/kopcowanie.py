# wybieranie szukamy max (zamieniamy na pierwsze miejsce, tak dalej, szuakmy tylko w czesci nie posrtowanej)
#   wstaienie: 2części posrotowana i nie i po jednym wstawiamy do posortowanej
#       bąbelkowe: całe przejście po tablicy, sprawdzamy zawsze dwa obok siebie do końca, za każdym razei na końcu największa
import random
import math

tab = []


def los(tab):
    for i in range(10):
        tab.append(random.randrange(1, 40))


def kublekowee(tab, i, j):
    if tab[i - 1] < tab[j - 1]:
        if (tab[floor(j / 2) - 1] < tab[j - 1]):
            swap(tab[j - 1], tab[floor(j / 2) - 1])
    else:
        if (tab[floor(i / 2) - 1] < tab[i - 1]):
            swap(tab[i - 1], tab[floor(i / 2) - 1])


def kubelkowe(tab, n, m):
    if (len(tab) % 2 != 0):
        for a in range(len(tab), 0, -2):
            kubelkowee(tab, a, a - 1)
            kubelkowe(tab, 2a, 2a + 1)

        los(tab)
        print(tab)

        print(tab)