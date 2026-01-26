def func(n):
    # n = 3
    if n == 0:
        return f"Zero"
    elif n > 0:
        return f"Positive"
    elif n < 0:
        return f"Negative"

print(func(3))