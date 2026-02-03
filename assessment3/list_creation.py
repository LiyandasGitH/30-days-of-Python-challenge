"""
Write a code to create a new list using odd-indexed elements from the first list and even-indexed elements from the second
"""

list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
res = list()

odd_e = list1[1::2] # [start:end:step]
# print(odd_e)
even_e = list2[0::2]
# print(even_e)

res.extend(odd_e)
res.extend(even_e)
print(res)