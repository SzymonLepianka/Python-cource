import cmath



def getMax(tab, n):
    max = tab[0]
    for i in range(1, n):
        if tab[i] > max:
            max = tab[i]
    return max


def bucketSort(tab, n):
    bucket = 10
    vector < int > B[bucket]
    max = getMax(tab, n)
    divider = ceil(int(max + 1) / bucket)
    for i in range(n):
        j = floor(arr[i] / divider)
        B[j].push_back(arr[i])
    for i in range(bucket):
        sort(B[i].begin(), B[i].end())
    k = 0;
    for i in range(bucket):
        for j in range(B[i].size()):
            arr[k + +] = B[i][j]


tab[] = {22, 45, 12, 8, 10, 6, 72, 81, 33, 18, 50, 14}
n = sizeof(arr) / sizeof(arr[0])
print(tab)
bucketSort(tab, n)
print(tab)
