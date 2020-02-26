import time
def pierwsze(max):
    t = []
    i = 0
    while(i <= max-2):
        t.append(i+2)
        i+=1
    m=0
    while(m<=max-2):
        x=t[m]
        while((t[m]+x)<=max and t[m]>0):
            t[m+x]=-1
            x+=t[m]
        m+=1
#    a=0
#    while(a<max-2):
#        if (t[a]>0):
#           print(t[a])
#        a+=1

max=int(input("max: "))
start_time = time.time()
pierwsze(max)
print("time: ", (time.time() - start_time))
