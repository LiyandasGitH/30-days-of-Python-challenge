def calculate_average(numbers):
    # numbers = [1, 2, 3, 4, 5, 6, 7]
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

print(calculate_average([1, 2, 3, 4, 5, 6, 7]))