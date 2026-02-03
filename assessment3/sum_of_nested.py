"""
Write a Python program to sum recursion lists using recursion.
"""

def sum_of_nested(data):
    total = 0
    for element in data:
        if isinstance(element, list):
            total += sum_of_nested(element)
        else:
            total += element
    return total

print(sum_of_nested( [1, 2, [3,4], [5,6]]))