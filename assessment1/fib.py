def fib_one(n):
    if n in {0, 1}:
        return n 
    else:
        return fib_one(n-1) + fib_one(n-2)


# def fib_one(n):
#     if n <= 1:
#         return n
#     return fib_one(n-1) + fib_one(n-2)

def fib_two(n):
    empt = []
    for i in range(n):
        empt.append(fib_one(i))
    return empt

print(fib_two(15))