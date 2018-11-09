def multi(*a):
    if len(a) == 0:
        return 0
    t = 1
    for i in a:
        t = t * i
    return t
print(multi(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))

