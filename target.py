def count_occurrences(lst, target):
    count = 0
    for item in lst:
        if item == target:
            count += 1
    return count
print(count_occurrences([1, 2, 3, 2, 2, 5]), 2)