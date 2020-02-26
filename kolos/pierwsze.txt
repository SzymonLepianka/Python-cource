def pierwsze(max):
    t = []
    for i in range(0, max-1):
        t.append(i+2)
    for m in range(0, max-1):
        x = t[m]
        while (t[m] + x) <= max and t[m] > 0:
            t[m + x] = -1
            x += t[m]
    for a in range(0, max-1):
        if t[a] > 0:
            print(t[a])

max = int(input("max: "))
pierwsze(max)
