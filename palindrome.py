def main():
    print(is_palindrome("hello"))
    print(is_palindrome("racecar"))
    
def is_palindrome(string) -> bool:
    return string == string[::-1]

if __name__ == "__main__":
    main()


# def is_palindrome(string:str) -> bool:
#     left, right = 0, len(string) - 1
    
#     while left < right:
#         if string[left] != string[right]:
#             return False
#         left += 1
#         right -= 1
#     return True
