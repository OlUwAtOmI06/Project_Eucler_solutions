"""
Sieve of Eratosthenes

prime limit= n(ln(n)+ln(ln(n)))
"""
import math
def limit(n):
    return int(n * (math.log(n) + math.log(math.log(n))))
def Sieve_of_Eratosthenes(n, target):
    primes = [True for _ in range(n+1)]
    p = 2
    prime = []

    while p * p <= n:
        if primes[p]:
            for i in range(p*p, n+1, p):
                primes[i] = False

        p += 1


    
    for i in range(2, n+1):
        if primes[i]:
            prime.append(i)

    return prime[target -1]
res = limit(10001)

print(Sieve_of_Eratosthenes(res, 10001))
