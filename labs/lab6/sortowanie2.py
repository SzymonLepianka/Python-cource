import random
import math
import time


def los(tab, n):
    for i in range(n):
        tab.append(random.randrange(1, 10000))


def SelectionSort(tab, n):
    for j in range(n):
        min = j
        for i in range(j + 1, n):
            if tab[i] < tab[min]:
                min = i
        if min != j:
            tab[min], tab[j] = tab[j], tab[min]


def InsertionSort(tab, n):
    for i in range(1, n):
        for j in range(0, i):
            if tab[i] < tab[j]:
                tab.insert(j, tab.pop(i))
                break


def BubbleSort(tab, n):
    czy = 1
    i = 0
    while czy != 0:
        czy = 0
        for j in range(n - i - 1):
            if tab[j + 1] < tab[j]:
                tab[j + 1], tab[j] = tab[j], tab[j + 1]
                czy = 1
        i += 1


def gpivot(tab, p, k):
    s = (p + k) // 2
    pivot = k
    if tab[p] < tab[s]:
        if tab[s] < tab[k]:
            pivot = s
    elif tab[p] < tab[k]:
        pivot = p
    return pivot


def Partition(tab, p, k):
    ipivot = gpivot(tab, p, k)
    vpivot = tab[ipivot]
    tab[ipivot], tab[p] = tab[p], tab[ipivot]
    storeindex = p
    for i in range(p, k + 1):
        if tab[i] < vpivot:
            storeindex += 1
            tab[storeindex], tab[i] = tab[i], tab[storeindex]
    tab[storeindex], tab[p] = tab[p], tab[storeindex]
    return storeindex


def QuickSort(tab, p, k):
    if p < k:
        r = Partition(tab, p, k)
        QuickSort(tab, p, r - 1)
        QuickSort(tab, r + 1, k)


def MergeSort(tab, p, k):
    if p < k:
        q = (p + k) // 2
        MergeSort(tab, p, q)
        MergeSort(tab, q + 1, k)
        Merge(tab, p, q + 1, k)


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


def HeapSort(tab, n):
    for i in range(n // 2 - 1, -1, -1):
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
        else:
            buckets[n - 1].append(tab[i])
    for i in range(n):
        if len(buckets[i]) > 1:
            InsertionSort(buckets[i], len(buckets[i]))
    posortowana = []
    for i in range(n):
        posortowana = posortowana + buckets[i]
    # return posortowana


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


# start_time = time.time()
# tutaj wstaw obliczenia
# print("--- %s seconds ---" % (time.time() - start_time))
tab = []
n = int(input("podaj dlugosc: "))
los(tab, n)
t1 = tab.copy()
t2 = tab.copy()
t3 = tab.copy()
t4 = tab.copy()
t5 = tab.copy()
t6 = tab.copy()
t7 = tab.copy()
t8 = tab.copy()
print(tab)
start_time = time.time()
SelectionSort(t1, n)
# print("SelectionSort: ", t1)
print( (time.time() - start_time))
start_time = time.time()
InsertionSort(t2, n)
# print("InsertionSort: ", t2)
print( (time.time() - start_time))
start_time = time.time()
BubbleSort(t3, n)
# print("BubbleSort: ", t3)
print( (time.time() - start_time))
start_time = time.time()
QuickSort(t4, 0, n - 1)
# print("QuickSort: ", t4)
print( (time.time() - start_time))
start_time = time.time()
MergeSort(t5, 0, n - 1)
# print("MergeSort: ", t5)
print( (time.time() - start_time))
start_time = time.time()
HeapSort(t6, n)
# print("HeapSort: ", t6)
print( (time.time() - start_time))
start_time = time.time()
print( BucketSort(t7, n))
print( (time.time() - start_time))
start_time = time.time()
RadixSort(t8)
# print("RadixSort: ", t8)
print( (time.time() - start_time))
