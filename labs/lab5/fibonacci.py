def fibreku(n):
    if n >= 2:
        return fibreku(n - 1) + fibreku(n - 2)
    elif n == 1:
        return 1
    else:
        return 0


def fibiter(n):
    a = 0
    b = 1
    c = 0

    for i in range(n):
        c = b
        b += a
        a = c
    return a


n = int(input("podaj n: "))
print(fibreku(n))
print(fibiter(n))
