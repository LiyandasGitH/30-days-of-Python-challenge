"""
Write a Python program to convert an integer to a string in any base using recursion
"""

def to_string(n, base):
    convert_str = "0123456789ABCDE"

    if n < base:
        return convert_str[n]

    return to_string(n // base, base) + convert_str[n % base]

print(to_string(2, 36))






"""
Converts string to int:
"""

# def conversion(s, index):
#     if index == len(s):
#         return 0
    
#     digit = int(s[index])

#     return digit * (10 ** (len(s) - index - 1)) + conversion(s, index +1)

# def convert(s):
#     return conversion(s, 0)

# print(convert("1234"))
