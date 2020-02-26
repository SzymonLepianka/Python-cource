import math
import random

tab = []


def los(tab, n):
    for i in range(n):
        tab.append(random.randrange(1, 40))


def counting(tab, exp1):
    n = len(tab)
    output = [0] * (n)
    count = [0] * (10)
    for i in range(0, n):
        index = math.floor((tab[i] / exp1))
        count[(index) % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        index = (tab[i] / exp1)
        output[count[math.floor((index) % 10)] - 1] = tab[i]
        count[math.floor((index) % 10)] -= 1
        i -= 1
    for i in range(0, len(tab)):
        tab[i] = output[i]


def RadixSort(tab):
    max = tab[0]
    for i in range(1, n):
        if tab[i] > max:
            max = tab[i]
    exp = 1
    while max / exp > 1:
        counting(tab, exp)
        exp *= 10


n = int(input("podaj dlugosc: "))
los(tab, n)
print(tab)
RadixSort(tab)
print(tab)
