"""

 2520 is the smallest number that can be divided by each of the numbers from  1 to  10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from  1 to 20 ?
"""

def find_hcf(a,b):
    while b != 0:
        a, b = b, a%b
    return a


def find_lcm(a,b):
    return abs(a * b) // find_hcf(a, b)

lcm = 1
for i in range(1, 21):
    lcm = find_lcm(lcm, i)

print(lcm)
