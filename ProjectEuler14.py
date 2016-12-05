import time
l,start=0,time.time()
a=[i for i in range(1,10**6,2)]
for n in a:
    q,p=1,n
    while n!=1:
        q+=1
        if n%2==0:
            n=n/2
        else:
            n=3*n+1
    if q>l:
        l,num=q,p
print (num)
end=time.time()
print(end-start)
        

