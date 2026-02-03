""""
Write a Python program to get the sum of a non-negative integer using recursion.
"""

def sum_of_digits(n):
    if n <= 0:
        return 0
    return (n % 10) + sum_of_digits(int(n // 10))
    # return 0 if n <= 0 else n + sum_of_digits(n-1)
    # if len(n) == 1:
    #     return n[0]
    # return n[0] + sum_of_digits(n[1:])

print(sum_of_digits(1234567))