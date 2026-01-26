def main():
    numbers = [1, 2, 3, 5000, 6000]
    print(find_largest(numbers))
    
def find_largest(numbers: list[int]):
    largest = numbers[0]
    for n in numbers:
        if n > largest:
            largest = n
    return largest
# print(find_largest([1, 2, 3, 5000, 6]))

if __name__ == "__main__":
    main()