import time

def primeNumbers(max):
    tab = []
    for i in range(2, max + 1):
        tab.append(i)
    for i in range(0, max - 1):
        value = tab[i]
        while(tab[i] != -1 and (value + tab[i]) <= max):
            tab[i + value] = -1
            value += tab[i]
    #for i in range (0, max - 1):
    #    if(tab[i] != -1):
    #       print(tab[i])


max=int(input("max: "))
start_time = time.time()
primeNumbers(max)
print("--- %s seconds ---" % (time.time() - start_time))
