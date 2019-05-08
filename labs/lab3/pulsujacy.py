import time
import os

while 1:
    wysokosc = int(input("wysokosc: "))
    szerokosc = int(input("szerokosc: "))
    if wysokosc % 2 != 0 and szerokosc % 2 != 0:
        break
min = min(wysokosc, szerokosc)
rmax = (min - 1) / 2
xs = (szerokosc + 1) / 2
ys = (wysokosc + 1) / 2
r = 0
k = 0
while 1:
    for i in range(0, wysokosc):
        for j in range(0, szerokosc):
            if j == szerokosc - 1:
                if r == (max(abs(xs - (j + 1)), abs(ys - (i + 1)))):
                    print("*")
                else:
                    print("0")
            else:
                if r == (max(abs(xs - (j + 1)), abs(ys - (i + 1)))):
                    print("*", end="")
                else:
                    print("0", end="")
    if r == rmax:
        k = 1
    if r != rmax and k == 0:
        r += 1
    if r == 0:
        k = 0
        r += 1
    if r != 0 and k == 1:
        r -= 1
    time.sleep(0.2)
    os.system('cls')
