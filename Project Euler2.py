#Fibonacci in Python
fib=[0,1]
z=0
i=2
while i<=100000000:
    fib.append(fib[i-2]+fib[i-1])
    i=i+1
    if max(fib) > 4000000:
        break
for i in fib:
    z+=1
m=z-1
del fib[m]
print fib
fib_notodd=[]
for i in fib:
    if i%2 == 0:
        fib_notodd.append(i)
print fib_notodd
result=0
for i in fib_notodd:
    result=result+i
print (result)
