import random

tab = []


def los(tab, n):
    for i in range(n):
        tab.append(random.randrange(1, 40))


def BucketSort(tab, n):
    max = tab[0]
    for i in range(1, n):
        if tab[i] > max:
            max = tab[i]
    size = max / n
    buckets = [[] for _ in range(n)]
    for i in range(n):
        j = int(tab[i] / size)
        if j != n:
            buckets[j].append(tab[i])
            # print("buckets[j]: ", buckets)
        else:
            buckets[n - 1].append(tab[i])
            # print("buckets[n-1]: ", buckets)
    for i in range(n):
        InsertionSort(buckets[i], len(buckets[i]))
    posortowana = []
    for i in range(n):
        posortowana = posortowana + buckets[i]
    return posortowana


def InsertionSort(tab, n):
    for i in range(1, n):
        for j in range(0, i):
            if tab[i] < tab[j]:
                tab.insert(j, tab.pop(i))
                break


n = int(input("podaj dlugosc: "))
los(tab, n)
print(tab)
print(BucketSort(tab, n))
