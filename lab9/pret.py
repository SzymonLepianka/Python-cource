cennik = [1, 5, 8, 9, 10, 16, 17, 20, 24, 26]
ciecie = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
optym = [0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]


def przytnijPret(n, cennik):
    t=[]
    if n <= 0:
        return 0
    maks = - 1
    for i in range(1, n + 1):
        if optym[n - i] > -1:
            sprz = cennik[i - 1] + optym[n - i]
        else:
            sprz = cennik[i - 1] + przytnijPret(n - i, cennik)
        if sprz > maks:
            maks = sprz
            ciecie[n+1]=i

    print("n:",n,"tab: ",t)
    optym[n] = maks
    return maks


n = int(input("Podaj dlugosc preta n = "))
print(przytnijPret(n, cennik))
print(optym)
print(ciecie)
