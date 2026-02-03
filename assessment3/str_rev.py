
def str_rev(s):
    if len(s) <= 1:
        return s 
    else:
        return str_rev(s[1:]) + s[0]
    
print(str_rev("have"))