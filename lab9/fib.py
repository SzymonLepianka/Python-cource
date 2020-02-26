pamiec=[0,1]
def fib(n):
    if n < len(pamiec):
        return pamiec[n]
    else:
        x=fib(n-1)+fib(n-2)
        pamiec.append(x)
        return x
n=int(input("podaj n: "))
print (fib(n))
