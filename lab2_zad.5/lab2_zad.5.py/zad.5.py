
max=1000000
i=1
while(i<=max):
    j=1
    k=0
    while(j<=i):
        if(i%j==0):
            k+=1
        j+=1
    if(k==2):
       print(i)
    i+=1
