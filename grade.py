def grade(score):
    if 90 <= score <= 100:
        return f"A"
    elif 80 <= score <= 89:
        return f"B"
    elif 70 <= score <= 79:
        return f"C"
    elif 60 <= score <= 69:
        return f"D"
    else:
        return f"F"

print(grade(89))