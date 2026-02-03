"""
Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0) using recursion .
"""

def sum_of_series(n):
    if n <= 0:
        return 0
    
