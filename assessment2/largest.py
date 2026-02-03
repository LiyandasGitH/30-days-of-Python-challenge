    
def numbers_(numbers):
    # numbers = [2, 25, 50, 100, 7, 1]

    largest = numbers[0]
    smallest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num 
            

print(numbers_([2, 25, 50, 100, 7, 1]))