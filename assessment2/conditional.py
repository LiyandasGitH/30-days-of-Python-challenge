def students_score(mark):
    if 75 <= mark <=100 :
        return("Distinction")
    elif 50 <= mark <= 74:
        return("Pass")
    elif mark <= 50:
        return("Fail")
    else:
        return("Invalid mark")

print(students_score(73))