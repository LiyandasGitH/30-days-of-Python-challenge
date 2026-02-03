"""
Write a Python program to solve the Fibonacci sequence using recursion.
"""

def fib(n):
    if n in [1,2]: # base case
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(7))

# def fib_two(n):
#     lis_ = []
#     for i in range(n):
#         lis_.append(fib(i))
#     return lis_ 

# print(fib_two(7))