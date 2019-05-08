import math
import time

n = int(input("MAX = "))
time1 = time.time()
z = [True for x in range(n + 1)]
for p in range(2, int(math.sqrt(n)) + 1):
    if z[p]:
        x = 2 * p
        while x <= n:
            z[x] = False
            x = x + p
print(time.time() - time1)