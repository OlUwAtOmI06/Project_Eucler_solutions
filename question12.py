def count_divisors(n):
    total = 1
    i = 2
    while i * i <= n:
        count = 0
        # count power of i
        while n % i == 0:
            n //= i
            count += 1
        # if i was a factor
        if count > 0:
            total *= (count + 1)
        i += 1
    # if n is still > 1 → it's prime
    if n > 1:
        total *= 2
    return total

def main():
    count = 1
    val = 1
    total = 1
    while val < 500:
        count += 1
        total += count
        val = count_divisors(total)

    return total


print(main())  
