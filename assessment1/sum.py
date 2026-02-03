def sum_of_numbers(n):
    total = 0
    for num in range(1, n + 1):
        total += num
    return total

print(sum_of_numbers(4))