def fib(n):
    a,b=1,1
    for i in range(n-1):
        a,b=b,a+b
    return a
n=20
while True:
    a=fib(n)
    q=str(a)
    if len(q) == 1000:
        break
    n+=1
print (n)
