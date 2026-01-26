# def find_factorial(n):
#     if n <= 1:
#         return n
#     else:
#         return n * find_factorial(n-1)
    
# print(find_factorial(5))

def factorial(n):
    if n in {0, 1}:
        return n
    return n * factorial(n-1)

print(factorial(5))