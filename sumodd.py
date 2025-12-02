def main():

    # Prints the total of odd numbers from 1 to n
    print(sumodd(7))

def sumodd(n: int) -> int:
    '''
        Write a function that takes a number n and returns the sum of all odd numbers from 1 to n.

        Example:
        For n = 7, the sum is 1 + 3 + 5 + 7 = 16.

    '''
    empt = []
    for i in range(1, n):
        if i % 2 == 0:
            continue
        else:
            empt.append(i)
            return sum(empt)
    
    count = 0
    for i in range(1, n):
        if i % 2 == 0:
            continue
        else:
            count += i 
    return count 
    

if __name__ == "__main__":
    main()