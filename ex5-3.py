def isNum(s):
    try:
        n = eval(s)
    except:
        return False
    return True

s = input("Enter a string:")
if isNum(s):
    print("{} is a number".format(s))
else:
    print("{} is not a number".format(s))

        
