import random
import time
import os
#wysokosc=int(input("wysokosc: "))
szerokosc=int(input("szerokosc: "))
#tab = [-1 for i in range(wysokosc)]
random.seed()
while(1):
    losowana = random.randrange(szerokosc)+1
    print(losowana)
    time.sleep(0.3)
    os.system('cls')

