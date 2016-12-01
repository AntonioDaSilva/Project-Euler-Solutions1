"""
Here we use Eratosthenes Sieve to solve the problem. In Eratosthenes sieve our
goal is finding prime numbers lower than n. And the below techinc is called
Eratosthenes method:
1.Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
2.Initially, let p equal 2, the smallest prime number.
3.Enumerate the multiples of p by counting to n from 2p in increments of p,
and mark them in the list (these will be 2p, 3p, 4p, ... ; the p itself
should not be marked).
4.Find the first number greater than p in the list that is not marked.
If there was no such number, stop. Otherwise, let p now equal this
new number (which is the next prime), and repeat from step 3.
So here we code it using python.
sum1 variable is for adding the prime numbers one by one.
sieve list is for checking the values if they are prime or not.
(while implementing the step 3,4.)
"""
def sumPrimes(n):
    sum1, sieve = 0, [True] * n
    for p in range(2, n):
        if sieve[p]:
            sum1 += p
            for i in range(p*p, n, p):
                sieve[i] = False
    return sum1

print (sumPrimes(2000000))
