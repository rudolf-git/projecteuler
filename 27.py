#!/bin/python
#i**2+a*i+b

import sympy
prime_count = 0

for a in range(-1000,1000):
    for b in sympy.primerange(1,1000):
        prime_seq = 0
        n = 0
        while sympy.isprime(n**2 + a*n + b):
            prime_seq += 1
            n += 1
        if prime_seq > prime_count:
            prime_count = prime_seq
            amax = a
            bmax = b


print(prime_count)
print(amax*bmax)

