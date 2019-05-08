import random

tab = []


def los(tab, n):
    for i in range(n):
        tab.append(random.randrange(1, 40))

def gpivot (tab,p,k):
    s=(p+k)//2
    pivot=k
    if tab[p]<tab[s] :
        if tab[s]<tab[k]:
            pivot=s
    elif tab[p]<tab[k]:
        pivot = p
    return pivot

def Partition(tab, p, k):

    ipivot=gpivot(tab,p,k)
    vpivot=tab[ipivot]
    tab[ipivot],tab[p]=tab[p],tab[ipivot]
    storeindex = p
    for i in range(p, k + 1):
        #print(".")
        if tab[i] < vpivot:
            #print("(", p, ",", k, ") zamieniam ", tab[storeindex], " z ", tab[i], ":")
            storeindex += 1
            tab[storeindex], tab[i] = tab[i], tab[storeindex]

            #print(tab)
    #print("ZANIENIAm ", tab[storeindex - 1], " z ", tab[p])
    tab[storeindex], tab[p] = tab[p], tab[storeindex]
    return storeindex


def QuickSort(tab, p, k):
    if p < k:
        r = Partition(tab, p, k)
        #print(tab)
        QuickSort(tab, p, r - 1)
        QuickSort(tab, r + 1, k)


n = int(input("podaj dlugosc: "))
los(tab, n)
print(tab)
# Partition (tab,0,n)
# print(tab)
print()
QuickSort(tab, 0, n-1)
print(tab)
