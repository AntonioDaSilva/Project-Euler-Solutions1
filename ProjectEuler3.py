def p(n):
    f = []
    d = 2
    while n > 1:
        while n % d == 0:
            f.append(d)
            n /= d
        d = d + 1

    return f


z = p(600851475143)
m = max(z)
print m
