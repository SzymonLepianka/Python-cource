import time

cennik = [1, 5, 8, 9, 10, 16, 17, 20, 24, 26]


def przytnijPret(n, cennik):
    if n <= 0:
        return 0
    maks = - 1
    for i in range(1, n + 1):
        sprz = cennik[i - 1] + przytnijPret(n - i, cennik)
        if sprz > maks:
            maks = sprz
    return maks


n = int(input("Podaj dlugosc preta n = "))
start_time = time.time()
print(przytnijPret(n, cennik))
print("time: ", (time.time() - start_time))
