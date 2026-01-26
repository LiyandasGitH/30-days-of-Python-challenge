def count_vowels(s):
    count = 0
    vowels = "aeiou"
    vowels_found = []
    for char in s.lower():
        if char in vowels:
            count += 1
            vowels_found.append(char)
    return vowels_found, count
        
print(count_vowels("lowercase"))
        
    