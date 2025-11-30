
# def is_even(n):
#     even = [2, 4, 6, 8, 10]
#     if n in even:
#         return True
#     else:
#         return False
# print(is_even(12))


# def is_even(n):
#     for x in range(0, 100, 2):
#         if n == x:
#             return True
#     return False
# print(is_even(3))

def is_even(n):
    return n % 2 == 0

print(is_even(33))