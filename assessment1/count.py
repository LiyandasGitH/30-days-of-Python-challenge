# def main():
#     print(countoccurrences("hello"))
    
# def countoccurrences(string) -> dict:
#     count = 0
#     temp = {}
#     for item in string:
#         if item == string:
#             count += 1
#         return count




# if __name__ == "__main__":
#     main()
    
    

def countoccurrences(string:str) -> dict:
    string_ = list(string.strip().strip(' ').lower())
    empt_dict = {}
    for char in string_:
        if char in empt_dict:
            continue
        empt_dict[char] = string.count(char)
        
    return empt_dict
print(countoccurrences("hello"))
