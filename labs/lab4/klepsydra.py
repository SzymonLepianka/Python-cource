#wejściowka
n = int(input("n: "))
m = n
puste = 0
pustep = 0
for i in range(n):
    for j in range(m + puste):
        if j == m + puste - 1:
#            if pustep < puste:
#                print(" ")
#                if i < (n + 1) / 2:
#                    pustep = 0
#                    puste += 1
#                    m -= 2
#                else:
#                    pustep = 0
#                    puste -= 1
#                    m += 2
#            else:
            print("x")
            if i + 1 < (n + 1) / 2:
                pustep = 0
                puste += 1
                m -= 2
            else:
                pustep = 0
                puste -= 1
                m += 2
        else:
            if pustep < puste:
                print(" ", end="")
                pustep += 1
            else:
                print("x", end="")
