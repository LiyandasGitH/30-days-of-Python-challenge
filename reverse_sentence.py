"""
Write a function that returns the reverse of a string,
Sentence should be in reverse order, not the words themselves 
"""

def reverse_words(sentence: str):
    words = sentence.split()
    return " ".join(words[::-1])
print(reverse_words("This is cool"))


# def reverse_words_no_slice(sentence: str):
#     words = sentence.split()
#     reversed_words = []

#     for i in range(len(words) - 1, -1, -1):
#         reversed_words.append(words[i])

#     return " ".join(reversed_words)

# print(reverse_words_no_slice("This is cool"))



# def reverse_words_clean(sentence: str):
#     words = sentence.split()
#     return " ".join(reversed(words))

# print(reverse_words_clean("This is cool"))




# def reverse_each_word(sentence: str):
#     words = sentence.split()
#     reversed_words = [word[::-1] for word in words]
#     return " ".join(reversed_words)

# print(reverse_each_word("This is so cool"))