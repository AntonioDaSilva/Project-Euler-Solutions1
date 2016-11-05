def nth_prime(n):
   b=[]
   num=2
   b.append(2)
   while len(b)-1<n:
        if all(num%i!=0 for i in range(2,int((num)**0.5)+1)):
            b.append(num)
        num += 1
   print b[n]
nth_prime(10001)
