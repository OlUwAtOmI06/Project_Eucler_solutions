"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two -digit numbers is 99 * 91 = 9009 .

Find the largest palindrome made from the product of two -digit numbers."""

def ranges():
    max_val = 0

    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            prod = i * j
            if str(prod) == str(prod)[::-1]:
                max_val = max(max_val, prod)

    return max_val

print(ranges())
