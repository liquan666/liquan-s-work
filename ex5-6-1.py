n=eval(input("请输入一个整数："))
def fact(n):
    if n in[1,2]:
        return 1
    else:
        return fact(n-1)+fact(n-2)
print(fact(n))
