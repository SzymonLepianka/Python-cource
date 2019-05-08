import random

tab = []


def los(tab, n):
    for i in range(n):
        tab.append(random.randrange(1, 40))


def MergeSort(tab, p, k):
    if p < k:
        q = (p + k) // 2
        MergeSort(tab, p, q)
        MergeSort(tab, q + 1, k)
        Merge(tab, p, q+1, k)


def Merge(tab, p, q, k):
    L = tab[p:q]
    P = tab[q:k + 1]
    L.append(999999999)
    P.append(999999999)
    i = j = 0
    for a in range(p, k + 1):
        if L[i] <= P[j]:
            tab[a] = L[i]
            i += 1
        else:
            tab[a] = P[j]
            j += 1


n = int(input("podaj dlugosc: "))
los(tab, n)
print(tab)
print()

MergeSort (tab,0,n-1)
print(tab)
