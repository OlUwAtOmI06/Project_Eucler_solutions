"""
The prime factors of 13195 are 5,7,13 and  29.

What is the largest prime factor of the number 600851475143 ?
"""


def prime_factors(nums):
    res = []
    divisor = 2
    while divisor <= nums:
        if nums % divisor == 0:
            res.append(divisor)
            nums = nums // divisor
        else:
            divisor += 1


    return res[-1]
print(prime_factors(600851475143))
