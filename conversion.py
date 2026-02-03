"""
Write a Python program to convert an integer to a string in any base using recursion
"""

def conversion(s, index):

    if index == len(s):
        return 0
    
    digit = int(s[index])

    return digit * (10 ** (len(s) - index - 1)) + conversion(s, index +1)

def convert(s):
    return conversion(s, 0)

print(convert("1234"))

# def conversion(s, accumulator=0):
#     if not s:
#         return accumulator
#     return conversion(s[1:], accumulator + ord(s[0]) - 48)
# #     else:
# #         first_dig_value = ord(s[0] - 48)

# #         new_accum = 10 * accumulator + first_dig_value

# #         return conversion(s[1:], new_accum)
    
# # num_s = "1234"
# # int_result = conversion(num_s)

# print(conversion("11"))