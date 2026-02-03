# def count_char(word:str, letter:str) -> int:
#     if letter == "":
#         return 0
#     if word[0] == letter:
#         return 1 + count_char(word[1:], letter)
#     else:
#         return 0 + count_char(word[1:], letter)
    
# print(count_char("apple", "p"))

# def count_char(s):
#     count = 0
#     letters = ''
#     letters_found = []
#     for char in s.lower():
#         if char in letters:
#             count += 1
#             letters_found.append(char)
#         return letters_found, count

# print(count_char("apple"))

def count_char(s):
    string = list(s)
    # print(string)
    count = [x for x in string if x == "p"]
    return len(count)
print(count_char("apple"))