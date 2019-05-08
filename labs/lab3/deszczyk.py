import random
import time
import os

wysokosc = int(input("wysokosc: "))
szerokosc = int(input("szerokosc: "))
tab = [-1 for i in range(wysokosc)]
random.seed()
while 1:
    losowana = random.randrange(szerokosc) + 1
    tab.insert(0, losowana)
    for i in range(0, wysokosc):
        for j in range(0, szerokosc):
            if j == szerokosc - 1:
                if (j + 1) == tab[i]:
                    print("*")
                else:
                    print("0")
            else:
                if (j + 1) == tab[i]:
                    print("*", end="")
                else:
                    print("0", end="")
    time.sleep(0.2)
    os.system('cls')
