import random

tab = []


def los(tab, n):
    for i in range(n):
        tab.append(random.randrange(1, 40))


def HeapSort(tab, n):
    for i in range (n // 2 - 1, -1, -1):
        MaxHeap(tab, n, i)
    for i in range(n - 1, 0, -1):
        tab[0], tab[i] = tab[i], tab[0]
        n -= 1
        MaxHeap(tab, n, 0)


def MaxHeap(tab, n, nrrodzic):
    max = nrrodzic
    lewe = nrrodzic * 2 + 1
    prawe = nrrodzic * 2 + 2
    if lewe < n and tab[lewe] > tab[max]:
        max = lewe
    if prawe < n and tab[prawe] > tab[max]:
        max = prawe
    if max != nrrodzic:
        tab[max], tab[nrrodzic] = tab[nrrodzic], tab[max]
        MaxHeap(tab, n, max)


n = int(input("podaj dlugosc: "))
los(tab, n)
print(tab)
HeapSort(tab, n)
print(tab)
