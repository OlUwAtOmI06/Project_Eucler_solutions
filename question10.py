def primes(num):
    res = [True for _ in range(num)]
    
    p = 2
    while p * p <= num:
        if res[p]:
            for i in range(p*p , num, p):
                res[i] = False
                
                
        p += 1
                
                
    prime = []
    for i in range(len(res)):
        if res[i]:
            prime.append(i)
            
    return prime[2:]
    
print(sum(primes(2000000)))
