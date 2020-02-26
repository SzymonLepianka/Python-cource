def pascal(a, b):
    if (a == 1 or b == 1 or a == b):
        return 1
    else:
        return pascal(a - 1, b) + pascal(a - 1, b - 1)


n = int(input("podaj n: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(pascal(i, j), end=" ")
    print()
