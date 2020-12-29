'''
Write a Python program using Sieve of Eratosthenes method for computing primes upto a specified number.
Note: In mathematics, the sieve of Eratosthenes, (Ancient Greek: κόσκινον Ἐρατοσθένους, kóskinon Eratosthénous)
 one of a number of prime number sieves, is a simple, ancient algorithm for finding all prime numbers up to any
  given limit.
'''
from time import perf_counter
n=int(input())
start=perf_counter()
d={i:'N' for i in range(2,n+1)}
for ele in d:
    inc=0
    while (ele*(ele+inc))<=n:
        d[(ele*(ele+inc))]='Y'
        inc+=1
#print(d)
print([i for (i,v) in d.items() if d[i]=='N'])
print(perf_counter()-start)
