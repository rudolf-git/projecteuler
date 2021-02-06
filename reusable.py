#!/bin/python
#file to dump all pieces of reusable code

def is_prime(number):
    if number == 1 or number == 2:
        return True
    for i in range(3, (number//2)+1,2):
        if number % i == 0:
            return False

    return True


def sieve(n):
	isprime = [True]*n
	isprime[0] = False
	isprime[1] = False
	for i in range(2,int(n**0.5+1)):
		index = i*2
		while index < n:
			isprime[index] = False
			index = index+i
	prime = []
	for i in range(n):
		if isprime[i] == True:
			prime.append(i)
	return prime
