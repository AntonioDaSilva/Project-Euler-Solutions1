def fact(n):
    if n==0:
        return 1
    else:
        a=1
        for i in range(0,n):
            a=a*n
            n-=1
            while(n==1):
                break
        return a
a=fact(100)
q=str(a)
sum_=0
for i in q:
    sum_+=int(i)
print (sum_)
