# =========================
# Assessment 4
# =========================


# ========= BASIC =========

def count_unique_elements(items):
    """Return the number of unique elements in the list."""
    # count = 0
    # unique_items = []
    # for item in items:
    #     if item not in unique_items:
    #         count += 1
    #         unique_items.append(item)
    count = 0
    unique_items = []
    for item in set(items):
        unique_items.append(item)
    for item in unique_items:
        count += 1
    return count


def merge_dictionaries(dict1, dict2):
    """Merge two dictionaries, overriding values from the first with the second."""
    for key, value in dict2.items():
        dict1[key] = value
        # print(dict1)
    return dict1    


def format_student_report(name, marks):
    """Return a formatted report showing a student's name and average mark."""
    count = 0
    total = 0
    for item in marks:
        total += item
        count += 1
    aveg_mark = total / count
    # result = {}
    # result[name] = str(f"{(aveg_mark):.2f}")
    result = name, f"{aveg_mark:.2f}"
    
    return result
    


def compress_string(text):
    """Compress a string by counting consecutive characters."""
    dict1 = {}
    for char in text:
        if char in dict1:
            dict1[char] += 1
        else:
            dict1[char] = 1
    compressed_str = ""
    for key, value in dict1.items():
        compressed_str += key 
        compressed_str += str(value)
    return compressed_str
    
print(compress_string("aaabbc"))
        


# ======= INTERMEDIATE =======

def group_by_length(words):
    """Group words into a dictionary based on their length."""
    dict1 = {}
    for word in words:
        # if len(word) not in dict1.keys():
            # dict1.update({len(word): [x for x in words if len(x) == len(word)]})
        if len(word) in dict1:
            dict1[len(word)].append(word)
        else:
            dict1[len(word)] = [word]
        
    return dict1
    ...
  

def reverse_list_recursively(items):
    """Reverse a list using recursion."""
    if not items:
        return []
    last = items.pop()
    return [last] + reverse_list_recursively(items)


def rotate_matrix_90(matrix):
    """Rotate a square matrix 90 degrees clockwise."""
    pass


# ========= ADVANCED =========

def flatten_nested_list(nested):
    """Flatten a nested list of arbitrary depth using recursion."""
    pass


def sum_nested_numbers(nested):
    """Return the sum of all numbers in a nested list using recursion."""
    pass


def generate_pascal_row(n):
    """Return the nth row of Pascal's Triangle using recursion."""
    pass
