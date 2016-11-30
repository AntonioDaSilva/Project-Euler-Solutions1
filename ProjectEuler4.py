#Project Euler problem 4 solution
print (max( a*b for b in range(100,1000) for a in range(100,1000)  if str(a*b) == str(a*b)[::-1]))


