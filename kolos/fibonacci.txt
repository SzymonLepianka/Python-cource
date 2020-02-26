tab = [0, 1, 1]


def fib_rekur_dyn(n):
    if len(tab) > n:
        return tab[n]
    else:
        x = fib_rekur_dyn(n - 1) + fib_rekur_dyn(n - 2)
        tab.append(x)
        return x

def fib_rekur(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return fib_rekur(n-1)+fib_rekur(n-2)

def fib_iter(n):
    a = 0
    b = 1
    if n == 0:
        return a
    if n == 1 or n == 2:
        return b
    else:
        for i in range(1, n):
            c = b
            b += a
            a = c
        return b


n = int(input("podaj n: "))
print(fib_rekur_dyn(n))
print(fib_rekur(n))
print(fib_iter(n))

