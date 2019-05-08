import random

tab = []


def los(tab, n):
    for i in range(n):
        tab.append(random.randrange(1, 40))

def RadixSort (tab):
    d=1
    m=10
    czy=1
    while (czy!=0):
        czy=0
        bucket = [[],[],[],[],[],[],[],[],[],[]]
        for i in tab:
            ktory=i%m//d
            bucket[ktory].append(i)
            if(czy==0 and ktory>0):
                czy=1
        print(bucket)
        print(tab)
        tab=[]
        for j in bucket:
            for k in j:
                tab.append(k)
        m*=10
        d*=10
    print("xxx", tab)

def RadixSort2(tab):
    d = 1
    m = 10
    czy = 1
    while (czy != 0):
        czy = 0
        bucket = [[], [], [], [], [], [], [], [], [], []]
        for i in tab:
            ktory = i % m // d
            bucket[ktory].append(i)
            if (czy == 0 and ktory > 0):
                czy = 1
        print(bucket)
        print(tab)
        a=0
        b=0
        tab=[]
        for b in range(m):
            buc=bucket[b]
            for i in buc:
                tab[a]=i
                a+=1
        m *= 10
        d *= 10



def RadixSort3 (tab, n):
    d=1
    m=10
    czy=1
    while (czy!=0):
        czy=0
        bucket = [[],[],[],[],[],[],[],[],[],[]]
        for i in tab:
            ktory = i % m
            ktory /= d

            bucket[int(ktory)].append(i)
        m *= 10
        d *= 10
        if (len(bucket[0])==n):
             return bucket[0]

        tab=[]
        t_append=tab.append
        for j in bucket:
            for k in j:
                t_append(k)

def radix_sort(random_list):
    len_random_list = len(random_list)
    modulus = 10
    div = 1
    while True:
        # empty array, [[] for i in range(10)]
        new_list = [[], [], [], [], [], [], [], [], [], []]
        for value in random_list:
            least_digit = value % modulus
            least_digit /= div
            new_list[least_digit].append(value)
        modulus = modulus * 10
        div = div * 10

        if len(new_list[0]) == len_random_list:
            return new_list[0]

        random_list = []
        rd_list_append = random_list.append
        for x in new_list:
            for y in x:
                rd_list_append(y)




n = int(input("podaj dlugosc: "))
los(tab, n)
print(tab)
#print(RadixSort3(tab,n))
RadixSort2(tab)
print("x")
print(tab)
print("______________")
#radixsort(tab)
print(tab)


