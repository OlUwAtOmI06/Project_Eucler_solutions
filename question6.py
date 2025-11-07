"""
The sum of the squares of the first ten natural numbers is 385,


The square of the sum of the first ten natural numbers is 3025,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .


square sum = [n (n+1)(2n + 1)] // 6
"""
def squ_sum(n):
    return n * (n + 1) * (2 * n + 1) // 6
def sum_t(n):
    res = n * (n + 1) // 2
    return res **2

first = squ_sum(100)
second = sum_t(100) 

print(first)
print(second)
res = second - first
print(res)
